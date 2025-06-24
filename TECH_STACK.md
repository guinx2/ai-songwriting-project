# AI 작곡 시스템 기술 스택 문서

## 📋 문서 개요
이 문서는 AI 작곡 시스템의 전체 기술 스택과 아키텍처를 상세히 설명합니다. 각 기술 선택의 근거와 구현 세부사항을 포함합니다.

---

## 🏗️ 시스템 아키텍처

### 전체 시스템 구조
```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                Frontend Layer                                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐                 │
│  │   UI Components │  │  State Manager  │  │  Audio Player   │                 │
│  │     (React)     │  │ (Redux/Zustand) │  │   (Web Audio)   │                 │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │ HTTP/WebSocket
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                API Gateway                                      │
│                              (FastAPI Server)                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            ▼                       ▼                       ▼
    ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
    │ Song Creation │     │ Export System │     │ Project Mgmt  │
    │    Module     │     │    Module     │     │    Module     │
    └───────────────┘     └───────────────┘     └───────────────┘
            │                       │                       │
            ▼                       ▼                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              Core Engine Layer                                 │
│                                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐                 │
│  │   AI Models     │  │ MIDI Generation │  │ Music Theory    │                 │
│  │  (TensorFlow)   │  │     Engine      │  │     Engine      │                 │
│  │                 │  │                 │  │                 │                 │
│  │ • LSTM/RNN      │  │ • Pattern Gen   │  │ • Chord Prog    │                 │
│  │ • Transformer   │  │ • Rhythm Gen    │  │ • Scale Theory  │                 │
│  │ • VAE/GAN       │  │ • Melody Gen    │  │ • Harmony Rules │                 │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘                 │
│           │                      │                      │                      │
│           └──────────────────────┼──────────────────────┘                      │
│                                  ▼                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐                 │
│  │ Audio Processing│  │ File Management │  │    Utilities    │                 │
│  │     Engine      │  │     System      │  │     Module      │                 │
│  │                 │  │                 │  │                 │                 │
│  │ • Format Conv   │  │ • MIDI I/O      │  │ • Validation    │                 │
│  │ • Quality Ctrl  │  │ • Audio I/O     │  │ • Logging       │                 │
│  │ • Stem Export   │  │ • Project Pack  │  │ • Config Mgmt   │                 │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                            Data Persistence Layer                              │
│                                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐                 │
│  │   Database      │  │  File System    │  │   Cache Layer   │                 │
│  │   (SQLite)      │  │    Storage      │  │   (Memory)      │                 │
│  │                 │  │                 │  │                 │                 │
│  │ • Songs         │  │ • MIDI Files    │  │ • Generated     │                 │
│  │ • Artists       │  │ • Audio Files   │  │   Content       │                 │
│  │ • Tracks        │  │ • Project Files │  │ • User Sessions │                 │
│  │ • Metadata      │  │ • Export Pkgs   │  │ • Temp Data     │                 │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        Ableton Live Integration Layer                          │
│                                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐                 │
│  │   Live API      │  │ MIDI Connection │  │ Max for Live    │                 │
│  │   Interface     │  │     Manager     │  │   Interface     │                 │
│  │                 │  │                 │  │                 │                 │
│  │ • Project Ctrl  │  │ • Port Mgmt     │  │ • Real-time     │                 │
│  │ • Track Mgmt    │  │ • Message I/O   │  │   Control       │                 │
│  │ • Playback      │  │ • Event Listen  │  │ • Parameter     │                 │
│  │ • Tempo/Transport│ │ • Sync/Clock   │  │   Automation    │                 │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘                 │
│           │                      │                      │                      │
│           └──────────────────────┼──────────────────────┘                      │
│                                  ▼                                             │
│                        ┌─────────────────┐                                     │
│                        │ Ableton Live    │                                     │
│                        │   (External)    │                                     │
│                        │                 │                                     │
│                        │ • Live Set      │                                     │
│                        │ • Audio Engine  │                                     │
│                        │ • Effects/Instr │                                     │
│                        └─────────────────┘                                     │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 데이터 플로우 다이어그램
```
[사용자 입력] → [Frontend] → [API Gateway] → [AI Models]
                                    ↓
[Music Theory] ← [MIDI Generation] ← [AI Output]
      ↓
[MIDI Files] → [Audio Processing] → [Export System]
      ↓                                    ↓
[Database] ← [File System] ← [Project Package]
      ↓
[Ableton Live] ← [MIDI Connection] ← [Live API]
```

---

## 🔧 백엔드 기술 스택

### 1. 핵심 언어 및 런타임
| 기술 | 버전 | 선택 이유 | 활용 분야 |
|------|------|-----------|-----------|
| **Python** | 3.12+ | AI/ML 생태계 풍부, 음악 처리 라이브러리 완성도 | 모든 백엔드 로직, AI 모델, 데이터 처리 |
| **Node.js** | 18+ (보조) | WebSocket 실시간 통신, npm 패키지 활용 | 실시간 통신 서버, 보조 스크립트 |

### 2. 웹 프레임워크 및 API
| 기술 | 버전 | 선택 이유 | 구현 기능 |
|------|------|-----------|-----------|
| **FastAPI** | 0.100+ | 고성능, 자동 문서화, 타입 힌트 지원 | REST API, WebSocket, 자동 검증 |
| **Uvicorn** | 0.22+ | ASGI 서버, 고성능 비동기 처리 | 프로덕션 서버 |
| **Pydantic** | 2.0+ | 데이터 검증, 직렬화, 타입 안전성 | API 스키마, 데이터 모델 |

### 3. 데이터베이스 및 ORM
| 기술 | 버전 | 선택 이유 | 활용 분야 |
|------|------|-----------|-----------|
| **SQLite** | 3.40+ | 파일 기반, 설치 불필요, 개발 편의성 | 곡/아티스트/트랙 메타데이터 |
| **SQLAlchemy** | 2.0+ | ORM 완성도, 타입 힌트 지원 | 데이터베이스 추상화 |
| **Alembic** | 1.11+ | 데이터베이스 마이그레이션 | 스키마 버전 관리 |

### 4. AI/ML 및 수치 연산
| 기술 | 버전 | 선택 이유 | 구현 기능 |
|------|------|-----------|-----------|
| **NumPy** | 1.24+ | 고성능 수치 연산, 배열 처리 | MIDI 데이터 처리, 신호 처리 |
| **SciPy** | 1.10+ | 과학 연산, 신호 처리 알고리즘 | 오디오 분석, 수학적 변환 |
| **TensorFlow** | 2.13+ | 음악 생성 모델 풍부, 안정성 | LSTM MIDI 생성, 멜로디 생성 |
| **PyTorch** | 2.0+ | 동적 그래프, 연구 친화적 | 실험적 모델, 커스텀 아키텍처 |
| **scikit-learn** | 1.3+ | 전통적 ML 알고리즘 | 패턴 분석, 클러스터링 |

### 5. MIDI 및 오디오 처리
| 기술 | 버전 | 선택 이유 | 구현 기능 |
|------|------|-----------|-----------|
| **python-rtmidi** | 1.5+ | 실시간 MIDI I/O, 크로스 플랫폼 | Ableton Live 실시간 통신 |
| **mido** | 1.3+ | MIDI 파일 처리, 메시지 파싱 | MIDI 파일 생성/편집 |
| **soundfile** | 0.12+ | 오디오 파일 I/O, 다양한 포맷 지원 | WAV/FLAC/MP3 파일 처리 |
| **librosa** | 0.10+ | 오디오 분석, 특성 추출 | 스펙트럼 분석, 템포 추출 |
| **pretty_midi** | 0.2.10+ | MIDI 데이터 구조화, 시각화 | 고급 MIDI 조작 |

### 6. 비동기 처리 및 통신
| 기술 | 버전 | 선택 이유 | 구현 기능 |
|------|------|-----------|-----------|
| **asyncio** | 표준 라이브러리 | 네이티브 비동기 지원 | 비동기 API, 실시간 처리 |
| **aiofiles** | 23.1+ | 비동기 파일 I/O | 대용량 파일 처리 |
| **websockets** | 11.0+ | 실시간 양방향 통신 | 브라우저-서버 실시간 연동 |

---

## 🎨 프론트엔드 기술 스택 (계획)

### 1. 핵심 프레임워크
| 기술 | 버전 | 선택 이유 | 구현 기능 |
|------|------|-----------|-----------|
| **TypeScript** | 5.1+ | 타입 안전성, 대규모 프로젝트 유지보수 | 모든 프론트엔드 코드 |
| **React** | 18+ | 컴포넌트 기반, 생태계 완성도 | UI 컴포넌트, 상태 관리 |
| **Vite** | 4.4+ | 빠른 번들링, ES 모듈 지원 | 개발 서버, 빌드 도구 |

### 2. 상태 관리 및 데이터
| 기술 | 버전 | 선택 이유 | 구현 기능 |
|------|------|-----------|-----------|
| **Zustand** | 4.3+ | 경량, 간단한 API | 글로벌 상태 관리 |
| **TanStack Query** | 4.29+ | 서버 상태 관리, 캐싱 | API 데이터 관리 |
| **React Hook Form** | 7.45+ | 성능 최적화된 폼 관리 | 사용자 입력 처리 |

### 3. UI 및 스타일링
| 기술 | 버전 | 선택 이유 | 구현 기능 |
|------|------|-----------|-----------|
| **Tailwind CSS** | 3.3+ | 유틸리티 우선, 빠른 스타일링 | 전체 UI 스타일링 |
| **Headless UI** | 1.7+ | 접근성 준수 컴포넌트 | 고급 UI 컴포넌트 |
| **Framer Motion** | 10.12+ | 고성능 애니메이션 | UI 애니메이션, 전환 |

### 4. 오디오 및 시각화
| 기술 | 버전 | 선택 이유 | 구현 기능 |
|------|------|-----------|-----------|
| **Tone.js** | 14.7+ | 웹 오디오 라이브러리 | 브라우저 오디오 재생 |
| **Web Audio API** | 네이티브 | 고성능 오디오 처리 | 실시간 오디오 처리 |
| **D3.js** | 7.8+ | 데이터 시각화 | 음악 데이터 차트 |

---

## 🔗 Ableton Live 연동 시스템

### 1. 연동 프로토콜
| 프로토콜 | 용도 | 구현 방식 | 성능 특성 |
|----------|------|-----------|-----------|
| **Live API** | 프로젝트 제어 | TCP Socket | 안정성 높음 |
| **MIDI** | 실시간 음악 데이터 | MIDI over USB/Network | 저지연 |
| **OSC** | 파라미터 제어 | UDP Socket | 고성능 |
| **Max for Live** | 고급 통합 | TCP/UDP Socket | 최고 유연성 |

### 2. 통신 아키텍처
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Python API    │◄──►│ MIDI Connection │◄──►│ Ableton Live    │
│   (FastAPI)     │    │    Manager      │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Live API       │    │ MIDI Message    │    │ Max for Live    │
│  Interface      │    │   Processing    │    │   Scripts       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 🗄️ 데이터베이스 설계

### 1. 스키마 구조
```sql
-- 아티스트 테이블
CREATE TABLE artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    genre_preferences TEXT, -- JSON 배열
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 장르 테이블
CREATE TABLE genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    tempo_range TEXT, -- "120-140"
    key_signatures TEXT, -- JSON 배열
    characteristics TEXT, -- JSON 객체
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 곡 테이블
CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist_id INTEGER REFERENCES artists(id) ON DELETE SET NULL,
    genre_id INTEGER REFERENCES genres(id) ON DELETE SET NULL,
    bpm INTEGER DEFAULT 120 CHECK (bpm BETWEEN 60 AND 200),
    key_signature TEXT DEFAULT 'C',
    time_signature TEXT DEFAULT '4/4',
    duration REAL CHECK (duration > 0),
    midi_data TEXT, -- Base64 encoded MIDI
    audio_file_path TEXT,
    project_file_path TEXT,
    lyrics TEXT,
    metadata TEXT, -- JSON 객체
    ai_generated BOOLEAN DEFAULT FALSE,
    generation_prompt TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 트랙 테이블
CREATE TABLE tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER NOT NULL REFERENCES songs(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    instrument TEXT,
    midi_channel INTEGER CHECK (midi_channel BETWEEN 1 AND 16),
    audio_file_path TEXT,
    volume REAL DEFAULT 1.0 CHECK (volume BETWEEN 0.0 AND 2.0),
    pan REAL DEFAULT 0.0 CHECK (pan BETWEEN -1.0 AND 1.0),
    muted BOOLEAN DEFAULT FALSE,
    soloed BOOLEAN DEFAULT FALSE,
    track_order INTEGER DEFAULT 0,
    effects_chain TEXT, -- JSON 배열
    automation_data TEXT, -- JSON 객체
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 프로젝트 설정 테이블
CREATE TABLE project_settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER UNIQUE REFERENCES songs(id) ON DELETE CASCADE,
    master_volume REAL DEFAULT 1.0,
    master_effects TEXT, -- JSON 배열
    ableton_project_path TEXT,
    export_settings TEXT, -- JSON 객체
    collaboration_settings TEXT, -- JSON 객체
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. 인덱싱 전략
```sql
-- 성능 최적화를 위한 인덱스
CREATE INDEX idx_songs_artist_genre ON songs(artist_id, genre_id);
CREATE INDEX idx_songs_created_at ON songs(created_at);
CREATE INDEX idx_tracks_song_id ON tracks(song_id);
CREATE INDEX idx_tracks_order ON tracks(song_id, track_order);
CREATE INDEX idx_songs_ai_generated ON songs(ai_generated);
```

---

## 🛠️ 개발 도구 및 환경

### 1. 패키지 관리 및 환경
| 도구 | 용도 | 설정 파일 |
|------|------|-----------|
| **pip** | Python 패키지 관리 | `requirements.txt` |
| **venv** | 가상환경 격리 | `venv/` |
| **npm** | Node.js 패키지 관리 | `package.json` |

### 2. 코드 품질 및 린팅
| 도구 | 버전 | 용도 | 설정 파일 |
|------|------|------|-----------|
| **Black** | 23.3+ | 코드 포매팅 | `pyproject.toml` |
| **isort** | 5.12+ | import 정렬 | `pyproject.toml` |
| **flake8** | 6.0+ | 린팅 | `.flake8` |
| **mypy** | 1.4+ | 정적 타입 검사 | `mypy.ini` |
| **pre-commit** | 3.3+ | Git 훅 자동화 | `.pre-commit-config.yaml` |

### 3. 테스트 프레임워크
| 도구 | 버전 | 용도 | 특징 |
|------|------|------|------|
| **pytest** | 7.4+ | 단위/통합 테스트 | 픽스처, 파라미터화 |
| **pytest-asyncio** | 0.21+ | 비동기 코드 테스트 | async/await 지원 |
| **httpx** | 0.24+ | HTTP 클라이언트 테스트 | FastAPI 테스트 |
| **pytest-cov** | 4.1+ | 테스트 커버리지 | 코드 커버리지 분석 |

### 4. 개발 환경 설정
```bash
# 개발 환경 설정 스크립트
#!/bin/bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
```

---

## 🚀 배포 및 인프라 (계획)

### 1. 컨테이너화
```dockerfile
# Dockerfile 예시
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2. 배포 환경
| 환경 | 플랫폼 | 용도 | 특징 |
|------|--------|------|------|
| **개발** | 로컬 | 개발/테스트 | Hot reload, 디버깅 |
| **스테이징** | Docker | 통합 테스트 | 프로덕션 환경 시뮬레이션 |
| **프로덕션** | AWS/GCP | 실제 서비스 | 고가용성, 모니터링 |

---

## 🔒 보안 및 성능

### 1. 보안 고려사항
| 영역 | 기술/방법 | 구현 내용 |
|------|-----------|-----------|
| **인증** | JWT | 토큰 기반 사용자 인증 |
| **CORS** | FastAPI CORS | 교차 출처 요청 제어 |
| **Rate Limiting** | slowapi | API 남용 방지 |
| **데이터 암호화** | cryptography | 민감 데이터 암호화 |
| **환경 변수** | python-dotenv | 민감 정보 분리 |

### 2. 성능 최적화
| 영역 | 방법 | 예상 효과 |
|------|------|-----------|
| **비동기 처리** | asyncio, FastAPI | 동시 요청 처리 |
| **데이터베이스** | 인덱싱, 쿼리 최적화 | 조회 성능 향상 |
| **캐싱** | Redis (선택사항) | 응답 속도 개선 |
| **CDN** | CloudFront (선택사항) | 정적 자원 배송 |

---

## 📊 모니터링 및 로깅

### 1. 로깅 시스템
```python
# 로깅 설정 예시
import logging
from pythonjsonlogger import jsonlogger

# 구조화된 로깅
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)
```

### 2. 메트릭 수집 (계획)
| 메트릭 | 도구 | 용도 |
|--------|------|------|
| **응답 시간** | Prometheus | API 성능 모니터링 |
| **에러율** | Sentry | 오류 추적 |
| **리소스 사용량** | Grafana | 시스템 리소스 모니터링 |

---

## 🔧 확장성 고려사항

### 1. 수평 확장
- **마이크로서비스**: 기능별 서비스 분리 가능
- **로드 밸런싱**: Nginx, HAProxy 활용
- **데이터베이스 샤딩**: 사용자별 데이터 분할

### 2. 수직 확장
- **메모리 최적화**: 대용량 MIDI 데이터 스트리밍
- **CPU 최적화**: AI 모델 추론 최적화
- **스토리지 최적화**: 오디오 파일 압축

---

## 📚 라이센스 및 의존성

### 1. 오픈소스 라이센스
- **프로젝트 라이센스**: MIT License
- **의존성 라이센스**: 각 패키지별 라이센스 준수 필요

### 2. 상용 소프트웨어
- **Ableton Live**: 사용자 개별 라이센스 필요
- **Max for Live**: Ableton Live Suite 포함

---

## 📈 개발 방법론

### 1. 개발 프로세스
- **애자일 방법론**: 2주 스프린트
- **테스트 주도 개발**: 핵심 기능에 TDD 적용
- **지속적 통합**: GitHub Actions

### 2. 코드 리뷰
- **Pull Request**: 모든 변경사항 리뷰
- **자동화된 검사**: 린팅, 테스트, 보안 스캔

---

**📅 마지막 업데이트**: 2024-06-24  
**👥 작성자**: AI 시스템 개발팀  
**🔄 다음 리뷰**: 주요 기술 스택 변경 시 