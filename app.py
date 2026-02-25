from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Arquitectura Analítica - Auditoría ML",
    version="3.0"
)

# ===============================
# Servir imágenes (carpeta estático)
# ===============================
app.mount("/estatico", StaticFiles(directory="estático"), name="estatico")


# ===============================
# Plantilla base
# ===============================

def layout(title, content):
    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial;
                margin: 0;
                background-color: #F4F6F9;
            }}
            nav {{
                background-color: #003865;
                padding: 15px;
            }}
            nav a {{
                color: white;
                margin-right: 20px;
                text-decoration: none;
                font-weight: bold;
            }}
            header {{
                padding: 40px;
                text-align: center;
                background-color: #005EB8;
                color: white;
            }}
            .container {{
                padding: 40px;
                max-width: 1100px;
                margin: auto;
            }}
            h2 {{
                color: #003865;
            }}
            .card {{
                background: white;
                padding: 30px;
                border-radius: 12px;
                margin-bottom: 30px;
                box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
            }}
            img {{
                width: 100%;
                border-radius: 10px;
                margin-top: 20px;
            }}
            a.button {{
                display: inline-block;
                padding: 12px 20px;
                background-color: #D71920;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                margin-top: 15px;
            }}
        </style>
    </head>
    <body>

    <nav>
        <a href="/">Inicio</a>
        <a href="/metodologia">Metodología</a>
        <a href="/datalake">Data Lake</a>
        <a href="/arquitectura">Arquitectura Azure</a>
        <a href="/modelo">Modelo ML</a>
        <a href="/dashboard">Dashboard</a>
        <a href="/docs">API</a>
    </nav>

    <header>
        <h1>{title}</h1>
    </header>

    <div class="container">
        {content}
    </div>

    </body>
    </html>
    """


# ===============================
# INICIO
# ===============================

@app.get("/", response_class=HTMLResponse)
def inicio():
    content = """
    <div class="card">
        <h2>Plataforma Integral de Auditoría con Machine Learning</h2>
        <p>
        Esta solución implementa una arquitectura moderna basada en modelo Medallion 
        (Bronze, Silver, Gold), procesamiento en Azure, modelos no supervisados 
        para detección de anomalías y visualización estratégica en Power BI.
        </p>
    </div>
    """
    return layout("Arquitectura Analítica Integral", content)


# ===============================
# METODOLOGÍA
# ===============================

@app.get("/metodologia", response_class=HTMLResponse)
def metodologia():
    content = """
    <div class="card">
        <h2>Metodología CRISP-DM Aplicada</h2>
        <p>
        El proyecto siguió la metodología CRISP-DM:
        </p>
        <ul>
            <li>Comprensión del negocio</li>
            <li>Comprensión y análisis exploratorio de datos</li>
            <li>Transformación y preparación</li>
            <li>Modelado con múltiples algoritmos</li>
            <li>Evaluación mediante Ensemble Score</li>
            <li>Despliegue como API productiva</li>
        </ul>
        <img src="/estatico/tubería.png">
    </div>

    <div class="card">
        <h2>Notebook del Pipeline en Azure ML</h2>
        <a class="button" target="_blank"
        href="https://ml.azure.com/fileexplorerAzNB?wsid=/subscriptions/76ed1c4c-2873-4232-97e7-02be03d92110/resourcegroups/rg-auditoria-ml/providers/Microsoft.MachineLearningServices/workspaces/mlw-auditoria2026&tid=4f2a92d8-1b15-462d-be76-09d1be64566c&activeFilePath=Users/ccriveraa89/Pipeline_Medallion_Auditoria_ML.ipynb">
        Ver Pipeline en Azure ML
        </a>
    </div>
    """
    return layout("Metodología y Flujo de Trabajo", content)


# ===============================
# DATA LAKE
# ===============================

@app.get("/datalake", response_class=HTMLResponse)
def datalake():
    content = """
    <div class="card">
        <h2>Arquitectura Medallion (Delta Lake)</h2>
        <p>
        La arquitectura se estructuró en tres capas:
        </p>
        <ul>
            <li><b>Bronze:</b> Datos crudos desde origen.</li>
            <li><b>Silver:</b> Datos limpios, transformados y validados.</li>
            <li><b>Gold:</b> Agregaciones listas para analítica.</li>
        </ul>
        <img src="/estatico/delta_lago.png">
    </div>

    <div class="card">
        <h2>Azure Blob Storage</h2>
        <a class="button" target="_blank"
        href="https://stmlauditoria2026.blob.core.windows.net/">
        Ver Storage en Azure
        </a>
    </div>
    """
    return layout("Arquitectura Data Lake", content)


# ===============================
# ARQUITECTURA AZURE
# ===============================

@app.get("/arquitectura", response_class=HTMLResponse)
def arquitectura():
    content = """
    <div class="card">
        <h2>Arquitectura Cloud en Azure</h2>
        <p>
        La solución integra ingesta, procesamiento, Machine Learning 
        y consumo analítico mediante Power BI.
        </p>
        <img src="/estatico/arquitectura azul.png">
    </div>
    """
    return layout("Arquitectura Cloud Azure", content)


# ===============================
# MODELO ML
# ===============================

@app.get("/modelo", response_class=HTMLResponse)
def modelo():
    content = """
    <div class="card">
        <h2>Modelo de Detección de Anomalías</h2>
        <p>
        Se implementó un enfoque ensemble combinando:
        </p>
        <ul>
            <li>Isolation Forest</li>
            <li>Local Outlier Factor</li>
            <li>One-Class SVM</li>
            <li>Elliptic Envelope</li>
        </ul>
        <p>
        El resultado es un score robusto que reduce falsos positivos.
        </p>
    </div>
    """
    return layout("Modelo Machine Learning", content)


# ===============================
# DASHBOARD
# ===============================

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    content = """
    <div class="card">
        <h2>Visualización Estratégica en Power BI</h2>
        <p>
        Los resultados del modelo se consumen mediante dashboards interactivos
        que permiten análisis territorial, institucional y de riesgo.
        </p>

        <a class="button" target="_blank"
        href="https://app.powerbi.com/links/_orIgkbZcp?ctid=08b5b193-b9bb-43f2-922b-7e2948a408e9&pbi_source=linkShare">
        Ver Dashboard Power BI
        </a>
    </div>
    """
    return layout("Dashboard Analítico", content)