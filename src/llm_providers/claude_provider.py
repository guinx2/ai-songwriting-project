"""
Claude Provider 구현

Anthropic Claude API를 사용하여 자연어 프롬프트를 음악 파라미터로 변환하는 Provider입니다.
Claude 3.5 Sonnet 모델에 최적화된 프롬프트 엔지니어링을 적용합니다.
"""

import json
import asyncio
from typing import Dict, Any, Optional
import httpx
from anthropic import AsyncAnthropic

from .base import LLMProvider, ProviderConfig, PromptTemplate, APIError, ParseError
from ..data_models.music_params import MusicParams


class ClaudeProvider(LLMProvider):
    """
    Claude Provider 구현
    
    Anthropic Claude API를 사용하여 자연어 프롬프트를 분석하고
    구조화된 음악 파라미터로 변환합니다.
    """
    
    def __init__(self, config: ProviderConfig):
        """
        Claude Provider 초기화
        
        Args:
            config: Provider 설정
        """
        # 기본 모델을 claude-4-sonnet으로 설정
        if not config.model_name or config.model_name == "claude-3-5-sonnet":
            config.model_name = "claude-4-sonnet"
            
        super().__init__(config)
        self.client = AsyncAnthropic(
            api_key=config.api_key,
            timeout=httpx.Timeout(config.timeout)
        )
        
        # Claude 특화 모델 매핑
        self.model_mapping = {
            "claude-4-sonnet": "claude-4-sonnet-20241022",
            "claude-3-5-sonnet": "claude-3-5-sonnet-20241022",
            "claude-3-sonnet": "claude-3-sonnet-20240229",
            "claude-3-haiku": "claude-3-haiku-20240307"
        }
        
        # 실제 모델명 설정
        self.actual_model = self.model_mapping.get(
            config.model_name, 
            config.model_name
        )
        
        self.logger.info(f"Claude Provider 초기화 완료 - 모델: {self.actual_model}")
    
    def _get_prompt_template(self) -> PromptTemplate:
        """
        Claude에 최적화된 프롬프트 템플릿 반환
        
        Returns:
            PromptTemplate: Claude 특화 프롬프트 템플릿
        """
        return PromptTemplate(
            system_prompt="""당신은 음악 제작 전문가입니다. 자연어로 된 음악 요청을 분석하여 정확한 음악 파라미터를 추출하는 것이 목표입니다.

**중요 지침:**
1. 반드시 유효한 JSON 형태로만 응답하세요
2. 모든 필드는 정확한 값으로 채워야 합니다
3. 장르는 3단계 계층 구조를 따라야 합니다
4. 템포는 60-200 BPM 범위 내에서 설정하세요
5. 조성은 "C major", "A minor" 형식을 사용하세요
6. 불명확한 정보는 장르와 분위기에 맞는 일반적인 값으로 설정하세요

**지원 장르 계층:**
- hip_hop → trap → melodic_trap/hard_trap/dark_trap
- hip_hop → boom_bap → old_school_boom_bap/modern_boom_bap/jazz_boom_bap  
- rock → j_rock → shibuya_kei/visual_kei/alternative_j_rock
- electronic → house → deep_house/tech_house/progressive_house

**악기 타입:** drums, bass, guitar, piano, synth_lead, synth_pad, vocals, strings, brass, percussion

**송 파트:** intro, verse, pre_chorus, chorus, bridge, outro, fill, breakdown""",
            
            user_prompt_format="""사용자 요청: "{user_input}"

위 요청을 분석하여 다음 형태의 JSON으로 응답해주세요:

{examples}

JSON만 반환하고 다른 설명은 포함하지 마세요:""",
            
            examples=[
                {
                    "input": "어두운 분위기의 붐뱁 드럼, 인트로용, 85BPM",
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
                        "artist_reference": null,
                        "country": null,
                        "style_descriptors": ["dark", "vintage", "underground"],
                        "technical_notes": null
                    }, ensure_ascii=False, indent=2)
                },
                {
                    "input": "지코 스타일 트랩 랩 플로우, 벌스용, 빠르고 강렬하게",
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
                        "artist_reference": "지코",
                        "country": "한국",
                        "style_descriptors": ["korean_trap", "melodic", "confident"],
                        "technical_notes": "Zico's characteristic flow patterns and Korean trap sensibility"
                    }, ensure_ascii=False, indent=2)
                },
                {
                    "input": "ONE OK ROCK 스타일 감성적인 기타 솔로, 브릿지용",
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
                        "country": "일본",
                        "style_descriptors": ["emotional", "soaring", "j_rock"],
                        "technical_notes": "Taka's signature emotional guitar style with soaring melodies"
                    }, ensure_ascii=False, indent=2)
                }
            ]
        )
    
    async def _make_api_call(self, prompt: str) -> Dict[str, Any]:
        """
        Claude API 호출
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            Dict[str, Any]: Claude API 응답
            
        Raises:
            APIError: API 호출 실패 시
        """
        try:
            self.logger.debug(f"Claude API 호출 시작 - 모델: {self.actual_model}")
            
            # Claude API 메시지 형태로 구성
            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
            
            # Claude API 호출
            response = await self.client.messages.create(
                model=self.actual_model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                system=self.prompt_template.system_prompt,
                messages=messages
            )
            
            self.logger.debug("Claude API 호출 성공")
            
            # 응답을 표준 형태로 변환
            return {
                "content": response.content[0].text if response.content else "",
                "model": response.model,
                "usage": {
                    "input_tokens": response.usage.input_tokens if response.usage else 0,
                    "output_tokens": response.usage.output_tokens if response.usage else 0
                },
                "status": "success"
            }
            
        except Exception as e:
            self.logger.error(f"Claude API 호출 실패: {e}")
            raise APIError(f"Claude API 호출 실패: {e}")
    
    def _extract_content(self, response_data: Dict[str, Any]) -> str:
        """
        Claude API 응답에서 내용 추출
        
        Args:
            response_data: Claude API 응답 데이터
            
        Returns:
            str: 추출된 내용
        """
        content = response_data.get("content", "")
        
        # Claude 응답에서 JSON 부분만 추출
        if "```json" in content:
            # 코드 블록 형태의 JSON 추출
            start = content.find("```json") + 7
            end = content.find("```", start)
            if end != -1:
                content = content[start:end].strip()
        elif content.strip().startswith('{'):
            # 이미 JSON 형태인 경우 그대로 사용
            content = content.strip()
        else:
            # JSON이 아닌 경우 찾아서 추출
            lines = content.split('\n')
            json_lines = []
            in_json = False
            
            for line in lines:
                if line.strip().startswith('{'):
                    in_json = True
                if in_json:
                    json_lines.append(line)
                if line.strip().endswith('}') and in_json:
                    break
            
            content = '\n'.join(json_lines)
        
        return content
    
    def estimate_cost(self, prompt: str) -> float:
        """
        Claude API 호출 비용 추정
        
        Args:
            prompt: 분석할 프롬프트
            
        Returns:
            float: 추정 비용 (USD)
        """
        # Claude 토큰 계산 (대략적)
        input_tokens = len(prompt.split()) * 1.3  # 영어 기준
        output_tokens = 500  # 예상 출력 토큰 수
        
        # Claude 3.5 Sonnet 가격 (2024년 기준)
        # Input: $3.00 per million tokens
        # Output: $15.00 per million tokens
        input_cost = (input_tokens / 1_000_000) * 3.00
        output_cost = (output_tokens / 1_000_000) * 15.00
        
        total_cost = input_cost + output_cost
        
        self.logger.debug(f"비용 추정 - Input: {input_tokens} tokens (${input_cost:.6f}), "
                         f"Output: {output_tokens} tokens (${output_cost:.6f}), "
                         f"Total: ${total_cost:.6f}")
        
        return total_cost
    
    async def generate_title_suggestion(self, params: MusicParams) -> str:
        """
        Claude를 사용한 음악 제목 생성
        
        Args:
            params: 음악 파라미터
            
        Returns:
            str: 제안된 곡 제목
        """
        title_prompt = f"""다음 음악 파라미터를 바탕으로 창의적이고 적절한 곡 제목을 하나만 제안해주세요:

장르: {params.to_genre_path()}
악기: {params.instrument.value}
파트: {params.song_part.value}
분위기: {params.mood}
템포: {params.tempo}BPM
키: {params.key}
아티스트 참조: {params.artist_reference or '없음'}
국가: {params.country or '없음'}

요구사항:
- 분위기와 장르에 맞는 제목
- 아티스트 참조가 있다면 해당 스타일 반영
- 한국어 또는 영어 (장르/아티스트에 따라 적절히 선택)
- 곡 제목만 반환 (설명 없이)

곡 제목:"""

        try:
            response_data = await self._make_api_call(title_prompt)
            content = self._extract_content(response_data)
            
            # 제목 정리 (따옴표, 줄바꿈 등 제거)
            title = content.strip().strip('"').strip("'").strip()
            
            # 여러 줄인 경우 첫 번째 줄만 사용
            if '\n' in title:
                title = title.split('\n')[0].strip()
            
            return title
            
        except Exception as e:
            self.logger.warning(f"Claude 제목 생성 실패: {e}")
            return self._generate_fallback_title(params)
    
    def _parse_text_response(self, content: str) -> MusicParams:
        """
        Claude 응답의 텍스트를 MusicParams로 파싱
        
        Args:
            content: Claude 응답 텍스트
            
        Returns:
            MusicParams: 파싱된 음악 파라미터
            
        Raises:
            ParseError: 파싱 실패 시
        """
        try:
            # JSON 파싱 시도
            if content.strip().startswith('{'):
                params_dict = json.loads(content.strip())
                return MusicParams(**params_dict)
            
            # JSON이 아닌 경우 Claude 특화 파싱
            # Claude가 때로는 설명과 함께 JSON을 반환할 수 있음
            lines = content.strip().split('\n')
            json_text = ""
            
            for i, line in enumerate(lines):
                if line.strip().startswith('{'):
                    # JSON 시작점 찾기
                    json_lines = []
                    brace_count = 0
                    
                    for j in range(i, len(lines)):
                        current_line = lines[j]
                        json_lines.append(current_line)
                        
                        # 중괄호 개수 세기
                        brace_count += current_line.count('{')
                        brace_count -= current_line.count('}')
                        
                        if brace_count == 0:
                            break
                    
                    json_text = '\n'.join(json_lines)
                    break
            
            if json_text:
                params_dict = json.loads(json_text)
                return MusicParams(**params_dict)
            
            raise ParseError("유효한 JSON을 찾을 수 없습니다")
            
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON 파싱 실패: {e}")
            self.logger.error(f"파싱 시도한 내용: {content[:500]}...")
            raise ParseError(f"JSON 파싱 실패: {e}")
        except Exception as e:
            self.logger.error(f"MusicParams 생성 실패: {e}")
            raise ParseError(f"MusicParams 생성 실패: {e}")
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Claude 모델 정보 반환
        
        Returns:
            Dict[str, Any]: 모델 정보
        """
        base_info = super().get_model_info()
        base_info.update({
            "provider": "Claude",
            "actual_model": self.actual_model,
            "api_version": "2023-06-01",
            "supports_system_prompt": True,
            "max_context_length": 200000,  # Claude 3.5 Sonnet 기준
            "strengths": [
                "natural_language_understanding",
                "structured_output",
                "korean_language_support",
                "music_domain_knowledge"
            ]
        })
        return base_info 