"""
Chapter 3: CSS — The Paint and Interior Design
From Zero to Principal Engineer: The Complete Web Development Mastery Course
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


# ============================================================================
# SECTION 3.1 — What CSS Does and How It Connects to HTML
# ============================================================================

def section_3_1(styles):
    s = []
    s.append(h1("3.1 What CSS Does and How It Connects to HTML", styles))
    s.append(p(
        "HTML gives your web page structure — headings, paragraphs, images, buttons. "
        "But if you loaded a plain HTML page in your browser right now, it would look like "
        "a plain text document from 1993. No colors. No layout. No fonts. No visual hierarchy. "
        "That is where CSS — Cascading Style Sheets — comes in. CSS is the language that tells "
        "the browser how every element should look and where it should sit on the screen.",
        styles
    ))
    s.append(analogy_box(
        "If HTML is the frame of a house — the walls, floors, and roof — then CSS is the "
        "interior designer. Two houses built from identical blueprints can look completely "
        "different depending on who decorates them. One might have white walls, minimalist "
        "furniture, and track lighting. The other might have dark wood panels, Persian rugs, "
        "and warm Edison bulbs. Same skeleton. Completely different experience. That is exactly "
        "what CSS does to HTML.",
        styles
    ))
    s.append(h2("Three Ways to Add CSS", styles))
    s.append(p(
        "CSS can be connected to your HTML document in three ways: inline styles, an internal "
        "style block, and an external stylesheet. Understanding the difference — and why one "
        "approach wins every time in production — is fundamental.",
        styles
    ))
    s.append(h3("Method 1: Inline Styles", styles))
    s.append(p(
        "Inline styles are written directly on an HTML element using the <b>style</b> attribute. "
        "They apply only to that single element and have the highest specificity of any CSS rule "
        "(short of !important). They look like this:",
        styles
    ))
    s.append(code_block(
        '<!-- inline-style.html -->\n'
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <title>Inline Style Example</title>\n'
        '</head>\n'
        '<body>\n'
        '    <h1 style="color: #e94560; font-size: 2rem; text-align: center;">\n'
        '        TradeBoard — Live Markets\n'
        '    </h1>\n'
        '    <p style="color: #555555; font-family: Georgia, serif; line-height: 1.7;">\n'
        '        Real-time stock prices updated every second.\n'
        '    </p>\n'
        '    <button style="background-color: #0f3460; color: white; padding: 10px 20px;\n'
        '                   border: none; border-radius: 4px; cursor: pointer;">\n'
        '        View Portfolio\n'
        '    </button>\n'
        '</body>\n'
        '</html>',
        filename='inline-style.html',
        styles=styles
    ))
    s.append(mistake_box(
        "Inline styles should almost never appear in production code. They are impossible to "
        "reuse, they bloat your HTML, they are a nightmare to maintain, and they cannot be "
        "overridden by external stylesheets without resorting to !important hacks. The only "
        "legitimate use for inline styles in modern web development is when JavaScript "
        "dynamically sets a style value that must be computed at runtime — and even then, "
        "CSS custom properties are often a cleaner solution.",
        styles
    ))
    s.append(h3("Method 2: Internal Style Block", styles))
    s.append(p(
        "The <b>&lt;style&gt;</b> tag lives inside your &lt;head&gt; and contains CSS rules "
        "that apply to the current page only. This is better than inline styles for "
        "single-page demos or email templates, but still not ideal for multi-page sites:",
        styles
    ))
    s.append(code_block(
        '<!-- internal-style.html -->\n'
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <title>Internal Style Example</title>\n'
        '    <style>\n'
        '        /* These rules apply to this page only */\n'
        '        body {\n'
        '            font-family: system-ui, -apple-system, sans-serif;\n'
        '            background-color: #f4f4f8;\n'
        '            margin: 0;\n'
        '            padding: 2rem;\n'
        '        }\n'
        '\n'
        '        h1 {\n'
        '            color: #1a1a2e;\n'
        '            font-size: 2.5rem;\n'
        '            margin-bottom: 0.5rem;\n'
        '        }\n'
        '\n'
        '        .stock-card {\n'
        '            background: white;\n'
        '            border-radius: 8px;\n'
        '            padding: 1.5rem;\n'
        '            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);\n'
        '            margin-bottom: 1rem;\n'
        '        }\n'
        '\n'
        '        .price-up {\n'
        '            color: #22c55e;\n'
        '            font-weight: bold;\n'
        '        }\n'
        '\n'
        '        .price-down {\n'
        '            color: #ef4444;\n'
        '            font-weight: bold;\n'
        '        }\n'
        '    </style>\n'
        '</head>\n'
        '<body>\n'
        '    <h1>TradeBoard</h1>\n'
        '    <div class="stock-card">\n'
        '        <h2>AAPL — Apple Inc.</h2>\n'
        '        <p>Price: $182.50 <span class="price-up">+2.3%</span></p>\n'
        '    </div>\n'
        '    <div class="stock-card">\n'
        '        <h2>TSLA — Tesla Inc.</h2>\n'
        '        <p>Price: $248.10 <span class="price-down">-1.1%</span></p>\n'
        '    </div>\n'
        '</body>\n'
        '</html>',
        filename='internal-style.html',
        styles=styles
    ))
    s.append(h3("Method 3: External Stylesheet (The Winner)", styles))
    s.append(p(
        "An external stylesheet is a separate <b>.css</b> file linked to your HTML via a "
        "&lt;link&gt; tag in the &lt;head&gt;. This is the correct approach for any real project. "
        "The browser downloads the CSS file once and caches it — so every subsequent page on your "
        "site loads faster. Your styles live in one place, so changing a color updates the whole "
        "site instantly. Your HTML stays clean and readable.",
        styles
    ))
    s.append(code_block(
        '<!-- index.html -->\n'
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '    <title>TradeBoard</title>\n'
        '    <!-- Link to external stylesheet -->\n'
        '    <link rel="stylesheet" href="styles/main.css">\n'
        '</head>\n'
        '<body>\n'
        '    <header class="site-header">\n'
        '        <h1 class="logo">TradeBoard</h1>\n'
        '        <nav class="main-nav">...</nav>\n'
        '    </header>\n'
        '    <main class="dashboard">...</main>\n'
        '</body>\n'
        '</html>',
        filename='index.html',
        styles=styles
    ))
    s.append(code_block(
        '/* styles/main.css */\n'
        '\n'
        '/* 1. Custom properties (design tokens) */\n'
        ':root {\n'
        '    --color-primary: #1a1a2e;\n'
        '    --color-accent: #e94560;\n'
        '    --color-surface: #ffffff;\n'
        '    --color-bg: #f4f4f8;\n'
        '    --font-sans: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n'
        '    --radius-card: 8px;\n'
        '    --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.1);\n'
        '    --spacing-md: 1rem;\n'
        '    --spacing-lg: 2rem;\n'
        '}\n'
        '\n'
        '/* 2. Global resets */\n'
        '*, *::before, *::after {\n'
        '    box-sizing: border-box;\n'
        '}\n'
        '\n'
        'body {\n'
        '    font-family: var(--font-sans);\n'
        '    background-color: var(--color-bg);\n'
        '    color: var(--color-primary);\n'
        '    margin: 0;\n'
        '    line-height: 1.6;\n'
        '}\n'
        '\n'
        '/* 3. Component styles */\n'
        '.site-header {\n'
        '    background-color: var(--color-primary);\n'
        '    padding: var(--spacing-md) var(--spacing-lg);\n'
        '    display: flex;\n'
        '    align-items: center;\n'
        '    justify-content: space-between;\n'
        '}\n'
        '\n'
        '.logo {\n'
        '    color: #ffffff;\n'
        '    font-size: 1.75rem;\n'
        '    margin: 0;\n'
        '    letter-spacing: -0.02em;\n'
        '}',
        filename='styles/main.css',
        styles=styles
    ))
    s.append(h2("The Cascade — What It Actually Means", styles))
    s.append(p(
        "The 'C' in CSS stands for Cascading. This word describes the algorithm the browser uses "
        "to decide which CSS rule wins when multiple rules target the same element. Understanding "
        "the cascade saves you hours of debugging mystery style conflicts.",
        styles
    ))
    s.append(p(
        "The cascade considers rules in this order of priority (highest wins):",
        styles
    ))
    s.append(bullet("<b>Origin and importance:</b> User agent styles (browser defaults) < Author styles (your CSS) < User styles < !important rules", styles))
    s.append(bullet("<b>Specificity:</b> How specific is the selector? (covered in section 3.3)", styles))
    s.append(bullet("<b>Order of appearance:</b> When specificity is equal, the last rule written wins", styles))
    s.append(analogy_box(
        "The cascade is like a military chain of command. The General's orders (your !important "
        "rules) override everyone. Below that, a Colonel (ID selectors) outranks a Captain (class "
        "selectors), who outranks a Private (element selectors). When two officers of equal rank "
        "give conflicting orders, the one who spoke last prevails. The cascade gives every CSS "
        "rule a rank — and when two rules conflict, the higher-ranked rule wins.",
        styles
    ))
    s.append(code_block(
        '/* How the browser reads CSS — cascade example */\n'
        '\n'
        '/* Rule 1 — element selector (low specificity) */\n'
        'h1 {\n'
        '    color: black;       /* specificity: 0,0,0,1 */\n'
        '}\n'
        '\n'
        '/* Rule 2 — class selector (medium specificity) */\n'
        '.page-title {\n'
        '    color: navy;        /* specificity: 0,0,1,0 — this WINS over Rule 1 */\n'
        '}\n'
        '\n'
        '/* Rule 3 — ID selector (high specificity) */\n'
        '#main-heading {\n'
        '    color: crimson;     /* specificity: 0,1,0,0 — this WINS over Rules 1 and 2 */\n'
        '}\n'
        '\n'
        '/* If all three rules target the same element:\n'
        '   <h1 class="page-title" id="main-heading">Hello</h1>\n'
        '   ...the text will be crimson, because ID wins. */\n'
        '\n'
        '/* The browser applies ALL matching rules, then resolves conflicts */\n'
        'h1 {\n'
        '    font-size: 2rem;   /* No conflict — this STILL applies */\n'
        '    color: black;       /* OVERRIDDEN by .page-title and #main-heading */\n'
        '}',
        filename='cascade-example.css',
        styles=styles
    ))
    s.append(h2("How the Browser Reads CSS", styles))
    s.append(p(
        "When your browser loads a page, it performs a precise sequence of operations to turn "
        "your HTML and CSS into the pixels you see on screen. This process is called the "
        "<b>rendering pipeline</b>. Knowing this pipeline is essential for writing performant CSS.",
        styles
    ))
    s.append(bullet("<b>1. Parse HTML:</b> The browser reads your HTML and builds the DOM (Document Object Model) — a tree of every element", styles))
    s.append(bullet("<b>2. Parse CSS:</b> The browser reads all stylesheets (linked, internal, and inline) and builds the CSSOM (CSS Object Model)", styles))
    s.append(bullet("<b>3. Build the Render Tree:</b> The browser combines DOM + CSSOM, attaching computed styles to each visible node", styles))
    s.append(bullet("<b>4. Layout:</b> The browser calculates the exact size and position of every element on the page (this is expensive)", styles))
    s.append(bullet("<b>5. Paint:</b> The browser fills in pixels — colors, text, images, borders, shadows", styles))
    s.append(bullet("<b>6. Composite:</b> The browser assembles layers and sends the final image to your GPU for display", styles))
    s.append(principal_box(
        "CSS that triggers Layout (step 4) is the most expensive — changing width, height, "
        "margin, padding, or font-size forces the browser to recalculate positions for potentially "
        "every element on the page. CSS that only triggers Paint (step 5) is cheaper — changing "
        "background-color or border-color. CSS that only triggers Composite (step 6) is cheapest "
        "— changing transform or opacity, which run on the GPU and never touch the CPU layout "
        "engine. This is why professional animations only animate transform and opacity.",
        styles
    ))
    return s


# ============================================================================
# SECTION 3.2 — Selectors — Targeting Elements
# ============================================================================

def section_3_2(styles):
    s = []
    s.append(h1("3.2 Selectors — Targeting Elements", styles))
    s.append(p(
        "A CSS selector is the part of a CSS rule that identifies which HTML elements the rule "
        "applies to. Selectors are the most powerful tool in your CSS toolkit. Mastering them "
        "means you can style any element in any situation without touching your HTML.",
        styles
    ))
    s.append(analogy_box(
        "Selectors are like giving instructions to a painter before they start work on your "
        "house. You can say 'paint every door blue' (element selector). Or 'paint only the "
        "front door blue' (ID selector). Or 'paint all the bedroom doors blue' (class selector). "
        "Or 'paint only doors that are inside bedrooms' (descendant combinator). The more "
        "specific your instruction, the more targeted the result.",
        styles
    ))
    s.append(h2("Basic Selectors", styles))
    s.append(h3("Element Selector", styles))
    s.append(p(
        "Targets all instances of an HTML element type. The broadest selector — use it for "
        "setting base defaults:",
        styles
    ))
    s.append(code_block(
        '/* Targets every <p> element on the page */\n'
        'p {\n'
        '    font-size: 1rem;\n'
        '    line-height: 1.7;\n'
        '    color: #333333;\n'
        '    margin-bottom: 1em;\n'
        '}\n'
        '\n'
        '/* Targets every <button> element */\n'
        'button {\n'
        '    cursor: pointer;\n'
        '    font-family: inherit;\n'
        '    border: none;\n'
        '    border-radius: 4px;\n'
        '    padding: 0.5rem 1.25rem;\n'
        '}\n'
        '\n'
        '/* Targets every <a> element */\n'
        'a {\n'
        '    color: #0066cc;\n'
        '    text-decoration: underline;\n'
        '}',
        filename='element-selectors.css',
        styles=styles
    ))
    s.append(h3("Class Selector", styles))
    s.append(p(
        "Targets elements that have a specific class attribute. This is the workhorse of CSS — "
        "most of your styling should use classes. A class is reusable across multiple elements "
        "and multiple element types. Prefix the class name with a dot (.):",
        styles
    ))
    s.append(code_block(
        '/* HTML */\n'
        '<div class="stock-card">AAPL</div>\n'
        '<article class="stock-card featured">TSLA</article>\n'
        '<section class="stock-card">NVDA</section>\n'
        '\n'
        '/* CSS — targets all three */\n'
        '.stock-card {\n'
        '    background: #ffffff;\n'
        '    border-radius: 8px;\n'
        '    padding: 1.5rem;\n'
        '    box-shadow: 0 2px 8px rgba(0,0,0,0.1);\n'
        '    margin-bottom: 1rem;\n'
        '}\n'
        '\n'
        '/* Targets only elements with BOTH classes */\n'
        '.stock-card.featured {\n'
        '    border: 2px solid #e94560;\n'
        '    box-shadow: 0 4px 16px rgba(233,69,96,0.2);\n'
        '}\n'
        '\n'
        '/* Class used for state */\n'
        '.price-up   { color: #22c55e; }\n'
        '.price-down { color: #ef4444; }\n'
        '.price-flat { color: #94a3b8; }',
        filename='class-selectors.css',
        styles=styles
    ))
    s.append(h3("ID Selector", styles))
    s.append(p(
        "Targets the single element with a specific id attribute. IDs must be unique on the page — "
        "you can only use each ID once. Prefix with a hash (#). IDs have very high specificity, "
        "which makes them hard to override. In modern CSS, prefer classes:",
        styles
    ))
    s.append(code_block(
        '/* HTML */\n'
        '<header id="site-header">...</header>\n'
        '<main id="dashboard">...</main>\n'
        '\n'
        '/* CSS */\n'
        '#site-header {\n'
        '    position: fixed;\n'
        '    top: 0;\n'
        '    left: 0;\n'
        '    right: 0;\n'
        '    z-index: 1000;\n'
        '    background: #1a1a2e;\n'
        '    height: 60px;\n'
        '}\n'
        '\n'
        '#dashboard {\n'
        '    margin-top: 60px;  /* offset for fixed header */\n'
        '    padding: 2rem;\n'
        '}',
        filename='id-selectors.css',
        styles=styles
    ))
    s.append(h2("Combinators", styles))
    s.append(p(
        "Combinators express a relationship between two selectors. They let you target elements "
        "based on where they appear in the document tree.",
        styles
    ))
    s.append(h3("Descendant Combinator (space)", styles))
    s.append(code_block(
        '/* Targets any <a> that is a descendant of .main-nav */\n'
        '/* (could be a direct child, grandchild, great-grandchild, etc.) */\n'
        '.main-nav a {\n'
        '    color: white;\n'
        '    text-decoration: none;\n'
        '    padding: 0.5rem 1rem;\n'
        '    display: block;\n'
        '}\n'
        '\n'
        '/* Targets any <span> inside a .stock-card */\n'
        '.stock-card span {\n'
        '    font-size: 0.875rem;\n'
        '    color: #888;\n'
        '}',
        filename='descendant-combinator.css',
        styles=styles
    ))
    s.append(h3("Child Combinator (>)", styles))
    s.append(code_block(
        '/* Targets <li> elements that are DIRECT children of .nav-list */\n'
        '/* Does NOT target nested <li> inside <li> */\n'
        '.nav-list > li {\n'
        '    display: inline-block;\n'
        '    margin-right: 1rem;\n'
        '}\n'
        '\n'
        '/* Only direct <p> children of .card get this style */\n'
        '.card > p {\n'
        '    font-size: 1.1rem;\n'
        '    font-weight: 600;\n'
        '}',
        filename='child-combinator.css',
        styles=styles
    ))
    s.append(h3("Adjacent Sibling Combinator (+)", styles))
    s.append(code_block(
        '/* Targets a <p> that immediately follows an <h2> */\n'
        'h2 + p {\n'
        '    font-size: 1.125rem;\n'
        '    color: #555;\n'
        '    margin-top: 0;\n'
        '}\n'
        '\n'
        '/* Targets a label that immediately follows a checkbox */\n'
        'input[type="checkbox"] + label {\n'
        '    cursor: pointer;\n'
        '    padding-left: 0.5rem;\n'
        '    user-select: none;\n'
        '}',
        filename='adjacent-sibling.css',
        styles=styles
    ))
    s.append(h3("General Sibling Combinator (~)", styles))
    s.append(code_block(
        '/* Targets ALL <p> elements that are siblings of an <h2> */\n'
        '/* (not just the immediately adjacent one) */\n'
        'h2 ~ p {\n'
        '    margin-left: 1rem;\n'
        '}\n'
        '\n'
        '/* Classic CSS-only accordion trick */\n'
        'input[type="checkbox"]:checked ~ .accordion-content {\n'
        '    display: block;\n'
        '    max-height: 500px;\n'
        '    overflow: hidden;\n'
        '}',
        filename='general-sibling.css',
        styles=styles
    ))
    s.append(h2("Pseudo-Classes", styles))
    s.append(p(
        "Pseudo-classes target elements in a specific state or position. They are written with "
        "a single colon (:) after the selector.",
        styles
    ))
    s.append(code_block(
        '/* ----------------------------------------\n'
        '   User interaction states\n'
        '   ---------------------------------------- */\n'
        '\n'
        '/* When the user hovers over the element */\n'
        '.btn:hover {\n'
        '    background-color: #c73854;\n'
        '    transform: translateY(-1px);\n'
        '    box-shadow: 0 4px 12px rgba(233, 69, 96, 0.4);\n'
        '}\n'
        '\n'
        '/* When an input or button has keyboard focus */\n'
        'input:focus, button:focus {\n'
        '    outline: 2px solid #e94560;\n'
        '    outline-offset: 2px;\n'
        '}\n'
        '\n'
        '/* When any descendant has focus (great for form groups) */\n'
        '.form-group:focus-within {\n'
        '    background-color: #f0f7ff;\n'
        '    border-color: #0066cc;\n'
        '}\n'
        '\n'
        '/* ----------------------------------------\n'
        '   Structural pseudo-classes\n'
        '   ---------------------------------------- */\n'
        '\n'
        '/* First child of its parent */\n'
        'li:first-child {\n'
        '    border-top: none;\n'
        '}\n'
        '\n'
        '/* Last child of its parent */\n'
        'li:last-child {\n'
        '    border-bottom: none;\n'
        '}\n'
        '\n'
        '/* Every 2nd child (even rows) */\n'
        'tr:nth-child(even) {\n'
        '    background-color: #f8f8f8;\n'
        '}\n'
        '\n'
        '/* Every 3rd item, starting from the 1st */\n'
        '.grid-item:nth-child(3n+1) {\n'
        '    clear: left;\n'
        '}\n'
        '\n'
        '/* First <p> regardless of sibling types */\n'
        'p:first-of-type {\n'
        '    font-size: 1.125rem;\n'
        '    font-weight: 500;\n'
        '}\n'
        '\n'
        '/* ----------------------------------------\n'
        '   Logical pseudo-classes (CSS Selectors Level 4)\n'
        '   ---------------------------------------- */\n'
        '\n'
        '/* Negation — all buttons that are NOT .primary */\n'
        'button:not(.primary) {\n'
        '    background: transparent;\n'
        '    border: 1px solid currentColor;\n'
        '}\n'
        '\n'
        '/* :is() — matches any selector in the list (less repetition) */\n'
        ':is(h1, h2, h3, h4) {\n'
        '    font-family: "Inter", system-ui, sans-serif;\n'
        '    font-weight: 700;\n'
        '    line-height: 1.2;\n'
        '}\n'
        '\n'
        '/* :where() — like :is() but contributes zero specificity */\n'
        ':where(article, section, aside) p {\n'
        '    line-height: 1.7;\n'
        '}',
        filename='pseudo-classes.css',
        styles=styles
    ))
    s.append(h2("Pseudo-Elements", styles))
    s.append(p(
        "Pseudo-elements style a specific part of an element, or insert generated content. "
        "They use double colons (::) in modern CSS, though browsers also accept a single colon "
        "for historical pseudo-elements like :before.",
        styles
    ))
    s.append(code_block(
        '/* Insert content BEFORE an element — no HTML needed */\n'
        '.required-label::before {\n'
        '    content: "* ";\n'
        '    color: #ef4444;\n'
        '    font-weight: bold;\n'
        '}\n'
        '\n'
        '/* Insert a decorative quote mark AFTER a blockquote */\n'
        'blockquote::after {\n'
        '    content: "\u201d";\n'
        '    font-size: 4rem;\n'
        '    color: #ddd;\n'
        '    position: absolute;\n'
        '    bottom: -1rem;\n'
        '    right: 1rem;\n'
        '}\n'
        '\n'
        '/* Style only the first line of a paragraph */\n'
        '.article-intro::first-line {\n'
        '    font-variant: small-caps;\n'
        '    letter-spacing: 0.08em;\n'
        '}\n'
        '\n'
        '/* Style the first letter (drop cap) */\n'
        '.article-body > p:first-child::first-letter {\n'
        '    font-size: 3.5em;\n'
        '    font-weight: 900;\n'
        '    float: left;\n'
        '    line-height: 0.8;\n'
        '    margin-right: 0.1em;\n'
        '    color: #e94560;\n'
        '}\n'
        '\n'
        '/* Style the placeholder text of an input */\n'
        'input::placeholder {\n'
        '    color: #aaaaaa;\n'
        '    font-style: italic;\n'
        '}\n'
        '\n'
        '/* Style text the user has selected */\n'
        '::selection {\n'
        '    background-color: #e94560;\n'
        '    color: white;\n'
        '}',
        filename='pseudo-elements.css',
        styles=styles
    ))
    s.append(h2("Attribute Selectors", styles))
    s.append(p(
        "Attribute selectors target elements based on the presence or value of their HTML "
        "attributes. They are written in square brackets and are far more powerful than most "
        "developers realize:",
        styles
    ))
    s.append(code_block(
        '/* [attr] — has the attribute, any value */\n'
        'a[target] {\n'
        '    /* Any link with a target attribute */\n'
        '    padding-right: 1.2em;\n'
        '}\n'
        '\n'
        '/* [attr=val] — exact value match */\n'
        'input[type="email"] {\n'
        '    background-image: url(icons/email.svg);\n'
        '    background-repeat: no-repeat;\n'
        '    background-position: right 0.75rem center;\n'
        '    padding-right: 2.5rem;\n'
        '}\n'
        '\n'
        'input[type="checkbox"] {\n'
        '    width: 1.25rem;\n'
        '    height: 1.25rem;\n'
        '    accent-color: #e94560;\n'
        '}\n'
        '\n'
        '/* [attr^=val] — starts with val */\n'
        'a[href^="https"] {\n'
        '    /* All secure links */\n'
        '    color: #22c55e;\n'
        '}\n'
        '\n'
        'a[href^="mailto"] {\n'
        '    /* All email links */\n'
        '    text-decoration: underline dotted;\n'
        '}\n'
        '\n'
        '/* [attr$=val] — ends with val */\n'
        'a[href$=".pdf"] {\n'
        '    /* PDF download links */\n'
        '    padding-right: 1.5em;\n'
        '    background: url(icons/pdf.svg) no-repeat right center;\n'
        '}\n'
        '\n'
        '/* [attr*=val] — contains val anywhere */\n'
        '[class*="icon-"] {\n'
        '    /* Any element whose class contains "icon-" */\n'
        '    display: inline-block;\n'
        '    width: 1em;\n'
        '    height: 1em;\n'
        '    vertical-align: middle;\n'
        '}\n'
        '\n'
        '/* Practical: style disabled form elements */\n'
        'button[disabled],\n'
        'input[disabled] {\n'
        '    opacity: 0.5;\n'
        '    cursor: not-allowed;\n'
        '    pointer-events: none;\n'
        '}',
        filename='attribute-selectors.css',
        styles=styles
    ))
    return s


# ============================================================================
# SECTION 3.3 — Specificity and the Cascade — The Pecking Order
# ============================================================================

def section_3_3(styles):
    s = []
    s.append(h1("3.3 Specificity and the Cascade — The Pecking Order", styles))
    s.append(p(
        "Specificity is the algorithm browsers use to decide which CSS rule takes effect when "
        "multiple rules could apply to the same element. Every selector has a specificity score, "
        "represented as a four-part value: (inline, IDs, classes/attributes/pseudo-classes, "
        "elements/pseudo-elements). The rule with the highest score wins.",
        styles
    ))
    s.append(analogy_box(
        "Specificity is like a scoring system used by a panel of judges at a competition. "
        "Four judges each hold up a score card: the Inline Style judge, the ID judge, the "
        "Class judge, and the Element judge. Their scores are compared from left to right — "
        "just like comparing 1,0,0,0 vs 0,99,0,0. Even a single point from the Inline judge "
        "beats any number of points from the ID judge. The judges never carry over: 0,1,0,0 "
        "always beats 0,0,999,0.",
        styles
    ))
    s.append(h2("The Specificity Calculation System", styles))
    s.append(p(
        "Each component adds to a different column. The columns are never added together — "
        "they are compared independently from left to right:",
        styles
    ))
    s.append(bullet("<b>Column A (inline styles):</b> 1,0,0,0 — style attribute directly on the element", styles))
    s.append(bullet("<b>Column B (ID selectors):</b> 0,1,0,0 per #id", styles))
    s.append(bullet("<b>Column C (class/attribute/pseudo-class):</b> 0,0,1,0 per .class, [attr], :hover, :nth-child(), etc.", styles))
    s.append(bullet("<b>Column D (element/pseudo-element):</b> 0,0,0,1 per tag, ::before, ::after, etc.", styles))
    s.append(bullet("<b>The universal selector (*) and combinators (+, >, ~, space):</b> 0,0,0,0 — no specificity contribution", styles))
    s.append(code_block(
        '/* Specificity calculation examples */\n'
        '\n'
        '/* Selector                               | A  B  C  D */\n'
        '/* -----------------------------------------|------------ */\n'
        '/* p                                      | 0, 0, 0, 1 */\n'
        '/* .card                                  | 0, 0, 1, 0 */\n'
        '/* #header                                | 0, 1, 0, 0 */\n'
        '/* style=""                               | 1, 0, 0, 0 */\n'
        '/* p.intro                                | 0, 0, 1, 1 */\n'
        '/* .card .title                           | 0, 0, 2, 0 */\n'
        '/* .nav li:first-child                    | 0, 0, 1, 2 */\n'
        '/* #header .nav a:hover                   | 0, 1, 2, 1 */\n'
        '/* .card .body p:first-child::first-line  | 0, 0, 2, 3 */\n'
        '\n'
        '/* Practical example — which rule wins? */\n'
        '\n'
        'h1 {\n'
        '    color: black;       /* 0,0,0,1 — LOSES */\n'
        '}\n'
        '\n'
        'header h1 {\n'
        '    color: navy;        /* 0,0,0,2 — beats above */\n'
        '}\n'
        '\n'
        '.site-header h1 {\n'
        '    color: darkblue;    /* 0,0,1,1 — beats above */\n'
        '}\n'
        '\n'
        '#main-header .site-header h1 {\n'
        '    color: royalblue;   /* 0,1,1,1 — beats above */\n'
        '}\n'
        '\n'
        '/* This h1 will be royalblue if it matches the last rule */\n'
        '/* <div id="main-header"><header class="site-header"><h1>Title</h1> */\n'
        '\n'
        '/* ----------------------------------------\n'
        '   :is(), :where(), and :not() specificity\n'
        '   ---------------------------------------- */\n'
        '\n'
        '/* :is() takes the specificity of its MOST specific argument */\n'
        ':is(#header, .card, p) {  /* specificity: 0,1,0,0 — the #header wins */\n'
        '    color: red;\n'
        '}\n'
        '\n'
        '/* :where() contributes ZERO specificity — great for base styles */\n'
        ':where(#header, .card, p) {  /* specificity: 0,0,0,0 */\n'
        '    color: red;\n'
        '}\n'
        '\n'
        '/* :not() takes the specificity of its argument */\n'
        'button:not(.primary) {  /* specificity: 0,0,1,1 */\n'
        '    background: transparent;\n'
        '}',
        filename='specificity-examples.css',
        styles=styles
    ))
    s.append(h2("Why !important Is a Code Smell", styles))
    s.append(p(
        "The !important declaration overrides all normal cascade rules and makes a rule win "
        "regardless of specificity. It sounds like a solution but it creates a vicious cycle: "
        "you use !important to override something, then someone else needs to override your "
        "!important so they add another !important, and soon your stylesheet is a battlefield "
        "of !important declarations that no one can reason about.",
        styles
    ))
    s.append(code_block(
        '/* The !important arms race — DON\'T do this */\n'
        '.button {\n'
        '    color: white !important;      /* round 1 */\n'
        '}\n'
        '\n'
        '#sidebar .button {\n'
        '    color: black !important;      /* round 2 — trying to override round 1 */\n'
        '}\n'
        '\n'
        '/* Now you\'re stuck. Adding more !important doesn\'t help because\n'
        '   when two rules both have !important, specificity decides again. */\n'
        '\n'
        '/* The CORRECT fix — restructure your selectors */\n'
        '.button { color: white; }\n'
        '.sidebar .button { color: black; }  /* higher specificity, no !important */\n'
        '\n'
        '/* Legitimate uses of !important: */\n'
        '/* 1. Utility classes that must always win (e.g., .hidden { display: none !important; }) */\n'
        '/* 2. Overriding third-party library styles you cannot edit */\n'
        '/* 3. User accessibility stylesheets */\n'
        '\n'
        '/* The .hidden example IS legitimate */\n'
        '.hidden {\n'
        '    display: none !important;  /* Nothing should override this utility */\n'
        '}',
        filename='important-smell.css',
        styles=styles
    ))
    s.append(mistake_box(
        "The most common specificity mistake: using IDs for styling. When you use #myId to "
        "style something, you make every future override require either another ID or !important. "
        "Use IDs only for JavaScript hooks (getElementById) and HTML anchor targets. Style "
        "everything with classes. This keeps specificity flat and your CSS maintainable.",
        styles
    ))
    s.append(h2("Inheritance", styles))
    s.append(p(
        "Some CSS properties automatically pass their value down from a parent element to its "
        "children. This is called <b>inheritance</b> and is an intentional CSS feature, not a bug. "
        "Understanding which properties inherit saves you from writing repetitive rules.",
        styles
    ))
    s.append(h3("Properties That Inherit (Typography properties mostly)", styles))
    s.append(code_block(
        '/* If you set these on body, all descendants inherit them */\n'
        'body {\n'
        '    font-family: system-ui, sans-serif;  /* inherited */\n'
        '    font-size: 16px;                     /* inherited */\n'
        '    color: #333333;                      /* inherited */\n'
        '    line-height: 1.6;                    /* inherited */\n'
        '    letter-spacing: 0;                   /* inherited */\n'
        '    word-spacing: 0;                     /* inherited */\n'
        '    text-align: left;                    /* inherited */\n'
        '    visibility: visible;                 /* inherited */\n'
        '    cursor: default;                     /* inherited */\n'
        '    list-style: disc;                    /* inherited */\n'
        '}\n'
        '\n'
        '/* You do NOT need to set font-family on every element —\n'
        '   it trickles down from body automatically */\n'
        '\n'
        '/* Properties that DO NOT inherit */\n'
        '/* width, height, margin, padding, border,\n'
        '   background, display, position, float,\n'
        '   box-shadow, transform, animation, overflow */\n'
        '\n'
        '/* Force inheritance with the "inherit" keyword */\n'
        '.special-input {\n'
        '    font-family: inherit;  /* explicitly inherit from parent */\n'
        '    font-size: inherit;\n'
        '    color: inherit;\n'
        '}\n'
        '\n'
        '/* Reset to browser default */\n'
        '.no-inherit {\n'
        '    color: initial;         /* resets to black (initial value) */\n'
        '}\n'
        '\n'
        '/* Use parent\'s value OR initial if not set */\n'
        '.smart-reset {\n'
        '    all: unset;             /* nuclear option — removes all styles */\n'
        '    display: block;         /* then add back what you need */\n'
        '}',
        filename='inheritance.css',
        styles=styles
    ))
    s.append(h2("Common Specificity Battles and How to Resolve Them", styles))
    s.append(code_block(
        '/* Problem: A third-party library adds high-specificity rules */\n'
        '/* Library CSS (you cannot edit this) */\n'
        '#widget-container .widget-button {\n'
        '    background: blue;   /* 0,1,1,0 */\n'
        '}\n'
        '\n'
        '/* Your CSS — you need it to be red */\n'
        '.widget-button {\n'
        '    background: red;    /* 0,0,1,0 — LOSES */\n'
        '}\n'
        '\n'
        '/* Solution 1: Match specificity */\n'
        '#widget-container .widget-button {\n'
        '    background: red;    /* 0,1,1,0 — WINS (last one wins on tie) */\n'
        '}\n'
        '\n'
        '/* Solution 2: Use :is() for a specificity boost */\n'
        ':is(#widget-container) .widget-button {\n'
        '    background: red;    /* 0,1,1,0 — matches */\n'
        '}\n'
        '\n'
        '/* Solution 3: CSS layers (see section 3.12) */\n'
        '@layer overrides {\n'
        '    .widget-button { background: red; }  /* layers override by order */\n'
        '}\n'
        '\n'
        '/* ----------------------------------------\n'
        '   Problem: Styles not applying as expected\n'
        '   ---------------------------------------- */\n'
        '\n'
        '/* Debugging technique: use browser DevTools */\n'
        '/* In DevTools, struck-through rules lost the cascade */\n'
        '/* Check the "Computed" tab to see the winning value */\n'
        '\n'
        '/* Prevention: Keep specificity flat */\n'
        '/* AVOID deeply nested selectors like: */\n'
        '.header .nav .nav-list .nav-item .nav-link:hover span {\n'
        '    color: white;  /* 0,0,4,3 — very hard to override */\n'
        '}\n'
        '\n'
        '/* PREFER single-class selectors: */\n'
        '.nav-link:hover {\n'
        '    color: white;  /* 0,0,1,0 — easy to override */\n'
        '}',
        filename='specificity-battles.css',
        styles=styles
    ))
    s.append(principal_box(
        "At scale, specificity debt is a silent codebase killer. Every time a developer adds "
        "a more-specific selector to override something, the baseline specificity creeps up. "
        "After a year of ten developers doing this, you end up with selectors three levels deep "
        "and !important scattered throughout. The solution is architectural: adopt a methodology "
        "like BEM (see section 3.13) that keeps every selector at exactly one class (specificity "
        "0,0,1,0). Flat specificity means anyone can override anything with a single class.",
        styles
    ))
    return s


# ============================================================================
# SECTION 3.4 — The Box Model — Every Element is a Box
# ============================================================================

def section_3_4(styles):
    s = []
    s.append(h1("3.4 The Box Model — Every Element is a Box", styles))
    s.append(p(
        "Every single HTML element — every heading, paragraph, div, button, image, and span — "
        "is rendered as a rectangular box. Understanding the box model is the difference between "
        "a developer who fights CSS and one who wields it with precision. The box model defines "
        "four areas around every element's content.",
        styles
    ))
    s.append(analogy_box(
        "Every HTML element is like a framed picture hanging on a wall. The picture itself is "
        "the content. The white matting inside the frame is the padding. The physical frame is "
        "the border. And the gap between this frame and the next frame on the wall is the margin. "
        "When you measure the total space the framed picture takes up on the wall, you measure "
        "from the outer edge of the gap — that is the margin box.",
        styles
    ))
    s.append(h2("The Four Areas of the Box Model", styles))
    s.append(code_block(
        '/* Visualizing the box model */\n'
        '.stock-card {\n'
        '    /* CONTENT: the actual text/children inside */\n'
        '    width: 300px;\n'
        '    height: auto;              /* or a specific height */\n'
        '\n'
        '    /* PADDING: space between content and border (inside the box) */\n'
        '    padding-top:    1.5rem;    /* 24px */\n'
        '    padding-right:  1.5rem;\n'
        '    padding-bottom: 1.5rem;\n'
        '    padding-left:   1.5rem;\n'
        '    /* shorthand: padding: 1.5rem;                  (all sides) */\n'
        '    /* shorthand: padding: 1rem 1.5rem;             (top+bottom, left+right) */\n'
        '    /* shorthand: padding: 1rem 1.5rem 1.25rem;     (top, left+right, bottom) */\n'
        '    /* shorthand: padding: 1rem 1.5rem 1.25rem 1rem;(top, right, bottom, left) */\n'
        '\n'
        '    /* BORDER: the visible line around the padding */\n'
        '    border-width: 1px;\n'
        '    border-style: solid;       /* solid, dashed, dotted, double, none */\n'
        '    border-color: #e2e8f0;\n'
        '    /* shorthand: border: 1px solid #e2e8f0; */\n'
        '\n'
        '    border-radius: 8px;        /* rounded corners */\n'
        '    /* individual corners: border-top-left-radius: 8px; etc. */\n'
        '\n'
        '    /* MARGIN: space outside the border (between elements) */\n'
        '    margin-bottom: 1rem;\n'
        '    /* Use auto for centering: */\n'
        '    /* margin: 0 auto;  -- centers block element horizontally */\n'
        '\n'
        '    background-color: #ffffff;\n'
        '    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);\n'
        '}',
        filename='box-model.css',
        styles=styles
    ))
    s.append(h2("box-sizing: border-box — The Rule You Always Set First", styles))
    s.append(p(
        "By default, the browser uses <b>content-box</b> sizing, which means that width and "
        "height only measure the content area. If you set width: 300px and padding: 20px, "
        "the total element width becomes 340px (300 + 20 + 20). This is the source of "
        "innumerable layout bugs for beginners. The fix is to use <b>border-box</b> sizing, "
        "where width includes the padding and border. Set this globally at the top of every "
        "stylesheet — without exception:",
        styles
    ))
    s.append(code_block(
        '/* The universal box-sizing reset — put this at the top of every stylesheet */\n'
        '*, *::before, *::after {\n'
        '    box-sizing: border-box;\n'
        '}\n'
        '\n'
        '/* NOW: */\n'
        '.box {\n'
        '    width: 300px;\n'
        '    padding: 20px;\n'
        '    border: 2px solid black;\n'
        '    /* Total width = exactly 300px */\n'
        '    /* Content width = 300 - 40 (padding) - 4 (border) = 256px */\n'
        '}\n'
        '\n'
        '/* WITHOUT border-box (old behavior content-box): */\n'
        '/* width: 300px + padding: 40px + border: 4px = 344px total -- SURPRISE! */\n'
        '\n'
        '/* Practical example: two columns at 50% each */\n'
        '.column {\n'
        '    width: 50%;\n'
        '    padding: 1rem;         /* With border-box, still exactly 50% wide */\n'
        '    float: left;           /* Without border-box: 50% + 2rem > 100% — breaks! */\n'
        '}',
        filename='box-sizing.css',
        styles=styles
    ))
    s.append(mistake_box(
        "Never use box-sizing: content-box in modern CSS. The only reason it exists as the "
        "default is historical — it was the original CSS specification. Every professional "
        "CSS project starts with *, *::before, *::after { box-sizing: border-box; }. "
        "If you inherit a codebase without this rule, adding it can shift layouts, so add "
        "it carefully and test thoroughly.",
        styles
    ))
    s.append(h2("Collapsing Margins", styles))
    s.append(p(
        "One of CSS's most surprising behaviors: vertical margins between adjacent block elements "
        "collapse into one. When two vertical margins touch, the browser uses the larger of the "
        "two — they do not add together. Horizontal margins never collapse.",
        styles
    ))
    s.append(code_block(
        '/* Margin collapse example */\n'
        'h2 {\n'
        '    margin-bottom: 1.5rem;   /* 24px */\n'
        '}\n'
        '\n'
        'p {\n'
        '    margin-top: 1rem;        /* 16px */\n'
        '}\n'
        '\n'
        '/* The gap between an h2 and the following p is:\n'
        '   NOT 24px + 16px = 40px\n'
        '   BUT max(24px, 16px) = 24px  <-- COLLAPSED */\n'
        '\n'
        '/* Margin collapse also happens parent-to-child */\n'
        '.card {\n'
        '    margin-top: 2rem;   /* 32px */\n'
        '    /* No border, no padding, no BFC trigger... */\n'
        '}\n'
        '\n'
        '.card h2 {\n'
        '    margin-top: 1rem;   /* 16px */\n'
        '    /* This margin "escapes" the .card and collapses with .card\'s margin */\n'
        '    /* Total gap above .card: max(32, 16) = 32px */\n'
        '}\n'
        '\n'
        '/* HOW TO PREVENT margin collapse */\n'
        '\n'
        '/* Option 1: Add padding to the parent */\n'
        '.card { padding-top: 1px; }  /* even 1px of padding stops the escape */\n'
        '\n'
        '/* Option 2: Add a border to the parent */\n'
        '.card { border-top: 1px solid transparent; }\n'
        '\n'
        '/* Option 3: Create a BFC (Block Formatting Context) */\n'
        '.card { overflow: hidden; }   /* or display: flow-root */\n'
        '.card { display: flow-root; } /* the modern, explicit way */\n'
        '\n'
        '/* Option 4: Use flexbox or grid (these never collapse margins) */\n'
        '.card { display: flex; flex-direction: column; gap: 1rem; }',
        filename='margin-collapse.css',
        styles=styles
    ))
    s.append(h2("Complete Box Model Visual Example", styles))
    s.append(code_block(
        '/* Complete styled component demonstrating every box model property */\n'
        '/* styles/stock-card.css */\n'
        '\n'
        '*, *::before, *::after { box-sizing: border-box; }\n'
        '\n'
        '.card-grid {\n'
        '    display: grid;\n'
        '    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));\n'
        '    gap: 1.5rem;\n'
        '    padding: 2rem;\n'
        '}\n'
        '\n'
        '.stock-card {\n'
        '    /* Content */\n'
        '    width: 100%;                     /* fills grid column */\n'
        '    min-height: 140px;\n'
        '\n'
        '    /* Padding — interior breathing room */\n'
        '    padding: 1.5rem;\n'
        '\n'
        '    /* Border */\n'
        '    border: 1px solid #e2e8f0;\n'
        '    border-radius: 12px;\n'
        '    border-top: 4px solid var(--accent-color, #e94560);\n'
        '\n'
        '    /* Margin — space between cards (handled by grid gap above) */\n'
        '    /* margin: 0; -- not needed, grid gap handles it */\n'
        '\n'
        '    /* Visual */\n'
        '    background-color: #ffffff;\n'
        '    box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 4px 12px rgba(0,0,0,0.05);\n'
        '}\n'
        '\n'
        '.stock-card__ticker {\n'
        '    font-size: 0.75rem;\n'
        '    font-weight: 700;\n'
        '    letter-spacing: 0.08em;\n'
        '    text-transform: uppercase;\n'
        '    color: #888;\n'
        '    margin-bottom: 0.25rem;\n'
        '    padding: 0;          /* no extra padding needed */\n'
        '}\n'
        '\n'
        '.stock-card__price {\n'
        '    font-size: 1.75rem;\n'
        '    font-weight: 700;\n'
        '    color: #1a1a2e;\n'
        '    margin: 0 0 0.5rem;\n'
        '    padding: 0;\n'
        '    /* line-height controls vertical space within text */\n'
        '    line-height: 1.2;\n'
        '}\n'
        '\n'
        '.stock-card__change {\n'
        '    display: inline-block;\n'
        '    padding: 0.2rem 0.6rem;      /* tight padding for a badge */\n'
        '    border-radius: 100px;        /* pill shape */\n'
        '    font-size: 0.875rem;\n'
        '    font-weight: 600;\n'
        '    margin: 0;\n'
        '}\n'
        '\n'
        '.stock-card__change--up {\n'
        '    background-color: #dcfce7;\n'
        '    color: #166534;\n'
        '}\n'
        '\n'
        '.stock-card__change--down {\n'
        '    background-color: #fee2e2;\n'
        '    color: #991b1b;\n'
        '}',
        filename='styles/stock-card.css',
        styles=styles
    ))
    return s


# ============================================================================
# SECTION 3.5 — Display and Positioning
# ============================================================================

def section_3_5(styles):
    s = []
    s.append(h1("3.5 Display and Positioning", styles))
    s.append(p(
        "Two of the most fundamental CSS properties are <b>display</b> and <b>position</b>. "
        "Together, they control how elements flow in the document and where they appear on screen. "
        "Misunderstanding these two properties is the source of most layout confusion for "
        "beginning and intermediate CSS developers.",
        styles
    ))
    s.append(h2("The display Property", styles))
    s.append(h3("block", styles))
    s.append(p(
        "Block elements start on a new line and stretch to fill the full width available. "
        "You can set their width and height. Examples: div, p, h1-h6, section, article, ul, li.",
        styles
    ))
    s.append(code_block(
        '.dashboard-section {\n'
        '    display: block;          /* this is the default for div */\n'
        '    width: 100%;             /* stretches to fill parent */\n'
        '    padding: 2rem;\n'
        '    margin-bottom: 2rem;     /* vertical margins work */\n'
        '    background: white;\n'
        '    border-radius: 8px;\n'
        '}',
        filename='display-block.css',
        styles=styles
    ))
    s.append(h3("inline", styles))
    s.append(p(
        "Inline elements flow within text — they do not start on a new line. You cannot set "
        "their width or height. Vertical padding and margin have limited effect. Examples: "
        "span, a, strong, em, code.",
        styles
    ))
    s.append(code_block(
        '.price-badge {\n'
        '    display: inline;         /* default for span */\n'
        '    color: #22c55e;\n'
        '    font-weight: bold;\n'
        '    /* width: 100px;  -- HAS NO EFFECT on inline elements */\n'
        '    /* height: 30px;  -- HAS NO EFFECT on inline elements */\n'
        '}',
        filename='display-inline.css',
        styles=styles
    ))
    s.append(h3("inline-block", styles))
    s.append(p(
        "The best of both worlds: flows inline with text, but you can set width, height, "
        "padding, and margin like a block. Perfect for badges, tags, and button-like spans:",
        styles
    ))
    s.append(code_block(
        '.tag {\n'
        '    display: inline-block;    /* flows in text, but has block properties */\n'
        '    padding: 0.25rem 0.75rem;\n'
        '    background: #e2e8f0;\n'
        '    border-radius: 100px;\n'
        '    font-size: 0.75rem;\n'
        '    font-weight: 600;\n'
        '    width: auto;              /* width WORKS on inline-block */\n'
        '    vertical-align: middle;   /* align with surrounding text */\n'
        '}\n'
        '\n'
        '/* Inline navigation items */\n'
        '.nav-item {\n'
        '    display: inline-block;\n'
        '    margin-right: 0.5rem;\n'
        '}\n'
        '\n'
        '.nav-item a {\n'
        '    display: block;           /* makes the full area clickable */\n'
        '    padding: 0.5rem 1rem;\n'
        '    color: white;\n'
        '    text-decoration: none;\n'
        '}',
        filename='display-inline-block.css',
        styles=styles
    ))
    s.append(h2("The position Property", styles))
    s.append(analogy_box(
        "The five position values describe how an element sits in the room. Static is the "
        "default: the element sits wherever the document flow puts it. Relative is scooting "
        "your chair a few inches — you move, but your original seat is still reserved in the "
        "flow. Absolute is picking up your chair entirely and placing it anywhere in the room "
        "— your original spot closes up. Fixed pins your chair to a specific spot on the wall "
        "that never moves even when the room rearranges. Sticky is a chair that follows you "
        "until it hits a wall, then sticks there.",
        styles
    ))
    s.append(h3("position: static (Default)", styles))
    s.append(code_block(
        '.normal-div {\n'
        '    position: static;    /* DEFAULT — no special positioning */\n'
        '    /* top, right, bottom, left, z-index have NO effect */\n'
        '    /* Element flows normally in the document */\n'
        '}',
        filename='position-static.css',
        styles=styles
    ))
    s.append(h3("position: relative", styles))
    s.append(code_block(
        '.nudged-icon {\n'
        '    position: relative;  /* Move relative to its normal position */\n'
        '    top: -2px;           /* Nudge 2px upward */\n'
        '    left: 4px;           /* Nudge 4px right */\n'
        '    /* IMPORTANT: the original space is PRESERVED in the layout */\n'
        '    /* Neighbors still act as if the element is in its original spot */\n'
        '}\n'
        '\n'
        '/* Most common use: establish a positioning context for absolute children */\n'
        '.stock-card {\n'
        '    position: relative;  /* Now absolute children position within this */\n'
        '    /* This element still flows normally */\n'
        '}',
        filename='position-relative.css',
        styles=styles
    ))
    s.append(h3("position: absolute", styles))
    s.append(code_block(
        '/* Child is placed relative to nearest positioned ancestor */\n'
        '\n'
        '.stock-card {\n'
        '    position: relative;     /* establish positioning context */\n'
        '    padding: 1.5rem;\n'
        '}\n'
        '\n'
        '.stock-card__badge {\n'
        '    position: absolute;     /* removed from normal flow */\n'
        '    top: -8px;              /* 8px above the card\'s top edge */\n'
        '    right: 1rem;            /* 1rem from the card\'s right edge */\n'
        '    /* The card does NOT make space for this — it overlaps */\n'
        '    background: #e94560;\n'
        '    color: white;\n'
        '    font-size: 0.7rem;\n'
        '    font-weight: 700;\n'
        '    padding: 0.2rem 0.5rem;\n'
        '    border-radius: 100px;\n'
        '    text-transform: uppercase;\n'
        '    letter-spacing: 0.06em;\n'
        '}\n'
        '\n'
        '/* Centering absolutely positioned elements */\n'
        '.overlay {\n'
        '    position: absolute;\n'
        '    top: 50%;\n'
        '    left: 50%;\n'
        '    transform: translate(-50%, -50%);  /* shift back by half own size */\n'
        '    /* This perfectly centers the element regardless of its size */\n'
        '}',
        filename='position-absolute.css',
        styles=styles
    ))
    s.append(h3("position: fixed", styles))
    s.append(code_block(
        '/* Fixed to the viewport — does not scroll */\n'
        '.site-header {\n'
        '    position: fixed;\n'
        '    top: 0;\n'
        '    left: 0;\n'
        '    right: 0;              /* or width: 100% */\n'
        '    height: 60px;\n'
        '    z-index: 1000;         /* must be above other content */\n'
        '    background: #1a1a2e;\n'
        '    box-shadow: 0 2px 8px rgba(0,0,0,0.2);\n'
        '}\n'
        '\n'
        '/* Remember to offset body content for fixed header */\n'
        'body {\n'
        '    padding-top: 60px;\n'
        '}\n'
        '\n'
        '/* Modal overlay */\n'
        '.modal-backdrop {\n'
        '    position: fixed;\n'
        '    inset: 0;              /* shorthand for top:0; right:0; bottom:0; left:0 */\n'
        '    background: rgba(0, 0, 0, 0.6);\n'
        '    z-index: 500;\n'
        '    display: flex;\n'
        '    align-items: center;\n'
        '    justify-content: center;\n'
        '}',
        filename='position-fixed.css',
        styles=styles
    ))
    s.append(h3("position: sticky", styles))
    s.append(code_block(
        '/* Behaves like relative until it reaches a threshold,\n'
        '   then sticks like fixed */\n'
        '\n'
        '.table-header {\n'
        '    position: sticky;\n'
        '    top: 0;              /* sticks when it reaches 0px from viewport top */\n'
        '    z-index: 10;\n'
        '    background: white;   /* must have background or content shows through */\n'
        '    border-bottom: 2px solid #e2e8f0;\n'
        '}\n'
        '\n'
        '/* Sticky sidebar in a blog layout */\n'
        '.sidebar {\n'
        '    position: sticky;\n'
        '    top: 80px;           /* 80px gap from viewport top (accounts for header) */\n'
        '    align-self: flex-start;  /* required inside flexbox, or it stretches */\n'
        '    max-height: calc(100vh - 80px);\n'
        '    overflow-y: auto;\n'
        '}',
        filename='position-sticky.css',
        styles=styles
    ))
    s.append(h2("Z-Index and Stacking Contexts", styles))
    s.append(analogy_box(
        "Z-index is like a stack of transparent sheets on an overhead projector. Each sheet "
        "can have a number — higher numbers go on top. But here is the critical part: if you "
        "put a stack of sheets inside a folder, the entire folder acts as one sheet. Elements "
        "inside a stacking context are isolated from z-index comparisons outside it. An element "
        "with z-index: 9999 inside a context with z-index: 1 will NEVER appear above an element "
        "with z-index: 2 outside that context.",
        styles
    ))
    s.append(code_block(
        '/* Z-index fundamentals */\n'
        '\n'
        '/* Z-index only works on positioned elements (not static) */\n'
        '.tooltip {\n'
        '    position: absolute;    /* must be positioned */\n'
        '    z-index: 100;          /* higher = closer to user */\n'
        '}\n'
        '\n'
        '.modal {\n'
        '    position: fixed;\n'
        '    z-index: 500;          /* above tooltip */\n'
        '}\n'
        '\n'
        '.site-header {\n'
        '    position: sticky;\n'
        '    z-index: 200;          /* above tooltip, below modal */\n'
        '}\n'
        '\n'
        '/* Stacking context created by: */\n'
        '/* - position + z-index other than auto */\n'
        '/* - opacity < 1 */\n'
        '/* - transform (any value except none) */\n'
        '/* - filter (any value except none) */\n'
        '/* - will-change */\n'
        '/* - isolation: isolate */\n'
        '\n'
        '.isolated-component {\n'
        '    isolation: isolate;    /* create stacking context without other effects */\n'
        '    /* Now z-index inside here is scoped to this component */\n'
        '}\n'
        '\n'
        '/* TradeBoard z-index scale */\n'
        ':root {\n'
        '    --z-dropdown:    10;\n'
        '    --z-sticky:      20;\n'
        '    --z-fixed:       30;\n'
        '    --z-modal-bg:    40;\n'
        '    --z-modal:       50;\n'
        '    --z-toast:       60;\n'
        '    --z-tooltip:     70;\n'
        '}',
        filename='z-index.css',
        styles=styles
    ))
    s.append(mistake_box(
        "The most common z-index mistake: setting z-index: 9999 on something and wondering "
        "why it's still behind another element. The answer is almost always stacking contexts. "
        "When an ancestor element has transform, opacity < 1, or filter applied, it creates "
        "a stacking context that caps all its children. Check the DevTools Layers panel to "
        "visualize stacking contexts. The fix is usually to move the element out of the "
        "creating ancestor, or apply isolation: isolate to the right container.",
        styles
    ))
    return s


# ============================================================================
# SECTION 3.6 — Flexbox — One-Dimensional Layout
# ============================================================================

def section_3_6(styles):
    s = []
    s.append(h1("3.6 Flexbox — One-Dimensional Layout", styles))
    s.append(p(
        "Flexbox (Flexible Box Layout) is a CSS layout mode designed for arranging items in "
        "a single dimension — either a row or a column. It handles the distribution of space "
        "and alignment of items with precision and flexibility that was impossible with floats "
        "and positioning tricks. Flexbox is the go-to tool for UI components: navbars, card "
        "rows, toolbars, form rows, and centered content.",
        styles
    ))
    s.append(analogy_box(
        "Flexbox is arranging books on a single shelf. The shelf is the flex container. The "
        "books are the flex items. You can decide whether books stand side-by-side (row) or "
        "stack vertically (column). You can push all books to one end, spread them evenly, "
        "or center them. Some books can be told to grow and fill empty space. You can align "
        "all books to the top edge, bottom edge, or center of the shelf. Flexbox gives you "
        "this control declaratively, without manual pixel math.",
        styles
    ))
    s.append(h2("Flex Container Properties", styles))
    s.append(code_block(
        '/* Apply to the PARENT to activate flexbox */\n'
        '.toolbar {\n'
        '    display: flex;                  /* activate flex */\n'
        '\n'
        '    /* Direction of the main axis */\n'
        '    flex-direction: row;            /* row | row-reverse | column | column-reverse */\n'
        '\n'
        '    /* Should items wrap if they overflow? */\n'
        '    flex-wrap: wrap;                /* nowrap | wrap | wrap-reverse */\n'
        '\n'
        '    /* Shorthand: flex-direction + flex-wrap */\n'
        '    flex-flow: row wrap;\n'
        '\n'
        '    /* Alignment on the MAIN axis (horizontal in row direction) */\n'
        '    justify-content: space-between;\n'
        '    /* flex-start | flex-end | center | space-between | space-around | space-evenly */\n'
        '\n'
        '    /* Alignment on the CROSS axis (vertical in row direction) */\n'
        '    align-items: center;\n'
        '    /* flex-start | flex-end | center | stretch | baseline */\n'
        '\n'
        '    /* When items wrap: alignment of ROWS on the cross axis */\n'
        '    align-content: flex-start;\n'
        '    /* same values as justify-content */\n'
        '\n'
        '    /* Gap between items (replaces margin hacks) */\n'
        '    gap: 1rem;                      /* row-gap + column-gap */\n'
        '    gap: 1rem 1.5rem;               /* row-gap 1rem, column-gap 1.5rem */\n'
        '    row-gap: 1rem;\n'
        '    column-gap: 1.5rem;\n'
        '}',
        filename='flex-container.css',
        styles=styles
    ))
    s.append(h2("Flex Item Properties", styles))
    s.append(code_block(
        '/* Apply to the CHILDREN to control their flex behavior */\n'
        '.nav-item {\n'
        '    /* flex-grow: how much extra space can this item absorb? */\n'
        '    /* 0 = don\'t grow (default). 1 = grow proportionally. */\n'
        '    flex-grow: 0;\n'
        '\n'
        '    /* flex-shrink: can this item shrink if container is too small? */\n'
        '    /* 1 = yes, shrink (default). 0 = no, never shrink. */\n'
        '    flex-shrink: 0;\n'
        '\n'
        '    /* flex-basis: the ideal starting size before growing/shrinking */\n'
        '    /* auto = use the element\'s natural size */\n'
        '    flex-basis: auto;\n'
        '\n'
        '    /* SHORTHAND: flex: grow shrink basis */\n'
        '    flex: 0 0 auto;       /* rigid — don\'t grow or shrink */\n'
        '    /* flex: 1;           -- grow: 1, shrink: 1, basis: 0 */\n'
        '    /* flex: auto;        -- grow: 1, shrink: 1, basis: auto */\n'
        '    /* flex: none;        -- grow: 0, shrink: 0, basis: auto (rigid) */\n'
        '\n'
        '    /* Override the container\'s align-items for this item only */\n'
        '    align-self: center;   /* flex-start | flex-end | center | stretch | baseline */\n'
        '\n'
        '    /* Override the visual order (NOT DOM order — bad for accessibility!) */\n'
        '    order: 0;             /* default. Larger = later in visual order */\n'
        '}',
        filename='flex-items.css',
        styles=styles
    ))
    s.append(h2("Common Flexbox Patterns", styles))
    s.append(h3("Pattern 1: Perfect Centering", styles))
    s.append(code_block(
        '/* The simplest centering solution in CSS history */\n'
        '.center-everything {\n'
        '    display: flex;\n'
        '    justify-content: center;  /* horizontal center */\n'
        '    align-items: center;      /* vertical center */\n'
        '    min-height: 100vh;        /* full viewport height */\n'
        '}\n'
        '\n'
        '/* Center a modal in a viewport */\n'
        '.modal-wrapper {\n'
        '    display: flex;\n'
        '    justify-content: center;\n'
        '    align-items: center;\n'
        '    position: fixed;\n'
        '    inset: 0;\n'
        '    background: rgba(0,0,0,0.5);\n'
        '}',
        filename='flex-centering.css',
        styles=styles
    ))
    s.append(h3("Pattern 2: Responsive Navigation Bar", styles))
    s.append(code_block(
        '/* HTML structure:\n'
        '   <header class="site-header">\n'
        '     <a class="logo" href="/">TradeBoard</a>\n'
        '     <nav class="main-nav">\n'
        '       <ul class="nav-list">\n'
        '         <li><a href="/markets">Markets</a></li>\n'
        '         <li><a href="/portfolio">Portfolio</a></li>\n'
        '         <li><a href="/news">News</a></li>\n'
        '       </ul>\n'
        '     </nav>\n'
        '     <div class="header-actions">\n'
        '       <button class="btn-sign-in">Sign In</button>\n'
        '     </div>\n'
        '   </header>\n'
        '*/\n'
        '\n'
        '.site-header {\n'
        '    display: flex;\n'
        '    align-items: center;\n'
        '    justify-content: space-between;\n'
        '    padding: 0 2rem;\n'
        '    height: 64px;\n'
        '    background: #1a1a2e;\n'
        '    position: sticky;\n'
        '    top: 0;\n'
        '    z-index: var(--z-fixed, 30);\n'
        '}\n'
        '\n'
        '.logo {\n'
        '    color: white;\n'
        '    font-size: 1.25rem;\n'
        '    font-weight: 800;\n'
        '    text-decoration: none;\n'
        '    letter-spacing: -0.03em;\n'
        '    flex-shrink: 0;    /* never compress the logo */\n'
        '}\n'
        '\n'
        '.nav-list {\n'
        '    display: flex;\n'
        '    list-style: none;\n'
        '    margin: 0;\n'
        '    padding: 0;\n'
        '    gap: 0.25rem;\n'
        '}\n'
        '\n'
        '.nav-list a {\n'
        '    display: block;\n'
        '    padding: 0.5rem 0.875rem;\n'
        '    color: rgba(255,255,255,0.75);\n'
        '    text-decoration: none;\n'
        '    border-radius: 6px;\n'
        '    font-size: 0.9rem;\n'
        '    font-weight: 500;\n'
        '    transition: color 0.2s, background 0.2s;\n'
        '}\n'
        '\n'
        '.nav-list a:hover,\n'
        '.nav-list a[aria-current="page"] {\n'
        '    color: white;\n'
        '    background: rgba(255,255,255,0.1);\n'
        '}\n'
        '\n'
        '.header-actions {\n'
        '    display: flex;\n'
        '    align-items: center;\n'
        '    gap: 0.75rem;\n'
        '    flex-shrink: 0;\n'
        '}\n'
        '\n'
        '.btn-sign-in {\n'
        '    background: #e94560;\n'
        '    color: white;\n'
        '    border: none;\n'
        '    border-radius: 6px;\n'
        '    padding: 0.5rem 1.25rem;\n'
        '    font-weight: 600;\n'
        '    font-size: 0.875rem;\n'
        '    cursor: pointer;\n'
        '    transition: background 0.2s, transform 0.15s;\n'
        '}\n'
        '\n'
        '.btn-sign-in:hover {\n'
        '    background: #c73854;\n'
        '    transform: translateY(-1px);\n'
        '}',
        filename='navbar-flex.css',
        styles=styles
    ))
    s.append(h3("Pattern 3: Card Row with Growing Cards", styles))
    s.append(code_block(
        '/* A row of cards that stretch to fill available space evenly */\n'
        '.card-row {\n'
        '    display: flex;\n'
        '    gap: 1.5rem;\n'
        '    flex-wrap: wrap;\n'
        '}\n'
        '\n'
        '.card-row .stock-card {\n'
        '    flex: 1 1 220px;      /* grow and shrink, ideal width 220px */\n'
        '    /* Cards fill a row, wrapping when they can\'t all fit at 220px */\n'
        '}\n'
        '\n'
        '/* Card internal layout using nested flexbox */\n'
        '.stock-card {\n'
        '    display: flex;\n'
        '    flex-direction: column;\n'
        '    gap: 0.5rem;\n'
        '    padding: 1.5rem;\n'
        '    background: white;\n'
        '    border-radius: 12px;\n'
        '    border: 1px solid #e2e8f0;\n'
        '}\n'
        '\n'
        '.stock-card__footer {\n'
        '    display: flex;\n'
        '    justify-content: space-between;\n'
        '    align-items: center;\n'
        '    margin-top: auto;     /* pushes footer to the bottom regardless of content */\n'
        '    padding-top: 1rem;\n'
        '    border-top: 1px solid #f1f5f9;\n'
        '}',
        filename='card-row-flex.css',
        styles=styles
    ))
    s.append(h3("Pattern 4: Holy Grail Sidebar Layout", styles))
    s.append(code_block(
        '/* Holy Grail: header, footer, main + sidebar(s) */\n'
        '/* HTML:\n'
        '   <div class="app-shell">\n'
        '     <header class="app-header">...</header>\n'
        '     <div class="app-body">\n'
        '       <aside class="sidebar sidebar--left">...</aside>\n'
        '       <main class="main-content">...</main>\n'
        '       <aside class="sidebar sidebar--right">...</aside>\n'
        '     </div>\n'
        '     <footer class="app-footer">...</footer>\n'
        '   </div>\n'
        '*/\n'
        '\n'
        '.app-shell {\n'
        '    display: flex;\n'
        '    flex-direction: column;\n'
        '    min-height: 100vh;\n'
        '}\n'
        '\n'
        '.app-header, .app-footer {\n'
        '    flex-shrink: 0;       /* never compress header/footer */\n'
        '}\n'
        '\n'
        '.app-body {\n'
        '    display: flex;\n'
        '    flex: 1;              /* grow to fill remaining height */\n'
        '    gap: 0;\n'
        '}\n'
        '\n'
        '.sidebar {\n'
        '    flex: 0 0 260px;      /* fixed width, never grow or shrink */\n'
        '    background: #f8fafc;\n'
        '    border-right: 1px solid #e2e8f0;\n'
        '    overflow-y: auto;\n'
        '}\n'
        '\n'
        '.sidebar--right {\n'
        '    border-right: none;\n'
        '    border-left: 1px solid #e2e8f0;\n'
        '}\n'
        '\n'
        '.main-content {\n'
        '    flex: 1;              /* grows to fill all remaining space */\n'
        '    overflow-y: auto;\n'
        '    padding: 2rem;\n'
        '}',
        filename='holy-grail-flex.css',
        styles=styles
    ))
    s.append(principal_box(
        "Flexbox is one-dimensional — it works along one axis at a time. When you find yourself "
        "nesting flex containers three levels deep to achieve a layout, that is a signal you "
        "should be using CSS Grid for the outer structure. The golden rule: use Flexbox for "
        "component-level alignment (navbar items, card internals, button groups) and Grid for "
        "page-level layout (dashboard structure, multi-column grids). They complement each "
        "other and are designed to be used together.",
        styles
    ))
    return s


# ============================================================================
# SECTION 3.7 — CSS Grid — Two-Dimensional Layout
# ============================================================================

def section_3_7(styles):
    s = []
    s.append(h1("3.7 CSS Grid — Two-Dimensional Layout", styles))
    s.append(p(
        "CSS Grid is the first CSS layout system designed to work in two dimensions simultaneously — "
        "rows AND columns at the same time. Before Grid, achieving a true two-dimensional layout "
        "required hacky float tricks, table-based layouts, or nested flexbox containers. Grid "
        "solves this elegantly, giving you precise control over both axes with minimal CSS.",
        styles
    ))
    s.append(analogy_box(
        "CSS Grid is a spreadsheet. Your grid container is the spreadsheet. The columns and "
        "rows are the grid lines you define. Each cell is an intersection of a row and column. "
        "You can place items in specific cells — 'this item goes in row 2, column 3.' Or you "
        "can let items flow automatically and just define the column structure. You can even "
        "span items across multiple rows and columns — just like merging cells in Excel.",
        styles
    ))
    s.append(h2("Grid Container Properties", styles))
    s.append(code_block(
        '/* Apply to the PARENT to activate CSS Grid */\n'
        '.dashboard {\n'
        '    display: grid;\n'
        '\n'
        '    /* Define columns: three equal columns */\n'
        '    grid-template-columns: 1fr 1fr 1fr;\n'
        '    /* Shorthand with repeat(): */\n'
        '    grid-template-columns: repeat(3, 1fr);\n'
        '\n'
        '    /* The fr unit: fraction of available space */\n'
        '    /* 1fr 2fr 1fr = 25% + 50% + 25% */\n'
        '    grid-template-columns: 1fr 2fr 1fr;\n'
        '\n'
        '    /* Mix fixed and flexible: sidebar + main + panel */\n'
        '    grid-template-columns: 260px 1fr 320px;\n'
        '\n'
        '    /* Define rows: first row is auto, rest take remaining space */\n'
        '    grid-template-rows: auto 1fr auto;\n'
        '    /* Or let rows size automatically (most common): */\n'
        '    /* grid-auto-rows: minmax(100px, auto); */\n'
        '\n'
        '    /* Gap between cells */\n'
        '    gap: 1.5rem;              /* both row and column gap */\n'
        '    row-gap: 1rem;\n'
        '    column-gap: 1.5rem;\n'
        '\n'
        '    /* Height */\n'
        '    min-height: 100vh;\n'
        '}',
        filename='grid-container.css',
        styles=styles
    ))
    s.append(h2("The fr Unit, repeat(), minmax(), auto-fill, auto-fit", styles))
    s.append(code_block(
        '/* fr = fraction of available space after fixed sizes are taken */\n'
        '.grid {\n'
        '    /* 3 equal columns */\n'
        '    grid-template-columns: repeat(3, 1fr);\n'
        '\n'
        '    /* 260px sidebar + flexible main */\n'
        '    grid-template-columns: 260px 1fr;\n'
        '\n'
        '    /* minmax(min, max) — column is at least min, at most max */\n'
        '    grid-template-columns: repeat(3, minmax(200px, 1fr));\n'
        '\n'
        '    /* auto-fill: fill row with as many columns as fit at minimum size */\n'
        '    /* creates empty columns if needed */\n'
        '    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));\n'
        '\n'
        '    /* auto-fit: same but collapses empty columns */\n'
        '    /* items GROW to fill all available space */\n'
        '    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));\n'
        '}\n'
        '\n'
        '/* The BEST responsive grid — no media queries needed! */\n'
        '.responsive-card-grid {\n'
        '    display: grid;\n'
        '    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));\n'
        '    gap: 1.5rem;\n'
        '    /* At 800px wide: shows 3 cards (3 x 240 = 720) */\n'
        '    /* At 500px wide: shows 2 cards (2 x 240 = 480) */\n'
        '    /* At 280px wide: shows 1 card  (1 x 240 = 240) */\n'
        '    /* Zero media queries. Pure grid math. */\n'
        '}',
        filename='grid-fr-units.css',
        styles=styles
    ))
    s.append(h2("Grid Template Areas — Named Layout Regions", styles))
    s.append(code_block(
        '/* grid-template-areas: draw your layout like ASCII art */\n'
        '\n'
        '/* HTML:\n'
        '   <div class="app-layout">\n'
        '     <header class="header">Header</header>\n'
        '     <aside class="sidebar">Sidebar</aside>\n'
        '     <main class="main">Main Content</main>\n'
        '     <aside class="panel">Info Panel</aside>\n'
        '     <footer class="footer">Footer</footer>\n'
        '   </div>\n'
        '*/\n'
        '\n'
        '.app-layout {\n'
        '    display: grid;\n'
        '    grid-template-columns: 240px 1fr 300px;\n'
        '    grid-template-rows: 64px 1fr 48px;\n'
        '    min-height: 100vh;\n'
        '    grid-template-areas:\n'
        '        "header  header  header"\n'
        '        "sidebar main    panel"\n'
        '        "footer  footer  footer";\n'
        '    gap: 0;\n'
        '}\n'
        '\n'
        '/* Assign each element to its named area */\n'
        '.header  { grid-area: header; }\n'
        '.sidebar { grid-area: sidebar; }\n'
        '.main    { grid-area: main; }\n'
        '.panel   { grid-area: panel; }\n'
        '.footer  { grid-area: footer; }\n'
        '\n'
        '/* Responsive: collapse to single column on mobile */\n'
        '@media (max-width: 768px) {\n'
        '    .app-layout {\n'
        '        grid-template-columns: 1fr;\n'
        '        grid-template-rows: auto;\n'
        '        grid-template-areas:\n'
        '            "header"\n'
        '            "main"\n'
        '            "sidebar"\n'
        '            "panel"\n'
        '            "footer";\n'
        '    }\n'
        '}',
        filename='grid-areas.css',
        styles=styles
    ))
    s.append(h2("Grid Item Placement", styles))
    s.append(code_block(
        '/* Control where items land in the grid */\n'
        '\n'
        '.stock-card--featured {\n'
        '    /* Span across columns 1 to 3 (two columns wide) */\n'
        '    grid-column: 1 / 3;       /* line 1 to line 3 */\n'
        '    grid-column: 1 / span 2;  /* start at line 1, span 2 columns */\n'
        '    grid-column: span 2;      /* auto-place, but span 2 */\n'
        '\n'
        '    /* Span across rows */\n'
        '    grid-row: 1 / 3;          /* spans two rows */\n'
        '    grid-row: span 2;\n'
        '\n'
        '    /* Shorthand: row-start / column-start / row-end / column-end */\n'
        '    grid-area: 1 / 1 / 3 / 3;  /* rows 1-3, columns 1-3 */\n'
        '}\n'
        '\n'
        '/* Negative line numbers: count from the end */\n'
        '.full-width {\n'
        '    grid-column: 1 / -1;      /* from first line to last line */\n'
        '}\n'
        '\n'
        '/* Named grid lines */\n'
        '.layout {\n'
        '    grid-template-columns: [sidebar-start] 260px [sidebar-end main-start] 1fr [main-end];\n'
        '}\n'
        '\n'
        '.main-area {\n'
        '    grid-column: main-start / main-end;  /* clearer than numbers */\n'
        '}',
        filename='grid-item-placement.css',
        styles=styles
    ))
    s.append(h2("Complete TradeBoard Dashboard Layout", styles))
    s.append(code_block(
        '/* TradeBoard complete dashboard using Grid + Flexbox */\n'
        '/* grid-template-areas: TradeBoard-style layout */\n'
        '\n'
        ':root {\n'
        '    --header-height: 64px;\n'
        '    --sidebar-width: 240px;\n'
        '    --panel-width:   320px;\n'
        '    --color-bg:       #0f1117;\n'
        '    --color-surface:  #1a1d27;\n'
        '    --color-border:   #2a2d3d;\n'
        '    --color-text:     #e2e8f0;\n'
        '    --color-accent:   #e94560;\n'
        '}\n'
        '\n'
        '/* Root layout */\n'
        '.tradeboard {\n'
        '    display: grid;\n'
        '    grid-template-columns: var(--sidebar-width) 1fr var(--panel-width);\n'
        '    grid-template-rows: var(--header-height) 1fr;\n'
        '    grid-template-areas:\n'
        '        "header header header"\n'
        '        "sidebar main   panel";\n'
        '    min-height: 100vh;\n'
        '    background: var(--color-bg);\n'
        '    color: var(--color-text);\n'
        '    font-family: system-ui, sans-serif;\n'
        '}\n'
        '\n'
        '.tradeboard__header {\n'
        '    grid-area: header;\n'
        '    background: var(--color-surface);\n'
        '    border-bottom: 1px solid var(--color-border);\n'
        '    display: flex;\n'
        '    align-items: center;\n'
        '    justify-content: space-between;\n'
        '    padding: 0 1.5rem;\n'
        '    position: sticky;\n'
        '    top: 0;\n'
        '    z-index: 100;\n'
        '}\n'
        '\n'
        '.tradeboard__sidebar {\n'
        '    grid-area: sidebar;\n'
        '    background: var(--color-surface);\n'
        '    border-right: 1px solid var(--color-border);\n'
        '    overflow-y: auto;\n'
        '    padding: 1rem;\n'
        '}\n'
        '\n'
        '.tradeboard__main {\n'
        '    grid-area: main;\n'
        '    overflow-y: auto;\n'
        '    padding: 1.5rem;\n'
        '\n'
        '    /* Inner grid for metric cards */\n'
        '    display: grid;\n'
        '    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));\n'
        '    grid-auto-rows: min-content;\n'
        '    gap: 1rem;\n'
        '    align-content: start;\n'
        '}\n'
        '\n'
        '.tradeboard__panel {\n'
        '    grid-area: panel;\n'
        '    background: var(--color-surface);\n'
        '    border-left: 1px solid var(--color-border);\n'
        '    overflow-y: auto;\n'
        '    padding: 1rem;\n'
        '    display: flex;\n'
        '    flex-direction: column;\n'
        '    gap: 0.75rem;\n'
        '}\n'
        '\n'
        '/* Responsive: tablet */\n'
        '@media (max-width: 1024px) {\n'
        '    .tradeboard {\n'
        '        grid-template-columns: var(--sidebar-width) 1fr;\n'
        '        grid-template-areas:\n'
        '            "header header"\n'
        '            "sidebar main";\n'
        '    }\n'
        '    .tradeboard__panel { display: none; }  /* hide right panel */\n'
        '}\n'
        '\n'
        '/* Responsive: mobile */\n'
        '@media (max-width: 640px) {\n'
        '    .tradeboard {\n'
        '        grid-template-columns: 1fr;\n'
        '        grid-template-rows: var(--header-height) 1fr;\n'
        '        grid-template-areas:\n'
        '            "header"\n'
        '            "main";\n'
        '    }\n'
        '    .tradeboard__sidebar { display: none; }  /* hide sidebar */\n'
        '}',
        filename='tradeboard-dashboard.css',
        styles=styles
    ))
    s.append(h2("When to Use Grid vs Flexbox", styles))
    s.append(bullet("<b>Use Grid</b> when you have a two-dimensional layout — both rows AND columns matter simultaneously", styles))
    s.append(bullet("<b>Use Grid</b> when you want content to conform to a defined structure (items fit INTO the grid)", styles))
    s.append(bullet("<b>Use Flexbox</b> when you have a one-dimensional layout — either a row OR a column", styles))
    s.append(bullet("<b>Use Flexbox</b> when you want the structure to conform to the content (grid expands around content)", styles))
    s.append(bullet("<b>Use both together:</b> Grid for page-level layout, Flexbox for component internals", styles))
    return s


# ============================================================================
# SECTION 3.8 — Responsive Design
# ============================================================================

def section_3_8(styles):
    s = []
    s.append(h1("3.8 Responsive Design", styles))
    s.append(p(
        "Responsive design means your website adapts to any screen size and device — from a "
        "4-inch phone to a 34-inch ultrawide monitor. In 2024, over 60% of web traffic comes "
        "from mobile devices. A non-responsive site is broken for the majority of your users.",
        styles
    ))
    s.append(analogy_box(
        "Responsive design is like water. Water takes the shape of any container you pour it "
        "into — a narrow bottle, a wide bowl, a tall glass. A well-designed responsive website "
        "does the same: it rearranges, resizes, and re-stacks its content to perfectly fill "
        "whatever screen it is viewed on, without losing functionality or readability.",
        styles
    ))
    s.append(h2("The Viewport Meta Tag — Required", styles))
    s.append(p(
        "Before media queries work, you must tell the browser to use the device's actual width "
        "instead of simulating a desktop viewport. This one line in your &lt;head&gt; is "
        "mandatory for any responsive site:",
        styles
    ))
    s.append(code_block(
        '<!-- In your <head> — required for responsive design -->\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '\n'
        '<!-- Without this, phones render at 980px then zoom out — not responsive! -->\n'
        '<!-- With this, a 390px wide phone gives you 390px to work with -->',
        filename='head-viewport.html',
        styles=styles
    ))
    s.append(h2("Media Queries — Syntax and Common Breakpoints", styles))
    s.append(code_block(
        '/* Media query syntax */\n'
        '@media [media-type] and ([feature]) {\n'
        '    /* CSS that applies only when condition is true */\n'
        '}\n'
        '\n'
        '/* Most common: screen size breakpoints */\n'
        '@media (max-width: 640px) {\n'
        '    /* Mobile — applied when viewport is 640px or narrower */\n'
        '}\n'
        '\n'
        '@media (min-width: 641px) and (max-width: 1024px) {\n'
        '    /* Tablet */\n'
        '}\n'
        '\n'
        '@media (min-width: 1025px) {\n'
        '    /* Desktop */\n'
        '}\n'
        '\n'
        '/* Common breakpoint scale (similar to Tailwind CSS defaults) */\n'
        '/* sm:  640px  — large phones, small tablets in portrait */\n'
        '/* md:  768px  — tablets */\n'
        '/* lg:  1024px — small laptops */\n'
        '/* xl:  1280px — desktops */\n'
        '/* 2xl: 1536px — large desktops/wide screens */\n'
        '\n'
        '/* Other useful media features */\n'
        '@media (orientation: landscape) { /* ... */ }\n'
        '@media (prefers-color-scheme: dark) { /* ... */ }\n'
        '@media (prefers-reduced-motion: reduce) { /* ... */ }\n'
        '@media (hover: hover) { /* user has a pointing device (mouse) */ }\n'
        '@media (pointer: coarse) { /* touch device — make targets bigger */ }',
        filename='media-queries.css',
        styles=styles
    ))
    s.append(h2("Mobile-First vs Desktop-First", styles))
    s.append(p(
        "Mobile-first means you write your base CSS for mobile screens, then use "
        "<b>min-width</b> media queries to add styles as the screen gets wider. "
        "Desktop-first means you write CSS for desktop, then use <b>max-width</b> queries "
        "to adjust for smaller screens.",
        styles
    ))
    s.append(code_block(
        '/* ========================================\n'
        '   MOBILE-FIRST (recommended approach)\n'
        '   ======================================== */\n'
        '\n'
        '/* Base styles: mobile */\n'
        '.card-grid {\n'
        '    display: grid;\n'
        '    grid-template-columns: 1fr;  /* single column on mobile */\n'
        '    gap: 1rem;\n'
        '    padding: 1rem;\n'
        '}\n'
        '\n'
        '/* Tablet+ */\n'
        '@media (min-width: 640px) {\n'
        '    .card-grid {\n'
        '        grid-template-columns: repeat(2, 1fr);  /* 2 columns */\n'
        '        gap: 1.25rem;\n'
        '        padding: 1.5rem;\n'
        '    }\n'
        '}\n'
        '\n'
        '/* Desktop+ */\n'
        '@media (min-width: 1024px) {\n'
        '    .card-grid {\n'
        '        grid-template-columns: repeat(3, 1fr);  /* 3 columns */\n'
        '        gap: 1.5rem;\n'
        '        padding: 2rem;\n'
        '    }\n'
        '}\n'
        '\n'
        '/* ========================================\n'
        '   DESKTOP-FIRST (works but adds complexity)\n'
        '   ======================================== */\n'
        '\n'
        '.card-grid {\n'
        '    grid-template-columns: repeat(3, 1fr);  /* desktop by default */\n'
        '}\n'
        '\n'
        '@media (max-width: 1023px) {\n'
        '    .card-grid { grid-template-columns: repeat(2, 1fr); }\n'
        '}\n'
        '@media (max-width: 639px) {\n'
        '    .card-grid { grid-template-columns: 1fr; }\n'
        '}',
        filename='mobile-first.css',
        styles=styles
    ))
    s.append(principal_box(
        "Mobile-first is not just a preference — it is a performance strategy. CSS is "
        "render-blocking. If you write desktop-first CSS with max-width media queries, "
        "mobile devices must download, parse, and apply ALL your CSS (including the desktop "
        "rules that immediately get overridden). Mobile-first ensures mobile devices process "
        "only the minimum CSS they need. For a codebase serving 60%+ mobile users, this is "
        "a meaningful performance win.",
        styles
    ))
    s.append(h2("Fluid Typography with clamp()", styles))
    s.append(p(
        "The clamp() function accepts three arguments: minimum, preferred, and maximum. "
        "It creates typography that smoothly scales between screen sizes without any "
        "media queries. The preferred value is typically a viewport width unit (vw):",
        styles
    ))
    s.append(code_block(
        '/* clamp(min, preferred, max) */\n'
        '\n'
        ':root {\n'
        '    /* Font size scales from 16px at 320px viewport to 20px at 1200px+ */\n'
        '    --font-base: clamp(1rem, 0.9rem + 0.5vw, 1.25rem);\n'
        '\n'
        '    /* H1: 28px on mobile up to 56px on desktop */\n'
        '    --font-h1: clamp(1.75rem, 1.25rem + 2.5vw, 3.5rem);\n'
        '\n'
        '    /* H2: 22px to 36px */\n'
        '    --font-h2: clamp(1.375rem, 1rem + 1.875vw, 2.25rem);\n'
        '\n'
        '    /* Padding: 1rem minimum, prefers 5%, 3rem maximum */\n'
        '    --spacing-page: clamp(1rem, 5vw, 3rem);\n'
        '}\n'
        '\n'
        'body { font-size: var(--font-base); }\n'
        'h1   { font-size: var(--font-h1); }\n'
        'h2   { font-size: var(--font-h2); }\n'
        '.page-container { padding: var(--spacing-page); }\n'
        '\n'
        '/* No media queries needed for these! The browser calculates\n'
        '   the right size automatically at every viewport width. */\n'
        '\n'
        '/* How to calculate clamp values:\n'
        '   You want 1rem at 320px and 1.5rem at 1200px.\n'
        '   slope = (1.5 - 1) / (1200 - 320) = 0.0005681 rem/px\n'
        '   intercept = 1 - (0.0005681 * 320) = 0.8182 rem\n'
        '   preferred = 0.8182rem + 0.05681 * 100vw\n'
        '   clamp(1rem, 0.82rem + 0.057vw * 100, 1.5rem) */\n'
        '/* Tools like utopia.fyi generate these automatically. */',
        filename='fluid-typography.css',
        styles=styles
    ))
    s.append(h2("Container Queries — The Modern Approach", styles))
    s.append(p(
        "Media queries are based on the viewport width. But what if you have a component that "
        "can appear in a wide main column or a narrow sidebar? Container queries let a component "
        "respond to the size of its <b>container</b>, not the viewport. This is a game-changer "
        "for component-based design:",
        styles
    ))
    s.append(code_block(
        '/* Container queries — supported in all modern browsers (2023+) */\n'
        '\n'
        '/* Step 1: Define which element is the container */\n'
        '.card-container {\n'
        '    container-type: inline-size;   /* respond to width changes */\n'
        '    container-name: card;          /* optional name */\n'
        '    /* shorthand: container: card / inline-size; */\n'
        '}\n'
        '\n'
        '/* Step 2: Write container query inside the component */\n'
        '.stock-card {\n'
        '    display: flex;\n'
        '    flex-direction: column;        /* default: stacked */\n'
        '    padding: 1rem;\n'
        '}\n'
        '\n'
        '/* When the CONTAINER is at least 400px wide, switch to row */\n'
        '@container card (min-width: 400px) {\n'
        '    .stock-card {\n'
        '        flex-direction: row;\n'
        '        align-items: center;\n'
        '        gap: 1.5rem;\n'
        '    }\n'
        '\n'
        '    .stock-card__chart {\n'
        '        display: block;            /* show chart only when wide enough */\n'
        '        width: 120px;\n'
        '        flex-shrink: 0;\n'
        '    }\n'
        '}\n'
        '\n'
        '/* Now the same .stock-card component:\n'
        '   - In a narrow sidebar: stacks vertically, no chart\n'
        '   - In a wide main column: row layout, chart visible\n'
        '   WITHOUT knowing anything about the viewport size! */',
        filename='container-queries.css',
        styles=styles
    ))
    s.append(h2("Responsive Images", styles))
    s.append(code_block(
        '/* Basic responsive image */\n'
        'img {\n'
        '    max-width: 100%;         /* never exceed container width */\n'
        '    height: auto;            /* maintain aspect ratio */\n'
        '    display: block;          /* remove inline gap below image */\n'
        '}\n'
        '\n'
        '/* Modern responsive images with srcset */\n'
        '/* HTML: tell browser about available image sizes */\n'
        '<!-- <img\n'
        '  src="chart-800.webp"\n'
        '  srcset="chart-400.webp 400w,\n'
        '          chart-800.webp 800w,\n'
        '          chart-1600.webp 1600w"\n'
        '  sizes="(max-width: 640px) 100vw,\n'
        '         (max-width: 1024px) 50vw,\n'
        '         33vw"\n'
        '  alt="Stock price chart for AAPL"\n'
        '  loading="lazy"\n'
        '  decoding="async"\n'
        '  width="800" height="400"\n'
        '> -->\n'
        '\n'
        '/* CSS for aspect-ratio boxes (prevent layout shift) */\n'
        '.chart-wrapper {\n'
        '    aspect-ratio: 16 / 9;    /* maintain 16:9 ratio */\n'
        '    width: 100%;\n'
        '    overflow: hidden;\n'
        '    border-radius: 8px;\n'
        '    background: #f1f5f9;     /* placeholder while loading */\n'
        '}\n'
        '\n'
        '.chart-wrapper img {\n'
        '    width: 100%;\n'
        '    height: 100%;\n'
        '    object-fit: cover;       /* cover | contain | fill */\n'
        '    object-position: center; /* where to anchor the crop */\n'
        '}',
        filename='responsive-images.css',
        styles=styles
    ))
    return s


# ============================================================================
# SECTION 3.9 — Typography
# ============================================================================

def section_3_9(styles):
    s = []
    s.append(h1("3.9 Typography", styles))
    s.append(p(
        "Typography is the single most powerful visual design lever in web development. "
        "Studies consistently show that users judge a website's professionalism primarily by "
        "its typography. A well-designed typographic system — consistent sizing, spacing, and "
        "font choices — makes everything look polished. Poor typography makes excellent content "
        "look amateur.",
        styles
    ))
    s.append(h2("Font Families and Font Stacks", styles))
    s.append(code_block(
        '/* Font stack: list fallbacks in case the preferred font fails to load */\n'
        ':root {\n'
        '    /* System UI stack — fastest, no download, looks native */\n'
        '    --font-sans:\n'
        '        system-ui,\n'
        '        -apple-system,           /* Safari/macOS */\n'
        '        BlinkMacSystemFont,      /* Chrome on macOS */\n'
        '        "Segoe UI",              /* Windows */\n'
        '        Roboto,                  /* Android */\n'
        '        Oxygen,                  /* KDE Linux */\n'
        '        Ubuntu,                  /* Ubuntu Linux */\n'
        '        Cantarell,               /* GNOME Linux */\n'
        '        sans-serif;              /* final fallback */\n'
        '\n'
        '    /* Monospace for code */\n'
        '    --font-mono:\n'
        '        "JetBrains Mono",\n'
        '        "Fira Code",\n'
        '        "Cascadia Code",\n'
        '        Menlo,                   /* macOS */\n'
        '        Monaco,                  /* macOS */\n'
        '        "Courier New",\n'
        '        monospace;\n'
        '\n'
        '    /* Serif for editorial content */\n'
        '    --font-serif:\n'
        '        "Georgia",\n'
        '        "Cambria",\n'
        '        "Times New Roman",\n'
        '        serif;\n'
        '}',
        filename='font-stacks.css',
        styles=styles
    ))
    s.append(h2("Loading Custom Fonts with @font-face", styles))
    s.append(code_block(
        '/* Self-hosting fonts with @font-face */\n'
        '\n'
        '@font-face {\n'
        '    font-family: "Inter";\n'
        '    font-style: normal;\n'
        '    font-weight: 400;\n'
        '    font-display: swap;                 /* FOUT strategy — see below */\n'
        '    src:\n'
        '        url("/fonts/inter-regular.woff2") format("woff2"),   /* preferred */\n'
        '        url("/fonts/inter-regular.woff")  format("woff");    /* fallback */\n'
        '}\n'
        '\n'
        '@font-face {\n'
        '    font-family: "Inter";\n'
        '    font-style: normal;\n'
        '    font-weight: 700;\n'
        '    font-display: swap;\n'
        '    src: url("/fonts/inter-bold.woff2") format("woff2");\n'
        '}\n'
        '\n'
        '/* Variable fonts — one file for ALL weights (modern approach) */\n'
        '@font-face {\n'
        '    font-family: "Inter";\n'
        '    font-style: normal;\n'
        '    font-weight: 100 900;               /* supports weight range */\n'
        '    font-display: swap;\n'
        '    src: url("/fonts/inter-variable.woff2") format("woff2-variations");\n'
        '}\n'
        '\n'
        '/* Now use the variable font with any weight */\n'
        'h1 { font-weight: 750; }  /* non-standard weight, smoothly interpolated */\n'
        '\n'
        '/* Google Fonts (external, fast CDN) */\n'
        '/* In HTML <head>: */\n'
        '/* <link rel="preconnect" href="https://fonts.googleapis.com"> */\n'
        '/* <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> */\n'
        '/* <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet"> */',
        filename='font-face.css',
        styles=styles
    ))
    s.append(h2("Web Font Loading Strategies", styles))
    s.append(p(
        "The <b>font-display</b> descriptor controls what happens while a web font is loading. "
        "This affects the user experience significantly:",
        styles
    ))
    s.append(bullet("<b>font-display: auto</b> — browser decides (usually swap or block)", styles))
    s.append(bullet("<b>font-display: block</b> — invisible text for up to 3 seconds, then swap (FOIT — Flash of Invisible Text)", styles))
    s.append(bullet("<b>font-display: swap</b> — show fallback immediately, swap when loaded (FOUT — Flash of Unstyled Text) — recommended", styles))
    s.append(bullet("<b>font-display: fallback</b> — invisible for 100ms, then fallback, swap only within 3 seconds", styles))
    s.append(bullet("<b>font-display: optional</b> — uses fallback if font is not instantly available — best for performance", styles))
    s.append(h2("Typographic Scale — Using Ratios", styles))
    s.append(p(
        "A typographic scale creates visual harmony by sizing headings proportionally. "
        "Instead of arbitrary pixel sizes, you multiply a base size by a consistent ratio. "
        "Common ratios: 1.25 (Major Third), 1.333 (Perfect Fourth), 1.618 (Golden Ratio).",
        styles
    ))
    s.append(code_block(
        '/* Typographic scale — Major Third ratio (1.25) */\n'
        '/* Base: 1rem (16px) */\n'
        '\n'
        ':root {\n'
        '    --text-xs:   0.64rem;    /* 10.24px — 16 / 1.25 / 1.25 */\n'
        '    --text-sm:   0.8rem;     /* 12.8px  — 16 / 1.25 */\n'
        '    --text-base: 1rem;       /* 16px */\n'
        '    --text-md:   1.25rem;    /* 20px    — 16 * 1.25 */\n'
        '    --text-lg:   1.563rem;   /* 25px    — 16 * 1.25^2 */\n'
        '    --text-xl:   1.953rem;   /* 31.25px — 16 * 1.25^3 */\n'
        '    --text-2xl:  2.441rem;   /* 39px    — 16 * 1.25^4 */\n'
        '    --text-3xl:  3.052rem;   /* 48.8px  — 16 * 1.25^5 */\n'
        '}\n'
        '\n'
        '/* Apply the scale */\n'
        'body  { font-size: var(--text-base); line-height: 1.6; }\n'
        'small { font-size: var(--text-sm); }\n'
        'h4    { font-size: var(--text-md);  line-height: 1.4; }\n'
        'h3    { font-size: var(--text-lg);  line-height: 1.35; }\n'
        'h2    { font-size: var(--text-xl);  line-height: 1.3; }\n'
        'h1    { font-size: var(--text-2xl); line-height: 1.2; }\n'
        '.hero-title { font-size: var(--text-3xl); line-height: 1.1; }\n'
        '\n'
        '/* Fluid: scale with viewport using clamp() */\n'
        ':root {\n'
        '    --text-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);\n'
        '    --text-h1: clamp(1.953rem, 1.5rem + 2.5vw, 3.052rem);\n'
        '}',
        filename='typographic-scale.css',
        styles=styles
    ))
    s.append(h2("Complete Typography System", styles))
    s.append(code_block(
        '/* Complete professional typography system for TradeBoard */\n'
        '\n'
        ':root {\n'
        '    /* Font families */\n'
        '    --font-sans: "Inter", system-ui, -apple-system, sans-serif;\n'
        '    --font-mono: "JetBrains Mono", "Fira Code", monospace;\n'
        '\n'
        '    /* Type scale (Perfect Fourth — 1.333) */\n'
        '    --text-xs:   0.563rem;    /* captions, labels */\n'
        '    --text-sm:   0.75rem;     /* secondary text */\n'
        '    --text-base: 1rem;        /* body text */\n'
        '    --text-md:   1.333rem;    /* lead text */\n'
        '    --text-lg:   1.777rem;    /* H3 */\n'
        '    --text-xl:   2.369rem;    /* H2 */\n'
        '    --text-2xl:  3.157rem;    /* H1 */\n'
        '    --text-3xl:  4.209rem;    /* display */\n'
        '\n'
        '    /* Line heights */\n'
        '    --leading-tight: 1.2;\n'
        '    --leading-snug:  1.35;\n'
        '    --leading-normal: 1.5;\n'
        '    --leading-relaxed: 1.65;\n'
        '    --leading-loose: 1.8;\n'
        '\n'
        '    /* Font weights */\n'
        '    --weight-light:   300;\n'
        '    --weight-normal:  400;\n'
        '    --weight-medium:  500;\n'
        '    --weight-semibold: 600;\n'
        '    --weight-bold:    700;\n'
        '    --weight-black:   900;\n'
        '\n'
        '    /* Letter spacing */\n'
        '    --tracking-tight:  -0.025em;\n'
        '    --tracking-normal:  0;\n'
        '    --tracking-wide:    0.025em;\n'
        '    --tracking-wider:   0.05em;\n'
        '    --tracking-widest:  0.1em;\n'
        '}\n'
        '\n'
        '/* Base styles */\n'
        'body {\n'
        '    font-family: var(--font-sans);\n'
        '    font-size: var(--text-base);\n'
        '    font-weight: var(--weight-normal);\n'
        '    line-height: var(--leading-relaxed);\n'
        '    color: #1a1a2e;\n'
        '    -webkit-font-smoothing: antialiased;\n'
        '    -moz-osx-font-smoothing: grayscale;\n'
        '    text-rendering: optimizeLegibility;\n'
        '}\n'
        '\n'
        '/* Heading styles */\n'
        'h1, h2, h3, h4, h5, h6 {\n'
        '    font-weight: var(--weight-bold);\n'
        '    line-height: var(--leading-tight);\n'
        '    letter-spacing: var(--tracking-tight);\n'
        '    margin-top: 0;\n'
        '}\n'
        '\n'
        'h1 { font-size: var(--text-2xl); }\n'
        'h2 { font-size: var(--text-xl); }\n'
        'h3 { font-size: var(--text-lg); }\n'
        'h4 { font-size: var(--text-md); }\n'
        '\n'
        '/* Code */\n'
        'code, pre, kbd, samp {\n'
        '    font-family: var(--font-mono);\n'
        '    font-size: 0.875em;         /* slightly smaller than surrounding text */\n'
        '    font-feature-settings: "liga" 1, "calt" 1;  /* ligatures for code */\n'
        '}\n'
        '\n'
        '/* Stock ticker — monospace, uppercase, tight tracking */\n'
        '.ticker {\n'
        '    font-family: var(--font-mono);\n'
        '    font-size: var(--text-sm);\n'
        '    font-weight: var(--weight-bold);\n'
        '    letter-spacing: var(--tracking-widest);\n'
        '    text-transform: uppercase;\n'
        '    color: #888;\n'
        '}\n'
        '\n'
        '/* Price — large, bold, tabular numbers */\n'
        '.price {\n'
        '    font-size: var(--text-xl);\n'
        '    font-weight: var(--weight-black);\n'
        '    font-variant-numeric: tabular-nums;  /* fixed-width digits — critical for prices! */\n'
        '    letter-spacing: var(--tracking-tight);\n'
        '    line-height: 1;\n'
        '}',
        filename='typography-system.css',
        styles=styles
    ))
    s.append(principal_box(
        "font-variant-numeric: tabular-nums is one of the most overlooked CSS properties in "
        "financial applications. By default, fonts use proportional digits where '1' is "
        "narrower than '8'. When prices update in real time, proportional digits cause the "
        "entire number to jitter as different-width digits swap in. Tabular numerals give "
        "every digit the same width — prices update smoothly and columns of numbers align "
        "perfectly. Always use tabular-nums for any financial data display.",
        styles
    ))
    return s


# ============================================================================
# SECTION 3.10 — Colors and Visual Design
# ============================================================================

def section_3_10(styles):
    s = []
    s.append(h1("3.10 Colors and Visual Design", styles))
    s.append(p(
        "Color is one of the most powerful tools in visual design — and one of the most "
        "mishandled in CSS. This section covers every color format in CSS, how to build "
        "a systematic color design token system, and the visual effects that make interfaces "
        "feel professional.",
        styles
    ))
    s.append(h2("CSS Color Formats", styles))
    s.append(code_block(
        '/* =====================================\n'
        '   HEX — most common, easy to copy from design tools\n'
        '   ===================================== */\n'
        '.element {\n'
        '    color: #e94560;         /* 6-digit hex: #RRGGBB */\n'
        '    color: #e945608c;       /* 8-digit hex with alpha: #RRGGBBAA */\n'
        '    color: #fff;            /* 3-digit shorthand for #ffffff */\n'
        '    color: #fff8;           /* 4-digit with alpha */\n'
        '}\n'
        '\n'
        '/* =====================================\n'
        '   RGB / RGBA — good for dynamic transparency\n'
        '   ===================================== */\n'
        '.element {\n'
        '    color: rgb(233, 69, 96);              /* R G B (0-255 each) */\n'
        '    color: rgba(233, 69, 96, 0.5);        /* with 50% transparency */\n'
        '    /* Modern syntax — space-separated, / for alpha */\n'
        '    color: rgb(233 69 96 / 50%);          /* same as above */\n'
        '    background: rgb(0 0 0 / 0.6);         /* semi-transparent overlay */\n'
        '}\n'
        '\n'
        '/* =====================================\n'
        '   HSL / HSLA — intuitive for color theory\n'
        '   H = Hue (0-360 degrees on color wheel)\n'
        '   S = Saturation (0% = grey, 100% = vivid)\n'
        '   L = Lightness (0% = black, 50% = full, 100% = white)\n'
        '   ===================================== */\n'
        '.element {\n'
        '    color: hsl(348, 79%, 59%);            /* the TradeBoard red */\n'
        '    color: hsla(348, 79%, 59%, 0.8);      /* 80% opaque */\n'
        '    /* HSL shines for theming — easy to create tints and shades */\n'
        '    --brand-h: 348;\n'
        '    --brand-s: 79%;\n'
        '    color: hsl(var(--brand-h), var(--brand-s), 59%);  /* base */\n'
        '    color: hsl(var(--brand-h), var(--brand-s), 75%);  /* lighter tint */\n'
        '    color: hsl(var(--brand-h), var(--brand-s), 40%);  /* darker shade */\n'
        '}\n'
        '\n'
        '/* =====================================\n'
        '   OKLCH — the modern perceptual color space (CSS Color 4)\n'
        '   L = Lightness (0-1, perceptually uniform)\n'
        '   C = Chroma (colorfulness, 0 = grey)\n'
        '   H = Hue (0-360 degrees)\n'
        '   ===================================== */\n'
        '.element {\n'
        '    /* Supported in all modern browsers */\n'
        '    color: oklch(0.65 0.22 16);           /* TradeBoard red in oklch */\n'
        '    color: oklch(0.65 0.22 16 / 80%);     /* with alpha */\n'
        '    /* OKLCH advantage: equal lightness means colors look equally bright */\n'
        '    /* Critical for accessible color palettes and dark mode */\n'
        '}',
        filename='color-formats.css',
        styles=styles
    ))
    s.append(h2("CSS Custom Properties — Design Tokens", styles))
    s.append(analogy_box(
        "CSS custom properties are like paint swatches at a hardware store. Instead of "
        "describing your color as 'that kind of crimson-ish red with some orange in it,' "
        "you give it a name: 'Firehouse Red.' Now every painter on the project knows exactly "
        "what color to use when they see 'Firehouse Red' in the instructions. If the client "
        "changes their mind and wants a slightly different red, you change the swatch "
        "definition once, and every room painted 'Firehouse Red' updates automatically.",
        styles
    ))
    s.append(code_block(
        '/* CSS Custom Properties (CSS Variables) */\n'
        '\n'
        '/* Declaration — on the :root to make globally available */\n'
        ':root {\n'
        '    --color-brand-500: #e94560;\n'
        '    --color-brand-400: #ed6b82;\n'
        '    --color-brand-600: #c73854;\n'
        '}\n'
        '\n'
        '/* Usage — var(--property-name, fallback) */\n'
        '.btn-primary {\n'
        '    background: var(--color-brand-500);\n'
        '    border-color: var(--color-brand-600);\n'
        '    color: white;\n'
        '}\n'
        '\n'
        '.btn-primary:hover {\n'
        '    background: var(--color-brand-600);\n'
        '}\n'
        '\n'
        '/* Custom properties can be scoped to components */\n'
        '.stock-card {\n'
        '    --card-accent: var(--color-brand-500);  /* default accent */\n'
        '    border-top: 3px solid var(--card-accent);\n'
        '}\n'
        '\n'
        '.stock-card.positive {\n'
        '    --card-accent: #22c55e;  /* override just for positive cards */\n'
        '}\n'
        '\n'
        '.stock-card.negative {\n'
        '    --card-accent: #ef4444;\n'
        '}\n'
        '\n'
        '/* Custom properties in JavaScript */\n'
        '/* const root = document.documentElement;\n'
        '   root.style.setProperty("--color-brand-500", "#ff6b35"); */',
        filename='custom-properties.css',
        styles=styles
    ))
    s.append(h2("Complete Design Token System for TradeBoard", styles))
    s.append(code_block(
        '/* tokens.css — the single source of truth for all design decisions */\n'
        '\n'
        ':root {\n'
        '    /* ============ Colors ============ */\n'
        '\n'
        '    /* Neutrals */\n'
        '    --neutral-50:  #f8fafc;\n'
        '    --neutral-100: #f1f5f9;\n'
        '    --neutral-200: #e2e8f0;\n'
        '    --neutral-300: #cbd5e1;\n'
        '    --neutral-400: #94a3b8;\n'
        '    --neutral-500: #64748b;\n'
        '    --neutral-600: #475569;\n'
        '    --neutral-700: #334155;\n'
        '    --neutral-800: #1e293b;\n'
        '    --neutral-900: #0f172a;\n'
        '\n'
        '    /* Brand (red) */\n'
        '    --brand-300: #f9a8b9;\n'
        '    --brand-400: #ed6b82;\n'
        '    --brand-500: #e94560;  /* primary */\n'
        '    --brand-600: #c73854;\n'
        '    --brand-700: #a42d43;\n'
        '\n'
        '    /* Semantic: positive (green) */\n'
        '    --positive-light: #dcfce7;\n'
        '    --positive:       #22c55e;\n'
        '    --positive-dark:  #16a34a;\n'
        '\n'
        '    /* Semantic: negative (red) */\n'
        '    --negative-light: #fee2e2;\n'
        '    --negative:       #ef4444;\n'
        '    --negative-dark:  #dc2626;\n'
        '\n'
        '    /* Semantic: neutral/unchanged */\n'
        '    --unchanged:      #94a3b8;\n'
        '\n'
        '    /* Surface colors */\n'
        '    --surface-page:      #f8fafc;\n'
        '    --surface-card:      #ffffff;\n'
        '    --surface-elevated:  #ffffff;\n'
        '    --surface-overlay:   rgba(0, 0, 0, 0.5);\n'
        '\n'
        '    /* Text colors */\n'
        '    --text-primary:   #0f172a;\n'
        '    --text-secondary: #475569;\n'
        '    --text-muted:     #94a3b8;\n'
        '    --text-on-dark:   #f8fafc;\n'
        '    --text-link:      #2563eb;\n'
        '\n'
        '    /* Border */\n'
        '    --border-subtle:  #f1f5f9;\n'
        '    --border-default: #e2e8f0;\n'
        '    --border-strong:  #cbd5e1;\n'
        '\n'
        '    /* ============ Shadows ============ */\n'
        '    --shadow-sm:  0 1px 2px rgba(0,0,0,0.05);\n'
        '    --shadow-md:  0 4px 6px rgba(0,0,0,0.07), 0 1px 3px rgba(0,0,0,0.06);\n'
        '    --shadow-lg:  0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05);\n'
        '    --shadow-xl:  0 20px 25px rgba(0,0,0,0.1), 0 8px 10px rgba(0,0,0,0.04);\n'
        '\n'
        '    /* ============ Radii ============ */\n'
        '    --radius-sm: 4px;\n'
        '    --radius-md: 8px;\n'
        '    --radius-lg: 12px;\n'
        '    --radius-xl: 16px;\n'
        '    --radius-full: 9999px;\n'
        '\n'
        '    /* ============ Spacing ============ */\n'
        '    --space-1:  0.25rem;   /*  4px */\n'
        '    --space-2:  0.5rem;    /*  8px */\n'
        '    --space-3:  0.75rem;   /* 12px */\n'
        '    --space-4:  1rem;      /* 16px */\n'
        '    --space-6:  1.5rem;    /* 24px */\n'
        '    --space-8:  2rem;      /* 32px */\n'
        '    --space-12: 3rem;      /* 48px */\n'
        '    --space-16: 4rem;      /* 64px */\n'
        '\n'
        '    /* ============ Z-Index Scale ============ */\n'
        '    --z-below:    -1;\n'
        '    --z-base:      0;\n'
        '    --z-dropdown: 10;\n'
        '    --z-sticky:   20;\n'
        '    --z-fixed:    30;\n'
        '    --z-overlay:  40;\n'
        '    --z-modal:    50;\n'
        '    --z-toast:    60;\n'
        '    --z-tooltip:  70;\n'
        '}\n'
        '\n'
        '/* Dark mode tokens */\n'
        '@media (prefers-color-scheme: dark) {\n'
        '    :root {\n'
        '        --surface-page:      #0f172a;\n'
        '        --surface-card:      #1e293b;\n'
        '        --surface-elevated:  #334155;\n'
        '        --text-primary:      #f8fafc;\n'
        '        --text-secondary:    #cbd5e1;\n'
        '        --text-muted:        #64748b;\n'
        '        --border-default:    #334155;\n'
        '        --border-strong:     #475569;\n'
        '    }\n'
        '}',
        filename='tokens.css',
        styles=styles
    ))
    s.append(h2("Gradients, Shadows, and Filters", styles))
    s.append(code_block(
        '/* ===== GRADIENTS ===== */\n'
        '\n'
        '/* Linear gradient */\n'
        '.hero {\n'
        '    background: linear-gradient(\n'
        '        135deg,              /* angle */\n'
        '        #1a1a2e 0%,          /* start color */\n'
        '        #16213e 50%,\n'
        '        #0f3460 100%         /* end color */\n'
        '    );\n'
        '}\n'
        '\n'
        '/* Radial gradient — circle from center */\n'
        '.glow-effect {\n'
        '    background: radial-gradient(\n'
        '        circle at center,\n'
        '        rgba(233, 69, 96, 0.15) 0%,\n'
        '        transparent 70%\n'
        '    );\n'
        '}\n'
        '\n'
        '/* Conic gradient — for pie/donut charts */\n'
        '.pie-chart {\n'
        '    background: conic-gradient(\n'
        '        #22c55e 0deg 180deg,    /* 50% green */\n'
        '        #ef4444 180deg 270deg,  /* 25% red */\n'
        '        #94a3b8 270deg 360deg   /* 25% grey */\n'
        '    );\n'
        '    border-radius: 50%;\n'
        '    width: 200px;\n'
        '    height: 200px;\n'
        '}\n'
        '\n'
        '/* ===== SHADOWS ===== */\n'
        '\n'
        '/* box-shadow: offset-x offset-y blur spread color */\n'
        '.card {\n'
        '    /* Simple drop shadow */\n'
        '    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);\n'
        '\n'
        '    /* Layered shadows for depth (more realistic) */\n'
        '    box-shadow:\n'
        '        0 1px 2px rgba(0,0,0,0.04),\n'
        '        0 4px 8px rgba(0,0,0,0.06),\n'
        '        0 12px 24px rgba(0,0,0,0.06);\n'
        '\n'
        '    /* Inset shadow (pressed/sunken effect) */\n'
        '    box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);\n'
        '\n'
        '    /* Colored glow for positive cards */\n'
        '    box-shadow: 0 4px 20px rgba(34, 197, 94, 0.2);\n'
        '}\n'
        '\n'
        '/* text-shadow: offset-x offset-y blur color */\n'
        '.hero-title {\n'
        '    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);\n'
        '}\n'
        '\n'
        '/* ===== FILTERS ===== */\n'
        '\n'
        '.loading-card {\n'
        '    filter: blur(2px);              /* Gaussian blur */\n'
        '    filter: brightness(1.2);        /* 120% brightness */\n'
        '    filter: contrast(1.5);          /* 150% contrast */\n'
        '    filter: grayscale(100%);        /* black and white */\n'
        '    filter: opacity(0.5);           /* 50% transparent */\n'
        '    filter: saturate(200%);         /* double saturation */\n'
        '    filter: sepia(80%);             /* vintage effect */\n'
        '    /* Combine filters */\n'
        '    filter: brightness(0.8) contrast(1.2) saturate(1.3);\n'
        '}\n'
        '\n'
        '/* backdrop-filter — applies filter to content BEHIND the element */\n'
        '.glass-panel {\n'
        '    background: rgba(255, 255, 255, 0.15);\n'
        '    backdrop-filter: blur(12px) saturate(180%);\n'
        '    -webkit-backdrop-filter: blur(12px) saturate(180%);\n'
        '    border: 1px solid rgba(255, 255, 255, 0.25);\n'
        '    border-radius: 12px;\n'
        '    /* Creates the frosted glass effect popular in financial UIs */\n'
        '}',
        filename='gradients-shadows-filters.css',
        styles=styles
    ))
    return s


# ============================================================================
# SECTION 3.11 — Transitions and Animations
# ============================================================================

def section_3_11(styles):
    s = []
    s.append(h1("3.11 Transitions and Animations", styles))
    s.append(p(
        "Movement and animation are fundamental to modern UI design. When done correctly, "
        "they communicate state changes, guide attention, and create a sense of polish. "
        "When done incorrectly, they cause motion sickness, frustrate users, and tank "
        "performance. CSS provides two mechanisms: transitions for simple A-to-B changes, "
        "and animations for complex multi-step sequences.",
        styles
    ))
    s.append(analogy_box(
        "A transition is a dimmer switch. When you flip a regular light switch, the room "
        "snaps from dark to light. When you use a dimmer, it smoothly fades. CSS transitions "
        "turn property changes into smooth fades. An animation is a choreographed dance — it "
        "has multiple positions, multiple steps, and can loop, reverse, and run on its own "
        "schedule without any user interaction required.",
        styles
    ))
    s.append(h2("The transition Property", styles))
    s.append(code_block(
        '/* transition: property duration timing-function delay */\n'
        '\n'
        '.btn {\n'
        '    background: #e94560;\n'
        '    color: white;\n'
        '    padding: 0.6rem 1.5rem;\n'
        '    border: none;\n'
        '    border-radius: 6px;\n'
        '    cursor: pointer;\n'
        '\n'
        '    /* Transition one property */\n'
        '    transition: background-color 0.2s ease;\n'
        '\n'
        '    /* Transition multiple properties */\n'
        '    transition:\n'
        '        background-color 0.2s ease,\n'
        '        transform        0.15s ease,\n'
        '        box-shadow       0.2s ease;\n'
        '\n'
        '    /* Shorthand for ALL properties (expensive! avoid in production) */\n'
        '    /* transition: all 0.2s ease; */\n'
        '}\n'
        '\n'
        '.btn:hover {\n'
        '    background: #c73854;\n'
        '    transform: translateY(-2px);\n'
        '    box-shadow: 0 4px 12px rgba(233, 69, 96, 0.4);\n'
        '}\n'
        '\n'
        '.btn:active {\n'
        '    transform: translateY(0);\n'
        '    box-shadow: none;\n'
        '}\n'
        '\n'
        '/* Timing functions */\n'
        '/* ease       — slow start, fast middle, slow end (default) */\n'
        '/* linear     — constant speed */\n'
        '/* ease-in    — slow start, fast end (acceleration) */\n'
        '/* ease-out   — fast start, slow end (deceleration) — most natural for exits */\n'
        '/* ease-in-out — slow start and end */\n'
        '/* cubic-bezier(x1,y1,x2,y2) — custom curve */\n'
        '\n'
        '/* Natural feeling transitions */\n'
        '.enter { transition: opacity 0.3s ease-out, transform 0.3s ease-out; }\n'
        '.exit  { transition: opacity 0.2s ease-in,  transform 0.2s ease-in; }',
        filename='transitions.css',
        styles=styles
    ))
    s.append(h2("@keyframes Animations", styles))
    s.append(code_block(
        '/* Define the animation with @keyframes */\n'
        '@keyframes fadeInUp {\n'
        '    from {\n'
        '        opacity: 0;\n'
        '        transform: translateY(16px);\n'
        '    }\n'
        '    to {\n'
        '        opacity: 1;\n'
        '        transform: translateY(0);\n'
        '    }\n'
        '}\n'
        '\n'
        '/* Multi-step animation with percentages */\n'
        '@keyframes pricePulse {\n'
        '    0%   { background-color: transparent; }\n'
        '    20%  { background-color: rgba(34, 197, 94, 0.3); }   /* flash green */\n'
        '    100% { background-color: transparent; }\n'
        '}\n'
        '\n'
        '@keyframes priceDropPulse {\n'
        '    0%   { background-color: transparent; }\n'
        '    20%  { background-color: rgba(239, 68, 68, 0.3); }   /* flash red */\n'
        '    100% { background-color: transparent; }\n'
        '}\n'
        '\n'
        '/* Spinner */\n'
        '@keyframes spin {\n'
        '    from { transform: rotate(0deg); }\n'
        '    to   { transform: rotate(360deg); }\n'
        '}\n'
        '\n'
        '/* Skeleton shimmer */\n'
        '@keyframes shimmer {\n'
        '    0%   { background-position: -400px 0; }\n'
        '    100% { background-position: 400px 0; }\n'
        '}\n'
        '\n'
        '/* Apply animations */\n'
        '\n'
        '/* animation: name duration timing-function delay iteration-count direction fill-mode */\n'
        '\n'
        '.stock-card {\n'
        '    animation: fadeInUp 0.4s ease-out both;\n'
        '    /* "both" = apply from/to values before/after animation runs */\n'
        '}\n'
        '\n'
        '/* Stagger card animations with delay */\n'
        '.stock-card:nth-child(1) { animation-delay: 0ms; }\n'
        '.stock-card:nth-child(2) { animation-delay: 80ms; }\n'
        '.stock-card:nth-child(3) { animation-delay: 160ms; }\n'
        '.stock-card:nth-child(4) { animation-delay: 240ms; }\n'
        '\n'
        '.price-updated-up {\n'
        '    animation: pricePulse 1s ease-out;\n'
        '}\n'
        '\n'
        '.price-updated-down {\n'
        '    animation: priceDropPulse 1s ease-out;\n'
        '}\n'
        '\n'
        '.spinner {\n'
        '    animation: spin 0.8s linear infinite;\n'
        '    width: 1.25rem;\n'
        '    height: 1.25rem;\n'
        '    border: 2px solid rgba(233, 69, 96, 0.2);\n'
        '    border-top-color: #e94560;\n'
        '    border-radius: 50%;\n'
        '}',
        filename='keyframe-animations.css',
        styles=styles
    ))
    s.append(h2("The transform Property", styles))
    s.append(code_block(
        '/* transform functions — these run on the GPU, never cause layout */\n'
        '\n'
        '/* translate — move without affecting layout */\n'
        '.tooltip {\n'
        '    transform: translateX(-50%);          /* center horizontally */\n'
        '    transform: translateY(-100%);         /* move above element */\n'
        '    transform: translate(-50%, -100%);    /* both axes */\n'
        '    transform: translate3d(-50%, 0, 0);   /* force GPU layer */\n'
        '}\n'
        '\n'
        '/* rotate */\n'
        '.icon-arrow {\n'
        '    transform: rotate(45deg);\n'
        '    transform: rotate(-90deg);\n'
        '}\n'
        '\n'
        '/* scale — grow or shrink */\n'
        '.card:hover {\n'
        '    transform: scale(1.02);               /* grow 2% */\n'
        '    transform: scale(0.95);               /* shrink 5% */\n'
        '    transform: scaleX(1.1);               /* only horizontal */\n'
        '}\n'
        '\n'
        '/* skew — tilt/shear */\n'
        '.decorative-bg {\n'
        '    transform: skewY(-6deg);              /* diagonal slice effect */\n'
        '}\n'
        '\n'
        '/* Combining transforms — ORDER MATTERS! */\n'
        '.combo {\n'
        '    /* Translate first, THEN rotate */\n'
        '    transform: translateX(100px) rotate(45deg);\n'
        '    /* vs. rotate first, THEN translate (very different result!) */\n'
        '    transform: rotate(45deg) translateX(100px);\n'
        '}\n'
        '\n'
        '/* Transform origin — the pivot point */\n'
        '.dropdown-icon {\n'
        '    transform-origin: center center;      /* default */\n'
        '    transform-origin: top left;\n'
        '    transform-origin: 50% 100%;           /* bottom center */\n'
        '    transition: transform 0.2s ease;\n'
        '}\n'
        '\n'
        '.dropdown-icon.open {\n'
        '    transform: rotate(180deg);\n'
        '}',
        filename='transforms.css',
        styles=styles
    ))
    s.append(h2("Performance — Only Animate transform and opacity", styles))
    s.append(p(
        "This is one of the most important CSS performance rules. Animating the wrong "
        "properties triggers expensive browser repaints or even full layout recalculations "
        "on every frame (60 times per second), making animations janky and draining the "
        "device battery.",
        styles
    ))
    s.append(bullet("<b>SAFE to animate (GPU composite):</b> transform, opacity — no layout or paint triggered", styles))
    s.append(bullet("<b>EXPENSIVE (triggers repaint):</b> color, background-color, border-color, box-shadow — only paint, no layout", styles))
    s.append(bullet("<b>VERY EXPENSIVE (triggers layout):</b> width, height, margin, padding, font-size, top/left/right/bottom — avoid in animations", styles))
    s.append(code_block(
        '/* WRONG — animating top/left causes layout recalc 60fps */\n'
        '@keyframes bad-slide {\n'
        '    from { left: -300px; }\n'
        '    to   { left: 0; }\n'
        '}\n'
        '\n'
        '/* CORRECT — animating transform runs on GPU */\n'
        '@keyframes good-slide {\n'
        '    from { transform: translateX(-300px); }\n'
        '    to   { transform: translateX(0); }\n'
        '}\n'
        '\n'
        '/* WRONG — animating width causes layout */\n'
        '.bad-expand:hover { width: 200px; }\n'
        '\n'
        '/* CORRECT — use transform: scaleX() instead */\n'
        '.good-expand:hover { transform: scaleX(1.2); }\n'
        '\n'
        '/* will-change — hint to browser to promote to GPU layer */\n'
        '/* Use sparingly — each layer consumes GPU memory */\n'
        '.animated-card {\n'
        '    will-change: transform, opacity;\n'
        '    /* Remove after animation: */\n'
        '    /* element.style.willChange = "auto"; */\n'
        '}\n'
        '\n'
        '/* prefers-reduced-motion — critical for accessibility */\n'
        '@media (prefers-reduced-motion: reduce) {\n'
        '    *,\n'
        '    *::before,\n'
        '    *::after {\n'
        '        animation-duration: 0.01ms !important;\n'
        '        animation-iteration-count: 1 !important;\n'
        '        transition-duration: 0.01ms !important;\n'
        '        scroll-behavior: auto !important;\n'
        '    }\n'
        '}\n'
        '/* Some users experience motion sickness from animations.\n'
        '   Respecting this media query is both ethical and often required by law. */',
        filename='animation-performance.css',
        styles=styles
    ))
    s.append(h2("Complete Animated Stock Card Example", styles))
    s.append(code_block(
        '/* Animated stock price card — production quality */\n'
        '\n'
        '/* Keyframes */\n'
        '@keyframes cardEnter {\n'
        '    from {\n'
        '        opacity: 0;\n'
        '        transform: translateY(12px) scale(0.98);\n'
        '    }\n'
        '    to {\n'
        '        opacity: 1;\n'
        '        transform: translateY(0) scale(1);\n'
        '    }\n'
        '}\n'
        '\n'
        '@keyframes priceUp {\n'
        '    0%   { color: inherit; background: transparent; }\n'
        '    15%  { color: #16a34a; background: rgba(34,197,94,0.12); }\n'
        '    85%  { color: #16a34a; background: rgba(34,197,94,0.06); }\n'
        '    100% { color: inherit; background: transparent; }\n'
        '}\n'
        '\n'
        '@keyframes priceDown {\n'
        '    0%   { color: inherit; background: transparent; }\n'
        '    15%  { color: #dc2626; background: rgba(239,68,68,0.12); }\n'
        '    85%  { color: #dc2626; background: rgba(239,68,68,0.06); }\n'
        '    100% { color: inherit; background: transparent; }\n'
        '}\n'
        '\n'
        '/* Card component */\n'
        '.stock-card {\n'
        '    background: white;\n'
        '    border-radius: 12px;\n'
        '    border: 1px solid #e2e8f0;\n'
        '    padding: 1.25rem 1.5rem;\n'
        '    cursor: pointer;\n'
        '    position: relative;\n'
        '    overflow: hidden;\n'
        '\n'
        '    /* Entry animation */\n'
        '    animation: cardEnter 0.4s ease-out both;\n'
        '\n'
        '    /* Hover transitions */\n'
        '    transition:\n'
        '        border-color 0.2s ease,\n'
        '        box-shadow   0.2s ease,\n'
        '        transform    0.2s ease;\n'
        '}\n'
        '\n'
        '.stock-card:hover {\n'
        '    border-color: #cbd5e1;\n'
        '    box-shadow:\n'
        '        0 4px 8px rgba(0,0,0,0.06),\n'
        '        0 12px 24px rgba(0,0,0,0.06);\n'
        '    transform: translateY(-2px);\n'
        '}\n'
        '\n'
        '.stock-card:active {\n'
        '    transform: translateY(0);\n'
        '    box-shadow: none;\n'
        '}\n'
        '\n'
        '/* Focus visible (keyboard navigation) */\n'
        '.stock-card:focus-visible {\n'
        '    outline: 2px solid #e94560;\n'
        '    outline-offset: 2px;\n'
        '}\n'
        '\n'
        '/* Price update flash */\n'
        '.stock-card__price {\n'
        '    font-size: 1.75rem;\n'
        '    font-weight: 800;\n'
        '    font-variant-numeric: tabular-nums;\n'
        '    line-height: 1;\n'
        '    border-radius: 4px;\n'
        '    padding: 0.1rem 0.25rem;\n'
        '    transition: color 0.3s;\n'
        '}\n'
        '\n'
        '.stock-card__price.flash-up {\n'
        '    animation: priceUp 1.2s ease-out both;\n'
        '}\n'
        '\n'
        '.stock-card__price.flash-down {\n'
        '    animation: priceDown 1.2s ease-out both;\n'
        '}\n'
        '\n'
        '/* Subtle left border accent */\n'
        '.stock-card::before {\n'
        '    content: "";\n'
        '    position: absolute;\n'
        '    left: 0;\n'
        '    top: 0;\n'
        '    bottom: 0;\n'
        '    width: 3px;\n'
        '    background: var(--card-accent, #e2e8f0);\n'
        '    border-radius: 12px 0 0 12px;\n'
        '    transition: background 0.3s;\n'
        '}\n'
        '\n'
        '.stock-card.positive { --card-accent: #22c55e; }\n'
        '.stock-card.negative { --card-accent: #ef4444; }\n'
        '\n'
        '/* Respect motion preferences */\n'
        '@media (prefers-reduced-motion: reduce) {\n'
        '    .stock-card,\n'
        '    .stock-card__price {\n'
        '        animation: none;\n'
        '        transition: none;\n'
        '    }\n'
        '}',
        filename='animated-stock-card.css',
        styles=styles
    ))
    return s


# ============================================================================
# SECTION 3.12 — Modern CSS Features (2024-2026)
# ============================================================================

def section_3_12(styles):
    s = []
    s.append(h1("3.12 Modern CSS Features (2024-2026)", styles))
    s.append(p(
        "CSS has evolved dramatically in recent years. Features that required JavaScript "
        "preprocessors or workarounds are now native. Understanding these modern features "
        "separates developers who write CSS from developers who architect CSS.",
        styles
    ))
    s.append(h2("CSS Nesting (Native)", styles))
    s.append(p(
        "Native CSS nesting lets you write child rules inside their parent selector — just "
        "like SCSS, but built into the browser. No preprocessor needed:",
        styles
    ))
    s.append(code_block(
        '/* Native CSS Nesting — supported in all modern browsers (2023+) */\n'
        '\n'
        '.stock-card {\n'
        '    background: white;\n'
        '    border-radius: 12px;\n'
        '    padding: 1.5rem;\n'
        '    border: 1px solid #e2e8f0;\n'
        '    transition: box-shadow 0.2s;\n'
        '\n'
        '    /* Nested selector — equivalent to .stock-card:hover */\n'
        '    &:hover {\n'
        '        box-shadow: 0 8px 24px rgba(0,0,0,0.1);\n'
        '    }\n'
        '\n'
        '    /* Nested child — equivalent to .stock-card .stock-card__title */\n'
        '    .stock-card__title {\n'
        '        font-size: 0.75rem;\n'
        '        font-weight: 700;\n'
        '        text-transform: uppercase;\n'
        '        letter-spacing: 0.08em;\n'
        '        color: #64748b;\n'
        '        margin: 0 0 0.25rem;\n'
        '    }\n'
        '\n'
        '    /* Nested with & combinator */\n'
        '    & + & {\n'
        '        margin-top: 0;  /* adjacent card cards */\n'
        '    }\n'
        '\n'
        '    /* Nested media query */\n'
        '    @media (max-width: 640px) {\n'
        '        padding: 1rem;\n'
        '    }\n'
        '\n'
        '    /* Modifier classes with nesting */\n'
        '    &.positive {\n'
        '        --card-accent: #22c55e;\n'
        '        border-left: 3px solid var(--card-accent);\n'
        '    }\n'
        '\n'
        '    &.negative {\n'
        '        --card-accent: #ef4444;\n'
        '        border-left: 3px solid var(--card-accent);\n'
        '    }\n'
        '}',
        filename='css-nesting.css',
        styles=styles
    ))
    s.append(h2("The :has() Selector", styles))
    s.append(p(
        "The :has() pseudo-class is sometimes called the 'parent selector' CSS never had. "
        "It selects an element based on whether it contains (or is followed by) a specified "
        "descendant or sibling. It enables conditional styling that previously required "
        "JavaScript:",
        styles
    ))
    s.append(code_block(
        '/* :has() — supported in all modern browsers (2023+) */\n'
        '\n'
        '/* Style a card that CONTAINS an image */\n'
        '.stock-card:has(img) {\n'
        '    padding-top: 0;\n'
        '}  /* no image = normal padding, has image = no top padding */\n'
        '\n'
        '/* Style a form group that contains a focused input */\n'
        '.form-group:has(input:focus) {\n'
        '    background: #f0f7ff;\n'
        '    border-color: #2563eb;\n'
        '}\n'
        '\n'
        '/* Style a form group that contains an invalid input */\n'
        '.form-group:has(input:invalid:not(:placeholder-shown)) {\n'
        '    --field-color: #ef4444;\n'
        '    color: var(--field-color);\n'
        '}\n'
        '\n'
        '.form-group:has(input:invalid:not(:placeholder-shown)) label {\n'
        '    color: #ef4444;\n'
        '}\n'
        '\n'
        '/* Navigation: style the parent li when the link is active */\n'
        '.nav-item:has(a[aria-current="page"]) {\n'
        '    background: rgba(255,255,255,0.1);\n'
        '    border-radius: 6px;\n'
        '}\n'
        '\n'
        '/* Dashboard: detect empty state */\n'
        '.watchlist:has(.watchlist-item:nth-child(5)) .show-more-btn {\n'
        '    display: block;  /* show "View more" when 5+ items */\n'
        '}\n'
        '\n'
        '/* Sibling selection */\n'
        'h2:has(+ p) {\n'
        '    margin-bottom: 0.5rem;  /* less space when followed by a paragraph */\n'
        '}',
        filename='has-selector.css',
        styles=styles
    ))
    s.append(h2("CSS @layer — Cascade Layers", styles))
    s.append(p(
        "CSS @layer lets you organize your CSS into named layers with a defined priority "
        "order. Layers with later declarations in the @layer statement win. This solves "
        "the nightmare of fighting third-party CSS specificity:",
        styles
    ))
    s.append(code_block(
        '/* Define layer order at the top of your CSS */\n'
        '/* Earlier in the list = lower priority */\n'
        '@layer reset, base, theme, layout, components, utilities, overrides;\n'
        '\n'
        '/* Assign CSS to layers */\n'
        '@layer reset {\n'
        '    *, *::before, *::after { box-sizing: border-box; }\n'
        '    * { margin: 0; padding: 0; }\n'
        '}\n'
        '\n'
        '@layer base {\n'
        '    body {\n'
        '        font-family: system-ui, sans-serif;\n'
        '        line-height: 1.6;\n'
        '    }\n'
        '    a { color: var(--color-link, #2563eb); }\n'
        '}\n'
        '\n'
        '@layer components {\n'
        '    .btn {\n'
        '        display: inline-flex;\n'
        '        align-items: center;\n'
        '        padding: 0.5rem 1.25rem;\n'
        '        border-radius: 6px;\n'
        '        font-weight: 600;\n'
        '        cursor: pointer;\n'
        '    }\n'
        '\n'
        '    .stock-card {\n'
        '        background: white;\n'
        '        border-radius: 12px;\n'
        '        padding: 1.5rem;\n'
        '        border: 1px solid #e2e8f0;\n'
        '    }\n'
        '}\n'
        '\n'
        '@layer utilities {\n'
        '    .hidden    { display: none; }\n'
        '    .sr-only   {\n'
        '        position: absolute;\n'
        '        width: 1px;\n'
        '        height: 1px;\n'
        '        padding: 0;\n'
        '        margin: -1px;\n'
        '        overflow: hidden;\n'
        '        clip: rect(0,0,0,0);\n'
        '        white-space: nowrap;\n'
        '        border: 0;\n'
        '    }\n'
        '    .text-center { text-align: center; }\n'
        '    .flex { display: flex; }\n'
        '    .items-center { align-items: center; }\n'
        '}\n'
        '\n'
        '/* Third-party CSS can be demoted */\n'
        '@layer vendor {\n'
        '    @import url("third-party-widget.css");\n'
        '}  /* Now all your unlayered CSS beats vendor CSS */\n'
        '\n'
        '/* Unlayered CSS (no @layer) always beats layered CSS */\n'
        '.my-override { color: red; }  /* beats everything in any layer */\n',
        filename='cascade-layers.css',
        styles=styles
    ))
    s.append(h2("CSS Subgrid", styles))
    s.append(code_block(
        '/* Subgrid — child grids participate in the parent grid\'s tracks */\n'
        '/* Supported in all modern browsers (2023+) */\n'
        '\n'
        '/* Without subgrid: cards have misaligned internal elements */\n'
        '.card-grid {\n'
        '    display: grid;\n'
        '    grid-template-columns: repeat(3, 1fr);\n'
        '    gap: 1rem;\n'
        '}\n'
        '\n'
        '.card {\n'
        '    /* Without subgrid, each card is its own independent grid */\n'
        '    display: grid;\n'
        '    grid-template-rows: auto 1fr auto;  /* title, content, footer */\n'
        '    /* But different cards have different heights — misaligned! */\n'
        '}\n'
        '\n'
        '/* WITH subgrid: all cards share the parent\'s row tracks */\n'
        '.card-grid {\n'
        '    display: grid;\n'
        '    grid-template-columns: repeat(3, 1fr);\n'
        '    grid-template-rows: repeat(3, auto);  /* 3 rows for title/body/footer */\n'
        '    gap: 1rem;\n'
        '    align-items: start;\n'
        '}\n'
        '\n'
        '/* Each card spans all 3 rows and uses SUBGRID */\n'
        '.card {\n'
        '    grid-row: span 3;           /* span 3 rows */\n'
        '    display: grid;\n'
        '    grid-template-rows: subgrid; /* inherit parent\'s row tracks */\n'
        '    gap: 0;\n'
        '}\n'
        '\n'
        '/* Now card__title always aligns with other cards\' titles */\n'
        '.card__title { grid-row: 1; }\n'
        '.card__body  { grid-row: 2; }\n'
        '.card__footer { grid-row: 3; }',
        filename='subgrid.css',
        styles=styles
    ))
    s.append(h2("Scroll-Driven Animations (Overview)", styles))
    s.append(code_block(
        '/* Scroll-driven animations — link animation progress to scroll position */\n'
        '/* Supported in Chrome 115+, Firefox (behind flag), Safari 18+ */\n'
        '\n'
        '/* Animate based on how far page has scrolled */\n'
        '@keyframes progress {\n'
        '    from { transform: scaleX(0); }\n'
        '    to   { transform: scaleX(1); }\n'
        '}\n'
        '\n'
        '.reading-progress-bar {\n'
        '    position: fixed;\n'
        '    top: 0;\n'
        '    left: 0;\n'
        '    height: 3px;\n'
        '    background: #e94560;\n'
        '    transform-origin: left;\n'
        '    animation: progress linear;\n'
        '    animation-timeline: scroll();    /* tied to root scroll */\n'
        '    animation-fill-mode: both;\n'
        '}\n'
        '\n'
        '/* Animate when element enters/exits view */\n'
        '@keyframes fadeInView {\n'
        '    from { opacity: 0; transform: translateY(30px); }\n'
        '    to   { opacity: 1; transform: translateY(0); }\n'
        '}\n'
        '\n'
        '.animate-on-scroll {\n'
        '    animation: fadeInView linear both;\n'
        '    animation-timeline: view();      /* tied to element visibility */\n'
        '    animation-range: entry 0% entry 40%;  /* trigger window */\n'
        '}',
        filename='scroll-driven.css',
        styles=styles
    ))
    s.append(h2("View Transitions API (Overview)", styles))
    s.append(code_block(
        '/* View Transitions — smooth animated page transitions */\n'
        '/* Supported in Chrome 111+, Safari 18+, Firefox (behind flag) */\n'
        '\n'
        '/* CSS: name elements for coordinated transitions */\n'
        '.stock-card {\n'
        '    view-transition-name: var(--ticker-id);  /* unique per card */\n'
        '}\n'
        '\n'
        '.hero-price {\n'
        '    view-transition-name: hero-price;\n'
        '}\n'
        '\n'
        '/* Customize the transition animation */\n'
        '::view-transition-old(hero-price) {\n'
        '    animation: 0.2s ease-in both fade-out;\n'
        '}\n'
        '\n'
        '::view-transition-new(hero-price) {\n'
        '    animation: 0.3s ease-out 0.1s both fade-in;\n'
        '}\n'
        '\n'
        '/* JavaScript: trigger the transition */\n'
        '/* if (!document.startViewTransition) { updateDOM(); return; }\n'
        '   document.startViewTransition(() => updateDOM()); */',
        filename='view-transitions.css',
        styles=styles
    ))
    return s


# ============================================================================
# SECTION 3.13 — CSS Architecture at Principal Engineer Level
# ============================================================================

def section_3_13(styles):
    s = []
    s.append(h1("3.13 CSS Architecture at Principal Engineer Level", styles))
    s.append(p(
        "Writing CSS that looks right on your laptop is easy. Writing CSS that looks right "
        "for 10 million users, across dozens of features built by 20 different developers "
        "over three years — that is architecture. This section covers the methodologies, "
        "patterns, and performance considerations that separate maintainable CSS systems "
        "from CSS chaos.",
        styles
    ))
    s.append(analogy_box(
        "At the Principal Engineer level, CSS is not 'make it look right.' It is 'make it "
        "look right for 10 million users, with a team of 20 developers, across 500 components, "
        "for the next three years.' Every architectural decision you make in CSS either "
        "compounds into technical debt or compounds into leverage. A thoughtful naming "
        "convention and token system is worth a hundred hotfixes.",
        styles
    ))
    s.append(h2("BEM Methodology", styles))
    s.append(p(
        "BEM (Block, Element, Modifier) is the most widely adopted CSS naming convention. "
        "It solves the specificity problem by ensuring every selector is exactly one class, "
        "making it easy to understand where any CSS rule applies just from reading the class name.",
        styles
    ))
    s.append(bullet("<b>Block:</b> A standalone component — .card, .nav, .btn, .modal", styles))
    s.append(bullet("<b>Element:</b> A part of a block — .card__title, .nav__item, .modal__body (double underscore)", styles))
    s.append(bullet("<b>Modifier:</b> A variant or state — .btn--primary, .card--featured, .nav__item--active (double dash)", styles))
    s.append(code_block(
        '/* BEM Example — TradeBoard Stock Card */\n'
        '\n'
        '/* Block */\n'
        '.stock-card {\n'
        '    background: white;\n'
        '    border-radius: 12px;\n'
        '    border: 1px solid #e2e8f0;\n'
        '    padding: 1.5rem;\n'
        '    position: relative;\n'
        '    overflow: hidden;\n'
        '}\n'
        '\n'
        '/* Elements (parts of the block) */\n'
        '.stock-card__header {\n'
        '    display: flex;\n'
        '    justify-content: space-between;\n'
        '    align-items: flex-start;\n'
        '    margin-bottom: 0.75rem;\n'
        '}\n'
        '\n'
        '.stock-card__ticker {\n'
        '    font-family: var(--font-mono);\n'
        '    font-size: 0.75rem;\n'
        '    font-weight: 700;\n'
        '    letter-spacing: 0.08em;\n'
        '    text-transform: uppercase;\n'
        '    color: #64748b;\n'
        '}\n'
        '\n'
        '.stock-card__name {\n'
        '    font-size: 0.8rem;\n'
        '    color: #94a3b8;\n'
        '    margin-top: 0.1rem;\n'
        '}\n'
        '\n'
        '.stock-card__price {\n'
        '    font-size: 1.75rem;\n'
        '    font-weight: 800;\n'
        '    font-variant-numeric: tabular-nums;\n'
        '    letter-spacing: -0.02em;\n'
        '    line-height: 1;\n'
        '    color: #0f172a;\n'
        '}\n'
        '\n'
        '.stock-card__change {\n'
        '    font-size: 0.8rem;\n'
        '    font-weight: 600;\n'
        '    font-variant-numeric: tabular-nums;\n'
        '    padding: 0.2rem 0.5rem;\n'
        '    border-radius: 100px;\n'
        '    display: inline-flex;\n'
        '    align-items: center;\n'
        '    gap: 0.2rem;\n'
        '}\n'
        '\n'
        '.stock-card__footer {\n'
        '    display: flex;\n'
        '    justify-content: space-between;\n'
        '    align-items: center;\n'
        '    margin-top: 1rem;\n'
        '    padding-top: 0.75rem;\n'
        '    border-top: 1px solid #f1f5f9;\n'
        '}\n'
        '\n'
        '.stock-card__volume {\n'
        '    font-size: 0.75rem;\n'
        '    color: #94a3b8;\n'
        '}\n'
        '\n'
        '.stock-card__sparkline {\n'
        '    height: 40px;\n'
        '    flex-shrink: 0;\n'
        '}\n'
        '\n'
        '/* Block Modifiers (variants) */\n'
        '.stock-card--positive {\n'
        '    border-top: 3px solid #22c55e;\n'
        '}\n'
        '\n'
        '.stock-card--positive .stock-card__change {\n'
        '    background: #dcfce7;\n'
        '    color: #166534;\n'
        '}\n'
        '\n'
        '.stock-card--negative {\n'
        '    border-top: 3px solid #ef4444;\n'
        '}\n'
        '\n'
        '.stock-card--negative .stock-card__change {\n'
        '    background: #fee2e2;\n'
        '    color: #991b1b;\n'
        '}\n'
        '\n'
        '.stock-card--featured {\n'
        '    grid-column: span 2;    /* takes 2 grid columns */\n'
        '    background: linear-gradient(135deg, #1a1a2e, #16213e);\n'
        '    color: white;\n'
        '    border: none;\n'
        '}\n'
        '\n'
        '.stock-card--loading {\n'
        '    pointer-events: none;\n'
        '}\n'
        '\n'
        '/* HTML usage:\n'
        '   <div class="stock-card stock-card--positive">\n'
        '     <div class="stock-card__header">\n'
        '       <div>\n'
        '         <span class="stock-card__ticker">AAPL</span>\n'
        '         <div class="stock-card__name">Apple Inc.</div>\n'
        '       </div>\n'
        '       <span class="stock-card__change">+2.3%</span>\n'
        '     </div>\n'
        '     <div class="stock-card__price">$182.50</div>\n'
        '     <div class="stock-card__footer">\n'
        '       <span class="stock-card__volume">Vol: 54.3M</span>\n'
        '       <svg class="stock-card__sparkline">...</svg>\n'
        '     </div>\n'
        '   </div>\n'
        '*/',
        filename='bem-example.css',
        styles=styles
    ))
    s.append(h2("Utility-First vs Component-First", styles))
    s.append(p(
        "Two main philosophies compete in modern CSS architecture: component-first (BEM, CSS "
        "Modules, Styled Components) and utility-first (Tailwind CSS, UnoCSS). Understanding "
        "both helps you choose the right tool and write better CSS regardless of which you pick.",
        styles
    ))
    s.append(h3("Component-First", styles))
    s.append(code_block(
        '/* Component-first: semantic class names, CSS in a separate file */\n'
        '/* Advantages: readable HTML, reusable components, no CSS in JS/HTML */\n'
        '\n'
        '/* CSS */\n'
        '.price-badge {\n'
        '    display: inline-flex;\n'
        '    align-items: center;\n'
        '    gap: 0.2rem;\n'
        '    padding: 0.25rem 0.6rem;\n'
        '    border-radius: 100px;\n'
        '    font-size: 0.8rem;\n'
        '    font-weight: 600;\n'
        '    font-variant-numeric: tabular-nums;\n'
        '}\n'
        '.price-badge--up   { background: #dcfce7; color: #166534; }\n'
        '.price-badge--down { background: #fee2e2; color: #991b1b; }\n'
        '\n'
        '/* HTML */\n'
        '<!-- <span class="price-badge price-badge--up">+2.3%</span> -->',
        filename='component-first.css',
        styles=styles
    ))
    s.append(h3("Utility-First (Tailwind-style)", styles))
    s.append(code_block(
        '/* Utility-first: compose directly in HTML, tiny single-purpose classes */\n'
        '/* Advantages: no naming, no context switching, no dead CSS */\n'
        '\n'
        '/* Equivalent Tailwind HTML: */\n'
        '<!-- <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full\n'
        '                  text-sm font-semibold tabular-nums\n'
        '                  bg-green-100 text-green-800">\n'
        '  +2.3%\n'
        '</span> -->\n'
        '\n'
        '/* Trade-offs:\n'
        '   Component-first:\n'
        '   + Clean HTML, semantic meaning\n'
        '   + Easy to find all styles for a component\n'
        '   - CSS file can grow large without pruning\n'
        '   - Requires thoughtful naming\n'
        '\n'
        '   Utility-first:\n'
        '   + HTML is the only source of truth\n'
        '   + No naming decisions\n'
        '   + CSS bundle stays small (purged automatically)\n'
        '   - HTML becomes verbose\n'
        '   - Harder to see the "shape" of a design\n'
        '\n'
        '   Principal Engineer view: both are valid at scale.\n'
        '   Use component-first for custom design systems.\n'
        '   Use utility-first (Tailwind) for rapid product development.\n'
        '   Many production apps use both together. */',
        filename='utility-first.css',
        styles=styles
    ))
    s.append(h2("CSS Performance", styles))
    s.append(h3("Unused CSS", styles))
    s.append(p(
        "CSS is render-blocking — the browser cannot display content until it has finished "
        "downloading and parsing all CSS. Sending thousands of lines of unused CSS to mobile "
        "users on 3G connections is a real performance crime.",
        styles
    ))
    s.append(bullet("Use PurgeCSS or Tailwind's built-in purging to remove unused rules in production", styles))
    s.append(bullet("CSS coverage in Chrome DevTools (Ctrl+Shift+P > 'Coverage') shows which CSS is used on a page", styles))
    s.append(bullet("Split CSS by page using code-splitting — don't send homepage CSS to the dashboard page", styles))
    s.append(h3("Reflow and Repaint", styles))
    s.append(code_block(
        '/* CSS that causes REFLOW (layout recalculation) — avoid in animations */\n'
        '/* Changing: width, height, margin, padding, border, font-size, */\n'
        '/* top, left, bottom, right (on positioned elements), display, float */\n'
        '\n'
        '/* CSS that causes REPAINT only (no layout) */\n'
        '/* Changing: color, background-color, box-shadow, border-color, */\n'
        '/* outline, border-radius, visibility */\n'
        '\n'
        '/* CSS that causes COMPOSITE only (GPU, cheapest) */\n'
        '/* Changing: transform, opacity */\n'
        '\n'
        '/* Use DevTools Performance panel to detect jank */\n'
        '/* Look for long frames (>16ms for 60fps) */\n'
        '/* Solid green bars = good. Yellow/red = janky */\n'
        '\n'
        '/* Containment — tell browser a subtree is independent */\n'
        '.stock-card {\n'
        '    contain: content;         /* layout, paint, and style containment */\n'
        '    /* This tells the browser: layout changes inside this element */\n'
        '    /* do not affect anything outside. Enables optimizations. */\n'
        '}\n'
        '\n'
        '/* content-visibility — skip rendering off-screen elements */\n'
        '.below-fold-section {\n'
        '    content-visibility: auto;    /* render only when near viewport */\n'
        '    contain-intrinsic-size: auto 300px;  /* hint for scroll estimation */\n'
        '    /* Can reduce initial render time by 50%+ on long pages */\n'
        '}',
        filename='css-performance.css',
        styles=styles
    ))
    s.append(principal_box(
        "The most impactful CSS performance decisions happen before you write a single line "
        "of CSS. A design system with CSS custom properties and a consistent component API "
        "prevents the proliferation of one-off styles. A CSS layer architecture prevents "
        "specificity wars that lead to !important. A component naming convention prevents "
        "dead code from accumulating. The senior engineer fixes CSS bugs. The principal "
        "engineer builds the system that prevents CSS bugs from happening in the first place.",
        styles
    ))
    return s


# ============================================================================
# EXERCISES
# ============================================================================

def section_exercises(styles):
    s = []
    s.append(page_break())
    s.append(h1("Chapter 3 Exercises", styles))
    s.append(p(
        "Apply everything you have learned. Each exercise builds on the TradeBoard project. "
        "Complete solutions are provided — attempt each exercise before reading the solution.",
        styles
    ))

    # -------------------------------------------------------------------------
    # Exercise 1
    # -------------------------------------------------------------------------
    s.append(exercise(
        1,
        "Style TradeBoard HTML — Colors, Typography, Spacing",
        [
            ("ExerciseBody",
             "Take the HTML structure from Chapter 2's TradeBoard exercises and apply a "
             "complete visual treatment: color palette, typography, spacing, and card styling. "
             "Use an external stylesheet. Apply the box-sizing reset. Use CSS custom properties "
             "for all colors. Create at least 3 stock cards with positive, negative, and neutral states."),
            ("ExerciseBody", "SOLUTION:"),
        ],
        styles=styles
    ))
    s.append(code_block(
        '/* styles/tradeboard.css */\n'
        '\n'
        '/* 1. Global box-sizing reset */\n'
        '*, *::before, *::after { box-sizing: border-box; }\n'
        '\n'
        '/* 2. Design tokens */\n'
        ':root {\n'
        '    --font-sans: system-ui, -apple-system, sans-serif;\n'
        '    --font-mono: "JetBrains Mono", "Fira Code", monospace;\n'
        '    --color-bg:       #f8fafc;\n'
        '    --color-surface:  #ffffff;\n'
        '    --color-primary:  #1a1a2e;\n'
        '    --color-accent:   #e94560;\n'
        '    --color-border:   #e2e8f0;\n'
        '    --color-text:     #0f172a;\n'
        '    --color-muted:    #64748b;\n'
        '    --color-positive: #22c55e;\n'
        '    --color-negative: #ef4444;\n'
        '    --radius-card:    12px;\n'
        '    --shadow-card:    0 1px 3px rgba(0,0,0,0.05), 0 4px 12px rgba(0,0,0,0.05);\n'
        '}\n'
        '\n'
        '/* 3. Base styles */\n'
        'body {\n'
        '    font-family: var(--font-sans);\n'
        '    background: var(--color-bg);\n'
        '    color: var(--color-text);\n'
        '    margin: 0;\n'
        '    line-height: 1.6;\n'
        '    -webkit-font-smoothing: antialiased;\n'
        '}\n'
        '\n'
        '/* 4. Site header */\n'
        '.site-header {\n'
        '    background: var(--color-primary);\n'
        '    padding: 0 2rem;\n'
        '    height: 64px;\n'
        '    display: flex;\n'
        '    align-items: center;\n'
        '    justify-content: space-between;\n'
        '    position: sticky;\n'
        '    top: 0;\n'
        '    z-index: 100;\n'
        '}\n'
        '.logo {\n'
        '    color: #fff;\n'
        '    font-size: 1.25rem;\n'
        '    font-weight: 800;\n'
        '    letter-spacing: -0.03em;\n'
        '    text-decoration: none;\n'
        '}\n'
        '.logo span { color: var(--color-accent); }\n'
        '\n'
        '/* 5. Dashboard layout */\n'
        '.dashboard {\n'
        '    max-width: 1200px;\n'
        '    margin: 2rem auto;\n'
        '    padding: 0 2rem;\n'
        '}\n'
        '\n'
        '/* 6. Card grid */\n'
        '.card-grid {\n'
        '    display: grid;\n'
        '    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));\n'
        '    gap: 1.25rem;\n'
        '    margin-top: 1.5rem;\n'
        '}\n'
        '\n'
        '/* 7. Stock card */\n'
        '.stock-card {\n'
        '    background: var(--color-surface);\n'
        '    border: 1px solid var(--color-border);\n'
        '    border-radius: var(--radius-card);\n'
        '    padding: 1.25rem 1.5rem;\n'
        '    box-shadow: var(--shadow-card);\n'
        '    border-top: 3px solid var(--card-accent, var(--color-border));\n'
        '    transition: box-shadow 0.2s, transform 0.2s;\n'
        '    cursor: pointer;\n'
        '}\n'
        '.stock-card:hover {\n'
        '    box-shadow: 0 8px 24px rgba(0,0,0,0.1);\n'
        '    transform: translateY(-2px);\n'
        '}\n'
        '.stock-card.positive { --card-accent: var(--color-positive); }\n'
        '.stock-card.negative { --card-accent: var(--color-negative); }\n'
        '\n'
        '.stock-card__ticker {\n'
        '    font-family: var(--font-mono);\n'
        '    font-size: 0.7rem;\n'
        '    font-weight: 700;\n'
        '    letter-spacing: 0.1em;\n'
        '    text-transform: uppercase;\n'
        '    color: var(--color-muted);\n'
        '    margin: 0 0 0.2rem;\n'
        '}\n'
        '.stock-card__price {\n'
        '    font-size: 1.75rem;\n'
        '    font-weight: 800;\n'
        '    font-variant-numeric: tabular-nums;\n'
        '    letter-spacing: -0.02em;\n'
        '    line-height: 1;\n'
        '    margin: 0.25rem 0;\n'
        '}\n'
        '.badge {\n'
        '    display: inline-block;\n'
        '    font-size: 0.75rem;\n'
        '    font-weight: 600;\n'
        '    padding: 0.2rem 0.5rem;\n'
        '    border-radius: 100px;\n'
        '    font-variant-numeric: tabular-nums;\n'
        '}\n'
        '.badge--up   { background: #dcfce7; color: #166534; }\n'
        '.badge--down { background: #fee2e2; color: #991b1b; }\n'
        '.badge--flat { background: #f1f5f9; color: #475569; }',
        filename='styles/tradeboard-solution.css',
        styles=styles
    ))

    # -------------------------------------------------------------------------
    # Exercise 2
    # -------------------------------------------------------------------------
    s.append(spacer(12))
    s.append(exercise(
        2,
        "Responsive Navigation Bar with CSS-Only Hamburger Menu",
        [
            ("ExerciseBody",
             "Build a navigation bar that shows normal links on desktop and collapses to a "
             "hamburger menu on mobile — using ONLY CSS (no JavaScript). Hint: use a hidden "
             "checkbox and the ~ (general sibling) combinator."),
            ("ExerciseBody", "SOLUTION:"),
        ],
        styles=styles
    ))
    s.append(code_block(
        '<!-- hamburger-nav.html -->\n'
        '<header class="navbar">\n'
        '    <a class="navbar__logo" href="/">TradeBoard</a>\n'
        '\n'
        '    <!-- Checkbox hack — hidden, but activates the menu -->\n'
        '    <input type="checkbox" id="nav-toggle" class="navbar__toggle-checkbox">\n'
        '    <label for="nav-toggle" class="navbar__hamburger" aria-label="Toggle navigation">\n'
        '        <span></span>\n'
        '        <span></span>\n'
        '        <span></span>\n'
        '    </label>\n'
        '\n'
        '    <nav class="navbar__menu">\n'
        '        <a href="/markets">Markets</a>\n'
        '        <a href="/portfolio">Portfolio</a>\n'
        '        <a href="/news">News</a>\n'
        '        <a href="/watchlist">Watchlist</a>\n'
        '    </nav>\n'
        '</header>',
        filename='hamburger-nav.html',
        styles=styles
    ))
    s.append(code_block(
        '/* hamburger-nav.css */\n'
        '\n'
        '.navbar {\n'
        '    display: flex;\n'
        '    align-items: center;\n'
        '    justify-content: space-between;\n'
        '    padding: 0 1.5rem;\n'
        '    height: 60px;\n'
        '    background: #1a1a2e;\n'
        '    position: sticky;\n'
        '    top: 0;\n'
        '    z-index: 100;\n'
        '}\n'
        '\n'
        '.navbar__logo {\n'
        '    color: white;\n'
        '    text-decoration: none;\n'
        '    font-size: 1.125rem;\n'
        '    font-weight: 800;\n'
        '    letter-spacing: -0.03em;\n'
        '}\n'
        '\n'
        '/* -------- Desktop: menu is always visible -------- */\n'
        '.navbar__menu {\n'
        '    display: flex;\n'
        '    gap: 0.25rem;\n'
        '}\n'
        '\n'
        '.navbar__menu a {\n'
        '    color: rgba(255,255,255,0.75);\n'
        '    text-decoration: none;\n'
        '    padding: 0.5rem 0.875rem;\n'
        '    border-radius: 6px;\n'
        '    font-size: 0.9rem;\n'
        '    font-weight: 500;\n'
        '    transition: color 0.2s, background 0.2s;\n'
        '}\n'
        '\n'
        '.navbar__menu a:hover {\n'
        '    color: white;\n'
        '    background: rgba(255,255,255,0.1);\n'
        '}\n'
        '\n'
        '/* -------- Hide checkbox and hamburger on desktop -------- */\n'
        '.navbar__toggle-checkbox,\n'
        '.navbar__hamburger {\n'
        '    display: none;\n'
        '}\n'
        '\n'
        '/* -------- Mobile breakpoint -------- */\n'
        '@media (max-width: 640px) {\n'
        '    /* Show hamburger */\n'
        '    .navbar__hamburger {\n'
        '        display: flex;\n'
        '        flex-direction: column;\n'
        '        justify-content: space-between;\n'
        '        width: 24px;\n'
        '        height: 18px;\n'
        '        cursor: pointer;\n'
        '        z-index: 200;\n'
        '    }\n'
        '\n'
        '    .navbar__hamburger span {\n'
        '        display: block;\n'
        '        width: 100%;\n'
        '        height: 2px;\n'
        '        background: white;\n'
        '        border-radius: 2px;\n'
        '        transition: transform 0.25s, opacity 0.25s;\n'
        '        transform-origin: center;\n'
        '    }\n'
        '\n'
        '    /* Animate hamburger to X when checked */\n'
        '    .navbar__toggle-checkbox:checked + .navbar__hamburger span:nth-child(1) {\n'
        '        transform: translateY(8px) rotate(45deg);\n'
        '    }\n'
        '    .navbar__toggle-checkbox:checked + .navbar__hamburger span:nth-child(2) {\n'
        '        opacity: 0;\n'
        '        transform: scaleX(0);\n'
        '    }\n'
        '    .navbar__toggle-checkbox:checked + .navbar__hamburger span:nth-child(3) {\n'
        '        transform: translateY(-8px) rotate(-45deg);\n'
        '    }\n'
        '\n'
        '    /* Collapse menu on mobile */\n'
        '    .navbar__menu {\n'
        '        position: fixed;\n'
        '        top: 60px;\n'
        '        left: 0;\n'
        '        right: 0;\n'
        '        background: #1a1a2e;\n'
        '        flex-direction: column;\n'
        '        padding: 1rem;\n'
        '        gap: 0.25rem;\n'
        '        transform: translateY(-110%);\n'
        '        transition: transform 0.3s ease;\n'
        '        border-bottom: 1px solid rgba(255,255,255,0.1);\n'
        '    }\n'
        '\n'
        '    /* Show menu when checkbox is checked */\n'
        '    /* ~ is general sibling — reaches across the hamburger label */\n'
        '    .navbar__toggle-checkbox:checked ~ .navbar__menu {\n'
        '        transform: translateY(0);\n'
        '    }\n'
        '\n'
        '    .navbar__menu a {\n'
        '        display: block;\n'
        '        padding: 0.75rem 1rem;\n'
        '        border-radius: 8px;\n'
        '        font-size: 1rem;\n'
        '    }\n'
        '}',
        filename='hamburger-nav.css',
        styles=styles
    ))

    # -------------------------------------------------------------------------
    # Exercise 3
    # -------------------------------------------------------------------------
    s.append(spacer(12))
    s.append(exercise(
        2,
        "Stock Price Card Component with Hover Effects",
        [
            ("ExerciseBody",
             "Create a polished stock price card component with: BEM class naming, smooth hover "
             "effect (lift + shadow), a colored top border that changes based on positive/negative "
             "state, an animated price flash when a new price arrives (add class via JS), "
             "and a sparkline placeholder (SVG or simple bar chart using div widths)."),
            ("ExerciseBody", "SOLUTION:"),
        ],
        styles=styles
    ))
    s.append(code_block(
        '<!-- stock-card-component.html -->\n'
        '<article class="stock-card stock-card--positive" tabindex="0">\n'
        '    <div class="stock-card__header">\n'
        '        <div class="stock-card__identity">\n'
        '            <span class="stock-card__ticker">AAPL</span>\n'
        '            <span class="stock-card__name">Apple Inc.</span>\n'
        '        </div>\n'
        '        <span class="stock-card__badge stock-card__badge--up">+2.3%</span>\n'
        '    </div>\n'
        '    <div class="stock-card__price">$182.50</div>\n'
        '    <div class="stock-card__footer">\n'
        '        <span class="stock-card__volume">Vol 54.3M</span>\n'
        '        <div class="stock-card__sparkline" aria-hidden="true">\n'
        '            <!-- Simple CSS bar chart sparkline -->\n'
        '            <span style="--h:40%"></span>\n'
        '            <span style="--h:55%"></span>\n'
        '            <span style="--h:45%"></span>\n'
        '            <span style="--h:70%"></span>\n'
        '            <span style="--h:60%"></span>\n'
        '            <span style="--h:85%"></span>\n'
        '            <span style="--h:75%"></span>\n'
        '            <span style="--h:90%"></span>\n'
        '        </div>\n'
        '    </div>\n'
        '</article>',
        filename='stock-card-component.html',
        styles=styles
    ))
    s.append(code_block(
        '/* stock-card-component.css */\n'
        '\n'
        '@keyframes cardEnter {\n'
        '    from { opacity: 0; transform: translateY(10px) scale(0.98); }\n'
        '    to   { opacity: 1; transform: translateY(0)   scale(1); }\n'
        '}\n'
        '@keyframes priceFlashUp {\n'
        '    0%,100% { background: transparent; color: inherit; }\n'
        '    20%     { background: rgba(34,197,94,0.15); color: #166534; }\n'
        '}\n'
        '@keyframes priceFlashDown {\n'
        '    0%,100% { background: transparent; color: inherit; }\n'
        '    20%     { background: rgba(239,68,68,0.15); color: #991b1b; }\n'
        '}\n'
        '\n'
        '.stock-card {\n'
        '    background: #fff;\n'
        '    border: 1px solid #e2e8f0;\n'
        '    border-top: 3px solid var(--card-color, #e2e8f0);\n'
        '    border-radius: 12px;\n'
        '    padding: 1.25rem 1.5rem;\n'
        '    cursor: pointer;\n'
        '    position: relative;\n'
        '    animation: cardEnter 0.35s ease-out both;\n'
        '    transition:\n'
        '        box-shadow 0.2s ease,\n'
        '        transform  0.2s ease,\n'
        '        border-color 0.3s;\n'
        '}\n'
        '.stock-card:hover, .stock-card:focus-visible {\n'
        '    box-shadow: 0 8px 20px rgba(0,0,0,0.09);\n'
        '    transform: translateY(-2px);\n'
        '    outline: none;\n'
        '}\n'
        '.stock-card:focus-visible { outline: 2px solid #e94560; outline-offset: 2px; }\n'
        '.stock-card--positive { --card-color: #22c55e; }\n'
        '.stock-card--negative { --card-color: #ef4444; }\n'
        '\n'
        '.stock-card__header {\n'
        '    display: flex;\n'
        '    justify-content: space-between;\n'
        '    align-items: flex-start;\n'
        '    margin-bottom: 0.75rem;\n'
        '}\n'
        '.stock-card__ticker {\n'
        '    display: block;\n'
        '    font-size: 0.7rem;\n'
        '    font-weight: 700;\n'
        '    letter-spacing: 0.09em;\n'
        '    text-transform: uppercase;\n'
        '    color: #64748b;\n'
        '    font-family: monospace;\n'
        '}\n'
        '.stock-card__name {\n'
        '    font-size: 0.78rem;\n'
        '    color: #94a3b8;\n'
        '    margin-top: 0.1rem;\n'
        '}\n'
        '.stock-card__badge {\n'
        '    font-size: 0.75rem;\n'
        '    font-weight: 700;\n'
        '    padding: 0.2rem 0.55rem;\n'
        '    border-radius: 100px;\n'
        '    font-variant-numeric: tabular-nums;\n'
        '}\n'
        '.stock-card__badge--up   { background: #dcfce7; color: #166534; }\n'
        '.stock-card__badge--down { background: #fee2e2; color: #991b1b; }\n'
        '.stock-card__price {\n'
        '    font-size: 1.8rem;\n'
        '    font-weight: 800;\n'
        '    font-variant-numeric: tabular-nums;\n'
        '    letter-spacing: -0.025em;\n'
        '    line-height: 1;\n'
        '    border-radius: 4px;\n'
        '    padding: 0.1rem 0.2rem;\n'
        '    margin: 0 -0.2rem;\n'
        '}\n'
        '.stock-card__price.flash-up   { animation: priceFlashUp   1s ease-out; }\n'
        '.stock-card__price.flash-down { animation: priceFlashDown 1s ease-out; }\n'
        '\n'
        '.stock-card__footer {\n'
        '    display: flex;\n'
        '    justify-content: space-between;\n'
        '    align-items: flex-end;\n'
        '    margin-top: 1rem;\n'
        '    padding-top: 0.75rem;\n'
        '    border-top: 1px solid #f1f5f9;\n'
        '}\n'
        '.stock-card__volume {\n'
        '    font-size: 0.72rem;\n'
        '    color: #94a3b8;\n'
        '}\n'
        '/* Mini sparkline using inline custom properties */\n'
        '.stock-card__sparkline {\n'
        '    display: flex;\n'
        '    align-items: flex-end;\n'
        '    gap: 2px;\n'
        '    height: 32px;\n'
        '}\n'
        '.stock-card__sparkline span {\n'
        '    display: block;\n'
        '    width: 4px;\n'
        '    height: var(--h, 50%);\n'
        '    background: var(--card-color, #94a3b8);\n'
        '    border-radius: 2px;\n'
        '    opacity: 0.6;\n'
        '}\n'
        '.stock-card--positive .stock-card__sparkline span { background: #22c55e; }\n'
        '.stock-card--negative .stock-card__sparkline span { background: #ef4444; }\n'
        '\n'
        '@media (prefers-reduced-motion: reduce) {\n'
        '    .stock-card, .stock-card__price { animation: none; transition: none; }\n'
        '}',
        filename='stock-card-component.css',
        styles=styles
    ))

    # -------------------------------------------------------------------------
    # Exercise 4
    # -------------------------------------------------------------------------
    s.append(spacer(12))
    s.append(exercise(
        3,
        "Build TradeBoard Layout Using CSS Grid + Flexbox, Fully Responsive",
        [
            ("ExerciseBody",
             "Build the complete TradeBoard application layout using CSS Grid for the page "
             "structure and Flexbox for component internals. Requirements: sticky header, "
             "left sidebar with watchlist, main content area with metric cards and chart, "
             "right panel with news feed. Fully responsive: desktop = 3 columns, "
             "tablet = 2 columns (hide right panel), mobile = 1 column (hide sidebar)."),
            ("ExerciseBody", "SOLUTION:"),
        ],
        styles=styles
    ))
    s.append(code_block(
        '/* tradeboard-layout-solution.css */\n'
        '\n'
        '*, *::before, *::after { box-sizing: border-box; }\n'
        '\n'
        ':root {\n'
        '    --header-h: 64px;\n'
        '    --sidebar-w: 220px;\n'
        '    --panel-w: 300px;\n'
        '    --bg: #0f1117;\n'
        '    --surface: #1a1d27;\n'
        '    --border: #252837;\n'
        '    --text: #e2e8f0;\n'
        '    --muted: #64748b;\n'
        '    --accent: #e94560;\n'
        '}\n'
        '\n'
        'body { margin: 0; background: var(--bg); color: var(--text);\n'
        '       font-family: system-ui, sans-serif; overflow-x: hidden; }\n'
        '\n'
        '/* ===== App Shell Grid ===== */\n'
        '.app {\n'
        '    display: grid;\n'
        '    grid-template-columns: var(--sidebar-w) 1fr var(--panel-w);\n'
        '    grid-template-rows: var(--header-h) 1fr;\n'
        '    grid-template-areas:\n'
        '        "header header header"\n'
        '        "sidebar main panel";\n'
        '    min-height: 100vh;\n'
        '}\n'
        '\n'
        '/* ===== Header ===== */\n'
        '.app__header {\n'
        '    grid-area: header;\n'
        '    background: var(--surface);\n'
        '    border-bottom: 1px solid var(--border);\n'
        '    display: flex;\n'
        '    align-items: center;\n'
        '    justify-content: space-between;\n'
        '    padding: 0 1.5rem;\n'
        '    position: sticky;\n'
        '    top: 0;\n'
        '    z-index: 50;\n'
        '}\n'
        '.app__logo { color: #fff; font-weight: 800; font-size: 1.1rem;\n'
        '             text-decoration: none; letter-spacing: -0.03em; }\n'
        '.app__logo span { color: var(--accent); }\n'
        '.app__header-actions { display: flex; align-items: center; gap: 0.75rem; }\n'
        '.app__search {\n'
        '    background: rgba(255,255,255,0.05);\n'
        '    border: 1px solid var(--border);\n'
        '    color: var(--text);\n'
        '    padding: 0.4rem 0.875rem;\n'
        '    border-radius: 6px;\n'
        '    font-size: 0.875rem;\n'
        '    width: 200px;\n'
        '    transition: border-color 0.2s, width 0.3s;\n'
        '}\n'
        '.app__search:focus {\n'
        '    outline: none;\n'
        '    border-color: var(--accent);\n'
        '    width: 260px;\n'
        '}\n'
        '\n'
        '/* ===== Sidebar ===== */\n'
        '.app__sidebar {\n'
        '    grid-area: sidebar;\n'
        '    background: var(--surface);\n'
        '    border-right: 1px solid var(--border);\n'
        '    overflow-y: auto;\n'
        '    padding: 1rem 0;\n'
        '    display: flex;\n'
        '    flex-direction: column;\n'
        '    gap: 0;\n'
        '}\n'
        '.sidebar-section { padding: 0.5rem 0; }\n'
        '.sidebar-title {\n'
        '    font-size: 0.65rem;\n'
        '    font-weight: 700;\n'
        '    letter-spacing: 0.1em;\n'
        '    text-transform: uppercase;\n'
        '    color: var(--muted);\n'
        '    padding: 0.5rem 1rem 0.25rem;\n'
        '}\n'
        '.sidebar-item {\n'
        '    display: flex;\n'
        '    align-items: center;\n'
        '    justify-content: space-between;\n'
        '    padding: 0.5rem 1rem;\n'
        '    cursor: pointer;\n'
        '    border-radius: 0;\n'
        '    transition: background 0.15s;\n'
        '    font-size: 0.875rem;\n'
        '}\n'
        '.sidebar-item:hover { background: rgba(255,255,255,0.05); }\n'
        '.sidebar-item__ticker { font-weight: 600; font-family: monospace; }\n'
        '.sidebar-item__change { font-size: 0.75rem; font-variant-numeric: tabular-nums; }\n'
        '.sidebar-item__change.up   { color: #22c55e; }\n'
        '.sidebar-item__change.down { color: #ef4444; }\n'
        '\n'
        '/* ===== Main Content ===== */\n'
        '.app__main {\n'
        '    grid-area: main;\n'
        '    overflow-y: auto;\n'
        '    padding: 1.5rem;\n'
        '    display: flex;\n'
        '    flex-direction: column;\n'
        '    gap: 1.5rem;\n'
        '}\n'
        '.metrics-grid {\n'
        '    display: grid;\n'
        '    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));\n'
        '    gap: 1rem;\n'
        '}\n'
        '.metric-card {\n'
        '    background: var(--surface);\n'
        '    border: 1px solid var(--border);\n'
        '    border-radius: 10px;\n'
        '    padding: 1.125rem 1.25rem;\n'
        '}\n'
        '.metric-card__label {\n'
        '    font-size: 0.7rem;\n'
        '    font-weight: 600;\n'
        '    letter-spacing: 0.08em;\n'
        '    text-transform: uppercase;\n'
        '    color: var(--muted);\n'
        '    margin-bottom: 0.5rem;\n'
        '}\n'
        '.metric-card__value {\n'
        '    font-size: 1.5rem;\n'
        '    font-weight: 800;\n'
        '    font-variant-numeric: tabular-nums;\n'
        '    letter-spacing: -0.02em;\n'
        '}\n'
        '.chart-card {\n'
        '    background: var(--surface);\n'
        '    border: 1px solid var(--border);\n'
        '    border-radius: 10px;\n'
        '    padding: 1.5rem;\n'
        '    min-height: 280px;\n'
        '    display: flex;\n'
        '    flex-direction: column;\n'
        '}\n'
        '\n'
        '/* ===== Right Panel ===== */\n'
        '.app__panel {\n'
        '    grid-area: panel;\n'
        '    background: var(--surface);\n'
        '    border-left: 1px solid var(--border);\n'
        '    overflow-y: auto;\n'
        '    padding: 1rem;\n'
        '    display: flex;\n'
        '    flex-direction: column;\n'
        '    gap: 0.75rem;\n'
        '}\n'
        '\n'
        '/* ===== Responsive ===== */\n'
        '@media (max-width: 1024px) {\n'
        '    .app {\n'
        '        grid-template-columns: var(--sidebar-w) 1fr;\n'
        '        grid-template-areas:\n'
        '            "header header"\n'
        '            "sidebar main";\n'
        '    }\n'
        '    .app__panel { display: none; }\n'
        '}\n'
        '@media (max-width: 640px) {\n'
        '    .app {\n'
        '        grid-template-columns: 1fr;\n'
        '        grid-template-areas:\n'
        '            "header"\n'
        '            "main";\n'
        '    }\n'
        '    .app__sidebar { display: none; }\n'
        '    .app__main { padding: 1rem; }\n'
        '}',
        filename='tradeboard-layout-solution.css',
        styles=styles
    ))

    # -------------------------------------------------------------------------
    # Exercise 5
    # -------------------------------------------------------------------------
    s.append(spacer(12))
    s.append(exercise(
        3,
        "Build a CSS Design System with Custom Properties",
        [
            ("ExerciseBody",
             "Create a comprehensive design system using CSS custom properties. Include: "
             "complete color palette (neutrals + brand + semantic), typographic scale, "
             "spacing scale, border radii, shadow scale, and a dark mode using the "
             "prefers-color-scheme media query. Use all tokens in at least 2 components."),
            ("ExerciseBody", "SOLUTION:"),
        ],
        styles=styles
    ))
    s.append(code_block(
        '/* design-system.css — complete token system */\n'
        '\n'
        ':root {\n'
        '    /* --- Color: Neutrals --- */\n'
        '    --color-neutral-0:   #ffffff;\n'
        '    --color-neutral-50:  #f8fafc;\n'
        '    --color-neutral-100: #f1f5f9;\n'
        '    --color-neutral-200: #e2e8f0;\n'
        '    --color-neutral-300: #cbd5e1;\n'
        '    --color-neutral-400: #94a3b8;\n'
        '    --color-neutral-500: #64748b;\n'
        '    --color-neutral-600: #475569;\n'
        '    --color-neutral-700: #334155;\n'
        '    --color-neutral-800: #1e293b;\n'
        '    --color-neutral-900: #0f172a;\n'
        '\n'
        '    /* --- Color: Brand --- */\n'
        '    --color-brand-light:  #f9a8b9;\n'
        '    --color-brand-base:   #e94560;\n'
        '    --color-brand-dark:   #a42d43;\n'
        '\n'
        '    /* --- Color: Semantic --- */\n'
        '    --color-success-light: #dcfce7;\n'
        '    --color-success:       #22c55e;\n'
        '    --color-success-dark:  #16a34a;\n'
        '    --color-error-light:   #fee2e2;\n'
        '    --color-error:         #ef4444;\n'
        '    --color-error-dark:    #dc2626;\n'
        '    --color-warning-light: #fef9c3;\n'
        '    --color-warning:       #eab308;\n'
        '    --color-info-light:    #dbeafe;\n'
        '    --color-info:          #3b82f6;\n'
        '\n'
        '    /* --- Aliases: Light Mode --- */\n'
        '    --color-bg:        var(--color-neutral-50);\n'
        '    --color-surface:   var(--color-neutral-0);\n'
        '    --color-border:    var(--color-neutral-200);\n'
        '    --color-text:      var(--color-neutral-900);\n'
        '    --color-text-2:    var(--color-neutral-600);\n'
        '    --color-text-3:    var(--color-neutral-400);\n'
        '    --color-primary:   var(--color-brand-base);\n'
        '\n'
        '    /* --- Typography Scale (Perfect Fourth 1.333) --- */\n'
        '    --text-xs:   0.563rem;\n'
        '    --text-sm:   0.75rem;\n'
        '    --text-base: 1rem;\n'
        '    --text-md:   1.333rem;\n'
        '    --text-lg:   1.777rem;\n'
        '    --text-xl:   2.369rem;\n'
        '    --text-2xl:  3.157rem;\n'
        '\n'
        '    /* --- Font Families --- */\n'
        '    --font-sans: system-ui, -apple-system, sans-serif;\n'
        '    --font-mono: "JetBrains Mono", "Fira Code", monospace;\n'
        '\n'
        '    /* --- Font Weights --- */\n'
        '    --fw-normal:   400;\n'
        '    --fw-medium:   500;\n'
        '    --fw-semibold: 600;\n'
        '    --fw-bold:     700;\n'
        '    --fw-black:    900;\n'
        '\n'
        '    /* --- Spacing Scale (4px base) --- */\n'
        '    --space-1:  0.25rem;   /*  4px */\n'
        '    --space-2:  0.5rem;    /*  8px */\n'
        '    --space-3:  0.75rem;   /* 12px */\n'
        '    --space-4:  1rem;      /* 16px */\n'
        '    --space-5:  1.25rem;   /* 20px */\n'
        '    --space-6:  1.5rem;    /* 24px */\n'
        '    --space-8:  2rem;      /* 32px */\n'
        '    --space-10: 2.5rem;    /* 40px */\n'
        '    --space-12: 3rem;      /* 48px */\n'
        '    --space-16: 4rem;      /* 64px */\n'
        '\n'
        '    /* --- Border Radii --- */\n'
        '    --radius-xs: 2px;\n'
        '    --radius-sm: 4px;\n'
        '    --radius-md: 8px;\n'
        '    --radius-lg: 12px;\n'
        '    --radius-xl: 16px;\n'
        '    --radius-2xl: 24px;\n'
        '    --radius-full: 9999px;\n'
        '\n'
        '    /* --- Shadows --- */\n'
        '    --shadow-xs: 0 1px 2px rgba(0,0,0,0.04);\n'
        '    --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);\n'
        '    --shadow-md: 0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.05);\n'
        '    --shadow-lg: 0 10px 15px rgba(0,0,0,0.08), 0 4px 6px rgba(0,0,0,0.04);\n'
        '    --shadow-xl: 0 20px 25px rgba(0,0,0,0.08), 0 8px 10px rgba(0,0,0,0.04);\n'
        '\n'
        '    /* --- Transitions --- */\n'
        '    --transition-fast:   0.12s ease;\n'
        '    --transition-base:   0.2s ease;\n'
        '    --transition-slow:   0.35s ease;\n'
        '}\n'
        '\n'
        '/* --- Dark Mode Aliases --- */\n'
        '@media (prefers-color-scheme: dark) {\n'
        '    :root {\n'
        '        --color-bg:      var(--color-neutral-900);\n'
        '        --color-surface: var(--color-neutral-800);\n'
        '        --color-border:  var(--color-neutral-700);\n'
        '        --color-text:    var(--color-neutral-50);\n'
        '        --color-text-2:  var(--color-neutral-300);\n'
        '        --color-text-3:  var(--color-neutral-500);\n'
        '        --shadow-md: 0 4px 6px rgba(0,0,0,0.3), 0 2px 4px rgba(0,0,0,0.2);\n'
        '        --shadow-lg: 0 10px 15px rgba(0,0,0,0.4), 0 4px 6px rgba(0,0,0,0.2);\n'
        '    }\n'
        '}\n'
        '\n'
        '/* --- Using tokens in components --- */\n'
        '.card {\n'
        '    background: var(--color-surface);\n'
        '    border: 1px solid var(--color-border);\n'
        '    border-radius: var(--radius-lg);\n'
        '    padding: var(--space-6);\n'
        '    box-shadow: var(--shadow-md);\n'
        '    color: var(--color-text);\n'
        '}\n'
        '\n'
        '.btn {\n'
        '    display: inline-flex;\n'
        '    align-items: center;\n'
        '    gap: var(--space-2);\n'
        '    padding: var(--space-2) var(--space-5);\n'
        '    border-radius: var(--radius-md);\n'
        '    font-size: var(--text-sm);\n'
        '    font-weight: var(--fw-semibold);\n'
        '    border: none;\n'
        '    cursor: pointer;\n'
        '    transition: background var(--transition-base), transform var(--transition-fast);\n'
        '}\n'
        '.btn--primary {\n'
        '    background: var(--color-primary);\n'
        '    color: white;\n'
        '}\n'
        '.btn--primary:hover { filter: brightness(0.9); transform: translateY(-1px); }',
        filename='design-system-solution.css',
        styles=styles
    ))

    # -------------------------------------------------------------------------
    # Exercise 6
    # -------------------------------------------------------------------------
    s.append(spacer(12))
    s.append(exercise(
        4,
        "CSS-Only Animated Skeleton Loader with Shimmer Effect",
        [
            ("ExerciseBody",
             "Build a skeleton loading screen for the TradeBoard stock card. The skeleton "
             "should have placeholders for: ticker label, company name, price, change badge, "
             "footer with volume and sparkline. Apply a shimmer animation that scans across "
             "all skeleton elements using a CSS gradient animation. No JavaScript required."),
            ("ExerciseBody", "SOLUTION:"),
        ],
        styles=styles
    ))
    s.append(code_block(
        '<!-- skeleton-loader.html -->\n'
        '<div class="skeleton-card">\n'
        '    <div class="skeleton-card__header">\n'
        '        <div class="skeleton-card__identity">\n'
        '            <div class="skeleton skeleton--ticker"></div>\n'
        '            <div class="skeleton skeleton--name"></div>\n'
        '        </div>\n'
        '        <div class="skeleton skeleton--badge"></div>\n'
        '    </div>\n'
        '    <div class="skeleton skeleton--price"></div>\n'
        '    <div class="skeleton-card__footer">\n'
        '        <div class="skeleton skeleton--volume"></div>\n'
        '        <div class="skeleton-card__bars">\n'
        '            <div class="skeleton skeleton--bar"></div>\n'
        '            <div class="skeleton skeleton--bar"></div>\n'
        '            <div class="skeleton skeleton--bar"></div>\n'
        '            <div class="skeleton skeleton--bar"></div>\n'
        '            <div class="skeleton skeleton--bar"></div>\n'
        '            <div class="skeleton skeleton--bar"></div>\n'
        '            <div class="skeleton skeleton--bar"></div>\n'
        '            <div class="skeleton skeleton--bar"></div>\n'
        '        </div>\n'
        '    </div>\n'
        '</div>',
        filename='skeleton-loader.html',
        styles=styles
    ))
    s.append(code_block(
        '/* skeleton-loader.css */\n'
        '\n'
        '/* Shimmer keyframe */\n'
        '@keyframes shimmer {\n'
        '    0%   { background-position: -600px 0; }\n'
        '    100% { background-position: 600px 0; }\n'
        '}\n'
        '\n'
        '/* Base skeleton element */\n'
        '.skeleton {\n'
        '    background: linear-gradient(\n'
        '        90deg,\n'
        '        #e2e8f0 0%,\n'
        '        #f1f5f9 40%,\n'
        '        #e8edf4 60%,\n'
        '        #e2e8f0 100%\n'
        '    );\n'
        '    background-size: 600px 100%;\n'
        '    border-radius: 4px;\n'
        '    animation: shimmer 1.4s ease-in-out infinite;\n'
        '}\n'
        '\n'
        '/* Dark mode shimmer */\n'
        '@media (prefers-color-scheme: dark) {\n'
        '    .skeleton {\n'
        '        background: linear-gradient(\n'
        '            90deg,\n'
        '            #1e293b 0%,\n'
        '            #334155 40%,\n'
        '            #273548 60%,\n'
        '            #1e293b 100%\n'
        '        );\n'
        '        background-size: 600px 100%;\n'
        '    }\n'
        '}\n'
        '\n'
        '/* Card container */\n'
        '.skeleton-card {\n'
        '    background: white;\n'
        '    border: 1px solid #e2e8f0;\n'
        '    border-radius: 12px;\n'
        '    padding: 1.25rem 1.5rem;\n'
        '    display: flex;\n'
        '    flex-direction: column;\n'
        '    gap: 0.75rem;\n'
        '}\n'
        '@media (prefers-color-scheme: dark) {\n'
        '    .skeleton-card { background: #1e293b; border-color: #334155; }\n'
        '}\n'
        '\n'
        '/* Skeleton size variants */\n'
        '.skeleton--ticker {\n'
        '    height: 10px;\n'
        '    width: 48px;\n'
        '    border-radius: 2px;\n'
        '}\n'
        '.skeleton--name {\n'
        '    height: 10px;\n'
        '    width: 80px;\n'
        '    margin-top: 4px;\n'
        '    border-radius: 2px;\n'
        '}\n'
        '.skeleton--badge {\n'
        '    height: 22px;\n'
        '    width: 52px;\n'
        '    border-radius: 100px;\n'
        '}\n'
        '.skeleton--price {\n'
        '    height: 36px;\n'
        '    width: 120px;\n'
        '    border-radius: 6px;\n'
        '}\n'
        '.skeleton--volume {\n'
        '    height: 10px;\n'
        '    width: 56px;\n'
        '    border-radius: 2px;\n'
        '}\n'
        '.skeleton--bar {\n'
        '    width: 4px;\n'
        '    border-radius: 2px;\n'
        '    animation-delay: calc(var(--i, 0) * 80ms);\n'
        '}\n'
        '\n'
        '/* Stagger bar heights (set --h via inline style or nth-child) */\n'
        '.skeleton--bar:nth-child(1) { height: 40%; }\n'
        '.skeleton--bar:nth-child(2) { height: 55%; }\n'
        '.skeleton--bar:nth-child(3) { height: 45%; }\n'
        '.skeleton--bar:nth-child(4) { height: 70%; }\n'
        '.skeleton--bar:nth-child(5) { height: 60%; }\n'
        '.skeleton--bar:nth-child(6) { height: 80%; }\n'
        '.skeleton--bar:nth-child(7) { height: 70%; }\n'
        '.skeleton--bar:nth-child(8) { height: 90%; }\n'
        '\n'
        '/* Layout */\n'
        '.skeleton-card__header {\n'
        '    display: flex;\n'
        '    justify-content: space-between;\n'
        '    align-items: flex-start;\n'
        '}\n'
        '.skeleton-card__footer {\n'
        '    display: flex;\n'
        '    justify-content: space-between;\n'
        '    align-items: flex-end;\n'
        '    padding-top: 0.75rem;\n'
        '    border-top: 1px solid #f1f5f9;\n'
        '}\n'
        '.skeleton-card__bars {\n'
        '    display: flex;\n'
        '    align-items: flex-end;\n'
        '    gap: 2px;\n'
        '    height: 32px;\n'
        '}\n'
        '\n'
        '/* Respect user motion preference */\n'
        '@media (prefers-reduced-motion: reduce) {\n'
        '    .skeleton {\n'
        '        animation: none;\n'
        '        background: #e2e8f0;\n'
        '    }\n'
        '    @media (prefers-color-scheme: dark) {\n'
        '        .skeleton { background: #334155; }\n'
        '    }\n'
        '}',
        filename='skeleton-loader.css',
        styles=styles
    ))
    return s


# ============================================================================
# MAIN BUILD FUNCTION
# ============================================================================

def build_chapter_3(styles):
    """Build and return the complete Chapter 3 story (list of flowables)."""
    story = []

    # Chapter cover page
    story.append(ChapterCoverPage(
        3,
        "CSS \u2014 The Paint and Interior Design",
        "Interior Design: How You Decorate the House",
        "PART 1: FOUNDATIONS"
    ))
    story.append(PageBreak())

    # Section 3.1
    story.extend(section_3_1(styles))
    story.append(page_break())

    # Section 3.2
    story.extend(section_3_2(styles))
    story.append(page_break())

    # Section 3.3
    story.extend(section_3_3(styles))
    story.append(page_break())

    # Section 3.4
    story.extend(section_3_4(styles))
    story.append(page_break())

    # Section 3.5
    story.extend(section_3_5(styles))
    story.append(page_break())

    # Section 3.6
    story.extend(section_3_6(styles))
    story.append(page_break())

    # Section 3.7
    story.extend(section_3_7(styles))
    story.append(page_break())

    # Section 3.8
    story.extend(section_3_8(styles))
    story.append(page_break())

    # Section 3.9
    story.extend(section_3_9(styles))
    story.append(page_break())

    # Section 3.10
    story.extend(section_3_10(styles))
    story.append(page_break())

    # Section 3.11
    story.extend(section_3_11(styles))
    story.append(page_break())

    # Section 3.12
    story.extend(section_3_12(styles))
    story.append(page_break())

    # Section 3.13
    story.extend(section_3_13(styles))
    story.append(page_break())

    # Exercises
    story.extend(section_exercises(styles))

    # Chapter checkpoint
    story.append(spacer(20))
    story.append(HorizontalLine())
    story.append(spacer(12))
    story.append(checkpoint(
        "Chapter 3 Complete: You now understand the full CSS foundation — "
        "selectors, specificity, the box model, flexbox, grid, responsive design, "
        "typography, color systems, animations, modern CSS, and CSS architecture at "
        "the Principal Engineer level.",
        styles
    ))
    story.append(spacer(8))
    story.append(p(
        "In Chapter 4, we bring the page to life with JavaScript — adding interactivity, "
        "responding to events, manipulating the DOM, and fetching live data for TradeBoard's "
        "real-time price feed.",
        styles
    ))

    return story

