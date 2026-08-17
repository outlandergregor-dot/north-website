#!/usr/bin/env python3
"""Applies approved Phase 1 public-trust corrections to the static NORTH site."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_STORE = "https://apps.apple.com/us/app/north-find-your-north/id6757988392"
OLD_APP_STORE = "https://apps.apple.com/app/north/id6742574901"


def replace_required(text: str, old: str, new: str, source: Path) -> str:
    if old not in text:
        raise RuntimeError(f"Expected source fragment was not found in {source}: {old[:80]!r}")
    return text.replace(old, new)


def remove_google_play_anchors(text: str) -> str:
    return re.sub(
        r"\s*<a\b[^>]*href=\"https://play\.google\.com/store/apps/details\?id=[^\"]+\"[^>]*>.*?</a>",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )


def write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace(OLD_APP_STORE, APP_STORE)
    text = remove_google_play_anchors(text)

    text = replace_required(
        text,
        '    <meta name="description" content="NORTH is your AI Life Operating System. Plan your day with Captain AI, focus with the 1-3-5 system, track your Safe Number, and build unstoppable momentum. Available in 14 languages. Free 7-day trial.">',
        '    <meta name="description" content="NORTH is an AI Life Operating System for planning a day, focusing on priorities, organizing money information, and noticing progress. Explore it on the App Store.">',
        path,
    )
    text = re.sub(
        r"\n\s*<!-- Hreflang:.*?\n\s*<link rel=\"alternate\" hreflang=\"x-default\" href=\"https://www\.yournorth\.app/\">",
        '\n    <!-- Phase 1 public website language: English only. -->\n    <link rel="alternate" hreflang="en" href="https://www.yournorth.app/">\n    <link rel="alternate" hreflang="x-default" href="https://www.yournorth.app/">',
        text,
        flags=re.DOTALL,
    )
    text = text.replace('Free 7-day trial.', 'Available on the App Store.')
    text = text.replace('7 days, no credit card', 'View current App Store terms')
    text = text.replace('14 languages supported', 'English website release')
    text = text.replace('"operatingSystem": "iOS, Android"', '"operatingSystem": "iOS"')
    text = text.replace('"description": "NORTH is your AI Life Operating System. Plan your day with Captain AI, focus with the proven 1-3-5 system, know your Safe Number, and build unstoppable momentum — in 14 languages."', '"description": "NORTH is an AI Life Operating System for planning a day, focusing on priorities, organizing money information, and noticing progress."')
    text = text.replace('"inLanguage": ["en","es","pt","fr","de","it","nl","sv","no","pl","tr","ar","ja","ko"],', '"inLanguage": ["en"],')
    text = text.replace('"description": "Free to download with 7-day free trial",', '"description": "Free to download. Current terms are displayed by the App Store.",')
    text = re.sub(r',\n\s*"aggregateRating": \{.*?\n\s*\}', '', text, flags=re.DOTALL)
    text = text.replace('"Safe Number — financial freedom tracking",', '"Safe Number — money-organization tracking",')
    text = text.replace('"14 Languages — full multilingual AI support"', '"English web release — additional web translations are not published"')
    text = text.replace('"text": "NORTH is an AI Life Operating System — a mobile app that helps you plan your day with Captain AI, focus with the 1-3-5 system, track your financial freedom number (Safe Number), and build unstoppable momentum. Available in 14 languages on iOS and Android."', '"text": "NORTH is an AI Life Operating System — an iPhone app that helps people plan a day, use the 1-3-5 system, organize Safe Number information, and notice progress. It is not professional advice."')
    text = text.replace('"text": "Your Safe Number (also called Freedom Number) is the monthly income that covers your essential needs and gives you financial peace of mind. NORTH helps you calculate it, track your progress toward it, and stay motivated every single day."', '"text": "Safe Number is a money-organization feature. It is not individualized financial, tax, investment, lending, insurance, legal, debt, or credit advice."')
    text = text.replace('"text": "NORTH supports 14 languages: English, Spanish, Portuguese, French, German, Italian, Dutch, Swedish, Norwegian, Polish, Turkish, Arabic, Japanese, and Korean. The app detects your device language automatically — no setup needed."', '"text": "The NORTH public website and Library launch in English. Language availability in the app may vary and is shown in the app."')
    text = text.replace('"text": "Yes. NORTH is free to download on iOS and Android with a 7-day free trial. No credit card is required to start."', '"text": "NORTH is available to download on the App Store. Current purchase and trial terms, where offered, are presented by Apple."')
    text = text.replace('                <a href="#newsletter" onclick="closeMobileNav()">Newsletter</a>\n', '')
    text = text.replace('                <a href="support.html" onclick="closeMobileNav()">Support</a>', '                <a href="/library" onclick="closeMobileNav()">Library</a>\n                <a href="support.html" onclick="closeMobileNav()">Support</a>')
    text = text.replace('<!-- Language Strip -->\n<div class="lang-strip" aria-hidden="true">\n    <div class="lang-strip-inner">\n        <span>🇺🇸 English</span><span>🇪🇸 Español</span><span>🇧🇷 Português</span>\n        <span>🇫🇷 Français</span><span>🇩🇪 Deutsch</span><span>🇮🇹 Italiano</span>\n        <span>🇳🇱 Nederlands</span><span>🇸🇪 Svenska</span><span>🇳🇴 Norsk</span>\n        <span>🇵🇱 Polski</span><span>🇹🇷 Türkçe</span><span>🇸🇦 العربية</span>\n        <span>🇯🇵 日本語</span><span>🇰🇷 한국어</span>\n        <!-- duplicate for seamless loop -->\n        <span>🇺🇸 English</span><span>🇪🇸 Español</span><span>🇧🇷 Português</span>\n        <span>🇫🇷 Français</span><span>🇩🇪 Deutsch</span><span>🇮🇹 Italiano</span>\n        <span>🇳🇱 Nederlands</span><span>🇸🇪 Svenska</span><span>🇳🇴 Norsk</span>\n        <span>🇵🇱 Polski</span><span>🇹🇷 Türkçe</span><span>🇸🇦 العربية</span>\n        <span>🇯🇵 日本語</span><span>🇰🇷 한국어</span>\n    </div>\n</div>\n\n', '')
    text = text.replace('                <a href="#newsletter">Newsletter</a>\n', '')
    text = text.replace('                <a href="support.html">Support</a>', '                <a href="/library">Library</a>\n                <a href="support.html">Support</a>')
    text = text.replace('                    <div class="store-badges">\n                        <span style="color: var(--white-40); font-size: 12px; align-self: center;">7-day free trial · No credit card required</span>\n                    </div>', '                    <div class="store-badges">\n                        <span style="color: var(--white-40); font-size: 12px; align-self: center;">Available on the App Store · Current terms shown by Apple</span>\n                    </div>')
    text = re.sub(r'<!-- Stats -->.*?<!-- Problem → Solution Story -->', '<!-- Phase 1 trust preflight: unsupported app-rating, platform, language, and trial stats removed. -->\n\n<!-- Problem → Solution Story -->', text, flags=re.DOTALL)
    text = text.replace('Captain AI plans your perfect day every morning', 'Captain AI helps you organize a practical plan for the day')
    text = text.replace('Safe Number tracks your path to financial freedom', 'Safe Number helps you organize money information you choose to track')
    text = text.replace('Weekly Compass realigns you every Sunday', 'Weekly Compass supports a regular review ritual')
    text = text.replace('Momentum tracking builds unstoppable streaks', 'Momentum tracking helps you notice completed wins')
    text = text.replace('Know the income number that unlocks your financial freedom. Track your progress toward the number that matters most.', 'Organize the monthly essentials and figures you choose to track. NORTH is a planning tool, not individualized financial advice.')
    text = text.replace('<h3>14 Languages</h3>\n                <p>NORTH speaks your language. Every AI insight, suggestion, and guidance is delivered in your chosen language — instantly.</p>', '<h3>Weekly Compass</h3>\n                <p>Set aside a regular moment to reflect on what moved, what felt difficult, and what you want to bring forward.</p>')
    text = text.replace('Your AI Guide That Plans Your Day', 'Your AI Guide for Daily Planning')
    text = text.replace("Captain AI analyzes your goals, energy, and schedule to suggest the best path forward. It's not just a task list — it's an intelligent guide that adapts to you.", "Captain AI can help you organize a daily plan around the information you choose to provide. It is a planning tool, not professional advice or a guarantee of results.")
    text = text.replace('Personalized daily briefings every morning', 'Daily planning prompts based on information you provide')
    text = text.replace('Responds in your chosen language instantly', 'Designed to help organize a practical next step')
    text = text.replace('Learns your patterns to improve over time', 'Supports a focused daily-planning routine')
    text = text.replace('The 1-3-5 method is the most effective daily planning framework ever created. NORTH implements this system automatically so you always know exactly what to work on.', 'The 1-3-5 method is a simple daily planning framework: one Big Thing, three supporting tasks, and five quick wins. NORTH can help you use the structure without promising an outcome.')
    text = text.replace('Never feel overwhelmed or directionless again', 'Use a smaller, intentional planning structure')
    text = text.replace('Know the Number That Sets You Free', 'Organize the Essentials You Want to See')
    text = text.replace('Your Safe Number is the monthly income that covers your essential needs and gives you peace of mind. NORTH helps you track it, visualize your progress, and stay motivated.', 'Safe Number helps you organize essential monthly figures you choose to track. It is for general organization and does not provide individualized financial, tax, investment, lending, insurance, legal, debt, or credit advice.')
    text = text.replace('Calculate your personal financial freedom number', 'Organize essential monthly figures')
    text = text.replace('Track income sources and progress', 'Review entries you choose to track')
    text = text.replace('Visual runway calculator and freedom timeline', 'Use figures as a personal organization reference')
    text = text.replace('Stay motivated with clear financial milestones', 'Speak with a qualified professional for advice tailored to you')
    text = text.replace('Generates your perfect day', 'Helps organize a daily plan')
    text = text.replace('Know your freedom target', 'Organize figures you choose to track')
    text = text.replace('Weekly clarity, productivity insights, and focus strategies for ambitious people. Join thousands building momentum every week.', 'Newsletter delivery is not active yet. NORTH will publish a clear opt-in when a consented delivery system is ready.')
    text = re.sub(r'<!-- Newsletter -->.*?<!-- Languages -->', '<!-- Phase 1 trust preflight: browser-only newsletter capture removed until a consented provider is configured. -->\n\n<!-- Languages -->', text, flags=re.DOTALL)
    text = re.sub(r'<!-- Languages -->.*?<!-- Download CTA -->', '<!-- Phase 1 language registry: public web and Library launch in English only. -->\n\n<!-- Download CTA -->', text, flags=re.DOTALL)
    text = text.replace('Download NORTH today and start focusing on what truly matters — in your language, on your terms.', 'Download NORTH from the App Store to explore the current app experience and terms.')
    text = text.replace('7-day free trial · No credit card required · Available in 14 languages', 'Available on iPhone · Current terms shown by Apple')
    text = text.replace('<li><a href="#newsletter">Newsletter</a></li>\n', '')
    text = text.replace('                <h4>Explore</h4>\n                <ul>', '                <h4>Explore</h4>\n                <ul>\n                    <li><a href="/library">NORTH Library</a></li>')
    text = text.replace('<p>Available on iOS &amp; Android · 14 Languages · 174 Countries</p>', '<p>Available on iPhone · Website and Library launch in English</p>')
    text = re.sub(r'// ── Newsletter Submit ──.*?// ── Lazy load', '// ── Newsletter capture intentionally disabled in Phase 1 ──\n\n// ── Lazy load', text, flags=re.DOTALL)
    library_section = '''<!-- NORTH Library Bridge -->
<section class="library-bridge" id="library">
    <div class="container">
        <div class="section-header centered">
            <div class="section-eyebrow">✦ NORTH Library</div>
            <h2 class="section-title">Take NORTH Beyond the App</h2>
            <p class="section-sub">A calm collection of practical tools and future learning formats. Start with one clear next step.</p>
        </div>
        <div class="library-bridge-grid">
            <a class="library-bridge-card" href="/library/free-tools"><span>✦</span><h3>Free Tools</h3><p>Start with one clear next step.</p><small>Explore free tools →</small></a>
            <a class="library-bridge-card" href="/library/resources"><span>◇</span><h3>Resources</h3><p>Practical tools you can use today.</p><small>Explore resources →</small></a>
            <a class="library-bridge-card" href="/library/programs"><span>↗</span><h3>Programs</h3><p>Guided resets with a defined finish line.</p><small>Explore programs →</small></a>
            <a class="library-bridge-card" href="/library/books"><span>○</span><h3>Books &amp; Audio</h3><p>The NORTH method in a durable format.</p><small>Explore books &amp; audio →</small></a>
        </div>
        <div style="text-align:center; margin-top:28px;"><a href="/library" class="btn-outline">Visit the NORTH Library</a></div>
    </div>
</section>
'''
    if library_section not in text:
        text = replace_required(text, '</section>\n\n<!-- App Store Rating -->', '</section>\n\n' + library_section + '\n<!-- App Store Rating -->', path)
    text = re.sub(r'<!-- App Store Rating -->.*?<!-- Use Cases -->', '<!-- Phase 1 trust preflight: unsupported rating and testimonial content removed. -->\n\n<!-- Use Cases -->', text, flags=re.DOTALL)
    bridge_css = '''
        /* ── NORTH Library Bridge ── */
        .library-bridge { background: var(--navy-deep); }
        .library-bridge-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
        .library-bridge-card { display: block; min-height: 218px; padding: 28px 24px; border: 1px solid rgba(255,255,255,0.10); border-radius: var(--radius-lg); background: linear-gradient(145deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02)); color: var(--white); text-decoration: none; transition: transform var(--transition), border-color var(--transition); }
        .library-bridge-card:hover { transform: translateY(-4px); border-color: var(--gold-border); }
        .library-bridge-card > span { display: block; color: var(--gold); font-size: 26px; margin-bottom: 28px; }
        .library-bridge-card h3 { margin-bottom: 8px; font-size: 18px; }
        .library-bridge-card p { color: var(--white-60); font-size: 14px; line-height: 1.6; }
        .library-bridge-card small { display: block; margin-top: 18px; color: var(--gold-light); font-weight: 700; }
        @media (max-width: 900px) { .library-bridge-grid { grid-template-columns: 1fr 1fr; } }
        @media (max-width: 600px) { .library-bridge-grid { grid-template-columns: 1fr; } .library-bridge-card { min-height: 0; } }
'''
    text = replace_required(text, '        /* ── Stats ── */', bridge_css + '\n        /* ── Stats ── */', path)
    write(path, text)


def update_support() -> None:
    path = ROOT / "support.html"
    text = path.read_text(encoding="utf-8").replace(OLD_APP_STORE, APP_STORE)
    text = remove_google_play_anchors(text)
    faq = '''<!-- FAQ -->
<section id="faq" class="faq-section">
    <div class="container">
        <p class="section-label">Frequently Asked Questions</p>
        <h2 class="section-title">Support and Public Information</h2>
        <div class="faq-container" id="faqContainer">
            <div class="faq-item"><div class="faq-question" onclick="toggleFAQ(this)">What is NORTH?<span class="faq-icon">+</span></div><div class="faq-answer"><p>NORTH is an AI Life Operating System for planning a day, focusing on priorities, organizing information you choose to track, and noticing progress. It is not a life coach, therapist, or financial advisor.</p></div></div>
            <div class="faq-item"><div class="faq-question" onclick="toggleFAQ(this)">Where is NORTH available?<span class="faq-icon">+</span></div><div class="faq-answer"><p>NORTH is currently available through the Apple App Store. We do not list an Android download until a live Google Play listing is verified.</p></div></div>
            <div class="faq-item"><div class="faq-question" onclick="toggleFAQ(this)">What is the 1-3-5 system?<span class="faq-icon">+</span></div><div class="faq-answer"><p>The 1-3-5 system is a simple planning framework: one Big Thing, three supporting tasks, and five quick wins. It is a planning structure, not a guarantee of results.</p></div></div>
            <div class="faq-item"><div class="faq-question" onclick="toggleFAQ(this)">What is Safe Number?<span class="faq-icon">+</span></div><div class="faq-answer"><p>Safe Number is a money-organization feature. It does not provide individualized financial, tax, investment, lending, insurance, legal, debt, or credit advice. For guidance tailored to your circumstances, consult a qualified professional.</p></div></div>
            <div class="faq-item"><div class="faq-question" onclick="toggleFAQ(this)">Where can I see current app price or trial terms?<span class="faq-icon">+</span></div><div class="faq-answer"><p>Current app purchase and trial terms, where offered, are presented by Apple on the App Store purchase screen. NORTH does not publish a separate web checkout in Phase 1.</p></div></div>
            <div class="faq-item"><div class="faq-question" onclick="toggleFAQ(this)">How do I cancel or request an iOS refund?<span class="faq-icon">+</span></div><div class="faq-answer"><p>Manage an iOS subscription through your Apple ID subscription settings. Apple handles refund requests under its policies; visit <a href="https://reportaproblem.apple.com" target="_blank" rel="noopener">reportaproblem.apple.com</a> to start a request.</p></div></div>
            <div class="faq-item"><div class="faq-question" onclick="toggleFAQ(this)">What languages are available on this website?<span class="faq-icon">+</span></div><div class="faq-answer"><p>The public website and NORTH Library launch in English. NORTH will publish additional web languages only after their product pages, support, legal content, delivery, and visual review are complete.</p></div></div>
        </div>
    </div>
</section>

'''
    text = re.sub(r'<!-- FAQ -->.*?<!-- Contact -->', faq + '<!-- Contact -->', text, flags=re.DOTALL)
    text = text.replace('Our team typically responds within 24 hours. Include your device type and app version for faster help.', 'Tell us what you need help with, your device type, and the app version if relevant.')
    text = text.replace('mailto:support@yournorth.app', 'mailto:hello@yournorth.app')
    cta = f'''<!-- CTA -->
<section class="cta-banner">
    <div class="container">
        <h2>Ready to <span>Find Your North?</span></h2>
        <p>Explore NORTH on the App Store. Current purchase and trial terms, where offered, are shown by Apple.</p>
        <div class="cta-buttons"><a href="{APP_STORE}" class="btn-gold" target="_blank" rel="noopener">View on the App Store</a></div>
    </div>
</section>

<!-- Footer -->'''
    text = re.sub(r'<!-- CTA -->.*?<!-- Footer -->', cta, text, flags=re.DOTALL)
    text = text.replace('<p>Available on iOS &amp; Android &middot; 14 Languages &middot; 174 Countries</p>', '<p>Available on iPhone &middot; Website and Library launch in English</p>')
    write(path, text)


def update_terms() -> None:
    path = ROOT / "terms.html"
    text = path.read_text(encoding="utf-8").replace(OLD_APP_STORE, APP_STORE)
    text = remove_google_play_anchors(text)
    billing = '''<h2>4. App Subscription Plans and Billing</h2>

                    <h3>4.1 App Store Purchases</h3>
                    <p>Where app subscriptions or trials are offered, the current price, renewal terms, trial availability, and purchase conditions are shown by Apple before you complete an in-app purchase. NORTH does not offer a separate web checkout in Phase 1.</p>

                    <h3>4.2 Cancellation</h3>
                    <p>You can manage an iOS subscription through your Apple ID subscription settings. The effect of cancellation and continued access are governed by the terms presented by Apple for your purchase.</p>

                    <h3>4.3 Refund Requests</h3>
                    <p>Apple handles iOS refund requests under its own policies. To start a request, visit <a href="https://reportaproblem.apple.com" target="_blank" rel="noopener">reportaproblem.apple.com</a>. You may contact <a href="mailto:hello@yournorth.app">hello@yournorth.app</a> for general support, but NORTH cannot promise a refund decision.</p>

                    '''
    text = re.sub(r'<h2>4\. Subscription Plans and Billing</h2>.*?<h2>5\. Acceptable Use</h2>', billing + '<h2>5. Acceptable Use</h2>', text, flags=re.DOTALL)
    text = text.replace('<h2>7. The Navigator and AI Features</h2>', '<h2>7. Captain AI and Planning Features</h2>')
    text = text.replace('The Navigator, voice assistant, and other AI-powered features in NORTH provide personalized productivity guidance based on your input and usage patterns. These features are designed to help you organize tasks and make decisions, but they:', 'Captain AI and other AI-powered planning features may provide organizational prompts based on information you choose to provide. They are designed to support planning, but they:')
    text = text.replace('The Navigator or any other feature', 'Captain AI or any other feature')
    text = text.replace('mailto:support@yournorth.app', 'mailto:hello@yournorth.app')
    write(path, text)


def update_privacy() -> None:
    path = ROOT / "privacy.html"
    text = path.read_text(encoding="utf-8").replace(OLD_APP_STORE, APP_STORE)
    text = remove_google_play_anchors(text)
    text = text.replace('<li><strong>Language Preference:</strong> Your selected app language from the 14 supported languages</li>', '<li><strong>Language Preference:</strong> Your selected app language, where available</li>')
    text = text.replace('<li><strong>Optimization Track:</strong> Your chosen track (Focus, Career, Money, Health, or Balance)</li>\n', '')
    text = text.replace('<li><strong>Website:</strong> <a href="support.html">yournorth.app/support</a></li>', '<li><strong>Website:</strong> <a href="support.html">yournorth.app/support</a></li>')
    text = text.replace('<p>Available on iOS &amp; Android &middot; 14 Languages &middot; 174 Countries</p>', '<p>Available on iPhone &middot; Website and Library launch in English</p>')
    write(path, text)


def update_legacy_pages() -> None:
    for path in ROOT.glob('*.html'):
        if path.name in {'index.html', 'support.html', 'terms.html', 'privacy.html'} or path.name.startswith('library'):
            continue
        text = path.read_text(encoding='utf-8').replace(OLD_APP_STORE, APP_STORE)
        text = remove_google_play_anchors(text)
        text = text.replace('financial freedom', 'financial clarity')
        text = text.replace('Financial Freedom', 'Financial Clarity')
        text = text.replace('plans your perfect day', 'helps organize a daily plan')
        text = text.replace('Plans Your Perfect Day', 'Helps Organize a Daily Plan')
        text = text.replace('most effective', 'simple')
        text = text.replace('Most Effective', 'Simple')
        write(path, text)


def main() -> None:
    update_index()
    update_support()
    update_terms()
    update_privacy()
    update_legacy_pages()
    print('Phase 1 public-trust updates applied.')


if __name__ == '__main__':
    main()
