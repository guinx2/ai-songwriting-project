"""
3단계 장르 계층 시스템

메인 장르 → 세부 장르 → 스타일 변형의 3단계 구조로
음악 장르를 체계적으로 분류하고 관리합니다.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import json


@dataclass
class GenreCharacteristics:
    """장르의 특성 정보"""
    tempo_range: Tuple[int, int]  # BPM 범위
    common_keys: List[str]        # 주로 사용되는 조성
    typical_instruments: List[str] # 전형적인 악기
    mood_descriptors: List[str]   # 분위기 설명자
    rhythm_patterns: List[str]    # 리듬 패턴
    cultural_context: Optional[str] = None  # 문화적 맥락


class GenreNode:
    """장르 트리의 노드"""
    
    def __init__(
        self,
        name: str,
        level: int,
        characteristics: Optional[GenreCharacteristics] = None,
        parent: Optional['GenreNode'] = None
    ):
        self.name = name
        self.level = level  # 1=메인, 2=세부, 3=스타일
        self.characteristics = characteristics
        self.parent = parent
        self.children: List['GenreNode'] = []
        
    def add_child(self, child: 'GenreNode') -> None:
        """자식 노드 추가"""
        child.parent = self
        self.children.append(child)
        
    def get_path(self) -> str:
        """루트부터 현재 노드까지의 경로 반환"""
        if self.parent is None:
            return self.name
        return f"{self.parent.get_path()}/{self.name}"
        
    def find_child_by_name(self, name: str) -> Optional['GenreNode']:
        """이름으로 직접 자식 노드 찾기"""
        for child in self.children:
            if child.name == name:
                return child
        return None


class GenreHierarchy:
    """3단계 장르 계층 시스템"""
    
    def __init__(self):
        self.roots: Dict[str, GenreNode] = {}
        self._setup_default_hierarchy()
        
    def _setup_default_hierarchy(self) -> None:
        """모듈화된 장르 계층 구조를 import하고 등록"""
        from .genres.hip_hop import create_hip_hop_hierarchy
        from .genres.rock import create_rock_hierarchy
        from .genres.electronic import create_electronic_hierarchy
        from .genres.jazz import create_jazz_hierarchy
        from .genres.pop import create_pop_hierarchy
        
        # 각 장르 모듈에서 계층 구조 생성하고 등록
        self.roots["hip_hop"] = create_hip_hop_hierarchy()
        self.roots["rock"] = create_rock_hierarchy()
        self.roots["electronic"] = create_electronic_hierarchy()
        self.roots["jazz"] = create_jazz_hierarchy()
        self.roots["pop"] = create_pop_hierarchy()

        
    def get_genre_path(self, main_genre: str, sub_genre: str, style_variant: str) -> Optional[str]:
        """3단계 장르 경로 반환"""
        if main_genre not in self.roots:
            return None
            
        root = self.roots[main_genre]
        sub_node = root.find_child_by_name(sub_genre)
        if not sub_node:
            return None
            
        style_node = sub_node.find_child_by_name(style_variant)
        if not style_node:
            return None
            
        return style_node.get_path()
        
    def validate_genre_combination(self, main_genre: str, sub_genre: str, style_variant: str) -> bool:
        """장르 조합이 유효한지 확인"""
        return self.get_genre_path(main_genre, sub_genre, style_variant) is not None
        
    def get_genre_characteristics(self, main_genre: str, sub_genre: str, style_variant: str) -> Optional[GenreCharacteristics]:
        """장르의 특성 정보 반환"""
        path = self.get_genre_path(main_genre, sub_genre, style_variant)
        if not path:
            return None
            
        # 경로를 통해 노드 찾기
        parts = path.split("/")
        current = self.roots[parts[0]]
        
        for part in parts[1:]:
            current = current.find_child_by_name(part)
            if not current:
                return None
                
        return current.characteristics
        
    def get_all_styles_for_genre(self, main_genre: str, sub_genre: str) -> List[str]:
        """특정 세부 장르의 모든 스타일 변형 반환"""
        if main_genre not in self.roots:
            return []
            
        root = self.roots[main_genre]
        sub_node = root.find_child_by_name(sub_genre)
        if not sub_node:
            return []
            
        return [child.name for child in sub_node.children]
        
    def get_all_subgenres_for_main(self, main_genre: str) -> List[str]:
        """메인 장르의 모든 세부 장르 반환"""
        if main_genre not in self.roots:
            return []
            
        return [child.name for child in self.roots[main_genre].children]
        
    def get_all_main_genres(self) -> List[str]:
        """모든 메인 장르 반환"""
        return list(self.roots.keys())
        
    def search_genres_by_characteristics(
        self, 
        tempo_range: Optional[Tuple[int, int]] = None,
        mood: Optional[str] = None,
        instruments: Optional[List[str]] = None
    ) -> List[Tuple[str, str, str]]:
        """특성으로 장르 검색"""
        results = []
        
        for main_genre, root in self.roots.items():
            for sub_node in root.children:
                for style_node in sub_node.children:
                    characteristics = style_node.characteristics
                    if not characteristics:
                        continue
                        
                    # 템포 범위 확인
                    if tempo_range:
                        min_tempo, max_tempo = tempo_range
                        char_min, char_max = characteristics.tempo_range
                        if not (char_min <= max_tempo and char_max >= min_tempo):
                            continue
                    
                    # 분위기 확인
                    if mood and mood not in characteristics.mood_descriptors:
                        continue
                        
                    # 악기 확인
                    if instruments:
                        if not any(inst in characteristics.typical_instruments for inst in instruments):
                            continue
                    
                    results.append((main_genre, sub_node.name, style_node.name))
        
        return results


# 전역 인스턴스 및 유틸리티 함수
_genre_hierarchy = None

def get_genre_hierarchy() -> GenreHierarchy:
    """전역 장르 계층 인스턴스 반환 (싱글톤)"""
    global _genre_hierarchy
    if _genre_hierarchy is None:
        _genre_hierarchy = GenreHierarchy()
    return _genre_hierarchy


def validate_genre_path(genre_path: str) -> bool:
    """장르 경로 유효성 검사 (genre/sub_genre/style_variant 형식)"""
    parts = genre_path.split("/")
    if len(parts) != 3:
        return False
        
    main_genre, sub_genre, style_variant = parts
    hierarchy = get_genre_hierarchy()
    return hierarchy.validate_genre_combination(main_genre, sub_genre, style_variant)


def get_genre_recommendations(
    base_genre: str,
    base_sub_genre: str,
    similarity_criteria: str = "mood"
) -> List[Tuple[str, str, str]]:
    """유사한 장르 추천"""
    hierarchy = get_genre_hierarchy()
    base_characteristics = hierarchy.get_genre_characteristics(
        base_genre, base_sub_genre, 
        hierarchy.get_all_styles_for_genre(base_genre, base_sub_genre)[0]
    )
    
    if not base_characteristics:
        return []
    
    recommendations = []
    
    if similarity_criteria == "mood":
        # 비슷한 분위기의 장르 찾기
        for mood in base_characteristics.mood_descriptors:
            similar_genres = hierarchy.search_genres_by_characteristics(mood=mood)
            recommendations.extend(similar_genres)
    elif similarity_criteria == "tempo":
        # 비슷한 템포의 장르 찾기
        tempo_range = base_characteristics.tempo_range
        similar_genres = hierarchy.search_genres_by_characteristics(tempo_range=tempo_range)
        recommendations.extend(similar_genres)
    
    # 중복 제거하고 원본 제외
    unique_recommendations = list(set(recommendations))
    original = (base_genre, base_sub_genre)
    
    return [
        (main, sub, style) for main, sub, style in unique_recommendations
        if (main, sub) != original
    ][:5]  # 상위 5개만 반환
