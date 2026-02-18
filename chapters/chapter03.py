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

