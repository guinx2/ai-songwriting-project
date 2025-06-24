"""
Ableton Live API 래퍼
Live 애플리케이션과의 통신 및 제어
"""

import os
import json
import time
from typing import Dict, List, Any, Optional
import logging
from .midi_connection import MidiConnection

logger = logging.getLogger(__name__)


class AbletonLiveAPI:
    """Ableton Live API 통신 클래스"""
    
    def __init__(self, midi_connection: Optional[MidiConnection] = None):
        self.midi_connection = midi_connection or MidiConnection()
        self.live_version = "Unknown"
        self.is_live_connected = False
        self.current_project = None
        
    def connect_to_live(self) -> bool:
        """Ableton Live에 연결"""
        try:
            # MIDI 연결 시도
            if self.midi_connection.connect_to_ableton():
                self.is_live_connected = True
                logger.info("Ableton Live 연결 성공")
                
                # Live 버전 정보 요청 (추후 구현)
                self.live_version = self._detect_live_version()
                return True
            else:
                logger.warning("Ableton Live MIDI 연결 실패")
                return False
                
        except Exception as e:
            logger.error(f"Ableton Live 연결 오류: {e}")
            return False
    
    def _detect_live_version(self) -> str:
        """Ableton Live 버전 감지"""
        try:
            # 실제로는 Live API를 통해 버전 정보를 받아올 수 있지만
            # 현재는 기본값 반환
            return "Live 12"
        except Exception:
            return "Unknown"
    
    def create_new_project(self, project_name: str, tempo: int = 120, key: str = "C") -> Dict[str, Any]:
        """새 Ableton Live 프로젝트 생성"""
        try:
            project_config = {
                "name": project_name,
                "tempo": tempo,
                "key": key,
                "created_at": time.time(),
                "tracks": [],
                "scenes": [],
                "master_track": {
                    "volume": 0.8,
                    "pan": 0.0,
                    "effects": []
                }
            }
            
            self.current_project = project_config
            logger.info(f"새 프로젝트 생성: {project_name}")
            
            return {
                "success": True,
                "project": project_config,
                "message": f"프로젝트 '{project_name}' 생성 완료"
            }
            
        except Exception as e:
            logger.error(f"프로젝트 생성 오류: {e}")
            return {"success": False, "error": str(e)}
    
    def add_track(self, track_name: str, track_type: str = "audio", instrument: Optional[str] = None) -> Dict[str, Any]:
        """프로젝트에 트랙 추가"""
        try:
            if not self.current_project:
                return {"success": False, "error": "활성 프로젝트가 없습니다"}
            
            track_config = {
                "id": len(self.current_project["tracks"]) + 1,
                "name": track_name,
                "type": track_type,  # "audio", "midi", "return", "master"
                "instrument": instrument,
                "volume": 0.8,
                "pan": 0.0,
                "mute": False,
                "solo": False,
                "arm": False,
                "clips": [],
                "effects": []
            }
            
            self.current_project["tracks"].append(track_config)
            logger.info(f"트랙 추가: {track_name} ({track_type})")
            
            return {
                "success": True,
                "track": track_config,
                "track_id": track_config["id"]
            }
            
        except Exception as e:
            logger.error(f"트랙 추가 오류: {e}")
            return {"success": False, "error": str(e)}
    
    def add_midi_clip(self, track_id: int, clip_name: str, notes: List[Dict], clip_length: float = 4.0) -> Dict[str, Any]:
        """MIDI 클립 추가"""
        try:
            if not self.current_project:
                return {"success": False, "error": "활성 프로젝트가 없습니다"}
            
            # 트랙 찾기
            track = None
            for t in self.current_project["tracks"]:
                if t["id"] == track_id:
                    track = t
                    break
            
            if not track:
                return {"success": False, "error": f"트랙 ID {track_id}를 찾을 수 없습니다"}
            
            clip_config = {
                "id": len(track["clips"]) + 1,
                "name": clip_name,
                "type": "midi",
                "length": clip_length,
                "loop": True,
                "notes": notes,
                "created_at": time.time()
            }
            
            track["clips"].append(clip_config)
            logger.info(f"MIDI 클립 추가: {clip_name} (트랙 {track_id})")
            
            return {
                "success": True,
                "clip": clip_config,
                "clip_id": clip_config["id"]
            }
            
        except Exception as e:
            logger.error(f"MIDI 클립 추가 오류: {e}")
            return {"success": False, "error": str(e)}
    
    def play_project(self) -> bool:
        """프로젝트 재생"""
        try:
            if not self.is_live_connected:
                logger.warning("Ableton Live에 연결되지 않음")
                return False
            
            # 재생 명령 MIDI 메시지 전송 (Play/Stop)
            # MIDI Control Change: Controller 1 = Play/Stop
            success = self.midi_connection.send_control_change(1, 1, 127)
            
            if success:
                logger.info("프로젝트 재생 시작")
            
            return success
            
        except Exception as e:
            logger.error(f"재생 오류: {e}")
            return False
    
    def stop_project(self) -> bool:
        """프로젝트 정지"""
        try:
            if not self.is_live_connected:
                logger.warning("Ableton Live에 연결되지 않음")
                return False
            
            # 정지 명령 MIDI 메시지 전송
            success = self.midi_connection.send_control_change(1, 1, 0)
            
            if success:
                logger.info("프로젝트 정지")
            
            return success
            
        except Exception as e:
            logger.error(f"정지 오류: {e}")
            return False
    
    def set_tempo(self, tempo: int) -> bool:
        """템포 설정"""
        try:
            if not self.current_project:
                return False
            
            self.current_project["tempo"] = tempo
            
            # Live에 템포 변경 명령 전송 (실제 구현시)
            # 현재는 내부 상태만 업데이트
            logger.info(f"템포 설정: {tempo} BPM")
            return True
            
        except Exception as e:
            logger.error(f"템포 설정 오류: {e}")
            return False
    
    def export_to_als_file(self, file_path: str) -> Dict[str, Any]:
        """Ableton Live 프로젝트 파일(.als) 생성"""
        try:
            if not self.current_project:
                return {"success": False, "error": "활성 프로젝트가 없습니다"}
            
            # ALS 파일 기본 구조 생성
            als_data = {
                "ableton": {
                    "version": "5.0.0",
                    "schema_change_count": "2",
                    "creator": "AI Songwriting System",
                    "revision": "1"
                },
                "live_set": {
                    "project_name": self.current_project["name"],
                    "tempo": self.current_project["tempo"],
                    "global_quantization": "4",
                    "tracks": self.current_project["tracks"],
                    "master_track": self.current_project["master_track"],
                    "locators": [],
                    "scenes": self.current_project.get("scenes", [])
                },
                "metadata": {
                    "created_by": "AI Songwriting System",
                    "created_at": self.current_project["created_at"],
                    "exported_at": time.time()
                }
            }
            
            # 디렉토리 생성
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            # JSON 형태로 저장 (실제 ALS는 XML이지만 개발 단계에서는 JSON 사용)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(als_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"ALS 파일 생성: {file_path}")
            
            return {
                "success": True,
                "file_path": file_path,
                "file_size": os.path.getsize(file_path),
                "tracks_count": len(self.current_project["tracks"])
            }
            
        except Exception as e:
            logger.error(f"ALS 파일 생성 오류: {e}")
            return {"success": False, "error": str(e)}
    
    def get_project_info(self) -> Dict[str, Any]:
        """현재 프로젝트 정보 반환"""
        if not self.current_project:
            return {"error": "활성 프로젝트가 없습니다"}
        
        return {
            "project": self.current_project,
            "live_version": self.live_version,
            "is_connected": self.is_live_connected,
            "tracks_count": len(self.current_project.get("tracks", [])),
            "clips_count": sum(len(track.get("clips", [])) for track in self.current_project.get("tracks", []))
        }
    
    def disconnect(self) -> None:
        """Ableton Live 연결 해제"""
        try:
            if self.midi_connection:
                self.midi_connection.disconnect()
            
            self.is_live_connected = False
            logger.info("Ableton Live 연결 해제")
            
        except Exception as e:
            logger.error(f"연결 해제 오류: {e}")


# 전역 Ableton Live API 인스턴스
global_live_api = AbletonLiveAPI()


def get_live_api() -> AbletonLiveAPI:
    """전역 Ableton Live API 인스턴스 반환"""
    return global_live_api 