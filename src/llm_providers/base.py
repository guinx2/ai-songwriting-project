"""
LLM Provider 추상 기본 클래스

모든 LLM Provider (Claude, EXAONE, GPT-4 등)가 구현해야 할 
공통 인터페이스와 유틸리티 메서드를 정의합니다.
"""

import json
import logging
import hashlib
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from datetime import datetime

from ..data_models.music_params import MusicParams, GenerationRequest, GenerationResult


@dataclass
class ProviderConfig:
    """LLM Provider 설정"""
    api_key: str
    model_name: str
    temperature: float = 0.7
    max_tokens: int = 2000
    timeout: int = 30
    retry_attempts: int = 3
    retry_delay: float = 1.0


@dataclass
class PromptTemplate:
    """프롬프트 템플릿"""
    system_prompt: str
    user_prompt_format: str
    examples: List[Dict[str, str]]


class LLMProviderError(Exception):
    """LLM Provider 관련 에러"""
    pass


class APIError(LLMProviderError):
    """API 호출 에러"""
    pass


class ParseError(LLMProviderError):
    """응답 파싱 에러"""
    pass


class LLMProvider(ABC):
    """
    LLM Provider 추상 기본 클래스
    
    모든 구체적인 LLM Provider (Claude, EXAONE, GPT-4)가 상속받아야 하는 클래스입니다.
    공통 기능과 인터페이스를 정의합니다.
    """
    
    def __init__(self, config: ProviderConfig):
        """
        LLM Provider 초기화
        
        Args:
            config: Provider 설정 정보
        """
        self.config = config
        self.logger = self._setup_logger()
        self.prompt_template = self._get_prompt_template()
        
    def _setup_logger(self) -> logging.Logger:
        """로거 설정"""
        logger = logging.getLogger(f"{self.__class__.__name__}")
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        return logger
    
    @abstractmethod
    def _get_prompt_template(self) -> PromptTemplate:
        """
        Provider별 프롬프트 템플릿 반환
        
        Returns:
            PromptTemplate: 해당 Provider에 최적화된 프롬프트 템플릿
        """
        pass
    
    @abstractmethod
    async def _make_api_call(self, prompt: str) -> Dict[str, Any]:
        """
        실제 API 호출 (Provider별 구현 필요)
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            Dict[str, Any]: API 응답 데이터
            
        Raises:
            APIError: API 호출 실패 시
        """
        pass
    
    def create_prompt(self, user_input: str) -> str:
        """
        사용자 입력을 LLM용 프롬프트로 변환
        
        Args:
            user_input: 사용자의 자연어 입력
            
        Returns:
            str: 완성된 프롬프트
        """
        return self.prompt_template.user_prompt_format.format(
            user_input=user_input,
            examples=self._format_examples()
        )
    
    def _format_examples(self) -> str:
        """예시들을 문자열로 포맷팅"""
        formatted_examples = []
        for i, example in enumerate(self.prompt_template.examples, 1):
            formatted_examples.append(
                f"예시 {i}:\n입력: {example['input']}\n출력: {example['output']}"
            )
        return "\n\n".join(formatted_examples)
    
    def parse_response(self, response_data: Dict[str, Any]) -> MusicParams:
        """
        API 응답을 MusicParams 객체로 파싱
        
        Args:
            response_data: API 응답 데이터
            
        Returns:
            MusicParams: 파싱된 음악 파라미터
            
        Raises:
            ParseError: 파싱 실패 시
        """
        try:
            # Provider별로 응답 형식이 다를 수 있으므로 구체 클래스에서 오버라이드 가능
            content = self._extract_content(response_data)
            
            # JSON 형태의 응답에서 MusicParams 추출
            if content.strip().startswith('{'):
                params_dict = json.loads(content.strip())
                return MusicParams(**params_dict)
            else:
                # JSON이 아닌 경우 별도 파싱 로직 적용
                return self._parse_text_response(content)
                
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            self.logger.error(f"응답 파싱 실패: {e}")
            self.logger.error(f"응답 내용: {response_data}")
            raise ParseError(f"응답 파싱 실패: {e}")
    
    @abstractmethod
    def _extract_content(self, response_data: Dict[str, Any]) -> str:
        """
        API 응답에서 실제 내용 추출 (Provider별 구현 필요)
        
        Args:
            response_data: API 응답 데이터
            
        Returns:
            str: 추출된 내용
        """
        pass
    
    def _parse_text_response(self, content: str) -> MusicParams:
        """
        텍스트 형태의 응답을 MusicParams로 파싱
        (기본 구현, 필요 시 오버라이드)
        
        Args:
            content: 텍스트 응답 내용
            
        Returns:
            MusicParams: 파싱된 음악 파라미터
        """
        # 기본적으로는 JSON 추출 시도
        # 구체 Provider에서 더 정교한 파싱 로직 구현 가능
        lines = content.strip().split('\n')
        for line in lines:
            if line.strip().startswith('{'):
                try:
                    params_dict = json.loads(line.strip())
                    return MusicParams(**params_dict)
                except (json.JSONDecodeError, ValueError):
                    continue
        
        raise ParseError("텍스트에서 유효한 JSON을 찾을 수 없습니다")
    
    async def analyze_prompt(self, user_input: str) -> MusicParams:
        """
        자연어 프롬프트를 분석하여 MusicParams로 변환
        
        Args:
            user_input: 사용자의 자연어 입력
            
        Returns:
            MusicParams: 분석된 음악 파라미터
            
        Raises:
            LLMProviderError: 분석 실패 시
        """
        try:
            self.logger.info(f"프롬프트 분석 시작: {user_input[:100]}...")
            
            # 프롬프트 생성
            prompt = self.create_prompt(user_input)
            
            # API 호출 (재시도 로직 포함)
            response_data = await self._make_api_call_with_retry(prompt)
            
            # 응답 파싱
            music_params = self.parse_response(response_data)
            
            self.logger.info(f"프롬프트 분석 완료: {music_params.get_summary()}")
            return music_params
            
        except Exception as e:
            self.logger.error(f"프롬프트 분석 실패: {e}")
            raise LLMProviderError(f"프롬프트 분석 실패: {e}")
    
    async def _make_api_call_with_retry(self, prompt: str) -> Dict[str, Any]:
        """
        재시도 로직이 포함된 API 호출
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            Dict[str, Any]: API 응답 데이터
        """
        last_error = None
        
        for attempt in range(self.config.retry_attempts):
            try:
                self.logger.debug(f"API 호출 시도 {attempt + 1}/{self.config.retry_attempts}")
                return await self._make_api_call(prompt)
                
            except APIError as e:
                last_error = e
                self.logger.warning(f"API 호출 실패 (시도 {attempt + 1}): {e}")
                
                if attempt < self.config.retry_attempts - 1:
                    import asyncio
                    await asyncio.sleep(self.config.retry_delay * (2 ** attempt))
                    
        raise APIError(f"모든 재시도 실패: {last_error}")
    
    def generate_prompt_hash(self, user_input: str) -> str:
        """
        프롬프트의 해시값 생성 (캐싱용)
        
        Args:
            user_input: 사용자 입력
            
        Returns:
            str: SHA-256 해시값
        """
        content = f"{self.__class__.__name__}:{user_input}:{self.config.model_name}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def estimate_cost(self, prompt: str) -> float:
        """
        API 호출 비용 추정
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            float: 추정 비용 (USD)
        """
        # 기본 구현: 토큰 수 기반 추정
        # 구체 Provider에서 더 정확한 비용 계산 구현 가능
        estimated_tokens = len(prompt.split()) * 1.3  # 대략적인 토큰 수 추정
        
        # Provider별 토큰당 비용 (기본값, 실제로는 오버라이드 필요)
        cost_per_token = 0.00001
        
        return estimated_tokens * cost_per_token
    
    async def generate_title_suggestion(self, params: MusicParams) -> str:
        """
        음악 파라미터 기반 곡 제목 생성
        
        Args:
            params: 음악 파라미터
            
        Returns:
            str: 제안된 곡 제목
        """
        # 곡 제목 생성용 프롬프트 (기본 구현)
        title_prompt = f"""
다음 음악 파라미터를 바탕으로 적절한 곡 제목을 제안해주세요:

장르: {params.to_genre_path()}
악기: {params.instrument.value}
분위기: {params.mood}
템포: {params.tempo}BPM
아티스트 참조: {params.artist_reference or 'None'}

1개의 창의적인 곡 제목만 반환해주세요.
"""
        
        try:
            response_data = await self._make_api_call(title_prompt)
            content = self._extract_content(response_data)
            return content.strip().strip('"').strip("'")
        except Exception as e:
            self.logger.warning(f"곡 제목 생성 실패: {e}")
            # 폴백: 파라미터 기반 자동 제목 생성
            return self._generate_fallback_title(params)
    
    def _generate_fallback_title(self, params: MusicParams) -> str:
        """
        폴백 곡 제목 생성
        
        Args:
            params: 음악 파라미터
            
        Returns:
            str: 생성된 곡 제목
        """
        components = [params.mood, params.style_variant, params.song_part.value]
        return ' '.join(word.title() for word in components)
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        모델 정보 반환
        
        Returns:
            Dict[str, Any]: 모델 정보
        """
        return {
            "provider": self.__class__.__name__,
            "model_name": self.config.model_name,
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
            "timeout": self.config.timeout,
            "config": {
                "api_key": "***" if self.config.api_key else None,
                "model_name": self.config.model_name,
                "temperature": self.config.temperature,
                "max_tokens": self.config.max_tokens,
                "timeout": self.config.timeout,
                "retry_attempts": self.config.retry_attempts,
                "retry_delay": self.config.retry_delay
            },
            "supported_features": [
                "analyze_prompt",
                "create_prompt", 
                "parse_response",
                "estimate_cost",
                "prompt_hash_generation"
            ],
            "api_version": "1.0"
        } 