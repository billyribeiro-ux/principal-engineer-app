"""Chapter 7: SvelteKit — The Full-Stack Framework"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_7(styles):
    story = []

    story.append(ChapterCoverPage(7, "SvelteKit \u2014 The Full-Stack Framework",
                                  "City Planning for Your Component Collection", "PART 2: LEVELING UP"))
    story.append(PageBreak())

    # ================================================================
    # 7.1 WHAT IS SVELTEKIT?
    # ================================================================
    story.append(h1("7.1 What Is SvelteKit?", styles))
    story.append(analogy_box(
        "Svelte is like having blueprints for individual buildings \u2014 you can design beautiful structures, "
        "but you still need to figure out where to put them, how to connect roads between them, and how to "
        "deliver water and electricity. SvelteKit is the city planning department. It decides where buildings "
        "go (routing), how goods are delivered (data loading), how the mail system works (form handling), "
        "and how the entire infrastructure connects together (deployment)."
    , styles))

    story.append(p(
        "SvelteKit is the official application framework for Svelte. While Svelte is a component framework "
        "(it tells you how to build individual UI pieces), SvelteKit is the full-stack framework that handles "
        "everything else: routing, server-side rendering, data loading, form handling, API endpoints, "
        "and deployment. If Svelte is React, then SvelteKit is Next.js."
    , styles))

    story.append(h2("Creating a SvelteKit Project", styles))
    story.append(code_block(
        '# Create a new SvelteKit project\n'
        'npx sv create tradeboard\n'
        'cd tradeboard\n'
        'npm install\n'
        'npm run dev\n\n'
        '# Project structure:\n'
        '# tradeboard/\n'
        '#   src/\n'
        '#     routes/          <-- File-based routing (pages live here)\n'
        '#       +page.svelte   <-- Homepage\n'
        '#       +layout.svelte <-- Root layout (wraps all pages)\n'
        '#     lib/             <-- Shared code ($lib alias)\n'
        '#       components/    <-- Reusable components\n'
        '#       server/        <-- Server-only code ($lib/server)\n'
        '#     app.html         <-- HTML shell template\n'
        '#     app.css          <-- Global styles\n'
        '#     hooks.server.ts  <-- Server hooks (middleware)\n'
        '#   static/            <-- Static assets (favicon, images)\n'
        '#   svelte.config.js   <-- SvelteKit configuration\n'
        '#   vite.config.ts     <-- Vite configuration\n'
        '#   tsconfig.json      <-- TypeScript configuration',
        filename="Creating a SvelteKit Project", styles=styles
    ))

    story.append(h2("The $lib Alias", styles))
    story.append(p(
        "SvelteKit provides the <code>$lib</code> import alias that points to <code>src/lib</code>. This "
        "eliminates ugly relative imports. Instead of <code>import Button from '../../../../lib/components/"
        "Button.svelte'</code>, you write <code>import Button from '$lib/components/Button.svelte'</code>. "
        "The <code>$lib/server</code> directory is special \u2014 code here can only be imported by server-side "
        "code, preventing accidental exposure of secrets."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand what SvelteKit is and how to create a new project.", styles))
    story.append(page_break())

    # ================================================================
    # 7.2 FILE-BASED ROUTING
    # ================================================================
    story.append(h1("7.2 File-Based Routing", styles))
    story.append(analogy_box(
        "File-based routing is like a city's street address system. The folder structure IS the map. "
        "If you want a building at 123 Main Street, you create a folder called 'main-street' and put "
        "building 123 inside it. No separate routing configuration needed \u2014 the file system IS the "
        "router. Every folder in <code>src/routes</code> becomes a URL path, and the files inside define "
        "what happens when someone visits that address."
    , styles))

    story.append(h2("Route Files", styles))
    story.append(p(
        "SvelteKit uses special filenames (always prefixed with +) to define what happens at each route:"
    , styles))

    story.append(bullet("<b>+page.svelte</b> \u2014 The page component. This is what the user sees.", styles))
    story.append(bullet("<b>+page.server.ts</b> \u2014 Server-side data loading and form actions for this page.", styles))
    story.append(bullet("<b>+page.ts</b> \u2014 Universal (client + server) data loading for this page.", styles))
    story.append(bullet("<b>+layout.svelte</b> \u2014 Layout wrapper that persists across child routes.", styles))
    story.append(bullet("<b>+layout.server.ts</b> \u2014 Server-side data loading for the layout.", styles))
    story.append(bullet("<b>+error.svelte</b> \u2014 Error page displayed when something goes wrong.", styles))
    story.append(bullet("<b>+server.ts</b> \u2014 API endpoint (no UI, just JSON/data responses).", styles))

    story.append(code_block(
        '// File structure -> URL mapping\n'
        '//\n'
        '// src/routes/\n'
        '//   +page.svelte                    -> /\n'
        '//   about/+page.svelte              -> /about\n'
        '//   dashboard/\n'
        '//     +page.svelte                  -> /dashboard\n'
        '//     +layout.svelte                -> wraps all /dashboard/* pages\n'
        '//     watchlist/+page.svelte        -> /dashboard/watchlist\n'
        '//     settings/+page.svelte         -> /dashboard/settings\n'
        '//   stocks/\n'
        '//     +page.svelte                  -> /stocks\n'
        '//     [ticker]/+page.svelte         -> /stocks/AAPL, /stocks/GOOG, etc.\n'
        '//   api/\n'
        '//     stocks/+server.ts             -> /api/stocks (API endpoint)\n'
        '//     stocks/[ticker]/+server.ts    -> /api/stocks/AAPL (API endpoint)',
        filename="File-Based Routing", styles=styles
    ))

    story.append(h2("Dynamic Route Parameters", styles))
    story.append(code_block(
        '<!-- src/routes/stocks/[ticker]/+page.svelte -->\n'
        '<script>\n'
        '  let { data } = $props();\n'
        '</script>\n\n'
        '<h1>{data.stock.name} ({data.stock.ticker})</h1>\n'
        '<p>Price: ${data.stock.price}</p>\n\n'
        '<!-- src/routes/stocks/[ticker]/+page.server.ts -->\n'
        '// The parameter name matches the folder name: [ticker]\n'
        'import { error } from "@sveltejs/kit";\n'
        'import type { PageServerLoad } from "./$types";\n\n'
        'export const load: PageServerLoad = async ({ params }) => {\n'
        '  // params.ticker comes from the [ticker] folder name\n'
        '  const stock = await getStock(params.ticker);\n\n'
        '  if (!stock) {\n'
        '    throw error(404, {\n'
        '      message: `Stock ${params.ticker} not found`\n'
        '    });\n'
        '  }\n\n'
        '  return { stock };\n'
        '};',
        filename="Dynamic Routes", styles=styles
    ))

    story.append(h2("Rest Parameters and Route Groups", styles))
    story.append(code_block(
        '// Rest parameters: [...rest] catches everything\n'
        '// src/routes/docs/[...path]/+page.svelte\n'
        '// Matches: /docs/getting-started, /docs/api/auth, /docs/a/b/c\n'
        '// params.path = "getting-started" or "api/auth" or "a/b/c"\n\n'
        '// Route groups: (group) organizes without affecting URL\n'
        '// src/routes/\n'
        '//   (auth)/\n'
        '//     login/+page.svelte      -> /login  (not /auth/login!)\n'
        '//     register/+page.svelte   -> /register\n'
        '//     +layout.svelte          -> shared auth layout\n'
        '//   (app)/\n'
        '//     dashboard/+page.svelte  -> /dashboard\n'
        '//     settings/+page.svelte   -> /settings\n'
        '//     +layout.svelte          -> shared app layout with nav\n'
        '//\n'
        '// The parentheses mean "group these routes together\n'
        '// for shared layouts, but don\'t add to the URL"',
        filename="Rest Parameters and Route Groups", styles=styles
    ))

    story.append(principal_box(
        "Route groups are one of SvelteKit's most powerful features. Use them to create different "
        "layouts for different sections of your app without nesting URLs. Your auth pages (login, register, "
        "forgot password) get a minimal centered layout, while your app pages (dashboard, settings) get "
        "the full layout with navigation sidebar. Both exist at the root URL level."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand file-based routing, dynamic parameters, rest parameters, "
                           "and route groups.", styles))
    story.append(page_break())

    # ================================================================
    # 7.3 LOADING DATA
    # ================================================================
    story.append(h1("7.3 Loading Data", styles))
    story.append(analogy_box(
        "Data loading in SvelteKit is like a city's delivery system. Server load functions are delivery "
        "trucks \u2014 they go to the warehouse (database), pick up goods, and deliver them to the store "
        "(your page) before it opens. Universal load functions are like having a local warehouse \u2014 the "
        "store can grab items itself. The key insight: delivery trucks (server loads) can access the "
        "warehouse's restricted area (databases, API keys), but the local warehouse (universal loads) "
        "is accessible from anywhere."
    , styles))

    story.append(h2("Server Load Functions", styles))
    story.append(p(
        "Server load functions run <b>only on the server</b>. They can access databases, read files, "
        "use secret API keys \u2014 anything that should never be exposed to the client. This is the most "
        "common and recommended pattern."
    , styles))

    story.append(code_block(
        '// src/routes/dashboard/+page.server.ts\n'
        'import type { PageServerLoad } from "./$types";\n'
        'import { db } from "$lib/server/database";\n'
        'import { STOCK_API_KEY } from "$env/static/private";\n\n'
        'export const load: PageServerLoad = async ({ locals, fetch }) => {\n'
        '  // locals.user was set by our auth hook\n'
        '  const userId = locals.user?.id;\n\n'
        '  // Parallel data fetching for performance\n'
        '  const [watchlist, recentTrades, marketSummary] = await Promise.all([\n'
        '    db.watchlist.findMany({\n'
        '      where: { userId },\n'
        '      include: { stock: true }\n'
        '    }),\n'
        '    db.trade.findMany({\n'
        '      where: { userId },\n'
        '      orderBy: { createdAt: "desc" },\n'
        '      take: 10\n'
        '    }),\n'
        '    fetch(`https://api.stocks.com/market?key=${STOCK_API_KEY}`)\n'
        '      .then(r => r.json())\n'
        '  ]);\n\n'
        '  return {\n'
        '    watchlist,\n'
        '    recentTrades,\n'
        '    marketSummary\n'
        '  };\n'
        '};\n\n'
        '<!-- src/routes/dashboard/+page.svelte -->\n'
        '<script>\n'
        '  let { data } = $props();\n'
        '  // data.watchlist, data.recentTrades, data.marketSummary\n'
        '  // are fully typed thanks to PageServerLoad!\n'
        '</script>\n\n'
        '<h1>Dashboard</h1>\n'
        '{#each data.watchlist as item}\n'
        '  <StockCard stock={item.stock} />\n'
        '{/each}',
        filename="Server Load Functions", styles=styles
    ))

    story.append(h2("Universal Load Functions", styles))
    story.append(p(
        "Universal load functions run on both server (first load) and client (subsequent navigations). "
        "Use them when you need to access browser APIs or when the data does not require server secrets."
    , styles))

    story.append(code_block(
        '// src/routes/stocks/+page.ts (note: .ts, not .server.ts)\n'
        'import type { PageLoad } from "./$types";\n\n'
        'export const load: PageLoad = async ({ fetch, url }) => {\n'
        '  const search = url.searchParams.get("q") || "";\n'
        '  const page = Number(url.searchParams.get("page")) || 1;\n\n'
        '  // This fetch() is special - on the server it makes a direct\n'
        '  // internal call; on the client it makes a normal HTTP request\n'
        '  const res = await fetch(\n'
        '    `/api/stocks?q=${search}&page=${page}`\n'
        '  );\n'
        '  const { data, meta } = await res.json();\n\n'
        '  return { stocks: data, pagination: meta, search };\n'
        '};',
        filename="Universal Load Functions", styles=styles
    ))

    story.append(mistake_box(
        "Never import server-only modules ($lib/server/*, $env/static/private) in universal load "
        "functions (+page.ts). They run on the client too, which would expose your secrets. If you "
        "need to access a database or private API key, use a server load function (+page.server.ts) "
        "instead. SvelteKit will throw a build error if you try, but understanding why prevents confusion."
    , styles))

    story.append(h2("Error Handling in Load Functions", styles))
    story.append(code_block(
        'import { error, redirect } from "@sveltejs/kit";\n\n'
        'export const load: PageServerLoad = async ({ params, locals }) => {\n'
        '  // Redirect if not authenticated\n'
        '  if (!locals.user) {\n'
        '    throw redirect(302, "/login");\n'
        '  }\n\n'
        '  const stock = await db.stock.findUnique({\n'
        '    where: { ticker: params.ticker }\n'
        '  });\n\n'
        '  // Throw expected errors (shown to user)\n'
        '  if (!stock) {\n'
        '    throw error(404, {\n'
        '      message: `Stock ${params.ticker} not found`\n'
        '    });\n'
        '  }\n\n'
        '  // Unexpected errors (try/catch) become 500s\n'
        '  // and are logged server-side\n'
        '  return { stock };\n'
        '};',
        filename="Error Handling in Load Functions", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You understand server load functions, universal load functions, and error handling.", styles))
    story.append(page_break())

    # ================================================================
    # 7.4 FORM ACTIONS
    # ================================================================
    story.append(h1("7.4 Form Actions", styles))
    story.append(analogy_box(
        "Form actions are like the paperwork processing department at city hall. You fill out a form "
        "(the HTML form), hand it to the clerk (submit to the server), they process it (action function), "
        "validate it (check for errors), and either approve it (return success data) or send it back with "
        "corrections needed (return validation errors). The beauty is that it works even if the computers "
        "are down (JavaScript disabled) \u2014 paper forms always work."
    , styles))

    story.append(h2("Default Actions", styles))
    story.append(code_block(
        '// src/routes/login/+page.server.ts\n'
        'import { fail, redirect } from "@sveltejs/kit";\n'
        'import type { Actions } from "./$types";\n'
        'import { verifyPassword } from "$lib/server/auth";\n\n'
        'export const actions: Actions = {\n'
        '  default: async ({ request, cookies }) => {\n'
        '    const formData = await request.formData();\n'
        '    const email = formData.get("email")?.toString() || "";\n'
        '    const password = formData.get("password")?.toString() || "";\n\n'
        '    // Validate\n'
        '    if (!email || !password) {\n'
        '      return fail(400, {\n'
        '        email,  // Send back so user doesn\'t retype\n'
        '        error: "Email and password are required"\n'
        '      });\n'
        '    }\n\n'
        '    // Authenticate\n'
        '    const user = await verifyPassword(email, password);\n'
        '    if (!user) {\n'
        '      return fail(401, {\n'
        '        email,\n'
        '        error: "Invalid email or password"\n'
        '      });\n'
        '    }\n\n'
        '    // Set session cookie\n'
        '    cookies.set("session_id", user.sessionId, {\n'
        '      path: "/",\n'
        '      httpOnly: true,\n'
        '      secure: true,\n'
        '      sameSite: "lax",\n'
        '      maxAge: 60 * 60 * 24 * 7  // 1 week\n'
        '    });\n\n'
        '    throw redirect(302, "/dashboard");\n'
        '  }\n'
        '};\n\n'
        '<!-- src/routes/login/+page.svelte -->\n'
        '<script>\n'
        '  import { enhance } from "$app/forms";\n'
        '  let { form } = $props();\n'
        '</script>\n\n'
        '<form method="POST" use:enhance>\n'
        '  {#if form?.error}\n'
        '    <p class="error">{form.error}</p>\n'
        '  {/if}\n\n'
        '  <label>\n'
        '    Email\n'
        '    <input name="email" type="email" value={form?.email || ""} />\n'
        '  </label>\n\n'
        '  <label>\n'
        '    Password\n'
        '    <input name="password" type="password" />\n'
        '  </label>\n\n'
        '  <button type="submit">Log In</button>\n'
        '</form>',
        filename="Default Form Action", styles=styles
    ))

    story.append(h2("Named Actions", styles))
    story.append(code_block(
        '// src/routes/dashboard/watchlist/+page.server.ts\n'
        'import { fail } from "@sveltejs/kit";\n'
        'import type { Actions } from "./$types";\n\n'
        'export const actions: Actions = {\n'
        '  add: async ({ request, locals }) => {\n'
        '    const formData = await request.formData();\n'
        '    const ticker = formData.get("ticker")?.toString();\n\n'
        '    if (!ticker || !/^[A-Z]{1,5}$/.test(ticker)) {\n'
        '      return fail(400, { error: "Invalid ticker symbol" });\n'
        '    }\n\n'
        '    await db.watchlist.create({\n'
        '      data: { userId: locals.user.id, ticker }\n'
        '    });\n\n'
        '    return { success: true, message: `${ticker} added` };\n'
        '  },\n\n'
        '  remove: async ({ request, locals }) => {\n'
        '    const formData = await request.formData();\n'
        '    const ticker = formData.get("ticker")?.toString();\n\n'
        '    await db.watchlist.delete({\n'
        '      where: { userId_ticker: {\n'
        '        userId: locals.user.id,\n'
        '        ticker: ticker!\n'
        '      }}\n'
        '    });\n\n'
        '    return { success: true };\n'
        '  }\n'
        '};\n\n'
        '<!-- Using named actions -->\n'
        '<form method="POST" action="?/add" use:enhance>\n'
        '  <input name="ticker" placeholder="AAPL" />\n'
        '  <button>Add to Watchlist</button>\n'
        '</form>\n\n'
        '<form method="POST" action="?/remove" use:enhance>\n'
        '  <input type="hidden" name="ticker" value={stock.ticker} />\n'
        '  <button>Remove</button>\n'
        '</form>',
        filename="Named Form Actions", styles=styles
    ))

    story.append(h2("Progressive Enhancement with use:enhance", styles))
    story.append(p(
        "The <code>use:enhance</code> directive is SvelteKit's progressive enhancement system. Without it, "
        "the form submits normally (full page reload). With it, SvelteKit intercepts the submission, sends "
        "it via fetch, and updates the page without a full reload. The form still works without JavaScript "
        "\u2014 a true progressive enhancement."
    , styles))

    story.append(code_block(
        '<!-- Custom enhance for optimistic updates -->\n'
        '<form method="POST" action="?/remove"\n'
        '  use:enhance={() => {\n'
        '    // Called BEFORE the form submits\n'
        '    removing = true;\n\n'
        '    return async ({ result, update }) => {\n'
        '      // Called AFTER the server responds\n'
        '      removing = false;\n'
        '      if (result.type === "success") {\n'
        '        // Custom success handling\n'
        '        showToast("Stock removed!");\n'
        '      }\n'
        '      await update();  // Apply server response\n'
        '    };\n'
        '  }}\n'
        '>\n'
        '  <button disabled={removing}>\n'
        '    {removing ? "Removing..." : "Remove"}\n'
        '  </button>\n'
        '</form>',
        filename="Custom Enhance Callback", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can implement form actions with validation, named actions, and "
                           "progressive enhancement.", styles))
    story.append(page_break())

    # ================================================================
    # 7.5 LAYOUTS AND ERROR HANDLING
    # ================================================================
    story.append(h1("7.5 Layouts and Error Handling", styles))

    story.append(h2("Nested Layouts", styles))
    story.append(p(
        "Layouts wrap pages and persist across navigation. A root layout wraps the entire app, and nested "
        "layouts add structure for specific sections. When you navigate between pages that share a layout, "
        "only the page content changes \u2014 the layout stays mounted."
    , styles))

    story.append(code_block(
        '<!-- src/routes/+layout.svelte (ROOT layout - wraps everything) -->\n'
        '<script>\n'
        '  let { children } = $props();\n'
        '</script>\n\n'
        '<div class="app">\n'
        '  <header>\n'
        '    <nav>\n'
        '      <a href="/">Home</a>\n'
        '      <a href="/dashboard">Dashboard</a>\n'
        '    </nav>\n'
        '  </header>\n\n'
        '  <main>\n'
        '    {@render children()}\n'
        '  </main>\n\n'
        '  <footer>TradeBoard &copy; 2024</footer>\n'
        '</div>\n\n'
        '<!-- src/routes/dashboard/+layout.svelte (NESTED layout) -->\n'
        '<script>\n'
        '  let { children, data } = $props();\n'
        '</script>\n\n'
        '<div class="dashboard-layout">\n'
        '  <aside class="sidebar">\n'
        '    <nav>\n'
        '      <a href="/dashboard">Overview</a>\n'
        '      <a href="/dashboard/watchlist">Watchlist</a>\n'
        '      <a href="/dashboard/trades">Trades</a>\n'
        '      <a href="/dashboard/settings">Settings</a>\n'
        '    </nav>\n'
        '    <p>Welcome, {data.user.name}</p>\n'
        '  </aside>\n\n'
        '  <div class="dashboard-content">\n'
        '    {@render children()}\n'
        '  </div>\n'
        '</div>',
        filename="Nested Layouts", styles=styles
    ))

    story.append(h2("Layout Data", styles))
    story.append(code_block(
        '// src/routes/dashboard/+layout.server.ts\n'
        '// This data is available to ALL pages under /dashboard/\n'
        'import { redirect } from "@sveltejs/kit";\n'
        'import type { LayoutServerLoad } from "./$types";\n\n'
        'export const load: LayoutServerLoad = async ({ locals }) => {\n'
        '  if (!locals.user) {\n'
        '    throw redirect(302, "/login");\n'
        '  }\n\n'
        '  return {\n'
        '    user: {\n'
        '      name: locals.user.name,\n'
        '      email: locals.user.email,\n'
        '      avatar: locals.user.avatar\n'
        '    }\n'
        '  };\n'
        '};',
        filename="Layout Data Loading", styles=styles
    ))

    story.append(h2("Error Pages", styles))
    story.append(code_block(
        '<!-- src/routes/+error.svelte (catches all errors) -->\n'
        '<script>\n'
        '  import { page } from "$app/stores";\n'
        '</script>\n\n'
        '<div class="error-page">\n'
        '  <h1>{$page.status}</h1>\n'
        '  <p>{$page.error?.message || "Something went wrong"}</p>\n\n'
        '  {#if $page.status === 404}\n'
        '    <p>The page you are looking for does not exist.</p>\n'
        '    <a href="/">Go Home</a>\n'
        '  {:else}\n'
        '    <p>Please try again later.</p>\n'
        '    <button onclick={() => location.reload()}>Retry</button>\n'
        '  {/if}\n'
        '</div>\n\n'
        '<!-- You can also have route-specific error pages -->\n'
        '<!-- src/routes/dashboard/+error.svelte -->\n'
        '<!-- This catches errors only within /dashboard/* -->',
        filename="Error Pages", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can create nested layouts, layout data loading, and error boundary pages.", styles))
    story.append(page_break())

    # ================================================================
    # 7.6 HOOKS AND MIDDLEWARE
    # ================================================================
    story.append(h1("7.6 Hooks and Middleware", styles))
    story.append(analogy_box(
        "Hooks are like security checkpoints at the city gates. Every person (request) entering the city "
        "must pass through the checkpoint. The guards (handle hook) can inspect credentials (cookies), "
        "add a visitor badge (set locals), redirect unauthorized visitors, or modify what they see on "
        "their way out (transform responses). Every single request goes through hooks before reaching "
        "any route."
    , styles))

    story.append(h2("The handle Hook", styles))
    story.append(code_block(
        '// src/hooks.server.ts\n'
        'import type { Handle } from "@sveltejs/kit";\n'
        'import { verifySession } from "$lib/server/auth";\n\n'
        'export const handle: Handle = async ({ event, resolve }) => {\n'
        '  // BEFORE the route handler runs:\n\n'
        '  // 1. Read session cookie\n'
        '  const sessionId = event.cookies.get("session_id");\n\n'
        '  // 2. Verify and attach user to locals\n'
        '  if (sessionId) {\n'
        '    const user = await verifySession(sessionId);\n'
        '    if (user) {\n'
        '      event.locals.user = user;\n'
        '    } else {\n'
        '      event.cookies.delete("session_id", { path: "/" });\n'
        '    }\n'
        '  }\n\n'
        '  // 3. Run the actual route handler\n'
        '  const response = await resolve(event);\n\n'
        '  // AFTER the route handler runs:\n\n'
        '  // 4. Add security headers to every response\n'
        '  response.headers.set("X-Frame-Options", "DENY");\n'
        '  response.headers.set("X-Content-Type-Options", "nosniff");\n\n'
        '  return response;\n'
        '};',
        filename="The handle Hook", styles=styles
    ))

    story.append(h2("Sequence Multiple Hooks", styles))
    story.append(code_block(
        'import { sequence } from "@sveltejs/kit/hooks";\n'
        'import type { Handle } from "@sveltejs/kit";\n\n'
        'const authHandle: Handle = async ({ event, resolve }) => {\n'
        '  // Authentication logic...\n'
        '  const sessionId = event.cookies.get("session_id");\n'
        '  if (sessionId) {\n'
        '    event.locals.user = await verifySession(sessionId);\n'
        '  }\n'
        '  return resolve(event);\n'
        '};\n\n'
        'const loggingHandle: Handle = async ({ event, resolve }) => {\n'
        '  const start = Date.now();\n'
        '  const response = await resolve(event);\n'
        '  const duration = Date.now() - start;\n'
        '  console.log(`${event.request.method} ${event.url.pathname} ${duration}ms`);\n'
        '  return response;\n'
        '};\n\n'
        'const securityHandle: Handle = async ({ event, resolve }) => {\n'
        '  // CSRF check for non-GET requests\n'
        '  if (event.request.method !== "GET") {\n'
        '    const origin = event.request.headers.get("Origin");\n'
        '    const host = event.request.headers.get("Host");\n'
        '    if (!origin || new URL(origin).host !== host) {\n'
        '      return new Response("Forbidden", { status: 403 });\n'
        '    }\n'
        '  }\n'
        '  return resolve(event);\n'
        '};\n\n'
        '// Hooks run in order: security -> auth -> logging\n'
        'export const handle = sequence(\n'
        '  securityHandle,\n'
        '  authHandle,\n'
        '  loggingHandle\n'
        ');',
        filename="Sequencing Hooks", styles=styles
    ))

    story.append(h2("The handleError Hook", styles))
    story.append(code_block(
        '// src/hooks.server.ts\n'
        'import type { HandleServerError } from "@sveltejs/kit";\n\n'
        'export const handleError: HandleServerError = async ({\n'
        '  error,\n'
        '  event,\n'
        '  status,\n'
        '  message\n'
        '}) => {\n'
        '  // Log unexpected errors (500s)\n'
        '  console.error(`[${status}] ${event.url.pathname}:`, error);\n\n'
        '  // Report to error tracking service\n'
        '  // await sentry.captureException(error);\n\n'
        '  // Return a safe error message to the client\n'
        '  // (never expose stack traces or internal details)\n'
        '  return {\n'
        '    message: "An unexpected error occurred. Please try again."\n'
        '  };\n'
        '};',
        filename="Error Handling Hook", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can implement authentication, logging, and security middleware using hooks.", styles))
    story.append(page_break())

    # ================================================================
    # 7.7 API ROUTES
    # ================================================================
    story.append(h1("7.7 API Routes", styles))
    story.append(p(
        "API routes (+server.ts files) create HTTP endpoints that return data instead of HTML. Use them "
        "for building REST APIs, webhooks, and any endpoint that external services or your own client-side "
        "code needs to call."
    , styles))

    story.append(code_block(
        '// src/routes/api/stocks/+server.ts\n'
        'import { json } from "@sveltejs/kit";\n'
        'import type { RequestHandler } from "./$types";\n\n'
        'export const GET: RequestHandler = async ({ url }) => {\n'
        '  const search = url.searchParams.get("q") || "";\n'
        '  const stocks = await db.stock.findMany({\n'
        '    where: { ticker: { contains: search.toUpperCase() } },\n'
        '    take: 20\n'
        '  });\n\n'
        '  return json({ data: stocks });\n'
        '};\n\n'
        'export const POST: RequestHandler = async ({ request, locals }) => {\n'
        '  if (!locals.user) {\n'
        '    return new Response("Unauthorized", { status: 401 });\n'
        '  }\n\n'
        '  const body = await request.json();\n'
        '  const stock = await db.stock.create({ data: body });\n\n'
        '  return json({ data: stock }, { status: 201 });\n'
        '};\n\n'
        '// src/routes/api/stocks/[ticker]/+server.ts\n'
        'export const GET: RequestHandler = async ({ params }) => {\n'
        '  const stock = await db.stock.findUnique({\n'
        '    where: { ticker: params.ticker }\n'
        '  });\n\n'
        '  if (!stock) {\n'
        '    return new Response("Not Found", { status: 404 });\n'
        '  }\n\n'
        '  return json({ data: stock });\n'
        '};\n\n'
        'export const DELETE: RequestHandler = async ({ params, locals }) => {\n'
        '  if (!locals.user) {\n'
        '    return new Response("Unauthorized", { status: 401 });\n'
        '  }\n\n'
        '  await db.stock.delete({ where: { ticker: params.ticker } });\n'
        '  return new Response(null, { status: 204 });\n'
        '};',
        filename="API Routes", styles=styles
    ))

    story.append(principal_box(
        "Use form actions for user interactions (forms, buttons) and API routes for programmatic access "
        "(client-side fetch, external services, mobile apps). Form actions give you progressive enhancement "
        "for free. API routes give you a clean REST interface. Do not use API routes as a workaround for "
        "form actions — each has its purpose."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You can create API routes with GET, POST, PUT, and DELETE handlers.", styles))
    story.append(page_break())

    # ================================================================
    # 7.8 ADVANCED SVELTEKIT
    # ================================================================
    story.append(h1("7.8 Advanced SvelteKit Patterns", styles))

    story.append(h2("SSR, CSR, and Prerendering", styles))
    story.append(p(
        "SvelteKit gives you fine-grained control over how each page is rendered. You can mix and match "
        "strategies per route."
    , styles))

    story.append(code_block(
        '// src/routes/about/+page.ts\n'
        '// Page options (per-route configuration)\n\n'
        '// Prerender at build time (great for static content)\n'
        'export const prerender = true;\n\n'
        '// Disable SSR (client-only rendering)\n'
        '// export const ssr = false;\n\n'
        '// Disable client-side routing (full page loads)\n'
        '// export const csr = false;\n\n'
        '// ---\n\n'
        '// Common patterns:\n'
        '// prerender = true  -> Static marketing pages, docs, blog\n'
        '// ssr = true (default) -> Dynamic pages, dashboard, user content\n'
        '// ssr = false       -> Admin panels, heavy client-side apps\n'
        '// csr = false       -> Maximum security, no JS needed\n\n'
        '// You can also set these in +layout.ts to apply to all children',
        filename="Page Rendering Options", styles=styles
    ))

    story.append(h2("Environment Variables", styles))
    story.append(code_block(
        '// SvelteKit provides 4 modules for env vars:\n\n'
        '// 1. $env/static/private - Build-time, server-only\n'
        'import { DATABASE_URL, API_SECRET } from "$env/static/private";\n'
        '// Tree-shakeable, replaced at build time\n'
        '// NEVER accessible from client code\n\n'
        '// 2. $env/static/public - Build-time, available everywhere\n'
        'import { PUBLIC_APP_NAME } from "$env/static/public";\n'
        '// Must be prefixed with PUBLIC_\n'
        '// Safe to use in components\n\n'
        '// 3. $env/dynamic/private - Runtime, server-only\n'
        'import { env } from "$env/dynamic/private";\n'
        'const dbUrl = env.DATABASE_URL;  // Read at runtime\n'
        '// Useful when env vars change between deploys\n\n'
        '// 4. $env/dynamic/public - Runtime, available everywhere\n'
        'import { env } from "$env/dynamic/public";\n'
        'const appName = env.PUBLIC_APP_NAME;',
        filename="Environment Variables", styles=styles
    ))

    story.append(h2("Adapters and Deployment", styles))
    story.append(code_block(
        '// svelte.config.js\n'
        'import adapter from "@sveltejs/adapter-auto";  // Auto-detect platform\n'
        '// import adapter from "@sveltejs/adapter-node";  // Node.js server\n'
        '// import adapter from "@sveltejs/adapter-static"; // Static site\n'
        '// import adapter from "@sveltejs/adapter-vercel"; // Vercel\n'
        '// import adapter from "@sveltejs/adapter-netlify"; // Netlify\n\n'
        'export default {\n'
        '  kit: {\n'
        '    adapter: adapter({\n'
        '      // Adapter-specific options\n'
        '    })\n'
        '  }\n'
        '};\n\n'
        '// adapter-node: Deploy anywhere that runs Node.js\n'
        '//   npm run build && node build\n\n'
        '// adapter-static: Full static site (no server)\n'
        '//   All pages must be prerenderable\n'
        '//   Deploy to GitHub Pages, S3, Cloudflare Pages\n\n'
        '// adapter-vercel/netlify: Optimized for those platforms\n'
        '//   Serverless functions, edge functions, ISR',
        filename="SvelteKit Adapters", styles=styles
    ))

    story.append(h2("Preloading for Speed", styles))
    story.append(code_block(
        '<!-- SvelteKit preloads pages on hover/focus -->\n'
        '<!-- This happens automatically for <a> elements! -->\n\n'
        '<!-- Default: preload on hover (desktop) or tap start (mobile) -->\n'
        '<a href="/stocks/AAPL">Apple Stock</a>\n\n'
        '<!-- Preload more eagerly: on viewport enter -->\n'
        '<a href="/stocks/AAPL" data-sveltekit-preload-data="hover">Apple</a>\n\n'
        '<!-- Preload just the code, not data -->\n'
        '<a href="/stocks/AAPL" data-sveltekit-preload-code>Apple</a>\n\n'
        '<!-- Programmatic navigation with preloading -->\n'
        '<script>\n'
        '  import { goto, preloadData } from "$app/navigation";\n\n'
        '  async function goToStock(ticker) {\n'
        '    await preloadData(`/stocks/${ticker}`);\n'
        '    goto(`/stocks/${ticker}`);\n'
        '  }\n'
        '</script>',
        filename="Preloading Strategies", styles=styles
    ))

    story.append(principal_box(
        "SvelteKit's preloading is the single biggest performance win you can get for free. On desktop, "
        "it starts loading the next page as soon as the user hovers over a link \u2014 by the time they "
        "click, the page is already loaded. This makes navigation feel instant. Make sure your load "
        "functions are fast (under 200ms) to take full advantage."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand SSR/CSR/prerendering options, environment variables, adapters, "
                           "and preloading strategies.", styles))
    story.append(page_break())

    # ================================================================
    # 7.9 TRADEBOARD SVELTEKIT SETUP
    # ================================================================
    story.append(h1("7.9 TradeBoard SvelteKit Setup", styles))
    story.append(p(
        "Let us apply everything from this chapter to set up the TradeBoard application's full "
        "SvelteKit architecture."
    , styles))

    story.append(h2("Route Structure", styles))
    story.append(code_block(
        '// TradeBoard route architecture\n'
        '// src/routes/\n'
        '//\n'
        '// (marketing)/\n'
        '//   +layout.svelte         -> Clean marketing layout\n'
        '//   +page.svelte           -> Landing page (/)\n'
        '//   pricing/+page.svelte   -> Pricing page (/pricing)\n'
        '//   about/+page.svelte     -> About page (/about)\n'
        '//\n'
        '// (auth)/\n'
        '//   +layout.svelte         -> Centered card layout\n'
        '//   login/+page.svelte     -> Login (/login)\n'
        '//   login/+page.server.ts  -> Login action\n'
        '//   register/+page.svelte  -> Register (/register)\n'
        '//   register/+page.server.ts -> Register action\n'
        '//\n'
        '// (app)/\n'
        '//   +layout.svelte          -> App layout with sidebar\n'
        '//   +layout.server.ts       -> Auth check + user data\n'
        '//   dashboard/\n'
        '//     +page.svelte          -> Dashboard home (/dashboard)\n'
        '//     +page.server.ts       -> Load watchlist + summary\n'
        '//   stocks/\n'
        '//     +page.svelte          -> Stock search (/stocks)\n'
        '//     [ticker]/+page.svelte -> Stock detail (/stocks/AAPL)\n'
        '//     [ticker]/+page.server.ts -> Load stock data\n'
        '//   watchlist/\n'
        '//     +page.svelte          -> Watchlist (/watchlist)\n'
        '//     +page.server.ts       -> CRUD actions\n'
        '//   settings/\n'
        '//     +page.svelte          -> Settings (/settings)\n'
        '//     +page.server.ts       -> Update settings action\n'
        '//\n'
        '// api/\n'
        '//   stocks/+server.ts       -> Stock search API\n'
        '//   stocks/[ticker]/+server.ts -> Stock detail API\n'
        '//   watchlist/+server.ts    -> Watchlist CRUD API\n'
        '//   health/+server.ts       -> Health check endpoint',
        filename="TradeBoard Route Architecture", styles=styles
    ))

    story.append(h2("The App Layout with Auth", styles))
    story.append(code_block(
        '// src/routes/(app)/+layout.server.ts\n'
        'import { redirect } from "@sveltejs/kit";\n'
        'import type { LayoutServerLoad } from "./$types";\n\n'
        'export const load: LayoutServerLoad = async ({ locals }) => {\n'
        '  // Every page inside (app)/ requires authentication\n'
        '  if (!locals.user) {\n'
        '    throw redirect(302, "/login");\n'
        '  }\n\n'
        '  return {\n'
        '    user: {\n'
        '      id: locals.user.id,\n'
        '      name: locals.user.name,\n'
        '      email: locals.user.email\n'
        '    }\n'
        '  };\n'
        '};',
        filename="Protected Layout", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can architect a full SvelteKit application with route groups, layouts, "
                           "and protected routes.", styles))
    story.append(page_break())

    # ================================================================
    # 7.10 PRINCIPAL ENGINEER PATTERNS
    # ================================================================
    story.append(h1("7.10 Principal Engineer SvelteKit Patterns", styles))

    story.append(h2("Streaming Data with Promises", styles))
    story.append(code_block(
        '// src/routes/dashboard/+page.server.ts\n'
        '// Stream slow data while showing fast data immediately\n\n'
        'export const load: PageServerLoad = async ({ locals }) => {\n'
        '  // Fast query - await immediately\n'
        '  const user = await db.user.findUnique({\n'
        '    where: { id: locals.user.id }\n'
        '  });\n\n'
        '  // Slow query - DON\'T await, return the promise\n'
        '  const marketNews = fetchMarketNews();  // no await!\n'
        '  const recommendations = getRecommendations(locals.user.id);\n\n'
        '  return {\n'
        '    user,           // Available immediately\n'
        '    marketNews,     // Streamed when ready\n'
        '    recommendations // Streamed when ready\n'
        '  };\n'
        '};\n\n'
        '<!-- +page.svelte -->\n'
        '<script>\n'
        '  let { data } = $props();\n'
        '</script>\n\n'
        '<!-- Shows immediately -->\n'
        '<h1>Welcome, {data.user.name}</h1>\n\n'
        '<!-- Shows loading state, then content when ready -->\n'
        '{#await data.marketNews}\n'
        '  <Spinner />\n'
        '{:then news}\n'
        '  {#each news as item}\n'
        '    <NewsCard {item} />\n'
        '  {/each}\n'
        '{:catch error}\n'
        '  <p>Could not load news.</p>\n'
        '{/await}',
        filename="Data Streaming", styles=styles
    ))

    story.append(h2("Type-Safe Navigation", styles))
    story.append(code_block(
        '// src/lib/navigation.ts\n'
        '// Create type-safe route helpers\n\n'
        'export const routes = {\n'
        '  home: () => "/",\n'
        '  login: () => "/login",\n'
        '  register: () => "/register",\n'
        '  dashboard: () => "/dashboard",\n'
        '  stock: (ticker: string) => `/stocks/${ticker}`,\n'
        '  watchlist: () => "/watchlist",\n'
        '  settings: () => "/settings",\n'
        '  api: {\n'
        '    stocks: (query?: string) =>\n'
        '      query ? `/api/stocks?q=${query}` : "/api/stocks",\n'
        '    stock: (ticker: string) => `/api/stocks/${ticker}`,\n'
        '  }\n'
        '} as const;\n\n'
        '// Usage:\n'
        '// <a href={routes.stock("AAPL")}>Apple</a>\n'
        '// goto(routes.dashboard())\n'
        '// fetch(routes.api.stocks("AAPL"))',
        filename="Type-Safe Routes", styles=styles
    ))

    story.append(principal_box(
        "Streaming is the most underutilized SvelteKit feature. Most pages have a mix of fast and slow "
        "data. Show the fast stuff immediately and stream in the slow stuff. Users perceive your app as "
        "fast because they see content right away, even if some data is still loading. The key is "
        "returning promises from your load function instead of awaiting them."
    , styles))

    story.append(spacer(16))

    # ================================================================
    # EXERCISES
    # ================================================================
    story.append(h1("Chapter 7 Exercises", styles))
    story.append(HorizontalLine())
    story.append(spacer(8))

    story.append(exercise(1, "Basic SvelteKit Routes", [
        ('ExerciseBody', '<b>Task:</b> Create a SvelteKit app with the following routes: a home page (/), '
         'an about page (/about), and a contact page (/contact). Add a root layout with navigation links '
         'to all three pages. Each page should display its title and some placeholder content. Add a '
         'custom error page that shows a friendly 404 message.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(2, "Dynamic Stock Pages", [
        ('ExerciseBody', '<b>Task:</b> Create a stock detail page at /stocks/[ticker]. Implement a server '
         'load function that receives the ticker parameter and returns mock stock data (price, change, '
         'volume, market cap). Display this data on the page. Handle the case where the ticker is not '
         'found by throwing a 404 error. Add a stock listing page at /stocks that links to 5 different '
         'stock pages.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(3, "Login Form with Actions", [
        ('ExerciseBody', '<b>Task:</b> Build a login form using SvelteKit form actions. The form should '
         'have email and password fields. The server action should validate that both fields are present, '
         'check against hardcoded credentials (email: admin@test.com, password: password123), return '
         'validation errors with fail(), and redirect to /dashboard on success. Use use:enhance for '
         'progressive enhancement. Show error messages from form.error.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(4, "Protected Dashboard with Hooks", [
        ('ExerciseBody', '<b>Task:</b> Implement authentication using hooks. Create a handle hook that '
         'reads a session cookie and attaches user data to event.locals. Create a (app) route group '
         'with a layout that checks for locals.user and redirects to /login if not authenticated. '
         'Add a dashboard page that displays user information from the layout data. Add login/logout '
         'functionality using form actions and cookies.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(5, "Full TradeBoard API", [
        ('ExerciseBody', '<b>Task:</b> Build the complete TradeBoard API layer. Create API routes for: '
         'GET /api/stocks (list with search and pagination), GET /api/stocks/[ticker] (detail), '
         'POST /api/watchlist (add stock), DELETE /api/watchlist/[ticker] (remove stock). Add '
         'authentication checks, input validation with Zod, proper HTTP status codes, and consistent '
         'error responses. Implement rate limiting in a hook. Write a streaming load function that '
         'fetches fast and slow data in parallel.'),
    ], styles))

    story.append(spacer(16))
    story.append(checkpoint("You have mastered SvelteKit: routing, data loading, form actions, layouts, "
                           "hooks, API routes, and advanced patterns like streaming and prerendering.", styles))
    story.append(page_break())

    return story
