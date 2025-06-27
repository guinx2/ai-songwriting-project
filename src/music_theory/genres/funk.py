"""
펑크 (Funk) 장르 계층 정의

펑크는 1960년대 중반 아프리카계 미국인 음악가들에 의해 시작된 음악 장르로, 
강한 리듬감과 그루브, 싱코페이션이 특징입니다. 베이스 라인과 드럼의 상호작용이 
음악의 핵심을 이루며, 댄스 음악의 기초가 되었습니다.

세부 장르:
- 클래식 펑크 (Classic Funk): 제임스 브라운과 조지 클린턴의 전통적인 펑크
- P-펑크 (P-Funk): 파라데리움 스타일의 사이키델릭 펑크
- 고-고 (Go-Go): 워싱턴 DC에서 발전한 펑크 변형
- 펑크 락 (Funk Rock): 펑크와 락의 융합
- 일렉트로 펑크 (Electro Funk): 전자음악과 펑크의 결합
- 네오 펑크 (Neo-Funk): 현대적으로 재해석된 펑크
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_classic_funk_hierarchy() -> GenreNode:
    """
    클래식 펑크 (Classic Funk) - 전통적인 펑크의 원형
    
    1960년대 후반 제임스 브라운에 의해 정립된 전통적인 펑크 스타일로, 
    강한 베이스 라인, 타이트한 드럼, 브라스 섹션이 특징입니다.
    """
    classic_funk = GenreNode(
        "classic_funk",
        2,
        GenreCharacteristics(
            tempo_range=(90, 120),
            common_keys=["E minor", "A minor", "G major", "C major"],
            typical_instruments=["funk_bass", "tight_drums", "brass_section", "funky_guitar"],
            mood_descriptors=["groovy", "tight", "rhythmic", "soulful"],
            rhythm_patterns=["funk_groove", "syncopated_bass", "tight_drums"],
            cultural_context="미국 아프리카계"
        )
    )
    
    # 제임스 브라운 스타일 - "펑크의 대부" 스타일
    classic_funk.add_child(GenreNode(
        "james_brown_funk", 3,
        GenreCharacteristics(
            tempo_range=(95, 115),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["driving_bass", "sharp_drums", "screaming_vocals"],
            mood_descriptors=["driving", "intense", "rhythmic", "powerful"],
            rhythm_patterns=["james_brown_groove", "tight_rhythm_section", "call_response"]
        )
    ))
    
    # 슬라이 앤 패밀리 스톤 스타일 - 사이키델릭 펑크
    classic_funk.add_child(GenreNode(
        "sly_family_funk", 3,
        GenreCharacteristics(
            tempo_range=(90, 110),
            common_keys=["G major", "C major", "F major"],
            typical_instruments=["psychedelic_guitar", "funky_keyboards", "group_vocals"],
            mood_descriptors=["psychedelic", "social", "experimental", "groovy"],
            rhythm_patterns=["sly_groove", "psychedelic_funk", "social_funk"]
        )
    ))
    
    # 어스 윈드 앤 파이어 스타일 - 디스코 펑크
    classic_funk.add_child(GenreNode(
        "earth_wind_fire_funk", 3,
        GenreCharacteristics(
            tempo_range=(100, 120),
            common_keys=["C major", "F major", "Bb major"],
            typical_instruments=["horn_section", "disco_strings", "smooth_vocals"],
            mood_descriptors=["uplifting", "sophisticated", "danceable", "spiritual"],
            rhythm_patterns=["disco_funk", "horn_arrangements", "smooth_groove"]
        )
    ))
    
    return classic_funk


def create_p_funk_hierarchy() -> GenreNode:
    """
    P-펑크 (P-Funk) - 파라데리움의 사이키델릭 펑크
    
    조지 클린턴이 이끈 파라데리움과 펑카델릭에 의해 개발된 스타일로, 
    사이키델릭한 사운드와 긴 잼 세션, 우주적 테마가 특징입니다.
    """
    p_funk = GenreNode(
        "p_funk",
        2,
        GenreCharacteristics(
            tempo_range=(85, 110),
            common_keys=["E minor", "A minor", "C major"],
            typical_instruments=["synthesizers", "talk_box", "heavy_bass", "spacey_effects"],
            mood_descriptors=["psychedelic", "spacey", "experimental", "freaky"],
            rhythm_patterns=["p_funk_groove", "space_funk", "long_jams"],
            cultural_context="우주적 펑크"
        )
    )
    
    # 펑카델릭 스타일 - 사이키델릭 중심
    p_funk.add_child(GenreNode(
        "funkadelic_style", 3,
        GenreCharacteristics(
            tempo_range=(80, 105),
            common_keys=["E minor", "A minor", "G minor"],
            typical_instruments=["distorted_guitar", "psychedelic_effects", "experimental_sounds"],
            mood_descriptors=["psychedelic", "experimental", "rock_influenced", "mind_bending"],
            rhythm_patterns=["psychedelic_funk", "experimental_jams", "mind_funk"]
        )
    ))
    
    # 파라데리움 스타일 - 더 리듬 중심
    p_funk.add_child(GenreNode(
        "parliament_style", 3,
        GenreCharacteristics(
            tempo_range=(90, 115),
            common_keys=["C major", "F major", "Bb major"],
            typical_instruments=["horn_section", "talk_box", "rhythm_guitar"],
            mood_descriptors=["rhythmic", "party", "danceable", "cosmic"],
            rhythm_patterns=["parliament_groove", "cosmic_funk", "party_rhythm"]
        )
    ))
    
    return p_funk


def create_go_go_hierarchy() -> GenreNode:
    """
    고-고 (Go-Go) - 워싱턴 DC의 독특한 펑크 변형
    
    1970년대 워싱턴 DC에서 발전한 펑크의 지역적 변형으로, 
    지속적인 비트와 콘가, 팀발레스의 사용이 특징입니다.
    """
    go_go = GenreNode(
        "go_go",
        2,
        GenreCharacteristics(
            tempo_range=(95, 125),
            common_keys=["E minor", "A minor", "D minor", "G minor"],
            typical_instruments=["congas", "timbales", "go_go_bass", "call_response_vocals"],
            mood_descriptors=["continuous", "participatory", "community", "rhythmic"],
            rhythm_patterns=["go_go_beat", "continuous_rhythm", "community_chants"],
            cultural_context="워싱턴 DC"
        )
    )
    
    # 클래식 고-고 - 전통적인 DC 고-고
    go_go.add_child(GenreNode(
        "classic_go_go", 3,
        GenreCharacteristics(
            tempo_range=(100, 120),
            common_keys=["E minor", "A minor", "D minor"],
            typical_instruments=["traditional_percussion", "go_go_bass", "dc_vocals"],
            mood_descriptors=["traditional", "community", "raw", "authentic"],
            rhythm_patterns=["classic_go_go", "dc_rhythm", "street_beat"]
        )
    ))
    
    # 모던 고-고 - 현대적 고-고
    go_go.add_child(GenreNode(
        "modern_go_go", 3,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["A minor", "D minor", "G minor"],
            typical_instruments=["modern_production", "electronic_elements", "updated_percussion"],
            mood_descriptors=["modern", "updated", "contemporary", "evolved"],
            rhythm_patterns=["modern_go_go", "contemporary_dc", "evolved_rhythm"]
        )
    ))
    
    return go_go


def create_funk_rock_hierarchy() -> GenreNode:
    """
    펑크 락 (Funk Rock) - 펑크와 락의 융합
    
    펑크의 그루브와 락의 에너지를 결합한 장르로, 
    강한 기타 리프와 펑키한 리듬이 공존합니다.
    """
    funk_rock = GenreNode(
        "funk_rock",
        2,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["E minor", "A minor", "G major", "D major"],
            typical_instruments=["funk_guitar", "rock_drums", "driving_bass", "powerful_vocals"],
            mood_descriptors=["energetic", "powerful", "groovy", "rock_driven"],
            rhythm_patterns=["funk_rock_groove", "guitar_funk", "rock_rhythm"],
            cultural_context="락-펑크 융합"
        )
    )
    
    # 레드 핫 칠리 페퍼스 스타일 - 얼터너티브 펑크 락
    funk_rock.add_child(GenreNode(
        "rhcp_style_funk_rock", 3,
        GenreCharacteristics(
            tempo_range=(110, 140),
            common_keys=["E minor", "A minor", "C major"],
            typical_instruments=["slap_bass", "alternative_guitar", "rap_rock_vocals"],
            mood_descriptors=["alternative", "energetic", "californian", "youthful"],
            rhythm_patterns=["slap_bass_funk", "alternative_rock", "rap_rock_fusion"]
        )
    ))
    
    # 프린스 스타일 - 미니애폴리스 사운드
    funk_rock.add_child(GenreNode(
        "prince_style_funk_rock", 3,
        GenreCharacteristics(
            tempo_range=(95, 125),
            common_keys=["A minor", "D minor", "E minor"],
            typical_instruments=["prince_guitar", "synthesizers", "drum_machine"],
            mood_descriptors=["sensual", "innovative", "pop_influenced", "artistic"],
            rhythm_patterns=["minneapolis_sound", "prince_groove", "innovative_funk"]
        )
    ))
    
    # 리빙 컬러 스타일 - 헤비 펑크 락
    funk_rock.add_child(GenreNode(
        "living_colour_funk_rock", 3,
        GenreCharacteristics(
            tempo_range=(115, 145),
            common_keys=["E minor", "G minor", "A minor"],
            typical_instruments=["heavy_guitar", "metal_drums", "funk_bass"],
            mood_descriptors=["heavy", "intense", "metal_influenced", "powerful"],
            rhythm_patterns=["heavy_funk", "metal_funk", "intense_groove"]
        )
    ))
    
    return funk_rock


def create_electro_funk_hierarchy() -> GenreNode:
    """
    일렉트로 펑크 (Electro Funk) - 전자음악과 펑크의 결합
    
    1980년대에 등장한 장르로, 드럼 머신과 신디사이저를 사용하여 
    펑크의 그루브를 전자적으로 재해석했습니다.
    """
    electro_funk = GenreNode(
        "electro_funk",
        2,
        GenreCharacteristics(
            tempo_range=(95, 130),
            common_keys=["C minor", "F minor", "A minor", "E minor"],
            typical_instruments=["drum_machine", "synthesizer_bass", "vocoder", "electronic_percussion"],
            mood_descriptors=["electronic", "futuristic", "robotic", "groovy"],
            rhythm_patterns=["electro_beat", "electronic_funk", "robot_rhythm"],
            cultural_context="전자 펑크"
        )
    )
    
    # 헤라비 - 독일 일렉트로 펑크
    electro_funk.add_child(GenreNode(
        "herbie_hancock_electro", 3,
        GenreCharacteristics(
            tempo_range=(100, 125),
            common_keys=["C minor", "A minor", "F minor"],
            typical_instruments=["fairlight_cmi", "vocoder", "electronic_drums"],
            mood_descriptors=["innovative", "jazzy", "electronic", "sophisticated"],
            rhythm_patterns=["rockit_style", "jazz_electro", "innovative_funk"]
        )
    ))
    
    # 아프리카 밤바타 스타일 - 힙합 일렉트로 펑크
    electro_funk.add_child(GenreNode(
        "afrika_bambaataa_electro", 3,
        GenreCharacteristics(
            tempo_range=(90, 115),
            common_keys=["E minor", "A minor", "C minor"],
            typical_instruments=["tr_808", "kraftwerk_samples", "rap_vocals"],
            mood_descriptors=["hip_hop", "street", "breakbeat", "urban"],
            rhythm_patterns=["planet_rock", "hip_hop_electro", "breakbeat_funk"]
        )
    ))
    
    return electro_funk


def create_neo_funk_hierarchy() -> GenreNode:
    """
    네오 펑크 (Neo-Funk) - 현대적으로 재해석된 펑크
    
    1990년대 이후 등장한 현대적 펑크로, 전통적인 펑크 요소에 
    현대적 프로덕션과 다양한 장르의 영향이 더해졌습니다.
    """
    neo_funk = GenreNode(
        "neo_funk",
        2,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["E minor", "A minor", "C major", "F major"],
            typical_instruments=["modern_bass", "contemporary_drums", "digital_effects", "neo_soul_vocals"],
            mood_descriptors=["modern", "sophisticated", "contemporary", "evolved"],
            rhythm_patterns=["neo_funk_groove", "modern_production", "contemporary_rhythm"],
            cultural_context="현대 펑크"
        )
    )
    
    # 네오 소울 펑크 - 소울과 결합된 현대 펑크
    neo_funk.add_child(GenreNode(
        "neo_soul_funk", 3,
        GenreCharacteristics(
            tempo_range=(85, 115),
            common_keys=["C major", "F major", "A minor"],
            typical_instruments=["neo_soul_keys", "organic_drums", "soulful_vocals"],
            mood_descriptors=["soulful", "organic", "sophisticated", "emotional"],
            rhythm_patterns=["neo_soul_groove", "organic_funk", "soulful_rhythm"]
        )
    ))
    
    # 일렉트로닉 네오 펑크 - 전자음악과 결합
    neo_funk.add_child(GenreNode(
        "electronic_neo_funk", 3,
        GenreCharacteristics(
            tempo_range=(95, 135),
            common_keys=["A minor", "E minor", "C minor"],
            typical_instruments=["electronic_bass", "digital_drums", "synthesized_elements"],
            mood_descriptors=["electronic", "futuristic", "digital", "contemporary"],
            rhythm_patterns=["electronic_funk", "digital_groove", "futuristic_rhythm"]
        )
    ))
    
    # 인디 펑크 - 독립적이고 실험적인 펑크
    neo_funk.add_child(GenreNode(
        "indie_funk", 3,
        GenreCharacteristics(
            tempo_range=(90, 125),
            common_keys=["E minor", "A minor", "G major"],
            typical_instruments=["indie_guitars", "vintage_bass", "creative_drums"],
            mood_descriptors=["independent", "creative", "experimental", "authentic"],
            rhythm_patterns=["indie_groove", "creative_funk", "experimental_rhythm"]
        )
    ))
    
    return neo_funk


def create_funk_hierarchy() -> GenreNode:
    """
    펑크 메인 계층 생성
    """
    funk = GenreNode(
        "funk",
        1,
        GenreCharacteristics(
            tempo_range=(80, 140),
            common_keys=["E minor", "A minor", "C major", "G major"],
            typical_instruments=["bass_guitar", "drums", "rhythm_guitar", "percussion"],
            mood_descriptors=["groovy", "rhythmic", "danceable", "soulful"],
            rhythm_patterns=["funk_groove", "syncopated_rhythm", "tight_pocket"],
            cultural_context="아프리카계 미국"
        )
    )
    
    # 서브 장르들 추가
    funk.add_child(create_classic_funk_hierarchy())
    funk.add_child(create_p_funk_hierarchy())
    funk.add_child(create_go_go_hierarchy())
    funk.add_child(create_funk_rock_hierarchy())
    funk.add_child(create_electro_funk_hierarchy())
    funk.add_child(create_neo_funk_hierarchy())
    
    return funk 