"""
일렉트로닉 (Electronic) 장르 계층 정의

일렉트로닉 음악은 전자 악기와 기술을 사용하여 만든 음악으로, 1940년대부터 시작되어
현재까지 끊임없이 진화하고 있는 장르입니다. 댄스 음악부터 앰비언트까지 
매우 다양한 스타일을 포괄합니다.

세부 장르:
- 하우스 (House): 4/4 비트 기반의 댄스 음악, 시카고에서 시작
- 테크노 (Techno): 미니멀하고 반복적인 전자음악, 디트로이트 기원
- 트랜스 (Trance): 몽환적이고 상승감 있는 댄스 음악
- 더브스텝 (Dubstep): 강한 베이스와 신코페이션이 특징
- 앰비언트 (Ambient): 분위기와 공간감을 중시하는 전자음악
- 드럼 앤 베이스 (Drum & Bass): 빠른 브레이크비트와 헤비 베이스
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_house_hierarchy() -> GenreNode:
    """
    하우스 (House) - 4/4 비트 기반의 댄스 음악
    
    1980년대 시카고에서 시작된 일렉트로닉 댄스 음악으로, 4/4 박자의 강한 킥 드럼과
    반복적인 베이스라인이 특징입니다. 클럽 문화와 함께 발전했습니다.
    """
    house = GenreNode(
        "house",
        2,
        GenreCharacteristics(
            tempo_range=(120, 130),
            common_keys=["C major", "A minor", "F major", "G major"],
            typical_instruments=["kick_drum", "hi_hats", "bass_synth", "piano"],
            mood_descriptors=["danceable", "uplifting", "rhythmic", "groovy"],
            rhythm_patterns=["four_on_floor", "house_groove", "syncopated_hi_hats"],
            cultural_context="1980년대 시카고"
        )
    )
    
    # 딥 하우스 - 더 깊고 소울풀한 하우스
    house.add_child(GenreNode(
        "deep_house", 3,
        GenreCharacteristics(
            tempo_range=(120, 125),
            common_keys=["A minor", "D minor", "F major"],
            typical_instruments=["deep_bass", "soulful_vocals", "warm_pads"],
            mood_descriptors=["deep", "soulful", "warm", "sophisticated"],
            rhythm_patterns=["deep_groove", "minimal_percussion", "soulful_elements"]
        )
    ))
    
    # 테크 하우스 - 테크노 요소가 가미된 하우스
    house.add_child(GenreNode(
        "tech_house", 3,
        GenreCharacteristics(
            tempo_range=(125, 130),
            common_keys=["C minor", "F minor", "G minor"],
            typical_instruments=["techno_elements", "driving_bass", "minimal_synths"],
            mood_descriptors=["driving", "minimal", "hypnotic", "underground"],
            rhythm_patterns=["driving_groove", "minimal_techno_elements", "hypnotic_loops"]
        )
    ))
    
    # 프로그레시브 하우스 - 긴 빌드업과 발전이 특징
    house.add_child(GenreNode(
        "progressive_house", 3,
        GenreCharacteristics(
            tempo_range=(125, 132),
            common_keys=["A minor", "E minor", "C major"],
            typical_instruments=["evolving_synths", "atmospheric_pads", "building_elements"],
            mood_descriptors=["progressive", "building", "atmospheric", "epic"],
            rhythm_patterns=["progressive_builds", "evolving_patterns", "epic_breakdowns"]
        )
    ))
    
    # 퓨처 하우스 - 현대적이고 미래적인 하우스
    house.add_child(GenreNode(
        "future_house", 3,
        GenreCharacteristics(
            tempo_range=(125, 128),
            common_keys=["G minor", "C minor", "F minor"],
            typical_instruments=["future_bass", "metallic_synths", "vocal_chops"],
            mood_descriptors=["futuristic", "bouncy", "modern", "energetic"],
            rhythm_patterns=["future_bounce", "vocal_chops", "metallic_elements"]
        )
    ))
    
    return house


def create_techno_hierarchy() -> GenreNode:
    """
    테크노 (Techno) - 미니멀하고 반복적인 전자음악
    
    1980년대 디트로이트에서 시작된 일렉트로닉 댄스 음악으로, 미니멀한 구조와
    반복적인 패턴, 기계적인 사운드가 특징입니다. 산업 도시의 분위기를 반영합니다.
    """
    techno = GenreNode(
        "techno",
        2,
        GenreCharacteristics(
            tempo_range=(120, 150),
            common_keys=["C minor", "A minor", "F minor", "G minor"],
            typical_instruments=["analog_synths", "drum_machines", "industrial_sounds"],
            mood_descriptors=["mechanical", "hypnotic", "industrial", "minimal"],
            rhythm_patterns=["techno_kick", "minimal_loops", "industrial_rhythms"],
            cultural_context="1980년대 디트로이트"
        )
    )
    
    # 미니멀 테크노 - 극도로 단순화된 테크노
    techno.add_child(GenreNode(
        "minimal_techno", 3,
        GenreCharacteristics(
            tempo_range=(125, 135),
            common_keys=["C minor", "F minor"],
            typical_instruments=["minimal_synths", "subtle_percussion", "space_elements"],
            mood_descriptors=["minimal", "hypnotic", "subtle", "spacious"],
            rhythm_patterns=["minimal_kicks", "subtle_variations", "spacious_arrangement"]
        )
    ))
    
    # 하드 테크노 - 더 강하고 공격적인 테크노
    techno.add_child(GenreNode(
        "hard_techno", 3,
        GenreCharacteristics(
            tempo_range=(140, 150),
            common_keys=["C minor", "G minor", "Bb minor"],
            typical_instruments=["hard_kicks", "distorted_synths", "aggressive_elements"],
            mood_descriptors=["hard", "aggressive", "intense", "driving"],
            rhythm_patterns=["hard_kicks", "aggressive_loops", "intense_builds"]
        )
    ))
    
    # 멜로딕 테크노 - 멜로디가 강조된 테크노
    techno.add_child(GenreNode(
        "melodic_techno", 3,
        GenreCharacteristics(
            tempo_range=(120, 130),
            common_keys=["A minor", "E minor", "D minor"],
            typical_instruments=["melodic_synths", "emotional_pads", "arpeggiated_sequences"],
            mood_descriptors=["melodic", "emotional", "atmospheric", "uplifting"],
            rhythm_patterns=["melodic_sequences", "emotional_builds", "atmospheric_textures"]
        )
    ))
    
    return techno


def create_trance_hierarchy() -> GenreNode:
    """
    트랜스 (Trance) - 몽환적이고 상승감 있는 댄스 음악
    
    1990년대 독일에서 시작된 일렉트로닉 댄스 음악으로, 몽환적인 멜로디와
    점진적인 빌드업, 감정적인 브레이크다운이 특징입니다.
    """
    trance = GenreNode(
        "trance",
        2,
        GenreCharacteristics(
            tempo_range=(128, 140),
            common_keys=["C major", "A minor", "F major", "G major"],
            typical_instruments=["trance_synths", "arpeggios", "emotional_pads"],
            mood_descriptors=["uplifting", "emotional", "euphoric", "transcendent"],
            rhythm_patterns=["trance_kick", "arpeggiated_bass", "emotional_builds"],
            cultural_context="1990년대 독일"
        )
    )
    
    # 업리프팅 트랜스 - 감정적이고 상승감 있는 트랜스
    trance.add_child(GenreNode(
        "uplifting_trance", 3,
        GenreCharacteristics(
            tempo_range=(132, 138),
            common_keys=["C major", "G major", "F major"],
            typical_instruments=["uplifting_leads", "emotional_strings", "epic_pads"],
            mood_descriptors=["uplifting", "euphoric", "emotional", "epic"],
            rhythm_patterns=["uplifting_builds", "emotional_breakdowns", "epic_drops"]
        )
    ))
    
    # 사이키델릭 트랜스 - 환각적이고 실험적인 트랜스
    trance.add_child(GenreNode(
        "psychedelic_trance", 3,
        GenreCharacteristics(
            tempo_range=(140, 150),
            common_keys=["A minor", "E minor", "B minor"],
            typical_instruments=["psychedelic_synths", "trippy_effects", "complex_rhythms"],
            mood_descriptors=["psychedelic", "trippy", "intense", "hypnotic"],
            rhythm_patterns=["psytrance_kick", "trippy_sequences", "complex_patterns"]
        )
    ))
    
    # 프로그레시브 트랜스 - 점진적 발전이 특징인 트랜스
    trance.add_child(GenreNode(
        "progressive_trance", 3,
        GenreCharacteristics(
            tempo_range=(128, 134),
            common_keys=["A minor", "D minor", "C major"],
            typical_instruments=["progressive_bass", "evolving_synths", "atmospheric_elements"],
            mood_descriptors=["progressive", "atmospheric", "building", "sophisticated"],
            rhythm_patterns=["progressive_grooves", "evolving_elements", "sophisticated_builds"]
        )
    ))
    
    return trance


def create_dubstep_hierarchy() -> GenreNode:
    """
    더브스텝 (Dubstep) - 강한 베이스와 신코페이션이 특징
    
    2000년대 초 영국 런던에서 시작된 일렉트로닉 음악으로, 강한 베이스라인과
    신코페이션된 드럼 패턴, 하프타임 리듬이 특징입니다.
    """
    dubstep = GenreNode(
        "dubstep",
        2,
        GenreCharacteristics(
            tempo_range=(140, 150),
            common_keys=["C minor", "F minor", "G minor", "Bb minor"],
            typical_instruments=["wobble_bass", "snare_drums", "sub_bass"],
            mood_descriptors=["heavy", "aggressive", "electronic", "bass_heavy"],
            rhythm_patterns=["halftime_drums", "wobble_bass", "syncopated_rhythms"],
            cultural_context="2000년대 영국 런던"
        )
    )
    
    # 브로스텝 - 더 공격적이고 강한 더브스텝
    dubstep.add_child(GenreNode(
        "brostep", 3,
        GenreCharacteristics(
            tempo_range=(140, 150),
            common_keys=["C minor", "F minor"],
            typical_instruments=["aggressive_bass", "distorted_synths", "heavy_drops"],
            mood_descriptors=["aggressive", "heavy", "intense", "chaotic"],
            rhythm_patterns=["heavy_drops", "aggressive_wobbles", "chaotic_rhythms"]
        )
    ))
    
    # 리퀴드 더브스텝 - 더 부드럽고 멜로딕한 더브스텝
    dubstep.add_child(GenreNode(
        "liquid_dubstep", 3,
        GenreCharacteristics(
            tempo_range=(140, 145),
            common_keys=["A minor", "C major", "F major"],
            typical_instruments=["smooth_bass", "melodic_elements", "liquid_pads"],
            mood_descriptors=["smooth", "melodic", "flowing", "emotional"],
            rhythm_patterns=["smooth_bass", "melodic_drops", "flowing_rhythms"]
        )
    ))
    
    # 미드템포 베이스 - 더 느린 템포의 베이스 음악
    dubstep.add_child(GenreNode(
        "midtempo_bass", 3,
        GenreCharacteristics(
            tempo_range=(90, 110),
            common_keys=["C minor", "G minor"],
            typical_instruments=["midtempo_bass", "industrial_elements", "dark_synths"],
            mood_descriptors=["dark", "industrial", "heavy", "atmospheric"],
            rhythm_patterns=["midtempo_groove", "industrial_rhythms", "dark_atmospheres"]
        )
    ))
    
    return dubstep


def create_ambient_hierarchy() -> GenreNode:
    """
    앰비언트 (Ambient) - 분위기와 공간감을 중시하는 전자음악
    
    1970년대 브라이언 이노에 의해 정의된 장르로, 분위기와 공간감을 중시하며
    배경음악으로서의 역할을 하는 전자음악입니다.
    """
    ambient = GenreNode(
        "ambient",
        2,
        GenreCharacteristics(
            tempo_range=(60, 100),
            common_keys=["C major", "A minor", "F major", "G major"],
            typical_instruments=["ambient_pads", "field_recordings", "atmospheric_textures"],
            mood_descriptors=["atmospheric", "spacious", "meditative", "peaceful"],
            rhythm_patterns=["minimal_rhythms", "atmospheric_textures", "spacious_arrangements"]
        )
    )
    
    # 다크 앰비언트 - 어둡고 분위기 있는 앰비언트
    ambient.add_child(GenreNode(
        "dark_ambient", 3,
        GenreCharacteristics(
            tempo_range=(60, 80),
            common_keys=["A minor", "D minor", "F minor"],
            typical_instruments=["dark_drones", "eerie_textures", "industrial_sounds"],
            mood_descriptors=["dark", "eerie", "mysterious", "haunting"],
            rhythm_patterns=["minimal_dark_rhythms", "eerie_textures", "haunting_atmospheres"]
        )
    ))
    
    # 스페이스 앰비언트 - 우주적이고 광활한 앰비언트
    ambient.add_child(GenreNode(
        "space_ambient", 3,
        GenreCharacteristics(
            tempo_range=(50, 90),
            common_keys=["C major", "G major", "F major"],
            typical_instruments=["cosmic_pads", "space_effects", "ethereal_textures"],
            mood_descriptors=["cosmic", "ethereal", "vast", "transcendent"],
            rhythm_patterns=["cosmic_rhythms", "ethereal_textures", "vast_soundscapes"]
        )
    ))
    
    return ambient


def create_drum_and_bass_hierarchy() -> GenreNode:
    """
    드럼 앤 베이스 (Drum & Bass) - 빠른 브레이크비트와 헤비 베이스
    
    1990년대 초 영국에서 시작된 일렉트로닉 음악으로, 빠른 브레이크비트 드럼과
    헤비한 베이스라인이 특징입니다.
    """
    drum_and_bass = GenreNode(
        "drum_and_bass",
        2,
        GenreCharacteristics(
            tempo_range=(160, 180),
            common_keys=["A minor", "E minor", "C minor", "G minor"],
            typical_instruments=["breakbeats", "sub_bass", "chopped_samples"],
            mood_descriptors=["energetic", "fast", "rhythmic", "urban"],
            rhythm_patterns=["amen_breaks", "sub_bass_lines", "chopped_samples"],
            cultural_context="1990년대 영국"
        )
    )
    
    # 리퀴드 DnB - 더 부드럽고 재즈적인 드럼 앤 베이스
    drum_and_bass.add_child(GenreNode(
        "liquid_dnb", 3,
        GenreCharacteristics(
            tempo_range=(170, 175),
            common_keys=["C major", "F major", "A minor"],
            typical_instruments=["smooth_bass", "jazz_samples", "liquid_pads"],
            mood_descriptors=["smooth", "jazzy", "flowing", "soulful"],
            rhythm_patterns=["smooth_breaks", "jazz_influenced", "liquid_grooves"]
        )
    ))
    
    # 뉴로 베이스 - 더 복잡하고 기술적인 베이스
    drum_and_bass.add_child(GenreNode(
        "neurobass", 3,
        GenreCharacteristics(
            tempo_range=(170, 180),
            common_keys=["C minor", "F minor"],
            typical_instruments=["complex_bass", "technical_drums", "neuro_synths"],
            mood_descriptors=["technical", "complex", "futuristic", "precise"],
            rhythm_patterns=["complex_breaks", "technical_bass", "neuro_patterns"]
        )
    ))
    
    return drum_and_bass


def create_electronic_hierarchy() -> GenreNode:
    """일렉트로닉 메인 장르 계층 구조 생성"""
    
    # === 일렉트로닉 메인 장르 ===
    electronic = GenreNode(
        "electronic", 
        1,
        GenreCharacteristics(
            tempo_range=(50, 200),
            common_keys=["C major", "A minor", "F major", "G major", "C minor"],
            typical_instruments=["synthesizers", "drum_machines", "samples", "effects"],
            mood_descriptors=["electronic", "synthetic", "modern", "technological"],
            rhythm_patterns=["electronic_beats", "synthesized_sounds", "digital_effects"],
            cultural_context="1940년대부터 현재"
        )
    )
    
    # 세부 장르들 추가
    electronic.add_child(create_house_hierarchy())
    electronic.add_child(create_techno_hierarchy())
    electronic.add_child(create_trance_hierarchy())
    electronic.add_child(create_dubstep_hierarchy())
    electronic.add_child(create_ambient_hierarchy())
    electronic.add_child(create_drum_and_bass_hierarchy())
    
    return electronic 