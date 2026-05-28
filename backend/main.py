from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS CONNECTION

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HOME API

@app.get("/")
def home():
    return {
        "message": "Transformer Health AI Backend Running"
    }

# PREDICTION API

@app.post("/predict")
def predict(data: dict):

    # DGA PARAMETERS

    hydrogen = data.get("hydrogen", 0)
    methane = data.get("methane", 0)
    ethylene = data.get("ethylene", 0)
    ethane = data.get("ethane", 0)
    acetylene = data.get("acetylene", 0)
    co = data.get("co", 0)

    # IR PARAMETERS

    kv = data.get("kv", 0)
    ir = data.get("ir", 0)

    # OIL PARAMETERS

    acid = data.get("acid", 0)
    water = data.get("water", 0)
    breakdown = data.get("breakdown", 0)
    viscosity = data.get("viscosity", 0)

    # HEALTH SCORE

    health_score = 100

    # DGA ANALYSIS

    if hydrogen > 1000:
        health_score -= 20

    if methane > 1000:
        health_score -= 20

    if acetylene > 50:
        health_score -= 30

    if ethylene > 100:
        health_score -= 10

    # IR ANALYSIS

    required_ir = kv + 1

    if ir < required_ir:
        health_score -= 20

    # OIL ANALYSIS

    if water > 40:
        health_score -= 10

    if acid > 0.3:
        health_score -= 10

    if breakdown < 30:
        health_score -= 20

    # FINAL CONDITION

    if health_score >= 80:
        condition = "Healthy"

    elif health_score >= 60:
        condition = "Caution"

    elif health_score >= 40:
        condition = "Abnormal"

    else:
        condition = "Danger"

    return {
        "condition": condition,
        "health_score": health_score,
        "required_ir": required_ir
    }