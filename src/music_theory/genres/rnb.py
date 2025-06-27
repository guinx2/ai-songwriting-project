"""
R&B (Rhythm & Blues) 장르 계층 정의

R&B는 1940년대 미국에서 아프리카계 미국인 음악 전통에서 발전한 장르로,
리듬과 블루스의 융합이 특징입니다. 소울, 펑크, 힙합 등 많은 장르의 
기원이 되었으며, 현재까지도 계속 진화하고 있습니다.

세부 장르:
- 클래식 R&B (Classic R&B): 1940-60년대 전통적인 R&B
- 소울 (Soul): 1960년대 감정적이고 영적인 R&B
- 펑크 (Funk): 1960년대 리듬 중심의 그루브 음악
- 컨템포러리 R&B (Contemporary R&B): 1980년대 이후 현대적 R&B
- 네오 소울 (Neo Soul): 1990년대 소울의 현대적 재해석
- 얼터너티브 R&B (Alternative R&B): 실험적이고 독창적인 R&B
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_classic_rnb_hierarchy() -> GenreNode:
    """
    클래식 R&B (Classic R&B) - 1940-60년대 전통적인 R&B
    
    리듬 앤 블루스의 원형으로, 블루스, 재즈, 가스펠의 영향을 받아 
    형성된 전통적인 스타일입니다. 강한 리듬과 감정적인 보컬이 특징입니다.
    """
    classic_rnb = GenreNode(
        "classic_rnb",
        2,
        GenreCharacteristics(
            tempo_range=(80, 140),
            common_keys=["Bb major", "F major", "C major", "G major"],
            typical_instruments=["electric_guitar", "upright_bass", "drums", "piano", "horn_section"],
            mood_descriptors=["soulful", "rhythmic", "emotional", "classic"],
            rhythm_patterns=["shuffle_rhythm", "blues_progression", "classic_rnb_groove"],
            cultural_context="1940-60년대 미국"
        )
    )
    
    # 점프 블루스 - 업템포의 리듬 블루스
    classic_rnb.add_child(GenreNode(
        "jump_blues", 3,
        GenreCharacteristics(
            tempo_range=(120, 160),
            common_keys=["Bb major", "F major", "C major"],
            typical_instruments=["saxophone", "trumpet", "piano", "upright_bass"],
            mood_descriptors=["energetic", "swinging", "danceable", "upbeat"],
            rhythm_patterns=["jump_rhythm", "swing_feel", "horn_riffs"]
        )
    ))
    
    # 두왑 - 보컬 그룹 중심의 R&B
    classic_rnb.add_child(GenreNode(
        "doo_wop", 3,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["vocal_harmonies", "minimal_instruments", "bass_vocals"],
            mood_descriptors=["harmonious", "nostalgic", "vocal", "sweet"],
            rhythm_patterns=["doo_wop_rhythm", "vocal_harmonies", "simple_backing"]
        )
    ))
    
    return classic_rnb


def create_soul_hierarchy() -> GenreNode:
    """
    소울 (Soul) - 1960년대 감정적이고 영적인 R&B
    
    가스펠과 R&B의 융합으로 탄생한 장르로, 강한 감정 표현과 
    영적인 메시지가 특징입니다. 아레사 프랭클린, 스티비 원더 등이 대표적입니다.
    """
    soul = GenreNode(
        "soul",
        2,
        GenreCharacteristics(
            tempo_range=(70, 150),
            common_keys=["C major", "F major", "Bb major", "A minor"],
            typical_instruments=["organ", "horn_section", "rhythm_guitar", "powerful_vocals"],
            mood_descriptors=["soulful", "emotional", "spiritual", "powerful"],
            rhythm_patterns=["soul_groove", "gospel_influenced", "emotional_builds"],
            cultural_context="1960년대 미국"
        )
    )
    
    # 모타운 - 디트로이트 소울 사운드
    soul.add_child(GenreNode(
        "motown", 3,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["C major", "F major", "Bb major"],
            typical_instruments=["motown_bass", "tambourine", "string_section", "call_response_vocals"],
            mood_descriptors=["polished", "commercial", "danceable", "detroit"],
            rhythm_patterns=["motown_beat", "four_on_floor", "tambourine_accent"],
            cultural_context="1960년대 디트로이트"
        )
    ))
    
    # 멤피스 소울 - 남부 소울 스타일
    soul.add_child(GenreNode(
        "memphis_soul", 3,
        GenreCharacteristics(
            tempo_range=(80, 130),
            common_keys=["F major", "Bb major", "C major"],
            typical_instruments=["stax_horns", "southern_rhythm", "gritty_vocals"],
            mood_descriptors=["gritty", "southern", "raw", "authentic"],
            rhythm_patterns=["memphis_groove", "southern_feel", "horn_stabs"],
            cultural_context="1960년대 멤피스"
        )
    ))
    
    # 필라델피아 소울 - 세련된 오케스트라 소울
    soul.add_child(GenreNode(
        "philadelphia_soul", 3,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["lush_strings", "sophisticated_arrangements", "smooth_vocals"],
            mood_descriptors=["sophisticated", "lush", "orchestral", "smooth"],
            rhythm_patterns=["philly_groove", "orchestral_arrangements", "smooth_flow"]
        )
    ))
    
    return soul


def create_contemporary_rnb_hierarchy() -> GenreNode:
    """
    컨템포러리 R&B (Contemporary R&B) - 1980년대 이후 현대적 R&B
    
    전통적인 R&B에 팝, 힙합, 일렉트로닉 요소를 결합한 현대적 스타일입니다.
    프로듀서 중심의 정교한 제작과 매끄러운 보컬이 특징입니다.
    """
    contemporary_rnb = GenreNode(
        "contemporary_rnb",
        2,
        GenreCharacteristics(
            tempo_range=(70, 120),
            common_keys=["A minor", "C major", "F major", "D minor"],
            typical_instruments=["synthesizers", "drum_machines", "smooth_vocals", "electric_piano"],
            mood_descriptors=["smooth", "polished", "contemporary", "sophisticated"],
            rhythm_patterns=["contemporary_groove", "syncopated_rhythms", "smooth_flow"],
            cultural_context="1980년대 이후"
        )
    )
    
    # 뉴 잭 스윙 - 힙합과 R&B의 융합
    contemporary_rnb.add_child(GenreNode(
        "new_jack_swing", 3,
        GenreCharacteristics(
            tempo_range=(90, 120),
            common_keys=["A minor", "C major", "F major"],
            typical_instruments=["hip_hop_beats", "swing_rhythms", "synthesizers"],
            mood_descriptors=["urban", "swinging", "hip_hop_influenced", "danceable"],
            rhythm_patterns=["new_jack_groove", "hip_hop_swing", "urban_rhythm"],
            cultural_context="1980년대 말"
        )
    ))
    
    # 콰이어트 스톰 - 부드럽고 로맨틱한 R&B
    contemporary_rnb.add_child(GenreNode(
        "quiet_storm", 3,
        GenreCharacteristics(
            tempo_range=(60, 90),
            common_keys=["A minor", "D minor", "F major"],
            typical_instruments=["soft_synths", "mellow_vocals", "gentle_rhythms"],
            mood_descriptors=["romantic", "mellow", "intimate", "smooth"],
            rhythm_patterns=["quiet_storm_groove", "gentle_rhythm", "romantic_flow"]
        )
    ))
    
    return contemporary_rnb


def create_neo_soul_hierarchy() -> GenreNode:
    """
    네오 소울 (Neo Soul) - 1990년대 소울의 현대적 재해석
    
    전통적인 소울과 현대적 프로덕션을 결합한 장르로, 더 실험적이고 
    아티스틱한 접근을 특징으로 합니다. 디앤젤로, 에리카 바두 등이 대표적입니다.
    """
    neo_soul = GenreNode(
        "neo_soul",
        2,
        GenreCharacteristics(
            tempo_range=(70, 110),
            common_keys=["A minor", "E minor", "D minor", "F major"],
            typical_instruments=["live_instruments", "organic_production", "soulful_vocals"],
            mood_descriptors=["organic", "soulful", "artistic", "authentic"],
            rhythm_patterns=["neo_soul_groove", "organic_rhythm", "live_feel"],
            cultural_context="1990년대"
        )
    )
    
    # 얼터너티브 소울 - 실험적인 소울
    neo_soul.add_child(GenreNode(
        "alternative_soul", 3,
        GenreCharacteristics(
            tempo_range=(60, 120),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["experimental_arrangements", "unconventional_structures"],
            mood_descriptors=["experimental", "alternative", "creative", "boundary_pushing"],
            rhythm_patterns=["experimental_grooves", "unconventional_rhythms", "creative_structures"]
        )
    ))
    
    return neo_soul


def create_alternative_rnb_hierarchy() -> GenreNode:
    """
    얼터너티브 R&B (Alternative R&B) - 실험적이고 독창적인 R&B
    
    2010년대 이후 등장한 장르로, 전통적인 R&B 구조에서 벗어나 
    일렉트로닉, 인디, 힙합 등 다양한 장르와 융합한 실험적 스타일입니다.
    """
    alternative_rnb = GenreNode(
        "alternative_rnb",
        2,
        GenreCharacteristics(
            tempo_range=(60, 130),
            common_keys=["A minor", "E minor", "C major", "F# minor"],
            typical_instruments=["electronic_elements", "atmospheric_production", "unique_vocals"],
            mood_descriptors=["atmospheric", "experimental", "moody", "innovative"],
            rhythm_patterns=["alternative_grooves", "experimental_rhythms", "atmospheric_textures"],
            cultural_context="2010년대 이후"
        )
    )
    
    # PBR&B - 인디와 R&B의 융합
    alternative_rnb.add_child(GenreNode(
        "pbr_rnb", 3,
        GenreCharacteristics(
            tempo_range=(70, 110),
            common_keys=["A minor", "E minor", "C major"],
            typical_instruments=["lo_fi_production", "indie_aesthetics", "atmospheric_vocals"],
            mood_descriptors=["indie", "atmospheric", "lo_fi", "hipster"],
            rhythm_patterns=["indie_rnb_groove", "lo_fi_rhythms", "atmospheric_beats"]
        )
    ))
    
    # 트랩 소울 - 트랩과 소울의 융합
    alternative_rnb.add_child(GenreNode(
        "trap_soul", 3,
        GenreCharacteristics(
            tempo_range=(60, 90),
            common_keys=["A minor", "C minor", "F minor"],
            typical_instruments=["trap_beats", "soulful_vocals", "modern_production"],
            mood_descriptors=["modern", "urban", "soulful", "trap_influenced"],
            rhythm_patterns=["trap_soul_groove", "modern_trap_beats", "soulful_melodies"]
        )
    ))
    
    return alternative_rnb


def create_rnb_hierarchy() -> GenreNode:
    """R&B 메인 장르 계층 구조 생성"""
    
    # === R&B 메인 장르 ===
    rnb = GenreNode(
        "rnb", 
        1,
        GenreCharacteristics(
            tempo_range=(60, 160),
            common_keys=["C major", "F major", "Bb major", "A minor", "E minor"],
            typical_instruments=["vocals", "electric_guitar", "bass", "drums", "keyboards"],
            mood_descriptors=["soulful", "rhythmic", "emotional", "groovy"],
            rhythm_patterns=["rnb_groove", "syncopated_rhythms", "soul_feel", "blues_influence"],
            cultural_context="1940년대 미국"
        )
    )
    
    # 세부 장르들 추가
    rnb.add_child(create_classic_rnb_hierarchy())
    rnb.add_child(create_soul_hierarchy())
    rnb.add_child(create_contemporary_rnb_hierarchy())
    rnb.add_child(create_neo_soul_hierarchy())
    rnb.add_child(create_alternative_rnb_hierarchy())
    
    return rnb 