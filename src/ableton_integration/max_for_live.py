"""
Max for Live 연동 인터페이스
"""
import json
import socket
import time
from typing import Dict, List, Optional, Any, Union
from threading import Thread, Event
import struct

class MaxForLiveInterface:
    """Max for Live와의 통신을 위한 인터페이스"""
    
    def __init__(self, host: str = "localhost", port: int = 7400):
        """
        Max for Live 인터페이스 초기화
        
        Args:
            host: Max for Live가 실행 중인 호스트
            port: 통신 포트 번호
        """
        self.host = host
        self.port = port
        self.socket: Optional[socket.socket] = None
        self.connected = False
        self.listening = False
        self.listen_thread: Optional[Thread] = None
        self.stop_event = Event()
        self.message_handlers: Dict[str, callable] = {}
        
    def connect(self) -> bool:
        """Max for Live에 연결"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5.0)  # 5초 타임아웃
            self.socket.connect((self.host, self.port))
            
            self.connected = True
            print(f"Max for Live 연결 성공: {self.host}:{self.port}")
            
            # 연결 확인 메시지 전송
            self.send_message("connect", {"client": "AI_Songwriting_System"})
            
            return True
            
        except Exception as e:
            print(f"Max for Live 연결 실패: {e}")
            self.connected = False
            return False
    
    def disconnect(self):
        """Max for Live 연결 해제"""
        try:
            self.stop_listening()
            
            if self.socket:
                # 연결 해제 메시지 전송
                self.send_message("disconnect", {})
                self.socket.close()
                self.socket = None
            
            self.connected = False
            print("Max for Live 연결 해제")
            
        except Exception as e:
            print(f"Max for Live 연결 해제 오류: {e}")
    
    def is_connected(self) -> bool:
        """연결 상태 확인"""
        return self.connected and self.socket is not None
    
    def send_message(self, command: str, data: Dict[str, Any]) -> bool:
        """Max for Live에 메시지 전송"""
        if not self.is_connected():
            print("Max for Live에 연결되지 않음")
            return False
        
        try:
            message = {
                "command": command,
                "data": data,
                "timestamp": time.time()
            }
            
            message_json = json.dumps(message)
            message_bytes = message_json.encode('utf-8')
            
            # 메시지 길이를 먼저 전송 (4바이트)
            length = struct.pack('!I', len(message_bytes))
            self.socket.send(length)
            
            # 메시지 내용 전송
            self.socket.send(message_bytes)
            
            return True
            
        except Exception as e:
            print(f"메시지 전송 실패: {e}")
            self.connected = False
            return False
    
    def receive_message(self) -> Optional[Dict[str, Any]]:
        """Max for Live로부터 메시지 수신"""
        if not self.is_connected():
            return None
        
        try:
            # 메시지 길이 수신 (4바이트)
            length_data = self.socket.recv(4)
            if len(length_data) < 4:
                return None
            
            message_length = struct.unpack('!I', length_data)[0]
            
            # 메시지 내용 수신
            message_data = b''
            while len(message_data) < message_length:
                chunk = self.socket.recv(message_length - len(message_data))
                if not chunk:
                    break
                message_data += chunk
            
            if len(message_data) < message_length:
                return None
            
            # JSON 파싱
            message_json = message_data.decode('utf-8')
            message = json.loads(message_json)
            
            return message
            
        except Exception as e:
            print(f"메시지 수신 실패: {e}")
            return None
    
    def start_listening(self) -> bool:
        """메시지 수신 시작"""
        if not self.is_connected():
            print("Max for Live에 연결되지 않음")
            return False
        
        if self.listening:
            return True
        
        self.stop_event.clear()
        self.listening = True
        self.listen_thread = Thread(target=self._listen_messages, daemon=True)
        self.listen_thread.start()
        
        print("Max for Live 메시지 수신 시작")
        return True
    
    def stop_listening(self):
        """메시지 수신 중지"""
        if not self.listening:
            return
        
        self.listening = False
        self.stop_event.set()
        
        if self.listen_thread:
            self.listen_thread.join(timeout=1.0)
            self.listen_thread = None
        
        print("Max for Live 메시지 수신 중지")
    
    def _listen_messages(self):
        """메시지 수신 스레드"""
        while self.listening and not self.stop_event.is_set():
            try:
                message = self.receive_message()
                if message:
                    self._handle_message(message)
                
                time.sleep(0.01)  # CPU 사용량 제한
                
            except Exception as e:
                print(f"메시지 수신 스레드 오류: {e}")
                time.sleep(0.1)
    
    def _handle_message(self, message: Dict[str, Any]):
        """수신된 메시지 처리"""
        command = message.get('command')
        if command and command in self.message_handlers:
            try:
                self.message_handlers[command](message)
            except Exception as e:
                print(f"메시지 핸들러 오류: {e}")
    
    def add_message_handler(self, command: str, handler: callable):
        """메시지 핸들러 추가"""
        self.message_handlers[command] = handler
    
    def remove_message_handler(self, command: str):
        """메시지 핸들러 제거"""
        if command in self.message_handlers:
            del self.message_handlers[command]
    
    # Max for Live 특화 메서드들
    def get_live_info(self) -> Optional[Dict[str, Any]]:
        """Live 정보 조회"""
        if self.send_message("get_live_info", {}):
            # 응답 대기 (실제로는 비동기 처리)
            time.sleep(0.1)
            return {"status": "success", "message": "Live info requested"}
        return None
    
    def set_tempo(self, bpm: float) -> bool:
        """템포 설정"""
        return self.send_message("set_tempo", {"bpm": bpm})
    
    def get_tempo(self) -> bool:
        """현재 템포 조회"""
        return self.send_message("get_tempo", {})
    
    def play(self) -> bool:
        """재생 시작"""
        return self.send_message("play", {})
    
    def stop(self) -> bool:
        """재생 중지"""
        return self.send_message("stop", {})
    
    def record(self) -> bool:
        """녹음 시작"""
        return self.send_message("record", {})
    
    def create_track(self, name: str, track_type: str = "midi") -> bool:
        """새 트랙 생성"""
        return self.send_message("create_track", {
            "name": name,
            "type": track_type
        })
    
    def select_track(self, track_index: int) -> bool:
        """트랙 선택"""
        return self.send_message("select_track", {"index": track_index})
    
    def set_track_volume(self, track_index: int, volume: float) -> bool:
        """트랙 볼륨 설정"""
        return self.send_message("set_track_volume", {
            "track_index": track_index,
            "volume": volume
        })
    
    def set_track_pan(self, track_index: int, pan: float) -> bool:
        """트랙 팬 설정"""
        return self.send_message("set_track_pan", {
            "track_index": track_index,
            "pan": pan
        })
    
    def mute_track(self, track_index: int, mute: bool = True) -> bool:
        """트랙 뮤트"""
        return self.send_message("mute_track", {
            "track_index": track_index,
            "mute": mute
        })
    
    def solo_track(self, track_index: int, solo: bool = True) -> bool:
        """트랙 솔로"""
        return self.send_message("solo_track", {
            "track_index": track_index,
            "solo": solo
        })
    
    def arm_track(self, track_index: int, arm: bool = True) -> bool:
        """트랙 녹음 준비"""
        return self.send_message("arm_track", {
            "track_index": track_index,
            "arm": arm
        })
    
    def load_instrument(self, track_index: int, instrument_name: str) -> bool:
        """트랙에 악기 로드"""
        return self.send_message("load_instrument", {
            "track_index": track_index,
            "instrument": instrument_name
        })
    
    def load_effect(self, track_index: int, effect_name: str, slot: int = 0) -> bool:
        """트랙에 이펙트 로드"""
        return self.send_message("load_effect", {
            "track_index": track_index,
            "effect": effect_name,
            "slot": slot
        })
    
    def set_device_parameter(self, track_index: int, device_index: int, 
                           parameter_index: int, value: float) -> bool:
        """디바이스 파라미터 설정"""
        return self.send_message("set_device_parameter", {
            "track_index": track_index,
            "device_index": device_index,
            "parameter_index": parameter_index,
            "value": value
        })
    
    def create_clip(self, track_index: int, scene_index: int, length: float) -> bool:
        """새 클립 생성"""
        return self.send_message("create_clip", {
            "track_index": track_index,
            "scene_index": scene_index,
            "length": length
        })
    
    def set_clip_notes(self, track_index: int, scene_index: int, 
                      notes: List[Dict[str, Any]]) -> bool:
        """클립에 노트 설정"""
        return self.send_message("set_clip_notes", {
            "track_index": track_index,
            "scene_index": scene_index,
            "notes": notes
        })
    
    def launch_clip(self, track_index: int, scene_index: int) -> bool:
        """클립 실행"""
        return self.send_message("launch_clip", {
            "track_index": track_index,
            "scene_index": scene_index
        })
    
    def stop_clip(self, track_index: int) -> bool:
        """클립 중지"""
        return self.send_message("stop_clip", {"track_index": track_index})
    
    def launch_scene(self, scene_index: int) -> bool:
        """씬 실행"""
        return self.send_message("launch_scene", {"scene_index": scene_index})
    
    def stop_all_clips(self) -> bool:
        """모든 클립 중지"""
        return self.send_message("stop_all_clips", {})
    
    def save_live_set(self, filepath: Optional[str] = None) -> bool:
        """Live 세트 저장"""
        data = {}
        if filepath:
            data["filepath"] = filepath
        return self.send_message("save_live_set", data)
    
    def load_live_set(self, filepath: str) -> bool:
        """Live 세트 로드"""
        return self.send_message("load_live_set", {"filepath": filepath})
    
    def export_audio(self, filepath: str, start_time: float = 0, 
                    end_time: Optional[float] = None) -> bool:
        """오디오 내보내기"""
        data = {
            "filepath": filepath,
            "start_time": start_time
        }
        if end_time is not None:
            data["end_time"] = end_time
        
        return self.send_message("export_audio", data)
    
    def send_midi_sequence(self, track_index: int, 
                          sequence: List[Dict[str, Any]]) -> bool:
        """MIDI 시퀀스 전송"""
        return self.send_message("send_midi_sequence", {
            "track_index": track_index,
            "sequence": sequence
        })
    
    def get_track_info(self, track_index: int) -> bool:
        """트랙 정보 조회"""
        return self.send_message("get_track_info", {"track_index": track_index})
    
    def get_all_tracks_info(self) -> bool:
        """모든 트랙 정보 조회"""
        return self.send_message("get_all_tracks_info", {})
    
    def set_quantization(self, quantization: str) -> bool:
        """클립 실행 퀀타이제이션 설정"""
        return self.send_message("set_quantization", {"quantization": quantization}) 