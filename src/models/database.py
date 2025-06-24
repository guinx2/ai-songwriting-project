"""
AI 작곡 시스템 데이터베이스 설정
SQLAlchemy를 사용한 데이터베이스 연결 및 설정
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

# 데이터베이스 URL 설정 (개발 환경: SQLite, 운영 환경: PostgreSQL)
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "sqlite:///./data/ai_songwriting.db"  # 기본값: SQLite
)

# SQLAlchemy 엔진 설정
if DATABASE_URL.startswith("sqlite"):
    # SQLite용 설정
    engine = create_engine(
        DATABASE_URL, 
        connect_args={"check_same_thread": False},
        echo=True  # 개발 중 SQL 쿼리 로깅
    )
else:
    # PostgreSQL용 설정
    engine = create_engine(DATABASE_URL, echo=True)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성 (모든 모델이 상속받을 기본 클래스)
Base = declarative_base()

def get_db():
    """
    데이터베이스 세션을 생성하고 반환
    FastAPI의 의존성 주입에서 사용
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """
    모든 테이블을 생성
    애플리케이션 시작 시 실행
    """
    Base.metadata.create_all(bind=engine)

def drop_tables():
    """
    모든 테이블을 삭제 (개발/테스트용)
    """
    Base.metadata.drop_all(bind=engine) 