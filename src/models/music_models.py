"""
AI 작곡 시스템 음악 모델 클래스들
"""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime
import json

@dataclass
class Artist:
    """아티스트 모델"""
    id: Optional[int] = None
    name: str = ""
    description: str = ""
    created_at: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

@dataclass
class Genre:
    """장르 모델"""
    id: Optional[int] = None
    name: str = ""
    description: str = ""
    created_at: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

@dataclass
class Track:
    """개별 트랙 모델"""
    id: Optional[int] = None
    song_id: Optional[int] = None
    name: str = ""
    instrument: str = ""
    midi_channel: Optional[int] = None
    audio_file_path: Optional[str] = None
    volume: float = 1.0
    pan: float = 0.0
    muted: bool = False
    soloed: bool = False
    track_order: int = 0
    created_at: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'song_id': self.song_id,
            'name': self.name,
            'instrument': self.instrument,
            'midi_channel': self.midi_channel,
            'audio_file_path': self.audio_file_path,
            'volume': self.volume,
            'pan': self.pan,
            'muted': self.muted,
            'soloed': self.soloed,
            'track_order': self.track_order,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

@dataclass
class Song:
    """곡 모델"""
    id: Optional[int] = None
    title: str = ""
    artist: Optional[Artist] = None
    genre: Optional[Genre] = None
    bpm: int = 120
    key_signature: str = "C"
    time_signature: str = "4/4"
    duration: Optional[float] = None
    midi_data: Optional[str] = None
    audio_file_path: Optional[str] = None
    project_file_path: Optional[str] = None
    lyrics: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    tracks: List[Track] = field(default_factory=list)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def add_track(self, track: Track):
        """트랙 추가"""
        track.song_id = self.id
        self.tracks.append(track)
    
    def remove_track(self, track_id: int):
        """트랙 제거"""
        self.tracks = [t for t in self.tracks if t.id != track_id]
    
    def get_track(self, track_id: int) -> Optional[Track]:
        """특정 트랙 조회"""
        return next((t for t in self.tracks if t.id == track_id), None)
    
    def get_tracks_by_instrument(self, instrument: str) -> List[Track]:
        """악기별 트랙 조회"""
        return [t for t in self.tracks if t.instrument == instrument]
    
    def set_metadata(self, key: str, value: Any):
        """메타데이터 설정"""
        self.metadata[key] = value
    
    def get_metadata(self, key: str, default=None):
        """메타데이터 조회"""
        return self.metadata.get(key, default)
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환"""
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist.to_dict() if self.artist else None,
            'genre': self.genre.to_dict() if self.genre else None,
            'bpm': self.bpm,
            'key_signature': self.key_signature,
            'time_signature': self.time_signature,
            'duration': self.duration,
            'midi_data': self.midi_data,
            'audio_file_path': self.audio_file_path,
            'project_file_path': self.project_file_path,
            'lyrics': self.lyrics,
            'metadata': self.metadata,
            'tracks': [track.to_dict() for track in self.tracks],
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Song':
        """딕셔너리에서 Song 객체 생성"""
        # Artist 처리
        artist = None
        if data.get('artist'):
            artist_data = data['artist']
            artist = Artist(
                id=artist_data.get('id'),
                name=artist_data.get('name', ''),
                description=artist_data.get('description', ''),
                created_at=datetime.fromisoformat(artist_data['created_at']) if artist_data.get('created_at') else None
            )
        
        # Genre 처리
        genre = None
        if data.get('genre'):
            genre_data = data['genre']
            genre = Genre(
                id=genre_data.get('id'),
                name=genre_data.get('name', ''),
                description=genre_data.get('description', ''),
                created_at=datetime.fromisoformat(genre_data['created_at']) if genre_data.get('created_at') else None
            )
        
        # Tracks 처리
        tracks = []
        if data.get('tracks'):
            for track_data in data['tracks']:
                track = Track(
                    id=track_data.get('id'),
                    song_id=track_data.get('song_id'),
                    name=track_data.get('name', ''),
                    instrument=track_data.get('instrument', ''),
                    midi_channel=track_data.get('midi_channel'),
                    audio_file_path=track_data.get('audio_file_path'),
                    volume=track_data.get('volume', 1.0),
                    pan=track_data.get('pan', 0.0),
                    muted=track_data.get('muted', False),
                    soloed=track_data.get('soloed', False),
                    track_order=track_data.get('track_order', 0),
                    created_at=datetime.fromisoformat(track_data['created_at']) if track_data.get('created_at') else None
                )
                tracks.append(track)
        
        return cls(
            id=data.get('id'),
            title=data.get('title', ''),
            artist=artist,
            genre=genre,
            bpm=data.get('bpm', 120),
            key_signature=data.get('key_signature', 'C'),
            time_signature=data.get('time_signature', '4/4'),
            duration=data.get('duration'),
            midi_data=data.get('midi_data'),
            audio_file_path=data.get('audio_file_path'),
            project_file_path=data.get('project_file_path'),
            lyrics=data.get('lyrics', ''),
            metadata=data.get('metadata', {}),
            tracks=tracks,
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else None,
            updated_at=datetime.fromisoformat(data['updated_at']) if data.get('updated_at') else None
        )
    
    def get_export_info(self) -> Dict[str, Any]:
        """내보내기용 정보 반환"""
        return {
            'title': self.title,
            'artist': self.artist.name if self.artist else 'Unknown',
            'genre': self.genre.name if self.genre else 'Unknown',
            'bpm': self.bpm,
            'key': self.key_signature,
            'time_signature': self.time_signature,
            'duration': self.duration,
            'track_count': len(self.tracks),
            'tracks': [
                {
                    'name': track.name,
                    'instrument': track.instrument,
                    'channel': track.midi_channel
                }
                for track in self.tracks
            ]
        } 