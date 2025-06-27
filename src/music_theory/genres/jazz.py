"""
재즈 (Jazz) 장르 계층 정의

재즈는 19세기 말 미국 남부에서 시작된 음악 장르로, 즉흥연주, 스윙 리듬, 
블루 노트가 특징입니다. 아프리카계 미국인 음악 전통과 유럽 음악의 
융합으로 탄생했으며, 20세기 음악에 큰 영향을 미쳤습니다.

세부 장르:
- 스무스 재즈 (Smooth Jazz): 부드럽고 접근하기 쉬운 재즈 스타일
- 비밥 (Bebop): 복잡한 화성과 빠른 템포의 전통 재즈
- 라틴 재즈 (Latin Jazz): 라틴 리듬과 재즈의 융합
- 애시드 재즈 (Acid Jazz): 펑크와 힙합 요소가 가미된 현대 재즈
- 퓨전 재즈 (Fusion Jazz): 록과 일렉트로닉 요소를 도입한 재즈
- 프리 재즈 (Free Jazz): 전통적 구조에서 벗어난 실험적 재즈
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_smooth_jazz_hierarchy() -> GenreNode:
    """
    스무스 재즈 (Smooth Jazz) - 부드럽고 접근하기 쉬운 재즈 스타일
    
    1970년대에 등장한 재즈 스타일로, 전통 재즈보다 더 부드럽고 멜로딕하며
    상업적으로 접근하기 쉬운 특징을 가지고 있습니다. 라디오 친화적인 재즈입니다.
    """
    smooth_jazz = GenreNode(
        "smooth_jazz",
        2,
        GenreCharacteristics(
            tempo_range=(80, 120),
            common_keys=["C major", "F major", "G major", "A minor"],
            typical_instruments=["saxophone", "electric_piano", "smooth_guitar", "soft_drums"],
            mood_descriptors=["smooth", "relaxing", "melodic", "sophisticated"],
            rhythm_patterns=["smooth_groove", "relaxed_swing", "contemporary_feel"],
            cultural_context="1970년대 미국"
        )
    )
    
    # 퓨전 재즈 - 록과 일렉트로닉 요소가 가미된 재즈
    smooth_jazz.add_child(GenreNode(
        "fusion_jazz", 3,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["electric_guitar", "synthesizer", "electric_bass", "fusion_drums"],
            mood_descriptors=["energetic", "electric", "modern", "technical"],
            rhythm_patterns=["fusion_grooves", "rock_influenced", "electric_energy"]
        )
    ))
    
    # 컨템포러리 재즈 - 현대적인 재즈 스타일
    smooth_jazz.add_child(GenreNode(
        "contemporary_jazz", 3,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["C major", "F major", "Bb major"],
            typical_instruments=["modern_instruments", "contemporary_arrangements", "polished_production"],
            mood_descriptors=["contemporary", "polished", "accessible", "modern"],
            rhythm_patterns=["contemporary_grooves", "modern_arrangements", "accessible_rhythms"]
        )
    ))
    
    # 칠 재즈 - 편안하고 차분한 재즈
    smooth_jazz.add_child(GenreNode(
        "chill_jazz", 3,
        GenreCharacteristics(
            tempo_range=(70, 100),
            common_keys=["A minor", "D minor", "F major"],
            typical_instruments=["mellow_instruments", "soft_percussion", "ambient_elements"],
            mood_descriptors=["chill", "relaxed", "ambient", "peaceful"],
            rhythm_patterns=["chill_grooves", "relaxed_rhythms", "ambient_textures"]
        )
    ))
    
    return smooth_jazz


def create_bebop_hierarchy() -> GenreNode:
    """
    비밥 (Bebop) - 복잡한 화성과 빠른 템포의 전통 재즈
    
    1940년대에 등장한 재즈 스타일로, 복잡한 화성 진행과 빠른 템포,
    즉흥연주에 중점을 둔 전통적이면서도 혁신적인 재즈입니다.
    """
    bebop = GenreNode(
        "bebop",
        2,
        GenreCharacteristics(
            tempo_range=(120, 200),
            common_keys=["Bb major", "F major", "C major", "G major"],
            typical_instruments=["trumpet", "saxophone", "piano", "upright_bass", "jazz_drums"],
            mood_descriptors=["energetic", "complex", "improvisational", "sophisticated"],
            rhythm_patterns=["swing_rhythm", "complex_syncopation", "bebop_lines"],
            cultural_context="1940년대 미국"
        )
    )
    
    # 하드 밥 - 더 강하고 블루지한 비밥
    bebop.add_child(GenreNode(
        "hard_bop", 3,
        GenreCharacteristics(
            tempo_range=(120, 180),
            common_keys=["F major", "Bb major", "C minor"],
            typical_instruments=["hard_bop_horns", "bluesy_piano", "driving_rhythm"],
            mood_descriptors=["hard", "bluesy", "driving", "soulful"],
            rhythm_patterns=["hard_swing", "bluesy_grooves", "driving_rhythms"]
        )
    ))
    
    # 쿨 재즈 - 더 차분하고 절제된 재즈
    bebop.add_child(GenreNode(
        "cool_jazz", 3,
        GenreCharacteristics(
            tempo_range=(80, 140),
            common_keys=["C major", "F major", "A minor"],
            typical_instruments=["muted_trumpet", "cool_saxophone", "subtle_rhythm"],
            mood_descriptors=["cool", "subtle", "restrained", "intellectual"],
            rhythm_patterns=["subtle_swing", "restrained_grooves", "cool_arrangements"]
        )
    ))
    
    # 모던 재즈 - 현대적으로 해석된 전통 재즈
    bebop.add_child(GenreNode(
        "modern_jazz", 3,
        GenreCharacteristics(
            tempo_range=(100, 180),
            common_keys=["G major", "D major", "E minor"],
            typical_instruments=["modern_horns", "contemporary_rhythm", "updated_arrangements"],
            mood_descriptors=["modern", "updated", "fresh", "contemporary"],
            rhythm_patterns=["modern_swing", "contemporary_grooves", "updated_feel"]
        )
    ))
    
    return bebop


def create_latin_jazz_hierarchy() -> GenreNode:
    """
    라틴 재즈 (Latin Jazz) - 라틴 리듬과 재즈의 융합
    
    재즈와 라틴 아메리카 음악의 융합으로 탄생한 장르로, 
    복잡한 리듬 패턴과 라틴 타악기가 특징입니다.
    """
    latin_jazz = GenreNode(
        "latin_jazz",
        2,
        GenreCharacteristics(
            tempo_range=(100, 160),
            common_keys=["C major", "F major", "G major", "A minor"],
            typical_instruments=["latin_percussion", "congas", "timbales", "latin_piano"],
            mood_descriptors=["rhythmic", "passionate", "danceable", "exotic"],
            rhythm_patterns=["latin_rhythms", "clave_patterns", "syncopated_grooves"],
            cultural_context="라틴 아메리카"
        )
    )
    
    # 보사노바 - 브라질의 부드러운 재즈 스타일
    latin_jazz.add_child(GenreNode(
        "bossa_nova", 3,
        GenreCharacteristics(
            tempo_range=(100, 130),
            common_keys=["C major", "F major", "A minor"],
            typical_instruments=["nylon_guitar", "soft_vocals", "subtle_percussion"],
            mood_descriptors=["smooth", "romantic", "brazilian", "sophisticated"],
            rhythm_patterns=["bossa_nova_rhythm", "subtle_sway", "brazilian_groove"],
            cultural_context="1950년대 브라질"
        )
    ))
    
    # 살사 재즈 - 살사 리듬과 재즈의 융합
    latin_jazz.add_child(GenreNode(
        "salsa_jazz", 3,
        GenreCharacteristics(
            tempo_range=(120, 160),
            common_keys=["C major", "F major", "Bb major"],
            typical_instruments=["salsa_horns", "latin_piano", "salsa_percussion"],
            mood_descriptors=["energetic", "danceable", "spicy", "vibrant"],
            rhythm_patterns=["salsa_rhythms", "montuno_patterns", "energetic_grooves"]
        )
    ))
    
    # 아프로 쿠반 - 아프리카-쿠바 전통과 재즈의 융합
    latin_jazz.add_child(GenreNode(
        "afro_cuban", 3,
        GenreCharacteristics(
            tempo_range=(110, 150),
            common_keys=["F major", "Bb major", "C major"],
            typical_instruments=["cuban_percussion", "afro_cuban_rhythms", "traditional_instruments"],
            mood_descriptors=["traditional", "spiritual", "rhythmic", "authentic"],
            rhythm_patterns=["afro_cuban_rhythms", "traditional_patterns", "spiritual_grooves"],
            cultural_context="쿠바-아프리카 전통"
        )
    ))
    
    return latin_jazz


def create_acid_jazz_hierarchy() -> GenreNode:
    """
    애시드 재즈 (Acid Jazz) - 펑크와 힙합 요소가 가미된 현대 재즈
    
    1980년대 영국에서 시작된 장르로, 재즈에 펑크, 힙합, 소울 등의 
    요소를 결합한 현대적인 재즈 스타일입니다.
    """
    acid_jazz = GenreNode(
        "acid_jazz",
        2,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["A minor", "E minor", "C major", "F major"],
            typical_instruments=["funky_bass", "hip_hop_drums", "jazz_instruments", "samples"],
            mood_descriptors=["funky", "groovy", "modern", "urban"],
            rhythm_patterns=["funk_grooves", "hip_hop_beats", "jazz_fusion"],
            cultural_context="1980년대 영국"
        )
    )
    
    # 펑크 재즈 - 펑크 요소가 강한 재즈
    acid_jazz.add_child(GenreNode(
        "funk_jazz", 3,
        GenreCharacteristics(
            tempo_range=(100, 120),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["funky_guitar", "slap_bass", "funk_drums"],
            mood_descriptors=["funky", "groovy", "rhythmic", "energetic"],
            rhythm_patterns=["funk_rhythms", "slap_bass_lines", "syncopated_grooves"]
        )
    ))
    
    # 누 재즈 - 일렉트로닉 요소가 가미된 재즈
    acid_jazz.add_child(GenreNode(
        "nu_jazz", 3,
        GenreCharacteristics(
            tempo_range=(80, 110),
            common_keys=["C major", "F major", "A minor"],
            typical_instruments=["electronic_elements", "jazz_instruments", "modern_production"],
            mood_descriptors=["modern", "electronic", "sophisticated", "atmospheric"],
            rhythm_patterns=["electronic_grooves", "modern_jazz_elements", "atmospheric_textures"]
        )
    ))
    
    # 힙합 재즈 - 힙합 요소가 가미된 재즈
    acid_jazz.add_child(GenreNode(
        "hip_hop_jazz", 3,
        GenreCharacteristics(
            tempo_range=(85, 110),
            common_keys=["A minor", "E minor", "C minor"],
            typical_instruments=["jazz_samples", "hip_hop_beats", "turntables"],
            mood_descriptors=["urban", "rhythmic", "sampled", "modern"],
            rhythm_patterns=["hip_hop_beats", "jazz_samples", "urban_grooves"]
        )
    ))
    
    return acid_jazz


def create_fusion_jazz_hierarchy() -> GenreNode:
    """
    퓨전 재즈 (Fusion Jazz) - 록과 일렉트로닉 요소를 도입한 재즈
    
    1960년대 말에 시작된 장르로, 전통 재즈에 록, 펑크, R&B 등의 
    요소를 융합한 실험적인 재즈 스타일입니다.
    """
    fusion_jazz = GenreNode(
        "fusion_jazz",
        2,
        GenreCharacteristics(
            tempo_range=(100, 160),
            common_keys=["E minor", "A minor", "D minor", "G minor"],
            typical_instruments=["electric_instruments", "synthesizers", "fusion_drums"],
            mood_descriptors=["electric", "energetic", "experimental", "technical"],
            rhythm_patterns=["fusion_grooves", "rock_influenced", "complex_rhythms"],
            cultural_context="1960년대 말 미국"
        )
    )
    
    # 록 퓨전 - 록 요소가 강한 퓨전 재즈
    fusion_jazz.add_child(GenreNode(
        "rock_fusion", 3,
        GenreCharacteristics(
            tempo_range=(120, 160),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["electric_guitar", "rock_drums", "electric_bass"],
            mood_descriptors=["energetic", "powerful", "rock_influenced", "driving"],
            rhythm_patterns=["rock_grooves", "powerful_rhythms", "driving_beats"]
        )
    ))
    
    # 일렉트로 퓨전 - 일렉트로닉 요소가 강한 퓨전
    fusion_jazz.add_child(GenreNode(
        "electro_fusion", 3,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["C minor", "F minor", "A minor"],
            typical_instruments=["synthesizers", "electronic_drums", "processed_instruments"],
            mood_descriptors=["electronic", "futuristic", "synthetic", "atmospheric"],
            rhythm_patterns=["electronic_grooves", "synthetic_rhythms", "futuristic_textures"]
        )
    ))
    
    return fusion_jazz


def create_free_jazz_hierarchy() -> GenreNode:
    """
    프리 재즈 (Free Jazz) - 전통적 구조에서 벗어난 실험적 재즈
    
    1950년대 말에 시작된 실험적인 재즈 스타일로, 전통적인 화성 진행과 
    형식에서 벗어나 자유로운 즉흥연주를 추구합니다.
    """
    free_jazz = GenreNode(
        "free_jazz",
        2,
        GenreCharacteristics(
            tempo_range=(60, 200),
            common_keys=["atonal", "free_form", "experimental"],
            typical_instruments=["experimental_instruments", "extended_techniques", "unconventional_sounds"],
            mood_descriptors=["experimental", "avant_garde", "free", "challenging"],
            rhythm_patterns=["free_rhythms", "experimental_patterns", "unconventional_structures"],
            cultural_context="1950년대 말 미국"
        )
    )
    
    # 아방가르드 재즈 - 극도로 실험적인 재즈
    free_jazz.add_child(GenreNode(
        "avant_garde_jazz", 3,
        GenreCharacteristics(
            tempo_range=(40, 220),
            common_keys=["atonal", "experimental"],
            typical_instruments=["extended_techniques", "prepared_instruments", "electronic_manipulation"],
            mood_descriptors=["avant_garde", "challenging", "intellectual", "abstract"],
            rhythm_patterns=["abstract_rhythms", "experimental_structures", "challenging_patterns"]
        )
    ))
    
    # 프리 임프로비제이션 - 완전히 자유로운 즉흥연주
    free_jazz.add_child(GenreNode(
        "free_improvisation", 3,
        GenreCharacteristics(
            tempo_range=(0, 300),
            common_keys=["completely_free", "no_structure"],
            typical_instruments=["any_instruments", "extended_techniques", "unconventional_sounds"],
            mood_descriptors=["completely_free", "spontaneous", "unpredictable", "pure"],
            rhythm_patterns=["no_fixed_rhythm", "spontaneous_patterns", "pure_improvisation"]
        )
    ))
    
    return free_jazz


def create_jazz_hierarchy() -> GenreNode:
    """재즈 메인 장르 계층 구조 생성"""
    
    # === 재즈 메인 장르 ===
    jazz = GenreNode(
        "jazz", 
        1,
        GenreCharacteristics(
            tempo_range=(60, 200),
            common_keys=["Bb major", "F major", "C major", "G major", "A minor"],
            typical_instruments=["saxophone", "trumpet", "piano", "upright_bass", "jazz_drums"],
            mood_descriptors=["improvisational", "sophisticated", "soulful", "expressive"],
            rhythm_patterns=["swing_rhythm", "syncopation", "improvisation", "blue_notes"],
            cultural_context="19세기 말 미국 남부"
        )
    )
    
    # 세부 장르들 추가
    jazz.add_child(create_smooth_jazz_hierarchy())
    jazz.add_child(create_bebop_hierarchy())
    jazz.add_child(create_latin_jazz_hierarchy())
    jazz.add_child(create_acid_jazz_hierarchy())
    jazz.add_child(create_fusion_jazz_hierarchy())
    jazz.add_child(create_free_jazz_hierarchy())
    
    return jazz 