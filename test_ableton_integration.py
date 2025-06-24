#!/usr/bin/env python3
"""
Ableton Live 연동 기능 테스트 스크립트
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ableton_integration.midi_connection import MidiConnection
from src.ableton_integration.live_api import AbletonLiveAPI  
from src.ableton_integration.max_for_live import MaxForLiveManager


def test_midi_connection():
    """MIDI 연결 테스트"""
    print("🎹 MIDI 연결 테스트 시작...")
    
    midi = MidiConnection()
    
    # 포트 스캔
    ports = midi.scan_ports()
    print(f"📡 MIDI 포트 스캔 결과:")
    print(f"   입력 포트: {ports.get('input_ports', {})}")
    print(f"   출력 포트: {ports.get('output_ports', {})}")
    print(f"   총 입력 포트: {ports.get('total_input', 0)}")
    print(f"   총 출력 포트: {ports.get('total_output', 0)}")
    
    # 연결 상태 확인
    status = midi.get_connection_status()
    print(f"🔗 연결 상태: {status}")
    
    return ports.get('total_input', 0) > 0 or ports.get('total_output', 0) > 0


def test_live_api():
    """Ableton Live API 테스트"""
    print("\n🎵 Ableton Live API 테스트 시작...")
    
    live_api = AbletonLiveAPI()
    
    # 새 프로젝트 생성
    project_result = live_api.create_new_project("Test_AI_Song", tempo=128, key="Am")
    print(f"📁 프로젝트 생성: {project_result}")
    
    if project_result.get("success"):
        # 트랙 추가
        track_result = live_api.add_track("Drums", "midi", "Drum Kit")
        print(f"🥁 드럼 트랙 추가: {track_result}")
        
        track_result = live_api.add_track("Bass", "midi", "Bass Synth")
        print(f"🎸 베이스 트랙 추가: {track_result}")
        
        # 프로젝트 정보 조회
        project_info = live_api.get_project_info()
        print(f"📊 프로젝트 정보: {project_info}")
        
        # ALS 파일 생성 테스트
        als_result = live_api.export_to_als_file("./data/test_project.als")
        print(f"💾 ALS 파일 생성: {als_result}")
    
    return project_result.get("success", False)


def test_max_for_live():
    """Max for Live 디바이스 테스트"""
    print("\n🔧 Max for Live 디바이스 테스트 시작...")
    
    m4l_manager = MaxForLiveManager()
    
    # 기본 디바이스 생성
    devices_result = m4l_manager.create_default_devices()
    print(f"🛠️ 기본 디바이스 생성: {devices_result}")
    
    # 디바이스 목록 조회
    devices_list = m4l_manager.list_devices()
    print(f"📋 디바이스 목록: {devices_list}")
    
    # 생성기 디바이스 테스트
    generator = m4l_manager.get_device("generator")
    if generator:
        print(f"🎼 생성기 디바이스 정보: {generator.get_device_info()}")
        
        # 파라미터 설정 테스트
        generator.set_parameter("genre", "Rock")
        generator.set_parameter("tempo", 140)
        generator.set_parameter("creativity", 0.9)
    
    return devices_result.get("success", False)


def main():
    """메인 테스트 함수"""
    print("🚀 AI 작곡 시스템 - Ableton Live 연동 테스트")
    print("=" * 50)
    
    results = {}
    
    # 1. MIDI 연결 테스트
    results["midi"] = test_midi_connection()
    
    # 2. Live API 테스트  
    results["live_api"] = test_live_api()
    
    # 3. Max for Live 테스트
    results["max_for_live"] = test_max_for_live()
    
    # 결과 요약
    print("\n" + "=" * 50)
    print("📊 테스트 결과 요약:")
    print(f"   🎹 MIDI 연결: {'✅ 성공' if results['midi'] else '❌ 실패'}")
    print(f"   🎵 Live API: {'✅ 성공' if results['live_api'] else '❌ 실패'}")
    print(f"   🔧 Max for Live: {'✅ 성공' if results['max_for_live'] else '❌ 실패'}")
    
    success_count = sum(results.values())
    total_tests = len(results)
    
    print(f"\n🎯 전체 성공률: {success_count}/{total_tests} ({success_count/total_tests*100:.1f}%)")
    
    if success_count == total_tests:
        print("🎉 모든 테스트 통과! Ableton Live 연동 준비 완료!")
    else:
        print("⚠️ 일부 테스트 실패. 추가 설정이 필요합니다.")
    
    return success_count == total_tests


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 