"""Chapter 2: HTML - The Skeleton"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_2(styles):
    story = []

    story.append(ChapterCoverPage(2, "HTML — The Skeleton",
                                  "Building a House: HTML is the Frame", "PART 1: FOUNDATIONS"))
    story.append(PageBreak())

    # 2.1 WHAT HTML ACTUALLY IS
    story.append(h1("2.1 What HTML Actually Is", styles))

    story.append(analogy_box(
        "HTML is the wooden frame of a house. It defines the structure — where the walls are, where "
        "the doors go, where the windows are. It does not decide what color the walls are painted "
        "(that is CSS) or whether the lights turn on when you clap your hands (that is JavaScript). "
        "Without the frame, there is no house. Without HTML, there is no web page."
    , styles))

    story.append(p(
        "HTML stands for <b>HyperText Markup Language</b>. <b>HyperText</b> means "
        "text that links to other text (hyperlinks). <b>Markup</b> means you annotate content with tags that "
        "describe its purpose. It is a markup language, not a programming language: it describes structure and "
        "meaning, not behavior."
    , styles))

    story.append(h2("Tags, Elements, and Attributes", styles))

    story.append(analogy_box(
        "A tag is like a labeled box. &lt;p&gt; is a box labeled 'paragraph.' Everything you put inside "
        "the box is treated as paragraph text. The opening tag is opening the box. The closing "
        "tag is sealing it shut. The content between them is what is inside the box."
    , styles))

    story.append(code_block(
        '&lt;!-- This is an HTML element --&gt;\n'
        '&lt;p class="intro"&gt;Welcome to TradeBoard.&lt;/p&gt;\n\n'
        '&lt;!-- Breaking it down: --&gt;\n'
        '&lt;!-- &lt;p          = opening tag --&gt;\n'
        '&lt;!-- class="intro" = attribute (name="value") --&gt;\n'
        '&lt;!-- Welcome...  = content (text) --&gt;\n'
        '&lt;!-- &lt;/p&gt;        = closing tag --&gt;\n\n'
        '&lt;!-- Self-closing tags have no content --&gt;\n'
        '&lt;img src="logo.png" alt="TradeBoard logo" /&gt;\n'
        '&lt;br /&gt;\n'
        '&lt;input type="text" placeholder="Search stocks..." /&gt;',
        filename="HTML Tags, Elements, and Attributes",
        styles=styles
    ))

    story.append(mistake_box(
        "Beginners often forget to close tags or close them in the wrong order. "
        "Rule: tags close in the reverse order they opened, like Russian nesting dolls. "
        "If you open A then B, you must close B then A."
    , styles))

    # 2.2 DOCUMENT STRUCTURE
    story.append(h1("2.2 Document Structure", styles))

    story.append(code_block(
        '&lt;!DOCTYPE html&gt;\n'
        '&lt;html lang="en"&gt;\n'
        '&lt;head&gt;\n'
        '  &lt;meta charset="UTF-8" /&gt;\n'
        '  &lt;meta name="viewport" content="width=device-width, initial-scale=1.0" /&gt;\n'
        '  &lt;meta name="description" content="TradeBoard - Personal Stock Watchlist" /&gt;\n'
        '  &lt;title&gt;TradeBoard - Stock Dashboard&lt;/title&gt;\n'
        '  &lt;link rel="stylesheet" href="css/styles.css" /&gt;\n'
        '&lt;/head&gt;\n'
        '&lt;body&gt;\n'
        '  &lt;h1&gt;Welcome to TradeBoard&lt;/h1&gt;\n'
        '  &lt;p&gt;Your personal stock watchlist dashboard.&lt;/p&gt;\n'
        '  &lt;script src="js/app.js" defer&gt;&lt;/script&gt;\n'
        '&lt;/body&gt;\n'
        '&lt;/html&gt;',
        filename="index.html - The Complete HTML Boilerplate",
        styles=styles
    ))

    story.append(p("Every line explained:", styles))
    story.append(bullet("<b>&lt;!DOCTYPE html&gt;</b> — Tells the browser this is modern HTML5. Without it, browsers enter quirks mode.", styles))
    story.append(bullet("<b>&lt;html lang=\"en\"&gt;</b> — Root element. lang tells screen readers and search engines the page language.", styles))
    story.append(bullet("<b>&lt;head&gt;</b> — Metadata ABOUT the page. Nothing here is visible on screen.", styles))
    story.append(bullet("<b>&lt;meta charset=\"UTF-8\"&gt;</b> — Character encoding supporting every language.", styles))
    story.append(bullet("<b>&lt;meta name=\"viewport\"&gt;</b> — Essential for mobile responsive rendering.", styles))
    story.append(bullet("<b>&lt;title&gt;</b> — Text shown in browser tab. Used by search engines for results.", styles))
    story.append(bullet("<b>&lt;body&gt;</b> — Everything visible on the page goes here.", styles))
    story.append(bullet("<b>&lt;script defer&gt;</b> — Loads JS. defer waits until HTML is fully parsed before executing.", styles))

    story.append(analogy_box(
        "The &lt;head&gt; is like the label on the outside of a shipping box — delivery address, "
        "tracking number, handling instructions. The &lt;body&gt; is what is actually inside the box."
    , styles))

    # 2.3 TEXT ELEMENTS
    story.append(h1("2.3 Text Elements", styles))

    story.append(h2("Headings: The Hierarchy of Importance", styles))
    story.append(code_block(
        '&lt;h1&gt;TradeBoard Dashboard&lt;/h1&gt;        &lt;!-- Only ONE per page --&gt;\n'
        '&lt;h2&gt;Market Overview&lt;/h2&gt;              &lt;!-- Major sections --&gt;\n'
        '&lt;h3&gt;Top Gainers&lt;/h3&gt;                  &lt;!-- Subsections --&gt;\n'
        '&lt;h4&gt;Technology Sector&lt;/h4&gt;            &lt;!-- Sub-subsections --&gt;\n'
        '&lt;h5&gt;Large Cap&lt;/h5&gt;                    &lt;!-- Rarely used --&gt;\n'
        '&lt;h6&gt;Individual Stocks&lt;/h6&gt;            &lt;!-- Almost never used --&gt;',
        filename="Heading Hierarchy",
        styles=styles
    ))

    story.append(analogy_box(
        "Headings are like a company org chart. There is only ONE CEO (h1). Under the CEO are several "
        "VPs (h2). Under each VP are directors (h3). You would never have two CEOs, and "
        "you would never have a director reporting directly to the CEO with no VP in between."
    , styles))

    story.append(mistake_box(
        "Never choose a heading level based on how it looks. Choose based on logical hierarchy. "
        "If h2 looks too big, use CSS to change its appearance — do not skip to h4 because it "
        "looks the right size. Screen readers and SEO depend on correct heading hierarchy."
    , styles))

    story.append(h2("Paragraphs and Inline Text", styles))
    story.append(code_block(
        '&lt;p&gt;AAPL closed at $178.52, up 1.3% from yesterday.&lt;/p&gt;\n\n'
        '&lt;!-- Semantic inline elements --&gt;\n'
        '&lt;p&gt;&lt;strong&gt;Warning:&lt;/strong&gt; Past performance does &lt;em&gt;not&lt;/em&gt;\n'
        '   guarantee future results.&lt;/p&gt;\n\n'
        '&lt;!-- strong = important (screen readers emphasize it) --&gt;\n'
        '&lt;!-- em = stressed emphasis (verbal stress) --&gt;\n'
        '&lt;!-- b = visually bold, no semantic meaning --&gt;\n'
        '&lt;!-- i = visually italic, no semantic meaning --&gt;\n\n'
        '&lt;p&gt;The ticker symbol is &lt;code&gt;AAPL&lt;/code&gt;.&lt;/p&gt;\n'
        '&lt;p&gt;&lt;small&gt;Data delayed by 15 minutes.&lt;/small&gt;&lt;/p&gt;',
        filename="Text Elements",
        styles=styles
    ))

    # 2.4 LINKS AND NAVIGATION
    story.append(h1("2.4 Links and Navigation", styles))

    story.append(analogy_box(
        "A link is a portal door. You walk through it and end up somewhere else. The href attribute "
        "is the address written on the door — it tells the browser where the portal leads."
    , styles))

    story.append(code_block(
        '&lt;!-- External link --&gt;\n'
        '&lt;a href="https://finance.yahoo.com"&gt;Yahoo Finance&lt;/a&gt;\n\n'
        '&lt;!-- Internal link --&gt;\n'
        '&lt;a href="/stocks/AAPL"&gt;Apple Inc.&lt;/a&gt;\n\n'
        '&lt;!-- New tab (always add rel for security) --&gt;\n'
        '&lt;a href="https://sec.gov" target="_blank"\n'
        '   rel="noopener noreferrer"&gt;SEC Filings&lt;/a&gt;\n\n'
        '&lt;!-- Download, email, phone --&gt;\n'
        '&lt;a href="/reports/q4.pdf" download&gt;Download Report&lt;/a&gt;\n'
        '&lt;a href="mailto:support@tradeboard.com"&gt;Email Us&lt;/a&gt;\n'
        '&lt;a href="tel:+15550123"&gt;Call Us&lt;/a&gt;\n\n'
        '&lt;!-- Skip navigation (accessibility) --&gt;\n'
        '&lt;a href="#main-content" class="skip-link"&gt;Skip to content&lt;/a&gt;',
        filename="Link Types",
        styles=styles
    ))

    story.append(mistake_box(
        "When using target=\"_blank\", ALWAYS add rel=\"noopener noreferrer\". Without this, "
        "the new page can access your page via window.opener — a security vulnerability called "
        "'tabnapping.' Modern browsers handle this by default, but explicit is better."
    , styles))

    # 2.5 IMAGES AND MEDIA
    story.append(h1("2.5 Images and Media", styles))

    story.append(analogy_box(
        "The alt attribute is like a museum placard next to a painting. If the painting is missing "
        "or the visitor is blind, the placard still describes what should be there. Every meaningful "
        "image MUST have descriptive alt text. Decorative images get alt=\"\" to tell screen readers to skip them."
    , styles))

    story.append(code_block(
        '&lt;!-- Basic image with required alt --&gt;\n'
        '&lt;img src="images/aapl-chart.png"\n'
        '     alt="Apple stock price chart showing 12-month uptrend"\n'
        '     width="600" height="400" /&gt;\n\n'
        '&lt;!-- Lazy loading (loads when scrolled into view) --&gt;\n'
        '&lt;img src="images/chart.png" alt="Stock chart"\n'
        '     loading="lazy" width="600" height="400" /&gt;\n\n'
        '&lt;!-- Responsive image with srcset --&gt;\n'
        '&lt;img src="chart-800.png"\n'
        '     srcset="chart-400.png 400w, chart-800.png 800w, chart-1200.png 1200w"\n'
        '     sizes="(max-width: 600px) 400px, (max-width: 1000px) 800px, 1200px"\n'
        '     alt="Responsive stock chart" /&gt;\n\n'
        '&lt;!-- Figure with caption --&gt;\n'
        '&lt;figure&gt;\n'
        '  &lt;img src="market-summary.png" alt="S&amp;P 500 Q4 performance" /&gt;\n'
        '  &lt;figcaption&gt;Figure 1: S&amp;P 500 quarterly performance&lt;/figcaption&gt;\n'
        '&lt;/figure&gt;',
        filename="Images and Media",
        styles=styles
    ))

    # 2.6 LISTS
    story.append(h1("2.6 Lists", styles))
    story.append(code_block(
        '&lt;!-- Unordered list (bullets) --&gt;\n'
        '&lt;ul&gt;\n'
        '  &lt;li&gt;Apple (AAPL)&lt;/li&gt;\n'
        '  &lt;li&gt;Microsoft (MSFT)&lt;/li&gt;\n'
        '  &lt;li&gt;Google (GOOGL)&lt;/li&gt;\n'
        '&lt;/ul&gt;\n\n'
        '&lt;!-- Ordered list (numbered) --&gt;\n'
        '&lt;ol&gt;\n'
        '  &lt;li&gt;Open a brokerage account&lt;/li&gt;\n'
        '  &lt;li&gt;Fund the account&lt;/li&gt;\n'
        '  &lt;li&gt;Research stocks&lt;/li&gt;\n'
        '  &lt;li&gt;Place your first trade&lt;/li&gt;\n'
        '&lt;/ol&gt;\n\n'
        '&lt;!-- Description list --&gt;\n'
        '&lt;dl&gt;\n'
        '  &lt;dt&gt;P/E Ratio&lt;/dt&gt;\n'
        '  &lt;dd&gt;Price-to-Earnings ratio. Stock price divided by earnings per share.&lt;/dd&gt;\n'
        '  &lt;dt&gt;Market Cap&lt;/dt&gt;\n'
        '  &lt;dd&gt;Total market value of outstanding shares.&lt;/dd&gt;\n'
        '&lt;/dl&gt;',
        filename="List Types",
        styles=styles
    ))

    # 2.7 TABLES
    story.append(h1("2.7 Tables", styles))

    story.append(analogy_box(
        "A table is a spreadsheet embedded in your page. &lt;thead&gt; is the header row with column "
        "names. &lt;tbody&gt; is all the data rows. &lt;tfoot&gt; is the totals row at the bottom."
    , styles))

    story.append(code_block(
        '&lt;table&gt;\n'
        '  &lt;caption&gt;Watchlist - Top Holdings&lt;/caption&gt;\n'
        '  &lt;thead&gt;\n'
        '    &lt;tr&gt;\n'
        '      &lt;th scope="col"&gt;Ticker&lt;/th&gt;\n'
        '      &lt;th scope="col"&gt;Company&lt;/th&gt;\n'
        '      &lt;th scope="col"&gt;Price&lt;/th&gt;\n'
        '      &lt;th scope="col"&gt;Change&lt;/th&gt;\n'
        '      &lt;th scope="col"&gt;Change %&lt;/th&gt;\n'
        '    &lt;/tr&gt;\n'
        '  &lt;/thead&gt;\n'
        '  &lt;tbody&gt;\n'
        '    &lt;tr&gt;\n'
        '      &lt;td&gt;AAPL&lt;/td&gt;\n'
        '      &lt;td&gt;Apple Inc.&lt;/td&gt;\n'
        '      &lt;td&gt;$178.52&lt;/td&gt;\n'
        '      &lt;td&gt;+$2.34&lt;/td&gt;\n'
        '      &lt;td&gt;+1.33%&lt;/td&gt;\n'
        '    &lt;/tr&gt;\n'
        '    &lt;tr&gt;\n'
        '      &lt;td&gt;MSFT&lt;/td&gt;\n'
        '      &lt;td&gt;Microsoft Corp.&lt;/td&gt;\n'
        '      &lt;td&gt;$415.20&lt;/td&gt;\n'
        '      &lt;td&gt;-$3.10&lt;/td&gt;\n'
        '      &lt;td&gt;-0.74%&lt;/td&gt;\n'
        '    &lt;/tr&gt;\n'
        '    &lt;tr&gt;\n'
        '      &lt;td&gt;GOOGL&lt;/td&gt;\n'
        '      &lt;td&gt;Alphabet Inc.&lt;/td&gt;\n'
        '      &lt;td&gt;$174.85&lt;/td&gt;\n'
        '      &lt;td&gt;+$1.20&lt;/td&gt;\n'
        '      &lt;td&gt;+0.69%&lt;/td&gt;\n'
        '    &lt;/tr&gt;\n'
        '  &lt;/tbody&gt;\n'
        '  &lt;tfoot&gt;\n'
        '    &lt;tr&gt;\n'
        '      &lt;th scope="row" colspan="2"&gt;Portfolio Average&lt;/th&gt;\n'
        '      &lt;td&gt;-&lt;/td&gt;\n'
        '      &lt;td&gt;+$0.15&lt;/td&gt;\n'
        '      &lt;td&gt;+0.43%&lt;/td&gt;\n'
        '    &lt;/tr&gt;\n'
        '  &lt;/tfoot&gt;\n'
        '&lt;/table&gt;',
        filename="TradeBoard Stock Table",
        styles=styles
    ))

    story.append(principal_box(
        "Tables are for DATA, never for layout. Use CSS Grid and Flexbox for layout. "
        "The scope attribute on th elements is critical for screen readers — it tells them "
        "whether a header applies to a column or row. Always include caption for context."
    , styles))

    # 2.8 FORMS
    story.append(h1("2.8 Forms — The Gateway to User Input", styles))

    story.append(analogy_box(
        "A form is like a paper application form at a government office. Each input field is a blank "
        "line. The submit button is handing the form to the clerk. The clerk (server) reads each "
        "field by its label (the name attribute) and processes the information."
    , styles))

    story.append(code_block(
        '&lt;form action="/api/search" method="GET"&gt;\n'
        '  &lt;fieldset&gt;\n'
        '    &lt;legend&gt;Search Stocks&lt;/legend&gt;\n\n'
        '    &lt;div&gt;\n'
        '      &lt;label for="ticker"&gt;Ticker Symbol&lt;/label&gt;\n'
        '      &lt;input type="text" id="ticker" name="ticker"\n'
        '             placeholder="e.g., AAPL" required\n'
        '             pattern="[A-Z]{1,5}" title="1-5 uppercase letters"\n'
        '             maxlength="5" /&gt;\n'
        '    &lt;/div&gt;\n\n'
        '    &lt;div&gt;\n'
        '      &lt;label for="exchange"&gt;Exchange&lt;/label&gt;\n'
        '      &lt;select id="exchange" name="exchange"&gt;\n'
        '        &lt;option value=""&gt;All Exchanges&lt;/option&gt;\n'
        '        &lt;optgroup label="United States"&gt;\n'
        '          &lt;option value="NYSE"&gt;NYSE&lt;/option&gt;\n'
        '          &lt;option value="NASDAQ"&gt;NASDAQ&lt;/option&gt;\n'
        '        &lt;/optgroup&gt;\n'
        '        &lt;optgroup label="International"&gt;\n'
        '          &lt;option value="LSE"&gt;London (LSE)&lt;/option&gt;\n'
        '          &lt;option value="TSE"&gt;Tokyo (TSE)&lt;/option&gt;\n'
        '        &lt;/optgroup&gt;\n'
        '      &lt;/select&gt;\n'
        '    &lt;/div&gt;\n\n'
        '    &lt;div&gt;\n'
        '      &lt;label for="date-from"&gt;Date From&lt;/label&gt;\n'
        '      &lt;input type="date" id="date-from" name="dateFrom" /&gt;\n'
        '    &lt;/div&gt;\n\n'
        '    &lt;fieldset&gt;\n'
        '      &lt;legend&gt;Filters&lt;/legend&gt;\n'
        '      &lt;label&gt;\n'
        '        &lt;input type="checkbox" name="filters" value="gainers" /&gt;\n'
        '        Top Gainers Only\n'
        '      &lt;/label&gt;\n'
        '      &lt;label&gt;\n'
        '        &lt;input type="checkbox" name="filters" value="dividend" /&gt;\n'
        '        Dividend Paying\n'
        '      &lt;/label&gt;\n'
        '    &lt;/fieldset&gt;\n\n'
        '    &lt;div&gt;\n'
        '      &lt;label for="min-price"&gt;Min Price ($)&lt;/label&gt;\n'
        '      &lt;input type="number" id="min-price" name="minPrice"\n'
        '             min="0" max="100000" step="0.01" /&gt;\n'
        '    &lt;/div&gt;\n\n'
        '    &lt;button type="submit"&gt;Search&lt;/button&gt;\n'
        '    &lt;button type="reset"&gt;Clear&lt;/button&gt;\n'
        '  &lt;/fieldset&gt;\n'
        '&lt;/form&gt;',
        filename="TradeBoard Stock Search Form",
        styles=styles
    ))

    story.append(p("Key form concepts:", styles))
    story.append(bullet("<b>action</b> — URL where form data is sent", styles))
    story.append(bullet("<b>method</b> — GET for searches (data in URL), POST for submissions (data in body)", styles))
    story.append(bullet("<b>name</b> — How the server identifies each field. Without name, data is NOT sent", styles))
    story.append(bullet("<b>label</b> — ALWAYS associate labels with inputs via for/id. Legal accessibility requirement.", styles))
    story.append(bullet("<b>required</b> — Browser prevents submission if empty", styles))
    story.append(bullet("<b>pattern</b> — Regex validation on the client side", styles))

    story.append(mistake_box(
        "The #1 form mistake: forgetting the name attribute on inputs. Without name, the server "
        "receives nothing from that field. Your form looks like it works, but data is silently lost."
    , styles))

    # 2.9 SEMANTIC HTML
    story.append(h1("2.9 Semantic HTML", styles))

    story.append(analogy_box(
        "Semantic HTML is like labeling rooms in a house. You could put a bed in any room, but "
        "labeling one 'bedroom' helps the real estate agent (search engine), building inspector "
        "(accessibility tools), and future renovators (other developers) understand your house."
    , styles))

    story.append(code_block(
        '&lt;body&gt;\n'
        '  &lt;a href="#main" class="skip-link"&gt;Skip to content&lt;/a&gt;\n\n'
        '  &lt;header&gt;\n'
        '    &lt;h1&gt;TradeBoard&lt;/h1&gt;\n'
        '    &lt;nav aria-label="Main navigation"&gt;\n'
        '      &lt;ul&gt;\n'
        '        &lt;li&gt;&lt;a href="/"&gt;Dashboard&lt;/a&gt;&lt;/li&gt;\n'
        '        &lt;li&gt;&lt;a href="/watchlist"&gt;Watchlist&lt;/a&gt;&lt;/li&gt;\n'
        '        &lt;li&gt;&lt;a href="/stocks"&gt;Stocks&lt;/a&gt;&lt;/li&gt;\n'
        '        &lt;li&gt;&lt;a href="/settings"&gt;Settings&lt;/a&gt;&lt;/li&gt;\n'
        '      &lt;/ul&gt;\n'
        '    &lt;/nav&gt;\n'
        '  &lt;/header&gt;\n\n'
        '  &lt;main id="main"&gt;\n'
        '    &lt;section aria-labelledby="market-heading"&gt;\n'
        '      &lt;h2 id="market-heading"&gt;Market Overview&lt;/h2&gt;\n'
        '      &lt;article&gt;\n'
        '        &lt;h3&gt;S&amp;P 500&lt;/h3&gt;\n'
        '        &lt;p&gt;Current: 5,234.18 (+0.82%)&lt;/p&gt;\n'
        '      &lt;/article&gt;\n'
        '    &lt;/section&gt;\n\n'
        '    &lt;section aria-labelledby="watchlist-heading"&gt;\n'
        '      &lt;h2 id="watchlist-heading"&gt;Your Watchlist&lt;/h2&gt;\n'
        '      &lt;!-- Stock table here --&gt;\n'
        '    &lt;/section&gt;\n'
        '  &lt;/main&gt;\n\n'
        '  &lt;aside aria-label="Market news"&gt;\n'
        '    &lt;h2&gt;Latest News&lt;/h2&gt;\n'
        '    &lt;article&gt;\n'
        '      &lt;h3&gt;Fed Holds Rates Steady&lt;/h3&gt;\n'
        '      &lt;p&gt;&lt;time datetime="2025-12-18"&gt;Dec 18, 2025&lt;/time&gt;&lt;/p&gt;\n'
        '    &lt;/article&gt;\n'
        '  &lt;/aside&gt;\n\n'
        '  &lt;footer&gt;\n'
        '    &lt;p&gt;Data for educational purposes only. &copy; 2025 TradeBoard&lt;/p&gt;\n'
        '  &lt;/footer&gt;\n'
        '&lt;/body&gt;',
        filename="TradeBoard - Complete Semantic HTML Structure",
        styles=styles
    ))

    story.append(p("Semantic elements:", styles))
    story.append(bullet("<b>&lt;header&gt;</b> — Introductory content, logo, nav", styles))
    story.append(bullet("<b>&lt;nav&gt;</b> — Major navigation blocks only", styles))
    story.append(bullet("<b>&lt;main&gt;</b> — Dominant content. Only ONE per page.", styles))
    story.append(bullet("<b>&lt;section&gt;</b> — Thematic grouping with a heading", styles))
    story.append(bullet("<b>&lt;article&gt;</b> — Self-contained content (blog post, stock card)", styles))
    story.append(bullet("<b>&lt;aside&gt;</b> — Tangentially related content (sidebars)", styles))
    story.append(bullet("<b>&lt;footer&gt;</b> — Footer: copyright, links, contact", styles))

    # 2.10 HTML BEST PRACTICES
    story.append(h1("2.10 HTML Best Practices at Principal Engineer Level", styles))

    story.append(principal_box(
        "At Principal Engineer level, HTML is the foundation of accessibility, SEO, and DX. "
        "Review HTML for: correct heading hierarchy, semantic elements, ARIA attributes, form "
        "accessibility, alt text quality, and document outline. Establish standards and integrate "
        "automated accessibility testing (axe-core, pa11y) into CI/CD."
    , styles))

    story.append(bullet("<b>Validate HTML</b> — Use the W3C Validator. Invalid HTML causes unpredictable rendering.", styles))
    story.append(bullet("<b>Minimize DOM depth</b> — Deep nesting slows CSS matching and layout. Avoid div soup.", styles))
    story.append(bullet("<b>Use Lighthouse</b> — Audit accessibility, SEO, best practices. Aim for 100 on accessibility.", styles))
    story.append(bullet("<b>Test with screen readers</b> — VoiceOver (Mac), NVDA (Windows). If it does not make sense read aloud, fix it.", styles))
    story.append(bullet("<b>First Rule of ARIA</b> — Do not use ARIA if a native HTML element exists. Native elements have built-in accessibility.", styles))

    # EXERCISES
    story.append(spacer(12))
    story.append(h1("Chapter 2 Exercises", styles))
    story.append(HorizontalLine())
    story.append(spacer(8))

    story.append(exercise(1, "Build the TradeBoard HTML Structure", [
        ('ExerciseBody', '<b>Requirements:</b> Create a complete HTML5 document for TradeBoard. Include: header with nav (Dashboard, Watchlist, Stocks, Settings), main content with a stock table (5+ stocks), sidebar with watchlist summary, footer. Use only semantic elements.'),
        ('ExerciseBody', '<b>Hint:</b> Start with the boilerplate from 2.2, add structure from 2.9.'),
        ('ExerciseBody', '<b>Level Up:</b> Add the stock search form from 2.8 and validate at validator.w3.org.'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(2, "Build a Complete Stock Search Form", [
        ('ExerciseBody', '<b>Requirements:</b> Text input for ticker (required, uppercase pattern), select for exchange with optgroups, date pickers, checkboxes for filters, number input for min price, submit/reset buttons. All with labels and validation.'),
        ('ExerciseBody', '<b>Solution:</b> See section 2.8 for the complete implementation.'),
        ('ExerciseBody', '<b>Level Up:</b> Add textarea for notes, radio group for sort order, range slider for risk tolerance.'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(3, "Create an Accessible Stock Data Table", [
        ('ExerciseBody', '<b>Requirements:</b> Table with 10 stocks. Include: caption, thead with scope="col", tbody, tfoot with totals. Columns: Ticker, Company, Sector, Price, Day Change, Change %, Volume, Market Cap.'),
        ('ExerciseBody', '<b>Hint:</b> Use scope="row" on ticker cells in tbody since they act as row headers.'),
        ('ExerciseBody', '<b>Level Up:</b> Test with a screen reader. Does the table make sense when read aloud?'),
    ], styles))

    story.append(spacer(16))
    story.append(checkpoint("You can build semantic, accessible HTML. TradeBoard has a solid skeleton. Time to make it beautiful with CSS.", styles))
    story.append(page_break())

    return story
