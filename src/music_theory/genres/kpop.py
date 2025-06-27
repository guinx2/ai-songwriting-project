"""
K-Pop (Korean Pop) 장르 계층 정의

K-Pop은 한국의 대중음악으로, 서구 팝 음악과 한국 전통 음악의 융합을 통해 
독창적인 사운드를 만들어냈습니다. 2010년대 이후 전 세계적으로 큰 인기를 얻으며 
한류의 중심이 되었습니다.

세부 장르:
- 아이돌 팝 (Idol Pop): 아이돌 그룹 중심의 메인스트림 K-pop
- K-힙합 (K-Hip Hop): 한국적 감성을 가진 힙합
- K-R&B: 한국적 감성의 R&B
- 트로트 (Trot): 한국 전통 대중가요의 현대적 재해석
- 시티팝 (City Pop): 한국식 시티팝, 일본 시티팝의 영향
- 인디 K-Pop: 독립적이고 실험적인 한국 팝
"""

from ..genre_system import GenreNode, GenreCharacteristics


def create_idol_pop_hierarchy() -> GenreNode:
    """
    아이돌 팝 (Idol Pop) - 메인스트림 K-Pop의 핵심
    
    한국 아이돌 그룹들이 주도하는 K-Pop의 메인스트림으로, 
    캐치한 멜로디, 화려한 퍼포먼스, 다양한 장르의 융합이 특징입니다.
    """
    idol_pop = GenreNode(
        "idol_pop",
        2,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["C major", "G major", "A minor", "F major"],
            typical_instruments=["synthesizers", "electronic_drums", "pop_vocals", "dance_beats"],
            mood_descriptors=["energetic", "catchy", "polished", "youthful"],
            rhythm_patterns=["kpop_beat", "dance_pop", "idol_rhythm"],
            cultural_context="한국 아이돌"
        )
    )
    
    # 보이그룹 스타일 - 남성 아이돌 그룹
    idol_pop.add_child(GenreNode(
        "boy_group_style", 3,
        GenreCharacteristics(
            tempo_range=(110, 140),
            common_keys=["A minor", "E minor", "C major"],
            typical_instruments=["powerful_synths", "electronic_beats", "rap_sections"],
            mood_descriptors=["powerful", "charismatic", "energetic", "masculine"],
            rhythm_patterns=["boy_group_beat", "powerful_rhythm", "charismatic_groove"]
        )
    ))
    
    # 걸그룹 스타일 - 여성 아이돌 그룹
    idol_pop.add_child(GenreNode(
        "girl_group_style", 3,
        GenreCharacteristics(
            tempo_range=(100, 130),
            common_keys=["C major", "F major", "G major"],
            typical_instruments=["bright_synths", "cute_vocals", "dance_production"],
            mood_descriptors=["cute", "bright", "charming", "elegant"],
            rhythm_patterns=["girl_group_beat", "cute_rhythm", "elegant_groove"]
        )
    ))
    
    # 4세대 아이돌 - 최신 세대 아이돌
    idol_pop.add_child(GenreNode(
        "4th_gen_idol", 3,
        GenreCharacteristics(
            tempo_range=(105, 145),
            common_keys=["A minor", "C major", "E minor"],
            typical_instruments=["modern_production", "trap_influence", "experimental_sounds"],
            mood_descriptors=["experimental", "modern", "diverse", "genre_bending"],
            rhythm_patterns=["4th_gen_beat", "experimental_kpop", "modern_idol_rhythm"]
        )
    ))
    
    return idol_pop


def create_khip_hop_hierarchy() -> GenreNode:
    """
    K-힙합 (K-Hip Hop) - 한국적 감성을 가진 힙합
    
    한국 특유의 언어적 특성과 문화적 배경을 바탕으로 한 힙합으로, 
    서구 힙합과는 다른 독특한 플로우와 감성이 특징입니다.
    """
    khip_hop = GenreNode(
        "khip_hop",
        2,
        GenreCharacteristics(
            tempo_range=(80, 140),
            common_keys=["A minor", "E minor", "C minor", "D minor"],
            typical_instruments=["korean_samples", "traditional_elements", "modern_beats"],
            mood_descriptors=["urban", "korean", "contemporary", "cultural"],
            rhythm_patterns=["korean_flow", "k_hip_hop_beat", "cultural_rhythm"],
            cultural_context="한국 힙합"
        )
    )
    
    # 올드스쿨 K-힙합 - 초기 한국 힙합
    khip_hop.add_child(GenreNode(
        "oldschool_khip_hop", 3,
        GenreCharacteristics(
            tempo_range=(85, 110),
            common_keys=["A minor", "E minor", "D minor"],
            typical_instruments=["classic_breaks", "korean_samples", "underground_production"],
            mood_descriptors=["underground", "authentic", "raw", "pioneering"],
            rhythm_patterns=["korean_oldschool", "underground_beat", "authentic_flow"]
        )
    ))
    
    # 트랩 K-힙합 - 트랩 영향의 한국 힙합
    khip_hop.add_child(GenreNode(
        "trap_khip_hop", 3,
        GenreCharacteristics(
            tempo_range=(120, 140),
            common_keys=["C minor", "F minor", "A minor"],
            typical_instruments=["trap_hi_hats", "808_drums", "korean_vocals"],
            mood_descriptors=["modern", "trap_influenced", "energetic", "contemporary"],
            rhythm_patterns=["korean_trap", "modern_khiphop", "trap_influenced_beat"]
        )
    ))
    
    # 인디 K-힙합 - 독립적인 한국 힙합
    khip_hop.add_child(GenreNode(
        "indie_khip_hop", 3,
        GenreCharacteristics(
            tempo_range=(90, 120),
            common_keys=["E minor", "A minor", "C major"],
            typical_instruments=["indie_production", "alternative_beats", "experimental_korean"],
            mood_descriptors=["independent", "artistic", "experimental", "alternative"],
            rhythm_patterns=["indie_korean_flow", "alternative_khiphop", "experimental_beat"]
        )
    ))
    
    return khip_hop


def create_krnb_hierarchy() -> GenreNode:
    """
    K-R&B - 한국적 감성의 R&B
    
    서구 R&B에 한국적 감성과 언어적 특성을 더한 장르로, 
    부드럽고 감성적인 멜로디와 한국어의 특성이 잘 드러납니다.
    """
    krnb = GenreNode(
        "krnb",
        2,
        GenreCharacteristics(
            tempo_range=(70, 120),
            common_keys=["C major", "A minor", "F major", "G major"],
            typical_instruments=["smooth_keyboards", "korean_vocals", "r&b_drums", "bass_guitar"],
            mood_descriptors=["smooth", "emotional", "korean_sensibility", "romantic"],
            rhythm_patterns=["korean_rnb_groove", "smooth_rhythm", "emotional_beat"],
            cultural_context="한국 R&B"
        )
    )
    
    # 네오 소울 K-R&B - 네오 소울 영향의 한국 R&B
    krnb.add_child(GenreNode(
        "neo_soul_krnb", 3,
        GenreCharacteristics(
            tempo_range=(70, 100),
            common_keys=["A minor", "F major", "C major"],
            typical_instruments=["neo_soul_keys", "organic_drums", "korean_soul_vocals"],
            mood_descriptors=["soulful", "organic", "sophisticated", "neo_soul"],
            rhythm_patterns=["korean_neo_soul", "organic_groove", "sophisticated_rhythm"]
        )
    ))
    
    # 얼터너티브 K-R&B - 실험적인 한국 R&B
    krnb.add_child(GenreNode(
        "alternative_krnb", 3,
        GenreCharacteristics(
            tempo_range=(80, 115),
            common_keys=["E minor", "A minor", "C major"],
            typical_instruments=["experimental_production", "alternative_rnb", "innovative_korean"],
            mood_descriptors=["experimental", "alternative", "innovative", "artistic"],
            rhythm_patterns=["alternative_korean_rnb", "experimental_groove", "innovative_rhythm"]
        )
    ))
    
    return krnb


def create_trot_hierarchy() -> GenreNode:
    """
    트로트 (Trot) - 한국 전통 대중가요의 현대적 재해석
    
    일제강점기부터 시작된 한국의 전통 대중가요로, 2020년대에 들어 
    젊은 세대들 사이에서 다시 인기를 얻으며 현대적으로 재해석되고 있습니다.
    """
    trot = GenreNode(
        "trot",
        2,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["C major", "G major", "F major", "D major"],
            typical_instruments=["accordion", "traditional_korean", "trot_rhythm", "korean_vocals"],
            mood_descriptors=["traditional", "nostalgic", "korean", "emotional"],
            rhythm_patterns=["trot_rhythm", "traditional_korean_beat", "nostalgic_groove"],
            cultural_context="한국 전통"
        )
    )
    
    # 클래식 트로트 - 전통적인 트로트
    trot.add_child(GenreNode(
        "classic_trot", 3,
        GenreCharacteristics(
            tempo_range=(110, 130),
            common_keys=["C major", "G major", "F major"],
            typical_instruments=["traditional_instrumentation", "classic_trot_vocals", "nostalgic_production"],
            mood_descriptors=["traditional", "nostalgic", "authentic", "classic"],
            rhythm_patterns=["classic_trot_rhythm", "traditional_beat", "nostalgic_pattern"]
        )
    ))
    
    # 뉴트로트 - 현대적으로 재해석된 트로트
    trot.add_child(GenreNode(
        "new_trot", 3,
        GenreCharacteristics(
            tempo_range=(105, 140),
            common_keys=["G major", "C major", "A minor"],
            typical_instruments=["modern_production", "contemporary_arrangement", "youthful_vocals"],
            mood_descriptors=["modern", "youthful", "trendy", "contemporary"],
            rhythm_patterns=["new_trot_rhythm", "modern_beat", "contemporary_pattern"]
        )
    ))
    
    return trot


def create_city_pop_hierarchy() -> GenreNode:
    """
    시티팝 (City Pop) - 한국식 시티팝
    
    일본 시티팝의 영향을 받아 한국적으로 재해석된 장르로, 
    도시적이고 세련된 사운드와 그루브가 특징입니다.
    """
    city_pop = GenreNode(
        "city_pop",
        2,
        GenreCharacteristics(
            tempo_range=(90, 120),
            common_keys=["C major", "F major", "G major", "A minor"],
            typical_instruments=["electric_piano", "smooth_bass", "city_pop_drums", "jazzy_guitar"],
            mood_descriptors=["sophisticated", "urban", "smooth", "nostalgic"],
            rhythm_patterns=["city_pop_groove", "urban_rhythm", "sophisticated_beat"],
            cultural_context="도시적"
        )
    )
    
    # 레트로 시티팝 - 복고적인 시티팝
    city_pop.add_child(GenreNode(
        "retro_city_pop", 3,
        GenreCharacteristics(
            tempo_range=(85, 110),
            common_keys=["F major", "C major", "A minor"],
            typical_instruments=["vintage_synths", "retro_production", "nostalgic_vocals"],
            mood_descriptors=["retro", "nostalgic", "vintage", "dreamy"],
            rhythm_patterns=["retro_groove", "vintage_rhythm", "nostalgic_beat"]
        )
    ))
    
    # 모던 시티팝 - 현대적인 시티팝
    city_pop.add_child(GenreNode(
        "modern_city_pop", 3,
        GenreCharacteristics(
            tempo_range=(95, 125),
            common_keys=["G major", "C major", "F major"],
            typical_instruments=["modern_production", "contemporary_instruments", "polished_vocals"],
            mood_descriptors=["modern", "polished", "contemporary", "sophisticated"],
            rhythm_patterns=["modern_city_groove", "contemporary_rhythm", "polished_beat"]
        )
    ))
    
    return city_pop


def create_indie_kpop_hierarchy() -> GenreNode:
    """
    인디 K-Pop - 독립적이고 실험적인 한국 팝
    
    메인스트림 K-Pop과는 다른 독립적이고 실험적인 한국 팝 음악으로, 
    창의적이고 개성적인 사운드가 특징입니다.
    """
    indie_kpop = GenreNode(
        "indie_kpop",
        2,
        GenreCharacteristics(
            tempo_range=(80, 140),
            common_keys=["A minor", "C major", "E minor", "G major"],
            typical_instruments=["indie_instruments", "alternative_production", "creative_vocals"],
            mood_descriptors=["independent", "creative", "alternative", "artistic"],
            rhythm_patterns=["indie_korean_rhythm", "alternative_beat", "creative_groove"],
            cultural_context="인디 씬"
        )
    )
    
    # 인디 락 K-Pop - 락 영향의 인디 한국 팝
    indie_kpop.add_child(GenreNode(
        "indie_rock_kpop", 3,
        GenreCharacteristics(
            tempo_range=(100, 140),
            common_keys=["E minor", "A minor", "G major"],
            typical_instruments=["indie_guitars", "rock_drums", "alternative_vocals"],
            mood_descriptors=["rock_influenced", "energetic", "alternative", "guitar_driven"],
            rhythm_patterns=["indie_rock_korean", "alternative_rock_beat", "guitar_driven_rhythm"]
        )
    ))
    
    # 인디 일렉트로닉 K-Pop - 전자음악 영향의 인디 한국 팝
    indie_kpop.add_child(GenreNode(
        "indie_electronic_kpop", 3,
        GenreCharacteristics(
            tempo_range=(90, 130),
            common_keys=["C major", "A minor", "F major"],
            typical_instruments=["electronic_production", "synthesizers", "experimental_sounds"],
            mood_descriptors=["electronic", "experimental", "atmospheric", "innovative"],
            rhythm_patterns=["indie_electronic_korean", "experimental_electronic", "atmospheric_beat"]
        )
    ))
    
    # 인디 포크 K-Pop - 포크 영향의 인디 한국 팝
    indie_kpop.add_child(GenreNode(
        "indie_folk_kpop", 3,
        GenreCharacteristics(
            tempo_range=(70, 110),
            common_keys=["G major", "C major", "A minor"],
            typical_instruments=["acoustic_guitar", "folk_instruments", "intimate_vocals"],
            mood_descriptors=["intimate", "folk_influenced", "organic", "storytelling"],
            rhythm_patterns=["indie_folk_korean", "acoustic_rhythm", "intimate_groove"]
        )
    ))
    
    return indie_kpop


def create_kpop_hierarchy() -> GenreNode:
    """
    K-Pop 메인 계층 생성
    """
    kpop = GenreNode(
        "kpop",
        1,
        GenreCharacteristics(
            tempo_range=(70, 145),
            common_keys=["C major", "G major", "A minor", "F major"],
            typical_instruments=["synthesizers", "electronic_drums", "korean_vocals", "modern_production"],
            mood_descriptors=["energetic", "polished", "catchy", "korean"],
            rhythm_patterns=["kpop_rhythm", "korean_pop_beat", "hallyu_groove"],
            cultural_context="한국"
        )
    )
    
    # 서브 장르들 추가
    kpop.add_child(create_idol_pop_hierarchy())
    kpop.add_child(create_khip_hop_hierarchy())
    kpop.add_child(create_krnb_hierarchy())
    kpop.add_child(create_trot_hierarchy())
    kpop.add_child(create_city_pop_hierarchy())
    kpop.add_child(create_indie_kpop_hierarchy())
    
    return kpop 