#!/usr/bin/env python3
"""
AI 작곡 시스템 내보내기 API 테스트 스크립트
"""
import requests
import json
import time
from pathlib import Path

# API 기본 설정
BASE_URL = "http://localhost:8000"
API_HEADERS = {
    "Content-Type": "application/json"
}

def test_api_connection():
    """API 서버 연결 테스트"""
    print("🔗 API 서버 연결 테스트...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ API 서버 연결 성공")
            return True
        else:
            print(f"❌ API 서버 연결 실패 (상태 코드: {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ API 서버 연결 오류: {e}")
        return False

def create_test_song():
    """테스트용 곡 생성"""
    print("\n🎵 테스트용 곡 생성...")
    
    song_data = {
        "title": "Test AI Song",
        "artist_name": "AI Composer",
        "genre_name": "Electronic",
        "bpm": 128,
        "key_signature": "Am",
        "time_signature": "4/4",
        "lyrics": "AI가 만든 테스트 곡입니다."
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/songs",
            headers=API_HEADERS,
            json=song_data
        )
        
        if response.status_code == 200:
            song = response.json()
            song_id = song['id']
            print(f"✅ 테스트 곡 생성 성공 (ID: {song_id})")
            
            # 트랙들 추가
            tracks_data = [
                {"name": "Kick", "instrument": "Drum Kit", "midi_channel": 1},
                {"name": "Snare", "instrument": "Drum Kit", "midi_channel": 2},
                {"name": "Hi-Hat", "instrument": "Drum Kit", "midi_channel": 3},
                {"name": "Bass", "instrument": "Bass Synth", "midi_channel": 4},
                {"name": "Lead", "instrument": "Lead Synth", "midi_channel": 5}
            ]
            
            for track_data in tracks_data:
                track_response = requests.post(
                    f"{BASE_URL}/songs/{song_id}/tracks",
                    headers=API_HEADERS,
                    json=track_data
                )
                if track_response.status_code == 200:
                    track = track_response.json()
                    print(f"  ✅ 트랙 '{track['name']}' 추가됨")
            
            return song_id
        else:
            print(f"❌ 곡 생성 실패 (상태 코드: {response.status_code})")
            print(f"응답: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ 곡 생성 오류: {e}")
        return None

def test_export_formats():
    """내보내기 형식 조회 테스트"""
    print("\n📋 내보내기 형식 조회 테스트...")
    
    try:
        response = requests.get(f"{BASE_URL}/export/formats")
        
        if response.status_code == 200:
            formats = response.json()
            print("✅ 내보내기 형식 조회 성공:")
            print(f"  📄 MIDI 형식: {formats['midi_formats']}")
            print(f"  🎵 오디오 형식: {formats['audio_formats']}")
            print(f"  🎛️ 믹싱 단계: {formats['mixing_stages']}")
            return True
        else:
            print(f"❌ 형식 조회 실패 (상태 코드: {response.status_code})")
            return False
            
    except Exception as e:
        print(f"❌ 형식 조회 오류: {e}")
        return False

def test_midi_export(song_id):
    """MIDI 내보내기 테스트"""
    print("\n🎹 MIDI 내보내기 테스트...")
    
    # 전체 곡 MIDI 내보내기
    try:
        print("  📥 전체 곡 MIDI 다운로드 중...")
        response = requests.get(f"{BASE_URL}/export/midi/{song_id}")
        
        if response.status_code == 200:
            # 파일 저장
            output_dir = Path("test_output")
            output_dir.mkdir(exist_ok=True)
            
            filepath = output_dir / f"test_song_{song_id}_full.mid"
            with open(filepath, "wb") as f:
                f.write(response.content)
            
            print(f"✅ 전체 MIDI 다운로드 성공: {filepath}")
            
            # 파일 크기 확인
            file_size = filepath.stat().st_size
            print(f"  📊 파일 크기: {file_size} bytes")
            
            return True
        else:
            print(f"❌ MIDI 다운로드 실패 (상태 코드: {response.status_code})")
            return False
            
    except Exception as e:
        print(f"❌ MIDI 다운로드 오류: {e}")
        return False

def test_audio_export(song_id):
    """오디오 내보내기 테스트"""
    print("\n🎧 오디오 내보내기 테스트...")
    
    formats = ["wav", "mp3", "flac"]
    stages = ["raw", "mixed", "mastered"]
    
    output_dir = Path("test_output")
    output_dir.mkdir(exist_ok=True)
    
    success_count = 0
    total_tests = len(formats) * len(stages)
    
    for format_type in formats:
        for stage in stages:
            try:
                print(f"  📥 {format_type.upper()} ({stage}) 다운로드 중...")
                
                params = {"format": format_type, "stage": stage}
                response = requests.get(
                    f"{BASE_URL}/export/audio/{song_id}",
                    params=params
                )
                
                if response.status_code == 200:
                    filename = f"test_song_{song_id}_{stage}_mix.{format_type}"
                    filepath = output_dir / filename
                    
                    with open(filepath, "wb") as f:
                        f.write(response.content)
                    
                    file_size = filepath.stat().st_size
                    print(f"    ✅ {filename} 다운로드 성공 ({file_size} bytes)")
                    success_count += 1
                else:
                    print(f"    ❌ {format_type} ({stage}) 다운로드 실패")
                    
            except Exception as e:
                print(f"    ❌ {format_type} ({stage}) 다운로드 오류: {e}")
    
    print(f"\n📊 오디오 내보내기 결과: {success_count}/{total_tests} 성공")
    return success_count == total_tests

def test_project_package_export(song_id):
    """프로젝트 패키지 내보내기 테스트"""
    print("\n📦 프로젝트 패키지 내보내기 테스트...")
    
    try:
        print("  📥 프로젝트 패키지 생성 중...")
        
        params = {
            "include_stems": True,
            "include_midi": True
        }
        
        response = requests.post(
            f"{BASE_URL}/export/project-package/{song_id}",
            params=params
        )
        
        if response.status_code == 200:
            output_dir = Path("test_output")
            output_dir.mkdir(exist_ok=True)
            
            # ZIP 파일 저장
            filename = f"test_song_{song_id}_project.zip"
            filepath = output_dir / filename
            
            with open(filepath, "wb") as f:
                f.write(response.content)
            
            file_size = filepath.stat().st_size
            print(f"✅ 프로젝트 패키지 다운로드 성공: {filepath}")
            print(f"  📊 패키지 크기: {file_size} bytes")
            
            # ZIP 파일 내용 확인
            import zipfile
            try:
                with zipfile.ZipFile(filepath, 'r') as zip_file:
                    file_list = zip_file.namelist()
                    print(f"  📋 패키지 내용 ({len(file_list)}개 파일):")
                    for file in sorted(file_list)[:10]:  # 처음 10개만 표시
                        print(f"    - {file}")
                    if len(file_list) > 10:
                        print(f"    ... 및 {len(file_list) - 10}개 추가 파일")
                        
            except Exception as e:
                print(f"  ⚠️ ZIP 파일 내용 확인 실패: {e}")
            
            return True
        else:
            print(f"❌ 프로젝트 패키지 생성 실패 (상태 코드: {response.status_code})")
            print(f"응답: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 프로젝트 패키지 생성 오류: {e}")
        return False

def test_stem_export(song_id):
    """스템 파일 내보내기 테스트"""
    print("\n🎛️ 스템 파일 내보내기 테스트...")
    
    # 먼저 트랙 목록 조회
    try:
        response = requests.get(f"{BASE_URL}/songs/{song_id}/tracks")
        if response.status_code != 200:
            print("❌ 트랙 목록 조회 실패")
            return False
        
        tracks = response.json()
        print(f"  📋 {len(tracks)}개 트랙 발견")
        
        output_dir = Path("test_output")
        output_dir.mkdir(exist_ok=True)
        
        success_count = 0
        
        for track in tracks:
            track_id = track['id']
            track_name = track['name']
            
            try:
                print(f"  📥 '{track_name}' 스템 다운로드 중...")
                
                params = {
                    "track_id": track_id,
                    "format": "wav",
                    "stage": "mixed"
                }
                
                response = requests.get(
                    f"{BASE_URL}/export/audio/{song_id}",
                    params=params
                )
                
                if response.status_code == 200:
                    filename = f"test_song_{song_id}_stem_{track_name}_mixed.wav"
                    filepath = output_dir / filename
                    
                    with open(filepath, "wb") as f:
                        f.write(response.content)
                    
                    file_size = filepath.stat().st_size
                    print(f"    ✅ {filename} 다운로드 성공 ({file_size} bytes)")
                    success_count += 1
                else:
                    print(f"    ❌ '{track_name}' 스템 다운로드 실패")
                    
            except Exception as e:
                print(f"    ❌ '{track_name}' 스템 다운로드 오류: {e}")
        
        print(f"\n📊 스템 내보내기 결과: {success_count}/{len(tracks)} 성공")
        return success_count == len(tracks)
        
    except Exception as e:
        print(f"❌ 스템 내보내기 테스트 오류: {e}")
        return False

def performance_test(song_id):
    """성능 테스트"""
    print("\n⚡ 성능 테스트...")
    
    tests = [
        ("MIDI 내보내기", f"{BASE_URL}/export/midi/{song_id}"),
        ("WAV 내보내기", f"{BASE_URL}/export/audio/{song_id}?format=wav&stage=mixed"),
        ("프로젝트 패키지", f"{BASE_URL}/export/project-package/{song_id}")
    ]
    
    for test_name, url in tests:
        try:
            print(f"  ⏱️ {test_name} 속도 측정...")
            
            start_time = time.time()
            
            if "project-package" in url:
                response = requests.post(url)
            else:
                response = requests.get(url)
            
            end_time = time.time()
            duration = end_time - start_time
            
            if response.status_code == 200:
                file_size = len(response.content)
                speed = file_size / duration / 1024  # KB/s
                print(f"    ✅ {test_name}: {duration:.2f}초, {file_size} bytes, {speed:.1f} KB/s")
            else:
                print(f"    ❌ {test_name}: 실패 (상태 코드: {response.status_code})")
                
        except Exception as e:
            print(f"    ❌ {test_name}: 오류 - {e}")

def cleanup_test_song(song_id):
    """테스트 곡 정리"""
    print(f"\n🧹 테스트 곡 정리 (ID: {song_id})...")
    
    try:
        response = requests.delete(f"{BASE_URL}/songs/{song_id}")
        
        if response.status_code == 200:
            print("✅ 테스트 곡 삭제 완료")
        else:
            print(f"⚠️ 테스트 곡 삭제 실패 (상태 코드: {response.status_code})")
            
    except Exception as e:
        print(f"⚠️ 테스트 곡 삭제 오류: {e}")

def main():
    """메인 테스트 실행"""
    print("🚀 AI 작곡 시스템 내보내기 API 테스트 시작\n")
    
    # 1. API 연결 테스트
    if not test_api_connection():
        print("\n❌ API 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요.")
        return
    
    # 2. 테스트 곡 생성
    song_id = create_test_song()
    if not song_id:
        print("\n❌ 테스트 곡을 생성할 수 없습니다.")
        return
    
    print(f"\n📝 테스트 대상 곡 ID: {song_id}")
    
    # 테스트 결과 수집
    test_results = []
    
    # 3. 기본 기능 테스트
    test_results.append(("내보내기 형식 조회", test_export_formats()))
    test_results.append(("MIDI 내보내기", test_midi_export(song_id)))
    test_results.append(("오디오 내보내기", test_audio_export(song_id)))
    test_results.append(("스템 내보내기", test_stem_export(song_id)))
    test_results.append(("프로젝트 패키지", test_project_package_export(song_id)))
    
    # 4. 성능 테스트
    performance_test(song_id)
    
    # 5. 정리
    cleanup_test_song(song_id)
    
    # 6. 결과 요약
    print("\n" + "="*50)
    print("📊 테스트 결과 요약")
    print("="*50)
    
    passed = 0
    total = len(test_results)
    
    for test_name, result in test_results:
        status = "✅ 통과" if result else "❌ 실패"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n전체 결과: {passed}/{total} 테스트 통과")
    
    if passed == total:
        print("🎉 모든 테스트가 성공적으로 완료되었습니다!")
    else:
        print("⚠️ 일부 테스트가 실패했습니다. 로그를 확인하세요.")
    
    # 출력 파일 정보
    output_dir = Path("test_output")
    if output_dir.exists():
        files = list(output_dir.glob("*"))
        if files:
            print(f"\n📁 생성된 테스트 파일들 ({len(files)}개):")
            print(f"위치: {output_dir.absolute()}")
            for file in sorted(files)[:5]:  # 처음 5개만 표시
                size = file.stat().st_size
                print(f"  - {file.name} ({size} bytes)")
            if len(files) > 5:
                print(f"  ... 및 {len(files) - 5}개 추가 파일")

if __name__ == "__main__":
    main() 