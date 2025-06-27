"""
락 (Rock) 장르 계층 정의

락은 1950년대 미국에서 시작된 대중음악 장르로, 일렉트릭 기타, 베이스, 드럼을 
기본으로 하는 강한 비트와 에너지 넘치는 연주가 특징입니다. 
수십 년간 진화하며 다양한 서브 장르를 만들어냈습니다.

세부 장르:
- J-락 (J-Rock): 일본 록 음악, 시부야계와 비주얼계 등 독특한 스타일
- 메탈코어 (Metalcore): 헤비메탈과 하드코어 펑크의 융합
- 인디 락 (Indie Rock): 독립적이고 실험적인 록 음악
- 클래식 락 (Classic Rock): 1960-70년대 전통적인 록 스타일
- 프로그레시브 락 (Progressive Rock): 복잡하고 실험적인 구조
- 얼터너티브 락 (Alternative Rock): 1980-90년대 주류에 대한 대안
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_j_rock_hierarchy() -> GenreNode:
    """
    J-락 (J-Rock) - 일본 록 음악
    
    일본에서 발전한 독특한 록 음악 스타일로, 서구 록과 일본 전통 음악의 
    융합을 통해 독창적인 사운드를 만들어냈습니다. 비주얼계, 시부야계 등 
    일본만의 독특한 서브 장르들이 특징입니다.
    """
    j_rock = GenreNode(
        "j_rock",
        2,
        GenreCharacteristics(
            tempo_range=(80, 180),
            common_keys=["A minor", "E minor", "C major", "G major"],
            typical_instruments=["electric_guitar", "bass", "drums", "vocals"],
            mood_descriptors=["emotional", "energetic", "japanese", "melodic"],
            rhythm_patterns=["j_rock_rhythm", "anime_style", "emotional_builds"],
            cultural_context="일본"
        )
    )
    
    # 시부야계 - 세련된 팝 록 스타일
    j_rock.add_child(GenreNode(
        "shibuya_kei", 3,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["clean_guitar", "synthesizer", "soft_drums"],
            mood_descriptors=["sophisticated", "pop", "urban", "stylish"],
            rhythm_patterns=["pop_rock", "sophisticated_groove", "clean_sound"],
            cultural_context="일본 시부야"
        )
    ))
    
    # 비주얼계 - 화려한 비주얼과 극적인 음악
    j_rock.add_child(GenreNode(
        "visual_kei", 3,
        GenreCharacteristics(
            tempo_range=(120, 200),
            common_keys=["A minor", "D minor", "E minor"],
            typical_instruments=["distorted_guitar", "dramatic_vocals", "heavy_drums"],
            mood_descriptors=["dramatic", "theatrical", "dark", "intense"],
            rhythm_patterns=["dramatic_builds", "theatrical_breaks", "intense_sections"],
            cultural_context="일본 비주얼계"
        )
    ))
    
    # 얼터너티브 J-락 - 실험적인 일본 록
    j_rock.add_child(GenreNode(
        "alternative_j_rock", 3,
        GenreCharacteristics(
            tempo_range=(90, 160),
            common_keys=["E minor", "B minor", "F# minor"],
            typical_instruments=["experimental_guitar", "unconventional_drums"],
            mood_descriptors=["alternative", "experimental", "indie", "creative"],
            rhythm_patterns=["experimental_rhythms", "unconventional_structures"]
        )
    ))
    
    # 애니송 락 - 애니메이션 주제가 스타일
    j_rock.add_child(GenreNode(
        "anisong_rock", 3,
        GenreCharacteristics(
            tempo_range=(120, 180),
            common_keys=["C major", "A minor", "G major"],
            typical_instruments=["power_chords", "energetic_drums", "anime_vocals"],
            mood_descriptors=["energetic", "heroic", "uplifting", "anime"],
            rhythm_patterns=["anime_openings", "heroic_builds", "energetic_choruses"]
        )
    ))
    
    return j_rock


def create_metalcore_hierarchy() -> GenreNode:
    """
    메탈코어 (Metalcore) - 헤비메탈과 하드코어의 융합
    
    1990년대에 등장한 장르로, 헤비메탈의 기술적 연주와 하드코어 펑크의 
    공격성을 결합한 스타일입니다. 브레이크다운과 멜로딕한 부분의 대비가 특징입니다.
    """
    metalcore = GenreNode(
        "metalcore",
        2,
        GenreCharacteristics(
            tempo_range=(120, 200),
            common_keys=["C minor", "D minor", "A minor", "E minor"],
            typical_instruments=["distorted_guitar", "screaming_vocals", "double_bass_drums"],
            mood_descriptors=["aggressive", "intense", "emotional", "heavy"],
            rhythm_patterns=["breakdowns", "blast_beats", "palm_muting"]
        )
    )
    
    # 멜로딕 메탈코어 - 멜로디가 강조된 메탈코어
    metalcore.add_child(GenreNode(
        "melodic_metalcore", 3,
        GenreCharacteristics(
            tempo_range=(130, 180),
            common_keys=["A minor", "E minor", "C minor"],
            typical_instruments=["melodic_guitar", "clean_vocals", "emotional_screams"],
            mood_descriptors=["melodic", "emotional", "powerful", "uplifting"],
            rhythm_patterns=["melodic_leads", "emotional_choruses", "dynamic_changes"]
        )
    ))
    
    # 프로그레시브 메탈코어 - 복잡한 구조의 메탈코어
    metalcore.add_child(GenreNode(
        "progressive_metalcore", 3,
        GenreCharacteristics(
            tempo_range=(100, 220),
            common_keys=["D minor", "F# minor", "B minor"],
            typical_instruments=["technical_guitar", "complex_drums", "varied_vocals"],
            mood_descriptors=["complex", "technical", "progressive", "innovative"],
            rhythm_patterns=["odd_time_signatures", "technical_riffs", "complex_structures"]
        )
    ))
    
    # 브레이크다운 메탈코어 - 브레이크다운에 집중한 스타일
    metalcore.add_child(GenreNode(
        "breakdown_metalcore", 3,
        GenreCharacteristics(
            tempo_range=(80, 160),
            common_keys=["C minor", "Bb minor", "F minor"],
            typical_instruments=["heavy_guitar", "breakdown_riffs", "aggressive_drums"],
            mood_descriptors=["heavy", "aggressive", "crushing", "intense"],
            rhythm_patterns=["heavy_breakdowns", "mosh_pit_sections", "crushing_riffs"]
        )
    ))
    
    return metalcore


def create_indie_rock_hierarchy() -> GenreNode:
    """
    인디 락 (Indie Rock) - 독립적이고 실험적인 록 음악
    
    1980년대부터 시작된 독립 음악 운동의 일환으로, 주류 음악 산업과 
    거리를 두고 창의적이고 실험적인 사운드를 추구하는 록 음악입니다.
    """
    indie_rock = GenreNode(
        "indie_rock",
        2,
        GenreCharacteristics(
            tempo_range=(80, 160),
            common_keys=["C major", "A minor", "G major", "E minor"],
            typical_instruments=["jangly_guitar", "indie_vocals", "simple_drums"],
            mood_descriptors=["independent", "creative", "authentic", "alternative"],
            rhythm_patterns=["indie_rhythms", "jangly_guitar", "lo_fi_production"]
        )
    )
    
    # 드림팝 - 몽환적인 인디 록
    indie_rock.add_child(GenreNode(
        "dream_pop", 3,
        GenreCharacteristics(
            tempo_range=(80, 120),
            common_keys=["C major", "F major", "A minor"],
            typical_instruments=["reverb_guitar", "ethereal_vocals", "atmospheric_synths"],
            mood_descriptors=["dreamy", "ethereal", "atmospheric", "nostalgic"],
            rhythm_patterns=["floating_rhythms", "reverb_washed", "atmospheric_textures"]
        )
    ))
    
    # 포스트 락 - 후기 록, 실험적 구조
    indie_rock.add_child(GenreNode(
        "post_rock", 3,
        GenreCharacteristics(
            tempo_range=(60, 140),
            common_keys=["E minor", "A minor", "D major"],
            typical_instruments=["ambient_guitar", "cinematic_builds", "minimal_drums"],
            mood_descriptors=["cinematic", "emotional", "atmospheric", "building"],
            rhythm_patterns=["slow_builds", "cinematic_crescendos", "ambient_sections"]
        )
    ))
    
    # 매스 락 - 수학적 구조의 복잡한 록
    indie_rock.add_child(GenreNode(
        "math_rock", 3,
        GenreCharacteristics(
            tempo_range=(100, 180),
            common_keys=["E minor", "B minor", "F# minor"],
            typical_instruments=["technical_guitar", "complex_drums", "tapping_techniques"],
            mood_descriptors=["technical", "complex", "mathematical", "precise"],
            rhythm_patterns=["odd_time_signatures", "technical_tapping", "complex_polyrhythms"]
        )
    ))
    
    # 쇼게이즈 - 이펙트 중심의 몽환적 록
    indie_rock.add_child(GenreNode(
        "shoegaze", 3,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["A minor", "E minor", "C major"],
            typical_instruments=["effects_heavy_guitar", "buried_vocals", "wall_of_sound"],
            mood_descriptors=["dreamy", "noisy", "atmospheric", "textural"],
            rhythm_patterns=["wall_of_sound", "effects_heavy", "buried_rhythms"]
        )
    ))
    
    return indie_rock


def create_classic_rock_hierarchy() -> GenreNode:
    """
    클래식 락 (Classic Rock) - 1960-70년대 전통적인 록 스타일
    
    록 음악의 황금기로 불리는 1960-70년대의 전통적인 록 스타일로,
    현재까지도 많은 사랑을 받는 시대를 초월한 음악입니다.
    """
    classic_rock = GenreNode(
        "classic_rock",
        2,
        GenreCharacteristics(
            tempo_range=(90, 150),
            common_keys=["A major", "E major", "D major", "G major"],
            typical_instruments=["electric_guitar", "organ", "classic_drums", "bass"],
            mood_descriptors=["classic", "timeless", "energetic", "authentic"],
            rhythm_patterns=["classic_rock_beat", "guitar_solos", "organ_fills"],
            cultural_context="1960-70년대"
        )
    )
    
    # 하드 락 - 더 강하고 공격적인 클래식 락
    classic_rock.add_child(GenreNode(
        "hard_rock", 3,
        GenreCharacteristics(
            tempo_range=(120, 160),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["distorted_guitar", "powerful_vocals", "heavy_drums"],
            mood_descriptors=["powerful", "aggressive", "energetic", "driving"],
            rhythm_patterns=["driving_beats", "power_chords", "guitar_riffs"]
        )
    ))
    
    # 블루스 락 - 블루스 기반의 록
    classic_rock.add_child(GenreNode(
        "blues_rock", 3,
        GenreCharacteristics(
            tempo_range=(80, 130),
            common_keys=["E major", "A major", "B major"],
            typical_instruments=["blues_guitar", "harmonica", "soulful_vocals"],
            mood_descriptors=["bluesy", "soulful", "emotional", "raw"],
            rhythm_patterns=["blues_progression", "shuffle_rhythms", "guitar_bends"]
        )
    ))
    
    # 사이키델릭 락 - 환각적이고 실험적인 록
    classic_rock.add_child(GenreNode(
        "psychedelic_rock", 3,
        GenreCharacteristics(
            tempo_range=(70, 140),
            common_keys=["A minor", "E minor", "C major"],
            typical_instruments=["effects_guitar", "sitar", "experimental_sounds"],
            mood_descriptors=["psychedelic", "experimental", "trippy", "colorful"],
            rhythm_patterns=["experimental_rhythms", "effects_heavy", "trippy_sounds"]
        )
    ))
    
    return classic_rock


def create_progressive_rock_hierarchy() -> GenreNode:
    """
    프로그레시브 락 (Progressive Rock) - 복잡하고 실험적인 구조의 록
    
    1970년대에 등장한 장르로, 클래식 음악의 복잡성과 재즈의 즉흥성을 
    록 음악에 도입한 실험적이고 기술적인 스타일입니다.
    """
    progressive_rock = GenreNode(
        "progressive_rock",
        2,
        GenreCharacteristics(
            tempo_range=(60, 200),
            common_keys=["C minor", "A minor", "E minor", "F# minor"],
            typical_instruments=["complex_guitar", "keyboards", "technical_drums"],
            mood_descriptors=["complex", "sophisticated", "technical", "epic"],
            rhythm_patterns=["complex_time_signatures", "instrumental_sections", "epic_compositions"]
        )
    )
    
    # 심포닉 프로그 - 오케스트라 요소가 가미된 프로그
    progressive_rock.add_child(GenreNode(
        "symphonic_prog", 3,
        GenreCharacteristics(
            tempo_range=(80, 180),
            common_keys=["D minor", "A minor", "C minor"],
            typical_instruments=["orchestral_keyboards", "classical_instruments", "epic_vocals"],
            mood_descriptors=["symphonic", "epic", "orchestral", "grandiose"],
            rhythm_patterns=["orchestral_arrangements", "epic_builds", "classical_structures"]
        )
    ))
    
    # 테크니컬 프로그 - 기술적 연주에 집중한 프로그
    progressive_rock.add_child(GenreNode(
        "technical_prog", 3,
        GenreCharacteristics(
            tempo_range=(100, 220),
            common_keys=["E minor", "B minor", "F# minor"],
            typical_instruments=["technical_guitar", "complex_bass", "intricate_drums"],
            mood_descriptors=["technical", "virtuosic", "complex", "challenging"],
            rhythm_patterns=["technical_passages", "virtuosic_solos", "complex_polyrhythms"]
        )
    ))
    
    return progressive_rock


def create_alternative_rock_hierarchy() -> GenreNode:
    """
    얼터너티브 락 (Alternative Rock) - 1980-90년대 주류에 대한 대안
    
    1980년대부터 1990년대에 걸쳐 주류 록에 대한 대안으로 등장한 장르로,
    그런지, 브릿팝 등 다양한 서브 장르를 포함합니다.
    """
    alternative_rock = GenreNode(
        "alternative_rock",
        2,
        GenreCharacteristics(
            tempo_range=(90, 160),
            common_keys=["A minor", "E minor", "C major", "G major"],
            typical_instruments=["alternative_guitar", "raw_vocals", "dynamic_drums"],
            mood_descriptors=["alternative", "raw", "authentic", "rebellious"],
            rhythm_patterns=["alternative_rhythms", "dynamic_changes", "raw_energy"]
        )
    )
    
    # 그런지 - 1990년대 시애틀 사운드
    alternative_rock.add_child(GenreNode(
        "grunge", 3,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["distorted_guitar", "angsty_vocals", "heavy_bass"],
            mood_descriptors=["angsty", "raw", "rebellious", "seattle"],
            rhythm_patterns=["grunge_rhythms", "distorted_riffs", "angsty_dynamics"],
            cultural_context="1990년대 시애틀"
        )
    ))
    
    # 브릿팝 - 1990년대 영국 팝 록
    alternative_rock.add_child(GenreNode(
        "britpop", 3,
        GenreCharacteristics(
            tempo_range=(110, 150),
            common_keys=["C major", "G major", "A major"],
            typical_instruments=["jangly_guitar", "british_vocals", "melodic_bass"],
            mood_descriptors=["british", "melodic", "confident", "anthemic"],
            rhythm_patterns=["britpop_rhythms", "anthemic_choruses", "jangly_guitar"],
            cultural_context="1990년대 영국"
        )
    ))
    
    return alternative_rock


def create_rock_hierarchy() -> GenreNode:
    """락 메인 장르 계층 구조 생성"""
    
    # === 락 메인 장르 ===
    rock = GenreNode(
        "rock", 
        1,
        GenreCharacteristics(
            tempo_range=(60, 220),
            common_keys=["A minor", "E minor", "C major", "G major", "D major"],
            typical_instruments=["electric_guitar", "bass", "drums", "vocals"],
            mood_descriptors=["energetic", "powerful", "rebellious", "expressive"],
            rhythm_patterns=["rock_beat", "guitar_riffs", "power_chords"],
            cultural_context="1950년대 미국"
        )
    )
    
    # 세부 장르들 추가
    rock.add_child(create_j_rock_hierarchy())
    rock.add_child(create_metalcore_hierarchy())
    rock.add_child(create_indie_rock_hierarchy())
    rock.add_child(create_classic_rock_hierarchy())
    rock.add_child(create_progressive_rock_hierarchy())
    rock.add_child(create_alternative_rock_hierarchy())
    
    return rock 