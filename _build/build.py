"""Static site generator for chinmaya2310.github.io.

Run:  python3 _build/build.py
Writes index.html, projects/<slug>/index.html, 404.html and sitemap.xml.
(_build/ starts with an underscore, so GitHub Pages' Jekyll does not publish it.)
"""
import json, os, re, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "/portfolio"
SITE = "https://chinmaya2310.github.io" + BASE
GA = "G-G5MBDW1E1F"
GSC = "30sAjotF1Gglg-_EVpD2LCbYcUsk-VZQFdx3HA7s4Ac"
EMAIL = "chinmayanayak018@gmail.com"
GITHUB = "https://github.com/Chinmaya2310"
NAME = "Chinmaya Kumar Nayak"
TODAY = datetime.date.today().isoformat()
RESUME = BASE + "/assets/Chinmaya_Nayak_Resume.pdf"

ICON = {
    "sun": '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    "moon": '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    "download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5a11.5 11.5 0 0 0-3.6 22.4c.6.1.8-.3.8-.6v-2c-3.2.7-3.9-1.5-3.9-1.5-.5-1.3-1.3-1.7-1.3-1.7-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.6-.3-5.3-1.3-5.3-5.7 0-1.3.5-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.2 1.2a11 11 0 0 1 5.8 0c2.2-1.5 3.2-1.2 3.2-1.2.6 1.6.2 2.8.1 3.1.8.8 1.2 1.9 1.2 3.1 0 4.4-2.7 5.4-5.3 5.7.4.4.8 1.1.8 2.2v3.2c0 .3.2.7.8.6A11.5 11.5 0 0 0 12 .5z"/></svg>',
    "file": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
}

# ---------------------------------------------------------------- projects
PROJECTS = [
    {
        "slug": "codebase-understanding-engine",
        "key": "cue",
        "kicker": "Developer tools · Security",
        "title": "Codebase Understanding Engine",
        "seo_title": "Codebase Understanding Engine: Call Graphs, RAG Q&A and Taint Analysis | Case Study",
        "desc": "Case study: a React/TypeScript + FastAPI tool that turns any GitHub repo into an interactive call graph, answers questions about the code with RAG, and flags SQL injection paths with taint analysis.",
        "card": "Paste a GitHub URL and get an interactive call graph, plain-English Q&A over the code, dead-code detection and taint analysis for dangerous sinks.",
        "tags": ["React", "TypeScript", "FastAPI", "PostgreSQL + pgvector", "Tree-sitter", "D3.js"],
        "repo": "https://github.com/Chinmaya2310/Codebase-Understanding-Engine",
        "og": "og-cue.png",
        "facts": [("Role", "Solo, full stack"), ("Type", "Developer tool"), ("Frontend", "React + TypeScript"), ("Backend", "FastAPI + PostgreSQL")],
        "lead": "Joining a new codebase usually means days of opening files one by one. CUE makes the structure of any public GitHub repository visible in minutes, and points at the code paths most likely to be exploitable.",
        "body": """
<h2>The problem</h2>
<p>Developers lose a lot of time on unfamiliar code: which function calls which, what is dead, and where user input ends up. Security reviewers have the same question in a sharper form: <em>can untrusted input reach a dangerous call?</em></p>

<h2>What I built</h2>
<ul>
  <li><strong>Parsing:</strong> Tree-sitter parsers for Python, JavaScript, TypeScript, Java and Go extract modules, classes, functions, imports and calls into a graph stored in PostgreSQL.</li>
  <li><strong>Code graph:</strong> an interactive D3 force-directed graph (drag, zoom, click to inspect) plus Mermaid architecture diagrams.</li>
  <li><strong>Ask AI:</strong> code chunks are embedded with sentence-transformers into pgvector, so questions like "where is authentication handled?" are answered with retrieval-augmented generation (RAG) grounded in the actual source.</li>
  <li><strong>Dead code:</strong> functions and classes with zero incoming calls or imports, ranked by confidence, with entry points skipped.</li>
  <li><strong>Security:</strong> taint analysis that walks the call graph (breadth-first, up to 6 hops) from user-input sources to dangerous sinks: <code>eval</code>/<code>exec</code>, <code>shell=True</code>, SQL built with string formatting, and <code>pickle</code>. Each finding gets an on-demand LLM explanation of why it is exploitable and how to fix it.</li>
</ul>

<figure>
  <img src="/assets/img/cue-security.webp" width="1200" height="1037" loading="lazy" alt="CUE security tab listing 8 high-confidence SQL injection paths in a deliberately vulnerable Python web app, with an AI explanation of one finding">
  <figcaption>The Security tab on a deliberately vulnerable app (dvpwa): 8 high-confidence SQL-injection paths, each with the call path, source, sink and a fix.</figcaption>
</figure>

<h2>Results</h2>
<div class="numbers">
  <div><b>5</b><span>languages parsed</span></div>
  <div><b>8 / 8</b><span>SQL-injection paths flagged high-confidence on dvpwa</span></div>
  <div><b>≤ 6 hops</b><span>call-path depth for taint tracking</span></div>
</div>
<div class="callout">Honest limitation: the analysis works at the call-graph level, so a tainted value may not actually reach the sink at runtime. The UI says so, and labels each finding with a confidence level.</div>

<h2>What I learned</h2>
<p>Static analysis is a precision game. Most of the work went into resolving calls correctly (<code>self.method</code>, <code>Class.method</code>, module functions) because every wrong edge becomes a false positive in the security view.</p>
""",
    },
    {
        "slug": "pharma-prescriber-copilot",
        "key": "pharma",
        "kicker": "Data science · Analytics",
        "title": "Pharma Prescriber Analytics Copilot",
        "seo_title": "Pharma Prescriber Analytics Copilot: Forecasting & Text-to-SQL on Medicare Part D | Case Study",
        "desc": "Case study: an end-to-end analytics pipeline on real CMS Medicare Part D data (69.7M claims) with prescriber segmentation, Prophet vs XGBoost vs LSTM demand forecasting and an agentic text-to-SQL assistant.",
        "card": "Forecasting, segmentation and a plain-English text-to-SQL assistant over real CMS Medicare Part D data: 518,946 rows and 69.7M claims.",
        "tags": ["Python", "FastAPI", "Streamlit", "XGBoost", "Prophet", "SQL"],
        "repo": "https://github.com/Chinmaya2310/pharma-prescriber-copilot",
        "og": "og-pharma.png",
        "facts": [("Role", "Solo, end to end"), ("Data", "CMS Medicare Part D"), ("Serving", "FastAPI + Streamlit"), ("MLOps", "GitHub Actions CI")],
        "lead": "A sales-operations team wants to know which prescribers are growing, how demand for a drug will move next year, and to ask ad-hoc questions without writing SQL. This project answers all three on real public data.",
        "body": """
<h2>The data</h2>
<p>Real <strong>CMS Medicare Part D prescriber</strong> data, at the grain each task needs: state-level demand series from 2013 to 2024 for forecasting, and prescriber-level detail from 2022 to 2024 for segmentation. Scope: 4 drugs (Metformin, Atorvastatin, Amoxicillin, Anastrozole) across 4 states (CA, TX, NY, FL).</p>
<div class="numbers">
  <div><b>69.7M</b><span>claims</span></div>
  <div><b>518,946</b><span>provider-drug-year rows</span></div>
  <div><b>187,436</b><span>prescribers</span></div>
  <div><b>12 yrs</b><span>of demand history</span></div>
</div>

<h2>What I built</h2>
<ul>
  <li><strong>Pipeline:</strong> ingest → clean → EDA → segmentation → forecasting, rerunnable with one command and checked by GitHub Actions CI on every push.</li>
  <li><strong>Segmentation:</strong> K-Means clusters prescribers by behaviour; a classifier predicts each prescriber's likely next-period growth.</li>
  <li><strong>Forecasting:</strong> Prophet vs XGBoost vs LSTM compared with walk-forward cross-validation, so models are judged on years they never saw.</li>
  <li><strong>Serving:</strong> a FastAPI service (<code>/segments/{npi}</code>, <code>/forecast/{drug}/{region}</code>, <code>/ask</code>) and a Streamlit dashboard.</li>
  <li><strong>Text-to-SQL assistant:</strong> an agent that writes SQL, runs it read-only, and answers from the actual rows, so every number is auditable.</li>
  <li><strong>Monitoring:</strong> a retrain job flags drift when forecast error (MAPE) exceeds 1.5× its historical average.</li>
</ul>

<figure>
  <img src="/assets/img/pharma-forecast.webp" width="840" height="480" loading="lazy" alt="Line chart of Amoxicillin claims in California from 2013 to 2024 with a Prophet forecast for 2025 and 2026">
  <figcaption>Amoxicillin demand in California: 12 years of history, the 2020 COVID dip, and the forecast.</figcaption>
</figure>

<h2>A design decision worth defending</h2>
<div class="callout"><strong>Why text-to-SQL and not RAG?</strong> The questions this data invites ("which specialty prescribes the most X in CA", "how did claims change year over year") are aggregations: a <code>GROUP BY</code>, not a document search. Generating SQL and answering from real rows avoids made-up numbers.</div>

<figure>
  <img src="/assets/img/pharma-by-state.webp" width="960" height="600" loading="lazy" alt="Stacked bar chart of 2024 claims by state and drug class for California, Florida, New York and Texas">
  <figcaption>Claims by state and drug class (2024), from the exploratory analysis.</figcaption>
</figure>

<h2>What I learned</h2>
<p>data.cms.gov blocks non-US traffic, so the pipeline supports a rotating US proxy for real downloads and a clearly labelled synthetic fixture for CI. Being explicit about which numbers are real mattered more than any model choice.</p>
""",
    },
    {
        "slug": "safewalk-alzheimers-tracker",
        "key": "safewalk",
        "kicker": "Mobile · Full stack",
        "title": "SafeWalk: Alzheimer's Patient Tracker",
        "seo_title": "SafeWalk: Alzheimer's Patient Tracker App (React Native, Node.js) | Case Study",
        "desc": "Case study: a React Native app that alerts a caregiver by Telegram or SMS, with a live map link, when a person with Alzheimer's walks outside a safe zone. Node.js/Express + MongoDB backend with JWT auth.",
        "card": "A React Native app that alerts a caregiver, with a live map link, the moment a patient walks outside a safe zone. Works with the screen off.",
        "tags": ["React Native", "Node.js", "Express", "MongoDB", "JWT", "Google Maps"],
        "repo": "https://github.com/Chinmaya2310/AlzeimerPatientTracker",
        "og": "og-safewalk.png",
        "facts": [("Role", "Full stack (revival & redesign)"), ("Platform", "Android"), ("Backend", "Node.js + MongoDB Atlas"), ("Alerts", "Telegram or SMS")],
        "lead": "People with Alzheimer's can wander and get lost within minutes. SafeWalk lets a caregiver draw a safe zone around home and get an alert, with a live map link, as soon as the patient walks out of it.",
        "body": """
<div class="phones">
  <img src="/assets/img/safewalk-safe-zone.webp" width="360" height="760" loading="lazy" alt="SafeWalk screen for setting a safe zone around home with radius options of 200 m, 500 m, 1 km and 2 km">
  <img src="/assets/img/safewalk-track-alert.webp" width="360" height="760" loading="lazy" alt="SafeWalk tracking screen showing the patient 520 m outside the safe zone and an alert sent to the caregiver">
  <img src="/assets/img/safewalk-home.webp" width="360" height="760" loading="lazy" alt="SafeWalk home dashboard with tracking status, safe zone radius, walks saved and alerts sent">
</div>

<h2>The problem</h2>
<p>Caregivers can't watch someone every minute, and generic location-sharing apps don't tell you <em>when it matters</em>. What they need is one reliable alert at the moment a patient leaves a familiar area, and not a flood of false alarms.</p>

<h2>What I built</h2>
<ul>
  <li><strong>Safe zone:</strong> the caregiver picks home on a map (drag the pin or tap) and a radius from 200 m to 2 km. Tracking can't start until a zone exists.</li>
  <li><strong>Background tracking:</strong> an Android foreground service keeps sending GPS points with the screen off; the server decides when to alert (server-side geofence).</li>
  <li><strong>Alerts that don't spam:</strong> an alert fires only after two GPS readings in a row are outside the zone (ignoring GPS jumps), and re-arms once the patient is back within 90% of the radius.</li>
  <li><strong>Telegram or SMS:</strong> free Telegram alerts with a map pin (connected once, by scanning a QR code) or SMS with a Google Maps link.</li>
  <li><strong>Security:</strong> JWT authentication, bcrypt password hashing and per-user authorization on the Node.js/Express + MongoDB API.</li>
</ul>

<h2>Reviving a 2021 project</h2>
<p>This started as a 2021 team project. In 2026 I rebuilt it so it actually works in the field:</p>
<ul>
  <li>Fixed an alert that re-sent on every screen re-render (SMS spam) so it fires once per exit.</li>
  <li>Moved secrets out of the code into environment variables.</li>
  <li>Redesigned every screen, added walk history, and hosted the backend on Render with MongoDB Atlas.</li>
</ul>

<figure>
  <img src="/assets/img/safewalk-walk.webp" width="360" height="760" loading="lazy" style="max-width:300px" alt="SafeWalk walk details screen with distance, duration and the route on a map">
  <figcaption>Every walk is saved with distance, duration and its route.</figcaption>
</figure>

<h2>What I learned</h2>
<p>Mobile location is noisy. Most of the reliability came from simple rules (two consecutive readings, a re-arm margin), not from more complicated code.</p>
""",
    },
    {
        "slug": "malaoi-gnn-malware-evasion",
        "key": "malaoi",
        "kicker": "Security research · M.Tech thesis",
        "title": "MalAOI: Evading GNN Malware Detectors",
        "seo_title": "MalAOI: Adversarial Attacks on GNN Malware Detectors (M.Tech Thesis) | Case Study",
        "desc": "M.Tech thesis case study: reproducing active opcode insertion with reinforcement learning to evade GCN, GAT and DGCNN graph-neural-network malware detectors on real BODMAS samples.",
        "card": "My M.Tech thesis: reproducing a 2025 adversarial-ML attack that uses reinforcement learning to slip malware past graph neural network detectors.",
        "tags": ["Python", "PyTorch", "Graph Neural Networks", "Reinforcement learning", "Security"],
        "repo": "https://github.com/Chinmaya2310/MalAOI-",
        "og": "og-malaoi.png",
        "facts": [("Type", "M.Tech thesis (in progress)"), ("Institute", "IIIT Allahabad"), ("Models", "GCN · GAT · DGCNN"), ("Data", "BODMAS malware")],
        "lead": "Graph neural networks are increasingly used to detect malware from its control-flow graph. My thesis asks how robust they really are when an attacker is allowed to modify the program.",
        "body": """
<h2>The question</h2>
<p>A GNN detector sees a program as a graph of code blocks. If an attacker inserts harmless instructions (opcodes) that change the graph but not the program's behaviour, can the detector be fooled, and how many changes does that take?</p>

<h2>Approach</h2>
<ul>
  <li><strong>Reproduction:</strong> I'm reproducing a 2025 <em>Scientific Reports</em> method, active opcode insertion (AOI), where a reinforcement-learning agent chooses which opcodes to insert and where.</li>
  <li><strong>Targets:</strong> three GNN detector architectures: GCN, GAT and DGCNN.</li>
  <li><strong>Data:</strong> real malware samples from the BODMAS dataset.</li>
  <li><strong>Constraint:</strong> insertions must preserve what the program does, so the attack stays realistic.</li>
</ul>

<h2>Why it matters</h2>
<p>A detector that scores well on a test set can still be easy to evade. Measuring how quickly the attack succeeds against each architecture tells defenders which models need adversarial training before deployment.</p>

<div class="callout">Status: in progress. Results will be published here when the thesis is complete.</div>
""",
    },
]

# ---------------------------------------------------------------- layout
def head(title, desc, path, og_image, og_type="website", jsonld=None):
    url = SITE + path
    ld = "".join(f'\n  <script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="{NAME}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#0f766e">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="{NAME}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/{og_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE}/assets/{og_image}">
  <meta name="google-site-verification" content="{GSC}">{ld}
  <script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
  <link rel="stylesheet" href="/assets/style.css">
  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA}');</script>
  <script src="/assets/main.js" defer></script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <nav aria-label="Main navigation">
      <a class="brand" href="/"><img src="/assets/avatar.svg" width="30" height="30" alt="">Chinmaya Nayak</a>
      <ul class="nav-links">
        <li><a href="/#fit">Fit check</a></li>
        <li><a href="/#projects">Projects</a></li>
        <li><a href="/#skills">Skills</a></li>
        <li><a href="/#contact">Contact</a></li>
      </ul>
      <a class="btn" href="{RESUME}" download data-track="resume_header" style="padding:8px 14px;font-size:.9rem">Résumé</a>
      <button class="theme-toggle" type="button" aria-label="Switch between light and dark theme">{ICON['sun']}{ICON['moon']}</button>
    </nav>
  </header>
"""

FOOT = f"""
  <footer class="site-footer">
    <div class="wrap">
      <span>&copy; 2026 {NAME}</span>
      <span><a href="{GITHUB}" rel="noopener" data-track="contact_github_footer">GitHub</a> · <a href="mailto:{EMAIL}" data-track="contact_email_footer">Email</a> · Hand-built static site on GitHub Pages</span>
    </div>
  </footer>
</body>
</html>
"""

PERSON = {
    "@context": "https://schema.org", "@type": "Person", "@id": SITE + "/#person",
    "name": NAME, "url": SITE + "/", "image": SITE + "/assets/og-image.png",
    "jobTitle": "Full-Stack Developer", "email": "mailto:" + EMAIL,
    "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Indian Institute of Information Technology, Allahabad"},
                 {"@type": "CollegeOrUniversity", "name": "New Horizon College of Engineering"}],
    "worksFor": {"@type": "Organization", "name": "Indian Institute of Information Technology, Allahabad"},
    "knowsAbout": ["React", "TypeScript", "React Native", "FastAPI", "Node.js", "PostgreSQL", "MongoDB",
                   "Information Security", "Application Security", "Machine Learning", "Time-series forecasting"],
    "sameAs": [GITHUB],
}

def card(p):
    tags = "".join(f"<li>{t}</li>" for t in p["tags"][:5])
    return f"""
        <article class="card reveal">
          <a class="thumb" href="/projects/{p['slug']}/" tabindex="-1" aria-hidden="true"><img src="/assets/img/cover-{p['key']}.webp" width="1280" height="720" loading="lazy" alt=""></a>
          <div class="body">
            <div class="kicker">{p['kicker']}</div>
            <h3><a href="/projects/{p['slug']}/" style="color:inherit;text-decoration:none">{p['title']}</a></h3>
            <p>{p['card']}</p>
            <ul class="tags">{tags}</ul>
            <div class="links">
              <a href="/projects/{p['slug']}/" data-track="case_study_{p['key']}">Read the case study →</a>
              <a href="{p['repo']}" rel="noopener" data-track="project_{p['key']}">Source code</a>
            </div>
          </div>
        </article>"""

# ---------------------------------------------------------------- home
def build_home():
    website = {"@context": "https://schema.org", "@type": "WebSite", "name": NAME + " Portfolio", "url": SITE + "/"}
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Projects",
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/projects/{p['slug']}/", "name": p["title"]}
                                 for i, p in enumerate(PROJECTS)]}
    html = head(f"{NAME} | Full-Stack Developer (React, FastAPI) & Security Portfolio",
                "Portfolio of Chinmaya Kumar Nayak, full-stack developer and M.Tech (Information Security) student at IIIT Allahabad. Paste a job description to see how my skills match, then explore project case studies.",
                "/", "og-image.png", "profile", [PERSON, website, items])
    html += f"""
  <main id="main">
    <section class="hero">
      <div class="wrap">
        <span class="status">Open to SDE, backend &amp; security roles</span>
        <span class="eyebrow" style="display:block">Full-stack developer · M.Tech, IIIT Allahabad</span>
        <h1>I build full-stack products <span class="hl">and I know how they break.</span></h1>
        <p class="lead">I'm Chinmaya Kumar Nayak. I ship web and mobile apps with React, TypeScript, FastAPI and Node.js, and I'm studying Cyber Laws &amp; Information Security at IIIT Allahabad, so security is part of how I build.</p>
        <div class="cta-row">
          <a class="btn" href="#fit" data-track="cta_hero_fit">{ICON['target']}Check my fit for your role</a>
          <a class="btn btn-ghost" href="{RESUME}" download data-track="resume_hero">{ICON['download']}Download résumé</a>
        </div>
        <div class="stats">
          <div class="stat reveal"><b>4</b><span>case studies</span></div>
          <div class="stat reveal"><b>69.7M</b><span>claims analysed</span></div>
          <div class="stat reveal"><b>10 mo</b><span>engineer at Infosys</span></div>
          <div class="stat reveal"><b>5</b><span>languages my code-graph tool parses</span></div>
        </div>
      </div>
    </section>

    <section id="fit" class="section fit" aria-labelledby="fit-title">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">For recruiters · 10-second check</span>
          <h2 id="fit-title">Does Chinmaya fit your role?</h2>
          <p>Paste a job description. You'll get a match score, the skills I can back with real projects, and the ones I don't claim yet. It runs in your browser; nothing you paste is sent anywhere.</p>
        </div>
        <div class="fit-box">
          <form id="fit-form" class="panel reveal">
            <label for="jd">Job description</label>
            <textarea id="jd" name="jd" placeholder="Paste the role's responsibilities and requirements here…"></textarea>
            <div class="samples"><span>No JD handy? Try:</span>
              <button type="button" class="chip-btn" data-sample="backend">Backend SDE</button>
              <button type="button" class="chip-btn" data-sample="security">AppSec engineer</button>
              <button type="button" class="chip-btn" data-sample="fullstack">Full-stack dev</button>
              <button type="button" class="chip-btn" data-sample="data">Data / ML</button>
            </div>
            <button class="btn" type="submit">{ICON['target']}Check my fit</button>
            <p class="privacy">Privacy: analysis happens on this page. Analytics only records the score, never your text.</p>
          </form>
          <div id="fit-result" class="panel reveal" aria-live="polite">
            <div class="result-empty">{ICON['doc']}<p>Your match report will appear here.</p></div>
          </div>
        </div>
      </div>
    </section>

    <section id="projects" class="section" aria-labelledby="projects-title">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">Selected work</span>
          <h2 id="projects-title">Projects, told as case studies</h2>
          <p>Each one covers the problem, what I built, the numbers, and what I'd defend in an interview.</p>
        </div>
        <div class="grid">{''.join(card(p) for p in PROJECTS)}
        </div>
      </div>
    </section>

    <section id="skills" class="section" aria-labelledby="skills-title">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">Toolbox</span>
          <h2 id="skills-title">Skills</h2>
        </div>
        <div class="skills">
          <div class="skill reveal"><h3>Languages</h3><ul class="tags"><li>Python</li><li>JavaScript</li><li>TypeScript</li><li>SQL</li><li>C / C++</li></ul></div>
          <div class="skill reveal"><h3>Web &amp; mobile</h3><ul class="tags"><li>React</li><li>React Native</li><li>D3.js</li><li>FastAPI</li><li>Node.js</li><li>Express</li><li>Django</li><li>REST APIs</li></ul></div>
          <div class="skill reveal"><h3>Data &amp; ML</h3><ul class="tags"><li>PostgreSQL</li><li>MongoDB</li><li>SQLite</li><li>pgvector</li><li>XGBoost</li><li>Prophet</li><li>PyTorch</li></ul></div>
          <div class="skill reveal"><h3>Security &amp; CS core</h3><ul class="tags"><li>Taint analysis</li><li>JWT / bcrypt</li><li>Adversarial ML</li><li>DSA</li><li>OS</li><li>Networks</li><li>DBMS</li></ul></div>
        </div>
      </div>
    </section>

    <section id="contact" class="section" aria-labelledby="contact-title">
      <div class="wrap contact-grid">
        <div class="reveal">
          <span class="eyebrow">Get in touch</span>
          <h2 id="contact-title">Let's talk about your team</h2>
          <p class="muted">I'm based in Prayagraj and open to full-time software developer, backend and security engineering roles.</p>
          <ul class="contact-list">
            <li><a href="{RESUME}" download data-track="resume_contact">{ICON['file']}Download my résumé (PDF)</a></li>
            <li><a href="mailto:{EMAIL}" data-track="contact_email">{ICON['mail']}{EMAIL}</a></li>
            <li><a href="{GITHUB}" rel="noopener" data-track="contact_github">{ICON['github']}github.com/Chinmaya2310</a></li>
          </ul>
        </div>
        <form id="contact-form" class="panel reveal">
          <div class="row">
            <div class="field"><label for="cf-name">Your name</label><input id="cf-name" name="name" autocomplete="name" required></div>
            <div class="field"><label for="cf-company">Company</label><input id="cf-company" name="company" autocomplete="organization"></div>
          </div>
          <div class="field"><label for="cf-email">Your email</label><input id="cf-email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="cf-msg">Message</label><textarea id="cf-msg" name="message" required placeholder="The role, the team, and a good time to talk"></textarea></div>
          <button class="btn" type="submit">{ICON['mail']}Send message</button>
          <p class="form-note">This opens your email app with the message ready to send.</p>
          <p id="thanks" class="thanks">Thanks! Your email app should have opened. If it didn't, write to {EMAIL}.</p>
        </form>
      </div>
    </section>
  </main>
"""
    html += FOOT
    write("index.html", html)

# ---------------------------------------------------------------- case studies
def build_case(i, p):
    path = f"/projects/{p['slug']}/"
    prev_p = PROJECTS[i - 1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    code = {"@context": "https://schema.org", "@type": "SoftwareSourceCode", "name": p["title"],
            "description": p["desc"], "codeRepository": p["repo"], "url": SITE + path,
            "image": f"{SITE}/assets/{p['og']}", "keywords": ", ".join(p["tags"]),
            "author": {"@id": SITE + "/#person", "@type": "Person", "name": NAME}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Projects", "item": SITE + "/#projects"},
        {"@type": "ListItem", "position": 3, "name": p["title"], "item": SITE + path}]}
    facts = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["facts"])
    tags = "".join(f"<li>{t}</li>" for t in p["tags"])
    html = head(p["seo_title"], p["desc"], path, p["og"], "article", [code, crumbs])
    html += f"""
  <main id="main" class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/#projects">Projects</a> / <span aria-current="page">{p['title']}</span></nav>
    <header class="cs-hero">
      <span class="eyebrow">{p['kicker']}</span>
      <h1>{p['title']}</h1>
      <p class="lead">{p['lead']}</p>
      <ul class="tags">{tags}</ul>
      <div class="cta-row">
        <a class="btn" href="{p['repo']}" rel="noopener" data-track="project_{p['key']}_casestudy">{ICON['github']}View source on GitHub</a>
        <a class="btn btn-ghost" href="/#fit" data-track="cta_casestudy_fit_{p['key']}">{ICON['target']}Check my fit for your role</a>
      </div>
      <dl class="facts">{facts}</dl>
    </header>
    <div class="cs-cover"><img src="/assets/img/cover-{p['key']}.webp" width="1280" height="720" alt="Cover image for the {p['title']} case study" fetchpriority="high"></div>
    <article class="prose">{p['body']}</article>

    <aside class="cs-cta">
      <h2>Hiring for a role like this?</h2>
      <p>Grab my one-page résumé, or paste your job description into the fit checker to see how my skills line up.</p>
      <div class="cta-row">
        <a class="btn" href="{RESUME}" download data-track="resume_casestudy_{p['key']}">{ICON['download']}Download résumé</a>
        <a class="btn btn-ghost" href="/#contact" data-track="cta_casestudy_contact_{p['key']}">{ICON['mail']}Contact me</a>
      </div>
    </aside>
    <nav class="pager" aria-label="More projects">
      <a href="/projects/{prev_p['slug']}/"><span>← Previous</span>{prev_p['title']}</a>
      <a href="/projects/{next_p['slug']}/"><span>Next →</span>{next_p['title']}</a>
    </nav>
  </main>
"""
    html += FOOT
    write(f"projects/{p['slug']}/index.html", html)

def build_404():
    html = head("Page not found | " + NAME, "This page doesn't exist. Head back to the portfolio of Chinmaya Kumar Nayak.", "/404.html", "og-image.png")
    html = html.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex">')
    html += f"""
  <main id="main"><section class="hero"><div class="wrap">
    <span class="eyebrow">Error 404</span>
    <h1>This page wandered off.</h1>
    <p class="lead">Unlike SafeWalk's patients, it didn't trigger an alert. Try one of these instead:</p>
    <div class="cta-row"><a class="btn" href="/">Back to home</a><a class="btn btn-ghost" href="/#projects">See projects</a></div>
  </div></section></main>
"""
    write("404.html", html + FOOT)

def build_sitemap():
    urls = [("/", "1.0", "monthly")] + [(f"/projects/{p['slug']}/", "0.8", "monthly") for p in PROJECTS]
    body = "".join(f"""  <url>
    <loc>{SITE}{u}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{c}</changefreq>
    <priority>{pr}</priority>
  </url>
""" for u, pr, c in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n')

def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if rel.endswith(".html"):
        # every root-relative link/asset lives under /portfolio now
        text = re.sub(r'(href|src)="/(?!/|portfolio/)', r'\1="' + BASE + '/', text)
    with open(path, "w") as f:
        f.write(text)
    print("wrote", rel)

if __name__ == "__main__":
    build_home()
    for i, p in enumerate(PROJECTS):
        build_case(i, p)
    build_404()
    build_sitemap()
