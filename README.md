# Avanti Buche — AI Engineer Portfolio

A cozy, interactive portfolio website built with **Streamlit**, inspired by the warm aesthetic of immersive room-based web experiences. Features a real photograph background, parallax mouse effect, floating butterflies, fireflies, piano background music, and a frosted-glass UI system.

---

## Live Demo

Deployed on Streamlit Cloud → [avantibuche.streamlit.app](https://avantibuche.streamlit.app/)

---

## Features

- **Cozy room background** with cursor-driven parallax effect — the room shifts as you move your mouse
- **Hotspot diamonds** placed on the room image — hover to preview, click to open section panels
- **Zoom on hover** — the room subtly zooms in when your cursor hits a hotspot
- **Frosted glass UI** — all panels, cards, and modals use dark semi-transparent blur
- **Day / Night toggle** — dims the room to a warm dark tone
- **Piano background music** — Enter with sound or silently; ♪ button toggles
- **Floating butterflies** — 4 species with realistic wings, veins, and antennae drawn on canvas
- **Fireflies** — soft glowing particles drifting across the scene
- **Cursor tooltip** — follows your cursor near hotspots with contextual labels
- **Hotspot preview cards** — peek card appears on hover before clicking
- **Smooth panel transitions** — content fades in each time a section opens
- **Mobile responsive** — nav and panels adapt to small screens
- **Image fallback** — warm gradient shown if background photo fails to load
- **Favicon** — ✨ emoji icon in the browser tab
- **Footer credit** — appears after entering the site

---

## Sections

| Section | Content |
|---|---|
| About | Summary, expertise tags, skill bars, education |
| Experience | Analyst role at Zothenix — themed responsibility clusters |
| Projects | AI Marketing Agency, Vedic Astrology RAG, Wheels.ai MaaS, CRM Dashboard, Prophet Forecasting |
| Contact | Email, LinkedIn, GitHub |

---

## Tech Stack

- **Python** + **Streamlit** — app shell and asset injection
- **HTML / CSS / JavaScript** — full custom UI rendered inside a Streamlit iframe
- **Canvas API** — butterflies, fireflies, parallax layer
- **Lora + Playfair Display** — Google Fonts (serif, italic)
- **Base64 encoding** — image and audio embedded directly in HTML for Streamlit Cloud compatibility

---

## Project Structure

```
app.py            # Streamlit entry point — encodes assets, injects into HTML
portfolio.html    # Full standalone HTML/CSS/JS portfolio
cozy_room.jpg     # Background room photograph
music.mp3         # Piano background music (Married Life)
requirements.txt  # Python dependencies
```

---

## Local Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

---

## Deploy to Streamlit Cloud

1. Pushed all files to a GitHub repo:
```bash
git add app.py portfolio.html requirements.txt cozy_room.jpg music.mp3
git commit -m "portfolio"
git push
```

2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set main file to `app.py`
5. Deploy

The image and music are base64-encoded at runtime from the repo files — no external hosting needed.

---

*Built with ✨ by Avanti Buche*
