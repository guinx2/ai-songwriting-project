"""
MIDI 연결 및 통신 관리
"""
import mido
import time
from typing import List, Optional, Dict, Any, Callable
from threading import Thread, Event
import queue

class MIDIConnection:
    """MIDI 장치와의 연결 및 통신을 관리하는 클래스"""
    
    def __init__(self):
        """MIDI 연결 초기화"""
        self.input_port: Optional[mido.ports.BaseInput] = None
        self.output_port: Optional[mido.ports.BaseOutput] = None
        self.listening = False
        self.listen_thread: Optional[Thread] = None
        self.stop_event = Event()
        self.message_queue = queue.Queue()
        self.message_callbacks: List[Callable] = []
        
    def get_available_ports(self) -> Dict[str, List[str]]:
        """사용 가능한 MIDI 포트 목록 반환"""
        return {
            "input_ports": mido.get_input_names(),
            "output_ports": mido.get_output_names()
        }
    
    def connect_input(self, port_name: Optional[str] = None) -> bool:
        """MIDI 입력 포트 연결"""
        try:
            if port_name is None:
                # 첫 번째 사용 가능한 포트 사용
                input_names = mido.get_input_names()
                if not input_names:
                    print("사용 가능한 MIDI 입력 포트가 없습니다")
                    return False
                port_name = input_names[0]
            
            self.input_port = mido.open_input(port_name)
            print(f"MIDI 입력 포트 '{port_name}' 연결 성공")
            return True
            
        except Exception as e:
            print(f"MIDI 입력 포트 연결 실패: {e}")
            return False
    
    def connect_output(self, port_name: Optional[str] = None) -> bool:
        """MIDI 출력 포트 연결"""
        try:
            if port_name is None:
                # 첫 번째 사용 가능한 포트 사용
                output_names = mido.get_output_names()
                if not output_names:
                    print("사용 가능한 MIDI 출력 포트가 없습니다")
                    return False
                port_name = output_names[0]
            
            self.output_port = mido.open_output(port_name)
            print(f"MIDI 출력 포트 '{port_name}' 연결 성공")
            return True
            
        except Exception as e:
            print(f"MIDI 출력 포트 연결 실패: {e}")
            return False
    
    def disconnect(self):
        """모든 MIDI 연결 해제"""
        self.stop_listening()
        
        if self.input_port:
            self.input_port.close()
            self.input_port = None
            print("MIDI 입력 포트 연결 해제")
        
        if self.output_port:
            self.output_port.close()
            self.output_port = None
            print("MIDI 출력 포트 연결 해제")
    
    def is_connected(self) -> Dict[str, bool]:
        """연결 상태 확인"""
        return {
            "input_connected": self.input_port is not None,
            "output_connected": self.output_port is not None,
            "listening": self.listening
        }
    
    def send_message(self, message: mido.Message) -> bool:
        """MIDI 메시지 전송"""
        if not self.output_port:
            print("MIDI 출력 포트가 연결되지 않음")
            return False
        
        try:
            self.output_port.send(message)
            return True
        except Exception as e:
            print(f"MIDI 메시지 전송 실패: {e}")
            return False
    
    def send_note_on(self, channel: int, note: int, velocity: int) -> bool:
        """Note On 메시지 전송"""
        message = mido.Message('note_on', channel=channel, note=note, velocity=velocity)
        return self.send_message(message)
    
    def send_note_off(self, channel: int, note: int, velocity: int = 64) -> bool:
        """Note Off 메시지 전송"""
        message = mido.Message('note_off', channel=channel, note=note, velocity=velocity)
        return self.send_message(message)
    
    def send_control_change(self, channel: int, control: int, value: int) -> bool:
        """Control Change 메시지 전송"""
        message = mido.Message('control_change', channel=channel, control=control, value=value)
        return self.send_message(message)
    
    def send_program_change(self, channel: int, program: int) -> bool:
        """Program Change 메시지 전송"""
        message = mido.Message('program_change', channel=channel, program=program)
        return self.send_message(message)
    
    def add_message_callback(self, callback: Callable[[mido.Message], None]):
        """메시지 수신 콜백 추가"""
        self.message_callbacks.append(callback)
    
    def remove_message_callback(self, callback: Callable[[mido.Message], None]):
        """메시지 수신 콜백 제거"""
        if callback in self.message_callbacks:
            self.message_callbacks.remove(callback)
    
    def start_listening(self) -> bool:
        """MIDI 메시지 수신 시작"""
        if not self.input_port:
            print("MIDI 입력 포트가 연결되지 않음")
            return False
        
        if self.listening:
            print("이미 MIDI 메시지를 수신 중입니다")
            return True
        
        self.stop_event.clear()
        self.listening = True
        self.listen_thread = Thread(target=self._listen_messages, daemon=True)
        self.listen_thread.start()
        
        print("MIDI 메시지 수신 시작")
        return True
    
    def stop_listening(self):
        """MIDI 메시지 수신 중지"""
        if not self.listening:
            return
        
        self.listening = False
        self.stop_event.set()
        
        if self.listen_thread:
            self.listen_thread.join(timeout=1.0)
            self.listen_thread = None
        
        print("MIDI 메시지 수신 중지")
    
    def _listen_messages(self):
        """MIDI 메시지 수신 스레드"""
        try:
            while self.listening and not self.stop_event.is_set():
                # 메시지 수신 (타임아웃 설정)
                try:
                    for message in self.input_port.iter_pending():
                        if not self.listening:
                            break
                        
                        # 메시지를 큐에 저장
                        self.message_queue.put(message)
                        
                        # 콜백 함수들 호출
                        for callback in self.message_callbacks:
                            try:
                                callback(message)
                            except Exception as e:
                                print(f"MIDI 메시지 콜백 오류: {e}")
                    
                    time.sleep(0.001)  # CPU 사용량 제한
                    
                except Exception as e:
                    print(f"MIDI 메시지 수신 오류: {e}")
                    time.sleep(0.1)
                    
        except Exception as e:
            print(f"MIDI 수신 스레드 오류: {e}")
        finally:
            self.listening = False
    
    def get_recent_messages(self, count: int = 10) -> List[Dict[str, Any]]:
        """최근 수신된 메시지들 반환"""
        messages = []
        temp_messages = []
        
        # 큐에서 메시지들 가져오기
        while not self.message_queue.empty() and len(temp_messages) < count * 2:
            try:
                message = self.message_queue.get_nowait()
                temp_messages.append(message)
            except queue.Empty:
                break
        
        # 최근 메시지들만 선택
        recent_messages = temp_messages[-count:] if len(temp_messages) > count else temp_messages
        
        # 딕셔너리 형태로 변환
        for msg in recent_messages:
            messages.append({
                "type": msg.type,
                "channel": getattr(msg, 'channel', None),
                "note": getattr(msg, 'note', None),
                "velocity": getattr(msg, 'velocity', None),
                "control": getattr(msg, 'control', None),
                "value": getattr(msg, 'value', None),
                "program": getattr(msg, 'program', None),
                "time": time.time()
            })
        
        return messages
    
    def play_sequence(self, sequence: List[Dict[str, Any]], tempo: int = 120) -> bool:
        """MIDI 시퀀스 재생"""
        if not self.output_port:
            print("MIDI 출력 포트가 연결되지 않음")
            return False
        
        try:
            # BPM을 초당 틱으로 변환
            ticks_per_second = (tempo * 480) / 60  # 480 ticks per quarter note
            
            for event in sequence:
                # 이벤트 타입에 따라 메시지 생성
                if event['type'] == 'note_on':
                    message = mido.Message(
                        'note_on',
                        channel=event.get('channel', 0),
                        note=event.get('note', 60),
                        velocity=event.get('velocity', 64)
                    )
                elif event['type'] == 'note_off':
                    message = mido.Message(
                        'note_off',
                        channel=event.get('channel', 0),
                        note=event.get('note', 60),
                        velocity=event.get('velocity', 64)
                    )
                elif event['type'] == 'control_change':
                    message = mido.Message(
                        'control_change',
                        channel=event.get('channel', 0),
                        control=event.get('control', 0),
                        value=event.get('value', 0)
                    )
                else:
                    continue
                
                # 메시지 전송
                self.send_message(message)
                
                # 다음 이벤트까지 대기
                if 'delay' in event:
                    time.sleep(event['delay'])
            
            return True
            
        except Exception as e:
            print(f"MIDI 시퀀스 재생 실패: {e}")
            return False
    
    def create_test_sequence(self) -> List[Dict[str, Any]]:
        """테스트용 MIDI 시퀀스 생성"""
        sequence = []
        
        # C 메이저 스케일
        notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C4-C5
        
        for note in notes:
            # Note On
            sequence.append({
                'type': 'note_on',
                'channel': 0,
                'note': note,
                'velocity': 80,
                'delay': 0
            })
            
            # Note Off (0.5초 후)
            sequence.append({
                'type': 'note_off',
                'channel': 0,
                'note': note,
                'velocity': 80,
                'delay': 0.5
            })
        
        return sequence 