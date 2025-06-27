#!/usr/bin/env python3
"""
장르 계층 시스템 테스트

3단계 장르 계층 시스템의 기능을 테스트합니다.
"""

import sys
import os
sys.path.append('src')

from music_theory.genre_system import (
    get_genre_hierarchy,
    validate_genre_path,
    get_genre_recommendations
)


def test_genre_hierarchy():
    """장르 계층 시스템 테스트"""
    print("🎵 장르 계층 시스템 테스트 시작\n")
    
    hierarchy = get_genre_hierarchy()
    
    # 1. 메인 장르 확인
    print("1. 메인 장르 목록:")
    main_genres = hierarchy.get_all_main_genres()
    for genre in main_genres:
        print(f"   - {genre}")
    print()
    
    # 2. 힙합 세부 장르 확인
    print("2. 힙합 세부 장르:")
    hip_hop_subgenres = hierarchy.get_all_subgenres_for_main("hip_hop")
    for subgenre in hip_hop_subgenres:
        print(f"   - {subgenre}")
    print()
    
    # 3. 트랩 스타일 변형 확인
    print("3. 트랩 스타일 변형:")
    trap_styles = hierarchy.get_all_styles_for_genre("hip_hop", "trap")
    for style in trap_styles:
        print(f"   - {style}")
    print()
    
    # 4. 장르 경로 유효성 검사
    print("4. 장르 경로 유효성 검사:")
    test_paths = [
        "hip_hop/trap/melodic_trap",
        "rock/j_rock/shibuya_kei",
        "electronic/house/deep_house",
        "invalid/path/test"
    ]
    
    for path in test_paths:
        is_valid = validate_genre_path(path)
        status = "✅ 유효" if is_valid else "❌ 무효"
        print(f"   {path}: {status}")
    print()
    
    # 5. 장르 특성 정보 확인
    print("5. 멜로딕 트랩 특성 정보:")
    characteristics = hierarchy.get_genre_characteristics("hip_hop", "trap", "melodic_trap")
    if characteristics:
        print(f"   템포 범위: {characteristics.tempo_range[0]}-{characteristics.tempo_range[1]} BPM")
        print(f"   주요 조성: {', '.join(characteristics.common_keys)}")
        print(f"   전형적 악기: {', '.join(characteristics.typical_instruments)}")
        print(f"   분위기: {', '.join(characteristics.mood_descriptors)}")
        print(f"   리듬 패턴: {', '.join(characteristics.rhythm_patterns)}")
    print()
    
    # 6. 특성 기반 장르 검색
    print("6. 특성 기반 장르 검색:")
    print("   어둡고 신비로운 분위기의 장르:")
    dark_genres = hierarchy.search_genres_by_characteristics(mood="dark")
    for main, sub, style in dark_genres:
        print(f"     - {main}/{sub}/{style}")
    print()
    
    print("   120-140 BPM 범위의 장르:")
    tempo_genres = hierarchy.search_genres_by_characteristics(tempo_range=(120, 140))
    for main, sub, style in tempo_genres[:5]:  # 상위 5개만
        print(f"     - {main}/{sub}/{style}")
    print()
    
    # 7. 장르 추천 시스템
    print("7. 장르 추천 시스템:")
    print("   트랩과 분위기가 비슷한 장르:")
    recommendations = get_genre_recommendations("hip_hop", "trap", "mood")
    for main, sub, style in recommendations:
        print(f"     - {main}/{sub}/{style}")
    print()
    
    print("✅ 모든 테스트 완료!")


if __name__ == "__main__":
    test_genre_hierarchy() 