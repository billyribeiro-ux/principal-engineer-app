"""Chapter 8: GSAP — Animation that Inspires"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_8(styles):
    story = []

    story.append(ChapterCoverPage(8, "GSAP \u2014 Animation that Inspires",
                                  "Choreographing the Ballet of the Web", "PART 2: LEVELING UP"))
    story.append(PageBreak())

    # ================================================================
    # 8.1 WHY GSAP?
    # ================================================================
    story.append(h1("8.1 Why GSAP?", styles))
    story.append(analogy_box(
        "CSS animations are like a music box \u2014 they play one tune, and it is pretty, but you cannot "
        "change the tempo mid-song, pause it, reverse it, or coordinate multiple music boxes. GSAP "
        "(GreenSock Animation Platform) is a full orchestra conductor. It can coordinate dozens of "
        "instruments (elements), control timing down to the millisecond, change direction on cue, "
        "and create performances that would be impossible with music boxes alone."
    , styles))

    story.append(p(
        "GSAP is the industry-standard JavaScript animation library used by companies like Google, "
        "Apple, Nike, and NASA. It provides sub-pixel precision, high performance across browsers, "
        "and an API that makes complex animations manageable."
    , styles))

    story.append(p("Why GSAP over CSS animations:", styles))
    story.append(bullet("<b>Timeline control</b> \u2014 Sequence, stagger, overlap, and reverse animations with precision.", styles))
    story.append(bullet("<b>ScrollTrigger</b> \u2014 Trigger animations based on scroll position with pinning and scrubbing.", styles))
    story.append(bullet("<b>Performance</b> \u2014 Optimized for 60fps, GPU-accelerated, handles thousands of elements.", styles))
    story.append(bullet("<b>Cross-browser</b> \u2014 Works identically in every browser, even older ones.", styles))
    story.append(bullet("<b>Svelte integration</b> \u2014 Works beautifully with Svelte 5's <code>$effect</code> and lifecycle.", styles))

    story.append(h2("Installation and Setup", styles))
    story.append(code_block(
        '# Install GSAP in your SvelteKit project\n'
        'npm install gsap\n\n'
        '# GSAP modules you will use:\n'
        '# gsap          - Core animation engine\n'
        '# ScrollTrigger  - Scroll-based animations\n'
        '# Flip           - Layout transition animations\n'
        '# Draggable      - Drag interactions\n\n'
        '// Import in your Svelte component\n'
        'import gsap from "gsap";\n'
        'import { ScrollTrigger } from "gsap/ScrollTrigger";\n\n'
        '// Register plugins\n'
        'gsap.registerPlugin(ScrollTrigger);',
        filename="GSAP Installation", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You understand why GSAP exists and how to install it.", styles))
    story.append(page_break())

    # ================================================================
    # 8.2 GSAP FUNDAMENTALS
    # ================================================================
    story.append(h1("8.2 GSAP Fundamentals", styles))

    story.append(h2("The Three Core Methods", styles))
    story.append(code_block(
        '// gsap.to() - Animate FROM current state TO target\n'
        'gsap.to(".stock-card", {\n'
        '  x: 100,           // Move 100px right\n'
        '  opacity: 0.5,     // Fade to 50%\n'
        '  scale: 1.2,       // Scale up 120%\n'
        '  duration: 0.8,    // Over 0.8 seconds\n'
        '  ease: "power2.out" // Easing function\n'
        '});\n\n'
        '// gsap.from() - Animate FROM target TO current state\n'
        '// Great for "entrance" animations\n'
        'gsap.from(".stock-card", {\n'
        '  y: 50,            // Start 50px below\n'
        '  opacity: 0,       // Start invisible\n'
        '  duration: 0.6,\n'
        '  ease: "back.out(1.7)" // Overshoot easing\n'
        '});\n\n'
        '// gsap.fromTo() - Control both start AND end\n'
        'gsap.fromTo(".progress-bar",\n'
        '  { width: "0%" },      // FROM\n'
        '  { width: "100%",      // TO\n'
        '    duration: 2,\n'
        '    ease: "none"        // Linear (no easing)\n'
        '  }\n'
        ');',
        filename="gsap.to(), gsap.from(), gsap.fromTo()", styles=styles
    ))

    story.append(h2("Properties You Can Animate", styles))
    story.append(bullet("<b>Position:</b> x, y, xPercent, yPercent, top, left, right, bottom", styles))
    story.append(bullet("<b>Scale:</b> scale, scaleX, scaleY", styles))
    story.append(bullet("<b>Rotation:</b> rotation, rotationX, rotationY (degrees)", styles))
    story.append(bullet("<b>Opacity:</b> opacity (0 to 1), autoAlpha (opacity + visibility)", styles))
    story.append(bullet("<b>Size:</b> width, height, padding, margin, borderRadius", styles))
    story.append(bullet("<b>Color:</b> color, backgroundColor, borderColor", styles))
    story.append(bullet("<b>Transform origin:</b> transformOrigin ('50% 50%', 'top left')", styles))

    story.append(h2("Easing Functions", styles))
    story.append(p(
        "Easing controls the rate of change during an animation. Linear animations feel robotic. "
        "Good easing makes animations feel natural and alive."
    , styles))

    story.append(code_block(
        '// Easing types (each has .in, .out, .inOut variants)\n'
        '// "power1.out"  - Subtle deceleration (default-ish)\n'
        '// "power2.out"  - More noticeable deceleration\n'
        '// "power3.out"  - Strong deceleration\n'
        '// "power4.out"  - Very strong deceleration\n'
        '// "back.out(1.7)" - Overshoots then settles\n'
        '// "elastic.out(1, 0.3)" - Bouncy spring effect\n'
        '// "bounce.out"  - Bounces at the end\n'
        '// "none"        - Linear (constant speed)\n\n'
        '// .in = starts slow, ends fast (accelerating)\n'
        '// .out = starts fast, ends slow (decelerating)\n'
        '// .inOut = slow-fast-slow (smooth both ends)\n\n'
        '// Principal Engineer rule:\n'
        '// UI entrances: use .out (decelerate into position)\n'
        '// UI exits: use .in (accelerate away)\n'
        '// Continuous: use .inOut (smooth throughout)',
        filename="Easing Functions", styles=styles
    ))

    story.append(h2("Stagger Animations", styles))
    story.append(code_block(
        '// Stagger - animate multiple elements with a delay between each\n'
        'gsap.from(".watchlist-item", {\n'
        '  y: 30,\n'
        '  opacity: 0,\n'
        '  duration: 0.5,\n'
        '  stagger: 0.1,       // 0.1s delay between each item\n'
        '  ease: "power2.out"\n'
        '});\n\n'
        '// Advanced stagger\n'
        'gsap.from(".grid-item", {\n'
        '  scale: 0,\n'
        '  opacity: 0,\n'
        '  duration: 0.6,\n'
        '  stagger: {\n'
        '    each: 0.08,       // Delay between each\n'
        '    from: "center",   // Start from center outward\n'
        '    grid: "auto",     // Stagger in 2D grid pattern\n'
        '    ease: "power1.in" // Easing of the stagger itself\n'
        '  }\n'
        '});',
        filename="Stagger Animations", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can use gsap.to/from/fromTo, easing, and stagger animations.", styles))
    story.append(page_break())

    # ================================================================
    # 8.3 TIMELINES
    # ================================================================
    story.append(h1("8.3 Timelines", styles))
    story.append(analogy_box(
        "A timeline is like a choreography sheet for a ballet. Instead of telling each dancer to start "
        "independently, the choreographer writes a sequence: 'Dancer A enters from left, then Dancer B "
        "spins, then both leap together.' A GSAP timeline sequences animations, coordinates them, and "
        "lets you control the entire performance as one unit \u2014 play, pause, reverse, speed up, or jump "
        "to any point."
    , styles))

    story.append(code_block(
        '// Create a timeline\n'
        'const tl = gsap.timeline({\n'
        '  defaults: { duration: 0.5, ease: "power2.out" }\n'
        '});\n\n'
        '// Chain animations - each waits for the previous\n'
        'tl.from(".header", { y: -50, opacity: 0 })\n'
        '  .from(".sidebar", { x: -200, opacity: 0 })\n'
        '  .from(".main-content", { opacity: 0 })\n'
        '  .from(".stock-cards", { y: 30, opacity: 0, stagger: 0.1 });\n\n'
        '// Position parameter - control timing precisely\n'
        'tl.from(".header", { y: -50, opacity: 0 })           // starts at 0s\n'
        '  .from(".sidebar", { x: -200, opacity: 0 }, "-=0.3") // overlap by 0.3s\n'
        '  .from(".content", { opacity: 0 }, "<")              // same start as prev\n'
        '  .from(".footer", { y: 50 }, "+=0.5")               // 0.5s gap after prev\n'
        '  .from(".cta", { scale: 0 }, 1.5);                  // absolute: at 1.5s\n\n'
        '// Timeline controls\n'
        'tl.play();      // Play forward\n'
        'tl.pause();     // Pause\n'
        'tl.reverse();   // Play backward\n'
        'tl.restart();   // Jump to start and play\n'
        'tl.progress(0.5); // Jump to 50%\n'
        'tl.timeScale(2);  // Double speed',
        filename="Timeline Basics", styles=styles
    ))

    story.append(h2("Dashboard Load Animation", styles))
    story.append(code_block(
        '// Real-world example: TradeBoard dashboard entrance\n'
        'function animateDashboardEntry() {\n'
        '  const tl = gsap.timeline({\n'
        '    defaults: { ease: "power3.out" }\n'
        '  });\n\n'
        '  tl\n'
        '    // 1. Header slides down\n'
        '    .from(".nav-bar", { y: -60, opacity: 0, duration: 0.6 })\n'
        '    // 2. Sidebar slides in (overlaps header by 0.2s)\n'
        '    .from(".sidebar", { x: -250, opacity: 0, duration: 0.5 }, "-=0.2")\n'
        '    // 3. Summary cards stagger in\n'
        '    .from(".summary-card", {\n'
        '      y: 40, opacity: 0, duration: 0.5,\n'
        '      stagger: 0.08\n'
        '    }, "-=0.3")\n'
        '    // 4. Chart draws in\n'
        '    .from(".chart-container", {\n'
        '      opacity: 0, scale: 0.95, duration: 0.6\n'
        '    }, "-=0.2")\n'
        '    // 5. Watchlist items cascade\n'
        '    .from(".watchlist-row", {\n'
        '      x: 30, opacity: 0, duration: 0.4,\n'
        '      stagger: 0.05\n'
        '    }, "-=0.3");\n\n'
        '  return tl;\n'
        '}',
        filename="Dashboard Animation", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can build complex, coordinated timeline animations.", styles))
    story.append(page_break())

    # ================================================================
    # 8.4 SCROLLTRIGGER
    # ================================================================
    story.append(h1("8.4 ScrollTrigger", styles))
    story.append(p(
        "ScrollTrigger connects animations to scroll position. Elements can animate into view as the "
        "user scrolls, pin in place, or scrub through an animation based on scroll progress."
    , styles))

    story.append(code_block(
        'import { ScrollTrigger } from "gsap/ScrollTrigger";\n'
        'gsap.registerPlugin(ScrollTrigger);\n\n'
        '// Basic: animate when element enters viewport\n'
        'gsap.from(".feature-section", {\n'
        '  y: 60,\n'
        '  opacity: 0,\n'
        '  duration: 0.8,\n'
        '  scrollTrigger: {\n'
        '    trigger: ".feature-section",  // Element that triggers\n'
        '    start: "top 80%",    // When top of trigger hits 80% of viewport\n'
        '    end: "bottom 20%",   // When bottom hits 20% of viewport\n'
        '    toggleActions: "play none none reverse"\n'
        '    // onEnter, onLeave, onEnterBack, onLeaveBack\n'
        '  }\n'
        '});\n\n'
        '// Scrub: animation progress tied to scroll position\n'
        'gsap.to(".progress-indicator", {\n'
        '  width: "100%",\n'
        '  ease: "none",\n'
        '  scrollTrigger: {\n'
        '    trigger: ".article",\n'
        '    start: "top top",\n'
        '    end: "bottom bottom",\n'
        '    scrub: true  // Smooth scrubbing\n'
        '  }\n'
        '});\n\n'
        '// Pin: element sticks while scroll animation plays\n'
        'gsap.to(".hero-text", {\n'
        '  x: -500,\n'
        '  scrollTrigger: {\n'
        '    trigger: ".hero-section",\n'
        '    start: "top top",\n'
        '    end: "+=1000",    // Pin for 1000px of scrolling\n'
        '    pin: true,        // Pin the trigger element\n'
        '    scrub: 1          // Smooth scrub with 1s lag\n'
        '  }\n'
        '});',
        filename="ScrollTrigger", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can trigger, scrub, and pin animations based on scroll position.", styles))
    story.append(page_break())

    # ================================================================
    # 8.5 GSAP + SVELTE 5
    # ================================================================
    story.append(h1("8.5 GSAP with Svelte 5", styles))
    story.append(p(
        "The key to using GSAP in Svelte 5 is the <code>$effect</code> rune. Use it to create animations "
        "when the component mounts, and return a cleanup function to kill animations when the component "
        "unmounts. Always use <code>gsap.context()</code> for cleanup."
    , styles))

    story.append(code_block(
        '<!-- AnimatedStockCard.svelte -->\n'
        '<script lang="ts">\n'
        '  import gsap from "gsap";\n'
        '  import type { Stock } from "$lib/types";\n\n'
        '  let { stock }: { stock: Stock } = $props();\n'
        '  let cardEl: HTMLElement;\n\n'
        '  // Create animation on mount, clean up on unmount\n'
        '  $effect(() => {\n'
        '    const ctx = gsap.context(() => {\n'
        '      // Entrance animation\n'
        '      gsap.from(cardEl, {\n'
        '        y: 30,\n'
        '        opacity: 0,\n'
        '        duration: 0.5,\n'
        '        ease: "power2.out"\n'
        '      });\n\n'
        '      // Hover animation\n'
        '      cardEl.addEventListener("mouseenter", () => {\n'
        '        gsap.to(cardEl, { scale: 1.02, duration: 0.2 });\n'
        '      });\n'
        '      cardEl.addEventListener("mouseleave", () => {\n'
        '        gsap.to(cardEl, { scale: 1, duration: 0.2 });\n'
        '      });\n'
        '    });\n\n'
        '    // Cleanup: kill all animations in this context\n'
        '    return () => ctx.revert();\n'
        '  });\n'
        '</script>\n\n'
        '<div bind:this={cardEl} class="stock-card">\n'
        '  <h3>{stock.ticker}</h3>\n'
        '  <p>${stock.price.toFixed(2)}</p>\n'
        '</div>',
        filename="GSAP + Svelte 5", styles=styles
    ))

    story.append(h2("Reactive Animations", styles))
    story.append(code_block(
        '<!-- PriceDisplay.svelte -->\n'
        '<script lang="ts">\n'
        '  import gsap from "gsap";\n\n'
        '  let { price }: { price: number } = $props();\n'
        '  let displayEl: HTMLElement;\n'
        '  let prevPrice = price;\n\n'
        '  // React to price changes with animation\n'
        '  $effect(() => {\n'
        '    if (price !== prevPrice) {\n'
        '      const color = price > prevPrice ? "#22c55e" : "#ef4444";\n\n'
        '      gsap.fromTo(displayEl,\n'
        '        { color, scale: 1.1 },\n'
        '        { color: "inherit", scale: 1, duration: 0.5 }\n'
        '      );\n\n'
        '      prevPrice = price;\n'
        '    }\n'
        '  });\n'
        '</script>\n\n'
        '<span bind:this={displayEl}>${price.toFixed(2)}</span>',
        filename="Reactive GSAP Animations", styles=styles
    ))

    story.append(mistake_box(
        "Always clean up GSAP animations when a Svelte component unmounts. Without cleanup, animations "
        "targeting removed elements cause memory leaks and errors. Use <code>gsap.context()</code> and "
        "call <code>ctx.revert()</code> in the <code>$effect</code> cleanup function. This kills all "
        "animations and ScrollTriggers created within that context."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You can integrate GSAP with Svelte 5 using $effect and gsap.context().", styles))
    story.append(page_break())

    # ================================================================
    # 8.6 ADVANCED TECHNIQUES
    # ================================================================
    story.append(h1("8.6 Advanced GSAP Techniques", styles))

    story.append(h2("The Flip Plugin", styles))
    story.append(code_block(
        '// FLIP = First, Last, Invert, Play\n'
        '// Animates layout changes smoothly\n'
        'import { Flip } from "gsap/Flip";\n'
        'gsap.registerPlugin(Flip);\n\n'
        '// Example: reorder a stock watchlist\n'
        'function reorderWatchlist(newOrder: string[]) {\n'
        '  // 1. Record current positions\n'
        '  const state = Flip.getState(".watchlist-item");\n\n'
        '  // 2. Reorder the DOM (Svelte reactive update)\n'
        '  stocks = newOrder.map(t => stocks.find(s => s.ticker === t)!);\n\n'
        '  // 3. Animate from old positions to new positions\n'
        '  Flip.from(state, {\n'
        '    duration: 0.5,\n'
        '    ease: "power2.inOut",\n'
        '    stagger: 0.05,\n'
        '    absolute: true,  // Position absolutely during animation\n'
        '    onComplete: () => console.log("Reorder complete")\n'
        '  });\n'
        '}',
        filename="Flip Plugin", styles=styles
    ))

    story.append(h2("Number Counter Animation", styles))
    story.append(code_block(
        '// Animate numbers counting up (great for dashboards)\n'
        'function animateCounter(element: HTMLElement, target: number) {\n'
        '  const counter = { value: 0 };\n\n'
        '  gsap.to(counter, {\n'
        '    value: target,\n'
        '    duration: 2,\n'
        '    ease: "power2.out",\n'
        '    onUpdate: () => {\n'
        '      element.textContent = "$" + counter.value.toLocaleString(\n'
        '        "en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }\n'
        '      );\n'
        '    }\n'
        '  });\n'
        '}\n\n'
        '// Usage: animateCounter(portfolioValueEl, 145_832.47);',
        filename="Counter Animation", styles=styles
    ))

    story.append(h2("PE: Animation Design System", styles))
    story.append(code_block(
        '// src/lib/animation/tokens.ts\n'
        '// Animation design tokens - consistent across the app\n\n'
        'export const DURATIONS = {\n'
        '  instant: 0.1,\n'
        '  fast: 0.2,\n'
        '  normal: 0.4,\n'
        '  slow: 0.6,\n'
        '  dramatic: 1.0\n'
        '} as const;\n\n'
        'export const EASINGS = {\n'
        '  enter: "power2.out",\n'
        '  exit: "power2.in",\n'
        '  move: "power2.inOut",\n'
        '  bounce: "back.out(1.7)",\n'
        '  spring: "elastic.out(1, 0.5)"\n'
        '} as const;\n\n'
        'export const STAGGERS = {\n'
        '  fast: 0.03,\n'
        '  normal: 0.06,\n'
        '  slow: 0.1\n'
        '} as const;\n\n'
        '// Reusable animation presets\n'
        'export const fadeIn = {\n'
        '  from: { opacity: 0, y: 20 },\n'
        '  config: { duration: DURATIONS.normal, ease: EASINGS.enter }\n'
        '};\n\n'
        'export const slideInLeft = {\n'
        '  from: { opacity: 0, x: -40 },\n'
        '  config: { duration: DURATIONS.normal, ease: EASINGS.enter }\n'
        '};',
        filename="Animation Design Tokens", styles=styles
    ))

    story.append(principal_box(
        "Create animation tokens just like you create design tokens for colors and spacing. Consistent "
        "animation durations and easings across your app create a polished, professional feel. Random "
        "durations and easings feel chaotic. Document your animation system: entrances use 'enter' "
        "easing, exits use 'exit' easing, and duration scales with element importance."
    , styles))

    story.append(spacer(16))

    # ================================================================
    # EXERCISES
    # ================================================================
    story.append(h1("Chapter 8 Exercises", styles))
    story.append(HorizontalLine())
    story.append(spacer(8))

    story.append(exercise(1, "Animated Stock Card", [
        ('ExerciseBody', '<b>Task:</b> Create a StockCard Svelte component that animates in when it '
         'mounts using gsap.from() with y offset and opacity. Add a hover animation that scales the '
         'card slightly. When the price prop changes, flash the price green (up) or red (down). '
         'Use gsap.context() for cleanup.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(2, "Dashboard Load Timeline", [
        ('ExerciseBody', '<b>Task:</b> Build a timeline that animates the TradeBoard dashboard entrance. '
         'Sequence: header slides down, sidebar slides in from left (overlapping), summary cards stagger '
         'in from below, chart fades in, and watchlist rows cascade in. Use position parameters (<, '
         '-=0.3, etc.) for overlap. Total animation should be under 2 seconds.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(3, "ScrollTrigger Landing Page", [
        ('ExerciseBody', '<b>Task:</b> Create a landing page with three feature sections. Each section '
         'should animate in when scrolled into view using ScrollTrigger. Add a progress bar that shows '
         'reading progress (scrubbed). Pin the hero section for 500px of scrolling while a headline '
         'types out. Use toggleActions to reverse animations when scrolling back up.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(4, "Animated Counter Dashboard", [
        ('ExerciseBody', '<b>Task:</b> Create a dashboard summary section with four metric cards: '
         'portfolio value ($), daily change (%), total trades (integer), and best performer (ticker). '
         'Animate the numbers counting up from zero when the component mounts. Use stagger for the '
         'cards. Format numbers appropriately (currency, percentage, integer).'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(5, "Animation Design System", [
        ('ExerciseBody', '<b>Task:</b> Create a complete animation design system for TradeBoard. Define '
         'animation tokens (durations, easings, staggers) in a tokens file. Create reusable Svelte '
         'actions (use:fadeIn, use:slideIn, use:staggerChildren) that apply consistent animations. '
         'Add prefers-reduced-motion support that disables animations for users who prefer it.'),
    ], styles))

    story.append(spacer(16))
    story.append(checkpoint("You have mastered GSAP: fundamentals, timelines, ScrollTrigger, Svelte 5 "
                           "integration, Flip animations, and animation design systems.", styles))
    story.append(page_break())

    return story
