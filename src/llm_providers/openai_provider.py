"""
OpenAI Provider 구현

OpenAI GPT-4 API를 사용하여 자연어 프롬프트를 음악 파라미터로 변환하는 Provider입니다.
GPT-4 모델에 최적화된 프롬프트 엔지니어링을 적용합니다.
"""

import json
import asyncio
from typing import Dict, Any, Optional
from openai import AsyncOpenAI

from .base import LLMProvider, ProviderConfig, PromptTemplate, APIError, ParseError
from ..data_models.music_params import MusicParams


class OpenAIProvider(LLMProvider):
    """
    OpenAI Provider 구현
    
    OpenAI GPT-4 API를 사용하여 자연어 프롬프트를 분석하고
    구조화된 음악 파라미터로 변환합니다.
    """
    
    def __init__(self, config: ProviderConfig):
        """
        OpenAI Provider 초기화
        
        Args:
            config: Provider 설정
        """
        super().__init__(config)
        self.client = AsyncOpenAI(
            api_key=config.api_key,
            timeout=config.timeout
        )
        
        # GPT 모델 매핑
        self.model_mapping = {
            "gpt-4": "gpt-4-turbo",
            "gpt-4-turbo": "gpt-4-turbo",
            "gpt-4o": "gpt-4o",
            "gpt-3.5-turbo": "gpt-3.5-turbo"
        }
        
        # 실제 모델명 설정
        self.actual_model = self.model_mapping.get(
            config.model_name, 
            config.model_name
        )
        
        self.logger.info(f"OpenAI Provider 초기화 완료 - 모델: {self.actual_model}")
    
    def _get_prompt_template(self) -> PromptTemplate:
        """
        OpenAI GPT에 최적화된 프롬프트 템플릿 반환
        
        Returns:
            PromptTemplate: OpenAI 특화 프롬프트 템플릿
        """
        return PromptTemplate(
            system_prompt="""You are a professional music producer and AI assistant specialized in analyzing natural language music requests and extracting precise musical parameters.

**CRITICAL INSTRUCTIONS:**
1. ALWAYS respond with valid JSON only - no explanations or additional text
2. ALL fields must be filled with accurate values
3. Use the 3-tier genre hierarchy system
4. Tempo must be within 60-200 BPM range
5. Key signatures should use format "C major" or "A minor"
6. For unclear information, use genre-appropriate defaults

**SUPPORTED GENRE HIERARCHY:**
- hip_hop → trap → melodic_trap/hard_trap/dark_trap
- hip_hop → boom_bap → old_school_boom_bap/modern_boom_bap/jazz_boom_bap  
- rock → j_rock → shibuya_kei/visual_kei/alternative_j_rock
- electronic → house → deep_house/tech_house/progressive_house

**INSTRUMENTS:** drums, bass, guitar, piano, synth_lead, synth_pad, vocals, strings, brass, percussion

**SONG PARTS:** intro, verse, pre_chorus, chorus, bridge, outro, fill, breakdown

**OUTPUT FORMAT:** Return ONLY the JSON object with no markdown formatting or explanations.""",
            
            user_prompt_format="""Analyze this music request and extract parameters as JSON:

"{user_input}"

Based on the examples below, return ONLY the JSON object:

{examples}""",
            
            examples=[
                {
                    "input": "Dark boom-bap drums for intro, 85 BPM",
                    "output": json.dumps({
                        "instrument": "drums",
                        "song_part": "intro",
                        "genre": "hip_hop",
                        "sub_genre": "boom_bap",
                        "style_variant": "old_school_boom_bap",
                        "mood": "dark",
                        "tempo": 85,
                        "key": "A minor",
                        "time_signature": "4/4",
                        "complexity": "medium",
                        "duration": "4_bars",
                        "energy_level": "low",
                        "artist_reference": None,
                        "country": None,
                        "style_descriptors": ["dark", "vintage", "underground"],
                        "technical_notes": None
                    })
                },
                {
                    "input": "Fast aggressive trap rap flow, verse section, Zico style",
                    "output": json.dumps({
                        "instrument": "vocals",
                        "song_part": "verse",
                        "genre": "hip_hop",
                        "sub_genre": "trap",
                        "style_variant": "melodic_trap",
                        "mood": "aggressive",
                        "tempo": 140,
                        "key": "C minor",
                        "time_signature": "4/4",
                        "complexity": "complex",
                        "duration": "4_bars",
                        "energy_level": "high",
                        "artist_reference": "Zico",
                        "country": "South Korea",
                        "style_descriptors": ["korean_trap", "melodic", "confident"],
                        "technical_notes": "Zico's characteristic flow patterns and Korean trap sensibility"
                    })
                },
                {
                    "input": "Emotional guitar solo like ONE OK ROCK, bridge section",
                    "output": json.dumps({
                        "instrument": "guitar",
                        "song_part": "bridge",
                        "genre": "rock",
                        "sub_genre": "j_rock",
                        "style_variant": "alternative_j_rock",
                        "mood": "emotional",
                        "tempo": 120,
                        "key": "E major",
                        "time_signature": "4/4",
                        "complexity": "complex",
                        "duration": "8_bars",
                        "energy_level": "medium",
                        "artist_reference": "ONE OK ROCK",
                        "country": "Japan",
                        "style_descriptors": ["emotional", "soaring", "j_rock"],
                        "technical_notes": "Taka's signature emotional guitar style with soaring melodies"
                    })
                }
            ]
        )
    
    async def _make_api_call(self, prompt: str) -> Dict[str, Any]:
        """
        OpenAI API 호출
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            Dict[str, Any]: OpenAI API 응답
            
        Raises:
            APIError: API 호출 실패 시
        """
        try:
            self.logger.debug(f"OpenAI API 호출 시작 - 모델: {self.actual_model}")
            
            # OpenAI API 메시지 형태로 구성
            messages = [
                {
                    "role": "system",
                    "content": self.prompt_template.system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
            
            # OpenAI API 호출
            response = await self.client.chat.completions.create(
                model=self.actual_model,
                messages=messages,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                response_format={"type": "json_object"}  # JSON 출력 강제
            )
            
            self.logger.debug("OpenAI API 호출 성공")
            
            # 응답을 표준 형태로 변환
            choice = response.choices[0] if response.choices else None
            if not choice:
                raise APIError("OpenAI API 응답이 비어있습니다")
            
            return {
                "content": choice.message.content or "",
                "model": response.model,
                "usage": {
                    "input_tokens": response.usage.prompt_tokens if response.usage else 0,
                    "output_tokens": response.usage.completion_tokens if response.usage else 0
                },
                "finish_reason": choice.finish_reason,
                "status": "success"
            }
            
        except Exception as e:
            self.logger.error(f"OpenAI API 호출 실패: {e}")
            raise APIError(f"OpenAI API 호출 실패: {e}")
    
    def _extract_content(self, response_data: Dict[str, Any]) -> str:
        """
        OpenAI API 응답에서 내용 추출
        
        Args:
            response_data: OpenAI API 응답 데이터
            
        Returns:
            str: 추출된 내용
        """
        content = response_data.get("content", "")
        
        # GPT-4의 JSON 모드 사용 시 일반적으로 깔끔한 JSON이 반환됨
        content = content.strip()
        
        # 혹시 markdown 코드 블록이 있다면 제거
        if content.startswith("```json"):
            start = content.find("```json") + 7
            end = content.rfind("```")
            if end != -1:
                content = content[start:end].strip()
        elif content.startswith("```"):
            start = content.find("```") + 3
            end = content.rfind("```")
            if end != -1:
                content = content[start:end].strip()
        
        return content
    
    def estimate_cost(self, prompt: str) -> float:
        """
        OpenAI API 호출 비용 추정
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            float: 추정 비용 (USD)
        """
        # GPT-4 토큰 계산 (대략적)
        input_tokens = len(prompt.split()) * 1.3  # 영어 기준
        output_tokens = 500  # 예상 출력 토큰 수
        
        # GPT-4 Turbo 가격 (2024년 기준)
        # Input: $10.00 per million tokens
        # Output: $30.00 per million tokens
        if "gpt-4" in self.actual_model.lower():
            input_rate = 10.00
            output_rate = 30.00
        else:  # GPT-3.5 Turbo
            input_rate = 0.50
            output_rate = 1.50
        
        input_cost = (input_tokens / 1_000_000) * input_rate
        output_cost = (output_tokens / 1_000_000) * output_rate
        
        total_cost = input_cost + output_cost
        
        self.logger.debug(f"비용 추정 - Input: {input_tokens} tokens (${input_cost:.6f}), "
                         f"Output: {output_tokens} tokens (${output_cost:.6f}), "
                         f"Total: ${total_cost:.6f}")
        
        return total_cost
    
    async def generate_title_suggestion(self, params: MusicParams) -> str:
        """
        OpenAI GPT를 사용한 음악 제목 생성
        
        Args:
            params: 음악 파라미터
            
        Returns:
            str: 제안된 곡 제목
        """
        title_prompt = f"""Generate a creative and appropriate song title based on these music parameters:

Genre Path: {params.to_genre_path()}
Instrument: {params.instrument.value}
Song Part: {params.song_part.value}
Mood: {params.mood}
Tempo: {params.tempo} BPM
Key: {params.key}
Artist Reference: {params.artist_reference or 'None'}
Country: {params.country or 'None'}

Requirements:
- Title should match the mood and genre
- If artist reference exists, reflect their style
- Use appropriate language (Korean or English based on genre/artist)
- Return ONLY the song title, no explanations

Song Title:"""

        try:
            # 시스템 프롬프트 수정 (제목 생성용)
            messages = [
                {
                    "role": "system",
                    "content": "You are a creative music producer who generates perfect song titles. Return only the title, no explanations or quotes."
                },
                {
                    "role": "user",
                    "content": title_prompt
                }
            ]
            
            response = await self.client.chat.completions.create(
                model=self.actual_model,
                messages=messages,
                max_tokens=50,
                temperature=0.8  # 창의성을 위해 높은 temperature
            )
            
            choice = response.choices[0] if response.choices else None
            if not choice or not choice.message.content:
                raise Exception("빈 응답")
            
            content = choice.message.content.strip()
            
            # 제목 정리 (따옴표, 줄바꿈 등 제거)
            title = content.strip('"').strip("'").strip()
            
            # 여러 줄인 경우 첫 번째 줄만 사용
            if '\n' in title:
                title = title.split('\n')[0].strip()
            
            return title
            
        except Exception as e:
            self.logger.warning(f"OpenAI 제목 생성 실패: {e}")
            return self._generate_fallback_title(params)
    
    def _parse_text_response(self, content: str) -> MusicParams:
        """
        OpenAI 응답의 텍스트를 MusicParams로 파싱
        
        Args:
            content: OpenAI 응답 텍스트
            
        Returns:
            MusicParams: 파싱된 음악 파라미터
            
        Raises:
            ParseError: 파싱 실패 시
        """
        try:
            # JSON 모드를 사용하므로 일반적으로 깔끔한 JSON이 반환됨
            content = content.strip()
            
            if not content:
                raise ParseError("빈 응답입니다")
            
            # JSON 파싱
            params_dict = json.loads(content)
            
            # MusicParams 객체 생성
            return MusicParams(**params_dict)
            
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON 파싱 실패: {e}")
            self.logger.error(f"파싱 시도한 내용: {content[:500]}...")
            raise ParseError(f"JSON 파싱 실패: {e}")
        except Exception as e:
            self.logger.error(f"MusicParams 생성 실패: {e}")
            raise ParseError(f"MusicParams 생성 실패: {e}")
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        OpenAI 모델 정보 반환
        
        Returns:
            Dict[str, Any]: 모델 정보
        """
        base_info = super().get_model_info()
        
        # 모델별 컨텍스트 길이 설정
        context_lengths = {
            "gpt-4-turbo": 128000,
            "gpt-4o": 128000,
            "gpt-4": 8192,
            "gpt-3.5-turbo": 16385
        }
        
        max_context = context_lengths.get(self.actual_model, 8192)
        
        base_info.update({
            "provider": "OpenAI",
            "actual_model": self.actual_model,
            "api_version": "v1",
            "supports_system_prompt": True,
            "supports_json_mode": True,
            "max_context_length": max_context,
            "strengths": [
                "structured_output",
                "json_formatting",
                "consistent_responses",
                "multilingual_support"
            ]
        })
        return base_info 