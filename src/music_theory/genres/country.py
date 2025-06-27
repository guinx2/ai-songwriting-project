"""
컨트리 (Country) 장르 계층 정의

컨트리 음악은 1920년대 미국 남부에서 시작된 음악 장르로, 민속 음악, 
서구 음악, 블루스의 영향을 받았습니다. 스토리텔링, 단순한 화성, 
어쿠스틱 악기의 사용이 특징입니다.

세부 장르:
- 클래식 컨트리 (Classic Country): 전통적인 컨트리의 원형
- 아웃로 컨트리 (Outlaw Country): 1970년대 반주류 컨트리 무브먼트
- 컨트리 팝 (Country Pop): 대중적이고 세련된 컨트리
- 얼터너티브 컨트리 (Alternative Country): 독립적이고 실험적인 컨트리
- 블루그래스 (Bluegrass): 빠르고 기교적인 전통 음악
- 호키 톤크 (Honky Tonk): 바 문화에서 나온 댄스 컨트리
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_classic_country_hierarchy() -> GenreNode:
    """
    클래식 컨트리 (Classic Country) - 전통적인 컨트리의 원형
    
    1940-60년대 행크 윌리엄스, 패치 클라인 등에 의해 정립된 전통적인 컨트리로, 
    단순한 구조, 감정적인 가사, 어쿠스틱 악기가 특징입니다.
    """
    classic_country = GenreNode(
        "classic_country",
        2,
        GenreCharacteristics(
            tempo_range=(80, 120),
            common_keys=["G major", "C major", "D major", "A major"],
            typical_instruments=["acoustic_guitar", "fiddle", "steel_guitar", "bass"],
            mood_descriptors=["traditional", "heartfelt", "simple", "authentic"],
            rhythm_patterns=["country_shuffle", "two_step", "waltz"],
            cultural_context="미국 남부"
        )
    )
    
    # 행크 윌리엄스 스타일 - 컨트리의 아버지
    classic_country.add_child(GenreNode(
        "hank_williams_style", 3,
        GenreCharacteristics(
            tempo_range=(90, 110),
            common_keys=["G major", "C major", "D major"],
            typical_instruments=["acoustic_guitar", "fiddle", "simple_rhythm"],
            mood_descriptors=["raw", "emotional", "simple", "pioneering"],
            rhythm_patterns=["hank_shuffle", "simple_country", "emotional_delivery"]
        )
    ))
    
    # 내쉬빌 사운드 - 1950-60년대 세련된 컨트리
    classic_country.add_child(GenreNode(
        "nashville_sound", 3,
        GenreCharacteristics(
            tempo_range=(80, 110),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["smooth_vocals", "string_section", "background_vocals"],
            mood_descriptors=["smooth", "polished", "sophisticated", "commercial"],
            rhythm_patterns=["smooth_country", "polished_production", "crossover_appeal"]
        )
    ))
    
    # 바커스필드 사운드 - 서부 컨트리
    classic_country.add_child(GenreNode(
        "bakersfield_sound", 3,
        GenreCharacteristics(
            tempo_range=(100, 130),
            common_keys=["E major", "A major", "B major"],
            typical_instruments=["telecaster_guitar", "loud_drums", "electric_bass"],
            mood_descriptors=["electric", "raw", "working_class", "honky_tonk"],
            rhythm_patterns=["bakersfield_shuffle", "electric_country", "honky_tonk_beat"]
        )
    ))
    
    return classic_country


def create_outlaw_country_hierarchy() -> GenreNode:
    """
    아웃로 컨트리 (Outlaw Country) - 1970년대 반주류 컨트리 무브먼트
    
    윌리 넬슨, 웨일론 제닝스 등이 주도한 반주류 컨트리 운동으로, 
    더 자유롭고 록적인 사운드, 반항적인 가사가 특징입니다.
    """
    outlaw_country = GenreNode(
        "outlaw_country",
        2,
        GenreCharacteristics(
            tempo_range=(85, 125),
            common_keys=["A minor", "E minor", "G major", "D major"],
            typical_instruments=["electric_guitar", "harmonica", "rough_vocals", "rock_drums"],
            mood_descriptors=["rebellious", "raw", "independent", "gritty"],
            rhythm_patterns=["outlaw_shuffle", "rock_influence", "rebellious_groove"],
            cultural_context="텍사스"
        )
    )
    
    # 윌리 넬슨 스타일 - 재즈 영향의 아웃로 컨트리
    outlaw_country.add_child(GenreNode(
        "willie_nelson_style", 3,
        GenreCharacteristics(
            tempo_range=(80, 105),
            common_keys=["A major", "D major", "G major"],
            typical_instruments=["nylon_string_guitar", "jazz_chords", "laid_back_vocals"],
            mood_descriptors=["laid_back", "jazzy", "conversational", "relaxed"],
            rhythm_patterns=["willie_swing", "jazz_country", "conversational_delivery"]
        )
    ))
    
    # 웨일론 제닝스 스타일 - 록 영향의 아웃로 컨트리
    outlaw_country.add_child(GenreNode(
        "waylon_jennings_style", 3,
        GenreCharacteristics(
            tempo_range=(95, 125),
            common_keys=["E minor", "A minor", "D major"],
            typical_instruments=["electric_guitar", "rock_drums", "driving_bass"],
            mood_descriptors=["driving", "rock_influenced", "rebellious", "powerful"],
            rhythm_patterns=["waylon_drive", "rock_country", "driving_rhythm"]
        )
    ))
    
    # 스티브 얼 스타일 - 모던 아웃로 컨트리
    outlaw_country.add_child(GenreNode(
        "steve_earle_style", 3,
        GenreCharacteristics(
            tempo_range=(90, 120),
            common_keys=["G major", "C major", "A minor"],
            typical_instruments=["alternative_guitars", "modern_production", "storytelling_vocals"],
            mood_descriptors=["modern", "literary", "political", "alternative"],
            rhythm_patterns=["modern_outlaw", "alternative_country", "literary_storytelling"]
        )
    ))
    
    return outlaw_country


def create_country_pop_hierarchy() -> GenreNode:
    """
    컨트리 팝 (Country Pop) - 대중적이고 세련된 컨트리
    
    1980년대 이후 등장한 대중적인 컨트리로, 팝 요소의 도입과 
    세련된 프로덕션, 크로스오버 어필이 특징입니다.
    """
    country_pop = GenreNode(
        "country_pop",
        2,
        GenreCharacteristics(
            tempo_range=(90, 140),
            common_keys=["C major", "G major", "F major", "A major"],
            typical_instruments=["electric_guitar", "synthesizers", "polished_vocals", "pop_drums"],
            mood_descriptors=["polished", "commercial", "accessible", "contemporary"],
            rhythm_patterns=["pop_country", "radio_friendly", "crossover_appeal"],
            cultural_context="메인스트림"
        )
    )
    
    # 1980년대 컨트리 팝 - 초기 크로스오버
    country_pop.add_child(GenreNode(
        "80s_country_pop", 3,
        GenreCharacteristics(
            tempo_range=(95, 125),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["80s_production", "synthesizers", "big_vocals"],
            mood_descriptors=["80s_style", "big_production", "crossover", "radio_friendly"],
            rhythm_patterns=["80s_country", "big_production", "decade_specific"]
        )
    ))
    
    # 모던 컨트리 팝 - 현대적 컨트리 팝
    country_pop.add_child(GenreNode(
        "modern_country_pop", 3,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["G major", "C major", "A major"],
            typical_instruments=["modern_production", "pop_elements", "contemporary_vocals"],
            mood_descriptors=["contemporary", "mainstream", "polished", "youthful"],
            rhythm_patterns=["modern_country", "pop_influenced", "contemporary_production"]
        )
    ))
    
    # 컨트리 록 - 록과 융합된 컨트리
    country_pop.add_child(GenreNode(
        "country_rock", 3,
        GenreCharacteristics(
            tempo_range=(110, 140),
            common_keys=["A major", "D major", "E major"],
            typical_instruments=["rock_guitars", "driving_drums", "powerful_vocals"],
            mood_descriptors=["energetic", "rock_influenced", "driving", "powerful"],
            rhythm_patterns=["country_rock_drive", "rock_energy", "driving_country"]
        )
    ))
    
    return country_pop


def create_alternative_country_hierarchy() -> GenreNode:
    """
    얼터너티브 컨트리 (Alternative Country) - 독립적이고 실험적인 컨트리
    
    1990년대 등장한 독립적인 컨트리로, 전통적인 컨트리 요소에 
    인디 록과 얼터너티브 록의 영향이 더해진 것이 특징입니다.
    """
    alternative_country = GenreNode(
        "alternative_country",
        2,
        GenreCharacteristics(
            tempo_range=(80, 130),
            common_keys=["A minor", "E minor", "G major", "C major"],
            typical_instruments=["indie_guitars", "alternative_production", "authentic_vocals"],
            mood_descriptors=["independent", "authentic", "experimental", "alternative"],
            rhythm_patterns=["alt_country", "indie_influence", "experimental_country"],
            cultural_context="인디 씬"
        )
    )
    
    # 언클 투팬 스타일 - 얼터너티브 컨트리 개척자
    alternative_country.add_child(GenreNode(
        "uncle_tupelo_style", 3,
        GenreCharacteristics(
            tempo_range=(85, 115),
            common_keys=["G major", "C major", "A minor"],
            typical_instruments=["punk_energy", "country_instruments", "raw_production"],
            mood_descriptors=["pioneering", "punk_influenced", "raw", "influential"],
            rhythm_patterns=["punk_country", "pioneering_alt_country", "raw_energy"]
        )
    ))
    
    # 윌코 스타일 - 실험적 얼터너티브 컨트리
    alternative_country.add_child(GenreNode(
        "wilco_style", 3,
        GenreCharacteristics(
            tempo_range=(75, 120),
            common_keys=["C major", "A minor", "F major"],
            typical_instruments=["experimental_guitars", "innovative_production", "artistic_vocals"],
            mood_descriptors=["experimental", "artistic", "innovative", "evolved"],
            rhythm_patterns=["experimental_country", "artistic_innovation", "progressive_alt_country"]
        )
    ))
    
    # 라이언 아담스 스타일 - 인디 팝 얼터너티브 컨트리
    alternative_country.add_child(GenreNode(
        "ryan_adams_style", 3,
        GenreCharacteristics(
            tempo_range=(80, 110),
            common_keys=["A minor", "E minor", "C major"],
            typical_instruments=["indie_production", "emotional_guitars", "heartfelt_vocals"],
            mood_descriptors=["emotional", "indie_influenced", "heartfelt", "melodic"],
            rhythm_patterns=["indie_country", "emotional_delivery", "melodic_alt_country"]
        )
    ))
    
    return alternative_country


def create_bluegrass_hierarchy() -> GenreNode:
    """
    블루그래스 (Bluegrass) - 빠르고 기교적인 전통 음악
    
    1940년대 빌 먼로에 의해 개발된 어쿠스틱 음악으로, 
    빠른 템포, 기교적인 연주, 하모니가 특징입니다.
    """
    bluegrass = GenreNode(
        "bluegrass",
        2,
        GenreCharacteristics(
            tempo_range=(120, 180),
            common_keys=["G major", "D major", "A major", "C major"],
            typical_instruments=["banjo", "mandolin", "fiddle", "acoustic_guitar", "upright_bass"],
            mood_descriptors=["energetic", "traditional", "virtuosic", "acoustic"],
            rhythm_patterns=["bluegrass_drive", "acoustic_virtuosity", "traditional_harmony"],
            cultural_context="애팔래치아"
        )
    )
    
    # 전통 블루그래스 - 빌 먼로 스타일
    bluegrass.add_child(GenreNode(
        "traditional_bluegrass", 3,
        GenreCharacteristics(
            tempo_range=(140, 180),
            common_keys=["G major", "D major", "A major"],
            typical_instruments=["classic_instrumentation", "high_lonesome_vocals", "traditional_harmony"],
            mood_descriptors=["traditional", "high_energy", "authentic", "virtuosic"],
            rhythm_patterns=["bill_monroe_style", "high_lonesome", "traditional_drive"]
        )
    ))
    
    # 프로그레시브 블루그래스 - 현대적 블루그래스
    bluegrass.add_child(GenreNode(
        "progressive_bluegrass", 3,
        GenreCharacteristics(
            tempo_range=(120, 160),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["modern_arrangements", "complex_harmony", "innovative_playing"],
            mood_descriptors=["progressive", "complex", "innovative", "contemporary"],
            rhythm_patterns=["progressive_bluegrass", "complex_arrangements", "innovative_harmony"]
        )
    ))
    
    # 뉴그래스 - 록 영향의 블루그래스
    bluegrass.add_child(GenreNode(
        "newgrass", 3,
        GenreCharacteristics(
            tempo_range=(110, 150),
            common_keys=["A major", "E major", "D major"],
            typical_instruments=["electric_elements", "rock_influence", "fusion_instruments"],
            mood_descriptors=["fusion", "rock_influenced", "electric", "contemporary"],
            rhythm_patterns=["newgrass_fusion", "rock_bluegrass", "electric_acoustic_blend"]
        )
    ))
    
    return bluegrass


def create_honky_tonk_hierarchy() -> GenreNode:
    """
    호키 톤크 (Honky Tonk) - 바 문화에서 나온 댄스 컨트리
    
    1940-50년대 텍사스와 오클라호마의 바에서 발전한 댄스 지향적 컨트리로, 
    전기 악기, 댄스 리듬, 술과 사랑에 관한 가사가 특징입니다.
    """
    honky_tonk = GenreNode(
        "honky_tonk",
        2,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["E major", "A major", "B major", "D major"],
            typical_instruments=["electric_guitar", "steel_guitar", "piano", "drums"],
            mood_descriptors=["danceable", "barroom", "working_class", "rough"],
            rhythm_patterns=["honky_tonk_shuffle", "two_step", "dance_rhythm"],
            cultural_context="텍사스 바"
        )
    )
    
    # 클래식 호키 톤크 - 1940-50년대 스타일
    honky_tonk.add_child(GenreNode(
        "classic_honky_tonk", 3,
        GenreCharacteristics(
            tempo_range=(110, 130),
            common_keys=["E major", "A major", "B major"],
            typical_instruments=["steel_guitar", "honky_tonk_piano", "electric_guitar"],
            mood_descriptors=["classic", "barroom", "authentic", "rough"],
            rhythm_patterns=["classic_shuffle", "barroom_beat", "dance_ready"]
        )
    ))
    
    # 네오 트래디셔널 - 1980년대 호키 톤크 부활
    honky_tonk.add_child(GenreNode(
        "neo_traditional", 3,
        GenreCharacteristics(
            tempo_range=(100, 125),
            common_keys=["D major", "G major", "A major"],
            typical_instruments=["traditional_instruments", "modern_production", "authentic_approach"],
            mood_descriptors=["neo_traditional", "authentic", "revivalist", "contemporary"],
            rhythm_patterns=["neo_trad_shuffle", "revivalist_approach", "modern_traditional"]
        )
    ))
    
    return honky_tonk


def create_country_hierarchy() -> GenreNode:
    """
    컨트리 메인 계층 생성
    """
    country = GenreNode(
        "country",
        1,
        GenreCharacteristics(
            tempo_range=(60, 180),
            common_keys=["G major", "C major", "D major", "A major"],
            typical_instruments=["guitar", "vocals", "fiddle", "steel_guitar"],
            mood_descriptors=["storytelling", "heartfelt", "authentic", "american"],
            rhythm_patterns=["country_rhythm", "storytelling", "american_roots"],
            cultural_context="미국"
        )
    )
    
    # 서브 장르들 추가
    country.add_child(create_classic_country_hierarchy())
    country.add_child(create_outlaw_country_hierarchy())
    country.add_child(create_country_pop_hierarchy())
    country.add_child(create_alternative_country_hierarchy())
    country.add_child(create_bluegrass_hierarchy())
    country.add_child(create_honky_tonk_hierarchy())
    
    return country 