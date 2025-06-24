# 🛠️ AI 작곡 시스템 기술 스택 & 아키텍처

## 🏗️ 시스템 아키텍처

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React 웹앱    │    │   Ableton Live  │    │  Max for Live   │
│  (프론트엔드)   │◄──►│      (DAW)      │◄──►│   (디바이스)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        ▲                        ▲
         │ HTTP API               │ MIDI                   │
         ▼                        │                        │
┌─────────────────┐               │                        │
│  FastAPI 서버   │───────────────┘                        │
│   (백엔드)      │                                        │
└─────────────────┘                                        │
         │                                                 │
         │                                                 │
┌─────────────────┐    ┌─────────────────┐                │
│ AI 모델 엔진    │    │   데이터베이스   │                │
│ (음악 생성)     │    │   (SQLite)     │                │
└─────────────────┘    └─────────────────┘                │
         │                        │                        │
         │                        │                        │
┌─────────────────┐    ┌─────────────────┐                │
│ MIDI 처리 모듈  │    │   파일 저장소   │                │
│ (music21/mido)  │    │ (MIDI/Audio)   │◄───────────────┘
└─────────────────┘    └─────────────────┘
```

---

## 🐍 **백엔드 (Python)**

### **웹 프레임워크**
- **FastAPI 0.115+**: 현대적인 고성능 웹 API 프레임워크
- **Uvicorn**: ASGI 서버 (비동기 처리)
- **Pydantic**: 데이터 검증 및 직렬화

### **데이터베이스**
- **SQLAlchemy 2.0+**: Python ORM
- **Alembic**: 데이터베이스 마이그레이션
- **SQLite**: 개발용 (→ PostgreSQL 배포시)

### **AI/ML 프레임워크**
```python
# 핵심 AI 라이브러리
tensorflow>=2.15.0      # Google의 머신러닝 프레임워크
torch>=2.1.0           # PyTorch 딥러닝 프레임워크
transformers>=4.35.0   # Hugging Face 모델 라이브러리
numpy>=1.24.0          # 수치 연산
scikit-learn>=1.3.0    # 머신러닝 알고리즘
```

### **음악 처리 라이브러리**
```python
# MIDI 및 음악 처리
music21>=9.1.0         # MIT의 음악 분석 툴킷
librosa>=0.10.1        # 오디오 분석 라이브러리
mido>=1.3.0            # MIDI 파일 처리
pretty_midi>=0.2.10    # MIDI 데이터 조작
python-rtmidi>=1.5.0   # 실시간 MIDI I/O
```

### **오디오 처리**
```python
# 오디오 신호 처리
soundfile>=0.12.0      # 오디오 파일 읽기/쓰기
audioread>=3.0.0       # 다양한 오디오 포맷 지원
resampy>=0.4.0         # 오디오 리샘플링
pyFluidSynth>=1.3.0    # 소프트웨어 신디사이저
```

---

## ⚛️ **프론트엔드 (React)**

### **핵심 프레임워크**
```json
{
  "react": "^18.2.0",
  "typescript": "^5.0.0",
  "vite": "^5.0.0"
}
```

### **상태 관리**
```json
{
  "@reduxjs/toolkit": "^2.0.0",
  "react-redux": "^9.0.0"
}
```

### **UI 컴포넌트**
```json
{
  "@mui/material": "^5.15.0",
  "@mui/icons-material": "^5.15.0",
  "tailwindcss": "^3.4.0"
}
```

### **오디오/MIDI 웹 라이브러리**
```json
{
  "tone": "^14.7.0",           // 웹 오디오 신디사이저
  "midi-parser-js": "^4.0.0",  // 웹에서 MIDI 파싱
  "web-audio-api": "^0.2.0"    // 웹 오디오 API 래퍼
}
```

---

## 🎵 **음악 처리 스택**

### **MIDI 워크플로우**
```
AI 모델 출력 → MIDI 데이터 → music21 처리 → 파일 저장 → Ableton Live
     ↓              ↓              ↓              ↓             ↓
  NumPy 배열    MIDI 메시지    음악 이론 검증   .mid 파일    실시간 재생
```

### **음악 이론 엔진**
- **music21**: 화성 분석, 조성 분석, 리듬 분석
- **커스텀 규칙**: 장르별 음악 이론 적용
- **검증 시스템**: 생성된 음악의 이론적 타당성 검사

### **장르별 특화 모듈**
```python
# 장르별 모델 아키텍처
genres/
├── rock/          # 록 음악 생성 모델
├── hiphop/        # 힙합 비트 생성 모델  
├── jpop/          # J-pop 멜로디 모델
├── jazz/          # 재즈 화성 진행 모델
└── classical/     # 클래식 구조 모델
```

---

## 🔗 **외부 연동**

### **Ableton Live 연동**
- **python-rtmidi**: MIDI 실시간 통신
- **Live API**: Ableton Live 원격 제어
- **Max for Live**: 커스텀 디바이스 개발

### **파일 포맷 지원**
```
생성 → MIDI (.mid)
     → Ableton Live Set (.als)  
     → Audio Export (.wav, .mp3)
     → 음악 분석 데이터 (.json)
```

---

## 📊 **데이터 모델**

### **핵심 엔티티**
```python
# 데이터베이스 스키마
class User(Base):           # 사용자 관리
class Composition(Base):    # 작곡 작품
class Track(Base):         # 악기별 트랙
class MidiFile(Base):      # MIDI 파일 메타데이터
class AbletonProject(Base): # Ableton 프로젝트
class GenerationParams(Base): # AI 생성 파라미터
```

### **AI 모델 데이터**
```python
# 모델 입/출력 형식
input_format = {
    "genre": str,           # "rock", "hiphop", "jpop", ...
    "tempo": int,           # 60-200 BPM
    "key": str,            # "C", "Am", "F#", ...
    "length": int,         # 16, 32, 64 마디
    "creativity": float    # 0.0-1.0 창의성 레벨
}

output_format = {
    "tracks": [
        {
            "instrument": str,     # "drums", "bass", "melody"
            "notes": List[Note],   # MIDI 노트 시퀀스
            "timing": List[float], # 타이밍 정보
            "velocity": List[int]  # 벨로시티 (강도)
        }
    ]
}
```

---

## 🚀 **배포 및 인프라**

### **컨테이너화**
```dockerfile
# 개발 환경
FROM python:3.12-slim
RUN apt-get update && apt-get install -y \
    libasound2-dev \
    portaudio19-dev \
    timidity
```

### **환경 설정**
```bash
# 개발 환경 변수
ENVIRONMENT=development
DATABASE_URL=sqlite:///./data/ai_songwriting.db
CORS_ORIGINS=["http://localhost:3000"]

# AI 모델 설정
AI_MODEL_PATH=./models/
DEVICE=cuda  # or cpu
BATCH_SIZE=32
```

---

## 🧪 **테스트 전략**

### **백엔드 테스트**
```python
# 테스트 구조
tests/
├── test_api/          # API 엔드포인트 테스트
├── test_models/       # AI 모델 테스트
├── test_midi/         # MIDI 처리 테스트
└── test_ableton/      # Ableton 연동 테스트
```

### **프론트엔드 테스트**
```typescript
// 테스트 도구
- Jest: 단위 테스트
- React Testing Library: 컴포넌트 테스트  
- Cypress: E2E 테스트
```

---

## 📈 **성능 최적화**

### **AI 모델 최적화**
- **모델 경량화**: 추론 속도 향상
- **배치 처리**: 다중 요청 효율적 처리
- **캐싱**: 자주 사용되는 생성 결과 저장

### **웹 성능**
- **React 최적화**: 메모이제이션, 코드 스플리팅
- **API 최적화**: 비동기 처리, 응답 캐싱
- **MIDI 스트리밍**: 실시간 데이터 전송

---

## 🔒 **보안 고려사항**

### **API 보안**
- **CORS**: 허용된 도메인만 접근
- **Rate Limiting**: API 요청 제한
- **Input Validation**: 모든 입력 데이터 검증

### **파일 보안**
- **업로드 제한**: 허용된 파일 형식만
- **경로 검증**: 디렉토리 순회 공격 방지
- **권한 관리**: 사용자별 파일 접근 권한

---

## 🌐 **브라우저 호환성**

### **지원 브라우저**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### **웹 오디오 기능**
- Web Audio API
- Web MIDI API (Chrome에서 완전 지원)
- File API (MIDI 파일 업로드/다운로드)

---

**📅 최종 업데이트**: 2024-01-XX  
**🔧 기술 스택 버전**: Python 3.12 + React 18 + FastAPI 0.115  
**🎯 최적화 목표**: 30초 이내 실시간 음악 생성 