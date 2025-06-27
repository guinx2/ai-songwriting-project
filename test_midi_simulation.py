#!/usr/bin/env python3
"""
MIDI 시뮬레이션 및 테스트 스크립트
"""
import time
import mido
import random
from pathlib import Path
from typing import List, Dict, Any

class MIDISimulator:
    """MIDI 시뮬레이션 클래스"""
    
    def __init__(self):
        """초기화"""
        self.sequences = []
        self.current_tempo = 120
        
    def generate_test_midi(self, output_path: str = "test_output/test_midi.mid"):
        """테스트용 MIDI 파일 생성"""
        print("🎹 테스트 MIDI 파일 생성 중...")
        
        # 출력 디렉토리 생성
        Path(output_path).parent.mkdir(exist_ok=True)
        
        # MIDI 파일 생성
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)
        
        # 메타데이터 추가
        track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(self.current_tempo)))
        track.append(mido.MetaMessage('track_name', name='AI Generated Track'))
        
        # C 메이저 스케일 노트들
        notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C4-C5
        
        time_elapsed = 0
        for i, note in enumerate(notes):
            # Note On
            track.append(mido.Message('note_on', channel=0, note=note, velocity=80, time=0))
            time_elapsed += 480  # 4분음표 길이
            
            # Note Off
            track.append(mido.Message('note_off', channel=0, note=note, velocity=80, time=480))
        
        # 파일 저장
        mid.save(output_path)
        print(f"✅ MIDI 파일 저장됨: {output_path}")
        
        return output_path
    
    def create_drum_pattern(self) -> List[Dict[str, Any]]:
        """드럼 패턴 생성"""
        pattern = []
        
        # 킥 드럼 (C1 = 36)
        kick_notes = [0, 480, 960, 1440]  # 4/4박자
        for time in kick_notes:
            pattern.append({
                'type': 'note_on',
                'channel': 9,  # 드럼 채널
                'note': 36,
                'velocity': 100,
                'time': time
            })
            pattern.append({
                'type': 'note_off',
                'channel': 9,
                'note': 36,
                'velocity': 0,
                'time': time + 100
            })
        
        # 스네어 드럼 (D1 = 38)
        snare_notes = [480, 1440]  # 2, 4박
        for time in snare_notes:
            pattern.append({
                'type': 'note_on',
                'channel': 9,
                'note': 38,
                'velocity': 90,
                'time': time
            })
            pattern.append({
                'type': 'note_off',
                'channel': 9,
                'note': 38,
                'velocity': 0,
                'time': time + 100
            })
        
        # 하이햇 (F#1 = 42)
        hihat_notes = [0, 240, 480, 720, 960, 1200, 1440, 1680]  # 8분음표
        for time in hihat_notes:
            pattern.append({
                'type': 'note_on',
                'channel': 9,
                'note': 42,
                'velocity': 60,
                'time': time
            })
            pattern.append({
                'type': 'note_off',
                'channel': 9,
                'note': 42,
                'velocity': 0,
                'time': time + 50
            })
        
        return sorted(pattern, key=lambda x: x['time'])
    
    def create_bass_line(self) -> List[Dict[str, Any]]:
        """베이스 라인 생성"""
        pattern = []
        
        # C 메이저 스케일의 베이스 노트들 (낮은 옥타브)
        bass_notes = [36, 38, 40, 41, 43, 45, 47, 48]  # C2-C3
        note_times = [0, 480, 960, 1440]  # 4분음표
        
        for i, time in enumerate(note_times):
            note = bass_notes[i % len(bass_notes)]
            
            pattern.append({
                'type': 'note_on',
                'channel': 1,
                'note': note,
                'velocity': 80,
                'time': time
            })
            pattern.append({
                'type': 'note_off',
                'channel': 1,
                'note': note,
                'velocity': 0,
                'time': time + 400
            })
        
        return pattern
    
    def create_chord_progression(self) -> List[Dict[str, Any]]:
        """코드 진행 생성"""
        pattern = []
        
        # C-Am-F-G 진행
        chords = [
            [60, 64, 67],  # C major (C-E-G)
            [57, 60, 64],  # A minor (A-C-E)
            [53, 57, 60],  # F major (F-A-C)
            [55, 59, 62]   # G major (G-B-D)
        ]
        
        chord_times = [0, 960, 1920, 2880]  # 2분음표
        
        for chord_idx, time in enumerate(chord_times):
            chord = chords[chord_idx]
            
            # 코드 노트들을 동시에 연주
            for note in chord:
                pattern.append({
                    'type': 'note_on',
                    'channel': 2,
                    'note': note,
                    'velocity': 70,
                    'time': time
                })
            
            # 코드 노트들을 동시에 해제
            for note in chord:
                pattern.append({
                    'type': 'note_off',
                    'channel': 2,
                    'note': note,
                    'velocity': 0,
                    'time': time + 800
                })
        
        return pattern
    
    def create_melody_line(self) -> List[Dict[str, Any]]:
        """멜로디 라인 생성"""
        pattern = []
        
        # C 메이저 스케일의 멜로디
        melody_notes = [72, 74, 76, 77, 79, 81, 83, 84]  # C5-C6
        note_durations = [240, 240, 480, 240, 240, 480, 240, 240]  # 다양한 길이
        
        time_offset = 0
        for i, (note, duration) in enumerate(zip(melody_notes, note_durations)):
            pattern.append({
                'type': 'note_on',
                'channel': 3,
                'note': note,
                'velocity': 85,
                'time': time_offset
            })
            pattern.append({
                'type': 'note_off',
                'channel': 3,
                'note': note,
                'velocity': 0,
                'time': time_offset + duration - 50
            })
            
            time_offset += duration
        
        return pattern
    
    def generate_complete_track(self, output_path: str = "test_output/complete_track.mid"):
        """완전한 트랙 생성"""
        print("🎵 완전한 트랙 생성 중...")
        
        # 출력 디렉토리 생성
        Path(output_path).parent.mkdir(exist_ok=True)
        
        # MIDI 파일 생성
        mid = mido.MidiFile()
        
        # 각 파트별 트랙 생성
        tracks_data = [
            ("Drums", self.create_drum_pattern()),
            ("Bass", self.create_bass_line()),
            ("Chords", self.create_chord_progression()),
            ("Melody", self.create_melody_line())
        ]
        
        for track_name, pattern in tracks_data:
            track = mido.MidiTrack()
            mid.tracks.append(track)
            
            # 트랙 메타데이터
            track.append(mido.MetaMessage('track_name', name=track_name))
            track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(self.current_tempo)))
            
            # 패턴을 MIDI 메시지로 변환
            last_time = 0
            for event in pattern:
                delta_time = event['time'] - last_time
                
                if event['type'] == 'note_on':
                    track.append(mido.Message(
                        'note_on',
                        channel=event['channel'],
                        note=event['note'],
                        velocity=event['velocity'],
                        time=delta_time
                    ))
                elif event['type'] == 'note_off':
                    track.append(mido.Message(
                        'note_off',
                        channel=event['channel'],
                        note=event['note'],
                        velocity=event['velocity'],
                        time=delta_time
                    ))
                
                last_time = event['time']
        
        # 파일 저장
        mid.save(output_path)
        print(f"✅ 완전한 트랙 저장됨: {output_path}")
        
        return output_path
    
    def analyze_midi_file(self, filepath: str):
        """MIDI 파일 분석"""
        print(f"\n🔍 MIDI 파일 분석: {filepath}")
        
        try:
            mid = mido.MidiFile(filepath)
            
            print(f"  📊 기본 정보:")
            print(f"    - 타입: {mid.type}")
            print(f"    - 트랙 수: {len(mid.tracks)}")
            print(f"    - 틱 단위: {mid.ticks_per_beat}")
            print(f"    - 총 길이: {mid.length:.2f}초")
            
            # 각 트랙 분석
            for i, track in enumerate(mid.tracks):
                print(f"\n  🎵 트랙 {i}:")
                
                note_count = 0
                tempo = None
                track_name = f"Track {i}"
                
                for msg in track:
                    if msg.type == 'note_on' and msg.velocity > 0:
                        note_count += 1
                    elif msg.type == 'set_tempo':
                        tempo = mido.tempo2bpm(msg.tempo)
                    elif msg.type == 'track_name':
                        track_name = msg.name
                
                print(f"    - 이름: {track_name}")
                print(f"    - 노트 수: {note_count}")
                if tempo:
                    print(f"    - 템포: {tempo:.1f} BPM")
        
        except Exception as e:
            print(f"❌ 분석 실패: {e}")
    
    def create_random_melody(self, length: int = 16) -> List[Dict[str, Any]]:
        """랜덤 멜로디 생성"""
        pattern = []
        
        # C 메이저 스케일
        scale_notes = [60, 62, 64, 65, 67, 69, 71, 72]
        note_durations = [240, 480, 720]  # 8분음표, 4분음표, 점4분음표
        
        time_offset = 0
        for i in range(length):
            note = random.choice(scale_notes)
            duration = random.choice(note_durations)
            velocity = random.randint(60, 100)
            
            pattern.append({
                'type': 'note_on',
                'channel': 0,
                'note': note,
                'velocity': velocity,
                'time': time_offset
            })
            pattern.append({
                'type': 'note_off',
                'channel': 0,
                'note': note,
                'velocity': 0,
                'time': time_offset + duration - 50
            })
            
            time_offset += duration
        
        return pattern
    
    def export_pattern_as_midi(self, pattern: List[Dict[str, Any]], 
                              output_path: str, track_name: str = "Generated Pattern"):
        """패턴을 MIDI 파일로 내보내기"""
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)
        
        # 메타데이터
        track.append(mido.MetaMessage('track_name', name=track_name))
        track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(self.current_tempo)))
        
        # 패턴을 MIDI 메시지로 변환
        last_time = 0
        for event in sorted(pattern, key=lambda x: x['time']):
            delta_time = event['time'] - last_time
            
            track.append(mido.Message(
                event['type'],
                channel=event.get('channel', 0),
                note=event['note'],
                velocity=event['velocity'],
                time=delta_time
            ))
            
            last_time = event['time']
        
        # 파일 저장
        Path(output_path).parent.mkdir(exist_ok=True)
        mid.save(output_path)
        print(f"✅ 패턴 저장됨: {output_path}")

def test_midi_generation():
    """MIDI 생성 테스트"""
    print("🚀 MIDI 생성 테스트 시작\n")
    
    simulator = MIDISimulator()
    
    # 1. 기본 테스트 MIDI 생성
    test_midi_path = simulator.generate_test_midi()
    simulator.analyze_midi_file(test_midi_path)
    
    # 2. 완전한 트랙 생성
    complete_track_path = simulator.generate_complete_track()
    simulator.analyze_midi_file(complete_track_path)
    
    # 3. 개별 패턴 테스트
    print("\n🥁 드럼 패턴 생성...")
    drum_pattern = simulator.create_drum_pattern()
    simulator.export_pattern_as_midi(drum_pattern, "test_output/drum_pattern.mid", "Drum Pattern")
    
    print("\n🎸 베이스 라인 생성...")
    bass_pattern = simulator.create_bass_line()
    simulator.export_pattern_as_midi(bass_pattern, "test_output/bass_line.mid", "Bass Line")
    
    print("\n🎹 코드 진행 생성...")
    chord_pattern = simulator.create_chord_progression()
    simulator.export_pattern_as_midi(chord_pattern, "test_output/chord_progression.mid", "Chord Progression")
    
    print("\n🎵 멜로디 라인 생성...")
    melody_pattern = simulator.create_melody_line()
    simulator.export_pattern_as_midi(melody_pattern, "test_output/melody_line.mid", "Melody Line")
    
    # 4. 랜덤 멜로디 생성
    print("\n🎲 랜덤 멜로디 생성...")
    for i in range(3):
        random_pattern = simulator.create_random_melody(16)
        simulator.export_pattern_as_midi(
            random_pattern, 
            f"test_output/random_melody_{i+1}.mid", 
            f"Random Melody {i+1}"
        )
    
    print("\n✅ 모든 MIDI 파일 생성 완료!")
    
    # 생성된 파일 목록
    output_dir = Path("test_output")
    if output_dir.exists():
        midi_files = list(output_dir.glob("*.mid"))
        print(f"\n📁 생성된 MIDI 파일들 ({len(midi_files)}개):")
        for file in sorted(midi_files):
            size = file.stat().st_size
            print(f"  - {file.name} ({size} bytes)")

def test_midi_playback_simulation():
    """MIDI 재생 시뮬레이션 테스트"""
    print("\n🔄 MIDI 재생 시뮬레이션 테스트...")
    
    simulator = MIDISimulator()
    
    # 테스트용 패턴 생성
    test_pattern = [
        {'type': 'note_on', 'channel': 0, 'note': 60, 'velocity': 80, 'time': 0},
        {'type': 'note_off', 'channel': 0, 'note': 60, 'velocity': 0, 'time': 480},
        {'type': 'note_on', 'channel': 0, 'note': 64, 'velocity': 80, 'time': 480},
        {'type': 'note_off', 'channel': 0, 'note': 64, 'velocity': 0, 'time': 960},
        {'type': 'note_on', 'channel': 0, 'note': 67, 'velocity': 80, 'time': 960},
        {'type': 'note_off', 'channel': 0, 'note': 67, 'velocity': 0, 'time': 1440},
    ]
    
    print("  🎵 패턴 재생 시뮬레이션 (3초)...")
    
    start_time = time.time()
    for event in test_pattern:
        # 실제 재생에서는 MIDI 포트로 전송됨
        event_time = event['time'] / 480.0 * 0.5  # 시간 조정 (빠른 재생)
        
        while time.time() - start_time < event_time:
            time.sleep(0.01)
        
        print(f"    ♪ {event['type']}: 채널 {event['channel']}, 노트 {event['note']}, 벨로시티 {event['velocity']}")
    
    print("  ✅ 재생 시뮬레이션 완료")

def performance_benchmark():
    """성능 벤치마크"""
    print("\n⚡ 성능 벤치마크 테스트...")
    
    simulator = MIDISimulator()
    
    # MIDI 파일 생성 성능
    start_time = time.time()
    for i in range(10):
        simulator.generate_test_midi(f"test_output/benchmark_{i}.mid")
    generation_time = time.time() - start_time
    print(f"  📊 MIDI 파일 10개 생성: {generation_time:.3f}초")
    
    # 패턴 생성 성능
    start_time = time.time()
    for i in range(100):
        pattern = simulator.create_random_melody(16)
    pattern_time = time.time() - start_time
    print(f"  🎵 랜덤 패턴 100개 생성: {pattern_time:.3f}초")
    
    # 메모리 사용량 시뮬레이션
    patterns = []
    start_time = time.time()
    for i in range(50):
        patterns.append(simulator.create_drum_pattern())
        patterns.append(simulator.create_bass_line())
        patterns.append(simulator.create_melody_line())
    memory_test_time = time.time() - start_time
    total_events = sum(len(pattern) for pattern in patterns)
    print(f"  🧠 패턴 150개 메모리 테스트: {memory_test_time:.3f}초, {total_events}개 이벤트")
    
    print("  ✅ 성능 벤치마크 완료")

def main():
    """메인 함수"""
    print("🎹 MIDI 시뮬레이션 테스트 시작\n")
    
    # 1. MIDI 생성 테스트
    test_midi_generation()
    
    # 2. 재생 시뮬레이션 테스트
    test_midi_playback_simulation()
    
    # 3. 성능 벤치마크
    performance_benchmark()
    
    print("\n🎉 모든 MIDI 시뮬레이션 테스트 완료!")
    print("\n📋 테스트 결과:")
    print("  ✅ 기본 MIDI 파일 생성")
    print("  ✅ 멀티 트랙 생성")
    print("  ✅ 개별 악기 패턴 생성")
    print("  ✅ 랜덤 멜로디 생성")
    print("  ✅ 재생 시뮬레이션")
    print("  ✅ 성능 벤치마크")
    
    print("\n💡 생성된 MIDI 파일들을 DAW에서 열어서 확인해보세요!")

if __name__ == "__main__":
    main() 