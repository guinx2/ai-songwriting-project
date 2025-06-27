"""
포크 (Folk) 장르 계층 정의

포크 음악은 전통적으로 구전으로 전해져 내려온 민속 음악으로, 각 지역과 문화의 
고유한 특성을 반영합니다. 단순한 멜로디, 어쿠스틱 악기, 스토리텔링이 특징입니다.

세부 장르:
- 트래디셔널 포크 (Traditional Folk): 각 지역의 전통 민속 음악
- 컨템포러리 포크 (Contemporary Folk): 현대적으로 재해석된 포크
- 포크 락 (Folk Rock): 포크와 락의 융합
- 인디 포크 (Indie Folk): 독립적이고 실험적인 포크
- 월드 포크 (World Folk): 세계 각국의 민속 음악
- 어반 포크 (Urban Folk): 도시적 감성의 포크
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_traditional_folk_hierarchy() -> GenreNode:
    """
    트래디셔널 포크 (Traditional Folk) - 각 지역의 전통 민속 음악
    
    수세기에 걸쳐 구전으로 전해져 내려온 전통 민속 음악으로, 
    각 지역과 문화의 고유한 특성과 역사를 담고 있습니다.
    """
    traditional_folk = GenreNode(
        "traditional_folk",
        2,
        GenreCharacteristics(
            tempo_range=(60, 120),
            common_keys=["G major", "D major", "A major", "C major"],
            typical_instruments=["acoustic_guitar", "fiddle", "banjo", "harmonica"],
            mood_descriptors=["traditional", "authentic", "cultural", "storytelling"],
            rhythm_patterns=["folk_rhythm", "traditional_patterns", "cultural_beats"],
            cultural_context="전통 문화"
        )
    )
    
    # 아메리칸 포크 - 미국 전통 민속 음악
    traditional_folk.add_child(GenreNode(
        "american_folk", 3,
        GenreCharacteristics(
            tempo_range=(70, 110),
            common_keys=["G major", "C major", "D major"],
            typical_instruments=["acoustic_guitar", "banjo", "harmonica", "fiddle"],
            mood_descriptors=["american", "rootsy", "historical", "pioneering"],
            rhythm_patterns=["american_folk", "frontier_rhythms", "pioneer_songs"]
        )
    ))
    
    # 셀틱 포크 - 아일랜드, 스코틀랜드 전통 음악
    traditional_folk.add_child(GenreNode(
        "celtic_folk", 3,
        GenreCharacteristics(
            tempo_range=(80, 140),
            common_keys=["D major", "A major", "E minor", "B minor"],
            typical_instruments=["fiddle", "tin_whistle", "bodhrán", "celtic_harp"],
            mood_descriptors=["celtic", "mystical", "traditional", "spirited"],
            rhythm_patterns=["jig", "reel", "celtic_rhythms"]
        )
    ))
    
    # 영국 포크 - 영국 전통 민속 음악
    traditional_folk.add_child(GenreNode(
        "british_folk", 3,
        GenreCharacteristics(
            tempo_range=(60, 100),
            common_keys=["G major", "C major", "F major"],
            typical_instruments=["acoustic_guitar", "concertina", "morris_instruments"],
            mood_descriptors=["pastoral", "english", "countryside", "medieval"],
            rhythm_patterns=["english_folk", "morris_dance", "pastoral_rhythms"]
        )
    ))
    
    return traditional_folk


def create_contemporary_folk_hierarchy() -> GenreNode:
    """
    컨템포러리 포크 (Contemporary Folk) - 현대적으로 재해석된 포크
    
    1960년대 포크 리바이벌 이후 등장한 현대적 포크로, 전통적인 포크 요소에 
    현대적 가사와 프로덕션이 더해진 것이 특징입니다.
    """
    contemporary_folk = GenreNode(
        "contemporary_folk",
        2,
        GenreCharacteristics(
            tempo_range=(70, 130),
            common_keys=["G major", "C major", "A minor", "D major"],
            typical_instruments=["acoustic_guitar", "harmonica", "modern_vocals", "light_percussion"],
            mood_descriptors=["modern", "introspective", "poetic", "contemporary"],
            rhythm_patterns=["contemporary_folk", "modern_storytelling", "poetic_rhythm"],
            cultural_context="현대"
        )
    )
    
    # 1960년대 포크 리바이벌 - 밥 딜런, 조안 바에즈 시대
    contemporary_folk.add_child(GenreNode(
        "60s_folk_revival", 3,
        GenreCharacteristics(
            tempo_range=(80, 120),
            common_keys=["G major", "D major", "C major"],
            typical_instruments=["acoustic_guitar", "harmonica", "protest_vocals"],
            mood_descriptors=["protest", "social", "revolutionary", "authentic"],
            rhythm_patterns=["protest_folk", "social_rhythm", "revolutionary_beat"]
        )
    ))
    
    # 싱어 송라이터 - 개인적이고 내성적인 포크
    contemporary_folk.add_child(GenreNode(
        "singer_songwriter", 3,
        GenreCharacteristics(
            tempo_range=(60, 100),
            common_keys=["C major", "A minor", "F major"],
            typical_instruments=["acoustic_guitar", "piano", "intimate_vocals"],
            mood_descriptors=["intimate", "personal", "introspective", "confessional"],
            rhythm_patterns=["intimate_folk", "confessional_rhythm", "personal_storytelling"]
        )
    ))
    
    # 네오 포크 - 현대적 포크
    contemporary_folk.add_child(GenreNode(
        "neo_folk", 3,
        GenreCharacteristics(
            tempo_range=(70, 110),
            common_keys=["A minor", "E minor", "G major"],
            typical_instruments=["modern_production", "contemporary_instruments", "updated_folk"],
            mood_descriptors=["modern", "updated", "contemporary", "evolved"],
            rhythm_patterns=["neo_folk_rhythm", "contemporary_patterns", "modern_folk"]
        )
    ))
    
    return contemporary_folk


def create_folk_rock_hierarchy() -> GenreNode:
    """
    포크 락 (Folk Rock) - 포크와 락의 융합
    
    1960년대 중반 밥 딜런의 전기 기타 도입으로 시작된 장르로, 
    포크의 가사와 멜로디에 락의 전기 악기와 에너지를 결합했습니다.
    """
    folk_rock = GenreNode(
        "folk_rock",
        2,
        GenreCharacteristics(
            tempo_range=(90, 140),
            common_keys=["G major", "C major", "A minor", "D major"],
            typical_instruments=["electric_guitar", "bass", "drums", "folk_vocals"],
            mood_descriptors=["energetic", "electric", "revolutionary", "folk_influenced"],
            rhythm_patterns=["folk_rock_rhythm", "electric_folk", "rock_storytelling"],
            cultural_context="1960년대"
        )
    )
    
    # 밥 딜런 스타일 - 포크 락의 창시자
    folk_rock.add_child(GenreNode(
        "bob_dylan_style", 3,
        GenreCharacteristics(
            tempo_range=(100, 130),
            common_keys=["G major", "C major", "D major"],
            typical_instruments=["electric_guitar", "harmonica", "revolutionary_vocals"],
            mood_descriptors=["revolutionary", "poetic", "electric", "groundbreaking"],
            rhythm_patterns=["dylan_rock", "electric_poetry", "revolutionary_rhythm"]
        )
    ))
    
    # 버즈 스타일 - 하모니 중심 포크 락
    folk_rock.add_child(GenreNode(
        "byrds_style", 3,
        GenreCharacteristics(
            tempo_range=(95, 125),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["12_string_guitar", "harmony_vocals", "jangly_guitars"],
            mood_descriptors=["jangly", "harmonic", "californian", "psychedelic"],
            rhythm_patterns=["jangle_folk", "harmony_rock", "californian_folk"]
        )
    ))
    
    # 사이먼 앤 가펑클 스타일 - 하모니 듀오
    folk_rock.add_child(GenreNode(
        "simon_garfunkel_style", 3,
        GenreCharacteristics(
            tempo_range=(70, 110),
            common_keys=["C major", "A minor", "F major"],
            typical_instruments=["acoustic_guitar", "close_harmony", "sophisticated_arrangements"],
            mood_descriptors=["sophisticated", "harmonic", "literary", "melodic"],
            rhythm_patterns=["sophisticated_folk", "harmony_duo", "literary_folk"]
        )
    ))
    
    return folk_rock


def create_indie_folk_hierarchy() -> GenreNode:
    """
    인디 포크 (Indie Folk) - 독립적이고 실험적인 포크
    
    2000년대 이후 등장한 독립적인 포크로, 전통적인 포크 요소에 
    인디 록의 실험성과 DIY 정신이 더해진 것이 특징입니다.
    """
    indie_folk = GenreNode(
        "indie_folk",
        2,
        GenreCharacteristics(
            tempo_range=(80, 130),
            common_keys=["C major", "A minor", "F major", "G major"],
            typical_instruments=["acoustic_guitar", "indie_production", "alternative_instruments"],
            mood_descriptors=["indie", "experimental", "authentic", "creative"],
            rhythm_patterns=["indie_folk_rhythm", "alternative_folk", "creative_patterns"],
            cultural_context="인디 씬"
        )
    )
    
    # 프리포크 - 실험적이고 자유로운 포크
    indie_folk.add_child(GenreNode(
        "freak_folk", 3,
        GenreCharacteristics(
            tempo_range=(60, 120),
            common_keys=["A minor", "E minor", "C major"],
            typical_instruments=["experimental_instruments", "unusual_arrangements", "psychedelic_folk"],
            mood_descriptors=["experimental", "psychedelic", "freaky", "unconventional"],
            rhythm_patterns=["freak_folk_rhythm", "experimental_patterns", "psychedelic_folk"]
        )
    ))
    
    # 안티포크 - 안티 무브먼트의 포크
    indie_folk.add_child(GenreNode(
        "anti_folk", 3,
        GenreCharacteristics(
            tempo_range=(90, 140),
            common_keys=["G major", "C major", "A minor"],
            typical_instruments=["lo_fi_production", "punk_attitude", "anti_establishment"],
            mood_descriptors=["anti_establishment", "punk_influenced", "raw", "rebellious"],
            rhythm_patterns=["anti_folk_rhythm", "punk_folk", "rebellious_patterns"]
        )
    ))
    
    # 체임버 포크 - 클래식 영향의 실험적 포크
    indie_folk.add_child(GenreNode(
        "chamber_folk", 3,
        GenreCharacteristics(
            tempo_range=(70, 110),
            common_keys=["F major", "C major", "A minor"],
            typical_instruments=["string_quartet", "classical_instruments", "chamber_arrangements"],
            mood_descriptors=["classical", "sophisticated", "chamber_influenced", "artistic"],
            rhythm_patterns=["chamber_folk", "classical_folk", "sophisticated_arrangements"]
        )
    ))
    
    return indie_folk


def create_world_folk_hierarchy() -> GenreNode:
    """
    월드 포크 (World Folk) - 세계 각국의 민속 음악
    
    전 세계 각 지역의 전통 민속 음악으로, 각 문화권의 고유한 악기와 
    리듬, 선율이 특징입니다.
    """
    world_folk = GenreNode(
        "world_folk",
        2,
        GenreCharacteristics(
            tempo_range=(60, 160),
            common_keys=["various_scales", "modal_keys", "ethnic_tunings"],
            typical_instruments=["traditional_instruments", "ethnic_percussion", "regional_strings"],
            mood_descriptors=["cultural", "traditional", "ethnic", "authentic"],
            rhythm_patterns=["ethnic_rhythms", "traditional_patterns", "cultural_beats"],
            cultural_context="세계 각국"
        )
    )
    
    # 라틴 포크 - 라틴 아메리카 민속 음악
    world_folk.add_child(GenreNode(
        "latin_folk", 3,
        GenreCharacteristics(
            tempo_range=(80, 140),
            common_keys=["A minor", "E minor", "G major"],
            typical_instruments=["classical_guitar", "charango", "quena", "latin_percussion"],
            mood_descriptors=["latin", "passionate", "traditional", "rhythmic"],
            rhythm_patterns=["latin_folk_rhythms", "traditional_latin", "indigenous_patterns"]
        )
    ))
    
    # 아프리칸 포크 - 아프리카 전통 음악
    world_folk.add_child(GenreNode(
        "african_folk", 3,
        GenreCharacteristics(
            tempo_range=(90, 160),
            common_keys=["pentatonic_scales", "african_modes"],
            typical_instruments=["djembe", "kora", "mbira", "african_drums"],
            mood_descriptors=["rhythmic", "tribal", "spiritual", "communal"],
            rhythm_patterns=["african_polyrhythms", "tribal_beats", "communal_rhythms"]
        )
    ))
    
    # 아시안 포크 - 아시아 전통 음악
    world_folk.add_child(GenreNode(
        "asian_folk", 3,
        GenreCharacteristics(
            tempo_range=(60, 120),
            common_keys=["pentatonic_scales", "asian_modes"],
            typical_instruments=["erhu", "guzheng", "shamisen", "asian_flutes"],
            mood_descriptors=["meditative", "traditional", "spiritual", "ancient"],
            rhythm_patterns=["asian_rhythms", "meditative_patterns", "traditional_asian"]
        )
    ))
    
    return world_folk


def create_urban_folk_hierarchy() -> GenreNode:
    """
    어반 포크 (Urban Folk) - 도시적 감성의 포크
    
    도시 환경에서 발전한 현대적 포크로, 도시적 주제와 현대적 사운드, 
    어반 라이프스타일이 반영된 것이 특징입니다.
    """
    urban_folk = GenreNode(
        "urban_folk",
        2,
        GenreCharacteristics(
            tempo_range=(80, 120),
            common_keys=["C major", "A minor", "F major", "G major"],
            typical_instruments=["acoustic_guitar", "urban_instruments", "modern_production"],
            mood_descriptors=["urban", "contemporary", "city_life", "modern"],
            rhythm_patterns=["urban_folk_rhythm", "city_beats", "contemporary_patterns"],
            cultural_context="도시"
        )
    )
    
    # 카페 포크 - 카페 문화의 포크
    urban_folk.add_child(GenreNode(
        "cafe_folk", 3,
        GenreCharacteristics(
            tempo_range=(70, 100),
            common_keys=["C major", "F major", "A minor"],
            typical_instruments=["acoustic_guitar", "soft_vocals", "intimate_arrangement"],
            mood_descriptors=["intimate", "cozy", "cafe_atmosphere", "relaxed"],
            rhythm_patterns=["cafe_rhythm", "intimate_folk", "cozy_patterns"]
        )
    ))
    
    # 인디 카페 포크 - 독립적인 카페 포크
    urban_folk.add_child(GenreNode(
        "indie_cafe_folk", 3,
        GenreCharacteristics(
            tempo_range=(75, 110),
            common_keys=["A minor", "C major", "G major"],
            typical_instruments=["indie_production", "alternative_arrangements", "creative_vocals"],
            mood_descriptors=["indie", "creative", "alternative", "artistic"],
            rhythm_patterns=["indie_cafe_rhythm", "alternative_folk", "creative_patterns"]
        )
    ))
    
    # 어쿠스틱 팝 - 팝 영향의 어반 포크
    urban_folk.add_child(GenreNode(
        "acoustic_pop", 3,
        GenreCharacteristics(
            tempo_range=(90, 120),
            common_keys=["C major", "G major", "F major"],
            typical_instruments=["acoustic_guitar", "pop_vocals", "accessible_arrangements"],
            mood_descriptors=["accessible", "pop_influenced", "melodic", "commercial"],
            rhythm_patterns=["acoustic_pop_rhythm", "pop_folk", "accessible_patterns"]
        )
    ))
    
    return urban_folk


def create_folk_hierarchy() -> GenreNode:
    """
    포크 메인 계층 생성
    """
    folk = GenreNode(
        "folk",
        1,
        GenreCharacteristics(
            tempo_range=(60, 160),
            common_keys=["G major", "C major", "D major", "A minor"],
            typical_instruments=["acoustic_guitar", "vocals", "harmonica", "fiddle"],
            mood_descriptors=["traditional", "storytelling", "authentic", "cultural"],
            rhythm_patterns=["folk_rhythm", "traditional_patterns", "storytelling_beat"],
            cultural_context="전통"
        )
    )
    
    # 서브 장르들 추가
    folk.add_child(create_traditional_folk_hierarchy())
    folk.add_child(create_contemporary_folk_hierarchy())
    folk.add_child(create_folk_rock_hierarchy())
    folk.add_child(create_indie_folk_hierarchy())
    folk.add_child(create_world_folk_hierarchy())
    folk.add_child(create_urban_folk_hierarchy())
    
    return folk 