# AI 작곡 시스템 내보내기 가이드

## 개요
AI 작곡 시스템은 다양한 형태의 파일 내보내기를 지원하여 다른 협업자들과 효과적으로 작업할 수 있도록 합니다. 이 가이드는 모든 내보내기 기능과 협업 워크플로우를 설명합니다.

## 지원하는 내보내기 형식

### 1. MIDI 파일 (.mid)
- **전체 곡 MIDI**: 모든 트랙이 포함된 완전한 MIDI 파일
- **트랙별 MIDI**: 개별 트랙만 포함된 MIDI 파일
- **용도**: 편곡, 악기 변경, 다른 DAW에서 편집

### 2. 오디오 파일
- **지원 형식**: WAV, MP3, FLAC
- **믹싱 단계**:
  - `raw`: 원본 오디오 (개별 트랙 처리 전)
  - `mixed`: 믹싱 완료된 오디오
  - `mastered`: 마스터링까지 완료된 최종 오디오

### 3. 스템 파일
- 각 트랙별로 분리된 오디오 파일
- 믹싱 엔지니어가 개별 요소를 조정할 수 있음
- WAV 형식으로 최고 품질 제공

### 4. 프로젝트 패키지 (.zip)
- 완전한 프로젝트의 모든 파일을 포함
- 구조화된 디렉토리 구성
- 메타데이터 및 사용 가이드 포함

## API 엔드포인트

### 기본 정보 조회
```http
GET /export/formats
```
지원하는 모든 내보내기 형식과 옵션을 조회합니다.

### MIDI 내보내기
```http
GET /export/midi/{song_id}?track_id={track_id}
```
- `song_id`: 내보낼 곡의 ID (필수)
- `track_id`: 특정 트랙 ID (선택사항, 없으면 전체 곡)

**예시:**
```bash
# 전체 곡 MIDI 다운로드
curl -O "http://localhost:8000/export/midi/1"

# 특정 트랙 MIDI 다운로드
curl -O "http://localhost:8000/export/midi/1?track_id=3"
```

### 오디오 내보내기
```http
GET /export/audio/{song_id}?format={format}&stage={stage}&track_id={track_id}
```
- `song_id`: 내보낼 곡의 ID (필수)
- `format`: wav, mp3, flac 중 선택 (기본값: wav)
- `stage`: raw, mixed, mastered 중 선택 (기본값: mixed)
- `track_id`: 특정 트랙 ID (선택사항, 스템 파일용)

**예시:**
```bash
# 믹싱된 WAV 파일 다운로드
curl -O "http://localhost:8000/export/audio/1?format=wav&stage=mixed"

# 마스터링된 MP3 파일 다운로드
curl -O "http://localhost:8000/export/audio/1?format=mp3&stage=mastered"

# 특정 트랙 스템 파일 다운로드
curl -O "http://localhost:8000/export/audio/1?format=wav&stage=mixed&track_id=2"
```

### 프로젝트 패키지 내보내기
```http
POST /export/project-package/{song_id}?include_stems={boolean}&include_midi={boolean}
```
- `song_id`: 내보낼 곡의 ID (필수)
- `include_stems`: 스템 파일 포함 여부 (기본값: true)
- `include_midi`: MIDI 파일 포함 여부 (기본값: true)

**예시:**
```bash
# 완전한 프로젝트 패키지 생성
curl -X POST -O "http://localhost:8000/export/project-package/1?include_stems=true&include_midi=true"
```

## 프로젝트 패키지 구조

프로젝트 패키지는 다음과 같은 구조로 생성됩니다:

```
Song_Title_project/
├── midi/                          # MIDI 파일들
│   ├── Song_Title_full.mid        # 전체 곡 MIDI
│   ├── Song_Title_track_Kick.mid  # 트랙별 MIDI
│   ├── Song_Title_track_Snare.mid
│   └── ...
├── stems/                         # 트랙별 오디오 파일들
│   ├── Song_Title_stem_Kick_raw.wav
│   ├── Song_Title_stem_Kick_mixed.wav
│   ├── Song_Title_stem_Snare_raw.wav
│   ├── Song_Title_stem_Snare_mixed.wav
│   └── ...
├── mixdown/                       # 최종 믹스 파일들
│   ├── Song_Title_mixed_mix.wav   # 믹싱된 버전
│   └── Song_Title_mastered_mix.wav # 마스터링된 버전
├── project_info.json             # 프로젝트 메타데이터
└── README.md                      # 프로젝트 정보 및 가이드
```

## 협업 워크플로우

### 1. 순차적 협업 워크플로우
AI 작곡부터 최종 마스터링까지 단계별로 진행하는 방식입니다.

#### 단계 1: AI 작곡 및 MIDI 생성
1. AI 시스템에서 곡을 생성
2. MIDI 파일 내보내기
   ```bash
   curl -O "http://localhost:8000/export/midi/1"
   ```

#### 단계 2: 편곡 및 악기 추가
1. 편곡자가 MIDI 파일을 받아서 작업
2. 편곡 완료 후 개별 트랙 스템 파일 요청
   ```bash
   # 각 트랙별 스템 파일 다운로드
   curl -O "http://localhost:8000/export/audio/1?format=wav&stage=raw&track_id=1"
   curl -O "http://localhost:8000/export/audio/1?format=wav&stage=raw&track_id=2"
   ```

#### 단계 3: 믹싱
1. 믹싱 엔지니어가 스템 파일들을 받아서 믹싱 작업
2. 믹싱 완료된 버전 확인
   ```bash
   curl -O "http://localhost:8000/export/audio/1?format=wav&stage=mixed"
   ```

#### 단계 4: 마스터링
1. 마스터링 엔지니어가 믹싱된 파일을 받아서 최종 작업
2. 마스터링된 최종 버전 다운로드
   ```bash
   curl -O "http://localhost:8000/export/audio/1?format=wav&stage=mastered"
   ```

### 2. 병렬 협업 워크플로우
여러 작업자가 동시에 작업할 수 있는 방식입니다.

#### 초기 설정
1. AI 작곡 완료 후 완전한 프로젝트 패키지 생성
   ```bash
   curl -X POST -O "http://localhost:8000/export/project-package/1"
   ```

#### 병렬 작업
1. **편곡자**: MIDI 파일들로 편곡 작업
2. **보컬리스트**: 가사와 멜로디 라인으로 보컬 녹음
3. **믹싱 엔지니어**: 기본 스템 파일들로 초기 믹싱 작업
4. **프로듀서**: 전체적인 방향성 검토

#### 최종 취합
1. 각자의 작업물을 시스템에 업로드
2. 최종 프로젝트 패키지 재생성
3. 마스터링 진행

### 3. 반복 개선 워크플로우
AI 생성물을 여러 번 개선해가는 방식입니다.

#### 반복 사이클
1. **AI 생성**: 초기 버전 생성
2. **검토**: MIDI 및 기본 오디오로 검토
   ```bash
   curl -O "http://localhost:8000/export/midi/1"
   curl -O "http://localhost:8000/export/audio/1?format=mp3&stage=mixed"
   ```
3. **피드백**: 개선 사항 파악
4. **재생성**: AI에 피드백 반영하여 새 버전 생성
5. **승인**: 만족할 때까지 반복

#### 최종 승인 후
1. 완전한 프로젝트 패키지 생성
2. 전문 스태프에게 전달

## 품질별 사용 가이드

### 데모/프로토타입 단계
- **형식**: MP3, Raw 단계
- **용도**: 빠른 검토, 아이디어 공유
```bash
curl -O "http://localhost:8000/export/audio/1?format=mp3&stage=raw"
```

### 프로덕션 단계
- **형식**: WAV, Mixed 단계
- **용도**: 정식 작업, 품질 중요
```bash
curl -O "http://localhost:8000/export/audio/1?format=wav&stage=mixed"
```

### 배포/마스터링 단계
- **형식**: WAV, Mastered 단계
- **용도**: 최종 배포, 상업적 사용
```bash
curl -O "http://localhost:8000/export/audio/1?format=wav&stage=mastered"
```

## 실용적인 사용 예시

### 예시 1: 원격 협업자에게 작업물 전달
```python
import requests

# 곡 ID 1의 모든 스템 파일을 WAV로 다운로드
song_id = 1
tracks_response = requests.get(f"http://localhost:8000/songs/{song_id}/tracks")
tracks = tracks_response.json()

for track in tracks:
    track_id = track['id']
    track_name = track['name']
    
    # 각 트랙의 믹싱된 스템 파일 다운로드
    response = requests.get(
        f"http://localhost:8000/export/audio/{song_id}",
        params={"format": "wav", "stage": "mixed", "track_id": track_id}
    )
    
    if response.status_code == 200:
        with open(f"stem_{track_name}.wav", "wb") as f:
            f.write(response.content)
        print(f"다운로드 완료: stem_{track_name}.wav")
```

### 예시 2: 자동화된 백업 시스템
```bash
#!/bin/bash
# 모든 곡의 프로젝트 패키지를 백업하는 스크립트

BACKUP_DIR="./backups/$(date +%Y%m%d)"
mkdir -p "$BACKUP_DIR"

# 모든 곡 ID 조회
SONGS=$(curl -s "http://localhost:8000/songs" | jq -r '.[].id')

for song_id in $SONGS; do
    echo "백업 중: 곡 ID $song_id"
    curl -X POST -o "$BACKUP_DIR/song_${song_id}_project.zip" \
         "http://localhost:8000/export/project-package/$song_id"
done

echo "백업 완료: $BACKUP_DIR"
```

### 예시 3: 품질별 파일 생성
```python
import requests
from pathlib import Path

def export_all_qualities(song_id, output_dir="exports"):
    """모든 품질의 파일을 생성하는 함수"""
    
    formats = ["wav", "mp3", "flac"]
    stages = ["raw", "mixed", "mastered"]
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    for format_type in formats:
        for stage in stages:
            try:
                response = requests.get(
                    f"http://localhost:8000/export/audio/{song_id}",
                    params={"format": format_type, "stage": stage}
                )
                
                if response.status_code == 200:
                    filename = f"song_{song_id}_{stage}.{format_type}"
                    filepath = output_path / filename
                    
                    with open(filepath, "wb") as f:
                        f.write(response.content)
                    
                    print(f"생성 완료: {filename}")
                else:
                    print(f"생성 실패: {format_type} ({stage})")
                    
            except Exception as e:
                print(f"오류: {format_type} ({stage}) - {e}")

# 사용 예시
export_all_qualities(1)
```

## 문제 해결

### 자주 발생하는 문제들

#### 1. 파일 다운로드 실패
**증상**: HTTP 500 에러 또는 빈 파일
**원인**: 서버 리소스 부족, 파일 생성 오류
**해결방법**:
```bash
# 서버 상태 확인
curl "http://localhost:8000/health"

# 곡이 존재하는지 확인
curl "http://localhost:8000/songs/1"
```

#### 2. 큰 파일 다운로드 시 타임아웃
**증상**: 프로젝트 패키지 다운로드 중 연결 끊어짐
**해결방법**:
```bash
# 타임아웃 설정을 늘려서 다운로드
curl --max-time 300 -X POST -O "http://localhost:8000/export/project-package/1"
```

#### 3. 스템 파일이 비어있음
**증상**: 트랙별 스템 파일이 무음이거나 매우 작음
**원인**: 해당 트랙에 실제 오디오 데이터가 없음
**해결방법**:
```bash
# 트랙 정보 확인
curl "http://localhost:8000/songs/1/tracks"

# 전체 믹스와 비교
curl -O "http://localhost:8000/export/audio/1?format=wav&stage=mixed"
```

### 성능 최적화 팁

#### 1. 병렬 다운로드
여러 파일을 동시에 다운로드하여 시간을 절약할 수 있습니다:
```bash
# 백그라운드에서 병렬 다운로드
curl -O "http://localhost:8000/export/midi/1" &
curl -O "http://localhost:8000/export/audio/1?format=wav&stage=mixed" &
curl -X POST -O "http://localhost:8000/export/project-package/1" &
wait
```

#### 2. 압축 형식 활용
네트워크 대역폭이 제한적인 경우 MP3 또는 FLAC을 사용:
```bash
# 고품질이지만 용량이 작은 FLAC
curl -O "http://localhost:8000/export/audio/1?format=flac&stage=mastered"
```

#### 3. 단계별 다운로드
필요한 단계의 파일만 선택적으로 다운로드:
```bash
# 최종 검토용으로는 MP3면 충분
curl -O "http://localhost:8000/export/audio/1?format=mp3&stage=mixed"

# 실제 작업용으로는 WAV 사용
curl -O "http://localhost:8000/export/audio/1?format=wav&stage=raw"
```

## 보안 및 권한 관리

### API 키 사용 (향후 구현 예정)
```bash
# API 키를 헤더에 포함하여 요청
curl -H "Authorization: Bearer YOUR_API_KEY" \
     -O "http://localhost:8000/export/midi/1"
```

### 파일 접근 제한
- 내보내기된 파일은 24시간 후 자동 삭제됩니다
- 대용량 파일은 임시 URL을 통해 제공됩니다
- 사용자별 다운로드 횟수 제한이 있을 수 있습니다

## 추가 기능 및 로드맵

### 현재 개발 중인 기능
- **실시간 스트리밍**: 파일 생성과 동시에 스트리밍 다운로드
- **압축 옵션**: 다양한 압축률과 품질 설정
- **메타데이터 커스터마이징**: 내보내기 시 메타데이터 수정 가능

### 향후 계획
- **클라우드 저장소 연동**: Google Drive, Dropbox 직접 업로드
- **협업 플랫폼 연동**: Slack, Discord 자동 알림
- **버전 관리**: 내보내기 히스토리 및 버전 비교

---

**문서 버전**: 1.0
**마지막 업데이트**: 2024-06-24
**지원 문의**: AI 시스템 개발팀 