"""
AI 작곡 시스템 데이터베이스 모델 정의
사용자, 작곡, 트랙, MIDI 파일, Ableton Live 프로젝트 등의 모델을 포함
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    """사용자 모델"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    # 관계 설정
    compositions = relationship("Composition", back_populates="user", cascade="all, delete-orphan")


class Composition(Base):
    """작곡 작품 모델"""
    __tablename__ = "compositions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    genre = Column(String(50), nullable=False)  # Rock, Hip-hop, Jpop, Jazz, Classical, Pop
    tempo = Column(Integer, default=120)  # BPM
    key_signature = Column(String(10), default="C")  # C, Am, G, etc.
    time_signature = Column(String(10), default="4/4")  # 4/4, 3/4, etc.
    duration = Column(Float)  # 곡 길이 (초)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_public = Column(Boolean, default=False)
    status = Column(String(20), default="draft")  # draft, completed, published
    
    # 관계 설정
    user = relationship("User", back_populates="compositions")
    tracks = relationship("Track", back_populates="composition", cascade="all, delete-orphan")
    midi_files = relationship("MidiFile", back_populates="composition", cascade="all, delete-orphan")
    ableton_project = relationship("AbletonProject", back_populates="composition", uselist=False, cascade="all, delete-orphan")
    generation_params = relationship("GenerationParams", back_populates="composition", cascade="all, delete-orphan")


class Track(Base):
    """개별 트랙 모델 (악기별 트랙)"""
    __tablename__ = "tracks"
    
    id = Column(Integer, primary_key=True, index=True)
    composition_id = Column(Integer, ForeignKey("compositions.id"), nullable=False)
    track_name = Column(String(100), nullable=False)
    instrument_type = Column(String(50), nullable=False)  # drums, bass, melody, harmony, lead, pad
    instrument_name = Column(String(100))  # Piano, Guitar, Violin, etc.
    midi_channel = Column(Integer, default=1)
    volume = Column(Float, default=0.8)  # 0.0 ~ 1.0
    pan = Column(Float, default=0.0)  # -1.0 ~ 1.0 (Left ~ Right)
    is_muted = Column(Boolean, default=False)
    track_order = Column(Integer, default=0)  # 트랙 순서
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # MIDI 데이터 (JSON 형태로 저장)
    midi_data = Column(JSON)  # Music21 또는 MIDI 이벤트 데이터
    
    # 관계 설정
    composition = relationship("Composition", back_populates="tracks")


class MidiFile(Base):
    """MIDI 파일 저장 모델"""
    __tablename__ = "midi_files"
    
    id = Column(Integer, primary_key=True, index=True)
    composition_id = Column(Integer, ForeignKey("compositions.id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_size = Column(Integer)  # bytes
    file_type = Column(String(20), default="midi")  # midi, mid
    track_count = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # 관계 설정
    composition = relationship("Composition", back_populates="midi_files")


class AbletonProject(Base):
    """Ableton Live 프로젝트 파일 모델"""
    __tablename__ = "ableton_projects"
    
    id = Column(Integer, primary_key=True, index=True)
    composition_id = Column(Integer, ForeignKey("compositions.id"), nullable=False)
    als_file_name = Column(String(255), nullable=False)
    als_file_path = Column(String(500), nullable=False)
    als_file_size = Column(Integer)  # bytes
    ableton_version = Column(String(20))  # Live 11, Live 12, etc.
    project_settings = Column(JSON)  # Ableton Live 프로젝트 설정
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계 설정
    composition = relationship("Composition", back_populates="ableton_project")


class GenerationParams(Base):
    """AI 음악 생성 파라미터 모델"""
    __tablename__ = "generation_params"
    
    id = Column(Integer, primary_key=True, index=True)
    composition_id = Column(Integer, ForeignKey("compositions.id"), nullable=False)
    model_type = Column(String(50), nullable=False)  # LSTM, Transformer, etc.
    model_version = Column(String(20))
    
    # 생성 파라미터
    temperature = Column(Float, default=0.8)  # 창의성 수준
    sequence_length = Column(Integer, default=128)  # 시퀀스 길이
    genre_weight = Column(Float, default=1.0)  # 장르 가중치
    
    # 장르별 특성 가중치
    genre_params = Column(JSON)  # 장르별 세부 파라미터
    
    # 악기별 생성 파라미터
    track_specific_params = Column(JSON)  # 트랙별 세부 파라미터
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # 관계 설정
    composition = relationship("Composition", back_populates="generation_params") 