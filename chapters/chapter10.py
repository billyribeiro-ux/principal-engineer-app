"""Chapter 10: Capstone Project — Production TradeBoard"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_10(styles):
    story = []

    story.append(ChapterCoverPage(10, "Capstone Project \u2014 Production TradeBoard",
                                  "Building Your City from the Ground Up", "PART 3: PRINCIPAL ENGINEER"))
    story.append(PageBreak())

    # ================================================================
    # 10.1 PROJECT OVERVIEW
    # ================================================================
    story.append(h1("10.1 The TradeBoard Project", styles))
    story.append(analogy_box(
        "Throughout this course, we have learned to lay foundations (HTML), paint walls (CSS), wire "
        "electricity (JavaScript), label circuit breakers (TypeScript), build with prefab modules "
        "(Svelte 5), plan the city (SvelteKit), choreograph the grand opening (GSAP), and design for "
        "scale (Architecture). Now it is time to build the entire city from the ground up. TradeBoard "
        "is your capstone project \u2014 a production-grade stock watchlist dashboard that combines every "
        "skill you have learned."
    , styles))

    story.append(p(
        "TradeBoard is a real-time stock watchlist and trading dashboard. Users can search for stocks, "
        "build watchlists, view price charts, and track their portfolio performance. It is built with "
        "SvelteKit, TypeScript, GSAP animations, and follows every principal engineer pattern we have "
        "covered."
    , styles))

    story.append(h2("Features", styles))
    story.append(bullet("<b>Authentication</b> \u2014 Sign up, log in, session management with secure cookies", styles))
    story.append(bullet("<b>Stock Search</b> \u2014 Real-time search with autocomplete and keyboard navigation", styles))
    story.append(bullet("<b>Watchlist</b> \u2014 Add/remove stocks, drag-to-reorder, persistent across sessions", styles))
    story.append(bullet("<b>Stock Detail</b> \u2014 Price chart, company info, key statistics, news feed", styles))
    story.append(bullet("<b>Dashboard</b> \u2014 Portfolio summary, top movers, market overview, animated counters", styles))
    story.append(bullet("<b>Responsive</b> \u2014 Mobile-first design, works on all screen sizes", styles))
    story.append(bullet("<b>Accessible</b> \u2014 WCAG 2.1 AA compliant, keyboard navigable, screen reader friendly", styles))
    story.append(bullet("<b>Performant</b> \u2014 SSR, code splitting, image optimization, sub-2s LCP", styles))

    story.append(h2("Tech Stack", styles))
    story.append(code_block(
        '// TradeBoard Tech Stack\n'
        '// Frontend Framework:  SvelteKit (Svelte 5 with runes)\n'
        '// Language:            TypeScript (strict mode)\n'
        '// Styling:             CSS with custom properties\n'
        '// Animation:           GSAP + ScrollTrigger\n'
        '// Database:            PostgreSQL with Prisma ORM\n'
        '// Authentication:      Session-based with bcrypt\n'
        '// Validation:          Zod schemas\n'
        '// Testing:             Vitest + Testing Library + Playwright\n'
        '// Deployment:          Vercel (adapter-vercel)\n'
        '// Version Control:     Git with trunk-based development',
        filename="Tech Stack", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You understand the scope and tech stack of the TradeBoard capstone project.", styles))
    story.append(page_break())

    # ================================================================
    # 10.2 PROJECT SETUP
    # ================================================================
    story.append(h1("10.2 Project Setup", styles))

    story.append(code_block(
        '# Create the project\n'
        'npx sv create tradeboard\n'
        '# Select: Skeleton project, TypeScript, ESLint, Prettier, Playwright\n\n'
        'cd tradeboard\n\n'
        '# Install dependencies\n'
        'npm install gsap\n'
        'npm install @prisma/client zod bcrypt\n'
        'npm install -D prisma @types/bcrypt\n'
        'npm install -D @testing-library/svelte vitest\n\n'
        '# Initialize Prisma\n'
        'npx prisma init\n\n'
        '# Project structure:\n'
        '# tradeboard/\n'
        '#   prisma/\n'
        '#     schema.prisma           # Database schema\n'
        '#   src/\n'
        '#     lib/\n'
        '#       components/\n'
        '#         atoms/              # Button, Badge, Input, etc.\n'
        '#         molecules/          # SearchBar, StockPrice, FormField\n'
        '#         organisms/          # Header, StockCard, WatchlistTable\n'
        '#       server/\n'
        '#         auth.ts             # Authentication logic\n'
        '#         database.ts         # Prisma client\n'
        '#       stores/\n'
        '#         watchlist.svelte.ts  # Watchlist state\n'
        '#       types.ts              # Shared type definitions\n'
        '#       animation/\n'
        '#         tokens.ts           # Animation design tokens\n'
        '#     routes/\n'
        '#       (marketing)/          # Landing, about, pricing\n'
        '#       (auth)/               # Login, register\n'
        '#       (app)/                # Dashboard, stocks, watchlist\n'
        '#       api/                  # REST API endpoints\n'
        '#     hooks.server.ts         # Auth + security middleware\n'
        '#   tests/                    # E2E tests',
        filename="Project Setup", styles=styles
    ))

    story.append(page_break())

    # ================================================================
    # 10.3 DATABASE SCHEMA
    # ================================================================
    story.append(h1("10.3 Database Schema", styles))

    story.append(code_block(
        '// prisma/schema.prisma\n'
        'datasource db {\n'
        '  provider = "postgresql"\n'
        '  url      = env("DATABASE_URL")\n'
        '}\n\n'
        'generator client {\n'
        '  provider = "prisma-client-js"\n'
        '}\n\n'
        'model User {\n'
        '  id        String   @id @default(cuid())\n'
        '  email     String   @unique\n'
        '  name      String\n'
        '  password  String   // bcrypt hashed\n'
        '  role      Role     @default(USER)\n'
        '  createdAt DateTime @default(now())\n'
        '  updatedAt DateTime @updatedAt\n\n'
        '  sessions  Session[]\n'
        '  watchlist WatchlistItem[]\n'
        '  trades    Trade[]\n'
        '}\n\n'
        'model Session {\n'
        '  id        String   @id @default(cuid())\n'
        '  userId    String\n'
        '  user      User     @relation(fields: [userId], references: [id])\n'
        '  expiresAt DateTime\n'
        '  createdAt DateTime @default(now())\n'
        '}\n\n'
        'model WatchlistItem {\n'
        '  id       String @id @default(cuid())\n'
        '  userId   String\n'
        '  user     User   @relation(fields: [userId], references: [id])\n'
        '  ticker   String\n'
        '  position Int    @default(0)  // For drag-to-reorder\n'
        '  addedAt  DateTime @default(now())\n\n'
        '  @@unique([userId, ticker])\n'
        '}\n\n'
        'model Trade {\n'
        '  id        String   @id @default(cuid())\n'
        '  userId    String\n'
        '  user      User     @relation(fields: [userId], references: [id])\n'
        '  ticker    String\n'
        '  action    TradeAction\n'
        '  quantity  Int\n'
        '  price     Float\n'
        '  total     Float\n'
        '  createdAt DateTime @default(now())\n'
        '}\n\n'
        'enum Role {\n'
        '  USER\n'
        '  ADMIN\n'
        '}\n\n'
        'enum TradeAction {\n'
        '  BUY\n'
        '  SELL\n'
        '}',
        filename="Prisma Database Schema", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You have defined the database schema for users, sessions, watchlists, and trades.", styles))
    story.append(page_break())

    # ================================================================
    # 10.4 AUTHENTICATION
    # ================================================================
    story.append(h1("10.4 Authentication System", styles))

    story.append(code_block(
        '// src/lib/server/auth.ts\n'
        'import bcrypt from "bcrypt";\n'
        'import { db } from "./database";\n\n'
        'const SALT_ROUNDS = 12;\n'
        'const SESSION_DURATION_MS = 7 * 24 * 60 * 60 * 1000; // 7 days\n\n'
        'export async function createUser(\n'
        '  email: string,\n'
        '  name: string,\n'
        '  password: string\n'
        ') {\n'
        '  const hashedPassword = await bcrypt.hash(password, SALT_ROUNDS);\n'
        '  return db.user.create({\n'
        '    data: { email, name, password: hashedPassword }\n'
        '  });\n'
        '}\n\n'
        'export async function login(email: string, password: string) {\n'
        '  const user = await db.user.findUnique({ where: { email } });\n'
        '  if (!user) return null;\n\n'
        '  const valid = await bcrypt.compare(password, user.password);\n'
        '  if (!valid) return null;\n\n'
        '  // Create session\n'
        '  const session = await db.session.create({\n'
        '    data: {\n'
        '      userId: user.id,\n'
        '      expiresAt: new Date(Date.now() + SESSION_DURATION_MS)\n'
        '    }\n'
        '  });\n\n'
        '  return { user, sessionId: session.id };\n'
        '}\n\n'
        'export async function verifySession(sessionId: string) {\n'
        '  const session = await db.session.findUnique({\n'
        '    where: { id: sessionId },\n'
        '    include: { user: true }\n'
        '  });\n\n'
        '  if (!session || session.expiresAt < new Date()) {\n'
        '    if (session) {\n'
        '      await db.session.delete({ where: { id: sessionId } });\n'
        '    }\n'
        '    return null;\n'
        '  }\n\n'
        '  return session.user;\n'
        '}\n\n'
        'export async function logout(sessionId: string) {\n'
        '  await db.session.delete({ where: { id: sessionId } });\n'
        '}',
        filename="Authentication Module", styles=styles
    ))

    story.append(h2("Login Form Action", styles))
    story.append(code_block(
        '// src/routes/(auth)/login/+page.server.ts\n'
        'import { fail, redirect } from "@sveltejs/kit";\n'
        'import { login } from "$lib/server/auth";\n'
        'import { z } from "zod";\n'
        'import type { Actions } from "./$types";\n\n'
        'const LoginSchema = z.object({\n'
        '  email: z.string().email("Please enter a valid email"),\n'
        '  password: z.string().min(1, "Password is required")\n'
        '});\n\n'
        'export const actions: Actions = {\n'
        '  default: async ({ request, cookies }) => {\n'
        '    const formData = Object.fromEntries(await request.formData());\n'
        '    const result = LoginSchema.safeParse(formData);\n\n'
        '    if (!result.success) {\n'
        '      return fail(400, {\n'
        '        email: formData.email?.toString(),\n'
        '        errors: result.error.flatten().fieldErrors\n'
        '      });\n'
        '    }\n\n'
        '    const loginResult = await login(result.data.email, result.data.password);\n\n'
        '    if (!loginResult) {\n'
        '      return fail(401, {\n'
        '        email: result.data.email,\n'
        '        errors: { email: ["Invalid email or password"] }\n'
        '      });\n'
        '    }\n\n'
        '    cookies.set("session_id", loginResult.sessionId, {\n'
        '      path: "/",\n'
        '      httpOnly: true,\n'
        '      secure: true,\n'
        '      sameSite: "lax",\n'
        '      maxAge: 60 * 60 * 24 * 7\n'
        '    });\n\n'
        '    throw redirect(302, "/dashboard");\n'
        '  }\n'
        '};',
        filename="Login Form Action", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You have built a complete authentication system with secure session management.", styles))
    story.append(page_break())

    # ================================================================
    # 10.5 CORE COMPONENTS
    # ================================================================
    story.append(h1("10.5 Core Components", styles))

    story.append(h2("StockCard Component", styles))
    story.append(code_block(
        '<!-- src/lib/components/organisms/StockCard.svelte -->\n'
        '<script lang="ts">\n'
        '  import gsap from "gsap";\n'
        '  import type { Stock } from "$lib/types";\n'
        '  import Badge from "../atoms/Badge.svelte";\n'
        '  import SparkLine from "../molecules/SparkLine.svelte";\n\n'
        '  interface Props {\n'
        '    stock: Stock;\n'
        '    onremove?: () => void;\n'
        '  }\n\n'
        '  let { stock, onremove }: Props = $props();\n'
        '  let cardEl: HTMLElement;\n\n'
        '  let changeClass = $derived(\n'
        '    stock.change > 0 ? "positive" :\n'
        '    stock.change < 0 ? "negative" : "neutral"\n'
        '  );\n\n'
        '  let changeSign = $derived(stock.change > 0 ? "+" : "");\n\n'
        '  $effect(() => {\n'
        '    const ctx = gsap.context(() => {\n'
        '      gsap.from(cardEl, {\n'
        '        y: 20, opacity: 0,\n'
        '        duration: 0.4, ease: "power2.out"\n'
        '      });\n'
        '    });\n'
        '    return () => ctx.revert();\n'
        '  });\n'
        '</script>\n\n'
        '<article bind:this={cardEl} class="stock-card">\n'
        '  <div class="stock-card__header">\n'
        '    <h3 class="stock-card__ticker">{stock.ticker}</h3>\n'
        '    <span class="stock-card__name">{stock.name}</span>\n'
        '  </div>\n\n'
        '  <div class="stock-card__price">\n'
        '    <span class="stock-card__current">\n'
        '      ${stock.price.toFixed(2)}\n'
        '    </span>\n'
        '    <Badge variant={changeClass}>\n'
        '      {changeSign}{stock.changePercent.toFixed(2)}%\n'
        '    </Badge>\n'
        '  </div>\n\n'
        '  <SparkLine data={stock.history} />\n\n'
        '  {#if onremove}\n'
        '    <button\n'
        '      class="stock-card__remove"\n'
        '      onclick={onremove}\n'
        '      aria-label="Remove {stock.ticker} from watchlist"\n'
        '    >\n'
        '      Remove\n'
        '    </button>\n'
        '  {/if}\n'
        '</article>',
        filename="StockCard Component", styles=styles
    ))

    story.append(h2("SearchBar Component", styles))
    story.append(code_block(
        '<!-- src/lib/components/molecules/SearchBar.svelte -->\n'
        '<script lang="ts">\n'
        '  import type { Stock } from "$lib/types";\n\n'
        '  let query = $state("");\n'
        '  let results = $state<Stock[]>([]);\n'
        '  let isOpen = $state(false);\n'
        '  let activeIndex = $state(-1);\n\n'
        '  // Debounced search\n'
        '  let debounceTimer: ReturnType<typeof setTimeout>;\n\n'
        '  function handleInput(e: Event) {\n'
        '    const value = (e.target as HTMLInputElement).value;\n'
        '    query = value;\n'
        '    clearTimeout(debounceTimer);\n\n'
        '    if (value.length < 1) {\n'
        '      results = []; isOpen = false;\n'
        '      return;\n'
        '    }\n\n'
        '    debounceTimer = setTimeout(async () => {\n'
        '      const res = await fetch(`/api/stocks?q=${value}`);\n'
        '      const data = await res.json();\n'
        '      results = data.data;\n'
        '      isOpen = results.length > 0;\n'
        '      activeIndex = -1;\n'
        '    }, 300);\n'
        '  }\n\n'
        '  function handleKeydown(e: KeyboardEvent) {\n'
        '    if (e.key === "ArrowDown") {\n'
        '      e.preventDefault();\n'
        '      activeIndex = Math.min(activeIndex + 1, results.length - 1);\n'
        '    } else if (e.key === "ArrowUp") {\n'
        '      e.preventDefault();\n'
        '      activeIndex = Math.max(activeIndex - 1, -1);\n'
        '    } else if (e.key === "Enter" && activeIndex >= 0) {\n'
        '      selectStock(results[activeIndex]);\n'
        '    } else if (e.key === "Escape") {\n'
        '      isOpen = false;\n'
        '    }\n'
        '  }\n\n'
        '  function selectStock(stock: Stock) {\n'
        '    window.location.href = `/stocks/${stock.ticker}`;\n'
        '  }\n'
        '</script>\n\n'
        '<div class="search-bar" role="combobox" aria-expanded={isOpen}>\n'
        '  <input\n'
        '    type="text"\n'
        '    placeholder="Search stocks..."\n'
        '    value={query}\n'
        '    oninput={handleInput}\n'
        '    onkeydown={handleKeydown}\n'
        '    role="searchbox"\n'
        '    aria-label="Search stocks"\n'
        '    aria-autocomplete="list"\n'
        '  />\n\n'
        '  {#if isOpen}\n'
        '    <ul class="search-results" role="listbox">\n'
        '      {#each results as stock, i}\n'
        '        <li\n'
        '          class="search-result"\n'
        '          class:active={i === activeIndex}\n'
        '          role="option"\n'
        '          aria-selected={i === activeIndex}\n'
        '          onclick={() => selectStock(stock)}\n'
        '        >\n'
        '          <strong>{stock.ticker}</strong>\n'
        '          <span>{stock.name}</span>\n'
        '          <span>${stock.price.toFixed(2)}</span>\n'
        '        </li>\n'
        '      {/each}\n'
        '    </ul>\n'
        '  {/if}\n'
        '</div>',
        filename="SearchBar Component", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You have built the core StockCard and SearchBar components.", styles))
    story.append(page_break())

    # ================================================================
    # 10.6 DASHBOARD PAGE
    # ================================================================
    story.append(h1("10.6 The Dashboard", styles))

    story.append(code_block(
        '// src/routes/(app)/dashboard/+page.server.ts\n'
        'import type { PageServerLoad } from "./$types";\n'
        'import { db } from "$lib/server/database";\n\n'
        'export const load: PageServerLoad = async ({ locals }) => {\n'
        '  const userId = locals.user.id;\n\n'
        '  // Fast queries: await immediately\n'
        '  const [watchlist, recentTrades] = await Promise.all([\n'
        '    db.watchlistItem.findMany({\n'
        '      where: { userId },\n'
        '      orderBy: { position: "asc" }\n'
        '    }),\n'
        '    db.trade.findMany({\n'
        '      where: { userId },\n'
        '      orderBy: { createdAt: "desc" },\n'
        '      take: 5\n'
        '    })\n'
        '  ]);\n\n'
        '  // Slow queries: stream (don\'t await)\n'
        '  const marketSummary = fetchMarketSummary();\n\n'
        '  return { watchlist, recentTrades, marketSummary };\n'
        '};',
        filename="Dashboard Data Loading", styles=styles
    ))

    story.append(h2("Dashboard Page Component", styles))
    story.append(code_block(
        '<!-- src/routes/(app)/dashboard/+page.svelte -->\n'
        '<script lang="ts">\n'
        '  import gsap from "gsap";\n'
        '  import StockCard from "$lib/components/organisms/StockCard.svelte";\n'
        '  import SummaryCard from "$lib/components/molecules/SummaryCard.svelte";\n\n'
        '  let { data } = $props();\n'
        '  let dashboardEl: HTMLElement;\n\n'
        '  // Animate dashboard entrance\n'
        '  $effect(() => {\n'
        '    const ctx = gsap.context(() => {\n'
        '      const tl = gsap.timeline({ defaults: { ease: "power2.out" } });\n\n'
        '      tl.from(".summary-card", {\n'
        '        y: 30, opacity: 0, duration: 0.4, stagger: 0.08\n'
        '      })\n'
        '      .from(".watchlist-item", {\n'
        '        x: 20, opacity: 0, duration: 0.3, stagger: 0.05\n'
        '      }, "-=0.2")\n'
        '      .from(".recent-trade", {\n'
        '        y: 15, opacity: 0, duration: 0.3, stagger: 0.04\n'
        '      }, "-=0.2");\n'
        '    }, dashboardEl);\n\n'
        '    return () => ctx.revert();\n'
        '  });\n'
        '</script>\n\n'
        '<div bind:this={dashboardEl} class="dashboard">\n'
        '  <h1>Dashboard</h1>\n\n'
        '  <section class="summary-grid">\n'
        '    <SummaryCard\n'
        '      label="Portfolio Value"\n'
        '      value="$145,832.47"\n'
        '      change={2.3}\n'
        '    />\n'
        '    <SummaryCard\n'
        '      label="Today\'s P&L"\n'
        '      value="+$1,247.00"\n'
        '      change={0.85}\n'
        '    />\n'
        '    <SummaryCard\n'
        '      label="Watchlist Stocks"\n'
        '      value={String(data.watchlist.length)}\n'
        '    />\n'
        '  </section>\n\n'
        '  <section class="watchlist">\n'
        '    <h2>Watchlist</h2>\n'
        '    {#each data.watchlist as item}\n'
        '      <div class="watchlist-item">\n'
        '        <StockCard stock={item} />\n'
        '      </div>\n'
        '    {/each}\n'
        '  </section>\n\n'
        '  <section class="recent-trades">\n'
        '    <h2>Recent Trades</h2>\n'
        '    {#each data.recentTrades as trade}\n'
        '      <div class="recent-trade">\n'
        '        <span>{trade.action} {trade.quantity} {trade.ticker}</span>\n'
        '        <span>${trade.total.toFixed(2)}</span>\n'
        '      </div>\n'
        '    {/each}\n'
        '  </section>\n'
        '</div>',
        filename="Dashboard Page", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You have built the dashboard with data loading and GSAP animations.", styles))
    story.append(page_break())

    # ================================================================
    # 10.7 ACCESSIBILITY AND PERFORMANCE
    # ================================================================
    story.append(h1("10.7 Accessibility and Performance", styles))

    story.append(h2("Accessibility Checklist", styles))
    story.append(bullet("<b>Semantic HTML</b> \u2014 Use <code>&lt;nav&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;aside&gt;</code> for landmark regions.", styles))
    story.append(bullet("<b>ARIA labels</b> \u2014 Every interactive element has an accessible name: <code>aria-label</code> for icon buttons, labels for inputs.", styles))
    story.append(bullet("<b>Keyboard navigation</b> \u2014 Tab order follows visual order. All interactive elements are focusable. Custom widgets have proper keyboard support.", styles))
    story.append(bullet("<b>Color contrast</b> \u2014 Text meets WCAG AA contrast ratios: 4.5:1 for normal text, 3:1 for large text.", styles))
    story.append(bullet("<b>Focus indicators</b> \u2014 Visible focus rings on all interactive elements. Never <code>outline: none</code> without a replacement.", styles))
    story.append(bullet("<b>Screen readers</b> \u2014 Dynamic content uses <code>aria-live</code> regions. Price changes announced to screen readers.", styles))
    story.append(bullet("<b>Motion</b> \u2014 Respect <code>prefers-reduced-motion</code>. Disable GSAP animations for users who prefer reduced motion.", styles))

    story.append(code_block(
        '// Respect reduced motion preference\n'
        'import gsap from "gsap";\n\n'
        '// Check user preference\n'
        'const prefersReducedMotion = \n'
        '  window.matchMedia("(prefers-reduced-motion: reduce)").matches;\n\n'
        'if (prefersReducedMotion) {\n'
        '  // Disable all GSAP animations globally\n'
        '  gsap.globalTimeline.timeScale(100); // Instant completion\n'
        '  // Or set all durations to 0\n'
        '  gsap.defaults({ duration: 0 });\n'
        '}',
        filename="Reduced Motion Support", styles=styles
    ))

    story.append(h2("Performance Optimization", styles))
    story.append(code_block(
        '// svelte.config.js - Prerender static pages\n'
        'export default {\n'
        '  kit: {\n'
        '    prerender: {\n'
        '      entries: ["/", "/about", "/pricing"]\n'
        '    }\n'
        '  }\n'
        '};\n\n'
        '// Preload critical data on hover\n'
        '// SvelteKit does this automatically for <a> elements!\n\n'
        '// Code split heavy components\n'
        '// The chart library only loads on the stock detail page:\n'
        'export const load: PageServerLoad = async ({ params }) => {\n'
        '  const stock = await getStock(params.ticker);\n'
        '  // Dynamically import heavy charting library\n'
        '  const { generateChart } = await import("$lib/charts");\n'
        '  return { stock, chart: generateChart(stock.history) };\n'
        '};',
        filename="Performance Patterns", styles=styles
    ))

    story.append(principal_box(
        "Performance and accessibility are not afterthoughts \u2014 they are requirements. A fast app that "
        "is not accessible excludes users. An accessible app that is slow frustrates everyone. Ship both "
        "from day one. Test with Lighthouse for performance and axe-core for accessibility as part of "
        "your CI pipeline."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You can build accessible, performant production applications.", styles))
    story.append(page_break())

    # ================================================================
    # 10.8 DEPLOYMENT
    # ================================================================
    story.append(h1("10.8 Deployment", styles))

    story.append(code_block(
        '# Deploy to Vercel\n'
        'npm install -D @sveltejs/adapter-vercel\n\n'
        '# svelte.config.js\n'
        'import adapter from "@sveltejs/adapter-vercel";\n\n'
        'export default {\n'
        '  kit: {\n'
        '    adapter: adapter({\n'
        '      runtime: "nodejs20.x"\n'
        '    })\n'
        '  }\n'
        '};\n\n'
        '# Environment variables (set in Vercel dashboard):\n'
        '# DATABASE_URL     = postgresql://...\n'
        '# SESSION_SECRET   = (random 64-char string)\n\n'
        '# Deploy\n'
        'npx vercel\n\n'
        '# Production deploy\n'
        'npx vercel --prod\n\n'
        '# Or connect GitHub repo for automatic deploys:\n'
        '# 1. Push to main -> automatic production deploy\n'
        '# 2. Push to PR branch -> preview deploy with unique URL',
        filename="Deployment", styles=styles
    ))

    story.append(h2("Production Checklist", styles))
    story.append(bullet("All environment variables set in production", styles))
    story.append(bullet("Database migrations applied (<code>npx prisma migrate deploy</code>)", styles))
    story.append(bullet("HTTPS enforced (Vercel does this automatically)", styles))
    story.append(bullet("Security headers set (CSP, X-Frame-Options, etc.)", styles))
    story.append(bullet("Error tracking configured (Sentry or similar)", styles))
    story.append(bullet("Health check endpoint active (/api/health)", styles))
    story.append(bullet("Lighthouse scores: Performance 90+, Accessibility 100, SEO 100", styles))
    story.append(bullet("All tests passing (unit, integration, E2E)", styles))
    story.append(bullet("Bundle size analyzed and optimized", styles))

    story.append(spacer(16))

    # ================================================================
    # EXERCISES
    # ================================================================
    story.append(h1("Chapter 10 Exercises", styles))
    story.append(HorizontalLine())
    story.append(spacer(8))

    story.append(exercise(3, "Build the Authentication System", [
        ('ExerciseBody', '<b>Task:</b> Implement the complete authentication flow: registration page '
         'with form validation (email, name, password, confirm password), login page, logout action, '
         'session management with hooks, and protected routes. Use bcrypt for password hashing, Zod for '
         'validation, and HttpOnly cookies for sessions. Test both happy path and error cases.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(4, "Build the Stock Search", [
        ('ExerciseBody', '<b>Task:</b> Build a real-time stock search with autocomplete. The search bar '
         'should debounce input (300ms), fetch results from /api/stocks, display results in a dropdown, '
         'support keyboard navigation (arrow keys + enter), and navigate to /stocks/[ticker] on selection. '
         'Add ARIA attributes for accessibility. Animate the dropdown with GSAP.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(4, "Build the Watchlist", [
        ('ExerciseBody', '<b>Task:</b> Implement the full watchlist feature: add stocks from search results, '
         'remove stocks with confirmation, drag-to-reorder using GSAP Draggable, persist order to the '
         'database. Use optimistic updates for add/remove operations. Add GSAP Flip animations for '
         'smooth reordering. Include empty state and loading states.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(5, "Full Production Deployment", [
        ('ExerciseBody', '<b>Task:</b> Deploy TradeBoard to production. Set up: GitHub repository with '
         'CI/CD pipeline (lint, test, build, deploy), Vercel project with environment variables, '
         'PostgreSQL database (Vercel Postgres or Supabase), error tracking with Sentry, and monitoring '
         'with Vercel Analytics. Achieve Lighthouse scores of 90+ for performance and 100 for '
         'accessibility. Document the deployment process in a README.'),
    ], styles))

    story.append(spacer(16))
    story.append(p(
        "Congratulations. You have completed the entire course. You started with zero knowledge of web "
        "development and now you have the skills of a principal engineer. You understand not just how "
        "to code, but how to architect systems, lead teams, make technical decisions, and build "
        "production-grade applications. The journey from zero to principal engineer is not about knowing "
        "every syntax \u2014 it is about understanding why things work the way they do and having the "
        "judgment to make the right decisions under uncertainty. Keep building. Keep learning. Keep "
        "pushing the craft forward."
    , styles))
    story.append(spacer(8))
    story.append(checkpoint("You have completed the From Zero to Principal Engineer course! You are ready "
                           "to build production-grade web applications with confidence.", styles))
    story.append(page_break())

    return story
