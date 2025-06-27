"""
LLM Provider Factory

설정에 따라 적절한 LLM Provider 인스턴스를 생성하고 관리하는 팩토리 클래스입니다.
다양한 Provider 간의 전환과 로드 밸런싱을 지원합니다.
"""

from typing import Dict, Type, Optional, List, Union
from enum import Enum
import logging

from .base import LLMProvider, ProviderConfig
from .claude_provider import ClaudeProvider
from .openai_provider import OpenAIProvider
from .exaone_provider import ExaoneProvider
from ..config.settings import Settings


class ProviderType(str, Enum):
    """지원하는 LLM Provider 타입"""
    CLAUDE = "claude"
    OPENAI = "openai"
    EXAONE = "exaone"


class LLMProviderFactory:
    """
    LLM Provider 팩토리 클래스
    
    설정에 따라 적절한 LLM Provider를 생성하고 관리합니다.
    여러 Provider 간의 로드 밸런싱과 폴백 기능을 제공합니다.
    """
    
    def __init__(self, settings: Settings):
        """
        팩토리 초기화
        
        Args:
            settings: 애플리케이션 설정
        """
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        
        # Provider 클래스 매핑
        self._provider_classes: Dict[ProviderType, Type[LLMProvider]] = {
            ProviderType.CLAUDE: ClaudeProvider,
            ProviderType.OPENAI: OpenAIProvider,
            ProviderType.EXAONE: ExaoneProvider
        }
        
        # 인스턴스 캐시
        self._provider_cache: Dict[ProviderType, LLMProvider] = {}
        
        self.logger.info("LLM Provider Factory 초기화 완료")
    
    def get_provider(
        self, 
        provider_type: Union[ProviderType, str],
        force_new: bool = False
    ) -> LLMProvider:
        """
        지정된 타입의 Provider 인스턴스 반환
        
        Args:
            provider_type: Provider 타입
            force_new: 새 인스턴스 강제 생성 여부
            
        Returns:
            LLMProvider: Provider 인스턴스
            
        Raises:
            ValueError: 지원하지 않는 Provider 타입
            RuntimeError: Provider 생성 실패
        """
        # 문자열을 ProviderType으로 변환
        if isinstance(provider_type, str):
            try:
                provider_type = ProviderType(provider_type.lower())
            except ValueError:
                raise ValueError(f"지원하지 않는 Provider 타입: {provider_type}")
        
        # 캐시된 인스턴스 반환 (force_new가 False인 경우)
        if not force_new and provider_type in self._provider_cache:
            return self._provider_cache[provider_type]
        
        # 새 인스턴스 생성
        provider_instance = self._create_provider(provider_type)
        
        # 캐시에 저장
        self._provider_cache[provider_type] = provider_instance
        
        return provider_instance
    
    def _create_provider(self, provider_type: ProviderType) -> LLMProvider:
        """
        Provider 인스턴스 생성
        
        Args:
            provider_type: Provider 타입
            
        Returns:
            LLMProvider: 생성된 Provider 인스턴스
            
        Raises:
            ValueError: 지원하지 않는 Provider 타입
            RuntimeError: Provider 생성 실패
        """
        if provider_type not in self._provider_classes:
            raise ValueError(f"지원하지 않는 Provider 타입: {provider_type}")
        
        try:
            # Provider별 설정 생성
            config = self._create_provider_config(provider_type)
            
            # Provider 클래스 가져오기
            provider_class = self._provider_classes[provider_type]
            
            # 인스턴스 생성
            provider_instance = provider_class(config)
            
            self.logger.info(f"{provider_type.value} Provider 인스턴스 생성 완료")
            
            return provider_instance
            
        except Exception as e:
            error_msg = f"{provider_type.value} Provider 생성 실패: {e}"
            self.logger.error(error_msg)
            raise RuntimeError(error_msg)
    
    def _create_provider_config(self, provider_type: ProviderType) -> ProviderConfig:
        """
        Provider별 설정 생성
        
        Args:
            provider_type: Provider 타입
            
        Returns:
            ProviderConfig: Provider 설정
            
        Raises:
            ValueError: API 키가 설정되지 않은 경우
        """
        llm_settings = self.settings.llm_provider
        
        # Provider별 API 키 매핑
        api_key_mapping = {
            ProviderType.CLAUDE: llm_settings.anthropic_api_key,
            ProviderType.OPENAI: llm_settings.openai_api_key,
            ProviderType.EXAONE: llm_settings.exaone_api_key
        }
        
        # Provider별 기본 모델 매핑
        default_model_mapping = {
            ProviderType.CLAUDE: "claude-4-sonnet",
            ProviderType.OPENAI: "gpt-4-turbo",
            ProviderType.EXAONE: "exaone-3.5-turbo"
        }
        
        # API 키 확인
        api_key = api_key_mapping.get(provider_type)
        if not api_key:
            raise ValueError(f"{provider_type.value} API 키가 설정되지 않았습니다")
        
        # 기본 모델명 설정
        model_name = default_model_mapping.get(provider_type)
        
        # ProviderConfig 생성
        return ProviderConfig(
            api_key=api_key,
            model_name=model_name,
            temperature=llm_settings.temperature,
            max_tokens=llm_settings.max_tokens,
            timeout=llm_settings.timeout,
            retry_attempts=llm_settings.retry_attempts,
            retry_delay=llm_settings.retry_delay
        )
    
    def get_provider_with_fallback(
        self, 
        provider_priority: List[Union[ProviderType, str]]
    ) -> LLMProvider:
        """
        우선순위에 따라 Provider 반환 (폴백 지원)
        
        Args:
            provider_priority: Provider 우선순위 리스트
            
        Returns:
            LLMProvider: 사용 가능한 첫 번째 Provider
            
        Raises:
            RuntimeError: 사용 가능한 Provider가 없는 경우
        """
        for provider_type in provider_priority:
            try:
                provider = self.get_provider(provider_type)
                self.logger.info(f"폴백 Provider 선택: {provider_type}")
                return provider
            except Exception as e:
                self.logger.warning(f"{provider_type} Provider 사용 불가: {e}")
                continue
        
        raise RuntimeError("사용 가능한 LLM Provider가 없습니다")
    
    def get_default_provider(self) -> LLMProvider:
        """
        기본 Provider 반환
        
        Returns:
            LLMProvider: 기본 Provider 인스턴스
        """
        default_provider = self.settings.llm_provider.default_provider
        
        try:
            return self.get_provider(default_provider)
        except Exception as e:
            self.logger.warning(f"기본 Provider({default_provider}) 사용 불가: {e}")
            
            # 폴백 순서: Claude -> OpenAI -> EXAONE
            fallback_order = [
                ProviderType.CLAUDE,
                ProviderType.OPENAI,
                ProviderType.EXAONE
            ]
            
            return self.get_provider_with_fallback(fallback_order)
    
    def get_available_providers(self) -> List[ProviderType]:
        """
        사용 가능한 Provider 타입 리스트 반환
        
        Returns:
            List[ProviderType]: 사용 가능한 Provider 타입들
        """
        available = []
        
        for provider_type in ProviderType:
            try:
                # API 키 존재 여부 확인
                config = self._create_provider_config(provider_type)
                if config.api_key:
                    available.append(provider_type)
            except Exception:
                continue
        
        return available
    
    def get_provider_info(self, provider_type: Union[ProviderType, str]) -> Dict:
        """
        Provider 정보 반환 (인스턴스 생성 없이)
        
        Args:
            provider_type: Provider 타입
            
        Returns:
            Dict: Provider 정보
        """
        if isinstance(provider_type, str):
            provider_type = ProviderType(provider_type.lower())
        
        # Provider별 정보
        provider_info = {
            ProviderType.CLAUDE: {
                "name": "Claude",
                "company": "Anthropic",
                "strengths": ["자연어 이해", "한국어 지원", "구조화된 출력"],
                "best_for": ["고품질 분석", "복잡한 프롬프트", "창의적 생성"]
            },
            ProviderType.OPENAI: {
                "name": "OpenAI GPT",
                "company": "OpenAI",
                "strengths": ["JSON 모드", "일관된 출력", "다국어 지원"],
                "best_for": ["구조화된 출력", "JSON 생성", "표준화된 응답"]
            },
            ProviderType.EXAONE: {
                "name": "EXAONE",
                "company": "LG AI Research",
                "strengths": ["한국어 특화", "K-pop 이해", "비용 효율성"],
                "best_for": ["한국 음악", "K-pop 분석", "한국 아티스트"]
            }
        }
        
        return provider_info.get(provider_type, {})
    
    def clear_cache(self):
        """Provider 인스턴스 캐시 초기화"""
        self._provider_cache.clear()
        self.logger.info("Provider 캐시 초기화 완료")
    
    def get_cost_estimate(
        self, 
        provider_type: Union[ProviderType, str], 
        prompt: str
    ) -> float:
        """
        특정 Provider의 비용 추정
        
        Args:
            provider_type: Provider 타입
            prompt: 분석할 프롬프트
            
        Returns:
            float: 추정 비용 (USD)
        """
        try:
            provider = self.get_provider(provider_type)
            return provider.estimate_cost(prompt)
        except Exception as e:
            self.logger.error(f"비용 추정 실패 ({provider_type}): {e}")
            return 0.0
    
    def compare_providers(self, prompt: str) -> Dict[str, float]:
        """
        모든 사용 가능한 Provider의 비용 비교
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            Dict[str, float]: Provider별 추정 비용
        """
        costs = {}
        
        for provider_type in self.get_available_providers():
            try:
                cost = self.get_cost_estimate(provider_type, prompt)
                costs[provider_type.value] = cost
            except Exception as e:
                self.logger.warning(f"{provider_type} 비용 추정 실패: {e}")
        
        return costs


# 팩토리 인스턴스 관리
_factory_instance: Optional[LLMProviderFactory] = None


def get_factory(settings: Optional[Settings] = None) -> LLMProviderFactory:
    """
    글로벌 팩토리 인스턴스 반환
    
    Args:
        settings: 설정 (첫 번째 호출 시 필수)
        
    Returns:
        LLMProviderFactory: 팩토리 인스턴스
    """
    global _factory_instance
    
    if _factory_instance is None:
        if settings is None:
            # 기본 설정으로 초기화
            from ..config.settings import Settings
            settings = Settings()
        
        _factory_instance = LLMProviderFactory(settings)
    
    return _factory_instance


def reset_factory():
    """팩토리 인스턴스 초기화"""
    global _factory_instance
    _factory_instance = None 