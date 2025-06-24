"""
Max for Live 디바이스 관리 모듈
AI 생성 음악을 위한 M4L 디바이스 템플릿 및 관리
"""

import os
import json
from typing import Dict, List, Any, Optional
import logging

logger = logging.getLogger(__name__)


class MaxForLiveDevice:
    """Max for Live 디바이스 관리 클래스"""
    
    def __init__(self, device_name: str):
        self.device_name = device_name
        self.device_path = None
        self.parameters = {}
        self.is_loaded = False
        
    def create_ai_generator_device(self, output_path: str) -> Dict[str, Any]:
        """AI 음악 생성을 위한 M4L 디바이스 생성"""
        try:
            device_template = {
                "device_info": {
                    "name": self.device_name,
                    "type": "midi_effect",
                    "version": "1.0.0",
                    "author": "AI Songwriting System",
                    "description": "AI 기반 실시간 음악 생성 디바이스"
                },
                "max_patch": {
                    "inlets": [
                        {"type": "midi", "description": "MIDI 입력"},
                        {"type": "control", "description": "제어 신호"}
                    ],
                    "outlets": [
                        {"type": "midi", "description": "생성된 MIDI"},
                        {"type": "audio", "description": "오디오 출력"}
                    ],
                    "objects": [
                        {
                            "name": "ai_generator",
                            "type": "external",
                            "function": "음악 생성 엔진"
                        },
                        {
                            "name": "genre_selector", 
                            "type": "umenu",
                            "items": ["Rock", "Hip-hop", "Jpop", "Jazz", "Classical", "Pop"]
                        },
                        {
                            "name": "tempo_control",
                            "type": "slider",
                            "range": [60, 200],
                            "default": 120
                        },
                        {
                            "name": "creativity_dial",
                            "type": "dial",
                            "range": [0.0, 1.0],
                            "default": 0.8
                        }
                    ]
                },
                "parameters": {
                    "genre": {
                        "type": "enum",
                        "values": ["Rock", "Hip-hop", "Jpop", "Jazz", "Classical", "Pop"],
                        "default": "Pop"
                    },
                    "tempo": {
                        "type": "int",
                        "min": 60,
                        "max": 200,
                        "default": 120
                    },
                    "creativity": {
                        "type": "float",
                        "min": 0.0,
                        "max": 1.0,
                        "default": 0.8
                    },
                    "key": {
                        "type": "enum",
                        "values": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
                        "default": "C"
                    },
                    "scale": {
                        "type": "enum", 
                        "values": ["Major", "Minor", "Dorian", "Mixolydian", "Pentatonic"],
                        "default": "Major"
                    }
                },
                "automation": {
                    "mappable_parameters": ["tempo", "creativity", "genre"],
                    "midi_learn": True
                }
            }
            
            # 디렉토리 생성
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # M4L 디바이스 파일 생성 (JSON 형태로 임시 저장)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(device_template, f, indent=2, ensure_ascii=False)
            
            self.device_path = output_path
            self.parameters = device_template["parameters"]
            
            logger.info(f"M4L 디바이스 생성: {output_path}")
            
            return {
                "success": True,
                "device_path": output_path,
                "template": device_template
            }
            
        except Exception as e:
            logger.error(f"M4L 디바이스 생성 오류: {e}")
            return {"success": False, "error": str(e)}
    
    def create_track_mixer_device(self, output_path: str) -> Dict[str, Any]:
        """트랙별 믹싱을 위한 M4L 디바이스 생성"""
        try:
            mixer_template = {
                "device_info": {
                    "name": f"{self.device_name}_Mixer",
                    "type": "audio_effect",
                    "version": "1.0.0",
                    "author": "AI Songwriting System",
                    "description": "AI 생성 트랙 믹싱 디바이스"
                },
                "max_patch": {
                    "inlets": [
                        {"type": "audio", "description": "오디오 입력 L"},
                        {"type": "audio", "description": "오디오 입력 R"}
                    ],
                    "outlets": [
                        {"type": "audio", "description": "믹싱된 오디오 L"},
                        {"type": "audio", "description": "믹싱된 오디오 R"}
                    ],
                    "tracks": [
                        {"name": "Drums", "volume": 0.8, "pan": 0.0},
                        {"name": "Bass", "volume": 0.7, "pan": -0.2},
                        {"name": "Melody", "volume": 0.6, "pan": 0.1},
                        {"name": "Harmony", "volume": 0.5, "pan": 0.0},
                        {"name": "Lead", "volume": 0.8, "pan": 0.3},
                        {"name": "Pad", "volume": 0.4, "pan": -0.1}
                    ]
                },
                "parameters": {
                    "master_volume": {
                        "type": "float",
                        "min": 0.0,
                        "max": 1.0,
                        "default": 0.8
                    },
                    "track_volumes": {
                        "type": "array",
                        "length": 6,
                        "default": [0.8, 0.7, 0.6, 0.5, 0.8, 0.4]
                    },
                    "track_pans": {
                        "type": "array", 
                        "length": 6,
                        "default": [0.0, -0.2, 0.1, 0.0, 0.3, -0.1]
                    }
                }
            }
            
            # 디렉토리 생성
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # 믹서 디바이스 파일 생성
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(mixer_template, f, indent=2, ensure_ascii=False)
            
            logger.info(f"믹서 디바이스 생성: {output_path}")
            
            return {
                "success": True,
                "device_path": output_path,
                "template": mixer_template
            }
            
        except Exception as e:
            logger.error(f"믹서 디바이스 생성 오류: {e}")
            return {"success": False, "error": str(e)}
    
    def load_device(self, device_path: str) -> bool:
        """M4L 디바이스 로드"""
        try:
            if not os.path.exists(device_path):
                logger.error(f"디바이스 파일을 찾을 수 없음: {device_path}")
                return False
            
            with open(device_path, 'r', encoding='utf-8') as f:
                device_data = json.load(f)
            
            self.device_path = device_path
            self.parameters = device_data.get("parameters", {})
            self.is_loaded = True
            
            logger.info(f"M4L 디바이스 로드 완료: {device_path}")
            return True
            
        except Exception as e:
            logger.error(f"디바이스 로드 오류: {e}")
            return False
    
    def set_parameter(self, param_name: str, value: Any) -> bool:
        """디바이스 파라미터 설정"""
        try:
            if not self.is_loaded:
                logger.warning("디바이스가 로드되지 않음")
                return False
            
            if param_name not in self.parameters:
                logger.warning(f"알 수 없는 파라미터: {param_name}")
                return False
            
            param_info = self.parameters[param_name]
            
            # 값 유효성 검사
            if param_info["type"] == "int":
                if param_info["min"] <= value <= param_info["max"]:
                    logger.info(f"파라미터 설정: {param_name} = {value}")
                    return True
            elif param_info["type"] == "float":
                if param_info["min"] <= value <= param_info["max"]:
                    logger.info(f"파라미터 설정: {param_name} = {value}")
                    return True
            elif param_info["type"] == "enum":
                if value in param_info["values"]:
                    logger.info(f"파라미터 설정: {param_name} = {value}")
                    return True
            
            logger.warning(f"잘못된 파라미터 값: {param_name} = {value}")
            return False
            
        except Exception as e:
            logger.error(f"파라미터 설정 오류: {e}")
            return False
    
    def get_parameter(self, param_name: str) -> Any:
        """디바이스 파라미터 조회"""
        try:
            if not self.is_loaded or param_name not in self.parameters:
                return None
            
            return self.parameters[param_name].get("default")
            
        except Exception as e:
            logger.error(f"파라미터 조회 오류: {e}")
            return None
    
    def get_device_info(self) -> Dict[str, Any]:
        """디바이스 정보 반환"""
        return {
            "name": self.device_name,
            "path": self.device_path,
            "is_loaded": self.is_loaded,
            "parameters": list(self.parameters.keys()) if self.parameters else [],
            "parameter_count": len(self.parameters) if self.parameters else 0
        }


class MaxForLiveManager:
    """Max for Live 디바이스 매니저"""
    
    def __init__(self):
        self.devices: Dict[str, MaxForLiveDevice] = {}
        self.device_directory = "./data/max_devices/"
        
    def create_default_devices(self) -> Dict[str, Any]:
        """기본 M4L 디바이스들 생성"""
        try:
            results = {}
            
            # AI 생성기 디바이스
            generator = MaxForLiveDevice("AI_Music_Generator")
            generator_path = os.path.join(self.device_directory, "ai_generator.json")
            result = generator.create_ai_generator_device(generator_path)
            results["generator"] = result
            
            if result["success"]:
                self.devices["generator"] = generator
            
            # 트랙 믹서 디바이스
            mixer = MaxForLiveDevice("AI_Track_Mixer")  
            mixer_path = os.path.join(self.device_directory, "track_mixer.json")
            result = mixer.create_track_mixer_device(mixer_path)
            results["mixer"] = result
            
            if result["success"]:
                self.devices["mixer"] = mixer
            
            logger.info("기본 M4L 디바이스 생성 완료")
            
            return {
                "success": True,
                "devices": results,
                "device_count": len([r for r in results.values() if r["success"]])
            }
            
        except Exception as e:
            logger.error(f"기본 디바이스 생성 오류: {e}")
            return {"success": False, "error": str(e)}
    
    def get_device(self, device_name: str) -> Optional[MaxForLiveDevice]:
        """디바이스 반환"""
        return self.devices.get(device_name)
    
    def list_devices(self) -> Dict[str, Any]:
        """로드된 디바이스 목록"""
        return {
            name: device.get_device_info() 
            for name, device in self.devices.items()
        }


# 전역 M4L 매니저 인스턴스
global_m4l_manager = MaxForLiveManager()


def get_m4l_manager() -> MaxForLiveManager:
    """전역 M4L 매니저 인스턴스 반환"""
    return global_m4l_manager 