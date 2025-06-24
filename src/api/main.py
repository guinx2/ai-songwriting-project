"""
AI 작곡 시스템 FastAPI 메인 애플리케이션
음악 생성, MIDI 처리, Ableton Live 연동을 위한 RESTful API
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import os
from datetime import datetime

# 내부 모듈 import
from ..models.database import get_db, create_tables
from ..models.music_models import User, Composition, Track, MidiFile
from sqlalchemy import text

# Ableton Live 연동 추가
from ..ableton_integration import MidiConnection, AbletonLiveAPI, MaxForLiveDevice
from ..ableton_integration.max_for_live import MaxForLiveManager

# FastAPI 앱 생성
app = FastAPI(
    title="AI 작곡 시스템 API",
    description="락, 힙합, Jpop 등 다양한 장르의 AI 음악 생성 및 Ableton Live 연동 시스템",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc"  # ReDoc
)

# CORS 설정 (React 프론트엔드 연동)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 환경, 운영에서는 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 애플리케이션 시작 시 데이터베이스 테이블 생성
@app.on_event("startup")
async def startup_event():
    """애플리케이션 시작 시 실행"""
    create_tables()
    print("🎵 AI 작곡 시스템 API 서버가 시작되었습니다!")
    print(f"📊 데이터베이스 연결 완료")
    print(f"🌐 API 문서: http://localhost:8000/docs")

    # 전역 인스턴스
    global midi_connection, live_api, m4l_manager
    midi_connection = MidiConnection()
    live_api = AbletonLiveAPI(midi_connection)
    m4l_manager = MaxForLiveManager()

@app.on_event("shutdown")
async def shutdown_event():
    """애플리케이션 종료 시 실행"""
    print("🔌 AI 작곡 시스템 API 서버가 종료되었습니다.")

# 기본 라우트
@app.get("/")
async def root():
    """API 루트 엔드포인트"""
    return {
        "message": "🎵 AI 작곡 시스템 API에 오신 것을 환영합니다!",
        "version": "1.0.0",
        "documentation": "/docs",
        "features": [
            "다양한 장르 음악 생성 (Rock, Hip-hop, Jpop, Jazz, Classical, Pop)",
            "악기별 트랙 생성 (드럼, 베이스, 멜로디, 화성)",
            "MIDI 파일 생성 및 다운로드",
            "Ableton Live 프로젝트 파일 생성",
            "실시간 음악 생성 및 재생"
        ],
        "timestamp": datetime.utcnow().isoformat()
    }

# 헬스체크 엔드포인트
@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """시스템 상태 확인"""
    try:
        # 데이터베이스 연결 테스트
        db.execute(text("SELECT 1"))
        
        return {
            "status": "healthy",
            "database": "connected", 
            "timestamp": datetime.utcnow().isoformat(),
            "services": {
                "api": "running",
                "database": "connected",
                "ai_models": "ready"  # 나중에 AI 모델 로드 상태로 업데이트
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"서비스 상태 확인 실패: {str(e)}"
        )

# 기본 작곡 목록 조회
@app.get("/compositions")
async def get_compositions(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """작곡 목록 조회"""
    compositions = db.query(Composition).offset(skip).limit(limit).all()
    return {
        "compositions": compositions,
        "total": db.query(Composition).count(),
        "skip": skip,
        "limit": limit
    }

# 새로운 작곡 생성 (기본 스키마)
@app.post("/compositions")
async def create_composition(
    title: str,
    genre: str,
    tempo: int = 120,
    key_signature: str = "C",
    db: Session = Depends(get_db)
):
    """새로운 작곡 생성"""
    # 임시 사용자 ID (나중에 인증 시스템으로 대체)
    temp_user_id = 1
    
    new_composition = Composition(
        user_id=temp_user_id,
        title=title,
        genre=genre,
        tempo=tempo,
        key_signature=key_signature,
        status="draft"
    )
    
    db.add(new_composition)
    db.commit()
    db.refresh(new_composition)
    
    return {
        "message": "작곡이 성공적으로 생성되었습니다!",
        "composition": new_composition,
        "id": new_composition.id
    }

# 특정 작곡 조회
@app.get("/compositions/{composition_id}")
async def get_composition(composition_id: int, db: Session = Depends(get_db)):
    """특정 작곡 상세 조회"""
    composition = db.query(Composition).filter(Composition.id == composition_id).first()
    
    if not composition:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="작곡을 찾을 수 없습니다."
        )
    
    return {
        "composition": composition,
        "tracks": composition.tracks,
        "midi_files": composition.midi_files
    }

# 에러 핸들러
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """일반 예외 처리"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "내부 서버 오류가 발생했습니다.",
            "detail": str(exc),
            "timestamp": datetime.utcnow().isoformat()
        }
    )

# Ableton Live 연동 추가
@app.get("/ableton/status")
async def get_ableton_status():
    """Ableton Live 연결 상태 확인"""
    try:
        midi_status = midi_connection.get_connection_status()
        live_info = live_api.get_project_info()
        
        return {
            "midi_connection": midi_status,
            "live_project": live_info,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"상태 확인 오류: {str(e)}")


@app.post("/ableton/connect")
async def connect_to_ableton():
    """Ableton Live에 연결"""
    try:
        success = live_api.connect_to_live()
        
        if success:
            return {
                "success": True,
                "message": "Ableton Live 연결 성공",
                "connection_status": midi_connection.get_connection_status()
            }
        else:
            return {
                "success": False,
                "message": "Ableton Live 연결 실패. Live가 실행 중이고 MIDI 포트가 활성화되어 있는지 확인하세요."
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"연결 오류: {str(e)}")


@app.post("/ableton/project/new")
async def create_ableton_project(
    name: str,
    tempo: int = 120,
    key: str = "C"
):
    """새 Ableton Live 프로젝트 생성"""
    try:
        result = live_api.create_new_project(name, tempo, key)
        
        if result.get("success"):
            # 데이터베이스에도 저장
            db = SessionLocal()
            try:
                new_project = AbletonProject(
                    name=name,
                    file_path="",  # 나중에 ALS 파일 생성시 업데이트
                    created_at=datetime.now()
                )
                db.add(new_project)
                db.commit()
                db.refresh(new_project)
                
                result["database_id"] = new_project.id
            finally:
                db.close()
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"프로젝트 생성 오류: {str(e)}")


@app.post("/ableton/project/add-track")
async def add_track_to_project(
    track_name: str,
    track_type: str = "midi",
    instrument: str = None
):
    """프로젝트에 트랙 추가"""
    try:
        result = live_api.add_track(track_name, track_type, instrument)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"트랙 추가 오류: {str(e)}")


@app.get("/ableton/midi/ports")
async def get_midi_ports():
    """사용 가능한 MIDI 포트 조회"""
    try:
        ports = midi_connection.scan_ports()
        return ports
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MIDI 포트 스캔 오류: {str(e)}")


@app.post("/ableton/midi/send-note")
async def send_midi_note(
    channel: int,
    note: int,
    velocity: int,
    duration: float = 0.5
):
    """MIDI 노트 전송"""
    try:
        if not midi_connection.is_connected:
            raise HTTPException(status_code=400, detail="MIDI가 연결되지 않음")
        
        # Note On
        success_on = midi_connection.send_note_on(channel, note, velocity)
        
        if success_on:
            # 지속 시간 후 Note Off (백그라운드에서)
            import asyncio
            asyncio.create_task(
                delayed_note_off(channel, note, duration)
            )
            
            return {
                "success": True,
                "message": f"노트 전송: Ch{channel}, Note{note}, Vel{velocity}"
            }
        else:
            return {"success": False, "message": "노트 전송 실패"}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MIDI 전송 오류: {str(e)}")


async def delayed_note_off(channel: int, note: int, duration: float):
    """지연된 Note Off"""
    await asyncio.sleep(duration)
    midi_connection.send_note_off(channel, note)


@app.get("/ableton/devices")
async def get_max_devices():
    """Max for Live 디바이스 목록 조회"""
    try:
        devices = m4l_manager.list_devices()
        return devices
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"디바이스 조회 오류: {str(e)}")


@app.post("/ableton/devices/create-defaults")
async def create_default_devices():
    """기본 Max for Live 디바이스 생성"""
    try:
        result = m4l_manager.create_default_devices()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"디바이스 생성 오류: {str(e)}")


@app.post("/ableton/project/export")
async def export_project_to_als(file_name: str):
    """프로젝트를 ALS 파일로 내보내기"""
    try:
        file_path = f"./data/ableton_projects/{file_name}.als"
        result = live_api.export_to_als_file(file_path)
        
        if result.get("success"):
            # 데이터베이스 업데이트
            db = SessionLocal()
            try:
                project = db.query(AbletonProject).filter(
                    AbletonProject.name == live_api.current_project["name"]
                ).first()
                
                if project:
                    project.file_path = file_path
                    db.commit()
            finally:
                db.close()
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"내보내기 오류: {str(e)}")

# 개발용 정보
if __name__ == "__main__":
    import uvicorn
    print("🚀 개발 서버를 시작합니다...")
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    ) 