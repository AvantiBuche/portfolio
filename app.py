import streamlit as st

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Avanti Buche | AI Engineer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────
# GLOBAL STYLES
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap');

/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.stApp > header { display: none; }
.stDeployButton { display: none; }
section[data-testid="stSidebar"] { display: none; }

/* ── Design Tokens ── */
:root {
  --bg:      #060912;
  --bg2:     #0c1018;
  --bg3:     #111722;
  --cyan:    #22d3ee;
  --violet:  #a78bfa;
  --gold:    #fbbf24;
  --rose:    #fb7185;
  --green:   #34d399;
  --text:    #e2e8f0;
  --muted:   #94a3b8;
  --border:  rgba(255,255,255,0.07);
  --border2: rgba(255,255,255,0.12);
}

/* ── App Shell ── */
.stApp {
  background: var(--bg);
  font-family: 'DM Sans', system-ui, sans-serif;
  color: var(--text);
}
.main .block-container {
  padding: 0 !important;
  max-width: 100% !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 3px; }

/* ══════════════════════════════════════
   FLOATING NAV
══════════════════════════════════════ */
.fl-nav {
  position: fixed; top: 20px; left: 50%; transform: translateX(-50%);
  z-index: 9999;
  display: flex; align-items: center; gap: 4px;
  background: rgba(6,9,18,0.82);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid var(--border2);
  border-radius: 50px;
  padding: 6px 10px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.5);
}
.fl-nav a {
  padding: 6px 15px; border-radius: 50px;
  font-size: 0.78rem; font-weight: 500;
  color: var(--muted); text-decoration: none;
  transition: all 0.2s; white-space: nowrap;
  letter-spacing: 0.02em;
}
.fl-nav a:hover { color: #fff; background: rgba(255,255,255,0.07); }

/* ══════════════════════════════════════
   HERO
══════════════════════════════════════ */
.hero {
  position: relative;
  min-height: 100vh;
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center;
  padding: 8rem 1.5rem 5rem;
  overflow: hidden;
}

/* Mesh gradient */
.hero::before {
  content: '';
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 70% 55% at 25% 10%,  rgba(167,139,250,.13) 0%, transparent 60%),
    radial-gradient(ellipse 60% 45% at 78% 88%,  rgba(34,211,238,.09)  0%, transparent 60%),
    radial-gradient(ellipse 100% 70% at 50%  0%, #0e1230 0%, transparent 65%);
  pointer-events: none;
}
/* Dot grid */
.hero::after {
  content: '';
  position: absolute; inset: 0;
  background-image: radial-gradient(rgba(255,255,255,0.035) 1px, transparent 1px);
  background-size: 30px 30px;
  pointer-events: none;
}

.hero-inner { position: relative; z-index: 1; max-width: 800px; width: 100%; }

/* Animated status chip */
@keyframes pulse-dot {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.3; }
}
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(18px); }
  to   { opacity: 1; transform: translateY(0); }
}

.hero-chip {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(52,211,153,.08);
  border: 1px solid rgba(52,211,153,.22);
  color: var(--green); padding: 7px 18px;
  border-radius: 50px; font-size: 0.76rem;
  font-weight: 600; letter-spacing: 0.14em;
  text-transform: uppercase; margin-bottom: 2rem;
  animation: fadeUp .55s ease both;
}
.hero-chip-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--green);
  animation: pulse-dot 2s infinite;
}

.hero-name {
  font-family: 'Syne', sans-serif;
  font-size: clamp(3.4rem, 9vw, 6.8rem);
  font-weight: 800; line-height: 1.0;
  letter-spacing: -0.025em;
  background: linear-gradient(135deg, #ffffff 0%, #22d3ee 55%, #a78bfa 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 1.2rem;
  animation: fadeUp .6s .1s ease both;
}

.hero-tagline {
  font-family: 'Syne', sans-serif;
  font-size: clamp(1rem, 2.3vw, 1.3rem);
  font-weight: 600; color: var(--cyan);
  letter-spacing: 0.06em; margin-bottom: 1.5rem;
  animation: fadeUp .6s .18s ease both;
}

.hero-bio {
  font-size: 1.02rem; color: var(--muted);
  line-height: 1.85; max-width: 620px;
  margin: 0 auto 2.5rem;
  animation: fadeUp .6s .26s ease both;
}

.hero-actions {
  display: flex; gap: 12px; justify-content: center;
  flex-wrap: wrap; margin-bottom: 3.5rem;
  animation: fadeUp .6s .34s ease both;
}
.btn {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 12px 26px; border-radius: 10px;
  font-size: 0.88rem; font-weight: 600;
  text-decoration: none !important; transition: all 0.22s;
  letter-spacing: 0.01em;
}
.btn-primary {
  background: linear-gradient(135deg, var(--violet) 0%, var(--cyan) 100%);
  color: #07090f !important;
}
.btn-primary:hover {
  opacity: .88; transform: translateY(-2px);
  box-shadow: 0 8px 28px rgba(167,139,250,.35);
}
.btn-ghost {
  background: transparent; color: var(--text) !important;
  border: 1px solid var(--border2);
}
.btn-ghost:hover {
  border-color: var(--violet); transform: translateY(-2px);
  background: rgba(167,139,250,.06);
}

/* Stats strip */
.hero-stats {
  display: flex; gap: 3rem; justify-content: center;
  flex-wrap: wrap; padding-top: 2.5rem;
  border-top: 1px solid var(--border);
  animation: fadeUp .6s .42s ease both;
}
.h-stat { text-align: center; }
.h-stat-n {
  font-family: 'Syne', sans-serif;
  font-size: 2.3rem; font-weight: 800;
  background: linear-gradient(135deg, var(--cyan), var(--violet));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.h-stat-l {
  font-size: 0.72rem; color: var(--muted);
  text-transform: uppercase; letter-spacing: 0.14em; margin-top: 3px;
}

/* ══════════════════════════════════════
   SECTION HELPERS
══════════════════════════════════════ */
.sec           { padding: 5.5rem 1.5rem; max-width: 1100px; margin: 0 auto; }
.sec-alt       { padding: 5.5rem 1.5rem; background: var(--bg2); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.sec-alt-inner { max-width: 1100px; margin: 0 auto; }

.sec-eyebrow {
  font-size: 0.72rem; font-weight: 700;
  color: var(--cyan); text-transform: uppercase;
  letter-spacing: 0.22em; margin-bottom: 10px;
}
.sec-h {
  font-family: 'Syne', sans-serif;
  font-size: clamp(1.9rem, 3.5vw, 2.6rem);
  font-weight: 800; color: #fff; line-height: 1.12;
}
.sec-rule {
  width: 52px; height: 3px;
  background: linear-gradient(90deg, var(--violet), var(--cyan));
  border-radius: 100px; margin: 18px 0 42px;
}

/* ══════════════════════════════════════
   ABOUT STRIP (below hero)
══════════════════════════════════════ */
.about-strip {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1px; background: var(--border);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}
.about-cell {
  padding: 28px 32px;
  background: var(--bg);
  display: flex; flex-direction: column; gap: 6px;
}
.about-cell-label { font-size: 0.7rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.14em; }
.about-cell-value { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: #fff; }
.about-cell-sub   { font-size: 0.82rem; color: var(--muted); }

/* ══════════════════════════════════════
   SKILLS
══════════════════════════════════════ */
.sk-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(275px, 1fr));
  gap: 18px;
}
.sk-card {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 16px; padding: 24px 22px 20px;
  transition: border-color .25s, transform .25s;
}
.sk-card:hover { border-color: rgba(167,139,250,.38); transform: translateY(-4px); }
.sk-card-head {
  display: flex; align-items: center; gap: 8px;
  font-family: 'Syne', sans-serif; font-size: 0.82rem; font-weight: 700;
  color: var(--violet); text-transform: uppercase;
  letter-spacing: 0.1em; margin-bottom: 16px;
}
.sk-tags { display: flex; flex-wrap: wrap; gap: 7px; }
.sk-tag {
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,.07);
  color: var(--text); padding: 5px 11px; border-radius: 7px;
  font-size: 0.8rem; transition: all .2s; cursor: default;
}
.sk-tag:hover { background: rgba(34,211,238,.1); border-color: rgba(34,211,238,.3); color: var(--cyan); }

/* ══════════════════════════════════════
   TIMELINE
══════════════════════════════════════ */
.tl { position: relative; padding-left: 24px; }
.tl::before {
  content: ''; position: absolute;
  left: 4px; top: 8px; bottom: 0; width: 2px;
  background: linear-gradient(180deg, var(--violet) 0%, var(--cyan) 60%, transparent 100%);
  border-radius: 2px;
}
.tl-item { position: relative; padding: 0 0 48px 32px; }
.tl-dot {
  position: absolute; left: -20px; top: 5px;
  width: 14px; height: 14px; border-radius: 50%;
  background: var(--violet); border: 2.5px solid var(--bg2);
  box-shadow: 0 0 16px rgba(167,139,250,.55);
}
.tl-date   { font-size: 0.75rem; font-weight: 700; color: var(--cyan); letter-spacing: .07em; text-transform: uppercase; margin-bottom: 5px; }
.tl-co     { font-family: 'Syne', sans-serif; font-size: 1.15rem; font-weight: 800; color: #fff; margin-bottom: 3px; }
.tl-role   { font-size: 0.9rem; color: var(--gold); font-style: italic; margin-bottom: 14px; }
.tl-body   { background: var(--bg3); border: 1px solid var(--border); border-radius: 12px; padding: 16px 20px; }
.tl-li     { position: relative; padding-left: 16px; color: var(--muted); font-size: .875rem; line-height: 1.78; margin-bottom: 7px; }
.tl-li::before { content: '▹'; position: absolute; left: 0; color: var(--cyan); }
.tl-li:last-child { margin-bottom: 0; }

/* ══════════════════════════════════════
   PROJECTS
══════════════════════════════════════ */
.proj-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
}
.proj-card {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 16px; padding: 24px;
  position: relative; overflow: hidden;
  display: flex; flex-direction: column;
  transition: border-color .25s, transform .3s;
}
.proj-card:hover { border-color: rgba(34,211,238,.35); transform: translateY(-6px); }
.proj-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0;
  height: 2px; background: linear-gradient(90deg, var(--violet), var(--cyan));
}
.proj-card.ind::before { background: linear-gradient(90deg, var(--gold), var(--rose)); }

.proj-badge {
  display: inline-block;
  background: rgba(34,211,238,.08); border: 1px solid rgba(34,211,238,.18);
  color: var(--cyan); padding: 3px 10px;
  border-radius: 50px; font-size: 0.68rem;
  font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.12em; margin-bottom: 14px; align-self: flex-start;
}
.proj-card.ind .proj-badge {
  background: rgba(251,191,36,.08); border-color: rgba(251,191,36,.18); color: var(--gold);
}
.proj-title {
  font-family: 'Syne', sans-serif; font-size: 1.05rem; font-weight: 700;
  color: #fff; line-height: 1.3; margin-bottom: 10px;
}
.proj-desc { color: var(--muted); font-size: .86rem; line-height: 1.77; margin-bottom: 16px; flex: 1; }
.proj-stack { display: flex; flex-wrap: wrap; gap: 6px; margin-top: auto; }
.proj-tech {
  background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.07);
  color: var(--muted); padding: 3px 9px; border-radius: 5px;
  font-size: 0.73rem; font-family: monospace; letter-spacing: .02em;
}

/* ══════════════════════════════════════
   EDUCATION
══════════════════════════════════════ */
.edu-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 18px;
}
.edu-card {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 16px; padding: 26px;
  transition: border-color .25s, transform .25s;
}
.edu-card:hover { border-color: rgba(167,139,250,.3); transform: translateY(-3px); }
.edu-icon  { font-size: 2.2rem; margin-bottom: 14px; }
.edu-deg   { font-family: 'Syne', sans-serif; font-size: 1.02rem; font-weight: 700; color: #fff; margin-bottom: 5px; }
.edu-school { font-size: .84rem; color: var(--muted); margin-bottom: 5px; line-height: 1.5; }
.edu-yr    { font-size: .8rem; color: var(--cyan); font-weight: 700; }

/* ══════════════════════════════════════
   CERTIFICATIONS
══════════════════════════════════════ */
.cert-list { display: flex; flex-direction: column; gap: 12px; }
.cert-row {
  display: flex; align-items: center; gap: 16px;
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 12px; padding: 16px 20px; transition: border-color .25s, transform .25s;
}
.cert-row:hover { border-color: rgba(251,191,36,.3); transform: translateX(4px); }
.cert-ico { font-size: 1.6rem; flex-shrink: 0; }
.cert-n   { font-weight: 600; font-size: .92rem; color: var(--text); }
.cert-iss { font-size: .8rem; color: var(--muted); margin-top: 2px; }

/* ══════════════════════════════════════
   EXTRA INFO CARDS
══════════════════════════════════════ */
.info-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 14px; margin-top: 1.5rem;
}
.info-card {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 12px; padding: 18px 20px;
  display: flex; align-items: flex-start; gap: 12px;
}
.info-card-ico { font-size: 1.3rem; flex-shrink: 0; margin-top: 2px; }
.info-card-text { font-size: 0.875rem; color: var(--muted); line-height: 1.65; }

/* ══════════════════════════════════════
   CONTACT
══════════════════════════════════════ */
.contact-sec {
  padding: 7rem 1.5rem;
  text-align: center;
  background: linear-gradient(180deg, var(--bg2) 0%, var(--bg) 100%);
  border-top: 1px solid var(--border);
}
.contact-inner { max-width: 780px; margin: 0 auto; }
.contact-sub {
  color: var(--muted); font-size: 1.02rem; line-height: 1.8;
  margin: 1.2rem auto 3rem; max-width: 500px;
}
.contact-grid {
  display: flex; flex-wrap: wrap; gap: 14px; justify-content: center;
}
.c-card {
  display: flex; flex-direction: column; align-items: center; gap: 6px;
  background: rgba(255,255,255,.03); border: 1px solid var(--border);
  border-radius: 16px; padding: 22px 28px; min-width: 165px;
  text-decoration: none !important; transition: all .25s;
}
.c-card:hover {
  border-color: rgba(34,211,238,.35); transform: translateY(-4px);
  background: rgba(34,211,238,.04);
}
.c-ico  { font-size: 1.9rem; }
.c-lbl  { font-size: 0.67rem; color: var(--muted); text-transform: uppercase; letter-spacing: .14em; }
.c-val  { font-size: 0.85rem; color: var(--text); font-weight: 500; }

/* ══════════════════════════════════════
   FOOTER
══════════════════════════════════════ */
.ft {
  text-align: center; padding: 30px 20px;
  border-top: 1px solid var(--border);
  color: var(--muted); font-size: 0.78rem; letter-spacing: .03em;
}
.ft span { color: var(--rose); }
.ft a    { color: var(--cyan); text-decoration: none; }
.ft a:hover { text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# FLOATING NAVIGATION
# ─────────────────────────────────────────────────────────────
st.markdown("""
<nav class="fl-nav">
  <a href="#about">About</a>
  <a href="#skills">Skills</a>
  <a href="#experience">Experience</a>
  <a href="#projects">Projects</a>
  <a href="#education">Education</a>
  <a href="#contact">Contact</a>
</nav>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# ❶  HERO
# ─────────────────────────────────────────────────────────────
st.markdown("""
<section class="hero" id="about">
  <div class="hero-inner">

    <div class="hero-chip">
      <span class="hero-chip-dot"></span>
      Open to New Opportunities
    </div>

    <h1 class="hero-name">Avanti Buche</h1>
    <p class="hero-tagline">AI Engineer · Gen AI · RAG · Agentic Systems · Analytics</p>

    <p class="hero-bio">
      Building intelligent systems that turn raw data into real decisions.
      Passionate about LLMs, multi-agent architectures, and end-to-end AI
      engineering — from forecasting pipelines to autonomous marketing agents.
      Thrives at the intersection of AI research and practical implementation.
    </p>

    <div class="hero-actions">
      <a class="btn btn-primary" href="mailto:avibuche@gmail.com">✉&nbsp; Get in Touch</a>
      <a class="btn btn-ghost"   href="https://linkedin.com/in/avantibuche" target="_blank">🔗&nbsp; LinkedIn</a>
      <a class="btn btn-ghost"   href="https://github.com/avantibuche"      target="_blank">🐙&nbsp; GitHub</a>
    </div>

    <div class="hero-stats">
      <div class="h-stat">
        <div class="h-stat-n">7+</div>
        <div class="h-stat-l">Years Experience</div>
      </div>
      <div class="h-stat">
        <div class="h-stat-n">5</div>
        <div class="h-stat-l">AI Projects</div>
      </div>
      <div class="h-stat">
        <div class="h-stat-n">25+</div>
        <div class="h-stat-l">Technologies</div>
      </div>
      <div class="h-stat">
        <div class="h-stat-n">3</div>
        <div class="h-stat-l">Certifications</div>
      </div>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# ABOUT STRIP
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="about-strip">
  <div class="about-cell">
    <span class="about-cell-label">Based in</span>
    <span class="about-cell-value">India</span>
    <span class="about-cell-sub">Kolkata / Bangalore / Remote</span>
  </div>
  <div class="about-cell">
    <span class="about-cell-label">Specialisation</span>
    <span class="about-cell-value">AI / LLM Engineering</span>
    <span class="about-cell-sub">RAG · Agentic AI · Analytics</span>
  </div>
  <div class="about-cell">
    <span class="about-cell-label">Education</span>
    <span class="about-cell-value">MCA · B.Sc CS & Maths</span>
    <span class="about-cell-sub">RTMNU Nagpur University</span>
  </div>
  <div class="about-cell">
    <span class="about-cell-label">Primary Language</span>
    <span class="about-cell-value">Python</span>
    <span class="about-cell-sub">LangChain · Agno · CrewAI</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# ❷  SKILLS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="sec-alt" id="skills">
  <div class="sec-alt-inner">
    <p class="sec-eyebrow">What I Work With</p>
    <h2 class="sec-h">Technical Skills</h2>
    <div class="sec-rule"></div>

    <div class="sk-grid">

      <div class="sk-card">
        <div class="sk-card-head">🧠 Core AI Expertise</div>
        <div class="sk-tags">
          <span class="sk-tag">Large Language Models</span>
          <span class="sk-tag">Generative AI</span>
          <span class="sk-tag">RAG</span>
          <span class="sk-tag">Agentic AI</span>
          <span class="sk-tag">Multi-Agent Systems</span>
          <span class="sk-tag">Prompt Engineering</span>
        </div>
      </div>

      <div class="sk-card">
        <div class="sk-card-head">📐 ML & Data Science</div>
        <div class="sk-tags">
          <span class="sk-tag">Machine Learning</span>
          <span class="sk-tag">Predictive Modeling</span>
          <span class="sk-tag">Analytics</span>
          <span class="sk-tag">Forecasting (Prophet)</span>
          <span class="sk-tag">Data Cleaning</span>
          <span class="sk-tag">CRM Analytics</span>
        </div>
      </div>

      <div class="sk-card">
        <div class="sk-card-head">🧰 Frameworks & Libraries</div>
        <div class="sk-tags">
          <span class="sk-tag">LangChain</span>
          <span class="sk-tag">CrewAI</span>
          <span class="sk-tag">Agno</span>
          <span class="sk-tag">TensorFlow</span>
          <span class="sk-tag">PyTorch</span>
          <span class="sk-tag">SciKit-Learn</span>
          <span class="sk-tag">Keras</span>
        </div>
      </div>

      <div class="sk-card">
        <div class="sk-card-head">📊 Data & Visualization</div>
        <div class="sk-tags">
          <span class="sk-tag">Pandas</span>
          <span class="sk-tag">NumPy</span>
          <span class="sk-tag">Matplotlib</span>
          <span class="sk-tag">Seaborn</span>
          <span class="sk-tag">Google Analytics</span>
          <span class="sk-tag">HubSpot</span>
          <span class="sk-tag">Zoho CRM</span>
        </div>
      </div>

      <div class="sk-card">
        <div class="sk-card-head">🛠 Tools & Infrastructure</div>
        <div class="sk-tags">
          <span class="sk-tag">Python</span>
          <span class="sk-tag">Docker</span>
          <span class="sk-tag">Streamlit</span>
          <span class="sk-tag">LanceDB</span>
          <span class="sk-tag">Ollama</span>
          <span class="sk-tag">PyCharm</span>
          <span class="sk-tag">Git</span>
        </div>
      </div>

      <div class="sk-card">
        <div class="sk-card-head">🤖 AI IDEs & Vibe Coding</div>
        <div class="sk-tags">
          <span class="sk-tag">Kiro</span>
          <span class="sk-tag">Cursor</span>
          <span class="sk-tag">Postman</span>
          <span class="sk-tag">Llama 3.1 / 3.2</span>
          <span class="sk-tag">Open-Source LLMs</span>
          <span class="sk-tag">Model Serving</span>
        </div>
      </div>

    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# ❸  EXPERIENCE
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="sec" id="experience">
  <p class="sec-eyebrow">Professional Journey</p>
  <h2 class="sec-h">Experience</h2>
  <div class="sec-rule"></div>

  <div class="tl">

    <!-- Job 1 -->
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-date">March 2026 – June 2026</div>
      <div class="tl-co">Aptpath, Bangalore &nbsp;·&nbsp; Client: Wheels.ai</div>
      <div class="tl-role">AI Intern – Vibe Coder</div>
      <div class="tl-body">
        <div class="tl-li">Contributed to Wheels.ai MaaS (Model-as-a-Service) platform development using AI-assisted software engineering workflows.</div>
        <div class="tl-li">Worked with AI IDEs and coding agents — Kiro, Cursor, Postman, and open-source LLMs — for rapid module implementation with minimal hand-written code.</div>
        <div class="tl-li">Created PRISM documentation, architectural prompts, and workflow designs for AI-assisted development pipelines.</div>
        <div class="tl-li">Containerized AI inference models using Docker for scalable, production-grade deployment.</div>
      </div>
    </div>

    <!-- Job 2 -->
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-date">June 2017 – October 2022</div>
      <div class="tl-co">Zothenix Innovations Pvt Ltd (formerly TechGenyz Software Pvt Ltd), Kolkata</div>
      <div class="tl-role">Analyst</div>
      <div class="tl-body">
        <div class="tl-li">Built marketing and sales analytics dashboards using CRM, HubSpot campaign data, and Google Analytics — enabling data-driven stakeholder decisions.</div>
        <div class="tl-li">Integrated and consolidated CRM data from Zoho CRM and HubSpot; developed dashboards for lead conversion, campaign ROI, and revenue trends.</div>
        <div class="tl-li">Built forecasting models using Facebook Prophet to predict monthly sales and website traffic with seasonality adjustments.</div>
        <div class="tl-li">Collaborated with marketing, sales, and product teams to define KPIs and deliver actionable insights that guided strategic planning.</div>
        <div class="tl-li">Improved conversion rates by <strong>20%</strong> through optimised campaign strategies, enhanced customer engagement, and targeted outreach.</div>
      </div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# ❹  PROJECTS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="sec-alt" id="projects">
  <div class="sec-alt-inner">
    <p class="sec-eyebrow">What I've Built</p>
    <h2 class="sec-h">Projects</h2>
    <div class="sec-rule"></div>

    <div class="proj-grid">

      <!-- Personal 1 -->
      <div class="proj-card">
        <div class="proj-badge">✦ Personal Project</div>
        <div class="proj-title">AI Marketing Agency – Multi-Agent Automation System</div>
        <div class="proj-desc">
          Designed a multi-agent AI platform where specialised agents collaborate autonomously —
          handling market research, audience analysis, content creation, SEO optimisation, social
          media strategy, and image prompt generation in one unified pipeline.
        </div>
        <div class="proj-stack">
          <span class="proj-tech">Agno</span>
          <span class="proj-tech">Ollama</span>
          <span class="proj-tech">Streamlit</span>
          <span class="proj-tech">Llama 3.1</span>
          <span class="proj-tech">DuckDuckGo API</span>
          <span class="proj-tech">Multi-Agent</span>
        </div>
      </div>

      <!-- Personal 2 -->
      <div class="proj-card">
        <div class="proj-badge">✦ Personal Project</div>
        <div class="proj-title">Vedic Astrology Expert – RAG-Based AI Assistant</div>
        <div class="proj-desc">
          Domain-specific AI assistant for Jyotish / astrology queries using Retrieval-Augmented
          Generation. Features PDF knowledge ingestion, hybrid semantic search via LanceDB,
          conversational memory, and citation-based responses grounded in real documents.
        </div>
        <div class="proj-stack">
          <span class="proj-tech">Agno</span>
          <span class="proj-tech">LanceDB</span>
          <span class="proj-tech">Ollama</span>
          <span class="proj-tech">Llama 3.2</span>
          <span class="proj-tech">RAG</span>
          <span class="proj-tech">Streamlit</span>
        </div>
      </div>

      <!-- Personal 3 -->
      <div class="proj-card">
        <div class="proj-badge">✦ Personal Project</div>
        <div class="proj-title">Wheels.ai – MaaS (Model-as-a-Service) Platform</div>
        <div class="proj-desc">
          Platform enabling users to access curated open-source AI models without hyperscaler
          dependency. Covers model catalog management, API key generation, usage tracking,
          and developer-facing interfaces with OpenAI-compatible APIs on GPU-backed infrastructure.
        </div>
        <div class="proj-stack">
          <span class="proj-tech">Docker</span>
          <span class="proj-tech">Kiro</span>
          <span class="proj-tech">Open-Source LLMs</span>
          <span class="proj-tech">GPU Infra</span>
          <span class="proj-tech">Postman</span>
          <span class="proj-tech">REST APIs</span>
        </div>
      </div>

      <!-- Industrial 1 -->
      <div class="proj-card ind">
        <div class="proj-badge">⚙ Industrial Project</div>
        <div class="proj-title">CRM & Lead Conversion Analytics Dashboard</div>
        <div class="proj-desc">
          Integrated, cleaned, and analysed CRM datasets from HubSpot and Zoho. Built dynamic
          dashboards tracking lead conversion, campaign ROI, and revenue trends. Boosted
          targeted outreach effectiveness and improved conversion rates by 20%.
        </div>
        <div class="proj-stack">
          <span class="proj-tech">HubSpot</span>
          <span class="proj-tech">Zoho CRM</span>
          <span class="proj-tech">Google Analytics</span>
          <span class="proj-tech">Python</span>
          <span class="proj-tech">Pandas</span>
          <span class="proj-tech">Dashboards</span>
        </div>
      </div>

      <!-- Industrial 2 -->
      <div class="proj-card ind">
        <div class="proj-badge">⚙ Industrial Project</div>
        <div class="proj-title">Sales & Website Traffic Forecasting Model</div>
        <div class="proj-desc">
          Time-series forecasting pipeline using Facebook Prophet to predict monthly sales and
          website traffic with seasonality adjustments. Delivered actionable insights for budget
          planning, trend analysis, and strategic campaign optimisation.
        </div>
        <div class="proj-stack">
          <span class="proj-tech">Facebook Prophet</span>
          <span class="proj-tech">Python</span>
          <span class="proj-tech">Pandas</span>
          <span class="proj-tech">Matplotlib</span>
          <span class="proj-tech">Time Series</span>
          <span class="proj-tech">Forecasting</span>
        </div>
      </div>

    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# ❺  EDUCATION + CERTIFICATIONS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="sec" id="education">

  <p class="sec-eyebrow">Academic Background</p>
  <h2 class="sec-h">Education</h2>
  <div class="sec-rule"></div>

  <div class="edu-grid">
    <div class="edu-card">
      <div class="edu-icon">🎓</div>
      <div class="edu-deg">Master of Computer Application (MCA)</div>
      <div class="edu-school">Ramdeobaba College of Engineering &amp; Management<br>RTMNU Nagpur University</div>
      <div class="edu-yr">Class of 2017</div>
    </div>
    <div class="edu-card">
      <div class="edu-icon">📐</div>
      <div class="edu-deg">B.Sc – Computers &amp; Mathematics</div>
      <div class="edu-school">Kamla Nehru College<br>RTMNU Nagpur University</div>
      <div class="edu-yr">Class of 2014</div>
    </div>
  </div>

  <!-- CERTIFICATIONS -->
  <div style="margin-top: 4.5rem;">
    <p class="sec-eyebrow">Credentials</p>
    <h2 class="sec-h">Certifications</h2>
    <div class="sec-rule"></div>

    <div class="cert-list">
      <div class="cert-row">
        <div class="cert-ico">🟢</div>
        <div>
          <div class="cert-n">NVIDIA Jetson AI Specialist</div>
          <div class="cert-iss">NVIDIA Corporation</div>
        </div>
      </div>
      <div class="cert-row">
        <div class="cert-ico">🧠</div>
        <div>
          <div class="cert-n">Neural Networks and Deep Learning</div>
          <div class="cert-iss">Great Learning</div>
        </div>
      </div>
      <div class="cert-row">
        <div class="cert-ico">📊</div>
        <div>
          <div class="cert-n">Skill Assessment Badge – Microsoft Excel</div>
          <div class="cert-iss">LinkedIn</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ADDITIONAL INFO -->
  <div style="margin-top: 4.5rem;">
    <p class="sec-eyebrow">What Drives Me</p>
    <h2 class="sec-h">Additional Information</h2>
    <div class="sec-rule"></div>
    <div class="info-grid">
      <div class="info-card">
        <div class="info-card-ico">🚀</div>
        <div class="info-card-text">Actively up-skilling in Generative AI, LLMs, RAG, and Agentic AI through independent projects and applied experimentation.</div>
      </div>
      <div class="info-card">
        <div class="info-card-ico">⚡</div>
        <div class="info-card-text">Quick learner with strong problem-solving abilities and a self-driven learning approach — turning curiosity into working systems.</div>
      </div>
      <div class="info-card">
        <div class="info-card-ico">🎯</div>
        <div class="info-card-text">Analytical thinker with a talent for communicating insights to both technical and non-technical stakeholders for strategic decisions.</div>
      </div>
      <div class="info-card">
        <div class="info-card-ico">🌱</div>
        <div class="info-card-text">Dedicated to building a long-term career in AI. Open to roles in AI Engineering, Gen AI, Machine Learning, and Python development.</div>
      </div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# ❻  CONTACT
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="contact-sec" id="contact">
  <div class="contact-inner">

    <p class="sec-eyebrow">Let's Build Something Together</p>
    <h2 class="sec-h">Get in Touch</h2>
    <p class="contact-sub">
      I'm open to full-time roles in AI Engineering, Generative AI, and Data Science,
      as well as collaborative projects and research opportunities. Feel free to reach out!
    </p>

    <div class="contact-grid">

      <a class="c-card" href="mailto:avibuche@gmail.com">
        <span class="c-ico">✉️</span>
        <span class="c-lbl">Email</span>
        <span class="c-val">avibuche@gmail.com</span>
      </a>

      <a class="c-card" href="tel:+919657640177">
        <span class="c-ico">📞</span>
        <span class="c-lbl">Phone</span>
        <span class="c-val">+91 96576 40177</span>
      </a>

      <a class="c-card" href="https://linkedin.com/in/avantibuche" target="_blank">
        <span class="c-ico">🔗</span>
        <span class="c-lbl">LinkedIn</span>
        <span class="c-val">avantibuche</span>
      </a>

      <a class="c-card" href="https://github.com/avantibuche" target="_blank">
        <span class="c-ico">🐙</span>
        <span class="c-lbl">GitHub</span>
        <span class="c-val">avantibuche</span>
      </a>

    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="ft">
  Designed &amp; built by <a href="mailto:avibuche@gmail.com">Avanti Buche</a>
  &nbsp;·&nbsp; AI Engineer &nbsp;·&nbsp; 2026
  &nbsp;·&nbsp; Made with <span>♥</span> and Python
</div>
""", unsafe_allow_html=True)
