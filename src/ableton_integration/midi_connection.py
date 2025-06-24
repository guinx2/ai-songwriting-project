"""
MIDI 연결 및 통신 모듈
python-rtmidi를 사용하여 Ableton Live와 MIDI 통신
"""

import rtmidi
import mido
import time
import threading
from typing import List, Optional, Callable, Dict, Any
import logging

logger = logging.getLogger(__name__)


class MidiConnection:
    """MIDI 입출력 연결 관리 클래스"""
    
    def __init__(self):
        self.midi_in: Optional[rtmidi.MidiIn] = None
        self.midi_out: Optional[rtmidi.MidiOut] = None
        self.input_ports: Dict[str, int] = {}
        self.output_ports: Dict[str, int] = {}
        self.is_connected = False
        self.callback_functions: List[Callable] = []
        
    def scan_ports(self) -> Dict[str, Any]:
        """사용 가능한 MIDI 포트를 스캔"""
        try:
            # MIDI 입력 포트 스캔
            midi_in = rtmidi.MidiIn()
            input_ports = {}
            for i in range(midi_in.get_port_count()):
                port_name = midi_in.get_port_name(i)
                input_ports[port_name] = i
                
            # MIDI 출력 포트 스캔  
            midi_out = rtmidi.MidiOut()
            output_ports = {}
            for i in range(midi_out.get_port_count()):
                port_name = midi_out.get_port_name(i)
                output_ports[port_name] = i
                
            self.input_ports = input_ports
            self.output_ports = output_ports
            
            logger.info(f"MIDI 입력 포트 발견: {list(input_ports.keys())}")
            logger.info(f"MIDI 출력 포트 발견: {list(output_ports.keys())}")
            
            return {
                "input_ports": input_ports,
                "output_ports": output_ports,
                "total_input": len(input_ports),
                "total_output": len(output_ports)
            }
            
        except Exception as e:
            logger.error(f"MIDI 포트 스캔 실패: {e}")
            return {"error": str(e)}
    
    def connect_to_ableton(self, input_port: Optional[str] = None, output_port: Optional[str] = None) -> bool:
        """Ableton Live에 연결"""
        try:
            # 포트 스캔
            ports_info = self.scan_ports()
            if "error" in ports_info:
                return False
                
            # 자동으로 Ableton Live 포트 찾기
            if not input_port:
                for port_name in self.input_ports.keys():
                    if "ableton" in port_name.lower() or "live" in port_name.lower():
                        input_port = port_name
                        break
                        
            if not output_port:
                for port_name in self.output_ports.keys():
                    if "ableton" in port_name.lower() or "live" in port_name.lower():
                        output_port = port_name
                        break
            
            # MIDI 입력 연결
            if input_port and input_port in self.input_ports:
                self.midi_in = rtmidi.MidiIn()
                self.midi_in.open_port(self.input_ports[input_port])
                self.midi_in.set_callback(self._midi_callback)
                logger.info(f"MIDI 입력 연결됨: {input_port}")
            
            # MIDI 출력 연결
            if output_port and output_port in self.output_ports:
                self.midi_out = rtmidi.MidiOut()
                self.midi_out.open_port(self.output_ports[output_port])
                logger.info(f"MIDI 출력 연결됨: {output_port}")
            
            self.is_connected = bool(self.midi_in or self.midi_out)
            return self.is_connected
            
        except Exception as e:
            logger.error(f"Ableton Live 연결 실패: {e}")
            return False
    
    def _midi_callback(self, message, data):
        """MIDI 메시지 수신 콜백"""
        try:
            midi_message, delta_time = message
            logger.debug(f"MIDI 메시지 수신: {midi_message}, 시간: {delta_time}")
            
            # 등록된 콜백 함수들 실행
            for callback in self.callback_functions:
                callback(midi_message, delta_time)
                
        except Exception as e:
            logger.error(f"MIDI 콜백 처리 오류: {e}")
    
    def send_midi_message(self, message: List[int]) -> bool:
        """MIDI 메시지 전송"""
        try:
            if not self.midi_out:
                logger.warning("MIDI 출력이 연결되지 않음")
                return False
                
            self.midi_out.send_message(message)
            logger.debug(f"MIDI 메시지 전송: {message}")
            return True
            
        except Exception as e:
            logger.error(f"MIDI 메시지 전송 실패: {e}")
            return False
    
    def send_note_on(self, channel: int, note: int, velocity: int) -> bool:
        """Note On 메시지 전송"""
        message = [0x90 + channel - 1, note, velocity]  # channel은 1-16, MIDI는 0-15
        return self.send_midi_message(message)
    
    def send_note_off(self, channel: int, note: int, velocity: int = 64) -> bool:
        """Note Off 메시지 전송"""
        message = [0x80 + channel - 1, note, velocity]
        return self.send_midi_message(message)
    
    def send_control_change(self, channel: int, controller: int, value: int) -> bool:
        """Control Change 메시지 전송"""
        message = [0xB0 + channel - 1, controller, value]
        return self.send_midi_message(message)
    
    def play_midi_sequence(self, notes: List[Dict], tempo: int = 120) -> None:
        """MIDI 시퀀스 재생"""
        def play_sequence():
            try:
                beat_duration = 60.0 / tempo  # BPM을 초로 변환
                
                for note_info in notes:
                    note = note_info.get('note', 60)
                    velocity = note_info.get('velocity', 80)
                    duration = note_info.get('duration', 0.5)
                    channel = note_info.get('channel', 1)
                    
                    # Note On
                    self.send_note_on(channel, note, velocity)
                    
                    # 지속 시간
                    time.sleep(duration * beat_duration)
                    
                    # Note Off
                    self.send_note_off(channel, note)
                    
                    # 다음 노트까지 간격
                    gap = note_info.get('gap', 0.1)
                    time.sleep(gap * beat_duration)
                    
            except Exception as e:
                logger.error(f"MIDI 시퀀스 재생 오류: {e}")
        
        # 별도 스레드에서 재생
        play_thread = threading.Thread(target=play_sequence)
        play_thread.daemon = True
        play_thread.start()
    
    def add_callback(self, callback_func: Callable) -> None:
        """MIDI 메시지 수신 콜백 추가"""
        self.callback_functions.append(callback_func)
    
    def disconnect(self) -> None:
        """MIDI 연결 해제"""
        try:
            if self.midi_in:
                self.midi_in.close_port()
                self.midi_in = None
                
            if self.midi_out:
                self.midi_out.close_port()
                self.midi_out = None
                
            self.is_connected = False
            logger.info("MIDI 연결 해제됨")
            
        except Exception as e:
            logger.error(f"MIDI 연결 해제 오류: {e}")
    
    def get_connection_status(self) -> Dict[str, Any]:
        """연결 상태 정보 반환"""
        return {
            "is_connected": self.is_connected,
            "has_input": bool(self.midi_in),
            "has_output": bool(self.midi_out),
            "available_input_ports": list(self.input_ports.keys()),
            "available_output_ports": list(self.output_ports.keys()),
            "callback_count": len(self.callback_functions)
        }
    
    def __del__(self):
        """소멸자 - 연결 정리"""
        self.disconnect()


# 전역 MIDI 연결 인스턴스
global_midi_connection = MidiConnection()


def get_midi_connection() -> MidiConnection:
    """전역 MIDI 연결 인스턴스 반환"""
    return global_midi_connection 