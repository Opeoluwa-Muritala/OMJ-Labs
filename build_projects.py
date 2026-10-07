"""Generate static project pages from the curated portfolio cards."""

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).parent / "dist"
INDEX = ROOT / "index.html"
PROJECTS = [
    ("fieldcrm", "FieldCRM", "Field credit, clearly connected.", "A field agent and loan origination system for Mainstreet Microfinance Bank. The Android client and web platform connect the work from first lead through review and decision.", ["Lead capture", "Loan applications", "Review workflow"], "https://fieldlms.omjlabs.com/"),
    ("sabimarket", "SabiMarket", "A marketplace with every role in view.", "A mobile commerce experience built around buyers, sellers, and delivery riders. The project brings discovery, selling, and fulfillment into a shared Android workflow.", ["Browse products", "Seller workspace", "Delivery flow"], None),
    ("scholarnavigate", "ScholarNavigate", "A clearer week for students.", "A student task management app designed to make planning and prioritization easier. It focuses on everyday progress rather than complicated productivity rituals.", ["Plan the week", "Prioritize tasks", "Track progress"], None),
    ("ticket-api", "ticket-api", "Support requests, organized.", "A web helpdesk system designed for support tickets across multiple organizations. It gives teams a way to follow requests from opening through resolution.", ["Open a ticket", "Review status", "Resolve requests"], None),
    ("kflite", "kflite", "Small models, useful inputs.", "An open source contribution to a Kotlin Multiplatform library for on-device TensorFlow Lite. The work centers on a normalization layer that prepares input data for models.", ["Prepare input", "Normalize data", "Run on device"], None),
    ("event-response", "Event-Response", "Know what is happening nearby.", "A location-aware web application for finding nearby events and reporting incidents. Map-based discovery makes local information easier to place in context.", ["Explore the map", "Find events", "Report incidents"], "https://event-response.vercel.app/"),
    ("haven-check", "Haven Check", "More confidence in student housing.", "An API built to help students around the University of Ilorin consider rent fairness, utility reliability, and possible scam risk before choosing a place to live.", ["Compare rent", "Check utilities", "Assess risk"], None),
    ("songs-of-the-kingdom", "Songs of the Kingdom", "A quiet place for familiar songs.", "An offline-first Android hymnal with a public-domain catalog. Search, reader settings, and persistent favorites keep the reading experience useful without a connection.", ["Find a song", "Read offline", "Save favorites"], None),
    ("new-kuz", "New_Kuz", "Connection, made immediate.", "A real-time messaging app for the KUZ community. The Android project uses Kotlin and Jetpack Compose, with Firebase Authentication and Firestore for account and message flows and Room for local chat storage.", ["Sign in", "Message someone", "Manage chats"], None),
    ("shoppal", "ShopPal", "Commerce in the conversation.", "A conversational commerce platform for Nigerian merchants. A vendor portal supports catalog and order management while WhatsApp chat helps shoppers discover products.", ["Manage a catalog", "Discover in chat", "Follow orders"], "https://shoppals.omjlabs.com/"),
    ("aptus", "Aptus", "Find the fit.", "A recruitment and assessment portal for job applications, candidate screening, timed assessments, interviews, documents, and offers. Candidates and hiring teams each have a workspace for the process.", ["Apply for roles", "Take assessments", "Manage interviews"], "https://aptus.omjlabs.com/"),
]

index = INDEX.read_text(encoding="utf-8")
index = index.replace("Ten selected builds.", "Eleven selected builds.").replace("All <span>10</span>", "All <span>11</span>")

shop_card = '''          <article class="project-card project-shoppal" data-repo="ShopPal" data-categories="systems">
            <div class="project-visual visual-shoppal" aria-hidden="true"><div class="visual-caption"><span>CONVERSATIONAL COMMERCE</span><span>10</span></div><div class="shop-chat"><span>Find what you need.</span><strong>SHOP<span>PAL</span></strong><small>SELL IN THE CONVERSATION</small></div><div class="shop-dots"><i></i><i></i><i></i></div><span class="visual-footnote">Concept visual / commerce in chat</span></div>
            <div class="project-content"><div class="project-topline"><span>10 / Commerce</span><span class="repo-meta">TypeScript / GitHub</span></div><h3>ShopPal</h3><p>A conversational commerce platform for Nigerian merchants, with a vendor portal and WhatsApp product discovery.</p><div class="project-bottom"><div class="stack"><span>Next.js</span><span>FastAPI</span><span>WhatsApp</span></div><a class="source-link" href="https://github.com/Opeoluwa-Muritala/ShopPal" target="_blank" rel="noopener noreferrer">Source</a></div></div>
          </article>
'''
if 'project-shoppal' not in index:
    index = index.replace('          <article class="project-card project-recruit"', shop_card + '          <article class="project-card project-recruit"')

new_kuz_card = '''          <article class="project-card project-newkuz" data-repo="New_Kuz" data-categories="mobile">
            <div class="project-visual visual-newkuz" aria-hidden="true"><div class="visual-caption"><span>KUZ CHAT / ANDROID</span><span>09</span></div><div class="newkuz-mark"><img src="./assets/previews/new-kuz-logo.png" alt="" loading="lazy" /></div><span class="visual-footnote">KUZ identity / from the app repository</span></div>
            <div class="project-content"><div class="project-topline"><span>09 / Communication</span><span class="repo-meta">Kotlin / GitHub</span></div><h3>New_Kuz</h3><p>A real-time messaging app for the KUZ community, built with Kotlin, Jetpack Compose, Firebase, and Room.</p><div class="project-bottom"><div class="stack"><span>Kotlin</span><span>Compose</span><span>Firebase</span></div><a class="source-link" href="https://github.com/Opeoluwa-Muritala/New_Kuz" target="_blank" rel="noopener noreferrer" aria-label="View New_Kuz source on GitHub">Source</a></div></div>
          </article>'''
index = re.sub(r'<article class="project-card project-openchat".*?</article>', new_kuz_card.strip(), index, flags=re.S)
index = re.sub(r'<article class="project-card project-newkuz".*?</article>', new_kuz_card.strip(), index, flags=re.S)

index = index.replace('data-repo="" data-categories="systems">\n            <div class="project-visual visual-recruit"', 'data-repo="Quizz" data-categories="systems">\n            <div class="project-visual visual-recruit"')
index = index.replace('<span>OMJ LABS / AI-NATIVE PRODUCT</span><span>10</span>', '<span>OMJ LABS / RECRUITMENT</span><span>11</span>')
index = index.replace('<span class="recruit-r">R</span><div><span>RECRUITMENT</span><strong>AI<span class="recruit-dot">.</span></strong></div>', '<span class="recruit-r">A</span><div><span>RECRUITMENT</span><strong>APTUS<span class="recruit-dot">.</span></strong></div>')
index = index.replace('<span>10 / In the lab</span><span class="repo-meta">OMJ Labs product</span></div><h3>Recruitment AI</h3><p>A separate AI-native recruitment product from OMJ Labs. More product details will be added as they are confirmed.</p><div class="project-bottom"><div class="stack"><span>AI-native</span><span>Recruitment</span></div></div>', '<span>11 / Recruitment</span><span class="repo-meta">Python / GitHub</span></div><h3>Aptus</h3><p>A recruitment and assessment portal for applications, candidate screening, timed assessments, interviews, documents, and offers.</p><div class="project-bottom"><div class="stack"><span>Flask</span><span>PostgreSQL</span><span>Recruitment</span></div><a class="source-link" href="https://github.com/Opeoluwa-Muritala/Quizz" target="_blank" rel="noopener noreferrer">Source</a></div>')
index = index.replace('Our work includes FieldCRM and a separate Recruitment AI product', 'Our work includes FieldCRM and Aptus, a recruitment and assessment product').replace('<strong>Recruitment AI</strong>', '<strong>Aptus</strong>')

cards = re.findall(r'<article class="project-card\b.*?</article>', index, flags=re.S)
if len(cards) != len(PROJECTS):
    raise RuntimeError(f"Expected {len(PROJECTS)} cards, found {len(cards)}")

pages_dir = ROOT / "projects"
pages_dir.mkdir(exist_ok=True)

for number, ((slug, title, tagline, description, features, live), card) in enumerate(zip(PROJECTS, cards), 1):
    visual = re.search(r'<div class="project-visual\b.*?</div>(?=\s*<div class="project-content")', card, flags=re.S)
    if not visual:
        raise RuntimeError(f"Missing visual for {slug}")
    visual_html = visual.group(0).replace('src="./assets/', 'src="../assets/')
    summary = re.search(r'<h3>.*?</h3><p>(.*?)</p>', card, flags=re.S).group(1)
    stack = re.search(r'<div class="stack">(.*?)</div>', card, flags=re.S).group(1)
    source = re.search(r'href="(https://github.com/[^"]+)"', card)
    links = (f'<a class="detail-button" href="{escape(live)}" target="_blank" rel="noopener noreferrer">Visit live site ↗</a>' if live else '')
    if source:
        links += f'<a class="detail-button detail-button-outline" href="{escape(source.group(1))}" target="_blank" rel="noopener noreferrer">Explore source ↗</a>'
    screens = ''.join(f'<div class="preview-screen"><div class="preview-bar"><span></span><span></span><span></span></div><div class="preview-body"><small>OMJ LABS / {number:02d}</small><strong>{escape(feature)}</strong><div class="preview-line"></div><div class="preview-line short"></div><div class="preview-block"></div><div class="preview-line"></div></div></div>' for feature in features)
    live_screen = f'<figure class="live-screen"><img src="../assets/previews/{slug}.png" alt="Current public landing screen of {escape(title)}" loading="lazy"><figcaption>Live product screen / <a href="{escape(live)}" target="_blank" rel="noopener noreferrer">Open website ↗</a></figcaption></figure>' if live else ''
    if slug == 'scholarnavigate':
        live_screen = '<div class="mobile-screens" aria-label="Screenshots from the ScholarNavigate repository">' + ''.join(f'<figure><img src="../assets/previews/scholarnavigate-{name}.jpg" alt="ScholarNavigate {name} screen" loading="lazy"><figcaption>{name.title()} / repository screenshot</figcaption></figure>' for name in ['login', 'dashboard', 'calendar', 'timer']) + '</div>'
    preview_intro = 'Screenshots from the project repository, followed by concept screens showing the main flows.' if slug == 'scholarnavigate' else ('A captured screen from the live product, followed by concept screens illustrating the main parts of the experience.' if live else 'Concept screens illustrating the main parts of the experience.')
    previous = PROJECTS[number - 2] if number > 1 else PROJECTS[-1]
    next_project = PROJECTS[number] if number < len(PROJECTS) else PROJECTS[0]
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#111b1d"><meta name="description" content="{escape(summary, quote=True)}"><title>{escape(title)} — OMJ Labs</title><link rel="icon" href="../favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><link rel="stylesheet" href="../project.css"><script src="../loading-3d.js" type="module"></script></head>
<body class="project-page detail-{slug}"><a class="skip-link" href="#main">Skip to content</a><div class="site-loader" aria-hidden="true"><div class="loader-stage"><div class="loader-art"><img src="../assets/omj-mark.svg" alt="" /></div><strong>OMJ <span>LABS</span></strong><small>IDEAS INTO USEFUL THINGS</small><span class="loader-track"><i></i></span></div></div><div class="site-shell"><header class="site-header"><a class="brand" href="../index.html" aria-label="OMJ Labs home"><img class="brand-emblem" src="../assets/omj-mark.svg" alt="" /><span class="brand-mark">OMJ<span>.</span></span><span class="brand-caption">LABS / PORTFOLIO</span></a><nav class="site-nav" aria-label="Main navigation"><a href="../index.html#work">Work</a><a href="../index.html#studio">Studio</a><a href="../index.html#experience">Experience</a></nav><a class="header-link" href="../index.html#work">All projects ↗</a></header>
<main id="main"><section class="detail-hero"><div class="detail-overline"><a href="../index.html#work">← All work</a><span>PROJECT {number:02d} / {len(PROJECTS):02d}</span></div><div class="detail-heading"><div><p class="detail-kicker">SELECTED WORK / OMJ LABS</p><h1>{escape(title)}<span>.</span></h1></div><p>{escape(tagline)}</p></div><div class="detail-intro"><p>{escape(summary)}</p><div class="detail-links">{links}</div></div></section>
<section class="detail-feature" aria-label="{escape(title)} visual preview">{visual_html}</section>
<section class="detail-story"><div><span class="detail-label">01 / THE PROJECT</span><h2>What it does<span>.</span></h2></div><div><p>{escape(description)}</p><div class="detail-stack"><span>BUILT WITH</span><div class="stack">{stack}</div></div></div></section>
<section class="detail-preview"><div class="detail-preview-heading"><div><span class="detail-label">02 / INTERFACE PREVIEW</span><h2>Inside the flow<span>.</span></h2></div><p>{preview_intro}</p></div>{live_screen}<div class="preview-grid">{screens}</div></section>
<nav class="detail-next" aria-label="Other projects"><a href="{previous[0]}.html"><small>← PREVIOUS PROJECT</small><strong>{escape(previous[1])}</strong></a><a href="{next_project[0]}.html"><small>NEXT PROJECT →</small><strong>{escape(next_project[1])}</strong></a></nav></main><footer class="site-footer"><a href="../index.html">OMJ Labs</a><span>Opeoluwa Muritala Joel</span></footer></div></body></html>'''
    page = page.replace('../index.html#', '../#').replace('../index.html', '../')
    (pages_dir / f"{slug}.html").write_text(page, encoding="utf-8")
    if f'href="./projects/{slug}.html"' not in card:
        replacement = card.replace('<h3>', f'<h3><a class="project-title-link" href="./projects/{slug}.html">', 1).replace('</h3>', '</a></h3>', 1)
        replacement = replacement.replace('<div class="project-bottom">', f'<a class="case-link" href="./projects/{slug}.html">View project story <span aria-hidden="true">↗</span></a><div class="project-bottom">', 1)
        if live:
            replacement = replacement.replace('<div class="project-bottom">', f'<div class="project-bottom"><a class="source-link live-link" href="{live}" target="_blank" rel="noopener noreferrer" aria-label="Open {escape(title)} live website">Live ↗</a>', 1)
        index = index.replace(card, replacement)

INDEX.write_text(index, encoding="utf-8")
