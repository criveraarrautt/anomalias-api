from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Arquitectura Analítica - Auditoría ML",
    version="4.0"
)

# ==============================
# STATIC FILES
# ==============================
app.mount("/static", StaticFiles(directory="static"), name="static")


# ==============================
# LAYOUT BASE
# ==============================
def layout(title, subtitle, paragraph1="", paragraph2="", image=None, link=None, link_text=None):

    image_html = f'<img src="/static/{image}">' if image else ""
    link_html = f'<a class="button" target="_blank" href="{link}">{link_text}</a>' if link else ""

    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
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
            .card {{
                background: white;
                padding: 30px;
                border-radius: 12px;
                margin-bottom: 30px;
                box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
            }}
            h2 {{
                color: #003865;
            }}
            img {{
                width: 100%;
                border-radius: 10px;
                margin-top: 20px;
            }}
            .button {{
                display: inline-block;
                padding: 12px 20px;
                background-color: #D71920;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                margin-top: 20px;
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
        <p>{subtitle}</p>
    </header>

    <div class="container">
        <div class="card">
            <h2>Contexto</h2>
            <p>{paragraph1}</p>
        </div>

        <div class="card">
            <h2>Aplicación práctica</h2>
            <p>{paragraph2}</p>
            {image_html}
            {link_html}
        </div>
    </div>

    </body>
    </html>
    """


# ==============================
# INICIO
# ==============================
@app.get("/", response_class=HTMLResponse)
def inicio():
    return layout(
        title="Plataforma Integral de Auditoría con Machine Learning",
        subtitle="Arquitectura Medallion + Azure ML + Power BI",
        paragraph1="""
        Esta solución integra arquitectura de datos moderna,
        modelos de detección de anomalías y visualización estratégica
        para fortalecer procesos de auditoría y análisis de riesgo.
        """,
        paragraph2="""
        El sistema permite procesar datos en Azure,
        aplicar modelos no supervisados y exponer resultados
        mediante API y dashboards ejecutivos.
        """
    )


# ==============================
# METODOLOGÍA
# ==============================
@app.get("/metodologia", response_class=HTMLResponse)
def metodologia():
    return layout(
        title="Metodología CRISP-DM",
        subtitle="Estructura del desarrollo analítico",
        paragraph1="""
        El proyecto se desarrolló bajo la metodología CRISP-DM,
        garantizando alineación con el negocio, exploración
        profunda de datos y validación técnica del modelo.
        """,
        paragraph2="""
        Se construyó un pipeline completo en Azure ML que integra
        limpieza, transformación, entrenamiento y evaluación
        de modelos no supervisados.
        """,
        image="pipeline.png",
        link="https://ml.azure.com/fileexplorerAzNB?wsid=/subscriptions/76ed1c4c-2873-4232-97e7-02be03d92110/resourcegroups/rg-auditoria-ml/providers/Microsoft.MachineLearningServices/workspaces/mlw-auditoria2026&tid=4f2a92d8-1b15-462d-be76-09d1be64566c&activeFilePath=Users/ccriveraa89/Pipeline_Medallion_Auditoria_ML.ipynb",
        link_text="Ver Notebook en Azure ML"
    )


# ==============================
# DATA LAKE
# ==============================
@app.get("/datalake", response_class=HTMLResponse)
def datalake():
    return layout(
        title="Arquitectura Medallion - Delta Lake",
        subtitle="Modelo Bronze – Silver – Gold",
        paragraph1="""
        La arquitectura Medallion permite organizar datos en capas
        progresivas de calidad, asegurando trazabilidad,
        gobierno y optimización analítica.
        """,
        paragraph2="""
        Se implementó un Delta Lake en Azure con separación
        de datos crudos, transformados y agregados para consumo.
        """,
        image="delta_lake.png",
        link="https://stmlauditoria2026.blob.core.windows.net/",
        link_text="Ver Azure Blob Storage"
    )


# ==============================
# ARQUITECTURA AZURE
# ==============================
@app.get("/arquitectura", response_class=HTMLResponse)
def arquitectura():
    return layout(
        title="Arquitectura Cloud Azure",
        subtitle="Infraestructura Analítica End-to-End",
        paragraph1="""
        La solución integra ingesta de datos, almacenamiento,
        procesamiento distribuido y Machine Learning en Azure.
        """,
        paragraph2="""
        El flujo conecta Data Lake, Azure ML y Power BI,
        permitiendo análisis estratégico en tiempo casi real.
        """,
        image="azure_arch.png"
    )


# ==============================
# MODELO ML
# ==============================
@app.get("/modelo", response_class=HTMLResponse)
def modelo():
    return layout(
        title="Modelo Ensemble de Detección de Anomalías",
        subtitle="Machine Learning No Supervisado",
        paragraph1="""
        Se combinaron múltiples algoritmos:
        Isolation Forest, Local Outlier Factor,
        One-Class SVM y Elliptic Envelope.
        """,
        paragraph2="""
        La integración de modelos reduce falsos positivos
        y fortalece la detección de comportamientos atípicos.
        """
    )


# ==============================
# DASHBOARD
# ==============================
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return layout(
        title="Dashboard Power BI",
        subtitle="Visualización Estratégica de Resultados",
        paragraph1="""
        Los resultados del modelo son consumidos mediante
        dashboards interactivos que permiten análisis
        territorial, institucional y de concentración de riesgo.
        """,
        paragraph2="""
        La visualización facilita la toma de decisiones
        basadas en evidencia analítica.
        """,
        link="https://app.powerbi.com/links/_orIgkbZcp?ctid=08b5b193-b9bb-43f2-922b-7e2948a408e9&pbi_source=linkShare",
        link_text="Abrir Dashboard Power BI"
    )