"""
설정 관리 시스템

환경 변수, API 키, LLM Provider 설정을 관리합니다.
"""

import os
from typing import Optional, Dict, Any
from pydantic import Field, validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()


class LLMProviderSettings(BaseSettings):
    """LLM Provider 설정"""
    
    # API Keys
    anthropic_api_key: Optional[str] = Field(None, env="ANTHROPIC_API_KEY")
    openai_api_key: Optional[str] = Field(None, env="OPENAI_API_KEY")
    exaone_api_key: Optional[str] = Field(None, env="EXAONE_API_KEY")
    
    # API Endpoints
    exaone_base_url: str = Field("https://api.exaone.ai/v1", env="EXAONE_BASE_URL")
    openai_base_url: str = Field("https://api.openai.com/v1", env="OPENAI_BASE_URL")
    
    # 기본 설정
    default_provider: str = Field("claude", env="DEFAULT_LLM_PROVIDER")
    max_tokens: int = Field(4000, env="MAX_TOKENS")
    temperature: float = Field(0.7, env="TEMPERATURE")
    
    @validator('default_provider')
    def validate_provider(cls, v):
        """지원하는 프로바이더인지 확인"""
        valid_providers = ['claude', 'openai', 'exaone']
        if v not in valid_providers:
            raise ValueError(f'지원하지 않는 프로바이더입니다: {v}. 지원 프로바이더: {valid_providers}')
        return v
    
    @validator('max_tokens')
    def validate_max_tokens(cls, v):
        """토큰 수 유효성 검사"""
        if not 100 <= v <= 8000:
            raise ValueError('max_tokens는 100-8000 사이여야 합니다')
        return v
    
    @validator('temperature')
    def validate_temperature(cls, v):
        """온도 유효성 검사"""
        if not 0.0 <= v <= 2.0:
            raise ValueError('temperature는 0.0-2.0 사이여야 합니다')
        return v
    
    def get_api_key(self, provider: str) -> Optional[str]:
        """프로바이더별 API 키 반환"""
        if provider == "claude":
            return self.anthropic_api_key
        elif provider == "openai":
            return self.openai_api_key
        elif provider == "exaone":
            return self.exaone_api_key
        else:
            raise ValueError(f"지원하지 않는 프로바이더: {provider}")
    
    def is_provider_available(self, provider: str) -> bool:
        """프로바이더가 사용 가능한지 확인 (API 키 존재 여부)"""
        api_key = self.get_api_key(provider)
        return api_key is not None and api_key.strip() != ""
    
    def get_available_providers(self) -> list:
        """사용 가능한 프로바이더 목록 반환"""
        providers = []
        for provider in ['claude', 'openai', 'exaone']:
            if self.is_provider_available(provider):
                providers.append(provider)
        return providers

    class Config:
        extra = "ignore"  # extra inputs 허용


class DatabaseSettings(BaseSettings):
    """데이터베이스 설정"""
    
    database_url: str = Field("sqlite:///./data/ai_songwriting.db", env="DATABASE_URL")
    echo_sql: bool = Field(False, env="ECHO_SQL")
    
    class Config:
        env_prefix = "DB_"
        extra = "ignore"


class MIDISettings(BaseSettings):
    """MIDI 생성 설정"""
    
    # 출력 디렉토리
    output_dir: str = Field("output/midi", env="MIDI_OUTPUT_DIR")
    generated_modules_dir: str = Field("generated_modules", env="GENERATED_MODULES_DIR")
    snippets_library_dir: str = Field("my_snippets", env="SNIPPETS_LIBRARY_DIR")
    
    # MIDI 설정
    ticks_per_quarter: int = Field(480, env="MIDI_TICKS_PER_QUARTER")
    default_velocity: int = Field(80, env="MIDI_DEFAULT_VELOCITY")
    
    # 오디오 미리보기 설정
    generate_preview: bool = Field(True, env="GENERATE_PREVIEW")
    preview_format: str = Field("wav", env="PREVIEW_FORMAT")
    sample_rate: int = Field(44100, env="PREVIEW_SAMPLE_RATE")
    
    @validator('ticks_per_quarter')
    def validate_ticks(cls, v):
        """MIDI 해상도 유효성 검사"""
        valid_ticks = [120, 240, 480, 960]
        if v not in valid_ticks:
            raise ValueError(f'ticks_per_quarter는 {valid_ticks} 중 하나여야 합니다')
        return v
    
    @validator('default_velocity')
    def validate_velocity(cls, v):
        """벨로시티 유효성 검사"""
        if not 1 <= v <= 127:
            raise ValueError('velocity는 1-127 사이여야 합니다')
        return v

    class Config:
        extra = "ignore"


class LoggingSettings(BaseSettings):
    """로깅 설정"""
    
    log_level: str = Field("INFO", env="LOG_LEVEL")
    log_file: str = Field("logs/ai_songwriting.log", env="LOG_FILE")
    log_format: str = Field(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        env="LOG_FORMAT"
    )
    
    @validator('log_level')
    def validate_log_level(cls, v):
        """로그 레벨 유효성 검사"""
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if v.upper() not in valid_levels:
            raise ValueError(f'log_level은 {valid_levels} 중 하나여야 합니다')
        return v.upper()

    class Config:
        extra = "ignore"


class Settings(BaseSettings):
    """전체 애플리케이션 설정"""
    
    # 프로젝트 정보
    project_name: str = "AI MIDI 생성 시스템"
    version: str = "1.0.0"
    debug: bool = Field(False, env="DEBUG")
    
    # 서브 설정들
    llm: LLMProviderSettings = LLMProviderSettings()
    database: DatabaseSettings = DatabaseSettings()
    midi: MIDISettings = MIDISettings()
    logging: LoggingSettings = LoggingSettings()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._ensure_directories()
    
    def _ensure_directories(self):
        """필요한 디렉토리들을 생성"""
        directories = [
            self.midi.output_dir,
            self.midi.generated_modules_dir,
            self.midi.snippets_library_dir,
            os.path.dirname(self.logging.log_file),
            "data",
            "temp"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def get_model_config(self, provider: Optional[str] = None) -> Dict[str, Any]:
        """특정 프로바이더의 모델 설정 반환"""
        provider = provider or self.llm.default_provider
        
        config = {
            "provider": provider,
            "max_tokens": self.llm.max_tokens,
            "temperature": self.llm.temperature,
            "api_key": self.llm.get_api_key(provider)
        }
        
        if provider == "exaone":
            config["base_url"] = self.llm.exaone_base_url
        elif provider == "openai":
            config["base_url"] = self.llm.openai_base_url
        
        return config
    
    def validate_setup(self) -> Dict[str, Any]:
        """설정 유효성 검사 및 상태 반환"""
        status = {
            "valid": True,
            "errors": [],
            "warnings": [],
            "available_providers": self.llm.get_available_providers()
        }
        
        # LLM Provider 검사
        if not status["available_providers"]:
            status["valid"] = False
            status["errors"].append("사용 가능한 LLM Provider가 없습니다. API 키를 확인하세요.")
        
        if self.llm.default_provider not in status["available_providers"]:
            status["warnings"].append(
                f"기본 프로바이더 '{self.llm.default_provider}'를 사용할 수 없습니다. "
                f"사용 가능한 프로바이더: {status['available_providers']}"
            )
        
        # 디렉토리 검사
        try:
            self._ensure_directories()
        except Exception as e:
            status["valid"] = False
            status["errors"].append(f"디렉토리 생성 실패: {e}")
        
        return status
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


# 전역 설정 인스턴스
settings = Settings()


def get_settings() -> Settings:
    """설정 인스턴스 반환 (의존성 주입용)"""
    return settings


def reload_settings() -> Settings:
    """설정 재로드"""
    global settings
    settings = Settings()
    return settings 