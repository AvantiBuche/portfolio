import streamlit as st
import streamlit.components.v1 as components
import base64, os

st.set_page_config(
    page_title="Avanti Buche | AI Engineer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header, .stDeployButton,
[data-testid="collapsedControl"],
section[data-testid="stSidebar"] { display: none !important; }

/* zero out all streamlit padding/margins */
.block-container,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="stVerticalBlock"] {
  padding: 0 !important;
  margin: 0 !important;
  max-width: 100% !important;
  gap: 0 !important;
}

html, body, .stApp {
  margin: 0 !important;
  padding: 0 !important;
  background: #1a1208 !important;
  overflow: hidden !important;
  height: 100vh !important;
  width: 100vw !important;
}

/* make the iframe fill the full viewport */
iframe {
  border: none !important;
  display: block !important;
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
}
</style>
""", unsafe_allow_html=True)

# encode background image
bg_data_uri = ""
for fname in ["cozy_room.jpg", "cozy_room.jpeg", "cozy_room.png", "cozy_room.webp"]:
    if os.path.exists(fname):
        mime = "image/" + fname.split(".")[-1].replace("jpg", "jpeg")
        with open(fname, "rb") as f:
            bg_data_uri = f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"
        break

with open("portfolio.html", "r") as f:
    html = f.read()

html = html.replace("__BG_IMAGE__", bg_data_uri)

# encode music
music_data_uri = ""
if os.path.exists("music.mp3"):
    with open("music.mp3", "rb") as f:
        music_data_uri = f"data:audio/mpeg;base64,{base64.b64encode(f.read()).decode()}"

html = html.replace("__MUSIC__", music_data_uri)

# height=10000 is just a large placeholder; CSS `position:fixed` overrides it
components.html(html, height=10000, scrolling=False)
