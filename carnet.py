import streamlit as st
from datetime import date

st.set_page_config(page_title="Permiso de Copiloto", page_icon="🪪", layout="centered")

# ---------- CONFIG "DATOS" (edita aquí) ----------
NOMBRE = "CANYAGU"
APODO = "Copiloto Oficial"
ID_PERMISO = "BB-001"
FECHA_EMISION = date.today().strftime("%d/%m/%Y")
VALIDEZ = "ANUAL"
PUNTOS = "15/15"
PROGRESO = 100  # %
FOTO_URL = ""  # opcional: pega url a una foto (https://...) o déjalo vacío

HABILIDADES = [
    "DJ de carretera",
    "Navegación GPS",
    "Gestión de snacks",
    "Detector de radares (por presentimiento)",
    "Apoyo moral en atascos",
]

RESTRICCIONES = [
    "Si el conductor se equivoca: se perdona y se REDIRIGE con cariño"
]

FRASE = "Permiso concedido por el Ministerio de Viajes Soto."
# -----------------------------------------------

st.markdown(
    """
    <style>
      /* Móvil-first: ancho máximo, tipografía limpia */
      .wrap { max-width: 420px; margin: 0 auto; padding: 6px 0 18px 0; }
      .card {
        border-radius: 22px;
        padding: 18px 18px 14px 18px;
        background: linear-gradient(135deg, rgba(20,20,20,1) 0%, rgba(52,25,120,1) 45%, rgba(0,170,255,1) 100%);
        box-shadow: 0 16px 40px rgba(0,0,0,.35);
        color: white;
        position: relative;
        overflow: hidden;
      }
      .chip {
        width: 54px; height: 40px;
        border-radius: 10px;
        background: linear-gradient(145deg, rgba(255,215,0,.85), rgba(255,255,255,.15));
        border: 1px solid rgba(255,255,255,.25);
        box-shadow: inset 0 0 0 1px rgba(0,0,0,.2);
      }
      .title { font-size: 18px; letter-spacing: .12em; text-transform: uppercase; opacity: .95; }
      .subtitle { font-size: 12px; opacity: .85; margin-top: -2px; }
      .name { font-size: 26px; font-weight: 800; margin-top: 10px; line-height: 1.1; }
      .badge {
        display: inline-block;
        margin-top: 10px;
        padding: 6px 10px;
        border-radius: 999px;
        background: rgba(255,255,255,.14);
        border: 1px solid rgba(255,255,255,.18);
        font-size: 12px;
      }
      .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 14px; }
      .field {
        background: rgba(0,0,0,.18);
        border: 1px solid rgba(255,255,255,.14);
        border-radius: 14px;
        padding: 10px 10px;
      }
      .label { font-size: 10px; opacity: .78; text-transform: uppercase; letter-spacing: .08em; }
      .value { font-size: 14px; font-weight: 650; margin-top: 2px; }
      .bar {
        height: 10px;
        width: 100%;
        border-radius: 999px;
        background: rgba(255,255,255,.18);
        overflow: hidden;
        margin-top: 10px;
      }
      .bar > div {
        height: 100%;
        width: 100%;
        border-radius: 999px;
        background: linear-gradient(90deg, rgba(0,255,170,1), rgba(255,255,255,.9));
      }
      .section {
        margin-top: 14px;
        background: rgba(0,0,0,.18);
        border: 1px solid rgba(255,255,255,.14);
        border-radius: 16px;
        padding: 12px 12px 10px 12px;
      }
      .section h3 { margin: 0 0 6px 0; font-size: 13px; letter-spacing: .08em; text-transform: uppercase; opacity: .9; }
      ul { margin: 6px 0 0 18px; padding: 0; }
      li { margin: 4px 0; font-size: 13px; }
      .footer {
        margin-top: 12px;
        font-size: 12px;
        opacity: .9;
      }
      .photo {
        width: 64px; height: 64px; border-radius: 18px;
        border: 1px solid rgba(255,255,255,.25);
        object-fit: cover;
        box-shadow: 0 10px 20px rgba(0,0,0,.25);
      }
      .toprow { display:flex; align-items:center; justify-content:space-between; gap: 10px; }
      .topright { display:flex; gap: 10px; align-items:center; }
      .watermark {
        position:absolute;
        right:-40px; top:30px;
        transform: rotate(18deg);
        font-size: 42px;
        opacity: .09;
        font-weight: 900;
        letter-spacing: .08em;
        user-select: none;
      }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="wrap">', unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="card">
      <div class="watermark">COPILOTO</div>
      <div class="toprow">
        <div>
          <div class="title">Permiso de Copiloto</div>
          <div class="subtitle">Documento oficialísimo • 100% válido en tu coche</div>
        </div>
        <div class="topright">
          <div class="chip"></div>
          {"<img class='photo' src='"+FOTO_URL+"'/>" if FOTO_URL else ""}
        </div>
      </div>

      <div class="name">{NOMBRE}</div>
      <div class="badge">🪪 {APODO} • ID {ID_PERMISO}</div>

      <div class="grid">
        <div class="field">
          <div class="label">Clase</div>
          <div class="value">COPILOTO (Premium)</div>
        </div>
        <div class="field">
          <div class="label">Puntos</div>
          <div class="value">{PUNTOS} ✅</div>
        </div>
        <div class="field">
          <div class="label">Emisión</div>
          <div class="value">{FECHA_EMISION}</div>
        </div>
        <div class="field">
          <div class="label">Validez</div>
          <div class="value">{VALIDEZ}</div>
        </div>
      </div>

      <div class="label" style="margin-top:12px;">Nivel de copiloto</div>
      <div class="bar"><div></div></div>
      <div class="value" style="margin-top:6px;">{PROGRESO}% completado 🏁</div>

      <div class="section">
        <h3>Habilidades desbloqueadas</h3>
        <ul>
          {''.join([f"<li>{h}</li>" for h in HABILIDADES])}
        </ul>
      </div>

      <div class="section">
        <h3>Restricciones (muy serias)</h3>
        <ul>
          {''.join([f"<li>{r}</li>" for r in RESTRICCIONES])}
        </ul>
      </div>

      <div class="footer">💬 {FRASE}</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption("Tip: guarda esta web en la pantalla de inicio para que parezca una app.")
st.markdown("</div>", unsafe_allow_html=True)