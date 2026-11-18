/* Portfolio interactions: theme, scroll reveal, GA4 events, JD fit checker, contact form. */
(function () {
  'use strict';
  var root = document.documentElement;
  root.classList.add('js');

  function track(name, params) {
    try { if (typeof window.gtag === 'function') window.gtag('event', name, params || {}); } catch (e) {}
  }

  /* ---------- Theme toggle ---------- */
  var toggle = document.querySelector('.theme-toggle');
  function currentTheme() {
    return root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
      track('theme_toggle', { theme: next });
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- Click tracking (CTAs, projects, contact links, résumé) ---------- */
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-track]');
    if (!el) return;
    var name = el.dataset.track;
    track('cta_click', { cta_name: name, link_url: el.href || '', page_path: location.pathname });
    if (name.indexOf('resume') === 0) track('resume_download', { location: name, page_path: location.pathname });
    if (name.indexOf('contact_') === 0) track('contact_click', { method: name.replace('contact_', '') });
  });

  /* ---------- Scroll milestone: reached the projects section ---------- */
  var projects = document.getElementById('projects');
  if (projects && 'IntersectionObserver' in window) {
    var seen = false;
    new IntersectionObserver(function (en) {
      if (!seen && en[0].isIntersecting) { seen = true; track('view_projects_section'); }
    }, { threshold: 0.25 }).observe(projects);
  }

  /* ---------- JD fit checker ---------- */
  var form = document.getElementById('fit-form');
  if (form) initFit(form);

  function initFit(form) {
    var P = {
      cue: { name: 'Codebase Understanding Engine', url: '/portfolio/projects/codebase-understanding-engine/' },
      pharma: { name: 'Pharma Prescriber Copilot', url: '/portfolio/projects/pharma-prescriber-copilot/' },
      safewalk: { name: 'SafeWalk tracker', url: '/portfolio/projects/safewalk-alzheimers-tracker/' },
      malaoi: { name: 'MalAOI thesis', url: '/portfolio/projects/malaoi-gnn-malware-evasion/' },
      infosys: { name: 'Infosys (10 months)', url: '' },
      ta: { name: 'IIIT Allahabad TA', url: '' },
      mtech: { name: 'M.Tech, IIIT Allahabad', url: '' }
    };
    // Skills I can back with evidence: [label, regex, evidence keys, one-line proof]
    var HAVE = [
      ['Python', /\bpython\b/, ['pharma', 'cue', 'malaoi'], 'Main language across three projects'],
      ['JavaScript', /\bjavascript\b|\bjs\b|\bes6\b/, ['safewalk', 'cue'], 'React Native app + Node.js API'],
      ['TypeScript', /\btypescript\b|\bts\b/, ['cue'], 'React/TypeScript frontend for CUE'],
      ['React', /\breact(\.js|js)?\b(?!\s*native)/, ['cue', 'infosys'], 'CUE frontend; UI components at Infosys'],
      ['React Native / mobile', /react\s*native|\bmobile (app|development)|\bandroid\b/, ['safewalk'], 'Shipped an Android app with background tracking'],
      ['Node.js / Express', /\bnode(\.js|js)?\b|\bexpress(\.js|js)?\b/, ['safewalk'], 'SafeWalk backend, hosted on Render'],
      ['FastAPI', /\bfastapi\b/, ['cue', 'pharma'], 'REST APIs for two projects'],
      ['Django', /\bdjango\b/, ['mtech'], 'Listed skill'],
      ['REST APIs', /\brest(ful)?\b|\bapis?\b|web services/, ['pharma', 'safewalk', 'cue'], 'Built three APIs (FastAPI ×2, Express)'],
      ['SQL', /\bsql\b|\bqueries\b/, ['pharma'], 'Text-to-SQL over 518,946 rows'],
      ['PostgreSQL', /\bpostgres(ql)?\b/, ['cue'], 'PostgreSQL + pgvector store'],
      ['MongoDB / NoSQL', /\bmongo(db)?\b|\bnosql\b/, ['safewalk'], 'MongoDB Atlas backend'],
      ['Databases', /\bdatabases?\b|\bdbms\b|\bsqlite\b/, ['pharma', 'cue', 'safewalk'], 'SQLite, PostgreSQL and MongoDB in production-style apps'],
      ['C / C++', /c\+\+|\bcpp\b|\bc programming\b|\bc\/c\+\+/, ['mtech'], 'Core language from coursework'],
      ['Data structures & algorithms', /data structures?|algorithms?|\bdsa\b|problem[- ]solving/, ['ta'], 'TA for Design & Analysis of Algorithms'],
      ['Operating systems', /operating systems?|\bos internals\b/, ['ta'], 'TA for Operating Systems labs'],
      ['Computer networks', /computer networks?|\bnetworking\b|tcp\/?ip/, ['mtech'], 'Core coursework, M.Tech'],
      ['OOP / design', /object[- ]oriented|\boop\b|design patterns|system design|low[- ]level design/, ['cue', 'pharma'], 'HLD/LLD docs written for my projects'],
      ['Machine learning', /machine learning|\bml\b|scikit|sklearn|predictive model/, ['pharma', 'malaoi'], 'Segmentation, classification, forecasting'],
      ['Deep learning / PyTorch', /deep learning|pytorch|neural network|\blstm\b|\bgnn\b/, ['malaoi', 'pharma'], 'GNNs in PyTorch; LSTM forecaster'],
      ['Forecasting / time series', /forecast|time[- ]series|prophet|xgboost/, ['pharma'], 'Prophet vs XGBoost vs LSTM, walk-forward CV'],
      ['Data analysis', /data analy(sis|tics)|\bpandas\b|\beda\b|dashboards?|streamlit|visuali[sz]ation/, ['pharma'], 'EDA + Streamlit dashboard on real CMS data'],
      ['LLMs / RAG / GenAI', /\bllms?\b|\brag\b|generative ai|gen ?ai|large language|embeddings?|vector (db|database|search)|langchain/, ['cue', 'pharma'], 'RAG over code; agentic text-to-SQL'],
      ['Data visualisation (D3)', /\bd3(\.js)?\b|data visuali[sz]ation/, ['cue'], 'Interactive D3 force-directed call graphs'],
      ['Application security', /application security|appsec|secure coding|owasp|vulnerabilit|static analysis|\bsast\b|threat model|security (engineer|review|testing)|sql injection/, ['cue'], 'Built taint analysis for dangerous sinks'],
      ['Information security', /information security|cyber ?security|infosec|security/, ['mtech', 'ta'], 'M.Tech in Cyber Laws & Information Security; Cyber Security TA'],
      ['Malware / adversarial ML', /malware|adversarial|threat (detection|intel)|reverse engineering/, ['malaoi'], 'Thesis on evading GNN malware detectors'],
      ['Authentication (JWT / OAuth)', /\bjwt\b|authentication|authori[sz]ation|\boauth\b|bcrypt/, ['safewalk'], 'JWT auth + bcrypt + per-user authorization'],
      ['CI/CD & Git', /\bci\/?cd\b|github actions|continuous integration|\bgit(hub)?\b/, ['pharma'], 'GitHub Actions CI on every push'],
      ['Cloud deployment', /deploy(ment|ing)?|\bhosting\b|\brender\b|\bheroku\b|\bpaas\b/, ['safewalk', 'pharma'], 'Backend on Render, DB on MongoDB Atlas'],
      ['Docker', /\bdocker\b|containers?/, ['cue'], 'PostgreSQL + pgvector run in Docker'],
      ['Frontend / UI', /front[- ]?end|\bui\b|user interface|\bhtml\b|\bcss\b|responsive/, ['cue', 'infosys', 'safewalk'], 'Reusable UI components at Infosys; redesigned SafeWalk'],
      ['Full-stack', /full[- ]?stack/, ['cue', 'safewalk'], 'End-to-end apps, frontend to database'],
      ['Backend', /back[- ]?end|server[- ]side|microservices?/, ['pharma', 'safewalk'], 'Three backends, two of them deployed'],
      ['Adobe AEM / CMS', /\baem\b|adobe experience|content management/, ['infosys'], 'AEM components & workflows at Infosys'],
      ['Teaching / communication', /communication|mentor|present(ation)?s?|documentation|technical writing/, ['ta'], 'Run labs and tutorials as a TA']
    ];
    // Skills I don't claim yet. Shown honestly.
    var GAP = [
      ['Java', /\bjava\b(?!script)/], ['Spring Boot', /\bspring\b/], ['Go', /\bgolang\b|\bgo (developer|language)\b/],
      ['Rust', /\brust\b/], ['Kotlin', /\bkotlin\b/], ['Swift / iOS', /\bswift\b|\bios\b/], ['C# / .NET', /c#|\.net\b/],
      ['PHP', /\bphp\b|laravel/], ['Ruby', /\bruby\b|\brails\b/], ['Angular', /\bangular\b/], ['Vue', /\bvue(\.js)?\b/],
      ['Next.js', /next\.?js/], ['GraphQL', /graphql/], ['AWS', /\baws\b|amazon web services|\bec2\b|\bs3\b|lambda/],
      ['Azure', /\bazure\b/], ['GCP', /\bgcp\b|google cloud/], ['Kubernetes', /kubernetes|\bk8s\b/], ['Terraform', /terraform/],
      ['Kafka', /\bkafka\b/], ['Redis', /\bredis\b/], ['Spark / Hadoop', /\bspark\b|hadoop|databricks/],
      ['Tableau / Power BI', /tableau|power ?bi/], ['Jenkins', /jenkins/], ['SIEM / SOC tools', /\bsiem\b|splunk|\bsoc\b|qradar|sentinel/],
      ['Penetration testing tools', /burp|metasploit|nmap|penetration testing|pentest/]
    ];

    var SAMPLES = {
      backend: 'Software Development Engineer (Backend). Build scalable REST APIs and microservices in Python or Java. Strong data structures and algorithms, object-oriented design and SQL (PostgreSQL). Experience with Docker, CI/CD pipelines, Git and cloud deployment on AWS. Exposure to Redis or Kafka is a plus. Good communication skills.',
      security: 'Security Engineer, Application Security. Perform secure code review and static analysis (SAST), threat modelling and vulnerability triage against the OWASP Top 10, including SQL injection. Script automation in Python. Familiarity with authentication (OAuth, JWT), Burp Suite, and cloud security on AWS or Azure. Information security degree preferred.',
      fullstack: 'Full-Stack Developer. React and TypeScript on the frontend, Node.js / Express or FastAPI on the backend, MongoDB and PostgreSQL databases. Build responsive UI, REST APIs, JWT authentication and deploy to the cloud. Next.js and GraphQL experience is a bonus.',
      data: 'Data Scientist / ML Engineer. Python, pandas, scikit-learn and SQL for data analysis and predictive modelling. Time-series forecasting, deep learning with PyTorch, and LLM / RAG applications. Build dashboards and communicate insights. Spark or Databricks a plus.'
    };

    var ta = document.getElementById('jd');
    var out = document.getElementById('fit-result');
    var debounce;

    document.querySelectorAll('[data-sample]').forEach(function (b) {
      b.addEventListener('click', function () {
        ta.value = SAMPLES[b.dataset.sample];
        track('fit_check_sample', { sample: b.dataset.sample });
        run('sample_' + b.dataset.sample);
      });
    });
    form.addEventListener('submit', function (e) { e.preventDefault(); run('pasted'); });

    function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

    function run(source) {
      var jd = ' ' + ta.value.toLowerCase().replace(/\s+/g, ' ') + ' ';
      if (jd.trim().length < 30) {
        out.innerHTML = '<p class="result-empty">Paste a little more of the job description (at least a couple of sentences).</p>';
        return;
      }
      var have = HAVE.filter(function (s) { return s[1].test(jd); });
      // "Information security" is a broad catch-all: drop it if a more specific security skill already matched
      if (have.some(function (s) { return s[0] === 'Application security' || s[0] === 'Malware / adversarial ML'; })) {
        have = have.filter(function (s) { return s[0] !== 'Information security'; });
      }
      var gap = GAP.filter(function (s) { return s[1].test(jd); });
      var total = have.length + gap.length;
      if (!total) {
        out.innerHTML = '<p class="result-empty">I couldn\'t spot specific tech skills in that text. Try pasting the "Requirements" part of the job post.</p>';
        return;
      }
      var score = Math.round(100 * have.length / total);
      var verdict = score >= 80 ? 'Strong fit' : score >= 60 ? 'Good fit' : score >= 40 ? 'Partial fit' : 'Stretch role';
      var html = '<div class="score"><div class="ring" style="--p:' + score + '" data-label="' + score + '%"></div>' +
        '<div><h3>' + verdict + '</h3><p>I match <b>' + have.length + ' of ' + total + '</b> skills this role asks for.</p></div></div>';
      html += '<ul class="match-list">' + have.slice(0, 8).map(function (s) {
        var links = s[2].map(function (k) {
          var p = P[k];
          return p.url ? '<a href="' + p.url + '" data-track="fit_evidence_' + k + '">' + esc(p.name) + '</a>' : esc(p.name);
        }).join(' · ');
        return '<li><b>✓ ' + esc(s[0]) + '</b> — ' + esc(s[3]) + '<br><small>' + links + '</small></li>';
      }).join('') + '</ul>';
      if (have.length > 8) html += '<p class="muted" style="font-size:.9rem">…and ' + (have.length - 8) + ' more matching skills.</p>';
      if (gap.length) {
        html += '<p style="margin:0;font-weight:600;font-size:.92rem">Not on my résumé yet (I pick things up fast):</p><div class="chips">' +
          gap.map(function (s) { return '<span class="chip">' + esc(s[0]) + '</span>'; }).join('') + '</div>';
      }
      html += '<div class="fit-cta"><p>Like the match? Let\'s talk.</p>' +
        '<a class="btn" href="/portfolio/assets/Chinmaya_Nayak_Resume.pdf" download data-track="resume_fit_checker">Download résumé</a>' +
        '<a class="btn btn-ghost" href="#contact" data-track="cta_fit_contact">Contact me</a></div>';
      out.innerHTML = html;
      out.setAttribute('tabindex', '-1');
      if (source === 'pasted' && innerWidth < 860) out.scrollIntoView({ behavior: 'smooth', block: 'start' });
      // Only aggregate numbers go to analytics, never the pasted text
      track('fit_check_run', { source: source, fit_score: score, matched_skills: have.length, missing_skills: gap.length });
    }

    ta.addEventListener('input', function () {
      clearTimeout(debounce);
      debounce = setTimeout(function () { if (ta.value.length > 200) run('typed'); }, 900);
    });
  }

  /* ---------- Contact form: compose an email (no backend on GitHub Pages) ---------- */
  var cf = document.getElementById('contact-form');
  if (cf) {
    cf.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = cf.elements;
      var subject = 'Opportunity for Chinmaya' + (f.company.value ? ' at ' + f.company.value : '');
      var body = f.message.value + '\n\n— ' + f.name.value + (f.company.value ? ', ' + f.company.value : '') + '\n' + f.email.value;
      track('generate_lead', { method: 'contact_form', has_company: !!f.company.value });
      location.href = 'mailto:chinmayanayak018@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      document.getElementById('thanks').style.display = 'block';
    });
  }
})();
