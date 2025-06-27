"""
힙합 (Hip-Hop) 장르 계층 정의

힙합은 1970년대 뉴욕 브롱크스에서 시작된 음악 장르로, 리듬감 있는 말하기(랩)와 
강한 비트를 특징으로 합니다. 현재는 전 세계적으로 가장 인기 있는 음악 장르 중 하나입니다.

세부 장르:
- 트랩 (Trap): 현대 힙합의 주류, 808 드럼과 하이햇 롤이 특징
- 붐뱁 (Boom Bap): 전통적인 힙합 스타일, 재즈 샘플링과 강한 스네어
- 드릴 (Drill): 어둡고 공격적인 스타일, 영국과 시카고에서 발전
- 로파이 힙합 (Lo-fi Hip Hop): 편안하고 차분한 스타일, 공부용 음악으로 인기
- 트릴 (Trill): 남부 힙합 스타일, 트랩과 크런크의 융합
- 클라우드 랩 (Cloud Rap): 몽환적이고 대기적인 사운드
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_trap_hierarchy() -> GenreNode:
    """
    트랩 (Trap) - 현대 힙합의 주류 장르
    
    2000년대 초 미국 남부에서 시작된 힙합 서브 장르로, 808 드럼머신의 강한 베이스와
    빠른 하이햇 롤, 스네어 클랩이 특징입니다. 현재 메인스트림 힙합의 주류를 이루고 있습니다.
    """
    trap = GenreNode(
        "trap",
        2,
        GenreCharacteristics(
            tempo_range=(120, 160),
            common_keys=["C minor", "F minor", "G minor", "Bb minor"],
            typical_instruments=["808_drums", "synth_lead", "vocals", "hi_hats"],
            mood_descriptors=["aggressive", "modern", "energetic", "urban"],
            rhythm_patterns=["hi_hat_rolls", "808_kicks", "snare_claps"],
            cultural_context="미국 남부"
        )
    )
    
    # 멜로딕 트랩 - 감성적이고 멜로디가 강조된 트랩
    trap.add_child(GenreNode(
        "melodic_trap", 3,
        GenreCharacteristics(
            tempo_range=(120, 150),
            common_keys=["C minor", "A minor", "F minor"],
            typical_instruments=["synth_lead", "piano", "vocals", "melodic_bass"],
            mood_descriptors=["melodic", "emotional", "modern", "atmospheric"],
            rhythm_patterns=["melodic_hi_hats", "emotional_808s", "smooth_transitions"]
        )
    ))
    
    # 하드 트랩 - 공격적이고 강한 트랩
    trap.add_child(GenreNode(
        "hard_trap", 3,
        GenreCharacteristics(
            tempo_range=(140, 160),
            common_keys=["C minor", "F minor", "G minor"],
            typical_instruments=["heavy_808", "distorted_synths", "aggressive_vocals"],
            mood_descriptors=["aggressive", "hard", "intense", "powerful"],
            rhythm_patterns=["heavy_808s", "hard_snares", "rapid_hi_hats"]
        )
    ))
    
    # 다크 트랩 - 어둡고 분위기 있는 트랩
    trap.add_child(GenreNode(
        "dark_trap", 3,
        GenreCharacteristics(
            tempo_range=(120, 140),
            common_keys=["A minor", "D minor", "F minor"],
            typical_instruments=["dark_synths", "deep_808", "atmospheric_pads"],
            mood_descriptors=["dark", "atmospheric", "mysterious", "moody"],
            rhythm_patterns=["dark_808s", "atmospheric_hi_hats", "eerie_sounds"]
        )
    ))
    
    # 라틴 트랩 - 라틴 음악과 융합된 트랩
    trap.add_child(GenreNode(
        "latin_trap", 3,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["A minor", "E minor", "B minor"],
            typical_instruments=["reggaeton_drums", "latin_percussion", "spanish_guitar"],
            mood_descriptors=["latin", "rhythmic", "passionate", "danceable"],
            rhythm_patterns=["reggaeton_beat", "latin_percussion", "dembow"],
            cultural_context="라틴 아메리카"
        )
    ))
    
    return trap


def create_boom_bap_hierarchy() -> GenreNode:
    """
    붐뱁 (Boom Bap) - 전통적인 힙합의 황금기 사운드
    
    1980년대 후반부터 1990년대 초반 힙합의 황금기를 대표하는 스타일로,
    재즈 샘플링과 강한 킥-스네어 패턴이 특징입니다. "붐뱁"이라는 이름은 
    킥(붐)과 스네어(뱁) 소리에서 유래되었습니다.
    """
    boom_bap = GenreNode(
        "boom_bap",
        2,
        GenreCharacteristics(
            tempo_range=(80, 110),
            common_keys=["A minor", "E minor", "G minor", "C minor"],
            typical_instruments=["sampled_drums", "jazz_samples", "piano", "vocals"],
            mood_descriptors=["nostalgic", "underground", "authentic", "raw"],
            rhythm_patterns=["boom_bap_drums", "jazz_samples", "vinyl_crackle"],
            cultural_context="뉴욕 힙합"
        )
    )
    
    # 올드스쿨 붐뱁 - 전통적인 90년대 스타일
    boom_bap.add_child(GenreNode(
        "old_school_boom_bap", 3,
        GenreCharacteristics(
            tempo_range=(85, 95),
            common_keys=["A minor", "E minor", "D minor"],
            typical_instruments=["vinyl_drums", "jazz_samples", "turntables"],
            mood_descriptors=["vintage", "authentic", "raw", "street"],
            rhythm_patterns=["classic_boom_bap", "vinyl_crackle", "scratch_sounds"]
        )
    ))
    
    # 모던 붐뱁 - 현대적으로 재해석된 붐뱁
    boom_bap.add_child(GenreNode(
        "modern_boom_bap", 3,
        GenreCharacteristics(
            tempo_range=(90, 110),
            common_keys=["G minor", "C minor", "F minor"],
            typical_instruments=["crisp_drums", "modern_bass", "clean_samples"],
            mood_descriptors=["modern", "crisp", "clean", "polished"],
            rhythm_patterns=["modern_boom_bap", "clean_samples", "tight_drums"]
        )
    ))
    
    # 재즈 붐뱁 - 재즈 요소가 강화된 붐뱁
    boom_bap.add_child(GenreNode(
        "jazz_boom_bap", 3,
        GenreCharacteristics(
            tempo_range=(80, 100),
            common_keys=["F major", "Bb major", "C major", "Eb major"],
            typical_instruments=["jazz_samples", "upright_bass", "piano", "horn_sections"],
            mood_descriptors=["sophisticated", "smooth", "jazzy", "intellectual"],
            rhythm_patterns=["jazz_influenced", "swing_feel", "complex_samples"]
        )
    ))
    
    return boom_bap


def create_drill_hierarchy() -> GenreNode:
    """
    드릴 (Drill) - 어둡고 공격적인 현대 힙합 스타일
    
    2010년대 초 시카고에서 시작되어 영국 런던으로 전파된 힙합 서브 장르입니다.
    어둡고 미니멀한 비트, 슬라이딩하는 808 베이스, 공격적인 가사가 특징입니다.
    """
    drill = GenreNode(
        "drill",
        2,
        GenreCharacteristics(
            tempo_range=(130, 150),
            common_keys=["C minor", "F minor", "Bb minor", "G minor"],
            typical_instruments=["drill_drums", "dark_synths", "sliding_808", "vocals"],
            mood_descriptors=["aggressive", "dark", "street", "raw"],
            rhythm_patterns=["drill_hi_hats", "sliding_808s", "minimal_drums"]
        )
    )
    
    # UK 드릴 - 영국식 드릴
    drill.add_child(GenreNode(
        "uk_drill", 3,
        GenreCharacteristics(
            tempo_range=(130, 145),
            common_keys=["C minor", "F minor", "Ab minor"],
            typical_instruments=["uk_drill_drums", "dark_pads", "distorted_bass"],
            mood_descriptors=["dark", "aggressive", "london_street", "gritty"],
            rhythm_patterns=["uk_drill_pattern", "sliding_808s", "sparse_drums"],
            cultural_context="영국 런던"
        )
    ))
    
    # 시카고 드릴 - 원조 드릴 스타일
    drill.add_child(GenreNode(
        "chicago_drill", 3,
        GenreCharacteristics(
            tempo_range=(135, 150),
            common_keys=["C minor", "Bb minor", "F minor"],
            typical_instruments=["chicago_drill_drums", "heavy_808", "dark_synths"],
            mood_descriptors=["raw", "street", "chicago_sound", "hardcore"],
            rhythm_patterns=["chicago_drill_pattern", "heavy_kicks", "drill_snares"],
            cultural_context="미국 시카고"
        )
    ))
    
    # 뉴욕 드릴 - 뉴욕식 드릴
    drill.add_child(GenreNode(
        "ny_drill", 3,
        GenreCharacteristics(
            tempo_range=(140, 155),
            common_keys=["D minor", "G minor", "C minor"],
            typical_instruments=["ny_drill_drums", "sample_chops", "heavy_bass"],
            mood_descriptors=["energetic", "aggressive", "ny_street", "sample_heavy"],
            rhythm_patterns=["ny_drill_pattern", "sample_chops", "bounce_drums"],
            cultural_context="미국 뉴욕"
        )
    ))
    
    return drill


def create_lofi_hip_hop_hierarchy() -> GenreNode:
    """
    로파이 힙합 (Lo-fi Hip Hop) - 편안하고 차분한 힙합 스타일
    
    낮은 음질(Lo-fi)의 따뜻한 사운드와 반복적인 루프, 재즈 샘플링이 특징인 
    힙합 서브 장르입니다. 공부나 작업용 배경음악으로 매우 인기가 높습니다.
    """
    lofi_hip_hop = GenreNode(
        "lofi_hip_hop",
        2,
        GenreCharacteristics(
            tempo_range=(70, 90),
            common_keys=["C major", "A minor", "F major", "G major"],
            typical_instruments=["vinyl_drums", "jazz_samples", "electric_piano", "vinyl_crackle"],
            mood_descriptors=["relaxed", "nostalgic", "chill", "cozy"],
            rhythm_patterns=["lofi_drums", "vinyl_crackle", "off_beat_snares"]
        )
    )
    
    # 재즈 로파이 - 재즈 요소가 강한 로파이
    lofi_hip_hop.add_child(GenreNode(
        "jazz_lofi", 3,
        GenreCharacteristics(
            tempo_range=(70, 85),
            common_keys=["F major", "Bb major", "D minor", "C major"],
            typical_instruments=["jazz_piano", "upright_bass", "vinyl_drums", "horn_samples"],
            mood_descriptors=["sophisticated", "mellow", "jazzy", "warm"],
            rhythm_patterns=["jazz_lofi_groove", "swing_samples", "jazz_chords"]
        )
    ))
    
    # 비트 로파이 - 단순하고 반복적인 로파이
    lofi_hip_hop.add_child(GenreNode(
        "beats_lofi", 3,
        GenreCharacteristics(
            tempo_range=(75, 90),
            common_keys=["C major", "A minor", "F major"],
            typical_instruments=["simple_drums", "electric_piano", "soft_bass"],
            mood_descriptors=["study", "chill", "repetitive", "focus"],
            rhythm_patterns=["simple_lofi_beat", "study_rhythm", "minimal_drums"]
        )
    ))
    
    # 소울 로파이 - 소울/R&B 샘플이 들어간 로파이
    lofi_hip_hop.add_child(GenreNode(
        "soul_lofi", 3,
        GenreCharacteristics(
            tempo_range=(65, 80),
            common_keys=["Eb major", "Ab major", "F minor"],
            typical_instruments=["soul_samples", "warm_pads", "vinyl_drums"],
            mood_descriptors=["soulful", "warm", "emotional", "vintage"],
            rhythm_patterns=["soul_groove", "warm_samples", "emotional_chops"]
        )
    ))
    
    return lofi_hip_hop


def create_trill_hierarchy() -> GenreNode:
    """
    트릴 (Trill) - 남부 힙합의 진화된 형태
    
    "True"와 "Real"의 합성어로, 텍사스와 루이지애나를 중심으로 한 남부 힙합 스타일입니다.
    트랩과 크런크의 요소를 결합하여 더욱 공격적이고 에너지 넘치는 사운드를 만들어냅니다.
    """
    trill = GenreNode(
        "trill",
        2,
        GenreCharacteristics(
            tempo_range=(70, 120),
            common_keys=["C minor", "F minor", "Bb minor"],
            typical_instruments=["southern_drums", "heavy_bass", "synth_leads"],
            mood_descriptors=["southern", "aggressive", "authentic", "raw"],
            rhythm_patterns=["trill_drums", "southern_bounce", "heavy_kicks"],
            cultural_context="미국 남부"
        )
    )
    
    # 클래식 트릴 - 전통적인 남부 스타일
    trill.add_child(GenreNode(
        "classic_trill", 3,
        GenreCharacteristics(
            tempo_range=(70, 90),
            common_keys=["C minor", "F minor"],
            typical_instruments=["classic_southern_drums", "deep_bass"],
            mood_descriptors=["classic", "authentic", "southern_pride"],
            rhythm_patterns=["classic_southern_bounce", "deep_kicks"]
        )
    ))
    
    # 모던 트릴 - 현대적으로 발전된 트릴
    trill.add_child(GenreNode(
        "modern_trill", 3,
        GenreCharacteristics(
            tempo_range=(90, 120),
            common_keys=["G minor", "Bb minor"],
            typical_instruments=["modern_southern_drums", "trap_elements"],
            mood_descriptors=["modern", "evolved", "trap_influenced"],
            rhythm_patterns=["modern_southern_bounce", "trap_influenced"]
        )
    ))
    
    return trill


def create_cloud_rap_hierarchy() -> GenreNode:
    """
    클라우드 랩 (Cloud Rap) - 몽환적이고 대기적인 힙합 스타일
    
    2000년대 후반에 등장한 힙합 서브 장르로, 몽환적인 신스 사운드와 
    리버브가 많이 걸린 보컬, 느린 템포가 특징입니다. 인터넷을 통해 확산되었습니다.
    """
    cloud_rap = GenreNode(
        "cloud_rap",
        2,
        GenreCharacteristics(
            tempo_range=(60, 90),
            common_keys=["A minor", "E minor", "C major", "F major"],
            typical_instruments=["ethereal_synths", "reverb_vocals", "atmospheric_pads"],
            mood_descriptors=["dreamy", "atmospheric", "ethereal", "spacey"],
            rhythm_patterns=["floating_drums", "ethereal_sounds", "ambient_textures"]
        )
    )
    
    # 앰비언트 클라우드 랩 - 더욱 대기적인 스타일
    cloud_rap.add_child(GenreNode(
        "ambient_cloud_rap", 3,
        GenreCharacteristics(
            tempo_range=(60, 75),
            common_keys=["A minor", "C major"],
            typical_instruments=["ambient_pads", "field_recordings", "minimal_drums"],
            mood_descriptors=["ambient", "meditative", "spacey"],
            rhythm_patterns=["minimal_drums", "ambient_textures"]
        )
    ))
    
    # 트랩 클라우드 랩 - 트랩 요소가 가미된 클라우드 랩
    cloud_rap.add_child(GenreNode(
        "trap_cloud_rap", 3,
        GenreCharacteristics(
            tempo_range=(75, 90),
            common_keys=["E minor", "F major"],
            typical_instruments=["trap_drums", "ethereal_synths", "808s"],
            mood_descriptors=["dreamy", "modern", "trap_influenced"],
            rhythm_patterns=["trap_drums", "ethereal_hi_hats"]
        )
    ))
    
    return cloud_rap


def create_hip_hop_hierarchy() -> GenreNode:
    """힙합 메인 장르 계층 구조 생성"""
    
    # === 힙합 메인 장르 ===
    hip_hop = GenreNode(
        "hip_hop", 
        1,
        GenreCharacteristics(
            tempo_range=(60, 160),
            common_keys=["C minor", "A minor", "G minor", "F minor"],
            typical_instruments=["drums", "bass", "vocals", "samples"],
            mood_descriptors=["urban", "rhythmic", "confident", "expressive"],
            rhythm_patterns=["boom_bap", "trap", "drill", "lofi"],
            cultural_context="뉴욕 브롱크스"
        )
    )
    
    # 세부 장르들 추가
    hip_hop.add_child(create_trap_hierarchy())
    hip_hop.add_child(create_boom_bap_hierarchy())
    hip_hop.add_child(create_drill_hierarchy())
    hip_hop.add_child(create_lofi_hip_hop_hierarchy())
    hip_hop.add_child(create_trill_hierarchy())
    hip_hop.add_child(create_cloud_rap_hierarchy())
    
    return hip_hop 