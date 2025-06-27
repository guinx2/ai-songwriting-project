"""
EXAONE Provider 구현

LG AI Research의 EXAONE 3.5 API를 사용하여 자연어 프롬프트를 음악 파라미터로 변환하는 Provider입니다.
한국어 처리에 특화되어 있으며, 한국 음악 문화와 아티스트에 대한 이해도가 높습니다.
"""

import json
import asyncio
from typing import Dict, Any, Optional
import httpx

from .base import LLMProvider, ProviderConfig, PromptTemplate, APIError, ParseError
from ..data_models.music_params import MusicParams


class ExaoneProvider(LLMProvider):
    """
    EXAONE Provider 구현
    
    EXAONE 3.5 API를 사용하여 자연어 프롬프트를 분석하고
    구조화된 음악 파라미터로 변환합니다.
    한국어 및 한국 음악 문화에 특화되어 있습니다.
    """
    
    def __init__(self, config: ProviderConfig):
        """
        EXAONE Provider 초기화
        
        Args:
            config: Provider 설정
        """
        super().__init__(config)
        
        # EXAONE API 설정
        self.base_url = "https://api.exaone.ai/v1"  # 실제 URL은 LG AI Research에서 제공
        self.headers = {
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json"
        }
        
        # EXAONE 모델 매핑
        self.model_mapping = {
            "exaone-3.5": "exaone-3.5-turbo",
            "exaone-3.5-turbo": "exaone-3.5-turbo",
            "exaone-3.0": "exaone-3.0"
        }
        
        # 실제 모델명 설정
        self.actual_model = self.model_mapping.get(
            config.model_name, 
            config.model_name
        )
        
        self.logger.info(f"EXAONE Provider 초기화 완료 - 모델: {self.actual_model}")
    
    def _get_prompt_template(self) -> PromptTemplate:
        """
        EXAONE에 최적화된 프롬프트 템플릿 반환 (한국어 특화)
        
        Returns:
            PromptTemplate: EXAONE 특화 프롬프트 템플릿
        """
        return PromptTemplate(
            system_prompt="""당신은 한국 음악 제작 전문가이자 AI 어시스턴트입니다. 자연어로 된 음악 요청을 분석하여 정확한 음악 파라미터를 추출하는 것이 목표입니다.

**핵심 지침:**
1. 반드시 유효한 JSON 형태로만 응답하세요
2. 모든 필드는 정확한 값으로 채워야 합니다
3. 3단계 장르 계층 구조를 따라야 합니다
4. 템포는 60-200 BPM 범위 내에서 설정하세요
5. 조성은 "C major", "A minor" 형식을 사용하세요
6. 불명확한 정보는 장르와 분위기에 맞는 일반적인 값으로 설정하세요
7. 한국 아티스트와 K-pop, K-힙합 스타일에 특별히 주의하세요

**지원 장르 계층:**
- hip_hop → trap → melodic_trap/hard_trap/dark_trap/korean_trap
- hip_hop → boom_bap → old_school_boom_bap/modern_boom_bap/korean_boom_bap
- kpop → idol_pop → girl_group/boy_group/solo_artist
- rock → k_rock → indie_k_rock/metal_k_rock/punk_k_rock
- electronic → k_electronic → future_bass/trap_edm/house_k_style

**한국 아티스트 특성 이해:**
- 지코: 멜로딕 트랩, 한국적 감성, 자신감 있는 플로우
- 수민 (SUMIN): 로파이 힙합, 감성적, 미니멀
- 크러쉬: R&B, 소울풀, 부드러운 감성
- 헤이즈: 어쿠스틱 팝, 허스키 보이스, 감성적
- 딘: 얼터너티브 R&B, 몽환적, 현대적

**악기 타입:** drums, bass, guitar, piano, synth_lead, synth_pad, vocals, strings, brass, percussion

**송 파트:** intro, verse, pre_chorus, chorus, bridge, outro, fill, breakdown""",
            
            user_prompt_format="""사용자 요청: "{user_input}"

위 요청을 분석하여 다음 형태의 JSON으로 응답해주세요:

{examples}

JSON만 반환하고 다른 설명은 포함하지 마세요:""",
            
            examples=[
                {
                    "input": "지코 스타일 트랩 랩 플로우, 벌스용, 빠르고 강렬하게",
                    "output": json.dumps({
                        "instrument": "vocals",
                        "song_part": "verse",
                        "genre": "hip_hop",
                        "sub_genre": "trap",
                        "style_variant": "korean_trap",
                        "mood": "confident",
                        "tempo": 140,
                        "key": "C minor",
                        "time_signature": "4/4",
                        "complexity": "complex",
                        "duration": "4_bars",
                        "energy_level": "high",
                        "artist_reference": "지코",
                        "country": "한국",
                        "style_descriptors": ["korean_trap", "melodic", "confident", "seoul_style"],
                        "technical_notes": "지코 특유의 멜로딕 트랩 플로우와 한국적 랩 감성"
                    }, ensure_ascii=False, indent=2)
                },
                {
                    "input": "수민 스타일 로파이 기타, 인트로용, 감성적이고 차분하게",
                    "output": json.dumps({
                        "instrument": "guitar",
                        "song_part": "intro",
                        "genre": "hip_hop",
                        "sub_genre": "lofi_hip_hop",
                        "style_variant": "korean_lofi",
                        "mood": "melancholic",
                        "tempo": 85,
                        "key": "D major",
                        "time_signature": "4/4",
                        "complexity": "simple",
                        "duration": "4_bars",
                        "energy_level": "low",
                        "artist_reference": "수민",
                        "country": "한국",
                        "style_descriptors": ["lofi", "emotional", "minimalist", "korean_indie"],
                        "technical_notes": "수민 특유의 미니멀하고 감성적인 기타 연주 스타일"
                    }, ensure_ascii=False, indent=2)
                },
                {
                    "input": "어두운 분위기의 붐뱁 드럼, 인트로용, 85BPM",
                    "output": json.dumps({
                        "instrument": "drums",
                        "song_part": "intro",
                        "genre": "hip_hop",
                        "sub_genre": "boom_bap",
                        "style_variant": "korean_boom_bap",
                        "mood": "dark",
                        "tempo": 85,
                        "key": "A minor",
                        "time_signature": "4/4",
                        "complexity": "medium",
                        "duration": "4_bars",
                        "energy_level": "low",
                        "artist_reference": None,
                        "country": "한국",
                        "style_descriptors": ["dark", "vintage", "underground", "seoul_underground"],
                        "technical_notes": None
                    }, ensure_ascii=False, indent=2)
                },
                {
                    "input": "아이유 스타일 감성 발라드 피아노, 코러스용",
                    "output": json.dumps({
                        "instrument": "piano",
                        "song_part": "chorus",
                        "genre": "kpop",
                        "sub_genre": "ballad",
                        "style_variant": "k_ballad",
                        "mood": "emotional",
                        "tempo": 72,
                        "key": "F major",
                        "time_signature": "4/4",
                        "complexity": "medium",
                        "duration": "8_bars",
                        "energy_level": "medium",
                        "artist_reference": "아이유",
                        "country": "한국",
                        "style_descriptors": ["emotional", "elegant", "korean_sentiment", "heartfelt"],
                        "technical_notes": "아이유 특유의 감성적이고 우아한 피아노 반주 스타일"
                    }, ensure_ascii=False, indent=2)
                }
            ]
        )
    
    async def _make_api_call(self, prompt: str) -> Dict[str, Any]:
        """
        EXAONE API 호출
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            Dict[str, Any]: EXAONE API 응답
            
        Raises:
            APIError: API 호출 실패 시
        """
        try:
            self.logger.debug(f"EXAONE API 호출 시작 - 모델: {self.actual_model}")
            
            # EXAONE API 요청 데이터 구성
            request_data = {
                "model": self.actual_model,
                "messages": [
                    {
                        "role": "system",
                        "content": self.prompt_template.system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": self.config.max_tokens,
                "temperature": self.config.temperature,
                "stream": False
            }
            
            # HTTP 클라이언트를 사용한 API 호출
            async with httpx.AsyncClient(
                timeout=httpx.Timeout(self.config.timeout)
            ) as client:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json=request_data
                )
                
                # HTTP 상태 코드 확인
                if response.status_code != 200:
                    error_msg = f"EXAONE API HTTP 오류 {response.status_code}: {response.text}"
                    self.logger.error(error_msg)
                    raise APIError(error_msg)
                
                response_data = response.json()
                
                self.logger.debug("EXAONE API 호출 성공")
                
                # 표준 형태로 응답 변환
                choices = response_data.get("choices", [])
                if not choices:
                    raise APIError("EXAONE API 응답에 choices가 없습니다")
                
                choice = choices[0]
                message = choice.get("message", {})
                usage = response_data.get("usage", {})
                
                return {
                    "content": message.get("content", ""),
                    "model": response_data.get("model", self.actual_model),
                    "usage": {
                        "input_tokens": usage.get("prompt_tokens", 0),
                        "output_tokens": usage.get("completion_tokens", 0)
                    },
                    "finish_reason": choice.get("finish_reason", "unknown"),
                    "status": "success"
                }
                
        except httpx.TimeoutException:
            error_msg = f"EXAONE API 타임아웃 ({self.config.timeout}초)"
            self.logger.error(error_msg)
            raise APIError(error_msg)
        except Exception as e:
            self.logger.error(f"EXAONE API 호출 실패: {e}")
            raise APIError(f"EXAONE API 호출 실패: {e}")
    
    def _extract_content(self, response_data: Dict[str, Any]) -> str:
        """
        EXAONE API 응답에서 내용 추출
        
        Args:
            response_data: EXAONE API 응답 데이터
            
        Returns:
            str: 추출된 내용
        """
        content = response_data.get("content", "")
        
        # EXAONE 응답에서 JSON 부분 추출
        content = content.strip()
        
        # 코드 블록 제거
        if "```json" in content:
            start = content.find("```json") + 7
            end = content.find("```", start)
            if end != -1:
                content = content[start:end].strip()
        elif content.startswith("```"):
            start = content.find("```") + 3
            end = content.rfind("```")
            if end != -1:
                content = content[start:end].strip()
        
        # JSON 시작점 찾기
        if not content.startswith('{'):
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('{'):
                    # JSON 부분만 추출
                    json_lines = []
                    brace_count = 0
                    
                    for j in range(i, len(lines)):
                        current_line = lines[j]
                        json_lines.append(current_line)
                        
                        brace_count += current_line.count('{')
                        brace_count -= current_line.count('}')
                        
                        if brace_count == 0:
                            break
                    
                    content = '\n'.join(json_lines)
                    break
        
        return content
    
    def estimate_cost(self, prompt: str) -> float:
        """
        EXAONE API 호출 비용 추정
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            float: 추정 비용 (USD)
        """
        # EXAONE 토큰 계산 (한국어 특화)
        # 한국어는 토큰 수가 영어보다 높을 수 있음
        input_tokens = len(prompt.split()) * 1.5  # 한국어 특성 반영
        output_tokens = 500  # 예상 출력 토큰 수
        
        # EXAONE 3.5 가격 (가정값 - 실제 가격은 LG AI Research 정책에 따름)
        # Input: $2.00 per million tokens (Claude보다 저렴하다고 가정)
        # Output: $10.00 per million tokens
        input_cost = (input_tokens / 1_000_000) * 2.00
        output_cost = (output_tokens / 1_000_000) * 10.00
        
        total_cost = input_cost + output_cost
        
        self.logger.debug(f"비용 추정 - Input: {input_tokens} tokens (${input_cost:.6f}), "
                         f"Output: {output_tokens} tokens (${output_cost:.6f}), "
                         f"Total: ${total_cost:.6f}")
        
        return total_cost
    
    async def generate_title_suggestion(self, params: MusicParams) -> str:
        """
        EXAONE을 사용한 한국어 음악 제목 생성
        
        Args:
            params: 음악 파라미터
            
        Returns:
            str: 제안된 곡 제목
        """
        # 한국어에 특화된 제목 생성 프롬프트
        title_prompt = f"""다음 음악 파라미터를 바탕으로 창의적이고 한국적 감성이 담긴 곡 제목을 하나만 제안해주세요:

장르 경로: {params.to_genre_path()}
악기: {params.instrument.value}
송 파트: {params.song_part.value}
분위기: {params.mood}
템포: {params.tempo}BPM
키: {params.key}
아티스트 참조: {params.artist_reference or '없음'}
국가: {params.country or '한국'}
스타일 특성: {', '.join(params.style_descriptors) if params.style_descriptors else '없음'}

요구사항:
- 분위기와 장르에 완벽하게 맞는 제목
- 아티스트 참조가 있다면 해당 아티스트의 스타일과 감성 반영
- 한국어 또는 영어 (아티스트와 장르에 따라 자연스럽게 선택)
- K-pop, K-힙합 등 한국 음악의 트렌드와 감성 고려
- 곡 제목만 반환 (설명이나 따옴표 없이)

곡 제목:"""

        try:
            response_data = await self._make_api_call(title_prompt)
            content = self._extract_content(response_data)
            
            # 제목 정리
            title = content.strip().strip('"').strip("'").strip()
            
            # 여러 줄인 경우 첫 번째 줄만 사용
            if '\n' in title:
                title = title.split('\n')[0].strip()
            
            # "곡 제목:" 등의 접두사 제거
            if ':' in title:
                title = title.split(':', 1)[-1].strip()
            
            return title
            
        except Exception as e:
            self.logger.warning(f"EXAONE 제목 생성 실패: {e}")
            return self._generate_fallback_title(params)
    
    def _parse_text_response(self, content: str) -> MusicParams:
        """
        EXAONE 응답의 텍스트를 MusicParams로 파싱
        
        Args:
            content: EXAONE 응답 텍스트
            
        Returns:
            MusicParams: 파싱된 음악 파라미터
            
        Raises:
            ParseError: 파싱 실패 시
        """
        try:
            content = content.strip()
            
            if not content:
                raise ParseError("빈 응답입니다")
            
            # JSON 파싱 시도
            params_dict = json.loads(content)
            
            # 한국어 특화 후처리
            if params_dict.get("country") is None and "korean" in str(params_dict).lower():
                params_dict["country"] = "한국"
            
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
        EXAONE 모델 정보 반환
        
        Returns:
            Dict[str, Any]: 모델 정보
        """
        base_info = super().get_model_info()
        base_info.update({
            "provider": "EXAONE",
            "actual_model": self.actual_model,
            "api_version": "v1",
            "supports_system_prompt": True,
            "max_context_length": 32768,  # EXAONE 3.5 기준 (가정값)
            "strengths": [
                "korean_language_expert",
                "korean_culture_understanding",
                "kpop_music_knowledge",
                "korean_artist_styles",
                "cost_effectiveness",
                "local_music_trends"
            ],
            "specialties": [
                "K-pop 분석",
                "한국 아티스트 스타일 모방",
                "한국어 자연어 처리",
                "한국 음악 문화 이해"
            ]
        })
        return base_info 