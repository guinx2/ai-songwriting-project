# src/ - 소스 코드 디렉토리

이 디렉토리는 AI 작곡 시스템의 모든 소스 코드를 포함합니다.

## 📁 디렉토리 구조

### `ai_models/`
- AI 음악 생성 모델 구현
- Transformer, RNN 기반 모델
- 장르별 특화 모델 (클래식, 재즈, 팝, 일렉트로닉, 락, 힙합, Jpop)

### `music_theory/`
- 음악 이론 관련 모듈
- 코드 진행, 스케일, 모드 처리
- 화성 분석 및 생성

### `midi_generation/`
- MIDI 파일 생성 및 처리
- 다중 트랙 지원
- 악기별 개별 트랙 생성

### `api/`
- REST API 엔드포인트
- FastAPI/Flask 기반 웹 서버
- 사용자 인터페이스와의 통신

### `models/`
- 데이터베이스 모델
- SQLAlchemy ORM 모델
- 사용자, 작품, 설정 관리

### `utils/`
- 유틸리티 함수들
- 공통 헬퍼 모듈
- 데이터 전처리 도구

### `ableton_integration/`
- Ableton Live 연동 모듈
- Max for Live API 연동
- .als 프로젝트 파일 생성 