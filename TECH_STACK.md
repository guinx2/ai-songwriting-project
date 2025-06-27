# 🎵 AI MIDI 생성 시스템 - 기술 스택 문서

## 📋 문서 개요
이 문서는 AI MIDI 생성 시스템의 전체 기술 스택과 아키텍처를 상세히 설명합니다. **고품질 MIDI 생성**에 집중한 실용적 솔루션의 기술적 구현을 다룹니다.

**마지막 업데이트**: 2024년 12월  
**프로젝트 단계**: Phase 1 - 핵심 아키텍처 구축 (Task 1 진행 중)  
**아키텍처**: 3단계 12개 태스크 기반 모듈식 구조

---

## 🏗️ 시스템 아키텍처 (3단계 구조)

### 전체 시스템 구조
```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        🎵 AI MIDI 생성 시스템                                   │
│                   자연어 프롬프트 → 4마디 MIDI 스니펫                           │
│                      (모듈식 레고 블록 작곡 시스템)                              │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ 🏗️ Phase 1      │     │ 🧩 Phase 2      │     │ 🚀 Phase 3      │
│ 핵심 아키텍처    │     │ 스니펫 관리 &   │     │ 최적화 &        │
│ (Tasks 1-5)     │     │ 개인화          │     │ 인터페이스      │
│                 │     │ (Tasks 6-10)    │     │ (Tasks 11-12)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

### 🏗️ Phase 1: 핵심 아키텍처 (Tasks 1-5)
```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           🏗️ 핵심 MIDI 생성 파이프라인                          │
│                                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐                 │
│  │   Task 1        │  │   Task 2        │  │   Task 3        │                 │
│  │ 핵심 아키텍처   │  │ 프롬프트 엔진   │  │ 데이터베이스    │                 │
│  │ & LLM Provider  │  │ & 파라미터      │  │ & 장르 시스템   │                 │
│  │                 │  │                 │  │                 │                 │
│  │ • 프로젝트 구조 │  │ • 자연어 분석   │  │ • SQLite 스키마 │                 │
│  │ • LLM 추상화    │  │ • 파라미터 추출 │  │ • 3단계 장르    │                 │
│  │ • 설정 관리     │  │ • 구조화 출력   │  │ • 아티스트 DB   │                 │
│  │ • 테스트 시스템 │  │ • 캐싱 시스템   │  │ • 메타데이터    │                 │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘                 │
│           │                      │                      │                      │
│           └──────────────────────┼──────────────────────┘                      │
│                                  ▼                                             │
│          ┌─────────────────┐  ┌─────────────────┐                             │
│          │   Task 4        │  │   Task 5        │                             │
│          │ 핵심 MIDI       │  │ MIDI 확장       │                             │
│          │ 생성 엔진       │  │ (다중 악기)     │                             │
│          │                 │  │                 │                             │
│          │ • 드럼 생성     │  │ • 베이스 라인   │                             │
│          │ • MIDI 출력     │  │ • 화성 악기     │                             │
│          │ • 4마디 구조    │  │ • 멜로디/리드   │                             │
│          │ • 품질 검증     │  │ • 멀티트랙 조화 │                             │
│          └─────────────────┘  └─────────────────┘                             │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 🔄 데이터 플로우
```
[자연어 프롬프트] → [LLM Provider] → [프롬프트 분석] → [MusicParams 생성]
                        ↓
[장르 시스템] → [아티스트 스타일] → [MIDI 생성 엔진] → [4마디 스니펫]
                        ↓
[품질 검증] → [메타데이터 생성] → [스니펫 저장] → [사용자 평가]
                        ↓
[스니펫 라이브러리] → [곡 구성 시스템] → [완성된 MIDI 출력]
```

---

## 🚀 현재 구현 상태

### ✅ 완료된 구성요소 (Task 1 - 40% 완료)
| 구성요소 | 상태 | 완성도 | 구현 내용 |
|----------|------|--------|-----------|
| **프로젝트 구조** | ✅ 완료 | 100% | src/ 디렉토리 구조, 모듈 분리 |
| **의존성 관리** | ✅ 완료 | 100% | requirements.txt, LLM Provider 라이브러리 |
| **MusicParams 모델** | ✅ 완료 | 100% | Pydantic 기반 데이터 구조 |
| **Settings 시스템** | ✅ 완료 | 100% | 다중 LLM Provider 설정 |
| **환경 설정** | ✅ 완료 | 100% | .env 템플릿, API 키 관리 |

### 🔄 진행 중인 구성요소
| 구성요소 | 진행률 | 다음 단계 | 예상 완료 |
|----------|--------|-----------|-----------|
| **Abstract LLMProvider** | 0% | 기본 클래스 구현 | Task 1.3 |
| **구체 Provider 클래스** | 0% | Claude, OpenAI, EXAONE | Task 1.4 |
| **Provider 팩토리** | 0% | 팩토리 패턴 구현 | Task 1.5 |

### ⏳ 계획된 구성요소 (우선순위별)
1. **🔥 최우선**: Tasks 2-5 (기본 MIDI 생성 파이프라인)
2. **🧩 중우선**: Tasks 6-10 (스니펫 관리 & 개인화)
3. **🚀 최종**: Tasks 11-12 (최적화 & 인터페이스)

---

## 🔧 핵심 기술 스택

### 1. 프로그래밍 언어 및 런타임
| 기술 | 버전 | 현재 상태 | 활용 분야 | 구현 Task |
|------|------|-----------|-----------|-----------|
| **Python** | 3.11+ | ✅ 설정 완료 | 모든 백엔드 로직, AI 처리 | All Tasks |
| **pip/venv** | 표준 | ✅ 설정 완료 | 패키지 관리, 가상환경 | 개발 환경 |

### 2. AI/LLM 서비스 및 API
| 기술 | 버전 | 현재 상태 | 구현 기능 | 구현 Task |
|------|------|-----------|-----------|-----------|
| **Claude 3.5 Sonnet** | API | ✅ 설정 완료 | 고품질 프롬프트 분석 | Task 1, 2 |
| **EXAONE 3.5** | API | ✅ 설정 완료 | 한국어 특화, 비용 효율성 | Task 1, 2 |
| **OpenAI GPT-4** | API | ✅ 설정 완료 | 백업 및 비교 분석 | Task 1, 2 |
| **anthropic** | 0.34.0+ | ✅ 설치 완료 | Claude API 클라이언트 | Task 1.4 |
| **openai** | 1.40.0+ | ✅ 설치 완료 | OpenAI API 클라이언트 | Task 1.4 |
| **httpx** | 0.25.0+ | ✅ 설치 완료 | 비동기 HTTP 요청 | Task 1.4 |

### 3. 데이터 검증 및 구조화
| 기술 | 버전 | 현재 상태 | 구현 기능 | 구현 Task |
|------|------|-----------|-----------|-----------|
| **Pydantic** | 2.0+ | ✅ 설치 완료 | 데이터 모델, 검증 | Task 1.2 |
| **pydantic-settings** | 2.0+ | ✅ 설치 완료 | 설정 관리 | Task 1.2 |
| **tiktoken** | 0.5.0+ | ✅ 설치 완료 | 토큰 계산 | Task 2 |

### 4. MIDI 처리 및 음악 이론
| 기술 | 버전 | 현재 상태 | 구현 기능 | 구현 Task |
|------|------|-----------|-----------|-----------|
| **mido** | 1.3+ | 📦 설치 예정 | MIDI 파일 생성/편집 | Task 4, 5 |
| **pretty_midi** | 0.2.10+ | 📦 설치 예정 | 고급 MIDI 조작 | Task 4, 5 |
| **music21** | 9.1+ | 📦 설치 예정 | 음악 이론 분석 | Task 4, 5 |

### 5. 데이터베이스 및 저장소
| 기술 | 버전 | 현재 상태 | 활용 분야 | 구현 Task |
|------|------|-----------|-----------|-----------|
| **SQLite** | 3.40+ | 📦 설치 예정 | 장르 시스템, 아티스트 DB | Task 3 |
| **Redis** | 7.0+ | 📦 설치 예정 | 프롬프트 캐싱 | Task 2, 11 |
| **JSON** | 표준 | ✅ 사용 중 | 메타데이터, 설정 | All Tasks |

### 6. 웹 프레임워크 및 API (Phase 3)
| 기술 | 버전 | 현재 상태 | 구현 기능 | 구현 Task |
|------|------|-----------|-----------|-----------|
| **FastAPI** | 0.100+ | 📋 계획됨 | REST API 서버 | Task 12 |
| **React** | 18+ | 📋 계획됨 | 웹 UI 인터페이스 | Task 12 |
| **WebSocket** | - | 📋 계획됨 | 실시간 진행률 | Task 12 |

### 7. 테스팅 및 개발 도구
| 기술 | 버전 | 현재 상태 | 활용 분야 | 구현 Task |
|------|------|-----------|-----------|-----------|
| **pytest** | 7.0+ | 📦 설치 예정 | 단위 테스트 | Task 1.5 |
| **black** | 23.0+ | 📦 설치 예정 | 코드 포맷팅 | 개발 환경 |
| **mypy** | 1.0+ | 📦 설치 예정 | 타입 검사 | 개발 환경 |

---

## 📊 아키텍처 세부사항

### 1. LLM Provider 아키텍처 (Task 1)
```python
# 추상화 구조
class LLMProvider(ABC):
    @abstractmethod
    async def analyze_prompt(self, prompt: str) -> MusicParams:
        pass
    
    @abstractmethod
    async def generate_description(self, params: MusicParams) -> str:
        pass

# 구체 구현
class ClaudeProvider(LLMProvider):
    # Claude 3.5 Sonnet 특화 구현
    
class ExaoneProvider(LLMProvider):
    # EXAONE 3.5 특화 구현
    
class OpenAIProvider(LLMProvider):
    # GPT-4 특화 구현
```

### 2. 데이터 모델 구조 (Task 1.2)
```python
@dataclass
class MusicParams:
    # 핵심 식별자
    instrument: Instrument
    song_part: SongPart
    
    # 3단계 장르 시스템
    genre: str              # 메인 장르 (hip_hop, rock, electronic)
    sub_genre: str          # 세부 장르 (trap, boom_bap, drill)
    style_variant: str      # 스타일 변형 (melodic_trap, old_school_boom_bap)
    
    # 아티스트 기반 생성
    artist_reference: Optional[str] = None
    country: Optional[str] = None
    
    # 음악적 특성
    mood: str
    tempo: int              # 60-200 BPM
    key: str               # C_major, A_minor, etc.
    time_signature: str    # 4/4, 3/4, 6/8, etc.
    
    # 생성 제어
    complexity: Complexity
    energy_level: EnergyLevel
    duration: Duration      # 4_bars, 8_bars, 16_bars
```

### 3. 장르 계층 시스템 (Task 3)
```sql
-- 3단계 장르 계층 구조
CREATE TABLE genres (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    parent_id INTEGER,
    level INTEGER,  -- 1=메인, 2=세부, 3=스타일
    characteristics JSON,
    FOREIGN KEY (parent_id) REFERENCES genres(id)
);

-- 예시 데이터
INSERT INTO genres (name, parent_id, level) VALUES
('hip_hop', NULL, 1),
('trap', 1, 2),
('melodic_trap', 2, 3),
('hard_trap', 2, 3);
```

### 4. MIDI 생성 엔진 (Task 4, 5)
```python
class MIDIGenerator:
    def __init__(self, genre_system: GenreSystem):
        self.genre_system = genre_system
        
    async def generate_drums(self, params: MusicParams) -> MIDITrack:
        # 장르별 드럼 패턴 생성
        
    async def generate_bass(self, params: MusicParams) -> MIDITrack:
        # 베이스 라인 생성
        
    async def generate_harmony(self, params: MusicParams) -> MIDITrack:
        # 화성 악기 생성 (피아노, 기타, 신스)
        
    async def generate_melody(self, params: MusicParams) -> MIDITrack:
        # 멜로디 및 리드 생성
```

---

## 🎯 성능 및 품질 목표

### 성능 지표
| 지표 | 목표 값 | 현재 상태 | 측정 방법 |
|------|---------|-----------|-----------|
| **프롬프트 분석 시간** | < 5초 | 미측정 | API 응답 시간 |
| **4마디 MIDI 생성** | < 30초 | 미측정 | 생성 완료 시간 |
| **API 성공률** | > 95% | 미측정 | 성공/실패 비율 |
| **메모리 사용량** | < 1GB | 미측정 | 시스템 모니터링 |

### 품질 지표
| 지표 | 목표 값 | 현재 상태 | 측정 방법 |
|------|---------|-----------|-----------|
| **장르 정확도** | > 85% | 미측정 | 사용자 평가 |
| **프롬프트 반영률** | > 90% | 미측정 | 파라미터 일치도 |
| **MIDI 품질** | DAW 호환 | 미측정 | 호환성 테스트 |
| **코드 커버리지** | > 80% | 0% | pytest 측정 |

---

## 🔄 개발 워크플로우

### 1. 개발 환경 설정
```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 의존성 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
# API 키 설정 필요
```

### 2. 테스트 실행
```bash
# 단위 테스트
pytest tests/

# 타입 검사
mypy src/

# 코드 포맷팅
black src/
```

### 3. 개발 프로세스
1. **기능 구현**: Task 단위로 개발
2. **테스트 작성**: 단위 테스트 및 통합 테스트
3. **코드 리뷰**: 품질 검증
4. **문서 업데이트**: 기술 문서 동기화

---

## 🚧 기술적 과제 및 해결 방안

### 1. LLM API 비용 최적화
**과제**: 대량의 프롬프트 처리 시 API 비용 증가
**해결방안**:
- Redis 기반 프롬프트 캐싱
- 효율적인 프롬프트 엔지니어링
- 모델별 비용 분석 및 최적 선택

### 2. MIDI 품질 일관성
**과제**: 장르별 음악적 특성 정확한 반영
**해결방안**:
- 음악 이론 규칙 엔진 구축
- 장르별 특화 알고리즘 개발
- 사용자 피드백 기반 품질 개선

### 3. 확장성 및 성능
**과제**: 다중 사용자 및 대량 요청 처리
**해결방안**:
- 비동기 처리 구조
- 캐싱 시스템 활용
- 모듈식 아키텍처로 확장성 확보

### 4. 데이터 품질 관리
**과제**: 아티스트 스타일 및 장르 데이터 정확성
**해결방안**:
- 수동 검증 시스템 구축
- 품질 점수 시스템 도입
- 지속적인 데이터 큐레이션

---

## 📚 외부 의존성 및 서비스

### AI/LLM 서비스
| 서비스 | 용도 | 비용 모델 | 백업 계획 |
|--------|------|-----------|-----------|
| **Claude 3.5 Sonnet** | 주요 프롬프트 분석 | 토큰 기반 | OpenAI GPT-4 |
| **EXAONE 3.5** | 한국어 특화 | 토큰 기반 | Claude |
| **OpenAI GPT-4** | 백업 및 비교 | 토큰 기반 | Claude |

### 인프라 서비스 (향후)
| 서비스 | 용도 | 현재 상태 | 구현 시기 |
|--------|------|-----------|-----------|
| **AWS S3** | MIDI 파일 저장 | 계획됨 | Phase 3 |
| **Redis Cloud** | 캐싱 서비스 | 계획됨 | Phase 2 |
| **PostgreSQL** | 프로덕션 DB | 계획됨 | Phase 3 |

---

## 🔍 모니터링 및 로깅

### 로깅 전략
```python
# 구조화된 로깅
import logging
import structlog

logger = structlog.get_logger()

# 사용 예시
logger.info("prompt_analyzed", 
           prompt_length=len(prompt),
           genre=params.genre,
           processing_time=elapsed_time)
```

### 메트릭 수집 (Phase 3)
- **성능 메트릭**: 응답 시간, 처리량
- **품질 메트릭**: 생성 성공률, 사용자 만족도
- **비용 메트릭**: API 호출 비용, 리소스 사용량

---

## 🎯 다음 단계 기술 구현

### 즉시 구현 (Task 1.3)
```python
# Abstract LLMProvider 기본 클래스
from abc import ABC, abstractmethod
from typing import Optional

class LLMProvider(ABC):
    def __init__(self, api_key: str, model_name: str):
        self.api_key = api_key
        self.model_name = model_name
    
    @abstractmethod
    async def analyze_prompt(self, prompt: str) -> MusicParams:
        """자연어 프롬프트를 MusicParams로 변환"""
        pass
    
    @abstractmethod
    async def generate_title(self, params: MusicParams) -> str:
        """음악 파라미터 기반 곡 제목 생성"""
        pass
    
    @abstractmethod
    def estimate_cost(self, prompt: str) -> float:
        """API 호출 비용 추정"""
        pass
```

### 단기 구현 (Task 1.4)
- Claude, OpenAI, EXAONE Provider 구체 클래스
- 각 Provider별 특화 프롬프트 템플릿
- 에러 처리 및 재시도 로직

### 중기 구현 (Task 2-5)
- 프롬프트 엔지니어링 엔진
- 장르 계층 시스템
- 기본 MIDI 생성 엔진

---

*마지막 업데이트: 2024년 12월*  
*현재 진행률: Phase 1 - Task 1 (40% 완료)*  
*다음 구현: Abstract LLMProvider 기본 클래스 (Task 1.3)* 