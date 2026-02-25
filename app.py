from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Arquitectura Analítica - Auditoría ML",
    version="5.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


# ===============================
# LAYOUT MODERNO
# ===============================

def layout(title, subtitle, paragraph1="", paragraph2="", image=None, link=None, link_text=None):

    image_html = f'<img src="/static/{image}" class="image">' if image else ""
    link_html = f'<a class="btn" target="_blank" href="{link}">{link_text}</a>' if link else ""

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

            h2 {{
                color: #003865;
                margin-bottom: 15px;
            }}

            .image {{
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
                font-weight: 500;
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
    return layout(
        "Plataforma Integral de Auditoría con Machine Learning",
        "Arquitectura Medallion + Azure ML + Power BI",
        """
        Esta solución integra arquitectura moderna de datos,
        procesamiento distribuido en la nube y modelos de detección
        de anomalías para fortalecer procesos de auditoría.
        """,
        """
        Permite identificar comportamientos atípicos,
        concentraciones territoriales y patrones de riesgo
        mediante análisis avanzado y visualización ejecutiva.
        """
    )


# ===============================
# METODOLOGÍA (SIN LINK)
# ===============================
@app.get("/metodologia", response_class=HTMLResponse)
def metodologia():
    return layout(
        "Metodología CRISP-DM",
        "Marco estructurado de desarrollo analítico",
        """
        El proyecto fue desarrollado bajo CRISP-DM,
        asegurando alineación estratégica, comprensión
        profunda de los datos y validación técnica del modelo.
        """,
        """
        Se realizó análisis exploratorio, transformación,
        selección de variables y evaluación comparativa
        de modelos no supervisados.
        """,
        image="pipeline.png"
    )


# ===============================
# DATA LAKE
# ===============================
@app.get("/datalake", response_class=HTMLResponse)
def datalake():
    return layout(
        "Arquitectura Medallion - Delta Lake",
        "Modelo Bronze – Silver – Gold",
        """
        La arquitectura Medallion organiza los datos en capas
        progresivas de calidad para garantizar trazabilidad,
        control y gobierno.
        """,
        """
        Bronze almacena datos crudos,
        Silver datos limpios y estructurados,
        Gold datos listos para analítica avanzada.
        """,
        image="delta_lake.png"
    )


# ===============================
# ARQUITECTURA CLOUD (AQUÍ VA EL STORAGE)
# ===============================
@app.get("/arquitectura", response_class=HTMLResponse)
def arquitectura():
    return layout(
        "Arquitectura Cloud Azure",
        "Infraestructura Analítica End-to-End",
        """
        La solución integra Data Lake, Azure ML
        y visualización estratégica.
        """,
        """
        Azure Blob Storage actúa como repositorio central
        de datos estructurados y no estructurados.
        """,
        image="azure_arch.png",
        link="https://portal.azure.com/#@ccriveraa89gmail.onmicrosoft.com/resource/subscriptions/76ed1c4c-2873-4232-97e7-02be03d92110/resourceGroups/rg-auditoria-ml/providers/Microsoft.Storage/storageAccounts/stmlauditoria2026/containersList",
        link_text="Explorar Azure Blob Storage"
    )


# ===============================
# MODELO ML (AQUÍ VA EL NOTEBOOK)
# ===============================
@app.get("/modelo", response_class=HTMLResponse)
def modelo():
    return layout(
        "Modelo Ensemble de Detección de Anomalías",
        "Machine Learning No Supervisado",
		"""
		Se implementó un enfoque ensemble combinando
		Isolation Forest, LOF, One-Class SVM y Elliptic Envelope.

		• Isolation Forest:
		Funciona como un auditor que separa registros uno a uno
		hasta encontrar cuáles se aíslan rápidamente del resto.
		Si un dato necesita muy pocos cortes para quedar solo,
		probablemente es anómalo.

		• Local Outlier Factor (LOF):
		Es como comparar un comercio con sus vecinos del mismo barrio.
		Si su comportamiento es muy diferente respecto a su entorno inmediato,
		se considera sospechoso, aunque a nivel global no lo parezca.

		• One-Class SVM:
		Actúa como un guardia que dibuja un perímetro alrededor
		del comportamiento normal.
		Todo lo que queda fuera de ese límite es marcado como atípico.

		• Elliptic Envelope:
		Funciona como medir qué tan lejos está un punto del “centro estadístico”.
		Si un registro está demasiado lejos del promedio multivariable,
		es tratado como una desviación significativa.

		La combinación de estos enfoques permite detectar
		diferentes tipos de anomalías y reducir falsos positivos,
		tal como lo haría un comité de auditores evaluando
		un mismo caso desde distintas perspectivas.
		""",
        """
        El modelo fue desarrollado y validado en Azure ML,
        permitiendo entrenamiento, versionamiento y despliegue.
        """,
        link="https://ml.azure.com/fileexplorerAzNB?wsid=/subscriptions/76ed1c4c-2873-4232-97e7-02be03d92110/resourcegroups/rg-auditoria-ml/providers/Microsoft.MachineLearningServices/workspaces/mlw-auditoria2026&tid=4f2a92d8-1b15-462d-be76-09d1be64566c&activeFilePath=Users/ccriveraa89/Pipeline_Medallion_Auditoria_ML.ipynb",
        link_text="Ver Notebook Azure ML"
    )


# ===============================
# DASHBOARD
# ===============================
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return layout(
        "Dashboard Power BI",
        "Visualización Estratégica de Resultados",
        """
        Los resultados del modelo se presentan mediante
        dashboards interactivos para análisis territorial
        e institucional.
        """,
        """
        La visualización facilita toma de decisiones
        basadas en evidencia analítica.
        """,
        link="https://app.powerbi.com/links/_orIgkbZcp?ctid=08b5b193-b9bb-43f2-922b-7e2948a408e9&pbi_source=linkShare",
        link_text="Abrir Dashboard Power BI"
    )