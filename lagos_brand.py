# =============================================================================
# Lagos NCD Thesis — Shared CSS for Streamlit Dashboards (Premium UI v2)
# =============================================================================
# Brand palette:
#   Nigeria green:     #008751
#   Lagos teal-blue:   #00897B
#   Warm gold:         #F9A825
#   Dark slate:        #1A1A2E
#   Light grey:        #F5F7FA
#   White:             #FFFFFF
# =============================================================================

LAGOS_BRAND_CSS = """
<style>
/* ====== Root variables ====== */
:root {
    --nigeria-green: #008751;
    --nigeria-green-dark: #006B40;
    --lagos-teal: #00897B;
    --lagos-teal-dark: #00695C;
    --gold-accent: #F9A825;
    --dark-slate: #1A1A2E;
    --light-grey: #F5F7FA;
    --mid-grey: #495057;
    --white: #FFFFFF;
    --border-grey: #DEE2E6;
}

/* ====== Page background & font ====== */
.stApp {
    background-color: var(--white);
    color: var(--dark-slate);
    font-family: "Inter", "Segoe UI", -apple-system, BlinkMacSystemFont,
                 Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 0.92rem;
    line-height: 1.5;
}

/* ====== GLOBAL TEXT VISIBILITY ====== */
.stApp p, .stApp span, .stApp div, .stApp label,
.stMarkdown p, .stMarkdown span, .stMarkdown li,
.stSlider label, .stSelectbox label, .stRadio label,
.stNumberInput label, .stTextInput label, .stTextArea label {
    color: #1A1A2E !important;
}

/* ====== HEADER HIERARCHY ====== */
h1 {
    color: var(--dark-slate) !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    border-bottom: 3px solid var(--nigeria-green) !important;
    padding-bottom: 6px !important;
    margin-top: 0 !important;
    margin-bottom: 12px !important;
    letter-spacing: -0.5px !important;
}

h2 {
    color: var(--lagos-teal-dark) !important;
    font-size: 1.3rem !important;
    font-weight: 600 !important;
    margin-top: 16px !important;
    margin-bottom: 8px !important;
    letter-spacing: -0.3px !important;
}

h3 {
    color: var(--dark-slate) !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    margin-top: 12px !important;
    margin-bottom: 6px !important;
}

h4 {
    color: var(--mid-grey) !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    margin-top: 10px !important;
    margin-bottom: 4px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.3px !important;
}

/* ====== REDUCE VERTICAL SPACING ====== */
.stMarkdown, .stMetric, .stDataFrame, .stPlotlyChart {
    margin-bottom: 8px !important;
}

.stMarkdown > div > p {
    margin-bottom: 6px !important;
    line-height: 1.45 !important;
}

/* Reduce Streamlit's default block spacing */
.stBlock {
    margin-bottom: 4px !important;
}

/* ====== SIDEBAR ====== */
section[data-testid="stSidebar"] {
    background-color: var(--light-grey) !important;
    border-right: 3px solid var(--nigeria-green) !important;
    min-width: 300px !important;
}

section[data-testid="stSidebar"] .stMarkdown h1 {
    color: var(--nigeria-green) !important;
    border-bottom: none !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.3px !important;
    margin-bottom: 4px !important;
}

section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stCaption {
    color: #333333 !important;
    font-size: 0.78rem !important;
    margin-bottom: 2px !important;
    line-height: 1.3 !important;
}

/* ====== INPUT WIDGETS — WHITE BACKGROUND, DARK TEXT ====== */
/* Selectbox */
.stSelectbox > div > div > div {
    background-color: var(--white) !important;
    color: var(--dark-slate) !important;
    border: 1px solid var(--border-grey) !important;
    border-radius: 6px !important;
}

.stSelectbox > div > div > div > div {
    color: var(--dark-slate) !important;
}

/* Number input */
.stNumberInput > div > div > input {
    background-color: var(--white) !important;
    color: var(--dark-slate) !important;
    border: 1px solid var(--border-grey) !important;
    border-radius: 6px !important;
}

/* Text input */
.stTextInput > div > div > input {
    background-color: var(--white) !important;
    color: var(--dark-slate) !important;
    border: 1px solid var(--border-grey) !important;
    border-radius: 6px !important;
}

/* Focus states — green border */
.stSelectbox > div > div:focus-within,
.stNumberInput > div > div:focus-within > input,
.stTextInput > div > div:focus-within > input {
    border-color: var(--nigeria-green) !important;
    box-shadow: 0 0 0 2px rgba(0, 135, 81, 0.15) !important;
}

/* ====== SLIDERS — green track, dark labels ====== */
.stSlider label {
    color: var(--dark-slate) !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
}

.stSlider [data-baseweb="slider"] {
    margin-top: 4px !important;
}

.stSlider .st-b7,
.stSlider [data-baseweb="slider"] span {
    color: var(--dark-slate) !important;
    font-size: 0.8rem !important;
}

/* ====== RADIO BUTTONS — dark text ====== */
.stRadio label, .stRadio label span {
    color: var(--dark-slate) !important;
    font-size: 0.88rem !important;
}

.stRadio [data-checked="true"] {
    background-color: var(--nigeria-green) !important;
    border-color: var(--nigeria-green) !important;
}

/* ====== BUTTONS ====== */
.stButton > button {
    background-color: var(--nigeria-green) !important;
    color: var(--white) !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 500 !important;
    padding: 6px 16px !important;
    transition: background-color 0.2s !important;
}

.stButton > button:hover {
    background-color: var(--nigeria-green-dark) !important;
}

/* ====== METRIC CARDS ====== */
[data-testid="stMetric"] {
    background-color: var(--light-grey) !important;
    border: 1px solid var(--border-grey) !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
    overflow: visible !important;
}

[data-testid="stMetric"] label {
    color: #333333 !important;
    font-size: 0.7rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.3px !important;
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.15 !important;
    margin-bottom: 2px !important;
    display: block !important;
}

[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    color: var(--dark-slate) !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.1 !important;
}

[data-testid="stMetric"] [data-testid="stMetricDelta"] {
    font-size: 0.68rem !important;
    color: #444444 !important;
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.15 !important;
    margin-top: 1px !important;
}

/* ====== DATAFRAMES ====== */
.stDataFrame {
    border: 1px solid var(--border-grey) !important;
    border-radius: 8px !important;
    overflow: hidden !important;
}

.stDataFrame thead th {
    background-color: var(--nigeria-green) !important;
    color: var(--white) !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.3px !important;
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.2 !important;
    padding: 6px 6px !important;
}

.stDataFrame tbody td {
    white-space: normal !important;
    word-break: break-word !important;
    font-size: 0.8rem !important;
    padding: 4px 6px !important;
    color: var(--dark-slate) !important;
    background-color: var(--white) !important;
}

.stDataFrame tbody tr:nth-child(even) td {
    background-color: var(--light-grey) !important;
}

/* ====== EXPANDERS ====== */
.streamlit-expanderHeader {
    background-color: var(--light-grey) !important;
    border-left: 3px solid var(--nigeria-green) !important;
    font-weight: 600 !important;
    color: var(--dark-slate) !important;
    font-size: 0.9rem !important;
}

/* ====== CAPTIONS ====== */
.stCaption {
    color: #555555 !important;
    font-size: 0.8rem !important;
    font-style: italic !important;
    margin-top: 2px !important;
}

/* ====== ALERT BOXES ====== */
.stAlert {
    border-radius: 6px !important;
    border-left: 4px solid !important;
    padding: 8px 12px !important;
    margin-bottom: 8px !important;
}

.stAlert-success { border-left-color: var(--nigeria-green) !important; }
.stAlert-warning { border-left-color: var(--gold-accent) !important; }
.stAlert-error   { border-left-color: #C62828 !important; }

/* ====== BRAND HEADER BAR ====== */
.lagos-brand-bar {
    background: linear-gradient(90deg, var(--nigeria-green) 0%, var(--lagos-teal) 100%);
    color: var(--white);
    padding: 10px 18px;
    border-radius: 8px;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.lagos-brand-bar h2 {
    color: var(--white) !important;
    margin: 0 !important;
    font-size: 1.2rem !important;
    font-weight: 600 !important;
    border-bottom: none !important;
}

.lagos-brand-bar .brand-meta {
    font-size: 0.78rem;
    opacity: 0.92;
    text-align: right;
    color: var(--white) !important;
}

/* ====== FOOTER ====== */
.lagos-footer {
    border-top: 2px solid var(--nigeria-green);
    padding-top: 8px;
    margin-top: 24px;
    color: #555555;
    font-size: 0.8rem;
    text-align: center;
}

.lagos-footer strong {
    color: var(--dark-slate);
}

/* ====== PLOTLY CHART CONTAINERS ====== */
.stPlotlyChart {
    border: 1px solid var(--border-grey) !important;
    border-radius: 8px !important;
    padding: 4px !important;
    background-color: var(--white) !important;
    margin-bottom: 6px !important;
}

/* ====== HIDE STREAMLIT CHROME ====== */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

/* ====== SCROLLBAR ====== */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--light-grey); }
::-webkit-scrollbar-thumb { background: var(--nigeria-green); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--nigeria-green-dark); }

/* ====== BULLET LISTS ====== */
.stMarkdown ul li {
    margin-bottom: 3px !important;
    line-height: 1.4 !important;
}

.stMarkdown ol li {
    margin-bottom: 3px !important;
    line-height: 1.4 !important;
}

/* =====% REDUCE SECTION DIVIDER SPACING ===% */
hr {
    margin-top: 8px !important;
    margin-bottom: 8px !important;
    border: none !important;
    border-top: 1px solid var(--border-grey) !important;
}

/* ====== HORIZONTAL RULES (st.markdown("---")) ====== */
.stMarkdown hr {
    margin-top: 8px !important;
    margin-bottom: 8px !important;
}
</style>
"""


def brand_header(title: str, subtitle: str = ""):
    """Returns HTML for a branded header bar with Nigeria green → Lagos teal gradient."""
    meta_html = f'<div class="brand-meta">{subtitle}</div>' if subtitle else ''
    return f"""
    <div class="lagos-brand-bar">
        <h2>{title}</h2>
        {meta_html}
    </div>
    """


def footer():
    """Returns HTML for a branded footer."""
    return """
    <div class="lagos-footer">
        <strong>Project Owner:</strong> Oghenewoke Atariata
    </div>
    """


def gis_digital_lock_banner():
    """Returns empty string (removed dark banner below overview)."""
    return ""

def data_integrity_badge():
    """Returns empty string."""
    return ""

import streamlit.components.v1 as components

def render_app_header(title: str = "Lagos NCD Policy Simulator",
                      subtitle: str = "Model A — Bayesian Hierarchical Poisson & Spatial Analytics"):
    """
    Renders an ultra-premium header with a live-ticking digital clock (WAT / GMT+1).
    Uses Streamlit HTML component to guarantee 100% reliable real-time ticking.
    """
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{
            margin: 0; padding: 0; overflow: hidden;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: transparent;
        }}
        .header-card {{
            background: linear-gradient(135deg, #004D40 0%, #008751 60%, #004D40 100%);
            border-radius: 12px;
            padding: 14px 22px;
            box-shadow: 0 4px 16px rgba(0, 77, 64, 0.25);
            display: flex;
            align-items: center;
            justify-content: space-between;
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #FFFFFF;
        }}
        .title-text {{
            font-size: 21px;
            font-weight: 800;
            letter-spacing: -0.4px;
            color: #FFFFFF;
            margin: 0;
        }}
        .subtitle-text {{
            font-size: 13px;
            font-weight: 500;
            color: #E0F2F1;
            margin-top: 3px;
        }}
        .clock-pill {{
            background: rgba(0, 0, 0, 0.25);
            border: 1px solid rgba(0, 230, 118, 0.4);
            border-radius: 10px;
            padding: 8px 18px;
            text-align: center;
            box-shadow: inset 0 0 10px rgba(0, 230, 118, 0.15);
        }}
        .clock-digits {{
            font-family: 'Consolas', 'Menlo', 'Monaco', monospace;
            font-size: 1.7rem;
            font-weight: 800;
            color: #00E676;
            letter-spacing: 2px;
            line-height: 1;
            text-shadow: 0 0 10px rgba(0, 230, 118, 0.6);
        }}
        .clock-label {{
            font-size: 10px;
            font-weight: 700;
            color: #A7FFEB;
            letter-spacing: 1px;
            margin-top: 4px;
            text-transform: uppercase;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
        }}
        .pulse-dot {{
            width: 6px;
            height: 6px;
            background-color: #00E676;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 6px #00E676;
            animation: pulse 1.5s infinite;
        }}
        @keyframes pulse {{
            0% {{ transform: scale(0.95); opacity: 0.8; }}
            50% {{ transform: scale(1.25); opacity: 1; }}
            100% {{ transform: scale(0.95); opacity: 0.8; }}
        }}
    </style>
    </head>
    <body>
        <div class="header-card">
            <div>
                <div class="title-text">{title}</div>
                <div class="subtitle-text">{subtitle}</div>
            </div>
            <div class="clock-pill">
                <div id="live-clock" class="clock-digits">--:--:--</div>
                <div class="clock-label">
                    <span class="pulse-dot"></span> WAT (GMT+1) &bull; NIGERIA
                </div>
            </div>
        </div>
        <script>
            function updateClock() {{
                const now = new Date();
                const wat = new Date(now.getTime() + (1 * 60 * 60 * 1000));
                const hh = String(wat.getUTCHours()).padStart(2, '0');
                const mm = String(wat.getUTCMinutes()).padStart(2, '0');
                const ss = String(wat.getUTCSeconds()).padStart(2, '0');
                document.getElementById('live-clock').innerText = hh + ':' + mm + ':' + ss;
            }}
            updateClock();
            setInterval(updateClock, 1000);
        </script>
    </body>
    </html>
    """
    components.html(html_code, height=88)

def app_header(title: str = "Lagos NCD Policy Simulator",
               subtitle: str = "Bayesian Spatial Analytics (20 LGAs)"):
    """Legacy wrapper for app_header."""
    return ""


def expert_footer():
    """Returns HTML for a clean, high-contrast expert contact card for Lawrence Oladeji."""
    return """
<div style="
    background: #FFFFFF; border: 1px solid #DEE2E6; border-left: 5px solid #008751;
    border-radius: 10px; padding: 16px 20px; margin-top: 14px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06); text-align: center;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
">
    <div style="font-size: 0.75rem; font-weight: 700; letter-spacing: 1.5px;
                text-transform: uppercase; color: #008751; margin-bottom: 2px;">
        Lead ML &amp; Data Science Expert
    </div>
    <div style="font-size: 1.3rem; font-weight: 800; color: #1A1A2E; margin-bottom: 6px;">
        Lawrence Oladeji
    </div>
    <div style="display: flex; justify-content: center; align-items: center; gap: 20px; flex-wrap: wrap; font-size: 0.95rem; font-weight: 600;">
        <div>
            &#9993;&#65039; <a href="mailto:oladeji.lawrence@gmail.com" style="color: #008751 !important; text-decoration: underline; font-weight: 700;">oladeji.lawrence@gmail.com</a>
        </div>
    </div>
</div>
"""





# =============================================================================
# Brand color constants for Plotly charts
# =============================================================================
LAGOS_COLORS = {
    "nigeria_green": "#008751",
    "nigeria_green_dark": "#006B40",
    "lagos_teal": "#00897B",
    "lagos_teal_dark": "#00695C",
    "gold_accent": "#F9A825",
    "dark_slate": "#1A1A2E",
    "light_grey": "#F5F7FA",
    "mid_grey": "#495057",
    "white": "#FFFFFF",
    "htn": "#008751",
    "cvd": "#C62828",
    "dm": "#F9A825",
    "routine": "#008751",
    "monitor": "#F9A825",
    "refer": "#C62828",
}

DISEASE_COLORS = [LAGOS_COLORS["htn"], LAGOS_COLORS["cvd"], LAGOS_COLORS["dm"]]

TRIAGE_COLORS = {"ROUTINE": LAGOS_COLORS["routine"],
                 "MONITOR": LAGOS_COLORS["monitor"],
                 "REFER": LAGOS_COLORS["refer"]}
