from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import numpy as np
import os

# ==============================
# Configuración básica
# ==============================

app = FastAPI(
    title="API Detección de Anomalías",
    version="1.0.0",
    description="Plataforma Analítica - Modelo de Anomalías con Machine Learning"
)

# ==============================
# Carga del modelo
# ==============================

MODEL_PATH = "modelo_anomalias_v1.pkl"

try:
    modelo = joblib.load(MODEL_PATH)
except Exception as e:
    modelo = None
    print(f"Error cargando modelo: {e}")

# ==============================
# Esquema de entrada
# ==============================

class InputData(BaseModel):
    TXTOTAL: float
    TXEFECTIVO: float
    RATIO_EFECTIVO: float
    HORA_MIN: float
    DOW: float
    USER_TX_MES: float
    CLI_TX_MES: float
    SCORE_REGLAS: float

# ==============================
# Página principal (Presentación)
# ==============================

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Plataforma Analítica - Modelo de Anomalías</title>
            <style>
                body {
                    font-family: 'Segoe UI', Arial, sans-serif;
                    margin: 0;
                    background-color: #F4F6F9;
                    color: #1A1A1A;
                }
                header {
                    background-color: #003865;
                    color: white;
                    padding: 30px;
                    text-align: center;
                }
                .container {
                    padding: 40px;
                    max-width: 1100px;
                    margin: auto;
                }
                .card {
                    background: white;
                    padding: 25px;
                    border-radius: 12px;
                    margin-bottom: 30px;
                    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
                    border-left: 6px solid #005EB8;
                }
                h2 { color: #003865; }
                a.button {
                    display: inline-block;
                    padding: 12px 20px;
                    background-color: #D71920;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: bold;
                }
                footer {
                    background-color: #003865;
                    color: white;
                    text-align: center;
                    padding: 15px;
                    margin-top: 40px;
                }
            </style>
        </head>
        <body>

            <header>
                <h1>Plataforma de Detección de Anomalías</h1>
                <p>Arquitectura Analítica | Machine Learning | API en la Nube</p>
            </header>

            <div class="container">

                <div class="card">
                    <h2>🏗 Arquitectura del Sistema</h2>
                    <ul>
                        <li><strong>Capa de Datos:</strong> Preprocesamiento y escalamiento.</li>
                        <li><strong>Capa de Modelado:</strong> Ensemble ML (IForest, LOF, SVM, PCA).</li>
                        <li><strong>Capa API:</strong> Microservicio FastAPI desplegado en Render.</li>
                        <li><strong>Capa Visualización:</strong> Dashboard estratégico en Power BI.</li>
                    </ul>
                </div>

                <div class="card">
                    <h2>📊 Dashboard Power BI</h2>
                    <p>Accede al monitoreo interactivo:</p>
                    <a href="https://app.powerbi.com/groups/me/reports/aa89ddd4-4770-4458-824a-9ea9508fc87b"
                       target="_blank"
                       class="button">
                        Ver Dashboard
                    </a>
                </div>

                <div class="card">
                    <h2>📘 Documentación Técnica</h2>
                    <a href="/docs" target="_blank" class="button">
                        Ir a Swagger
                    </a>
                </div>

            </div>

            <footer>
                Arquitectura Analítica | Modelo de Anomalías | Deploy Cloud
            </footer>

        </body>
    </html>
    """

# ==============================
# Endpoint de predicción
# ==============================

@app.post("/predict")
def predict(data: InputData):
    if modelo is None:
        raise HTTPException(status_code=500, detail="Modelo no cargado")

    try:
        X = np.array([[ 
            data.TXTOTAL,
            data.TXEFECTIVO,
            data.RATIO_EFECTIVO,
            data.HORA_MIN,
            data.DOW,
            data.USER_TX_MES,
            data.CLI_TX_MES,
            data.SCORE_REGLAS
        ]])

        scaler = modelo["scaler"]
        iforest = modelo["iforest"]
        lof = modelo["lof"]
        ocsvm = modelo["ocsvm"]
        ee = modelo["elliptic"]
        pca = modelo["pca"]

        Xs = scaler.transform(X)

        s_if = -iforest.decision_function(Xs)
        s_lof = -lof.decision_function(Xs)
        s_svm = -ocsvm.decision_function(Xs)
        s_ee = -ee.decision_function(Xs)

        Z = pca.transform(Xs)
        Xrec = pca.inverse_transform(Z)
        recon = np.mean((Xs - Xrec) ** 2, axis=1)

        ensemble = np.mean([s_if, s_lof, s_svm, s_ee, recon], axis=0)

        return {
            "anomaly_score": float(ensemble[0]),
            "status": "Anómala" if ensemble[0] > 0 else "Normal"
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ==============================
# Health Check
# ==============================

@app.get("/health")
def health():
    return {"status": "OK", "modelo_cargado": modelo is not None}