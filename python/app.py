from fastapi import FastAPI, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# BASE_DIR 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
dotenv_path = os.path.join(BASE_DIR, '.env')

# .env 파일 로드
load_dotenv(dotenv_path)

# 환경 변수 가져오기
FASTAPI = os.getenv('FASTAPI')

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React 앱의 URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 연결 확인
@app.get("/")
async def root():
    return {"message": "연결 성공"}

# 전체 소음 데이터 조회
@app.get("/getNoiseData")
async def get_noise_data():
    try:
        response = requests.get(FASTAPI + "/getNoiseDataAll")
        datas = response.json()
        result = []
        for data in datas:
            label = data["label"]
            decibel = data["decibel"]
            timemap = data["timemap"]
            lat = float(timemap[:10])
            lon = float(timemap[10:20])
            if (label != "silence") and (label != "speech"):
                result.append({
                    "location": {
                        "lat": lat,
                        "lon": lon
                    },
                    "label": label,
                    "decibel": decibel
                })
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 일주일 동안의 소음 데이터 조회
@app.get("/getNoiseDataWeek")
async def get_noise_data_week():
    try:
        response = requests.get(FASTAPI + "/getNoiseDataWeek")
        datas = response.json()
        result = []
        for data in datas:
            label = data["label"]
            decibel = data["decibel"]
            timemap = data["timemap"]
            lat = float(timemap[:10])
            lon = float(timemap[10:21])
            if (label != "silence") and (label != "speech"):
                result.append({
                    "location": {
                        "lat": lat,
                        "lon": lon
                    },
                    "label": label,
                    "decibel": decibel
                })
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 하루 동안의 소음 데이터 조회
@app.get("/getNoiseDataOneDay")
async def get_noise_data_one_day():
    try:
        response = requests.get(FASTAPI+ "/getNoiseDataOneDay")
        datas = response.json()
        result = []
        for data in datas:
            label = data["label"]
            decibel = data["decibel"]
            timemap = data["timemap"]
            lat = float(timemap[:10])
            lon = float(timemap[10:21])
            if (label != "silence") and (label != "speech"):
                result.append({
                    "location": {
                        "lat": lat,
                        "lon": lon
                    },
                    "label": label,
                    "decibel": decibel
                })
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5200)