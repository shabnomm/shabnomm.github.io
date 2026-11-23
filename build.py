import os
NAV=[("Home","index.html"),("Documentation Lab","documentation/"),("Published Work","work/"),("Process","research/"),("About","about.html"),("Contact","about.html#contact")]
def page(path,title,desc,body):
    root="../"*path.count("/")
    nav="".join(f'<a href="{root}{h}"{" aria-current=\"page\"" if (root+h).replace("../","")==path.replace("index.html","") or (h=="index.html" and path=="index.html") else ""}>{n}</a>' for n,h in NAV)
    html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,200;0,300;0,400;0,600;1,600&family=Michroma&display=swap"><link rel="stylesheet" href="{root}assets/style.css"><script defer src="{root}assets/main.js"></script></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="top"><a class="brand" href="{root}index.html" aria-label="Shanzia Shabnom Mithun, home">SM</a><nav aria-label="Main">{nav}</nav></header>
<main id="main">{body}</main>
<footer><p><a href="https://www.linkedin.com/in/sshabnom/">LinkedIn</a><a href="https://github.com/shabnomm">GitHub</a><a href="https://medium.com/@shabnommithun">Medium</a><a href="mailto:shabnommithun@gmail.com">Email</a></p><p class="copy">Shanzia Shabnom Mithun · Dhaka, Bangladesh</p></footer></body></html>'''
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True); open(path,"w").write(html)

def doc(kind,domain,title,demo,label,url=None,extra=''):
    link=f'<a href="{url}" aria-label="Read {title} (GitHub Gist)">Read more →</a>' if url else '<span class="wip">In progress</span>'
    return f'<article class="card"><p class="meta">{kind} · {domain}</p><h3>{title}</h3><p>{demo}</p><p class="label">{label}</p>{extra}{link}</article>'
IND="Independent portfolio sample"; REAL="Based on a real project, details anonymized"
srs=doc("SRS","Computer vision","Intelligent Traffic Signal Control System","Shows how a client need becomes numbered, testable requirements: priorities, acceptance criteria with worked numbers, fail-safe behaviour, use cases and a traceability matrix. Follows IEEE 830 and ISO/IEC/IEEE 29148 conventions.",REAL,"https://gist.github.com/shabnomm/bdd443b17d7ca2249df6d1f20a3d6b37")
prd=doc("PRD","E-commerce, AI","AI-Native E-commerce QA Engine","Shows how an AI product is framed for a team: the shopper problem, answers that cite their source or decline and hand off to a human, and illustrative targets.",IND,"https://gist.github.com/shabnomm/b7a67e0d119a841d265dc10b07026201")
api=doc("API reference","E-commerce, AI","AI-Native E-commerce QA Engine","Shows a complete developer reference: authentication and scopes, endpoints, parameters, idempotency rules, error format, rate limits, pagination, and cURL and Python examples. Contract assumptions are flagged for engineering to confirm.",IND,"https://gist.github.com/shabnomm/ec081c6962bdcabe55e3d51aed4357ac")

page("index.html","Shanzia Shabnom Mithun — Technical writer and ML engineer","Technical writer and ML engineer who understands your system first and writes documentation and technical content for your audience: SRS, API reference, user guides and AI/ML articles.",f"""
<section class="hero"><h1 class="name">Shanzia Shabnom Mithun</h1><div class="subs"><p class="sub">Technical writer · ML engineer &amp; developer</p><p class="sub">Dhaka, Bangladesh</p></div>
<p class="lead">I write software documentation and technical content as an ML engineer: I understand your system first, learn your perspective, and prepare it for your target audience.</p>
<p><a class="btn" href="about.html#contact">Get in touch</a><a class="btn alt" href="documentation/">Read the samples</a></p></section>
<section class="proof" aria-label="Proof points"><div><strong>7</strong><span>writing samples</span></div><div><strong>4+ years</strong><span>editorial writing</span></div><div><strong>1,500+</strong><span>articles delivered</span></div></section>
<section><p class="ghost" aria-hidden="true">Docs</p><h2>Featured documentation</h2><div class="grid">{srs}{api}</div><p><a href="documentation/">All documentation samples →</a></p></section>
<section><p class="ghost" aria-hidden="true">Published</p><h2>Where my writing has run</h2><div class="grid">
<article class="card"><p class="meta">Magazine · 4+ years, ongoing</p><h3>Muktoakash</h3><p>Assistant Research Editor at the oldest real estate magazine in Bangladesh. I research topics, history, and unique buildings and projects.</p></article>
<article class="card"><p class="meta">Editorial · about 9 months</p><h3>MSN-syndicated content</h3><p>1,500+ articles with the editorial panel. Ghostwritten under other people's names, so none are linked here.</p></article>
<article class="card"><p class="meta">Technical articles · 3 published</p><h3>Towards AI</h3><p>Machine learning articles on ResNet accuracy, retinal disease domain generalization and an AI search engine.</p><a href="work/">Read them →</a></article>
<article class="card"><p class="meta">Tutorial · 1 published</p><h3>Real Python</h3><p>Nuitka: Compile Python Into a Standalone Executable.</p><a href="work/">Read it →</a></article></div></section>
<section><p class="ghost" aria-hidden="true">Services</p><h2>What I write</h2><div class="three">
<div><h3>Technical content</h3><p>Tutorials, technical articles and research-based publications.</p></div>
<div><h3>Software documentation</h3><p>SRS, API reference, product documentation, user guides and technical design documents.</p></div>
<div><h3>AI and engineering communication</h3><p>AI/ML explainers, developer guides and workflow documentation.</p></div></div></section>
<section><p class="ghost" aria-hidden="true">Contact</p><h2>Tell me about your system</h2><p class="lead">Send me the system and the audience. I will take it from there.</p><p class="contact"><a href="mailto:shabnommithun@gmail.com">shabnommithun@gmail.com</a><br><a href="https://www.linkedin.com/in/sshabnom/">LinkedIn</a><br><a href="https://github.com/shabnomm">GitHub</a><br><a href="https://medium.com/@shabnommithun">Medium</a></p></section>""")
tdd=doc("TDD","Computer vision","Technical Design Document: Intelligent Traffic Signal Control System","Shows how requirements become a design: architecture and component diagrams, an allocation algorithm with test cases, a signal state machine, failure handling, design decisions with trade-offs, an emergency timing budget and open questions. Companion to the SRS.",IND,"https://gist.github.com/shabnomm/c1726ad303c2f6cd644cd49b82c62888",extra="""<p class="exc">Excerpt: zero-density rule</p><pre><code>If every uncapped lane has zero density, the remaining time\nis shared equally among them. Without this rule the cycle\nwould end up shorter than C.</code></pre>""")
ug=doc("User guide","Real estate","PropDesk User Guide","Shows task-based documentation for non-technical users: numbered steps, notes, cautions and warnings placed before the step they apply to, role-based reading paths, a troubleshooting table, FAQ and glossary.",IND,"https://gist.github.com/shabnomm/74156f0e4f5efeb6797dc852c701fc75",extra="""<p class="exc">Excerpt: caution before the steps</p><pre><code>Caution: Changing the area unit later does not convert\nexisting listings. Choose it before you add listings.\n1. Select Settings, then Agency profile.\n2. Enter the agency name, phone number, address and logo.\n3. Choose the area unit (square feet or square meters).</code></pre>""")
ins=doc("Tutorial","Python, LLMs","Return Structured Data From LLMs With Instructor","Shows how a tutorial opens with a problem the reader recognizes (fragile handling of LLM output) and then introduces Instructor and Pydantic models as the fix.","Based on a real project","https://gist.github.com/shabnomm/ee487ead68cca583980fd56b2a5b40a7")
nui=doc("Tutorial","Python","Nuitka: Compile Python Into a Standalone Executable","Shows tutorial structure for a developer audience: learning outcomes up front, compiling versus bundling, standalone and onefile modes, and trade-offs stated next to the benefits.","Draft of a published Real Python tutorial","https://gist.github.com/shabnomm/3aab9a7139ae540d4d86e96f7462c040",extra="""<p class="exc">Published version</p><p><a href="https://realpython.com/nuitka/">realpython.com/nuitka</a></p>""")
srs_d=srs.replace("</p><a href","</p><p class=\"exc\">Excerpt: FR-5</p><pre><code>The system shall allocate green time in proportion to lane\ndensity, after giving each lane the minimum green and capping\neach lane at the maximum green.\nAcceptance: densities 20, 10, 5, 5 produce greens of\n40, 25, 17.5 and 17.5 s.</code></pre><a href",1)
api_d=api.replace("</p><a href","</p><p class=\"exc\">Excerpt: error format</p><pre><code>{\"error\": {\"type\": \"invalid_request\",\n  \"code\": \"missing_parameter\",\n  \"message\": \"The product_id parameter is required.\",\n  \"param\": \"product_id\", \"request_id\": \"req_6b2f9d\"}}</code></pre><a href",1)
page("documentation/index.html","Documentation Lab — Shanzia Shabnom Mithun","Software documentation samples: SRS, PRD and API reference.",f'''
<h1>Documentation Lab</h1><p class="lead">Each sample is labelled by origin. Fictional work is never presented as a client engagement.</p>
<div class="grid">{srs_d}{tdd}{api_d}{ug}{prd}{ins}{nui}</div>
''')

def ta(t,u,p): return f"""<article class="case"><p class="meta">Towards AI · Technical article</p><h2>{t}</h2><p>{p}</p><p><a href="{u}">Read the article →</a></p></article>"""
M="https://medium.com/towards-artificial-intelligence/"
page("work/index.html","Published Work — Shanzia Shabnom Mithun","Published technical writing on Real Python and Towards AI.",f"""
<h1>Published Work</h1><p class="lead">Magazine and editorial work, one Real Python tutorial and three Towards AI articles.</p>
<article class="case"><p class="meta">Magazine · 4+ years, ongoing</p><h2>Muktoakash</h2><dl><dt>Role</dt><dd>Assistant Research Editor at the oldest real estate magazine in Bangladesh.</dd><dt>Work</dt><dd>I gather articles, research topics and history, and write about unique buildings and projects.</dd></dl></article>
<article class="case"><p class="meta">Editorial · about 9 months</p><h2>MSN-syndicated content</h2><dl><dt>Role</dt><dd>Editorial Analyst and Automation Developer, working with the editorial panel.</dd><dt>Work</dt><dd>1,500+ articles: readability, SEO and consistency, keyword analysis for headlines, and scripts that automated repetitive editorial tasks.</dd><dt>Note</dt><dd>Much of the writing was ghostwriting, published under other people's names, so none of it is linked here.</dd></dl></article>
<article class="case"><p class="meta">Real Python · Tutorial</p><h2>Nuitka: Compile Python Into a Standalone Executable</h2><dl>
<dt>Problem</dt><dd>Developers who need to distribute a Python application usually reach for a bundler such as PyInstaller. Nuitka works differently, so readers need to know how it differs and what it costs.</dd>
<dt>My role</dt><dd>Author of the tutorial.</dd>
<dt>Approach</dt><dd>Contrasts compiling Python to C with bundling it alongside the interpreter, explains standalone (folder) and onefile (single file) modes, and states the trade-offs, such as longer builds and compiler requirements, next to the benefits.</dd>
<dt>Outcome</dt><dd>Published on Real Python.</dd></dl><p><a href="https://realpython.com/nuitka/">Read the tutorial →</a></p></article>
{ta("ResNet Hits 98% Accuracy",M+"resnet-hits-98-accuracy-0713cad9afc9","How a ResNet model reached 98% accuracy.")}
{ta("Why Your Retinal Disease Model Fails Outside the Lab",M+"why-your-retinal-disease-model-fails-outside-the-lab-acbec5f4bb01","A retinal disease model that performs well in the lab can fail on data from other sources: the domain generalization problem.")}
{ta("I Built a Production-Grade AI Search Engine on a 20GB Laptop. No Cloud Required.",M+"i-built-a-production-grade-ai-search-engine-on-a-20gb-laptop-no-cloud-required-b83196b14e34","Building an AI search engine that runs on a laptop without cloud services.")}
<h2>More on Medium</h2><p>Articles on my own <a href="https://medium.com/@shabnommithun">Medium profile</a>.</p><ul class="plain"><li><a href="https://medium.com/@shabnommithun/what-a-pencil-and-paper-space-mission-can-teach-kids-about-coding-527931144808">What a Pencil-and-Paper Space Mission Can Teach Kids About Coding</a></li><li><a href="https://medium.com/@shabnommithun/building-a-real-estate-ai-automation-engine-with-n8n-groq-and-supabase-5760a7fee3af">Building a Real Estate AI Automation Engine with n8n, Groq and Supabase</a></li><li><a href="https://medium.com/@shabnommithun/why-most-ai-projects-fail-before-deployment-f93fe072e4d0">Why Most AI Projects Fail Before Deployment</a></li><li><a href="https://medium.com/@shabnommithun/how-i-built-an-ai-powered-field-service-dispatch-system-solo-full-architecture-20afd837e0c9">How I Built an AI-Powered Field Service Dispatch System Solo: Full Architecture</a></li></ul>""")

steps=[("Understand the system","I start with the system itself: how it works, what it is for and where it can fail."),("Know your perspective","I learn what you need the document to do, who owns it and what you already know."),("Prepare it for your audience","I write for the people who will use it, whether developers, reviewers or end users, at the level of detail they need."),("Check it","I verify claims, examples and numbers against the system, and write acceptance criteria and edge cases where they matter.")]
li="".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a,b in steps)
page("research/index.html","Process — Shanzia Shabnom Mithun","How I turn an engineering system into clear documentation.",f'''
<h1>Process</h1><p class="lead">Engineering first, then writing: understand the system, learn your perspective, prepare it for your target audience.</p>
<ol class="flow">{li}</ol>
<h2>Working style</h2><p>I work independently. Give me the project and the audience, and I will plan, draft and check the document myself.</p>''')

def x(t,m,p): return f'<article class="case"><h2>{t}</h2><p class="meta">{m}</p><p>{p}</p></article>'
expw="".join([
x("Muktoakash — Assistant Research Editor","Oldest real estate magazine in Bangladesh · about 4 years, ongoing","I gather articles, research topics and history, and write about unique buildings and projects."),
x("Real Python — Technical Writer","Jun 2026 – present","I write Python tutorials through practical examples and editorial review. One tutorial is published: <a href='work/'>Nuitka</a>."),
x("Towards AI — Technical Article Contributor","Jan 2026 – present","Technical machine learning articles on medical imaging, domain generalization and AI systems. Three published. <a href='work/'>Read them</a>."),
x("MSN-syndicated content via FoodnService — Editorial Analyst &amp; Automation Developer","Aug 2025 – May 2026","High-volume editorial production across 1,500+ articles, working with the editorial panel: readability, SEO and consistency, keyword analysis for headlines and updates, performance tracking, and scripts that automated repetitive editorial tasks. Much of the writing was ghostwriting, published under other people's names, so it is not linked here."),
])
expe="".join([
x("Independent ML and Data Science Client Solutions","Present","I deliver machine learning and data science solutions for clients as an independent engineer."),
x("Monico Technologies Limited — Software Engineer","Apr 2026 – present","I work on two applications and validate features with boundary value analysis, equivalence partitioning and edge-case scenarios."),
x("Independent Research Mentor — Freelance","Oct 2025 – Sep 2026","Mentored two student thesis projects, guiding methodology, coding, experimental evaluation and thesis writing."),
x("SuperAnnotate (SME Careers) — Safety AI Trainer","2026 – present, project-based","Assess AI responses against safety criteria and document structured evaluation decisions."),
x("TELUS Digital — GenAI expert","Recently selected","Recently selected as a GenAI expert and working as an AI trainer."),
x("Civion Labs","AI automation agency · building","I am building Civion Labs, an AI automation agency, alongside my client work and writing."),
])
page("about.html","About and Experience — Shanzia Shabnom Mithun","Experience in editorial writing, technical writing, software development and AI training.",f"""
<h1 id="about">About</h1><div class="about"><img class="oval" src="assets/shanzia.jpg" alt="Portrait of Shanzia Shabnom Mithun" width="720" height="960"><div><p>I am an ML engineer and developer who writes technical documentation and content. I graduated in Computer Science and Engineering from East West University in 2026, with a major in Intelligent Systems and Data Science and a minor in Software Engineering. My work covers software development, machine learning research and data analysis.</p>
<p>What I enjoy most is engineering work: taking a hard problem, finding where the difficulty actually is, and solving it. I enjoy documenting that work just as much, so the problem, the decisions and the results are clear to the people who need them.</p>
<p>I build tools such as document Q&amp;A with cited answers, semantic product search and a field service dispatch system, and I have written about several of them. At Monico Technologies I work as a software engineer, and my QA work there is why I write requirements with acceptance criteria and edge cases. I also take on ML and data science client projects independently.</p>
<h2>Research</h2><p>I was research lead on four research projects: carbon-conscious NLP model selection and Alzheimer's MRI classification with explainability (both manuscripts under peer review), retinal image classification with domain generalization (my capstone, with an ongoing extension), and betel leaf disease classification with explainable AI (ongoing). Going through peer review means I understand how technical claims are checked, and I explain complex results clearly.</p></div></div>
<h1>Experience</h1><h2>Writing</h2>{expw}<h2>Engineering and AI</h2>{expe}<h1 id="contact">Contact</h1>
<p class="contact"><a href="mailto:shabnommithun@gmail.com">shabnommithun@gmail.com</a><br><a href="https://www.linkedin.com/in/sshabnom/">LinkedIn</a><br><a href="https://github.com/shabnomm">GitHub: shabnomm</a><br><a href="https://medium.com/@shabnommithun">Medium</a></p>""")

os.makedirs("assets",exist_ok=True)
open("assets/style.css","w").write('''
:root{color-scheme:light;--b1:#ece7df;--b2:#f5f2ec;--fg:#111;--mut:#47433c;--ac:#2b4a3a;--line:rgba(0,0,0,.3);--ghost:rgba(70,58,46,.4);--x:Michroma,"Josefin Sans",sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}::selection{background:var(--fg);color:var(--b2)}
body{margin:0;background:var(--b1);color:var(--fg);font:400 1.06rem/1.75 "Josefin Sans",system-ui,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2{font-family:"Josefin Sans",sans-serif;text-transform:uppercase}
h1{font-weight:200;font-size:clamp(2.2rem,8vw,6rem);line-height:1.02;letter-spacing:.01em;margin:4.5rem 0 1.5rem}
h2{font-weight:300;font-size:clamp(1.5rem,3vw,2.1rem);letter-spacing:.06em;margin:0 0 1.5rem}
h3{font-weight:400;font-size:1.15rem;letter-spacing:.03em;margin:.2rem 0 .3rem}
main,header.top,footer{max-width:62rem;margin:0 auto;padding:0 1.5rem}
a{color:var(--fg);text-underline-offset:4px}a:focus-visible,button:focus-visible{outline:2px solid var(--ac);outline-offset:3px}
.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;background:var(--b2);padding:.5rem;z-index:99}
header.top{position:sticky;top:0;z-index:10;max-width:none;display:flex;flex-wrap:wrap;align-items:center;gap:.6rem 2rem;padding:1.1rem max(1.5rem,calc((100% - 59rem)/2));background:color-mix(in srgb,var(--b1) 85%,transparent);backdrop-filter:blur(8px)}
.brand{font:italic 600 1.7rem/1 "Josefin Sans",sans-serif;color:var(--fg);text-decoration:none;margin-right:auto;letter-spacing:-.04em}
.top nav{display:flex;flex-wrap:wrap;gap:.4rem 1.8rem}.top nav a{font:400 .72rem var(--x);letter-spacing:.12em;text-transform:lowercase;color:var(--fg);text-decoration:none;opacity:.7}.top nav a:hover,.top nav a[aria-current]{opacity:1;text-decoration:underline}
.meta,.label,.exc,dt,.sub,.btn,.proof span,footer,.card>a{font-family:var(--x);font-size:.72rem;letter-spacing:.12em;line-height:1.9}
section{position:relative;isolation:isolate;padding:7rem 0 5rem}
section:before{content:"";position:absolute;z-index:-1;top:0;bottom:0;left:50%;width:100vw;transform:translateX(-50%);background:var(--b2)}
section:nth-of-type(odd):before{background:var(--b1)}
.hero{padding:3rem 0 5rem}.hero:after{content:"";position:absolute;z-index:-1;top:0;bottom:0;left:50%;width:100vw;transform:translateX(-50%);pointer-events:none;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1400 900' preserveAspectRatio='none'%3E%3Cg fill='none' stroke='%23000' stroke-opacity='.2'%3E%3Cpath d='M-50 520C300 140 900 160 1450 560'/%3E%3Cpath d='M-50 880C400 380 1000 420 1450 140'/%3E%3C/g%3E%3C/svg%3E") center/100% 100% no-repeat}
.subs{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem;margin-bottom:3rem}.sub{margin:0}
.lead{font-weight:300;font-size:clamp(1.25rem,2.4vw,1.7rem);line-height:1.5;max-width:40rem;margin:0 0 2.5rem}
.btn{display:inline-block;background:var(--fg);color:var(--b2);padding:.9rem 2.6rem;text-decoration:none;margin:0 1rem 1rem 0;border:1px solid var(--fg)}.btn.alt{background:none;color:var(--fg)}.btn:hover{opacity:.8}
.ghost{font-weight:200;font-size:clamp(3.6rem,15vw,10.5rem);line-height:.9;text-transform:uppercase;color:transparent;-webkit-text-stroke:1.2px var(--ghost);margin:-.4em 0 .15em -.04em;user-select:none}
.proof{padding:3.5rem 0}.proof{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:2rem}
.proof strong{display:block;font:200 clamp(1.8rem,3.5vw,2.6rem)/1.15 "Josefin Sans";text-transform:uppercase}.proof span{color:var(--mut)}
.three{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:2.5rem;counter-reset:n}.three>div{border-top:1px solid var(--line);padding-top:1rem;counter-increment:n}.three>div:before{content:"0" counter(n);font:400 .72rem var(--x);letter-spacing:.12em}.three p{color:var(--mut)}
.grid{display:block}.card{display:grid;grid-template-columns:1fr auto;gap:.1rem 2rem;border-bottom:1px solid var(--line);padding:1.8rem 0}.card>*{grid-column:1;margin:0}.card>a{grid-column:2;grid-row:1/span 3;align-self:center;color:var(--fg);text-decoration:none;border:1px solid var(--line);border-radius:50%/65%;padding:.5rem 1.4rem}.card>a:hover{background:var(--fg);color:var(--b2)}
.case{border-bottom:1px solid var(--line);padding:2rem 0;margin:0}.case>h2{margin:.2rem 0 .6rem;font-size:1.6rem}.case p{margin:.3rem 0}
.meta{color:var(--mut)}.card p,.case p{color:var(--fg)}
.label{display:inline-block;width:fit-content;border:1px solid var(--fg);padding:.15rem .7rem;margin:.7rem 0!important}.wip{color:var(--mut)}
.exc{color:var(--mut);margin-top:1rem!important}pre{margin:.4rem 0 1rem;padding:1rem 1.2rem;background:rgba(255,255,255,.35);border:1px solid var(--line);overflow-x:auto;font:.78rem/1.6 ui-monospace,Menlo,Consolas,monospace}code{font-family:inherit}
dl{margin:0}dt{margin-top:1rem;color:var(--mut)}dd{margin:.2rem 0 0}
.plain{list-style:none;padding:0}.plain li{border-bottom:1px solid var(--line);padding:.8rem 0}
.flow{list-style:none;padding:0;margin:3rem 0;counter-reset:s}.flow li{counter-increment:s;display:grid;grid-template-columns:5rem 1fr;border-bottom:1px solid var(--line);padding:1.4rem 0}.flow li:before{content:"0" counter(s);font:400 .72rem var(--x);letter-spacing:.12em;padding-top:.6rem}.flow li>*{grid-column:2;margin:0}.flow p{color:var(--mut)}
.about{display:grid;grid-template-columns:minmax(9rem,15rem) 1fr;gap:3rem;align-items:start;margin:2rem 0}.oval{aspect-ratio:3/4;border-radius:50%;background:var(--fg);color:var(--b2);display:grid;place-items:center;font:200 clamp(2.5rem,6vw,4rem) "Josefin Sans";letter-spacing:.04em}
img.oval{width:100%;height:auto;object-fit:cover;display:block;background:none}
.contact{border:1px solid var(--fg);padding:2rem;line-height:2.3;font-size:1.1rem}
footer{margin-top:5rem;padding-top:2rem;padding-bottom:3rem;text-align:center;border-top:1px solid var(--line)}footer p{display:flex;flex-wrap:wrap;justify-content:center;gap:.5rem 3rem;margin:.5rem 0}footer a{color:var(--fg);text-decoration:none}footer a:hover{text-decoration:underline}.copy{color:var(--mut)}
.js .rv{opacity:0;transform:translateY(14px);transition:opacity .7s ease,transform .7s ease}.js .rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.js .rv{opacity:1;transform:none;transition:none}}
@media(max-width:720px){header.top{gap:.3rem 1.4rem}.brand{width:100%;margin-right:0}.card{grid-template-columns:1fr}.card>a{grid-column:1;grid-row:auto;justify-self:start;margin-top:.8rem}.about{grid-template-columns:1fr}.oval{max-width:12rem}.flow li{grid-template-columns:3rem 1fr}h1{margin-top:3rem}}
''')
open("assets/main.js","w").write('''(function(){var r=document.documentElement;if("IntersectionObserver" in window&&!matchMedia("(prefers-reduced-motion:reduce)").matches){r.classList.add("js");var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{threshold:.08});document.querySelectorAll(".card,.case,.flow li,.three>div").forEach(function(el){el.classList.add("rv");io.observe(el)})}})();''')
open("README.md","w").write('''# Portfolio (GitHub Pages)

Static site: plain HTML, CSS, vanilla JS. Pages are generated by `build.py` (optional; you can also edit the HTML directly).

## Deploy
1. Create a public repo on GitHub, e.g. `shabnomm.github.io` (user site) or `portfolio` (project site).
2. Upload everything in this folder to the `main` branch (`git add . && git commit -m "Initial site" && git push`).
3. Repo **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main, folder: / (root)** → Save.
4. Wait about a minute. Site URL: `https://shabnomm.github.io/` or `https://shabnomm.github.io/portfolio/`.
5. Replace every `[ADD: ...]` placeholder (search the folder for `[ADD`), including the `og:url` meta tags, then push again.
''')
