from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Arquitectura Analítica - Auditoría ML",
    version="6.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


# ===============================
# LAYOUT BASE MODERNO
# ===============================

def layout(title, subtitle, content_html):

    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                margin: 0;
                background-color: #F4F6F9;
                color: #1F2937;
            }}

            nav {{
                background: linear-gradient(90deg, #003865, #005EB8);
                padding: 15px 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}

            nav a {{
                color: white;
                text-decoration: none;
                margin-right: 20px;
                font-weight: 500;
            }}

            header {{
                padding: 80px 20px;
                text-align: center;
                background: linear-gradient(180deg, #005EB8, #003865);
                color: white;
            }}

            header h1 {{
                font-size: 42px;
                margin-bottom: 10px;
            }}

            header p {{
                font-size: 18px;
                opacity: 0.9;
            }}

            .container {{
                max-width: 1100px;
                margin: auto;
                padding: 60px 20px;
            }}

            .card {{
                background: white;
                padding: 40px;
                border-radius: 14px;
                margin-bottom: 40px;
                box-shadow: 0px 10px 30px rgba(0,0,0,0.05);
                transition: 0.3s;
            }}

            .card:hover {{
                transform: translateY(-5px);
            }}

            .text-block {{
                line-height: 1.8;
                white-space: pre-line;
            }}

            .model-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
                gap: 30px;
                margin-top: 30px;
            }}

            .model-card {{
                background: white;
                padding: 30px;
                border-radius: 14px;
                box-shadow: 0px 8px 25px rgba(0,0,0,0.05);
                transition: 0.3s;
            }}

            .model-card:hover {{
                transform: translateY(-6px);
            }}

            img {{
                width: 100%;
                border-radius: 10px;
                margin-top: 25px;
            }}

            .btn {{
                display: inline-block;
                padding: 12px 22px;
                background-color: #D71920;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                margin-top: 25px;
            }}

            footer {{
                text-align: center;
                padding: 30px;
                background-color: #003865;
                color: white;
                margin-top: 40px;
            }}
        </style>
    </head>

    <body>

    <nav>
        <div style="color:white;font-weight:600;">Auditoría ML</div>
        <div>
            <a href="/">Inicio</a>
            <a href="/metodologia">Metodología</a>
            <a href="/datalake">Data Lake</a>
            <a href="/arquitectura">Arquitectura Cloud</a>
            <a href="/modelo">Modelo ML</a>
            <a href="/dashboard">Dashboard</a>
            <a href="/docs">API</a>
        </div>
    </nav>

    <header>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </header>

    <div class="container">
        {content_html}
    </div>

    <footer>
        Arquitectura Analítica · Azure ML · Power BI
    </footer>

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
        <div class="text-block">
        Esta solución integra arquitectura moderna de datos,
        procesamiento distribuido en la nube y modelos de detección
        de anomalías para fortalecer procesos de auditoría.
        </div>
    </div>

    <div class="card">
        <div class="text-block">
        Permite identificar comportamientos atípicos,
        concentraciones territoriales y patrones de riesgo
        mediante análisis avanzado y visualización ejecutiva.
        </div>
    </div>
    """

    return layout(
        "Plataforma Integral de Auditoría con Machine Learning",
        "Arquitectura Medallion + Azure ML + Power BI",
        content
    )


# ===============================
# METODOLOGÍA
# ===============================
@app.get("/metodologia", response_class=HTMLResponse)
def metodologia():

    content = """
    <div class="card">
        <div class="text-block">
        El proyecto fue desarrollado bajo CRISP-DM,
        asegurando alineación estratégica,
        comprensión profunda de los datos
        y validación técnica del modelo.
        </div>
        <img src="/static/pipeline.png">
    </div>
    """

    return layout(
        "Metodología CRISP-DM",
        "Marco estructurado de desarrollo analítico",
        content
    )


# ===============================
# DATA LAKE
# ===============================
@app.get("/datalake", response_class=HTMLResponse)
def datalake():

    content = """
    <div class="card">
        <div class="text-block">
        Arquitectura Bronze – Silver – Gold
        para garantizar trazabilidad y gobierno de datos.
        </div>
        <img src="/static/delta_lake.png">
    </div>
    """

    return layout(
        "Arquitectura Medallion",
        "Modelo Delta Lake",
        content
    )


# ===============================
# ARQUITECTURA CLOUD
# ===============================
@app.get("/arquitectura", response_class=HTMLResponse)
def arquitectura():

    content = """
    <div class="card">
        <div class="text-block">
        Integración de Data Lake, Azure ML y visualización estratégica.
        Azure Blob Storage actúa como repositorio central.
        </div>
        <img src="/static/azure_arch.png">
        <a class="btn" target="_blank"
        href="https://stmlauditoria2026.blob.core.windows.net/">
        Explorar Azure Blob Storage
        </a>
    </div>
    """

    return layout(
        "Arquitectura Cloud Azure",
        "Infraestructura Analítica End-to-End",
        content
    )


# ===============================
# MODELO ML
# ===============================
@app.get("/modelo", response_class=HTMLResponse)
def modelo():

    content = """
    <div class="model-grid">

        <div class="model-card">
            <h3>Isolation Forest</h3>
            <p>Como un auditor que separa registros hasta encontrar cuáles se aíslan rápidamente.</p>
        </div>

        <div class="model-card">
            <h3>Local Outlier Factor</h3>
            <p>Compara cada registro con sus vecinos inmediatos para detectar diferencias locales.</p>
        </div>

        <div class="model-card">
            <h3>One-Class SVM</h3>
            <p>Dibuja un perímetro alrededor del comportamiento normal y marca lo que queda fuera.</p>
        </div>

        <div class="model-card">
            <h3>Elliptic Envelope</h3>
            <p>Mide la distancia estadística respecto al centro multivariable.</p>
        </div>

    </div>

    <a class="btn" target="_blank"
    href="https://ml.azure.com/fileexplorerAzNB?wsid=/subscriptions/76ed1c4c-2873-4232-97e7-02be03d92110/resourcegroups/rg-auditoria-ml/providers/Microsoft.MachineLearningServices/workspaces/mlw-auditoria2026">
    Ver Notebook Azure ML
    </a>
    """

    return layout(
        "Modelo Ensemble de Detección de Anomalías",
        "Machine Learning No Supervisado",
        content
    )


# ===============================
# DASHBOARD
# ===============================
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():

    content = """
    <div class="card">
        <div class="text-block">
        Visualización estratégica de resultados del modelo
        mediante dashboards interactivos en Power BI.
        </div>
        <a class="btn" target="_blank"
        href="https://app.powerbi.com/links/_orIgkbZcp?ctid=08b5b193-b9bb-43f2-922b-7e2948a408e9&pbi_source=linkShare">
        Abrir Dashboard Power BI
        </a>
    </div>
    """

    return layout(
        "Dashboard Power BI",
        "Visualización Estratégica",
        content
    )