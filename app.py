from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Plataforma Arquitectura Analítica",
    version="2.0"
)

# Servir imágenes
app.mount("/static", StaticFiles(directory="static"), name="static")


# =============================
# Plantilla base
# =============================

def layout(title, content):
    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Arial;
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
        </style>
    </head>
    <body>

    <nav>
        <a href="/">Inicio</a>
        <a href="/metodologia">Metodología</a>
        <a href="/arquitectura-datalake">Data Lake</a>
        <a href="/arquitectura-cloud">Arquitectura Cloud</a>
        <a href="/modelo-ml">Modelo ML</a>
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


# =============================
# Páginas
# =============================

@app.get("/", response_class=HTMLResponse)
def inicio():
    content = """
    <div class="card">
        <h2>Visión General</h2>
        <p>
        Plataforma integral para detección de anomalías basada en arquitectura moderna:
        Data Lake + Machine Learning + API + BI.
        </p>
    </div>
    """
    return layout("Plataforma de Detección de Anomalías", content)


@app.get("/metodologia", response_class=HTMLResponse)
def metodologia():
    content = """
    <div class="card">
        <h2>Metodología CRISP-DM</h2>
        <ul>
            <li>Identificación de necesidades del negocio</li>
            <li>Estudio y comprensión de datos</li>
            <li>Transformación y EDA</li>
            <li>Modelado</li>
            <li>Evaluación</li>
            <li>Despliegue</li>
        </ul>
        <p>Aplicación práctica sobre dataset transaccional bancario.</p>
    </div>
    """
    return layout("Metodología CRISP-DM", content)


@app.get("/arquitectura-datalake", response_class=HTMLResponse)
def datalake():
    content = """
    <div class="card">
        <h2>Arquitectura Bronze – Silver – Gold</h2>
        <p>
        Se implementó modelo conceptual Delta Lake:
        </p>
        <ul>
            <li>Bronze: Datos crudos</li>
            <li>Silver: Datos transformados y limpios</li>
            <li>Gold: Agregaciones para negocio</li>
        </ul>
        <img src="/static/delta_lake.png">
    </div>
    """
    return layout("Arquitectura Data Lake", content)


@app.get("/arquitectura-cloud", response_class=HTMLResponse)
def cloud():
    content = """
    <div class="card">
        <h2>Arquitectura Cloud (Azure Stack)</h2>
        <p>
        Arquitectura moderna:
        Ingesta → Data Lake → Procesamiento → ML → API → BI
        </p>
        <img src="/static/azure_arch.png">
    </div>
    """
    return layout("Arquitectura Cloud", content)


@app.get("/modelo-ml", response_class=HTMLResponse)
def modelo():
    content = """
    <div class="card">
        <h2>Modelo de Detección de Anomalías</h2>
        <ul>
            <li>Isolation Forest</li>
            <li>Local Outlier Factor</li>
            <li>One-Class SVM</li>
            <li>Elliptic Envelope</li>
            <li>PCA (reducción dimensional)</li>
        </ul>
        <p>
        Se construyó un ensemble score para robustecer la detección.
        </p>
    </div>
    """
    return layout("Modelo Machine Learning", content)


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    content = """
    <div class="card">
        <h2>Dashboard Power BI</h2>
        <p>
        Visualización estratégica conectada a la API.
        </p>
        <a href="https://app.powerbi.com/groups/me/reports/aa89ddd4-4770-4458-824a-9ea9508fc87b"
           target="_blank"
           style="background:#D71920;color:white;padding:12px 20px;border-radius:8px;text-decoration:none;">
           Ver Dashboard
        </a>
    </div>
    """
    return layout("Visualización BI", content)