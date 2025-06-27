"""
음악 파라미터 데이터 모델

자연어 프롬프트에서 추출된 음악적 파라미터를 구조화하여 저장하는 데이터 모델입니다.
3단계 장르 시스템, 아티스트 기반 생성, 4마디 스니펫 관리를 지원합니다.
"""

from typing import List, Optional, Literal
from pydantic import BaseModel, Field, validator
from enum import Enum


class SongPart(str, Enum):
    """곡의 구성 요소"""
    INTRO = "intro"
    VERSE = "verse"
    PRE_CHORUS = "pre_chorus"
    CHORUS = "chorus"
    BRIDGE = "bridge"
    OUTRO = "outro"
    FILL = "fill"
    BREAKDOWN = "breakdown"


class Instrument(str, Enum):
    """지원하는 악기 타입"""
    DRUMS = "drums"
    BASS = "bass"
    GUITAR = "guitar"
    PIANO = "piano"
    SYNTH_LEAD = "synth_lead"
    SYNTH_PAD = "synth_pad"
    VOCALS = "vocals"
    STRINGS = "strings"
    BRASS = "brass"
    PERCUSSION = "percussion"


class EnergyLevel(str, Enum):
    """에너지 레벨"""
    VERY_LOW = "very_low"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very_high"


class Complexity(str, Enum):
    """복잡도 레벨"""
    SIMPLE = "simple"
    MEDIUM = "medium"
    COMPLEX = "complex"
    VERY_COMPLEX = "very_complex"


class Duration(str, Enum):
    """스니펫 길이"""
    TWO_BARS = "2_bars"
    FOUR_BARS = "4_bars"
    EIGHT_BARS = "8_bars"
    SIXTEEN_BARS = "16_bars"


class MusicParams(BaseModel):
    """
    음악 생성을 위한 파라미터 모델
    
    자연어 프롬프트에서 추출된 모든 음악적 정보를 구조화하여 저장합니다.
    """
    
    # 기본 음악 정보
    instrument: Instrument = Field(..., description="메인 악기")
    song_part: SongPart = Field(..., description="곡의 구성 요소")
    
    # 3단계 장르 시스템
    genre: str = Field(..., description="메인 장르 (힙합, 락, 일렉트로닉 등)")
    sub_genre: str = Field(..., description="세부 장르 (트랩, J락, 하우스 등)")
    style_variant: str = Field(..., description="스타일 변형 (멜로딕 트랩, 시부야계 등)")
    
    # 음악적 특성
    mood: str = Field(..., description="분위기 (어두운, 밝은, 감성적 등)")
    tempo: int = Field(..., ge=60, le=200, description="BPM (60-200)")
    key: str = Field(..., description="조성 (C major, A minor 등)")
    time_signature: str = Field(default="4/4", description="박자 (4/4, 3/4 등)")
    
    # 복잡도 및 구조
    complexity: Complexity = Field(default=Complexity.MEDIUM, description="복잡도")
    duration: Duration = Field(default=Duration.FOUR_BARS, description="길이")
    energy_level: EnergyLevel = Field(default=EnergyLevel.MEDIUM, description="에너지 레벨")
    
    # 아티스트 기반 생성
    artist_reference: Optional[str] = Field(None, description="참조 아티스트 (지코, ONE OK ROCK 등)")
    country: Optional[str] = Field(None, description="국가/지역 (한국, 일본, 미국 등)")
    
    # 추가 설명
    style_descriptors: List[str] = Field(default_factory=list, description="스타일 설명 키워드")
    technical_notes: Optional[str] = Field(None, description="기술적 요구사항")
    
    @validator('tempo')
    def validate_tempo(cls, v):
        """템포 유효성 검사"""
        if not 60 <= v <= 200:
            raise ValueError('템포는 60-200 BPM 사이여야 합니다')
        return v
    
    @validator('key')
    def validate_key(cls, v):
        """조성 유효성 검사"""
        valid_keys = [
            'C major', 'C minor', 'C# major', 'C# minor',
            'D major', 'D minor', 'D# major', 'D# minor',
            'E major', 'E minor', 'F major', 'F minor',
            'F# major', 'F# minor', 'G major', 'G minor',
            'G# major', 'G# minor', 'A major', 'A minor',
            'A# major', 'A# minor', 'B major', 'B minor'
        ]
        if v not in valid_keys:
            raise ValueError(f'유효하지 않은 조성입니다: {v}')
        return v
    
    @validator('time_signature')
    def validate_time_signature(cls, v):
        """박자 유효성 검사"""
        valid_signatures = ['4/4', '3/4', '2/4', '6/8', '9/8', '12/8', '7/8', '5/4']
        if v not in valid_signatures:
            raise ValueError(f'유효하지 않은 박자입니다: {v}')
        return v
    
    def to_genre_path(self) -> str:
        """3단계 장르를 경로 형태로 반환"""
        return f"{self.genre}/{self.sub_genre}/{self.style_variant}"
    
    def to_filename(self) -> str:
        """파일명으로 사용할 수 있는 문자열 생성"""
        parts = [
            self.style_variant.replace(' ', '_').lower(),
            self.instrument.value,
            self.song_part.value,
            f"{self.tempo}bpm"
        ]
        if self.artist_reference:
            parts.insert(0, self.artist_reference.replace(' ', '_').lower())
        
        return '_'.join(parts)
    
    def get_summary(self) -> str:
        """파라미터 요약 문자열 반환"""
        summary = f"{self.to_genre_path()} {self.instrument.value} {self.song_part.value}"
        if self.artist_reference:
            summary = f"{self.artist_reference} 스타일 " + summary
        summary += f" ({self.tempo}BPM, {self.mood})"
        return summary


class GenerationRequest(BaseModel):
    """MIDI 생성 요청 모델"""
    
    prompt: str = Field(..., description="자연어 프롬프트")
    music_params: Optional[MusicParams] = Field(None, description="파싱된 음악 파라미터")
    output_format: str = Field(default="midi", description="출력 형식")
    include_preview: bool = Field(default=True, description="미리보기 오디오 생성 여부")
    
    class Config:
        json_schema_extra = {
            "example": {
                "prompt": "어두운 분위기의 붐뱁 드럼, 인트로용, 85BPM, 4마디",
                "output_format": "midi",
                "include_preview": True
            }
        }


class GenerationResult(BaseModel):
    """MIDI 생성 결과 모델"""
    
    id: str = Field(..., description="생성 결과 고유 ID")
    music_params: MusicParams = Field(..., description="사용된 음악 파라미터")
    
    # 파일 경로들
    midi_file: str = Field(..., description="생성된 MIDI 파일 경로")
    metadata_file: str = Field(..., description="메타데이터 JSON 파일 경로")
    preview_audio: Optional[str] = Field(None, description="미리보기 오디오 파일 경로")
    analysis_file: Optional[str] = Field(None, description="AI 분석 텍스트 파일 경로")
    
    # 품질 메트릭
    quality_score: float = Field(..., ge=0, le=10, description="AI 품질 점수 (0-10)")
    confidence: float = Field(..., ge=0, le=1, description="생성 신뢰도 (0-1)")
    
    # 추천 정보
    recommended_usage: List[str] = Field(default_factory=list, description="추천 사용 용도")
    similar_snippets: List[str] = Field(default_factory=list, description="유사한 스니펫 ID들")
    
    # 생성 정보
    generation_time: float = Field(..., description="생성 소요 시간 (초)")
    model_used: str = Field(..., description="사용된 AI 모델")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "snippet_20240127_143052_001",
                "midi_file": "generated_modules/dark_boombap_intro_85bpm.mid",
                "metadata_file": "generated_modules/dark_boombap_intro_85bpm_meta.json",
                "quality_score": 8.5,
                "confidence": 0.92,
                "generation_time": 2.3,
                "model_used": "claude-3.5-sonnet"
            }
        } 