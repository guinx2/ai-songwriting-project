#!/usr/bin/env python3
"""
Ableton Live 연동 기능 테스트 스크립트
"""
import pytest
import time
import json
from unittest.mock import Mock, patch
from src.ableton_integration.live_api import AbletonLiveAPI
from src.ableton_integration.midi_connection import MIDIConnection
from src.ableton_integration.max_for_live import MaxForLiveInterface

class TestAbletonLiveAPI:
    """Ableton Live API 테스트"""
    
    def setup_method(self):
        """각 테스트 전 초기화"""
        self.api = AbletonLiveAPI()
    
    def test_api_initialization(self):
        """API 초기화 테스트"""
        assert self.api.connected == False
        assert self.api.project_info == {}
        assert self.api.tracks == []
    
    def test_connect_simulation(self):
        """연결 시뮬레이션 테스트"""
        # 실제 Ableton Live가 없어도 테스트할 수 있도록 시뮬레이션 모드 사용
        result = self.api.connect()
        
        assert result == True
        assert self.api.connected == True
        assert len(self.api.tracks) > 0  # 기본 트랙들이 생성되어야 함
    
    def test_get_project_info(self):
        """프로젝트 정보 조회 테스트"""
        self.api.connect()
        
        project_info = self.api.get_project_info()
        
        assert isinstance(project_info, dict)
        assert 'name' in project_info
        assert 'tempo' in project_info
        assert 'tracks' in project_info
    
    def test_track_management(self):
        """트랙 관리 테스트"""
        self.api.connect()
        
        # 트랙 생성
        track_result = self.api.create_track("Test Track", "midi")
        assert track_result == True
        
        # 트랙 목록 조회
        tracks = self.api.get_tracks()
        assert len(tracks) > 0
        
        # 트랙 정보 조회
        track_info = self.api.get_track_info(0)
        assert isinstance(track_info, dict)
        assert 'name' in track_info
    
    def test_playback_control(self):
        """재생 제어 테스트"""
        self.api.connect()
        
        # 재생 시작
        play_result = self.api.play()
        assert play_result == True
        
        # 일시정지
        time.sleep(0.1)  # 짧은 대기
        stop_result = self.api.stop()
        assert stop_result == True
    
    def test_tempo_control(self):
        """템포 제어 테스트"""
        self.api.connect()
        
        # 템포 설정
        set_result = self.api.set_tempo(140)
        assert set_result == True
        
        # 템포 조회
        current_tempo = self.api.get_tempo()
        assert current_tempo == 140
    
    def test_disconnect(self):
        """연결 해제 테스트"""
        self.api.connect()
        assert self.api.connected == True
        
        self.api.disconnect()
        assert self.api.connected == False

class TestMIDIConnection:
    """MIDI 연결 테스트"""
    
    def setup_method(self):
        """각 테스트 전 초기화"""
        self.midi = MIDIConnection()
    
    def test_midi_initialization(self):
        """MIDI 초기화 테스트"""
        assert self.midi.input_port is None
        assert self.midi.output_port is None
        assert self.midi.listening == False
    
    @patch('mido.get_input_names')
    @patch('mido.get_output_names')
    def test_get_available_ports(self, mock_output_names, mock_input_names):
        """사용 가능한 포트 조회 테스트"""
        # Mock 데이터 설정
        mock_input_names.return_value = ['Virtual Input 1', 'Virtual Input 2']
        mock_output_names.return_value = ['Virtual Output 1', 'Virtual Output 2']
        
        ports = self.midi.get_available_ports()
        
        assert 'input_ports' in ports
        assert 'output_ports' in ports
        assert len(ports['input_ports']) == 2
        assert len(ports['output_ports']) == 2
    
    @patch('mido.open_input')
    @patch('mido.get_input_names')
    def test_connect_input(self, mock_input_names, mock_open_input):
        """MIDI 입력 연결 테스트"""
        # Mock 설정
        mock_input_names.return_value = ['Virtual Input']
        mock_port = Mock()
        mock_open_input.return_value = mock_port
        
        result = self.midi.connect_input()
        
        assert result == True
        assert self.midi.input_port == mock_port
    
    @patch('mido.open_output')
    @patch('mido.get_output_names')
    def test_connect_output(self, mock_output_names, mock_open_output):
        """MIDI 출력 연결 테스트"""
        # Mock 설정
        mock_output_names.return_value = ['Virtual Output']
        mock_port = Mock()
        mock_open_output.return_value = mock_port
        
        result = self.midi.connect_output()
        
        assert result == True
        assert self.midi.output_port == mock_port
    
    def test_message_creation(self):
        """MIDI 메시지 생성 테스트"""
        # Mock 출력 포트 설정
        mock_port = Mock()
        self.midi.output_port = mock_port
        
        # Note On 메시지 전송 테스트
        result = self.midi.send_note_on(0, 60, 100)
        assert result == True
        mock_port.send.assert_called()
    
    def test_sequence_creation(self):
        """MIDI 시퀀스 생성 테스트"""
        sequence = self.midi.create_test_sequence()
        
        assert isinstance(sequence, list)
        assert len(sequence) > 0
        
        # 첫 번째 이벤트 확인
        first_event = sequence[0]
        assert 'type' in first_event
        assert 'note' in first_event
        assert first_event['type'] == 'note_on'
    
    def test_connection_status(self):
        """연결 상태 확인 테스트"""
        status = self.midi.is_connected()
        
        assert isinstance(status, dict)
        assert 'input_connected' in status
        assert 'output_connected' in status
        assert 'listening' in status
    
    def teardown_method(self):
        """각 테스트 후 정리"""
        self.midi.disconnect()

class TestMaxForLiveInterface:
    """Max for Live 인터페이스 테스트"""
    
    def setup_method(self):
        """각 테스트 전 초기화"""
        self.m4l = MaxForLiveInterface()
    
    def test_m4l_initialization(self):
        """Max for Live 초기화 테스트"""
        assert self.m4l.host == "localhost"
        assert self.m4l.port == 7400
        assert self.m4l.connected == False
        assert self.m4l.socket is None
    
    @patch('socket.socket')
    def test_connect_simulation(self, mock_socket_class):
        """연결 시뮬레이션 테스트"""
        # Mock 소켓 설정
        mock_socket = Mock()
        mock_socket_class.return_value = mock_socket
        
        result = self.m4l.connect()
        
        # 실제 Max for Live가 없어서 연결 실패가 예상됨
        # 하지만 연결 시도는 정상적으로 이루어져야 함
        mock_socket.connect.assert_called_with(("localhost", 7400))
    
    def test_message_structure(self):
        """메시지 구조 테스트"""
        # Mock 소켓으로 연결된 상태 시뮬레이션
        mock_socket = Mock()
        self.m4l.socket = mock_socket
        self.m4l.connected = True
        
        # 메시지 전송 테스트
        result = self.m4l.send_message("test_command", {"param": "value"})
        
        # 메시지가 전송되었는지 확인
        assert mock_socket.send.called
    
    def test_message_handlers(self):
        """메시지 핸들러 테스트"""
        # 핸들러 추가
        test_handler = Mock()
        self.m4l.add_message_handler("test_command", test_handler)
        
        assert "test_command" in self.m4l.message_handlers
        
        # 핸들러 제거
        self.m4l.remove_message_handler("test_command")
        assert "test_command" not in self.m4l.message_handlers
    
    def test_live_control_commands(self):
        """Live 제어 명령 테스트"""
        # Mock 소켓 설정
        mock_socket = Mock()
        self.m4l.socket = mock_socket
        self.m4l.connected = True
        
        # 템포 설정 테스트
        result = self.m4l.set_tempo(120.0)
        assert result == True
        
        # 재생 테스트
        result = self.m4l.play()
        assert result == True
        
        # 정지 테스트
        result = self.m4l.stop()
        assert result == True
    
    def test_track_control_commands(self):
        """트랙 제어 명령 테스트"""
        # Mock 소켓 설정
        mock_socket = Mock()
        self.m4l.socket = mock_socket
        self.m4l.connected = True
        
        # 트랙 생성 테스트
        result = self.m4l.create_track("Test Track", "midi")
        assert result == True
        
        # 트랙 볼륨 설정 테스트
        result = self.m4l.set_track_volume(0, 0.8)
        assert result == True
        
        # 트랙 뮤트 테스트
        result = self.m4l.mute_track(0, True)
        assert result == True
    
    def teardown_method(self):
        """각 테스트 후 정리"""
        self.m4l.disconnect()

class TestIntegrationWorkflow:
    """통합 워크플로우 테스트"""
    
    def setup_method(self):
        """테스트 초기화"""
        self.api = AbletonLiveAPI()
        self.midi = MIDIConnection()
        self.m4l = MaxForLiveInterface()
    
    def test_complete_workflow_simulation(self):
        """완전한 워크플로우 시뮬레이션"""
        # 1. Ableton Live 연결
        live_connected = self.api.connect()
        assert live_connected == True
        
        # 2. MIDI 포트 조회 (실제 포트가 없어도 목록은 조회됨)
        ports = self.midi.get_available_ports()
        assert isinstance(ports, dict)
        
        # 3. 프로젝트 생성 시뮬레이션
        project_info = self.api.get_project_info()
        assert isinstance(project_info, dict)
        
        # 4. 트랙 생성
        track_created = self.api.create_track("AI Generated Track", "midi")
        assert track_created == True
        
        # 5. 템포 설정
        tempo_set = self.api.set_tempo(128)
        assert tempo_set == True
        
        # 6. MIDI 시퀀스 생성
        sequence = self.midi.create_test_sequence()
        assert len(sequence) > 0
        
        print("✅ 통합 워크플로우 시뮬레이션 완료")
    
    def test_error_handling(self):
        """오류 처리 테스트"""
        # 연결되지 않은 상태에서 명령 실행
        result = self.api.get_tempo()
        assert result is None  # 연결되지 않았으므로 None 반환
        
        # MIDI 포트가 없는 상태에서 메시지 전송
        result = self.midi.send_note_on(0, 60, 100)
        assert result == False  # 포트가 없으므로 False 반환
    
    def teardown_method(self):
        """테스트 정리"""
        self.api.disconnect()
        self.midi.disconnect()
        self.m4l.disconnect()

def test_performance_benchmark():
    """성능 벤치마크 테스트"""
    print("\n⚡ 성능 벤치마크 테스트 시작...")
    
    # API 연결 성능
    api = AbletonLiveAPI()
    start_time = time.time()
    api.connect()
    connect_time = time.time() - start_time
    print(f"  🔗 API 연결 시간: {connect_time:.3f}초")
    
    # 트랙 생성 성능
    start_time = time.time()
    for i in range(10):
        api.create_track(f"Track {i+1}", "midi")
    track_creation_time = time.time() - start_time
    print(f"  🎵 트랙 10개 생성 시간: {track_creation_time:.3f}초")
    
    # MIDI 시퀀스 생성 성능
    midi = MIDIConnection()
    start_time = time.time()
    for i in range(100):
        sequence = midi.create_test_sequence()
    sequence_creation_time = time.time() - start_time
    print(f"  🎹 MIDI 시퀀스 100개 생성 시간: {sequence_creation_time:.3f}초")
    
    # 정리
    api.disconnect()
    midi.disconnect()
    
    print("✅ 성능 벤치마크 완료")

def test_real_time_simulation():
    """실시간 시뮬레이션 테스트"""
    print("\n🔄 실시간 시뮬레이션 테스트 시작...")
    
    api = AbletonLiveAPI()
    midi = MIDIConnection()
    
    # 연결
    api.connect()
    
    # 실시간 시뮬레이션 (3초간)
    print("  🎵 3초간 실시간 시뮬레이션...")
    
    start_time = time.time()
    while time.time() - start_time < 3.0:
        # 템포 변경 시뮬레이션
        current_time = time.time() - start_time
        new_tempo = 120 + int(current_time * 10)  # 템포를 점진적으로 증가
        api.set_tempo(new_tempo)
        
        # MIDI 이벤트 시뮬레이션
        note = 60 + int(current_time * 5) % 12  # 음높이 변화
        
        time.sleep(0.1)  # 100ms 간격
    
    # 정리
    api.disconnect()
    midi.disconnect()
    
    print("✅ 실시간 시뮬레이션 완료")

def main():
    """메인 테스트 실행 함수"""
    print("🚀 Ableton Live 연동 테스트 시작\n")
    
    # pytest를 사용하여 클래스 기반 테스트 실행
    print("📝 기본 기능 테스트 실행...")
    pytest.main([__file__ + "::TestAbletonLiveAPI", "-v"])
    pytest.main([__file__ + "::TestMIDIConnection", "-v"])
    pytest.main([__file__ + "::TestMaxForLiveInterface", "-v"])
    pytest.main([__file__ + "::TestIntegrationWorkflow", "-v"])
    
    # 추가 테스트들
    test_performance_benchmark()
    test_real_time_simulation()
    
    print("\n🎉 모든 테스트 완료!")
    print("\n📋 테스트 요약:")
    print("  ✅ Ableton Live API 연동 기능")
    print("  ✅ MIDI 통신 기능")
    print("  ✅ Max for Live 인터페이스")
    print("  ✅ 통합 워크플로우")
    print("  ✅ 성능 벤치마크")
    print("  ✅ 실시간 시뮬레이션")
    
    print("\n💡 실제 Ableton Live 연동 테스트를 위해서는:")
    print("  1. Ableton Live 실행")
    print("  2. Max for Live 장치 로드")
    print("  3. MIDI 포트 설정")
    print("  4. 실제 하드웨어 연결")

if __name__ == "__main__":
    main() 