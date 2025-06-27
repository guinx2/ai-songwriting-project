"""
AI 작곡 시스템 데이터베이스 연결 및 관리
"""
import os
import sqlite3
from pathlib import Path
from typing import Optional, List, Dict, Any
import json
from datetime import datetime

class Database:
    """SQLite 데이터베이스 관리 클래스"""
    
    def __init__(self, db_path: Optional[str] = None):
        """
        데이터베이스 초기화
        
        Args:
            db_path: 데이터베이스 파일 경로 (기본: data/songs.db)
        """
        if db_path is None:
            # 프로젝트 루트의 data 디렉토리에 DB 파일 생성
            project_root = Path(__file__).parent.parent.parent
            db_dir = project_root / "data"
            db_dir.mkdir(exist_ok=True)
            db_path = str(db_dir / "songs.db")
        
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
        self._create_tables()
    
    def connect(self) -> sqlite3.Connection:
        """데이터베이스 연결"""
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Row 객체로 반환
        return self.connection
    
    def disconnect(self):
        """데이터베이스 연결 해제"""
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def _create_tables(self):
        """테이블 생성"""
        conn = self.connect()
        cursor = conn.cursor()
        
        # Artists 테이블
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Genres 테이블
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Songs 테이블
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist_id INTEGER,
            genre_id INTEGER,
            bpm INTEGER DEFAULT 120,
            key_signature TEXT DEFAULT 'C',
            time_signature TEXT DEFAULT '4/4',
            duration REAL,
            midi_data TEXT,
            audio_file_path TEXT,
            project_file_path TEXT,
            lyrics TEXT,
            metadata TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (artist_id) REFERENCES artists (id),
            FOREIGN KEY (genre_id) REFERENCES genres (id)
        )
        ''')
        
        # Tracks 테이블 (곡 내의 개별 트랙)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            instrument TEXT,
            midi_channel INTEGER,
            audio_file_path TEXT,
            volume REAL DEFAULT 1.0,
            pan REAL DEFAULT 0.0,
            muted BOOLEAN DEFAULT FALSE,
            soloed BOOLEAN DEFAULT FALSE,
            track_order INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (song_id) REFERENCES songs (id) ON DELETE CASCADE
        )
        ''')
        
        # 인덱스 생성
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_songs_artist ON songs(artist_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_songs_genre ON songs(genre_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_tracks_song ON tracks(song_id)')
        
        conn.commit()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[sqlite3.Row]:
        """SELECT 쿼리 실행"""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """INSERT/UPDATE/DELETE 쿼리 실행"""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid if cursor.lastrowid else cursor.rowcount
    
    def get_song_by_id(self, song_id: int) -> Optional[Dict[str, Any]]:
        """ID로 song 조회"""
        query = '''
        SELECT s.*, a.name as artist_name, g.name as genre_name 
        FROM songs s
        LEFT JOIN artists a ON s.artist_id = a.id
        LEFT JOIN genres g ON s.genre_id = g.id
        WHERE s.id = ?
        '''
        result = self.execute_query(query, (song_id,))
        return dict(result[0]) if result else None
    
    def get_tracks_by_song_id(self, song_id: int) -> List[Dict[str, Any]]:
        """Song ID로 해당하는 모든 트랙 조회"""
        query = '''
        SELECT * FROM tracks 
        WHERE song_id = ? 
        ORDER BY track_order, id
        '''
        results = self.execute_query(query, (song_id,))
        return [dict(row) for row in results]
    
    def create_song(self, title: str, artist_name: str = None, genre_name: str = None, **kwargs) -> int:
        """새 song 생성"""
        artist_id = None
        genre_id = None
        
        # Artist 처리
        if artist_name:
            artist_id = self.get_or_create_artist(artist_name)
        
        # Genre 처리
        if genre_name:
            genre_id = self.get_or_create_genre(genre_name)
        
        # Song 생성
        query = '''
        INSERT INTO songs (title, artist_id, genre_id, bpm, key_signature, 
                          time_signature, duration, midi_data, audio_file_path,
                          project_file_path, lyrics, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        
        params = (
            title,
            artist_id,
            genre_id,
            kwargs.get('bpm', 120),
            kwargs.get('key_signature', 'C'),
            kwargs.get('time_signature', '4/4'),
            kwargs.get('duration'),
            kwargs.get('midi_data'),
            kwargs.get('audio_file_path'),
            kwargs.get('project_file_path'),
            kwargs.get('lyrics'),
            json.dumps(kwargs.get('metadata', {}))
        )
        
        return self.execute_update(query, params)
    
    def get_or_create_artist(self, name: str) -> int:
        """Artist 조회 또는 생성"""
        # 먼저 존재하는지 확인
        result = self.execute_query("SELECT id FROM artists WHERE name = ?", (name,))
        if result:
            return result[0]['id']
        
        # 없으면 생성
        return self.execute_update("INSERT INTO artists (name) VALUES (?)", (name,))
    
    def get_or_create_genre(self, name: str) -> int:
        """Genre 조회 또는 생성"""
        # 먼저 존재하는지 확인
        result = self.execute_query("SELECT id FROM genres WHERE name = ?", (name,))
        if result:
            return result[0]['id']
        
        # 없으면 생성
        return self.execute_update("INSERT INTO genres (name) VALUES (?)", (name,))
    
    def add_track_to_song(self, song_id: int, name: str, **kwargs) -> int:
        """Song에 트랙 추가"""
        query = '''
        INSERT INTO tracks (song_id, name, instrument, midi_channel, 
                           audio_file_path, volume, pan, muted, soloed, track_order)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        
        params = (
            song_id,
            name,
            kwargs.get('instrument'),
            kwargs.get('midi_channel'),
            kwargs.get('audio_file_path'),
            kwargs.get('volume', 1.0),
            kwargs.get('pan', 0.0),
            kwargs.get('muted', False),
            kwargs.get('soloed', False),
            kwargs.get('track_order', 0)
        )
        
        return self.execute_update(query, params)
    
    def update_song(self, song_id: int, **kwargs):
        """Song 업데이트"""
        # 업데이트할 필드들 동적 생성
        fields = []
        values = []
        
        for key, value in kwargs.items():
            if key in ['title', 'bpm', 'key_signature', 'time_signature', 
                      'duration', 'midi_data', 'audio_file_path', 
                      'project_file_path', 'lyrics']:
                fields.append(f"{key} = ?")
                values.append(value)
            elif key == 'metadata':
                fields.append("metadata = ?")
                values.append(json.dumps(value))
        
        if not fields:
            return
        
        # updated_at 추가
        fields.append("updated_at = CURRENT_TIMESTAMP")
        values.append(song_id)
        
        query = f"UPDATE songs SET {', '.join(fields)} WHERE id = ?"
        self.execute_update(query, tuple(values))
    
    def delete_song(self, song_id: int):
        """Song 삭제 (트랙들도 함께 삭제됨 - CASCADE)"""
        self.execute_update("DELETE FROM songs WHERE id = ?", (song_id,))
    
    def get_all_songs(self, limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
        """모든 song 조회"""
        query = '''
        SELECT s.*, a.name as artist_name, g.name as genre_name 
        FROM songs s
        LEFT JOIN artists a ON s.artist_id = a.id
        LEFT JOIN genres g ON s.genre_id = g.id
        ORDER BY s.created_at DESC
        LIMIT ? OFFSET ?
        '''
        results = self.execute_query(query, (limit, offset))
        return [dict(row) for row in results]
    
    def search_songs(self, search_term: str) -> List[Dict[str, Any]]:
        """곡 검색"""
        query = '''
        SELECT s.*, a.name as artist_name, g.name as genre_name 
        FROM songs s
        LEFT JOIN artists a ON s.artist_id = a.id
        LEFT JOIN genres g ON s.genre_id = g.id
        WHERE s.title LIKE ? OR a.name LIKE ? OR g.name LIKE ?
        ORDER BY s.created_at DESC
        '''
        search_pattern = f"%{search_term}%"
        results = self.execute_query(query, (search_pattern, search_pattern, search_pattern))
        return [dict(row) for row in results]

# 데이터베이스 인스턴스 (싱글톤 패턴)
_db_instance = None

def get_database() -> Database:
    """데이터베이스 인스턴스 반환"""
    global _db_instance
    if _db_instance is None:
        _db_instance = Database()
    return _db_instance 