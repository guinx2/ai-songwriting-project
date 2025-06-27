"""
팝 (Pop) 장르 계층 정의

팝 음악은 대중음악(Popular Music)의 줄임말로, 상업적 성공과 대중적 어필을 
목적으로 하는 음악 장르입니다. 접근하기 쉬운 멜로디와 구조가 특징이며, 
시대와 지역에 따라 다양한 스타일로 발전했습니다.

세부 장르:
- K-팝 (K-Pop): 한국 대중음악, 글로벌 인기
- J-팝 (J-Pop): 일본 대중음악, 독특한 일본 스타일
- 인디 팝 (Indie Pop): 독립적이고 실험적인 팝 음악
- 일렉트로 팝 (Electro Pop): 전자음악 요소가 가미된 팝
- 댄스 팝 (Dance Pop): 댄스 요소가 강한 팝 음악
- 팝 록 (Pop Rock): 록 요소가 가미된 팝 음악
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_k_pop_hierarchy() -> GenreNode:
    """
    K-팝 (K-Pop) - 한국 대중음악
    
    1990년대부터 본격적으로 발전한 한국의 대중음악으로, 2000년대 후반부터 
    전 세계적인 인기를 얻고 있습니다. 아이돌 그룹 중심의 체계적인 시스템과 
    높은 완성도의 퍼포먼스가 특징입니다.
    """
    k_pop = GenreNode(
        "k_pop",
        2,
        GenreCharacteristics(
            tempo_range=(80, 140),
            common_keys=["C major", "G major", "A minor", "F major"],
            typical_instruments=["synth_pop", "electronic_beats", "korean_vocals", "idol_harmonies"],
            mood_descriptors=["energetic", "catchy", "polished", "korean"],
            rhythm_patterns=["k_pop_beats", "idol_choreography", "korean_groove"],
            cultural_context="1990년대부터 한국"
        )
    )
    
    # 아이돌 팝 - 아이돌 그룹 중심의 K-팝
    k_pop.add_child(GenreNode(
        "idol_pop", 3,
        GenreCharacteristics(
            tempo_range=(100, 130),
            common_keys=["C major", "G major", "F major"],
            typical_instruments=["idol_vocals", "choreography_beats", "group_harmonies"],
            mood_descriptors=["bright", "energetic", "synchronized", "commercial"],
            rhythm_patterns=["idol_choreography", "synchronized_vocals", "commercial_hooks"]
        )
    ))
    
    # 인디 K-팝 - 독립적인 한국 팝 음악
    k_pop.add_child(GenreNode(
        "indie_k_pop", 3,
        GenreCharacteristics(
            tempo_range=(80, 120),
            common_keys=["A minor", "E minor", "C major"],
            typical_instruments=["indie_instruments", "korean_indie_vocals", "alternative_arrangements"],
            mood_descriptors=["indie", "alternative", "authentic", "artistic"],
            rhythm_patterns=["indie_grooves", "alternative_korean", "artistic_arrangements"]
        )
    ))
    
    # K-발라드 - 한국식 발라드
    k_pop.add_child(GenreNode(
        "k_ballad", 3,
        GenreCharacteristics(
            tempo_range=(60, 90),
            common_keys=["C major", "F major", "A minor"],
            typical_instruments=["piano_ballad", "emotional_vocals", "orchestral_strings"],
            mood_descriptors=["emotional", "romantic", "dramatic", "heartfelt"],
            rhythm_patterns=["ballad_rhythm", "emotional_builds", "dramatic_crescendos"],
            cultural_context="한국 발라드 전통"
        )
    ))
    
    # K-R&B - 한국식 R&B
    k_pop.add_child(GenreNode(
        "k_rnb", 3,
        GenreCharacteristics(
            tempo_range=(70, 110),
            common_keys=["A minor", "E minor", "D minor"],
            typical_instruments=["rnb_vocals", "smooth_beats", "korean_soul"],
            mood_descriptors=["smooth", "soulful", "sophisticated", "korean_rnb"],
            rhythm_patterns=["rnb_grooves", "smooth_korean", "soulful_rhythms"]
        )
    ))
    
    return k_pop


def create_j_pop_hierarchy() -> GenreNode:
    """
    J-팝 (J-Pop) - 일본 대중음악
    
    1990년대에 정립된 일본의 대중음악으로, 독특한 일본적 감성과 
    다양한 서구 음악 스타일의 융합이 특징입니다. 애니메이션과 
    게임 문화와도 밀접한 관련이 있습니다.
    """
    j_pop = GenreNode(
        "j_pop",
        2,
        GenreCharacteristics(
            tempo_range=(80, 150),
            common_keys=["C major", "G major", "A minor", "F major"],
            typical_instruments=["j_pop_synths", "japanese_vocals", "pop_arrangements"],
            mood_descriptors=["japanese", "melodic", "colorful", "unique"],
            rhythm_patterns=["j_pop_beats", "japanese_groove", "colorful_arrangements"],
            cultural_context="1990년대 일본"
        )
    )
    
    # 시부야계 팝 - 세련된 일본 팝
    j_pop.add_child(GenreNode(
        "shibuya_kei_pop", 3,
        GenreCharacteristics(
            tempo_range=(100, 130),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["sophisticated_pop", "jazz_influences", "urban_sounds"],
            mood_descriptors=["sophisticated", "urban", "stylish", "refined"],
            rhythm_patterns=["shibuya_groove", "sophisticated_pop", "urban_style"],
            cultural_context="1990년대 시부야"
        )
    ))
    
    # 시티 팝 - 도시적인 일본 팝
    j_pop.add_child(GenreNode(
        "city_pop", 3,
        GenreCharacteristics(
            tempo_range=(90, 120),
            common_keys=["F major", "Bb major", "C major"],
            typical_instruments=["city_pop_synths", "smooth_vocals", "urban_bass"],
            mood_descriptors=["nostalgic", "urban", "smooth", "retro"],
            rhythm_patterns=["city_pop_groove", "urban_rhythms", "nostalgic_feel"],
            cultural_context="1980년대 일본"
        )
    ))
    
    # J-발라드 - 일본식 발라드
    j_pop.add_child(GenreNode(
        "j_ballad", 3,
        GenreCharacteristics(
            tempo_range=(60, 90),
            common_keys=["C major", "F major", "A minor"],
            typical_instruments=["piano_ballad", "japanese_vocals", "emotional_strings"],
            mood_descriptors=["emotional", "romantic", "japanese_sentiment", "touching"],
            rhythm_patterns=["ballad_rhythm", "japanese_emotion", "touching_builds"]
        )
    ))
    
    # 애니송 팝 - 애니메이션 주제가 스타일
    j_pop.add_child(GenreNode(
        "anisong_pop", 3,
        GenreCharacteristics(
            tempo_range=(120, 160),
            common_keys=["C major", "G major", "A minor"],
            typical_instruments=["anime_synths", "energetic_vocals", "colorful_arrangements"],
            mood_descriptors=["energetic", "colorful", "anime", "uplifting"],
            rhythm_patterns=["anime_beats", "energetic_builds", "colorful_rhythms"]
        )
    ))
    
    return j_pop


def create_indie_pop_hierarchy() -> GenreNode:
    """
    인디 팝 (Indie Pop) - 독립적이고 실험적인 팝 음악
    
    1980년대부터 시작된 독립 음악 운동의 일환으로, 주류 팝과 거리를 두고 
    더 창의적이고 실험적인 접근을 하는 팝 음악입니다.
    """
    indie_pop = GenreNode(
        "indie_pop",
        2,
        GenreCharacteristics(
            tempo_range=(80, 140),
            common_keys=["C major", "A minor", "G major", "F major"],
            typical_instruments=["indie_guitars", "lo_fi_production", "unique_vocals"],
            mood_descriptors=["indie", "authentic", "creative", "alternative"],
            rhythm_patterns=["indie_grooves", "lo_fi_beats", "creative_arrangements"]
        )
    )
    
    # 로파이 팝 - 저음질 미학의 팝
    indie_pop.add_child(GenreNode(
        "lo_fi_pop", 3,
        GenreCharacteristics(
            tempo_range=(70, 110),
            common_keys=["A minor", "F major", "C major"],
            typical_instruments=["lo_fi_instruments", "vintage_sounds", "tape_saturation"],
            mood_descriptors=["nostalgic", "dreamy", "vintage", "intimate"],
            rhythm_patterns=["lo_fi_grooves", "vintage_rhythms", "intimate_feels"]
        )
    ))
    
    # 챔버 팝 - 클래식 악기가 가미된 팝
    indie_pop.add_child(GenreNode(
        "chamber_pop", 3,
        GenreCharacteristics(
            tempo_range=(80, 120),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["orchestral_instruments", "chamber_arrangements", "refined_production"],
            mood_descriptors=["sophisticated", "orchestral", "refined", "elegant"],
            rhythm_patterns=["chamber_rhythms", "orchestral_arrangements", "refined_grooves"]
        )
    ))
    
    # 트윈클 팝 - 반짝이는 사운드의 팝
    indie_pop.add_child(GenreNode(
        "twee_pop", 3,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["C major", "G major", "F major"],
            typical_instruments=["jangly_guitars", "sweet_vocals", "innocent_sounds"],
            mood_descriptors=["sweet", "innocent", "charming", "whimsical"],
            rhythm_patterns=["jangly_rhythms", "sweet_grooves", "innocent_beats"]
        )
    ))
    
    return indie_pop


def create_electro_pop_hierarchy() -> GenreNode:
    """
    일렉트로 팝 (Electro Pop) - 전자음악 요소가 가미된 팝
    
    1980년대부터 발전한 장르로, 팝 음악에 신시사이저와 전자음악 요소를 
    결합한 스타일입니다. 현대 팝 음악의 주류 중 하나입니다.
    """
    electro_pop = GenreNode(
        "electro_pop",
        2,
        GenreCharacteristics(
            tempo_range=(100, 130),
            common_keys=["C major", "A minor", "F major", "G major"],
            typical_instruments=["synthesizers", "electronic_drums", "vocoder", "digital_effects"],
            mood_descriptors=["electronic", "modern", "synthetic", "danceable"],
            rhythm_patterns=["electronic_beats", "synth_pop_grooves", "digital_rhythms"]
        )
    )
    
    # 신스팝 - 신시사이저 중심의 팝
    electro_pop.add_child(GenreNode(
        "synth_pop", 3,
        GenreCharacteristics(
            tempo_range=(100, 120),
            common_keys=["C major", "A minor", "F major"],
            typical_instruments=["vintage_synths", "drum_machines", "synth_bass"],
            mood_descriptors=["retro", "synthetic", "nostalgic", "electronic"],
            rhythm_patterns=["synth_pop_beats", "retro_grooves", "synthetic_rhythms"],
            cultural_context="1980년대"
        )
    ))
    
    # 퓨처 팝 - 미래적인 전자 팝
    electro_pop.add_child(GenreNode(
        "future_pop", 3,
        GenreCharacteristics(
            tempo_range=(110, 130),
            common_keys=["A minor", "C major", "G minor"],
            typical_instruments=["futuristic_synths", "modern_production", "digital_vocals"],
            mood_descriptors=["futuristic", "modern", "polished", "digital"],
            rhythm_patterns=["future_beats", "modern_grooves", "digital_rhythms"]
        )
    ))
    
    # 일렉트로클래시 - 레트로 전자음악과 팝의 융합
    electro_pop.add_child(GenreNode(
        "electroclash", 3,
        GenreCharacteristics(
            tempo_range=(120, 140),
            common_keys=["C minor", "A minor", "F minor"],
            typical_instruments=["retro_electronics", "punk_attitude", "club_beats"],
            mood_descriptors=["retro", "edgy", "club", "rebellious"],
            rhythm_patterns=["electroclash_beats", "retro_club_grooves", "edgy_rhythms"]
        )
    ))
    
    return electro_pop


def create_dance_pop_hierarchy() -> GenreNode:
    """
    댄스 팝 (Dance Pop) - 댄스 요소가 강한 팝 음악
    
    1980년대부터 발전한 장르로, 팝 음악에 댄스 음악의 리듬과 에너지를 
    결합한 스타일입니다. 클럽과 라디오 모두에서 인기를 얻는 것이 목표입니다.
    """
    dance_pop = GenreNode(
        "dance_pop",
        2,
        GenreCharacteristics(
            tempo_range=(120, 130),
            common_keys=["C major", "G major", "A minor", "F major"],
            typical_instruments=["dance_beats", "pop_vocals", "club_synths", "bass_lines"],
            mood_descriptors=["energetic", "danceable", "uplifting", "commercial"],
            rhythm_patterns=["four_on_floor", "dance_grooves", "pop_hooks"]
        )
    )
    
    # 유로댄스 팝 - 유럽식 댄스 팝
    dance_pop.add_child(GenreNode(
        "eurodance_pop", 3,
        GenreCharacteristics(
            tempo_range=(125, 135),
            common_keys=["C major", "G major", "F major"],
            typical_instruments=["eurodance_synths", "rap_vocals", "dance_vocals"],
            mood_descriptors=["energetic", "european", "club", "euphoric"],
            rhythm_patterns=["eurodance_beats", "club_grooves", "euphoric_builds"],
            cultural_context="1990년대 유럽"
        )
    ))
    
    # 틴 팝 - 10대 대상의 댄스 팝
    dance_pop.add_child(GenreNode(
        "teen_pop", 3,
        GenreCharacteristics(
            tempo_range=(110, 130),
            common_keys=["C major", "G major", "F major"],
            typical_instruments=["teen_friendly_production", "catchy_hooks", "youthful_vocals"],
            mood_descriptors=["youthful", "catchy", "innocent", "commercial"],
            rhythm_patterns=["teen_pop_beats", "catchy_rhythms", "youthful_energy"]
        )
    ))
    
    # EDM 팝 - EDM 요소가 가미된 팝
    dance_pop.add_child(GenreNode(
        "edm_pop", 3,
        GenreCharacteristics(
            tempo_range=(125, 135),
            common_keys=["A minor", "C major", "G major"],
            typical_instruments=["edm_drops", "festival_synths", "big_room_elements"],
            mood_descriptors=["festival", "energetic", "massive", "euphoric"],
            rhythm_patterns=["edm_drops", "festival_builds", "big_room_beats"]
        )
    ))
    
    return dance_pop


def create_pop_rock_hierarchy() -> GenreNode:
    """
    팝 록 (Pop Rock) - 록 요소가 가미된 팝 음악
    
    1960년대부터 발전한 장르로, 팝 음악의 접근성과 록 음악의 에너지를 
    결합한 스타일입니다. 라디오 친화적이면서도 록의 역동성을 가집니다.
    """
    pop_rock = GenreNode(
        "pop_rock",
        2,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["C major", "G major", "A minor", "F major"],
            typical_instruments=["electric_guitars", "pop_vocals", "rock_drums", "bass_guitar"],
            mood_descriptors=["energetic", "accessible", "radio_friendly", "uplifting"],
            rhythm_patterns=["rock_beats", "pop_structures", "guitar_driven"]
        )
    )
    
    # 파워 팝 - 강한 에너지의 팝 록
    pop_rock.add_child(GenreNode(
        "power_pop", 3,
        GenreCharacteristics(
            tempo_range=(120, 150),
            common_keys=["C major", "G major", "A major"],
            typical_instruments=["power_chords", "harmonized_vocals", "driving_drums"],
            mood_descriptors=["powerful", "energetic", "catchy", "driving"],
            rhythm_patterns=["power_pop_beats", "driving_rhythms", "energetic_grooves"]
        )
    ))
    
    # 소프트 록 - 부드러운 팝 록
    pop_rock.add_child(GenreNode(
        "soft_rock", 3,
        GenreCharacteristics(
            tempo_range=(80, 120),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["acoustic_guitars", "soft_vocals", "gentle_drums"],
            mood_descriptors=["soft", "mellow", "easy_listening", "relaxed"],
            rhythm_patterns=["soft_rhythms", "mellow_grooves", "gentle_beats"]
        )
    ))
    
    # 아레나 록 - 대형 공연장용 팝 록
    pop_rock.add_child(GenreNode(
        "arena_rock", 3,
        GenreCharacteristics(
            tempo_range=(110, 140),
            common_keys=["A minor", "C major", "G major"],
            typical_instruments=["anthemic_guitars", "stadium_vocals", "big_drums"],
            mood_descriptors=["anthemic", "stadium", "massive", "crowd_pleasing"],
            rhythm_patterns=["arena_beats", "anthemic_rhythms", "stadium_grooves"]
        )
    ))
    
    return pop_rock


def create_pop_hierarchy() -> GenreNode:
    """팝 메인 장르 계층 구조 생성"""
    
    # === 팝 메인 장르 ===
    pop = GenreNode(
        "pop", 
        1,
        GenreCharacteristics(
            tempo_range=(60, 160),
            common_keys=["C major", "G major", "A minor", "F major", "D major"],
            typical_instruments=["vocals", "guitars", "keyboards", "drums", "bass"],
            mood_descriptors=["catchy", "accessible", "commercial", "melodic"],
            rhythm_patterns=["pop_beats", "catchy_hooks", "verse_chorus_structure"],
            cultural_context="20세기 중반부터 현재"
        )
    )
    
    # 세부 장르들 추가
    pop.add_child(create_k_pop_hierarchy())
    pop.add_child(create_j_pop_hierarchy())
    pop.add_child(create_indie_pop_hierarchy())
    pop.add_child(create_electro_pop_hierarchy())
    pop.add_child(create_dance_pop_hierarchy())
    pop.add_child(create_pop_rock_hierarchy())
    
    return pop 
    return pop 