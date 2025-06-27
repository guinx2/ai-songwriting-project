"""
레게 (Reggae) 장르 계층 정의

레게는 1960년대 후반 자메이카에서 시작된 음악 장르로, 스카와 록스테디에서 
발전했습니다. 강한 오프비트, 베이스 라인의 중요성, 라스타파리 문화와의 
연관성이 특징입니다.

세부 장르:
- 루츠 레게 (Roots Reggae): 전통적이고 영적인 레게의 원형
- 댄스홀 (Dancehall): 1980년대 등장한 디지털 레게
- 덥 (Dub): 레게의 실험적 변형, 에코와 리버브 중심
- 러버스 락 (Lovers Rock): 로맨틱하고 부드러운 레게
- 레게톤 (Reggaeton): 라틴 아메리카의 레게 변형
- UK 레게 (UK Reggae): 영국에서 발전한 레게 변형
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_roots_reggae_hierarchy() -> GenreNode:
    """
    루츠 레게 (Roots Reggae) - 전통적이고 영적인 레게의 원형
    
    1970년대 밥 말리에 의해 대중화된 전통적인 레게 스타일로, 
    라스타파리 사상과 사회적 메시지, 영적 주제가 특징입니다.
    """
    roots_reggae = GenreNode(
        "roots_reggae",
        2,
        GenreCharacteristics(
            tempo_range=(60, 90),
            common_keys=["A minor", "E minor", "C major", "G major"],
            typical_instruments=["bass_guitar", "drums", "rhythm_guitar", "organ"],
            mood_descriptors=["spiritual", "conscious", "rootsy", "meditative"],
            rhythm_patterns=["one_drop", "rockers", "steppers"],
            cultural_context="자메이카 라스타파리"
        )
    )
    
    # 원 드랍 스타일 - 클래식한 레게 리듬
    roots_reggae.add_child(GenreNode(
        "one_drop_reggae", 3,
        GenreCharacteristics(
            tempo_range=(65, 80),
            common_keys=["A minor", "E minor", "D minor"],
            typical_instruments=["one_drop_drums", "walking_bass", "skank_guitar"],
            mood_descriptors=["meditative", "deep", "spiritual", "grounded"],
            rhythm_patterns=["one_drop_rhythm", "bass_emphasis", "meditative_groove"]
        )
    ))
    
    # 락커스 스타일 - 더 드라이빙한 레게
    roots_reggae.add_child(GenreNode(
        "rockers_reggae", 3,
        GenreCharacteristics(
            tempo_range=(70, 90),
            common_keys=["E minor", "A minor", "C major"],
            typical_instruments=["rockers_drums", "driving_bass", "militant_rhythm"],
            mood_descriptors=["militant", "driving", "powerful", "conscious"],
            rhythm_patterns=["rockers_rhythm", "four_on_floor", "militant_beat"]
        )
    ))
    
    # 나이아빙기 스타일 - 전통적 드러밍
    roots_reggae.add_child(GenreNode(
        "nyabinghi_reggae", 3,
        GenreCharacteristics(
            tempo_range=(60, 75),
            common_keys=["A minor", "D minor", "G major"],
            typical_instruments=["nyabinghi_drums", "traditional_percussion", "chanting"],
            mood_descriptors=["traditional", "ceremonial", "spiritual", "ancient"],
            rhythm_patterns=["nyabinghi_rhythm", "traditional_drums", "ceremonial_beat"]
        )
    ))
    
    return roots_reggae


def create_dancehall_hierarchy() -> GenreNode:
    """
    댄스홀 (Dancehall) - 1980년대 등장한 디지털 레게
    
    1980년대 디지털 악기와 드럼 머신의 도입으로 등장한 레게의 현대적 형태로, 
    더 빠른 템포와 파티 분위기, 디지털 사운드가 특징입니다.
    """
    dancehall = GenreNode(
        "dancehall",
        2,
        GenreCharacteristics(
            tempo_range=(90, 140),
            common_keys=["C minor", "F minor", "A minor", "E minor"],
            typical_instruments=["drum_machine", "digital_bass", "synthesizers", "toasting_vocals"],
            mood_descriptors=["party", "energetic", "digital", "danceable"],
            rhythm_patterns=["dancehall_rhythm", "digital_beats", "party_groove"],
            cultural_context="자메이카 댄스홀"
        )
    )
    
    # 클래식 댄스홀 - 1980년대 스타일
    dancehall.add_child(GenreNode(
        "classic_dancehall", 3,
        GenreCharacteristics(
            tempo_range=(95, 125),
            common_keys=["C minor", "F minor", "A minor"],
            typical_instruments=["casio_mt30", "digital_drums", "sleng_teng_bass"],
            mood_descriptors=["classic", "digital", "pioneering", "raw"],
            rhythm_patterns=["sleng_teng", "classic_digital", "80s_dancehall"]
        )
    ))
    
    # 모던 댄스홀 - 현대적 댄스홀
    dancehall.add_child(GenreNode(
        "modern_dancehall", 3,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["A minor", "E minor", "C minor"],
            typical_instruments=["modern_production", "trap_influenced", "contemporary_vocals"],
            mood_descriptors=["modern", "trap_influenced", "international", "contemporary"],
            rhythm_patterns=["modern_dancehall", "trap_fusion", "contemporary_rhythm"]
        )
    ))
    
    # 로 댄스홀 - 원초적이고 거친 스타일
    dancehall.add_child(GenreNode(
        "raw_dancehall", 3,
        GenreCharacteristics(
            tempo_range=(90, 120),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["minimal_production", "raw_vocals", "street_sounds"],
            mood_descriptors=["raw", "street", "authentic", "hardcore"],
            rhythm_patterns=["raw_rhythm", "street_beats", "hardcore_dancehall"]
        )
    ))
    
    return dancehall


def create_dub_hierarchy() -> GenreNode:
    """
    덥 (Dub) - 레게의 실험적 변형
    
    1970년대 킹 터비와 리 페리에 의해 개발된 레게의 실험적 형태로, 
    에코, 리버브, 딜레이 등의 이펙트와 베이스와 드럼의 강조가 특징입니다.
    """
    dub = GenreNode(
        "dub",
        2,
        GenreCharacteristics(
            tempo_range=(70, 100),
            common_keys=["A minor", "E minor", "C major", "D minor"],
            typical_instruments=["echo_chamber", "spring_reverb", "mixing_board", "effects"],
            mood_descriptors=["spacey", "experimental", "hypnotic", "atmospheric"],
            rhythm_patterns=["dub_rhythm", "space_echo", "experimental_mix"],
            cultural_context="자메이카 스튜디오"
        )
    )
    
    # 킹 터비 스타일 - 클래식 덥의 아버지
    dub.add_child(GenreNode(
        "king_tubby_dub", 3,
        GenreCharacteristics(
            tempo_range=(70, 85),
            common_keys=["A minor", "E minor", "D minor"],
            typical_instruments=["analog_delay", "spring_reverb", "mixing_console"],
            mood_descriptors=["pioneering", "analog", "revolutionary", "deep"],
            rhythm_patterns=["tubby_style", "analog_effects", "revolutionary_mix"]
        )
    ))
    
    # 리 페리 스타일 - 블랙 아크 사운드
    dub.add_child(GenreNode(
        "lee_perry_dub", 3,
        GenreCharacteristics(
            tempo_range=(65, 90),
            common_keys=["E minor", "A minor", "C major"],
            typical_instruments=["black_ark_effects", "experimental_sounds", "psychedelic_mixing"],
            mood_descriptors=["psychedelic", "experimental", "mystical", "cosmic"],
            rhythm_patterns=["black_ark_style", "psychedelic_dub", "cosmic_mixing"]
        )
    ))
    
    # 모던 덥 - 현대적 덥
    dub.add_child(GenreNode(
        "modern_dub", 3,
        GenreCharacteristics(
            tempo_range=(75, 105),
            common_keys=["C major", "A minor", "F major"],
            typical_instruments=["digital_effects", "modern_production", "contemporary_mix"],
            mood_descriptors=["modern", "digital", "contemporary", "evolved"],
            rhythm_patterns=["modern_dub_style", "digital_effects", "contemporary_dub"]
        )
    ))
    
    return dub


def create_lovers_rock_hierarchy() -> GenreNode:
    """
    러버스 락 (Lovers Rock) - 로맨틱하고 부드러운 레게
    
    1970년대 영국에서 발전한 레게의 변형으로, 사랑과 로맨스를 주제로 하며 
    부드럽고 멜로디컬한 사운드가 특징입니다.
    """
    lovers_rock = GenreNode(
        "lovers_rock",
        2,
        GenreCharacteristics(
            tempo_range=(70, 95),
            common_keys=["C major", "F major", "A minor", "G major"],
            typical_instruments=["smooth_bass", "romantic_vocals", "soft_guitars", "gentle_keyboards"],
            mood_descriptors=["romantic", "smooth", "gentle", "loving"],
            rhythm_patterns=["lovers_rhythm", "smooth_groove", "romantic_beat"],
            cultural_context="영국 자메이카 커뮤니티"
        )
    )
    
    # 클래식 러버스 락 - 1970-80년대 스타일
    lovers_rock.add_child(GenreNode(
        "classic_lovers_rock", 3,
        GenreCharacteristics(
            tempo_range=(70, 85),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["vintage_production", "sweet_vocals", "romantic_arrangements"],
            mood_descriptors=["classic", "sweet", "vintage", "heartfelt"],
            rhythm_patterns=["classic_lovers", "sweet_rhythm", "vintage_romance"]
        )
    ))
    
    # 모던 러버스 락 - 현대적 로맨틱 레게
    lovers_rock.add_child(GenreNode(
        "modern_lovers_rock", 3,
        GenreCharacteristics(
            tempo_range=(75, 95),
            common_keys=["A minor", "C major", "F major"],
            typical_instruments=["contemporary_production", "modern_vocals", "updated_arrangements"],
            mood_descriptors=["contemporary", "updated", "modern_romance", "polished"],
            rhythm_patterns=["modern_lovers", "contemporary_romance", "updated_groove"]
        )
    ))
    
    return lovers_rock


def create_reggaeton_hierarchy() -> GenreNode:
    """
    레게톤 (Reggaeton) - 라틴 아메리카의 레게 변형
    
    1990년대 푸에르토리코에서 발전한 장르로, 레게의 리듬에 힙합과 
    라틴 음악의 요소를 결합한 것이 특징입니다.
    """
    reggaeton = GenreNode(
        "reggaeton",
        2,
        GenreCharacteristics(
            tempo_range=(85, 105),
            common_keys=["A minor", "E minor", "C minor", "D minor"],
            typical_instruments=["dembow_drums", "latin_percussion", "rap_vocals", "reggaeton_bass"],
            mood_descriptors=["latin", "urban", "danceable", "rhythmic"],
            rhythm_patterns=["dembow", "reggaeton_beat", "latin_rhythm"],
            cultural_context="푸에르토리코"
        )
    )
    
    # 클래식 레게톤 - 1990-2000년대 스타일
    reggaeton.add_child(GenreNode(
        "classic_reggaeton", 3,
        GenreCharacteristics(
            tempo_range=(90, 100),
            common_keys=["A minor", "E minor", "D minor"],
            typical_instruments=["classic_dembow", "traditional_reggaeton", "old_school_rap"],
            mood_descriptors=["classic", "underground", "raw", "original"],
            rhythm_patterns=["classic_dembow", "old_school_reggaeton", "underground_beat"]
        )
    ))
    
    # 모던 레게톤 - 현대적 메인스트림 레게톤
    reggaeton.add_child(GenreNode(
        "modern_reggaeton", 3,
        GenreCharacteristics(
            tempo_range=(85, 105),
            common_keys=["C minor", "A minor", "E minor"],
            typical_instruments=["modern_production", "pop_influenced", "mainstream_vocals"],
            mood_descriptors=["mainstream", "polished", "commercial", "contemporary"],
            rhythm_patterns=["modern_dembow", "pop_reggaeton", "mainstream_rhythm"]
        )
    ))
    
    # 트랩 레게톤 - 트랩과 융합된 레게톤
    reggaeton.add_child(GenreNode(
        "trap_reggaeton", 3,
        GenreCharacteristics(
            tempo_range=(80, 95),
            common_keys=["C minor", "F minor", "A minor"],
            typical_instruments=["trap_hi_hats", "808_drums", "trap_influenced"],
            mood_descriptors=["trap_influenced", "modern", "dark", "urban"],
            rhythm_patterns=["trap_dembow", "latin_trap", "hybrid_rhythm"]
        )
    ))
    
    return reggaeton


def create_uk_reggae_hierarchy() -> GenreNode:
    """
    UK 레게 (UK Reggae) - 영국에서 발전한 레게 변형
    
    1970년대부터 영국 자메이카 커뮤니티에서 발전한 레게로, 
    영국적 감성과 사회적 의식, 현지 문화와의 융합이 특징입니다.
    """
    uk_reggae = GenreNode(
        "uk_reggae",
        2,
        GenreCharacteristics(
            tempo_range=(75, 110),
            common_keys=["A minor", "E minor", "C major", "D minor"],
            typical_instruments=["uk_production", "british_vocals", "local_influences"],
            mood_descriptors=["british", "conscious", "multicultural", "urban"],
            rhythm_patterns=["uk_reggae_style", "british_groove", "multicultural_rhythm"],
            cultural_context="영국"
        )
    )
    
    # 2-톤 스카 - 스카와 레게의 융합
    uk_reggae.add_child(GenreNode(
        "two_tone_ska", 3,
        GenreCharacteristics(
            tempo_range=(120, 160),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["ska_guitar", "brass_section", "upbeat_rhythm"],
            mood_descriptors=["energetic", "upbeat", "ska_influenced", "youthful"],
            rhythm_patterns=["ska_upstroke", "two_tone_rhythm", "energetic_ska"]
        )
    ))
    
    # 정글/드럼 앤 베이스 레게 - 전자음악과 융합
    uk_reggae.add_child(GenreNode(
        "jungle_reggae", 3,
        GenreCharacteristics(
            tempo_range=(160, 180),
            common_keys=["A minor", "E minor", "C minor"],
            typical_instruments=["breakbeats", "jungle_bass", "ragga_vocals"],
            mood_descriptors=["electronic", "fast", "jungle_influenced", "urban"],
            rhythm_patterns=["jungle_breaks", "ragga_jungle", "electronic_reggae"]
        )
    ))
    
    # UK 덥 - 영국식 덥
    uk_reggae.add_child(GenreNode(
        "uk_dub", 3,
        GenreCharacteristics(
            tempo_range=(70, 100),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["british_production", "uk_effects", "experimental_sounds"],
            mood_descriptors=["experimental", "british", "atmospheric", "innovative"],
            rhythm_patterns=["uk_dub_style", "british_experimental", "innovative_dub"]
        )
    ))
    
    return uk_reggae


def create_reggae_hierarchy() -> GenreNode:
    """
    레게 메인 계층 생성
    """
    reggae = GenreNode(
        "reggae",
        1,
        GenreCharacteristics(
            tempo_range=(60, 180),
            common_keys=["A minor", "E minor", "C major", "G major"],
            typical_instruments=["bass_guitar", "drums", "rhythm_guitar", "keyboards"],
            mood_descriptors=["rhythmic", "conscious", "spiritual", "groovy"],
            rhythm_patterns=["reggae_skank", "offbeat_emphasis", "bass_prominence"],
            cultural_context="자메이카"
        )
    )
    
    # 서브 장르들 추가
    reggae.add_child(create_roots_reggae_hierarchy())
    reggae.add_child(create_dancehall_hierarchy())
    reggae.add_child(create_dub_hierarchy())
    reggae.add_child(create_lovers_rock_hierarchy())
    reggae.add_child(create_reggaeton_hierarchy())
    reggae.add_child(create_uk_reggae_hierarchy())
    
    return reggae 