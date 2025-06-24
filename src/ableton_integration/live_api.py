"""
Ableton Live API 연동 클래스
"""
import time
import json
from typing import Dict, List, Optional, Any
from pathlib import Path

class AbletonLiveAPI:
    """Ableton Live와의 연동을 위한 API 클래스"""
    
    def __init__(self):
        """API 초기화"""
        self.connected = False
        self.project_info = {}
        self.tracks = []
        
    def connect(self) -> bool:
        """Ableton Live에 연결"""
        try:
            # 실제 구현에서는 Live API 연결 로직
            # 현재는 시뮬레이션
            print("Ableton Live 연결 시도...")
            time.sleep(1)  # 연결 시뮬레이션
            
            self.connected = True
            print("Ableton Live 연결 성공!")
            
            # 기본 프로젝트 정보 로드
            self._load_project_info()
            
            return True
            
        except Exception as e:
            print(f"Ableton Live 연결 실패: {e}")
            self.connected = False
            return False
    
    def disconnect(self):
        """Ableton Live 연결 해제"""
        try:
            print("Ableton Live 연결 해제...")
            self.connected = False
            self.project_info = {}
            self.tracks = []
            print("연결 해제 완료")
            
        except Exception as e:
            print(f"연결 해제 오류: {e}")
    
    def is_connected(self) -> bool:
        """연결 상태 확인"""
        return self.connected
    
    def _load_project_info(self):
        """현재 프로젝트 정보 로드"""
        if not self.connected:
            return
        
        # 실제 구현에서는 Live API를 통해 정보 조회
        # 현재는 시뮬레이션 데이터
        self.project_info = {
            "name": "AI Generated Song",
            "bpm": 120,
            "time_signature": "4/4",
            "key": "C",
            "length": 240.0,  # 초 단위
            "created_at": "2024-06-24T10:00:00",
            "last_modified": "2024-06-24T18:00:00"
        }
        
        # 트랙 정보 시뮬레이션
        self.tracks = [
            {
                "id": 1,
                "name": "Kick",
                "type": "drum",
                "color": "#FF4444",
                "volume": 0.8,
                "pan": 0.0,
                "muted": False,
                "soloed": False,
                "armed": False,
                "midi_channel": 1
            },
            {
                "id": 2,
                "name": "Snare",
                "type": "drum",
                "color": "#44FF44",
                "volume": 0.7,
                "pan": 0.0,
                "muted": False,
                "soloed": False,
                "armed": False,
                "midi_channel": 2
            },
            {
                "id": 3,
                "name": "Hi-Hat",
                "type": "drum",
                "color": "#4444FF",
                "volume": 0.6,
                "pan": 0.1,
                "muted": False,
                "soloed": False,
                "armed": False,
                "midi_channel": 3
            },
            {
                "id": 4,
                "name": "Bass",
                "type": "instrument",
                "color": "#FF44FF",
                "volume": 0.9,
                "pan": 0.0,
                "muted": False,
                "soloed": False,
                "armed": False,
                "midi_channel": 4
            },
            {
                "id": 5,
                "name": "Lead Synth",
                "type": "instrument",
                "color": "#FFFF44",
                "volume": 0.8,
                "pan": -0.2,
                "muted": False,
                "soloed": False,
                "armed": False,
                "midi_channel": 5
            }
        ]
    
    def get_project_info(self) -> Dict[str, Any]:
        """프로젝트 정보 반환"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        return {
            "project": self.project_info,
            "tracks": self.tracks,
            "track_count": len(self.tracks)
        }
    
    def get_tracks(self) -> List[Dict[str, Any]]:
        """모든 트랙 정보 반환"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        return self.tracks
    
    def get_track_by_id(self, track_id: int) -> Optional[Dict[str, Any]]:
        """특정 트랙 정보 반환"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        return next((t for t in self.tracks if t['id'] == track_id), None)
    
    def create_track(self, name: str, track_type: str = "instrument") -> Dict[str, Any]:
        """새 트랙 생성"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        new_track = {
            "id": len(self.tracks) + 1,
            "name": name,
            "type": track_type,
            "color": "#FFFFFF",
            "volume": 0.8,
            "pan": 0.0,
            "muted": False,
            "soloed": False,
            "armed": False,
            "midi_channel": len(self.tracks) + 1
        }
        
        self.tracks.append(new_track)
        print(f"트랙 '{name}' 생성됨")
        
        return new_track
    
    def delete_track(self, track_id: int) -> bool:
        """트랙 삭제"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        track = self.get_track_by_id(track_id)
        if not track:
            return False
        
        self.tracks = [t for t in self.tracks if t['id'] != track_id]
        print(f"트랙 '{track['name']}' 삭제됨")
        
        return True
    
    def update_track(self, track_id: int, **kwargs) -> bool:
        """트랙 설정 업데이트"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        track = self.get_track_by_id(track_id)
        if not track:
            return False
        
        # 업데이트 가능한 필드들
        updatable_fields = ['name', 'volume', 'pan', 'muted', 'soloed', 'armed', 'color']
        
        for key, value in kwargs.items():
            if key in updatable_fields:
                track[key] = value
        
        print(f"트랙 '{track['name']}' 업데이트됨")
        return True
    
    def send_midi_data(self, midi_data: str) -> bool:
        """MIDI 데이터 전송"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        try:
            # 실제 구현에서는 Live API를 통해 MIDI 데이터 전송
            print("MIDI 데이터 전송 중...")
            time.sleep(0.5)  # 전송 시뮬레이션
            print("MIDI 데이터 전송 완료")
            
            return True
            
        except Exception as e:
            print(f"MIDI 데이터 전송 실패: {e}")
            return False
    
    def start_playback(self) -> bool:
        """재생 시작"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        try:
            print("재생 시작")
            return True
        except Exception as e:
            print(f"재생 시작 실패: {e}")
            return False
    
    def stop_playback(self) -> bool:
        """재생 중지"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        try:
            print("재생 중지")
            return True
        except Exception as e:
            print(f"재생 중지 실패: {e}")
            return False
    
    def record_start(self) -> bool:
        """녹음 시작"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        try:
            print("녹음 시작")
            return True
        except Exception as e:
            print(f"녹음 시작 실패: {e}")
            return False
    
    def record_stop(self) -> bool:
        """녹음 중지"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        try:
            print("녹음 중지")
            return True
        except Exception as e:
            print(f"녹음 중지 실패: {e}")
            return False
    
    def set_tempo(self, bpm: int) -> bool:
        """템포 설정"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        try:
            self.project_info['bpm'] = bpm
            print(f"템포 {bpm}BPM으로 설정됨")
            return True
        except Exception as e:
            print(f"템포 설정 실패: {e}")
            return False
    
    def get_tempo(self) -> int:
        """현재 템포 조회"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        return self.project_info.get('bpm', 120)
    
    def save_project(self, filepath: Optional[str] = None) -> bool:
        """프로젝트 저장"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        try:
            if filepath:
                print(f"프로젝트를 {filepath}에 저장")
            else:
                print("프로젝트 저장")
            
            return True
        except Exception as e:
            print(f"프로젝트 저장 실패: {e}")
            return False
    
    def export_audio(self, output_path: str, format: str = "wav") -> bool:
        """오디오 내보내기"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        try:
            print(f"오디오를 {output_path}에 {format} 형식으로 내보내기")
            time.sleep(2)  # 내보내기 시뮬레이션
            print("오디오 내보내기 완료")
            
            return True
        except Exception as e:
            print(f"오디오 내보내기 실패: {e}")
            return False
    
    def get_current_time(self) -> float:
        """현재 재생 시간 조회 (초)"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        # 실제 구현에서는 Live API를 통해 현재 시간 조회
        return 0.0  # 시뮬레이션
    
    def set_current_time(self, time_seconds: float) -> bool:
        """재생 위치 설정"""
        if not self.connected:
            raise Exception("Ableton Live에 연결되지 않음")
        
        try:
            print(f"재생 위치를 {time_seconds}초로 설정")
            return True
        except Exception as e:
            print(f"재생 위치 설정 실패: {e}")
            return False 