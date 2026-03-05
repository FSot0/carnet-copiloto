import streamlit as st
from datetime import date
import time

st.set_page_config(page_title="Permiso de Copiloto", page_icon="🪪", layout="centered")

# ---------- DATOS (edita aquí) ----------
NOMBRE = "CANYAGU"
APODO = "Copilota Oficial"
ID_PERMISO = "BB-001"
LICENCIA = "CP-2026-001"
FECHA_EMISION = "08/03/2026" 
VALIDEZ = "ANUAL"
PUNTOS = "15/15"
PROGRESO = 100  # %

# OJO: el enlace que has pasado es un ALBUM de Imgur.
# Streamlit suele necesitar un enlace directo a la imagen (acabe en .jpg/.png).
# Si no se ve, abre el álbum, abre la foto concreta y copia el "Direct link" (i.imgur.com/...jpg).
FOTO_URL = "https://i.imgur.com/jyJdpBB.jpeg"

HABILIDADES = [
    "DJ de carretera",
    "Navegación GPS",
    "Gestión de snacks",
    "Apoyo moral en atascos",
]

RESTRICCIONES = [
    "Si el conductor se equivoca: se perdona"
]

FRASE = "Permiso concedido por el Ministerio de Viajes y Risas."
# --------------------------------------


# ---------- Query params (compatibilidad) ----------
def get_query_params():
    # Streamlit nuevo: st.query_params
    try:
        qp = dict(st.query_params)
        # st.query_params puede devolver valores tipo list/str según versión
        return {k: (v[0] if isinstance(v, list) and v else v) for k, v in qp.items()}
    except Exception:
        try:
            qp = st.experimental_get_query_params()
            return {k: (v[0] if isinstance(v, list) and v else v) for k, v in qp.items()}
        except Exception:
            return {}

params = get_query_params()

# Sorpresa al venir desde NFC: añade ?from=nfc a la URL grabada en la tarjeta
if params.get("from", "").lower() == "nfc":
    st.balloons()

# ---------- CSS (móvil-first) ----------
st.markdown(
    """
<style>
/* Móvil-first */
.wrap { max-width: 420px; margin: 0 auto; padding: 10px 10px 18px 10px; }

.card {
  width: 100%;
  border-radius: 22px;
  padding: 18px 18px 14px 18px;
  background: linear-gradient(135deg, rgba(20,20,20,1) 0%, rgba(52,25,120,1) 45%, rgba(0,170,255,1) 100%);
  box-shadow: 0 16px 40px rgba(0,0,0,.35);
  color: white;
  position: relative;
  overflow: hidden;
}

.title { font-size: 16px; letter-spacing: .14em; text-transform: uppercase; opacity: .95; }
.subtitle { font-size: 12px; opacity: .85; margin-top: 4px; max-width: 260px; }

.toprow { display:flex; align-items:flex-start; justify-content:space-between; gap: 12px; }
.topright { display:flex; gap: 10px; align-items:flex-start; }

.chip {
  width: 54px; height: 40px;
  border-radius: 10px;
  background: linear-gradient(145deg, rgba(255,215,0,.85), rgba(255,255,255,.15));
  border: 1px solid rgba(255,255,255,.25);
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.2);
}

.photo {
  width: 70px; height: 90px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,.25);
  object-fit: cover;
  box-shadow: 0 10px 20px rgba(0,0,0,.25);
  background: rgba(0,0,0,.15);
}

.name { font-size: 26px; font-weight: 850; margin-top: 12px; line-height: 1.1; }
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
.value { font-size: 14px; font-weight: 700; margin-top: 2px; }

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

.footer { margin-top: 12px; font-size: 12px; opacity: .9; }

.watermark {
  position:absolute;
  right:-55px; top:30px;
  transform: rotate(18deg);
  font-size: 44px;
  opacity: .10;
  font-weight: 900;
  letter-spacing: .08em;
  user-select: none;
}

/* “Holograma” */
.holo {
  position:absolute;
  bottom: 12px;
  right: 14px;
  width: 64px;
  height: 64px;
  border-radius: 16px;
  background: conic-gradient(from 180deg, rgba(255,255,255,.10), rgba(0,255,170,.18), rgba(255,255,255,.10));
  border: 1px solid rgba(255,255,255,.18);
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.12);
  display:flex;
  align-items:center;
  justify-content:center;
  font-size: 28px;
  opacity: .65;
}

/* Loader “escaneo” */
.scanbox {
  border-radius: 18px;
  padding: 14px;
  background: rgba(0,0,0,.06);
  border: 1px solid rgba(0,0,0,.06);
}
</style>
""",
    unsafe_allow_html=True
)

# ---------- Animación de “escaneo” ----------
placeholder = st.empty()

with placeholder.container():
    st.markdown('<div class="wrap">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="scanbox">
          <div style="font-weight:800; font-size:16px;">Verificando licencia…</div>
          <div style="opacity:.75; margin-top:4px; font-size:12px;">Escaneo NFC en curso</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(0, text="Iniciando…")

time.sleep(0.35)
with placeholder.container():
    st.markdown('<div class="wrap">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="scanbox">
          <div style="font-weight:800; font-size:16px;">Verificando licencia…</div>
          <div style="opacity:.75; margin-top:4px; font-size:12px;">Comprobando puntos y clase</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(60, text="Validando…")

time.sleep(0.45)
with placeholder.container():
    st.markdown('<div class="wrap">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="scanbox">
          <div style="font-weight:800; font-size:16px;">Verificando licencia…</div>
          <div style="opacity:.75; margin-top:4px; font-size:12px;">Autorización concedida ✅</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(100, text="Listo")

time.sleep(0.30)

# ---------- Render “carnet” ----------
photo_html = ""
if FOTO_URL:
    photo_html = f"<img class='photo' src='{FOTO_URL}' alt='Foto'/>"

card_html = f"""
<div class="wrap">
  <div class="card">
    <div class="watermark">COPILOTO</div>

    <div class="toprow">
      <div>
        <div class="title">Permiso de Copiloto</div>
        <div class="subtitle">Documento oficialísimo • 100% válido en tu coche</div>
      </div>
      <div class="topright">
        <div class="chip"></div>
        {photo_html}
      </div>
    </div>

    <div class="name">{NOMBRE}</div>
    <div class="badge">🪪 {APODO} • ID {ID_PERMISO} • LIC {LICENCIA}</div>

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

    <div class="holo">🚗</div>
  </div>
</div>
"""

placeholder.empty()
st.markdown(card_html, unsafe_allow_html=True)
