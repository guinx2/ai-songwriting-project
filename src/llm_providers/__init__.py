"""
LLM Providers 모듈

다양한 LLM Provider (Claude, OpenAI, EXAONE)를 위한 통합 인터페이스를 제공합니다.
추상 기본 클래스와 팩토리 패턴을 통해 일관된 API를 제공합니다.

사용 예시:
    # 팩토리를 통한 Provider 생성
    from src.llm_providers import get_factory, ProviderType
    
    factory = get_factory()
    claude_provider = factory.get_provider(ProviderType.CLAUDE)
    
    # 프롬프트 분석
    params = await claude_provider.analyze_prompt("어두운 붐뱁 드럼 인트로")
    
    # 폴백 Provider 사용
    provider = factory.get_provider_with_fallback([
        ProviderType.CLAUDE, 
        ProviderType.EXAONE, 
        ProviderType.OPENAI
    ])
    
    # 기본 Provider 사용
    default_provider = factory.get_default_provider()
    
    # 비용 비교
    costs = factory.compare_providers("지코 스타일 트랩 랩")
"""

from .base import (
    LLMProvider,
    ProviderConfig,
    PromptTemplate,
    LLMProviderError,
    APIError,
    ParseError
)

from .claude_provider import ClaudeProvider
from .openai_provider import OpenAIProvider  
from .exaone_provider import ExaoneProvider

from .factory import (
    LLMProviderFactory,
    ProviderType,
    get_factory,
    reset_factory
)

# 주요 클래스들을 모듈 레벨에서 접근 가능하도록 export
__all__ = [
    # 기본 클래스들
    'LLMProvider',
    'ProviderConfig', 
    'PromptTemplate',
    
    # 에러 클래스들
    'LLMProviderError',
    'APIError',
    'ParseError',
    
    # 구체 Provider 클래스
    'ClaudeProvider',
    'OpenAIProvider',
    'ExaoneProvider',
    
    # 팩토리 관련
    'LLMProviderFactory',
    'ProviderType',
    'get_factory',
    'reset_factory',
    
    # 편의 함수들
    'create_provider',
    'get_default_provider',
    'analyze_prompt_with_fallback'
]

# 모듈 정보
__version__ = '1.0.0'
__author__ = 'AI MIDI Generation System'
__description__ = 'LLM Provider abstraction layer for music parameter extraction'

# 편의 함수들
def create_provider(
    provider_type: ProviderType, 
    settings=None
) -> LLMProvider:
    """
    Provider 인스턴스 생성을 위한 편의 함수
    
    Args:
        provider_type: 생성할 Provider 타입
        settings: 설정 객체 (선택사항)
        
    Returns:
        LLMProvider: 생성된 Provider 인스턴스
    """
    factory = get_factory(settings)
    return factory.get_provider(provider_type)


def get_default_provider(settings=None) -> LLMProvider:
    """
    기본 Provider 반환을 위한 편의 함수
    
    Args:
        settings: 설정 객체 (선택사항)
        
    Returns:
        LLMProvider: 기본 Provider 인스턴스
    """
    factory = get_factory(settings)
    return factory.get_default_provider()


async def analyze_prompt_with_fallback(
    prompt: str,
    provider_priority=None,
    settings=None
):
    """
    폴백을 지원하는 프롬프트 분석 편의 함수
    
    Args:
        prompt: 분석할 프롬프트
        provider_priority: Provider 우선순위 (선택사항)
        settings: 설정 객체 (선택사항)
        
    Returns:
        MusicParams: 분석된 음악 파라미터
        
    Raises:
        RuntimeError: 모든 Provider에서 실패한 경우
    """
    if provider_priority is None:
        provider_priority = [
            ProviderType.CLAUDE,
            ProviderType.EXAONE, 
            ProviderType.OPENAI
        ]
    
    factory = get_factory(settings)
    provider = factory.get_provider_with_fallback(provider_priority)
    
    return await provider.analyze_prompt(prompt)
