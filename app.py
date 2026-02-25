from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="API Modelo Anomalías")

modelo = joblib.load("modelo_anomalias_v1.pkl")

def minmax_0_100(x):
    return 100 * (x - np.min(x)) / (np.max(x) - np.min(x) + 1e-8)

@app.get("/")
def home():
    return {"mensaje": "API de Anomalías Activa"}

@app.post("/predict")
def predict(data: list):
    df = pd.DataFrame(data)

    scaler = modelo["scaler"]
    iforest = modelo["iforest"]
    lof = modelo["lof"]
    ocsvm = modelo["ocsvm"]
    ee = modelo["elliptic"]
    pca = modelo["pca"]

    Xs = scaler.transform(df)

    s_if = minmax_0_100(-iforest.decision_function(Xs))
    s_lof = minmax_0_100(-lof.decision_function(Xs))
    s_svm = minmax_0_100(-ocsvm.decision_function(Xs))
    s_ee = minmax_0_100(-ee.decision_function(Xs))

    Z = pca.transform(Xs)
    Xrec = pca.inverse_transform(Z)
    recon = np.mean((Xs - Xrec)**2, axis=1)
    s_pca = minmax_0_100(recon)

    ensemble = np.mean([s_if, s_lof, s_svm, s_ee, s_pca], axis=0)

    return {"ANOM_ENSEMBLE": ensemble.tolist()}