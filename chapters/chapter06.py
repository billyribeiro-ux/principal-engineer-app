#!/usr/bin/env python3
"""Chapter 6: Svelte 5 - The Modern UI Framework"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_6(styles):
    story = []

    # Cover
    story.append(ChapterCoverPage(6, "Svelte 5 — The Modern UI Framework", "Your Construction Crew That Builds at the Factory", "PART 2: LEVELING UP"))
    story.append(PageBreak())

    # ── 6.1 Why Svelte 5 ──────────────────────────────────────────────────────
    story.append(h1("6.1 Why Svelte 5?", styles))
    story.append(p(
        "React and Vue ship a runtime library to the browser that interprets your component code at runtime. "
        "Svelte takes a radically different approach: it is a <b>compiler</b>. Your .svelte files are compiled "
        "at build time into tight, vanilla JavaScript with no framework overhead in the bundle.",
        styles
    ))
    story.append(analogy_box(
        "<b>Factory vs. Shipping Crew:</b> React is like hiring a skilled crew that shows up to your job site every day (the browser) with a "
        "full tool truck (the runtime). They're great, but every client pays for that truck. Svelte is like "
        "a factory that pre-fabricates your walls, cabinets, and wiring off-site. By the time anything "
        "reaches the browser, it's already purpose-built vanilla JS — no tool truck needed.",
        styles
    ))
    story.append(p("Key advantages of Svelte 5 over its predecessors and competitors:", styles))
    story.append(bullet("No virtual DOM diffing — direct DOM mutations generated at compile time", styles))
    story.append(bullet("Smaller bundles — only the code your component uses is emitted", styles))
    story.append(bullet("Runes system — explicit, fine-grained reactivity replacing the magic $: label syntax", styles))
    story.append(bullet("Snippets — reusable markup fragments replacing slots", styles))
    story.append(bullet("First-class TypeScript support throughout", styles))
    story.append(bullet("Performance on par with or exceeding hand-written DOM code", styles))
    story.append(p(
        "Svelte 5 introduced <b>runes</b> — compiler-understood function calls (prefixed with $) that "
        "declare reactive state, derived values, and side effects. They replace the implicit reactivity "
        "of Svelte 3/4 with something explicit and composable.",
        styles
    ))
    story.append(principal_box(
        "<b>PE Principle: Choose the right abstraction level:</b> Svelte's compiler approach means the abstraction cost is paid at build time, not runtime. "
        "For performance-critical UIs — trading dashboards, real-time data grids — this matters. "
        "A principal engineer chooses tools whose costs align with where they can afford to pay them.",
        styles
    ))

    # ── 6.2 First Component ───────────────────────────────────────────────────
    story.append(h1("6.2 Your First Svelte 5 Component", styles))
    story.append(p(
        "A .svelte file has three optional sections: a script block, markup, and a style block. "
        "Each component is a self-contained unit — styles are scoped by default.",
        styles
    ))
    story.append(analogy_box(
        "<b>The Self-Contained Room:</b> A Svelte component is like a hotel room: it has its own furniture (markup), its own decor "
        "rules (scoped styles), and its own logic (script). Guests in room 201 can't accidentally "
        "move furniture in room 202 — style scoping prevents collisions.",
        styles
    ))
    story.append(code_block(
        '''<!-- StockTicker.svelte -->
<script lang="ts">
  // Rune-based reactive state
  let price = $state(142.50);
  let symbol = $state("AAPL");
  let change = $derived(price - 140.00);
  let changePercent = $derived(((change / 140.00) * 100).toFixed(2));

  function refresh() {
    // Simulate a price update
    price = +(price + (Math.random() - 0.5) * 2).toFixed(2);
  }
</script>

<div class="ticker">
  <span class="symbol">{symbol}</span>
  <span class="price">${price.toFixed(2)}</span>
  <span class="change" class:positive={change >= 0} class:negative={change < 0}>
    {change >= 0 ? "+" : ""}{change.toFixed(2)} ({changePercent}%)
  </span>
  <button onclick={refresh}>Refresh</button>
</div>

<style>
  /* Scoped — only applies inside this component */
  .ticker {
    display: flex;
    gap: 1rem;
    align-items: center;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    background: #1a1a2e;
    color: white;
    font-family: "Courier New", monospace;
  }
  .symbol { font-weight: bold; font-size: 1.1rem; }
  .price  { font-size: 1.2rem; }
  .positive { color: #22c55e; }
  .negative { color: #ef4444; }
</style>''',
        styles
    ))
    story.append(p(
        "Notice <b>lang=\"ts\"</b> on the script tag — TypeScript works out of the box. "
        "Event handlers use the new <b>onclick</b> attribute (no on:click in Svelte 5). "
        "The <b>class:</b> directive conditionally applies CSS classes.",
        styles
    ))

    # ── 6.3 Runes ─────────────────────────────────────────────────────────────
    story.append(h1("6.3 Runes — The Reactivity System", styles))
    story.append(p(
        "Runes are special compiler-recognized calls that express reactive intent. "
        "They look like function calls but are transformed at compile time.",
        styles
    ))

    story.append(h2("$state — The Whiteboard", styles))
    story.append(analogy_box(
        "<b>$state — The Whiteboard:</b> Think of $state as a whiteboard in the office. Anyone can look at it, and whenever "
        "you erase and rewrite it, everyone who was watching automatically updates their understanding. "
        "The compiler wires up exactly who watches which whiteboard.",
        styles
    ))
    story.append(code_block(
        '''<script lang="ts">
  // Primitive state
  let count = $state(0);
  let name  = $state("Alice");

  // Object state — deep reactivity, mutations are tracked
  let user = $state({ name: "Alice", age: 30, scores: [95, 87, 92] });

  function birthday() {
    user.age++;              // mutation tracked automatically
    user.scores.push(99);    // array mutation also tracked
  }

  // Class with runes
  class Cart {
    items = $state<string[]>([]);
    total = $derived(this.items.length);

    add(item: string) { this.items.push(item); }
    remove(i: number) { this.items.splice(i, 1); }
  }

  const cart = new Cart();
</script>''',
        styles
    ))

    story.append(h2("$derived — The Calculator", styles))
    story.append(analogy_box(
        "<b>$derived — The Calculator:</b> A $derived value is like a calculator display: you never manually set it. "
        "You change the inputs, and the display updates itself. Try to write to it and "
        "the compiler stops you — calculators don't take input on their display.",
        styles
    ))
    story.append(code_block(
        '''<script lang="ts">
  let prices = $state([142.50, 98.30, 215.00]);
  let quantity = $state(10);

  // Simple derived
  const total = $derived(prices.reduce((s, p) => s + p, 0) * quantity);

  // $derived.by for multi-line logic
  const stats = $derived.by(() => {
    const sorted = [...prices].sort((a, b) => a - b);
    return {
      min: sorted[0],
      max: sorted[sorted.length - 1],
      avg: +(prices.reduce((s, p) => s + p, 0) / prices.length).toFixed(2),
    };
  });
</script>

<p>Total: ${total.toFixed(2)}</p>
<p>Min: ${stats.min} | Max: ${stats.max} | Avg: ${stats.avg}</p>''',
        styles
    ))

    story.append(h2("$effect — The Watchdog", styles))
    story.append(analogy_box(
        "<b>$effect — The Watchdog:</b> A $effect is a watchdog process. Every time state it reads changes, it runs again. "
        "It can also clean up after itself — like a guard who locks the previous door before "
        "moving to the next post. Return a cleanup function and Svelte calls it automatically.",
        styles
    ))
    story.append(code_block(
        '''<script lang="ts">
  let symbol = $state("AAPL");
  let ws: WebSocket | null = null;

  // Runs after mount and whenever `symbol` changes
  $effect(() => {
    ws = new WebSocket(`wss://prices.example.com/${symbol}`);
    ws.onmessage = (e) => { /* handle */ };

    // Cleanup: called before next run or on destroy
    return () => {
      ws?.close();
      ws = null;
    };
  });

  // $effect.pre runs BEFORE DOM updates — useful for measurements
  $effect.pre(() => {
    console.log("About to paint, current symbol:", symbol);
  });
</script>''',
        styles
    ))

    story.append(h2("$props and $bindable", styles))
    story.append(code_block(
        '''<!-- PriceCard.svelte -->
<script lang="ts">
  interface Props {
    symbol: string;
    price: number;
    currency?: string;       // optional with default
    onSelect?: () => void;   // callback prop
  }

  // Destructure with defaults
  let { symbol, price, currency = "USD", onSelect }: Props = $props();

  // $bindable allows parent to two-way bind this prop
  let { value = $bindable(0) } = $props();
</script>

<div onclick={onSelect} role="button" tabindex="0">
  <strong>{symbol}</strong>
  <span>{currency} {price.toFixed(2)}</span>
</div>''',
        styles
    ))

    story.append(h2("$inspect — Debug Utility", styles))
    story.append(code_block(
        '''<script lang="ts">
  let count = $state(0);

  // Logs to console whenever count changes (dev only — stripped in prod)
  $inspect(count);

  // Custom handler
  $inspect(count).with((type, value) => {
    console.table({ type, value });
  });
</script>''',
        styles
    ))
    story.append(mistake_box(
        "<b>Svelte 4 vs Svelte 5 Syntax:</b> Never mix Svelte 4 and Svelte 5 syntax. In Svelte 5: use $state() not let x = 0 for "
        "reactive variables, use onclick not on:click, use $props() not export let, and use "
        "snippets not slots. Mixing causes confusing compiler errors.",
        styles
    ))

    # ── 6.4 Component Composition ─────────────────────────────────────────────
    story.append(h1("6.4 Component Composition", styles))
    story.append(p(
        "Svelte 5 replaces slots with <b>snippets</b> — named, typed, reusable markup fragments "
        "that can receive arguments. This is strictly more powerful than slot-based composition.",
        styles
    ))
    story.append(code_block(
        '''<!-- DataTable.svelte — parent uses snippets -->
<script lang="ts">
  import type { Snippet } from "svelte";

  interface Props {
    rows: unknown[];
    header: Snippet;
    row: Snippet<[unknown, number]>;  // receives (item, index)
    empty?: Snippet;
  }

  let { rows, header, row, empty }: Props = $props();
</script>

<table>
  <thead>{@render header()}</thead>
  <tbody>
    {#if rows.length === 0}
      {@render empty?.()}
    {:else}
      {#each rows as item, i}
        <tr>{@render row(item, i)}</tr>
      {/each}
    {/if}
  </tbody>
</table>''',
        styles
    ))
    story.append(code_block(
        '''<!-- Usage of DataTable with snippets -->
<script lang="ts">
  import DataTable from "./DataTable.svelte";

  interface Stock { symbol: string; price: number; change: number; }
  let stocks = $state<Stock[]>([
    { symbol: "AAPL", price: 142.50, change: 1.2 },
    { symbol: "GOOG", price: 2815.00, change: -0.8 },
  ]);
</script>

<DataTable rows={stocks}>
  {#snippet header()}
    <tr><th>Symbol</th><th>Price</th><th>Change %</th></tr>
  {/snippet}

  {#snippet row(stock: Stock, i: number)}
    <td>{stock.symbol}</td>
    <td>${stock.price.toFixed(2)}</td>
    <td class:positive={stock.change > 0}>{stock.change}%</td>
  {/snippet}

  {#snippet empty()}
    <tr><td colspan="3">No stocks to display</td></tr>
  {/snippet}
</DataTable>''',
        styles
    ))
    story.append(p(
        "Callback props replace event forwarding. Pass functions as props instead of "
        "dispatching custom events — this is more TypeScript-friendly and explicit.",
        styles
    ))

    # ── 6.5 Control Flow ──────────────────────────────────────────────────────
    story.append(h1("6.5 Control Flow", styles))
    story.append(code_block(
        '''<!-- Conditional rendering -->
{#if user.isLoggedIn}
  <Dashboard {user} />
{:else if user.isPending}
  <LoadingSpinner />
{:else}
  <LoginForm />
{/if}

<!-- List rendering — always key by unique id for efficient diffing -->
{#each stocks as stock (stock.symbol)}
  <StockRow {stock} />
{:else}
  <p>No stocks found.</p>
{/each}

<!-- Async blocks -->
{#await fetchPrice(symbol)}
  <Skeleton />
{:then data}
  <PriceDisplay price={data.price} />
{:catch error}
  <ErrorMessage message={error.message} />
{/await}

<!-- Raw HTML (sanitize first!) -->
{@html sanitizedContent}

<!-- Local constant to avoid recomputing in template -->
{@const discounted = price * 0.9}
<p>Sale price: ${discounted.toFixed(2)}</p>''',
        styles
    ))
    story.append(principal_box(
        "<b>Always key your {#each} blocks:</b> Without a key, Svelte patches DOM nodes in place. With a key like (item.id), "
        "Svelte knows exactly which node to move, update, or remove. Unkeyed lists cause "
        "subtle bugs with animations, inputs retaining wrong values, and O(n) unnecessary work.",
        styles
    ))

    # ── 6.6 Bindings ──────────────────────────────────────────────────────────
    story.append(h1("6.6 Bindings", styles))
    story.append(code_block(
        '''<script lang="ts">
  let name    = $state("");
  let accepted = $state(false);
  let size    = $state<"S" | "M" | "L">("M");
  let sizes   = $state<string[]>([]);
  let canvasEl: HTMLCanvasElement;

  // Component with $bindable prop
  // In child: let { value = $bindable() } = $props();
  let childValue = $state(0);
</script>

<!-- Text input — two-way bind -->
<input type="text"  bind:value={name} placeholder="Your name" />

<!-- Checkbox -->
<input type="checkbox" bind:checked={accepted} />
<label>I accept the terms</label>

<!-- Radio group — bind:group shares state across radios -->
{#each ["S", "M", "L"] as s}
  <input type="radio" bind:group={size} value={s} id="size-{s}" />
  <label for="size-{s}">{s}</label>
{/each}

<!-- Multi-select checkbox group -->
{#each ["Tech", "Finance", "Health"] as sector}
  <input type="checkbox" bind:group={sizes} value={sector} />
  <label>{sector}</label>
{/each}

<!-- DOM element reference -->
<canvas bind:this={canvasEl} width="400" height="300"></canvas>

<!-- Component binding — child must expose $bindable prop -->
<Counter bind:value={childValue} />
<p>Child value from parent: {childValue}</p>''',
        styles
    ))

    # ── 6.7 Lifecycle ─────────────────────────────────────────────────────────
    story.append(h1("6.7 Lifecycle with $effect", styles))
    story.append(p(
        "In Svelte 5, $effect replaces onMount and onDestroy for most use cases. "
        "Effects run after the DOM is updated and return an optional cleanup function.",
        styles
    ))
    story.append(code_block(
        '''<script lang="ts">
  import { onMount, onDestroy } from "svelte"; // still available for compat

  let chartEl: HTMLDivElement;
  let chart: Chart | null = null;
  let data = $state<number[]>([]);

  // Equivalent of onMount + onDestroy combined
  $effect(() => {
    // Runs once on mount (no reactive reads = no re-runs)
    chart = new Chart(chartEl, { type: "line", data: { datasets: [] } });

    return () => {
      chart?.destroy();  // cleanup on component destroy
      chart = null;
    };
  });

  // Re-runs whenever `data` changes
  $effect(() => {
    if (!chart) return;
    chart.data.datasets[0].data = data;
    chart.update();
  });

  // $effect.pre — before DOM paint, for measurements
  $effect.pre(() => {
    const height = chartEl?.offsetHeight;
    console.log("Pre-paint height:", height);
  });
</script>

<div bind:this={chartEl}></div>''',
        styles
    ))
    story.append(mistake_box(
        "<b>Avoid reading reactive state you don't intend to track:</b> Every $state variable read inside an $effect body creates a subscription. "
        "If you read a value for a one-time setup but don't want re-runs, use "
        "untrack(() => myState) from 'svelte' to opt out of tracking for that read.",
        styles
    ))

    # ── 6.8 Stores & Shared State ─────────────────────────────────────────────
    story.append(h1("6.8 Stores & Shared State", styles))
    story.append(code_block(
        '''<!-- stores/watchlist.ts -->
import { writable, readable, derived, get } from "svelte/store";

// Writable store — read/write from anywhere
export const watchlist = writable<string[]>(
  JSON.parse(localStorage.getItem("watchlist") ?? "[]")
);

// Persist to localStorage whenever it changes
watchlist.subscribe((val) => {
  localStorage.setItem("watchlist", JSON.stringify(val));
});

// Readable store — external data source
export const serverTime = readable<Date>(new Date(), (set) => {
  const id = setInterval(() => set(new Date()), 1000);
  return () => clearInterval(id);  // cleanup
});

// Derived store — computed from others
export const watchlistCount = derived(watchlist, ($wl) => $wl.length);

// Custom store with methods
function createPriceStore() {
  const { subscribe, update, set } = writable<Record<string, number>>({});
  return {
    subscribe,
    updatePrice(symbol: string, price: number) {
      update((prices) => ({ ...prices, [symbol]: price }));
    },
    reset: () => set({}),
  };
}
export const prices = createPriceStore();''',
        styles
    ))
    story.append(code_block(
        '''<!-- In a .svelte component — auto-subscription with $ prefix -->
<script lang="ts">
  import { watchlist, prices, watchlistCount } from "$lib/stores/watchlist";

  // $store auto-subscribes and unsubscribes on destroy
  // No need to call .subscribe() manually
</script>

<p>Watching {$watchlistCount} stocks</p>
<ul>
  {#each $watchlist as symbol (symbol)}
    <li>{symbol}: ${($prices[symbol] ?? 0).toFixed(2)}</li>
  {/each}
</ul>''',
        styles
    ))

    story.append(h2("Context API — Component-Scoped Globals", styles))
    story.append(code_block(
        '''<!-- Parent.svelte -->
<script lang="ts">
  import { setContext } from "svelte";
  import { writable } from "svelte/store";

  const theme = writable<"light" | "dark">("dark");
  setContext("theme", theme);
</script>

<!-- DeepChild.svelte (any depth) -->
<script lang="ts">
  import { getContext } from "svelte";
  import type { Writable } from "svelte/store";

  const theme = getContext<Writable<"light" | "dark">>("theme");
</script>
<div class="container" data-theme={$theme}>...</div>''',
        styles
    ))
    story.append(principal_box(
        "<b>Store vs Context vs Runes — When to Use What:</b> Use $state in a .svelte.ts file (a 'rune module') for app-level state that benefits "
        "from the compiler's fine-grained tracking. Use stores when you need store contracts "
        "(subscribe/set/update) for interop. Use context for component-tree-scoped data "
        "where you don't want prop drilling but also don't want global state.",
        styles
    ))

    # ── 6.9 Transitions ───────────────────────────────────────────────────────
    story.append(h1("6.9 Transitions & Animations", styles))
    story.append(analogy_box(
        "<b>Choreographed Entrance:</b> Transitions are like a choreographed entrance at a gala. Each guest (element) "
        "knows their cue — fade in, slide from left, scale up. The director (Svelte) "
        "coordinates so nothing collides. The `in:` and `out:` directives let you specify "
        "different choreography for entering vs leaving.",
        styles
    ))
    story.append(code_block(
        '''<script lang="ts">
  import { fade, fly, slide, scale } from "svelte/transition";
  import { flip } from "svelte/animate";
  import { quintOut } from "svelte/easing";

  let visible = $state(true);
  let items   = $state(["AAPL", "GOOG", "MSFT"]);

  function addItem() { items = [...items, "AMZN"]; }
  function removeItem(sym: string) { items = items.filter(s => s !== sym); }

  // Custom transition
  function typewriter(node: Element, { speed = 40 } = {}) {
    const text = node.textContent ?? "";
    return {
      duration: text.length * speed,
      tick: (t: number) => {
        node.textContent = text.slice(0, Math.trunc(text.length * t));
      },
    };
  }
</script>

{#if visible}
  <!-- Different in/out transitions -->
  <div in:fly={{ y: -20, duration: 300 }} out:fade={{ duration: 200 }}>
    <h2 transition:slide={{ duration: 400, easing: quintOut }}>
      Market Summary
    </h2>
  </div>
{/if}

<!-- Animated list with FLIP -->
<ul>
  {#each items as sym (sym)}
    <li animate:flip={{ duration: 300 }}
        in:fly={{ x: -50, duration: 300 }}
        out:fade={{ duration: 200 }}>
      {sym}
      <button onclick={() => removeItem(sym)}>×</button>
    </li>
  {/each}
</ul>

<p use:typewriter={{ speed: 30 }}>Live market data...</p>''',
        styles
    ))

    # ── 6.10 Actions ──────────────────────────────────────────────────────────
    story.append(h1("6.10 Actions (use: Directive)", styles))
    story.append(analogy_box(
        "<b>USB Dongle:</b> An action is like a USB dongle — a self-contained capability you plug into any DOM node. "
        "The node doesn't need to know about the action; it just gains new powers: "
        "click-outside detection, tooltip behavior, intersection observation.",
        styles
    ))
    story.append(code_block(
        '''<!-- actions/index.ts -->
import type { Action } from "svelte/action";

// Click-outside action
export const clickOutside: Action<HTMLElement, () => void> = (node, callback) => {
  function handle(event: MouseEvent) {
    if (!node.contains(event.target as Node)) callback?.();
  }
  document.addEventListener("click", handle, true);
  return {
    destroy() { document.removeEventListener("click", handle, true); },
    update(newCb) { callback = newCb; },
  };
};

// Tooltip action
export const tooltip: Action<HTMLElement, string> = (node, text) => {
  let tip: HTMLDivElement | null = null;

  function show() {
    tip = document.createElement("div");
    tip.className = "tooltip";
    tip.textContent = text;
    document.body.appendChild(tip);
    const rect = node.getBoundingClientRect();
    tip.style.cssText =
      `top:${rect.top - 36 + window.scrollY}px;left:${rect.left}px;position:absolute`;
  }
  function hide() { tip?.remove(); tip = null; }

  node.addEventListener("mouseenter", show);
  node.addEventListener("mouseleave", hide);

  return {
    destroy() {
      node.removeEventListener("mouseenter", show);
      node.removeEventListener("mouseleave", hide);
      hide();
    },
    update(newText) { text = newText; },
  };
};

// Intersection observer action
export const inView: Action<HTMLElement, (visible: boolean) => void> = (node, cb) => {
  const obs = new IntersectionObserver(([entry]) => cb(entry.isIntersecting));
  obs.observe(node);
  return { destroy() { obs.disconnect(); } };
};''',
        styles
    ))
    story.append(code_block(
        '''<!-- Using actions in a component -->
<script lang="ts">
  import { clickOutside, tooltip, inView } from "$lib/actions";

  let open = $state(false);
  let loaded = $state(false);
</script>

<div use:clickOutside={() => (open = false)}>
  {#if open}<Dropdown />{/if}
</div>

<button use:tooltip={"Refresh prices"} onclick={refresh}>
  Refresh
</button>

<div use:inView={(visible) => { if (visible) loaded = true; }}>
  {#if loaded}<HeavyChart />{/if}
</div>''',
        styles
    ))

    # ── 6.11 Advanced Patterns ────────────────────────────────────────────────
    story.append(h1("6.11 Advanced Patterns", styles))

    story.append(h2("Dynamic Components & Special Elements", styles))
    story.append(code_block(
        '''<script lang="ts">
  import StockRow from "./StockRow.svelte";
  import CryptoRow from "./CryptoRow.svelte";

  type RowType = "stock" | "crypto";
  let rowType = $state<RowType>("stock");

  const components = { stock: StockRow, crypto: CryptoRow } as const;
</script>

<!-- Dynamic component selection -->
<svelte:component this={components[rowType]} price={142.50} />

<!-- Window/document event listeners — no manual cleanup needed -->
<svelte:window onkeydown={(e) => { if (e.key === "Escape") closeModal(); }} />
<svelte:document onclick={handleGlobalClick} />

<!-- Inject into document <head> -->
<svelte:head>
  <title>TradeBoard — {symbol}</title>
  <meta name="description" content="Live prices for {symbol}" />
</svelte:head>

<!-- Dynamic element tag -->
<svelte:element this={headingLevel === 1 ? "h1" : "h2"} class="title">
  Market Overview
</svelte:element>''',
        styles
    ))

    story.append(h2("Recursive Components", styles))
    story.append(code_block(
        '''<!-- TreeNode.svelte — renders a nested portfolio tree -->
<script lang="ts">
  import TreeNode from "./TreeNode.svelte"; // self-import is fine

  interface Node { name: string; value: number; children?: Node[]; }
  let { node, depth = 0 }: { node: Node; depth?: number } = $props();
</script>

<div style="padding-left: {depth * 1.5}rem">
  <span>{node.name}: ${node.value.toLocaleString()}</span>
  {#if node.children}
    {#each node.children as child (child.name)}
      <svelte:self node={child} depth={depth + 1} />
    {/each}
  {/if}
</div>''',
        styles
    ))

    story.append(h2("class: and style: Directives", styles))
    story.append(code_block(
        '''<script lang="ts">
  let active = $state(false);
  let color  = $state("#22c55e");
  let opacity = $state(1);
</script>

<!-- class: directive — cleaner than ternaries in class attr -->
<button
  class="btn"
  class:active={active}
  class:disabled={!active}
  onclick={() => (active = !active)}
>
  Toggle
</button>

<!-- style: directive — reactive inline styles -->
<div
  style:color={color}
  style:opacity={opacity}
  style:transition="opacity 0.3s ease"
>
  Styled dynamically
</div>''',
        styles
    ))

    # ── 6.12 Svelte at PE Level ───────────────────────────────────────────────
    story.append(h1("6.12 Svelte at Principal Engineer Level", styles))

    story.append(h2("Performance", styles))
    story.append(bullet("Prefer $derived over redundant $effect chains — derived values are synchronous and skip the microtask queue", styles))
    story.append(bullet("Use {#key expr} to force full remount when identity changes (e.g., navigating between user profiles)", styles))
    story.append(bullet("Virtualize long lists with svelte-virtual or a custom action — the DOM is the bottleneck, not Svelte", styles))
    story.append(bullet("Lazy-load heavy components with dynamic import() inside {#await} blocks", styles))

    story.append(h2("State Management at Scale", styles))
    story.append(code_block(
        '''// state/portfolio.svelte.ts — rune module (not a component)
// .svelte.ts files can use runes outside components!

export class PortfolioStore {
  positions = $state<Map<string, number>>(new Map());
  prices    = $state<Map<string, number>>(new Map());

  totalValue = $derived.by(() => {
    let total = 0;
    for (const [sym, qty] of this.positions) {
      total += (this.prices.get(sym) ?? 0) * qty;
    }
    return total;
  });

  updatePrice(symbol: string, price: number) {
    this.prices.set(symbol, price);
  }

  addPosition(symbol: string, qty: number) {
    const current = this.positions.get(symbol) ?? 0;
    this.positions.set(symbol, current + qty);
  }
}

// Singleton — import and use anywhere
export const portfolio = new PortfolioStore();''',
        styles
    ))

    story.append(h2("Component Library Design", styles))
    story.append(bullet("Use $props() with explicit TypeScript interfaces — never use any or unknown for prop types", styles))
    story.append(bullet("Export prop types alongside components for consumers: export type { ButtonProps }", styles))
    story.append(bullet("Design for composition: accept snippets for customizable regions instead of boolean flags", styles))
    story.append(bullet("Use CSS custom properties (variables) for theming — consumers override at root, not in your code", styles))

    story.append(h2("Testing", styles))
    story.append(code_block(
        '''// StockCard.test.ts
import { render, screen, fireEvent } from "@testing-library/svelte";
import StockCard from "./StockCard.svelte";

test("displays price and updates on refresh", async () => {
  const { component } = render(StockCard, {
    props: { symbol: "AAPL", initialPrice: 142.50 },
  });

  expect(screen.getByText("AAPL")).toBeInTheDocument();
  expect(screen.getByText(/142\.50/)).toBeInTheDocument();

  await fireEvent.click(screen.getByRole("button", { name: /refresh/i }));
  // After refresh, price should have changed
  expect(screen.queryByText(/142\.50/)).not.toBeInTheDocument();
});

test("emits onSelect callback when clicked", async () => {
  const onSelect = vi.fn();
  render(StockCard, { props: { symbol: "AAPL", price: 142.50, onSelect } });

  await fireEvent.click(screen.getByRole("button"));
  expect(onSelect).toHaveBeenCalledOnce();
});''',
        styles
    ))

    story.append(h2("Accessibility (a11y)", styles))
    story.append(bullet("Svelte's compiler warns on a11y violations at build time — treat them as errors, not warnings", styles))
    story.append(bullet("Use role, aria-label, and aria-live for dynamic content like price tickers", styles))
    story.append(bullet("Test with keyboard navigation — all interactive elements must be reachable and operable via keyboard", styles))
    story.append(bullet("Provide prefers-reduced-motion alternatives for all transitions and animations", styles))
    story.append(code_block(
        '''<!-- a11y-aware ticker -->
<script lang="ts">
  import { prefersReducedMotion } from "$lib/utils";
  let price = $state(142.50);
</script>

<output
  aria-live="polite"
  aria-atomic="true"
  aria-label="Current price for AAPL"
>
  ${price.toFixed(2)}
</output>

{#if !prefersReducedMotion}
  <div transition:fly={{ y: -8, duration: 300 }}>Updated!</div>
{/if}''',
        styles
    ))
    story.append(principal_box(
        "<b>PE Principle: Svelte's compiler is your first reviewer:</b> Treat every Svelte compiler warning as a code review comment from a senior engineer. "
        "The a11y warnings, unused CSS selectors, missing keys — these are the compiler "
        "catching real bugs before they ship. A principal engineer configures CI to fail "
        "on warnings, not just errors.",
        styles
    ))

    # ── Checkpoint ────────────────────────────────────────────────────────────
    story.append(checkpoint("Chapter 6 Checkpoint: Svelte 5 Mastery", styles))
    story.append(bullet("You understand why Svelte's compiler approach differs from runtime frameworks", styles))
    story.append(bullet("You can create .svelte components with TypeScript", styles))
    story.append(bullet("You can declare reactive state with $state, $derived, and $effect", styles))
    story.append(bullet("You can compose components using $props() and snippets", styles))
    story.append(bullet("You can use control flow: if, each with keys, await", styles))
    story.append(bullet("You can bind form inputs with bind:value, bind:checked, bind:group", styles))
    story.append(bullet("You can use stores and auto-subscribe with $", styles))
    story.append(bullet("You can add transitions and animate list reordering with flip", styles))
    story.append(bullet("You can write and apply actions with the use: directive", styles))
    story.append(bullet("You understand context API vs stores vs rune modules", styles))
    story.append(PageBreak())

    # ── Exercises ─────────────────────────────────────────────────────────────
    story.append(h1("Chapter 6 Exercises", styles))

    story.append(exercise(
        1,
        "Rebuild TradeBoard Stock Table as Svelte Component",
        [
            ("BulletText", "Create StockTable.svelte with typed props: stocks: Stock[]"),

            ("BulletText", "Use #each stocks as stock (stock.symbol) with key"),

            ("BulletText", "Add a sort-by-column feature using $derived and $state for sortKey and sortDir"),

            ("BulletText", "Style with scoped CSS — alternating row colors, positive/negative change color"),

            ("BulletText", "Add a search/filter input bound with bind:value that filters the list in real-time"),
        ],
        styles
    ))

    story.append(exercise(
        2,
        "StockCard Component with Typed Props",
        [
            ("BulletText", "Create StockCard.svelte with interface Props  symbol, price, change, onSelect?: () => void "),

            ("BulletText", "Display symbol, formatted price, change with color-coded badge"),

            ("BulletText", "Add click handler that calls onSelect callback prop"),

            ("BulletText", "Export a 'selected' $bindable prop so parent can two-way bind selection state"),

            ("BulletText", "Add transition:scale when the card mounts using in:scale= duration: 200 "),
        ],
        styles
    ))

    story.append(exercise(
        3,
        "Complete Watchlist with localStorage and Derived Stats",
        [
            ("BulletText", "Create stores/watchlist.svelte.ts rune module exporting a WatchlistStore class"),

            ("BulletText", "Persist watchlist to localStorage via $effect in the store class"),

            ("BulletText", "Add $derived stats: totalValue, bestPerformer, worstPerformer, avgChange"),

            ("BulletText", "Build WatchlistPanel.svelte that shows the list and stats"),

            ("BulletText", "Add ability to add/remove symbols with animated list transitions using fly and flip"),
        ],
        styles
    ))

    story.append(exercise(
        4,
        "Real-Time Price Ticker with WebSocket Simulation",
        [
            ("BulletText", "Create a PriceFeed action (use:priceFeed) that simulates a WebSocket with setInterval"),

            ("BulletText", "The action dispatches custom 'priceupdate' events with  symbol, price, change "),

            ("BulletText", "Build TickerTape.svelte: a horizontal scrolling list of live prices"),

            ("BulletText", "Use $effect to subscribe to price events and update $state"),

            ("BulletText", "Add flash animation (green/red) when price changes using class: and $effect"),
        ],
        styles
    ))

    story.append(exercise(
        5,
        "Full Component Library: Button, Input, Modal, Toast, DataTable",
        [
            ("BulletText", "Button.svelte: variants (primary/secondary/danger), sizes (sm/md/lg), loading state with spinner"),

            ("BulletText", "Input.svelte: label, error message, bind:value via $bindable, validation callback prop"),

            ("BulletText", "Modal.svelte: backdrop click to close via clickOutside action, focus trap, svelte:head for scroll lock"),

            ("BulletText", "Toast.svelte + ToastContainer.svelte: context-based toast system, auto-dismiss with $effect timer"),

            ("BulletText", "DataTable.svelte: snippet-based headers and rows, sortable columns, pagination, empty state snippet"),

            ("BulletText", "Export all from lib/index.ts with full TypeScript types. Write tests for each with @testing-library/svelte"),
        ],
        styles
    ))

    story.append(PageBreak())
    return story


if __name__ == "__main__":
    print("Chapter 6 module loaded successfully.")
    print("Export: build_chapter_6(styles)")

    # ================================================================
    # 6.12 SVELTE AT PRINCIPAL ENGINEER LEVEL
    # ================================================================
    story.append(h1("6.12 Svelte at Principal Engineer Level", styles))

    story.append(p(
        "Writing Svelte components that work is table stakes. At the principal engineer "
        "level, you optimize for performance at scale, design APIs that other engineers "
        "can use without reading your source code, and build components that are "
        "maintainable, accessible, and testable. This section covers the meta-skills "
        "that separate framework users from framework architects.",
        styles
    ))

    story.append(h2("Performance Profiling Svelte Apps", styles))
    story.append(p(
        "Svelte's compilation model eliminates many React performance pitfalls, but "
        "poorly structured reactivity can still create performance problems. The main "
        "culprits are excessive effect runs, large reactive state objects, and "
        "computationally expensive derived values.",
        styles
    ))

    story.append(code_block(
        "// Performance anti-patterns and fixes\n"
        "\n"
        "// ANTI-PATTERN: Effect that runs too often\n"
        "// This runs every time ANY state changes because it reads everything\n"
        "$effect(() => {\n"
        "  console.log(stocks, sortKey, filter, page); // reads all 4 variables\n"
        "  updateURL();\n"
        "});\n"
        "\n"
        "// BETTER: Split into focused effects\n"
        "$effect(() => {\n"
        "  // Only runs when page changes\n"
        "  const currentPage = page;\n"
        "  updateURLParam('page', currentPage.toString());\n"
        "});\n"
        "\n"
        "$effect(() => {\n"
        "  // Only runs when filter changes\n"
        "  const currentFilter = filter;\n"
        "  updateURLParam('filter', currentFilter);\n"
        "});\n"
        "\n"
        "// ANTI-PATTERN: Expensive derived in render\n"
        "// Recalculates on every change to stocks (even non-sort-related)\n"
        "const sortedStocks = $derived(\n"
        "  [...stocks].sort((a, b) => expensiveSort(a, b))\n"
        ");\n"
        "\n"
        "// BETTER: Use untrack() to avoid unnecessary dependencies\n"
        "// Or structure state to minimize what triggers the sort\n"
        "import { untrack } from 'svelte';\n"
        "\n"
        "const sortedStocks = $derived.by(() => {\n"
        "  // Depend on sortKey and stocks, but not on selectedId\n"
        "  const key = sortKey;\n"
        "  const data = stocks;\n"
        "  return [...data].sort((a, b) => {\n"
        "    const aVal = a[key as keyof typeof a] as number | string;\n"
        "    const bVal = b[key as keyof typeof b] as number | string;\n"
        "    return typeof aVal === 'string'\n"
        "      ? aVal.localeCompare(bVal as string)\n"
        "      : (aVal as number) - (bVal as number);\n"
        "  });\n"
        "});",
        "performance-patterns.ts",
        styles
    ))

    story.append(h2("Large-Scale State Management Architecture", styles))
    story.append(p(
        "For a large application like a full trading platform, you need a deliberate "
        "state architecture. Here is a pattern that scales well in large Svelte applications:",
        styles
    ))

    story.append(code_block(
        "// src/lib/state/\n"
        "//   index.ts          - barrel export\n"
        "//   market.svelte.ts  - market-wide state (prices, status)\n"
        "//   portfolio.svelte.ts - user portfolio\n"
        "//   ui.svelte.ts      - UI-only state (selected, open panels)\n"
        "//   alerts.svelte.ts  - alert/notification state\n"
        "\n"
        "// market.svelte.ts\n"
        "// All state in one reactive module (works in SSR and client)\n"
        "\n"
        "interface MarketState {\n"
        "  status: 'pre-market' | 'open' | 'after-hours' | 'closed';\n"
        "  prices: Map<string, number>;\n"
        "  lastUpdated: Date | null;\n"
        "}\n"
        "\n"
        "// State is module-level: one instance for the entire app\n"
        "let state = $state<MarketState>({\n"
        "  status: 'closed',\n"
        "  prices: new Map(),\n"
        "  lastUpdated: null,\n"
        "});\n"
        "\n"
        "// Read-only derived values (computed from state)\n"
        "export const marketStatus = $derived(state.status);\n"
        "export const isMarketOpen = $derived(state.status === 'open');\n"
        "export const priceCount = $derived(state.prices.size);\n"
        "\n"
        "// Action functions (the only way to mutate state)\n"
        "export function setMarketStatus(\n"
        "  status: MarketState['status']\n"
        "): void {\n"
        "  state.status = status;\n"
        "}\n"
        "\n"
        "export function updatePrice(ticker: string, price: number): void {\n"
        "  state.prices.set(ticker, price);\n"
        "  state.lastUpdated = new Date();\n"
        "}\n"
        "\n"
        "export function getPrice(ticker: string): number | undefined {\n"
        "  return state.prices.get(ticker);\n"
        "}",
        "market.svelte.ts",
        styles
    ))

    story.append(h2("Component API Design for Reusable Libraries", styles))
    story.append(p(
        "When designing a component for a shared library (not just one page), treat the "
        "Props interface as a public API contract. These principles guide good "
        "component API design:",
        styles
    ))
    story.append(bullet("<b>Minimal required props:</b> Everything optional should be optional with sensible defaults. Users should be able to render your component with one prop and get a working result.", styles))
    story.append(bullet("<b>Typed callback names:</b> Use on-prefix convention (onclick, onchange, onsubmit) for event callbacks to match HTML conventions and improve discoverability.", styles))
    story.append(bullet("<b>Escape hatches:</b> Always provide a class prop and/or style prop. Users will always need to customize something you did not anticipate.", styles))
    story.append(bullet("<b>Slots/Snippets for content:</b> Do not accept text as a prop when a snippet would allow richer content. Accept both: text prop for simple cases, snippet for complex cases.", styles))

    story.append(h2("Testing Svelte Components with Vitest and Testing Library", styles))
    story.append(code_block(
        "// StockCard.test.ts\n"
        "import { describe, it, expect, vi } from 'vitest';\n"
        "import { render, screen, fireEvent } from '@testing-library/svelte';\n"
        "import StockCard from './StockCard.svelte';\n"
        "\n"
        "describe('StockCard', () => {\n"
        "  const defaultProps = {\n"
        "    ticker: 'AAPL',\n"
        "    price: 182.63,\n"
        "    change: 2.35,\n"
        "    changePercent: 1.31,\n"
        "  };\n"
        "\n"
        "  it('renders ticker and price', () => {\n"
        "    render(StockCard, { props: defaultProps });\n"
        "    expect(screen.getByText('AAPL')).toBeInTheDocument();\n"
        "    expect(screen.getByText('$182.63')).toBeInTheDocument();\n"
        "  });\n"
        "\n"
        "  it('shows positive change in green', () => {\n"
        "    render(StockCard, { props: defaultProps });\n"
        "    const changeEl = screen.getByText('+2.35');\n"
        "    expect(changeEl).toHaveClass('positive');\n"
        "  });\n"
        "\n"
        "  it('shows negative change in red', () => {\n"
        "    render(StockCard, {\n"
        "      props: { ...defaultProps, change: -3.20, changePercent: -1.72 }\n"
        "    });\n"
        "    const changeEl = screen.getByText('-3.20');\n"
        "    expect(changeEl).toHaveClass('negative');\n"
        "  });\n"
        "\n"
        "  it('calls onclick when clicked', async () => {\n"
        "    const onClickMock = vi.fn();\n"
        "    render(StockCard, {\n"
        "      props: { ...defaultProps, onclick: onClickMock }\n"
        "    });\n"
        "    const card = screen.getByRole('button');\n"
        "    await fireEvent.click(card);\n"
        "    expect(onClickMock).toHaveBeenCalledWith('AAPL');\n"
        "  });\n"
        "\n"
        "  it('is keyboard accessible', async () => {\n"
        "    const onClickMock = vi.fn();\n"
        "    render(StockCard, {\n"
        "      props: { ...defaultProps, onclick: onClickMock }\n"
        "    });\n"
        "    const card = screen.getByRole('button');\n"
        "    await fireEvent.keyDown(card, { key: 'Enter' });\n"
        "    expect(onClickMock).toHaveBeenCalled();\n"
        "  });\n"
        "\n"
        "  it('does not render volume when not provided', () => {\n"
        "    render(StockCard, { props: defaultProps });\n"
        "    expect(screen.queryByText(/Vol:/)).not.toBeInTheDocument();\n"
        "  });\n"
        "\n"
        "  it('renders volume when provided', () => {\n"
        "    render(StockCard, {\n"
        "      props: { ...defaultProps, volume: 45_000_000 }\n"
        "    });\n"
        "    expect(screen.getByText('Vol: 45.0M')).toBeInTheDocument();\n"
        "  });\n"
        "});",
        "StockCard.test.ts",
        styles
    ))

    story.append(h2("Accessibility: ARIA, Keyboard Navigation, Focus Management", styles))
    story.append(p(
        "Accessible Svelte components are not an afterthought. Svelte's compiler includes "
        "an a11y warning system that flags missing ARIA attributes, invalid roles, and "
        "interactive elements without keyboard support. Build accessibility in from "
        "the start.",
        styles
    ))

    story.append(code_block(
        "<!-- AccessibleStockCard.svelte -->\n"
        "<!-- A fully accessible interactive card component -->\n"
        "<script lang=\"ts\">\n"
        "  interface Props {\n"
        "    ticker: string;\n"
        "    price: number;\n"
        "    change: number;\n"
        "    isSelected?: boolean;\n"
        "    onselect?: (ticker: string) => void;\n"
        "  }\n"
        "\n"
        "  let {\n"
        "    ticker,\n"
        "    price,\n"
        "    change,\n"
        "    isSelected = false,\n"
        "    onselect,\n"
        "  }: Props = $props();\n"
        "\n"
        "  const isPositive = $derived(change >= 0);\n"
        "  const changeStr = $derived(\n"
        "    `${isPositive ? 'up' : 'down'} ${Math.abs(change).toFixed(2)} dollars`\n"
        "  );\n"
        "  const ariaLabel = $derived(\n"
        "    `${ticker}, price ${price.toFixed(2)}, ${changeStr} today`\n"
        "  );\n"
        "\n"
        "  function handleKeydown(e: KeyboardEvent): void {\n"
        "    if (e.key === 'Enter' || e.key === ' ') {\n"
        "      e.preventDefault();\n"
        "      onselect?.(ticker);\n"
        "    }\n"
        "  }\n"
        "</script>\n"
        "\n"
        "<article\n"
        "  class=\"stock-card\"\n"
        "  class:selected={isSelected}\n"
        "  role=\"button\"\n"
        "  tabindex=\"0\"\n"
        "  aria-pressed={isSelected}\n"
        "  aria-label={ariaLabel}\n"
        "  onclick={() => onselect?.(ticker)}\n"
        "  onkeydown={handleKeydown}\n"
        ">\n"
        "  <!-- Screen reader: skip the visual change display -->\n"
        "  <!-- Use aria-hidden to hide decorative elements -->\n"
        "  <div class=\"ticker\" aria-hidden=\"true\">{ticker}</div>\n"
        "  <div class=\"price\" aria-hidden=\"true\">${price.toFixed(2)}</div>\n"
        "\n"
        "  <!-- Visually styled, aria-hidden since ariaLabel covers it -->\n"
        "  <div\n"
        "    class=\"change\"\n"
        "    class:positive={isPositive}\n"
        "    class:negative={!isPositive}\n"
        "    aria-hidden=\"true\"\n"
        "  >\n"
        "    {isPositive ? '+' : ''}{change.toFixed(2)}\n"
        "  </div>\n"
        "</article>\n"
        "\n"
        "<style>\n"
        "  .stock-card:focus-visible {\n"
        "    outline: 2px solid #e94560;\n"
        "    outline-offset: 2px;\n"
        "  }\n"
        "\n"
        "  /* Never suppress focus outlines without providing an alternative */\n"
        "  .stock-card:focus:not(:focus-visible) {\n"
        "    outline: none;\n"
        "  }\n"
        "</style>",
        "AccessibleStockCard.svelte",
        styles
    ))

    story.append(principal_box(
        "The Svelte compiler's a11y warnings are not optional suggestions \u2014 treat them "
        "as errors in your CI pipeline. Add <b>// @ts-expect-error</b> or fix the issue; "
        "never silence the warning with a disable comment unless you have a specific reason "
        "and document it. Build a component library audit checklist: every interactive "
        "element has role + tabindex, every image has alt, every form input has a label, "
        "every modal manages focus (traps it when open, restores on close). Run axe-core "
        "in your test suite. A11y is not a feature \u2014 it is a requirement.",
        styles
    ))

    story.append(PageBreak())


    # ================================================================
    # EXERCISES
    # ================================================================
    story.append(h1("Chapter 6 Exercises", styles))

    story.append(p(
        "These exercises build a complete trading dashboard component library. Complete "
        "them in order \u2014 each exercise builds on the previous. All solutions use "
        "Svelte 5 runes and TypeScript throughout.",
        styles
    ))

    # Exercise 1
    story.append(exercise(
        1,
        "TradeBoard Stock Table with Reactive Filtering and Sorting",
        [
            ("ExerciseTitle", "Build a complete TradeBoard component"),
            ("ExerciseBody",
             "Create src/lib/TradeBoard.svelte that displays a table of stocks with reactive "
             "filtering by ticker/name and sorting by any column. Requirements: (1) Display "
             "ticker, company name, price, change, change%, volume in a table. (2) A text "
             "input filters rows reactively as user types. (3) Clicking a column header sorts "
             "by that column, clicking again reverses order. (4) Show a sort indicator (arrow) "
             "on the active column. (5) Highlight positive changes green and negative changes red. "
             "(6) Show row count: 'Showing X of Y stocks'. All done with $state and $derived only."
            ),
            ("ExerciseTitle", "Complete Solution:"),
            ("ExerciseBody",
             "<script lang=\"ts\">\n"
             "  interface Stock {\n"
             "    id: string;\n"
             "    ticker: string;\n"
             "    company: string;\n"
             "    price: number;\n"
             "    change: number;\n"
             "    changePercent: number;\n"
             "    volume: number;\n"
             "  }\n"
             "  type SortKey = keyof Pick<Stock, 'ticker'|'company'|'price'|'change'|'changePercent'|'volume'>;\n"
             "  let filter = $state('');\n"
             "  let sortKey = $state<SortKey>('ticker');\n"
             "  let sortAsc = $state(true);\n"
             "  const stocks = $state<Stock[]>([\n"
             "    {id:'1',ticker:'AAPL',company:'Apple Inc.',price:182.63,change:2.35,changePercent:1.31,volume:45000000},\n"
             "    {id:'2',ticker:'MSFT',company:'Microsoft Corp.',price:415.20,change:-1.80,changePercent:-0.43,volume:22000000},\n"
             "    {id:'3',ticker:'GOOG',company:'Alphabet Inc.',price:141.80,change:0.95,changePercent:0.67,volume:18000000},\n"
             "    {id:'4',ticker:'TSLA',company:'Tesla Inc.',price:195.40,change:-8.20,changePercent:-4.03,volume:95000000},\n"
             "    {id:'5',ticker:'AMZN',company:'Amazon.com Inc.',price:178.25,change:3.10,changePercent:1.77,volume:31000000},\n"
             "  ]);\n"
             "  const filtered = $derived(filter\n"
             "    ? stocks.filter(s => s.ticker.toLowerCase().includes(filter.toLowerCase()) ||\n"
             "                         s.company.toLowerCase().includes(filter.toLowerCase()))\n"
             "    : stocks\n"
             "  );\n"
             "  const sorted = $derived([...filtered].sort((a, b) => {\n"
             "    const aVal = a[sortKey]; const bVal = b[sortKey];\n"
             "    const cmp = typeof aVal === 'string' ? aVal.localeCompare(bVal as string) : (aVal as number) - (bVal as number);\n"
             "    return sortAsc ? cmp : -cmp;\n"
             "  }));\n"
             "  function sortBy(key: SortKey) {\n"
             "    if (sortKey === key) { sortAsc = !sortAsc; } else { sortKey = key; sortAsc = true; }\n"
             "  }\n"
             "  function indicator(key: SortKey) {\n"
             "    if (sortKey !== key) return '';\n"
             "    return sortAsc ? ' ▲' : ' ▼';\n"
             "  }\n"
             "</script>\n"
             "<input bind:value={filter} placeholder=\"Filter by ticker or company...\" />\n"
             "<p>Showing {sorted.length} of {stocks.length} stocks</p>\n"
             "<table>\n"
             "  <thead>\n"
             "    <tr>\n"
             "      {#each (['ticker','company','price','change','changePercent','volume'] as SortKey[]) as col}\n"
             "        <th onclick={() => sortBy(col)} style=\"cursor:pointer\">{col}{indicator(col)}</th>\n"
             "      {/each}\n"
             "    </tr>\n"
             "  </thead>\n"
             "  <tbody>\n"
             "    {#each sorted as stock (stock.id)}\n"
             "      <tr>\n"
             "        <td><strong>{stock.ticker}</strong></td>\n"
             "        <td>{stock.company}</td>\n"
             "        <td>${stock.price.toFixed(2)}</td>\n"
             "        <td class:positive={stock.change>=0} class:negative={stock.change<0}>\n"
             "          {stock.change>=0?'+':''}{stock.change.toFixed(2)}\n"
             "        </td>\n"
             "        <td class:positive={stock.changePercent>=0} class:negative={stock.changePercent<0}>\n"
             "          {stock.changePercent>=0?'+':''}{stock.changePercent.toFixed(2)}%\n"
             "        </td>\n"
             "        <td>{(stock.volume/1e6).toFixed(1)}M</td>\n"
             "      </tr>\n"
             "    {/each}\n"
             "  </tbody>\n"
             "</table>"
            ),
        ],
        styles
    ))

    story.append(spacer(12))

    # Exercise 2
    story.append(exercise(
        2,
        "StockCard Component with Typed Props and Sparkline",
        [
            ("ExerciseTitle", "Build a complete StockCard component"),
            ("ExerciseBody",
             "Create src/lib/StockCard.svelte with fully typed props: ticker (string), "
             "companyName (string), price (number), change (number), changePercent (number), "
             "volume (number), history (number[] \u2014 array of recent prices for sparkline), "
             "optional onclick callback. The component must: render all data, show a mini "
             "sparkline SVG chart using the history array, visually indicate positive/negative "
             "change, and be fully keyboard accessible with role='button' and tabindex='0'."
            ),
            ("ExerciseTitle", "Complete Solution:"),
            ("ExerciseBody",
             "<!-- StockCard.svelte -->\n"
             "<script lang=\"ts\">\n"
             "  interface Props {\n"
             "    ticker: string; companyName: string; price: number;\n"
             "    change: number; changePercent: number; volume: number;\n"
             "    history?: number[];\n"
             "    onclick?: (ticker: string) => void;\n"
             "    class?: string;\n"
             "  }\n"
             "  let { ticker, companyName, price, change, changePercent,\n"
             "        volume, history = [], onclick, class: className = '' }: Props = $props();\n"
             "  const isPositive = $derived(change >= 0);\n"
             "  const sparkPath = $derived(() => {\n"
             "    if (history.length < 2) return '';\n"
             "    const w = 80; const h = 30;\n"
             "    const min = Math.min(...history); const max = Math.max(...history);\n"
             "    const range = max - min || 1;\n"
             "    const pts = history.map((v, i) => {\n"
             "      const x = (i / (history.length - 1)) * w;\n"
             "      const y = h - ((v - min) / range) * h;\n"
             "      return `${x},${y}`;\n"
             "    });\n"
             "    return `M ${pts.join(' L ')}`;\n"
             "  })();\n"
             "  function handleKey(e: KeyboardEvent) {\n"
             "    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onclick?.(ticker); }\n"
             "  }\n"
             "</script>\n"
             "<article class=\"stock-card {className}\" class:positive={isPositive} class:negative={!isPositive}\n"
             "         role=\"button\" tabindex=\"0\" aria-label=\"{ticker} {price.toFixed(2)}, {isPositive?'up':'down'} {Math.abs(changePercent).toFixed(2)} percent\"\n"
             "         onclick={() => onclick?.(ticker)} onkeydown={handleKey}>\n"
             "  <header>\n"
             "    <strong class=\"ticker\">{ticker}</strong>\n"
             "    <span class=\"company\">{companyName}</span>\n"
             "  </header>\n"
             "  <div class=\"price-row\">\n"
             "    <span class=\"price\">${price.toFixed(2)}</span>\n"
             "    <span class=\"change\">{isPositive?'+':''}{changePercent.toFixed(2)}%</span>\n"
             "  </div>\n"
             "  {#if history.length >= 2}\n"
             "    <svg width=\"80\" height=\"30\" aria-hidden=\"true\">\n"
             "      <path d={sparkPath} fill=\"none\" stroke={isPositive?'#4caf50':'#ef5350'} stroke-width=\"1.5\" />\n"
             "    </svg>\n"
             "  {/if}\n"
             "  <footer class=\"volume\">Vol: {(volume/1e6).toFixed(1)}M</footer>\n"
             "</article>"
            ),
        ],
        styles
    ))

    story.append(spacer(12))

    # Exercise 3
    story.append(exercise(
        3,
        "Complete Watchlist with LocalStorage Persistence and Derived Stats",
        [
            ("ExerciseTitle", "Build a persistent watchlist with statistics"),
            ("ExerciseBody",
             "Create src/lib/Watchlist.svelte that manages a list of watched stocks. "
             "Requirements: (1) Add stocks by ticker symbol, validate format (1-5 uppercase letters). "
             "(2) Remove stocks with a remove button and animation. (3) Persist the watchlist to "
             "localStorage \u2014 reload the page and your list is still there. (4) Show derived stats: "
             "total tickers, average mock price, count of positive/negative movers. "
             "(5) Use transitions (fly + fade) for add/remove animations. "
             "(6) Show an empty state when the list is empty."
            ),
            ("ExerciseTitle", "Complete Solution:"),
            ("ExerciseBody",
             "<!-- Watchlist.svelte -->\n"
             "<script lang=\"ts\">\n"
             "  import { fly, fade } from 'svelte/transition';\n"
             "  import { flip } from 'svelte/animate';\n"
             "  interface WatchItem { id: string; ticker: string; mockPrice: number; mockChange: number; }\n"
             "  const STORAGE_KEY = 'tradeboard-watchlist';\n"
             "  function loadFromStorage(): WatchItem[] {\n"
             "    try {\n"
             "      const raw = localStorage.getItem(STORAGE_KEY);\n"
             "      return raw ? JSON.parse(raw) as WatchItem[] : [];\n"
             "    } catch { return []; }\n"
             "  }\n"
             "  let items = $state<WatchItem[]>(loadFromStorage());\n"
             "  let input = $state('');\n"
             "  let error = $state('');\n"
             "  $effect(() => {\n"
             "    localStorage.setItem(STORAGE_KEY, JSON.stringify(items));\n"
             "  });\n"
             "  const stats = $derived({\n"
             "    total: items.length,\n"
             "    avgPrice: items.length ? items.reduce((s,i)=>s+i.mockPrice,0)/items.length : 0,\n"
             "    gainers: items.filter(i=>i.mockChange>0).length,\n"
             "    losers: items.filter(i=>i.mockChange<0).length,\n"
             "  });\n"
             "  function validate(ticker: string): boolean {\n"
             "    return /^[A-Z]{1,5}$/.test(ticker.toUpperCase());\n"
             "  }\n"
             "  function addTicker(): void {\n"
             "    const t = input.trim().toUpperCase();\n"
             "    if (!validate(t)) { error = 'Invalid ticker (1-5 uppercase letters)'; return; }\n"
             "    if (items.some(i=>i.ticker===t)) { error = `${t} already in watchlist`; return; }\n"
             "    error = '';\n"
             "    items = [...items, {\n"
             "      id: crypto.randomUUID(), ticker: t,\n"
             "      mockPrice: 50 + Math.random() * 450,\n"
             "      mockChange: (Math.random() - 0.5) * 20,\n"
             "    }];\n"
             "    input = '';\n"
             "  }\n"
             "  function remove(id: string): void {\n"
             "    items = items.filter(i=>i.id!==id);\n"
             "  }\n"
             "</script>\n"
             "<div class=\"watchlist\">\n"
             "  <div class=\"stats\">\n"
             "    <span>Watching: {stats.total}</span>\n"
             "    <span>Avg Price: ${stats.avgPrice.toFixed(2)}</span>\n"
             "    <span class=\"green\">{stats.gainers} up</span>\n"
             "    <span class=\"red\">{stats.losers} down</span>\n"
             "  </div>\n"
             "  <form onsubmit={(e)=>{e.preventDefault();addTicker();}}>\n"
             "    <input bind:value={input} placeholder=\"Add ticker...\" />\n"
             "    <button type=\"submit\">Add</button>\n"
             "  </form>\n"
             "  {#if error}<p class=\"error\">{error}</p>{/if}\n"
             "  {#if items.length === 0}\n"
             "    <p class=\"empty\" in:fade>Your watchlist is empty. Add a ticker above.</p>\n"
             "  {:else}\n"
             "    {#each items as item (item.id)}\n"
             "      <div class=\"item\" animate:flip={{duration:300}}\n"
             "           in:fly={{x:200,duration:300}} out:fade={{duration:200}}>\n"
             "        <strong>{item.ticker}</strong>\n"
             "        <span>${item.mockPrice.toFixed(2)}</span>\n"
             "        <span class:pos={item.mockChange>0} class:neg={item.mockChange<0}>\n"
             "          {item.mockChange>0?'+':''}{item.mockChange.toFixed(2)}\n"
             "        </span>\n"
             "        <button onclick={()=>remove(item.id)} aria-label=\"Remove {item.ticker}\">x</button>\n"
             "      </div>\n"
             "    {/each}\n"
             "  {/if}\n"
             "</div>"
            ),
        ],
        styles
    ))

    story.append(spacer(12))

    # Exercise 4
    story.append(exercise(
        4,
        "Real-Time Price Ticker with WebSocket Simulation and Auto-Scroll",
        [
            ("ExerciseTitle", "Build a real-time animated price ticker"),
            ("ExerciseBody",
             "Create src/lib/PriceTicker.svelte that simulates real-time price updates. "
             "Use a setInterval to simulate WebSocket messages every 1-2 seconds. Requirements: "
             "(1) Display a horizontal scrolling ticker tape of stock symbols and prices. "
             "(2) When a price updates, flash the price element green (increase) or red (decrease) "
             "using a custom transition. (3) Auto-scroll the ticker tape continuously (CSS animation). "
             "(4) Stop scrolling on hover, resume on mouse leave. (5) Allow toggling ticker on/off. "
             "(6) Use $effect for the interval with proper cleanup. All TypeScript."
            ),
            ("ExerciseTitle", "Complete Solution:"),
            ("ExerciseBody",
             "<!-- PriceTicker.svelte -->\n"
             "<script lang=\"ts\">\n"
             "  import type { TransitionConfig } from 'svelte/transition';\n"
             "  interface TickerItem { ticker: string; price: number; prev: number; change: number; }\n"
             "  let running = $state(true);\n"
             "  let paused = $state(false);\n"
             "  let items = $state<TickerItem[]>([\n"
             "    {ticker:'AAPL',price:182.63,prev:182.63,change:0},\n"
             "    {ticker:'MSFT',price:415.20,prev:415.20,change:0},\n"
             "    {ticker:'GOOG',price:141.80,prev:141.80,change:0},\n"
             "    {ticker:'TSLA',price:195.40,prev:195.40,change:0},\n"
             "    {ticker:'AMZN',price:178.25,prev:178.25,change:0},\n"
             "    {ticker:'NVDA',price:875.39,prev:875.39,change:0},\n"
             "  ]);\n"
             "  let flashMap = $state<Map<string,string>>(new Map());\n"
             "  function priceFlash(node: Element, color: string): TransitionConfig {\n"
             "    return { duration: 800, css: (t) => {\n"
             "      const opacity = t > 0.5 ? 1 : t * 2;\n"
             "      const bg = t > 0.5 ? 1 - (t-0.5)*2 : 0;\n"
             "      return `background-color: rgba(${color==='green'?'76,175,80':'239,83,80'},${bg}); opacity:${opacity};`;\n"
             "    }};\n"
             "  }\n"
             "  function simulateTick(): void {\n"
             "    const idx = Math.floor(Math.random() * items.length);\n"
             "    const item = items[idx];\n"
             "    const delta = (Math.random() - 0.48) * item.price * 0.005;\n"
             "    const newPrice = Math.max(0.01, item.price + delta);\n"
             "    const color = delta >= 0 ? 'green' : 'red';\n"
             "    items[idx] = { ...item, prev: item.price, price: newPrice, change: delta };\n"
             "    flashMap = new Map(flashMap).set(item.ticker, color);\n"
             "    setTimeout(() => {\n"
             "      const next = new Map(flashMap); next.delete(item.ticker);\n"
             "      flashMap = next;\n"
             "    }, 900);\n"
             "  }\n"
             "  $effect(() => {\n"
             "    if (!running) return;\n"
             "    const interval = setInterval(simulateTick, 1200);\n"
             "    return () => clearInterval(interval);\n"
             "  });\n"
             "</script>\n"
             "<div class=\"ticker-controls\">\n"
             "  <button onclick={() => running = !running}>{running ? 'Pause' : 'Resume'} Ticker</button>\n"
             "</div>\n"
             "<div class=\"ticker-outer\" onmouseenter={() => paused=true} onmouseleave={() => paused=false}>\n"
             "  <div class=\"ticker-tape\" class:paused>\n"
             "    {#each [...items, ...items] as item, i (i)}\n"
             "      <span class=\"tick-item\" class:flash-green={flashMap.get(item.ticker)==='green'}\n"
             "            class:flash-red={flashMap.get(item.ticker)==='red'}>\n"
             "        <strong>{item.ticker}</strong>\n"
             "        <span>${item.price.toFixed(2)}</span>\n"
             "        <span class:pos={item.change>=0} class:neg={item.change<0}>\n"
             "          {item.change>=0?'+':''}{item.change.toFixed(2)}\n"
             "        </span>\n"
             "      </span>\n"
             "    {/each}\n"
             "  </div>\n"
             "</div>\n"
             "<style>\n"
             "  .ticker-outer { overflow: hidden; white-space: nowrap; background: #1a1a2e; padding: 8px 0; }\n"
             "  .ticker-tape { display: inline-flex; gap: 32px; animation: scroll 20s linear infinite; }\n"
             "  .ticker-tape.paused { animation-play-state: paused; }\n"
             "  @keyframes scroll { from { transform: translateX(0); } to { transform: translateX(-50%); } }\n"
             "  .tick-item { display: inline-flex; gap: 6px; padding: 0 8px; transition: background 0.8s; }\n"
             "  .flash-green { background: rgba(76,175,80,0.3); }\n"
             "  .flash-red { background: rgba(239,83,80,0.3); }\n"
             "  .pos { color: #4caf50; } .neg { color: #ef5350; }\n"
             "</style>"
            ),
        ],
        styles
    ))

    story.append(spacer(12))

    # Exercise 5
    story.append(exercise(
        5,
        "Complete Component Library: Button, Input, Modal, Toast, DataTable, Dropdown",
        [
            ("ExerciseTitle", "Build a full typed, accessible, animated component library"),
            ("ExerciseBody",
             "Create src/lib/components/ with six production-quality components. Each must be "
             "fully typed with TypeScript, keyboard accessible, and support theming via CSS "
             "custom properties. This is a principal engineer-level exercise \u2014 focus on "
             "API design, accessibility, and robustness."
            ),
            ("ExerciseTitle", "Button.svelte - Complete Solution:"),
            ("ExerciseBody",
             "<!-- Button.svelte -->\n"
             "<script lang=\"ts\">\n"
             "  import type { Snippet } from 'svelte';\n"
             "  interface Props {\n"
             "    variant?: 'primary'|'secondary'|'ghost'|'danger';\n"
             "    size?: 'sm'|'md'|'lg';\n"
             "    disabled?: boolean;\n"
             "    loading?: boolean;\n"
             "    type?: 'button'|'submit'|'reset';\n"
             "    class?: string;\n"
             "    children: Snippet;\n"
             "    onclick?: (e: MouseEvent) => void;\n"
             "  }\n"
             "  let {\n"
             "    variant='primary', size='md', disabled=false, loading=false,\n"
             "    type='button', class:className='', children, onclick\n"
             "  }: Props = $props();\n"
             "  const isDisabled = $derived(disabled || loading);\n"
             "</script>\n"
             "<button {type} class=\"btn btn-{variant} btn-{size} {className}\"\n"
             "        disabled={isDisabled} aria-disabled={isDisabled} aria-busy={loading}\n"
             "        {onclick}>\n"
             "  {#if loading}<span class=\"spinner\" aria-hidden=\"true\"></span>{/if}\n"
             "  {@render children()}\n"
             "</button>"
            ),
            ("ExerciseTitle", "Modal.svelte - Complete Solution:"),
            ("ExerciseBody",
             "<!-- Modal.svelte - Focus trap + accessible dialog -->\n"
             "<script lang=\"ts\">\n"
             "  import { fade, scale } from 'svelte/transition';\n"
             "  import type { Snippet } from 'svelte';\n"
             "  interface Props {\n"
             "    open: boolean;\n"
             "    title: string;\n"
             "    onClose: () => void;\n"
             "    children: Snippet;\n"
             "    footer?: Snippet<[() => void]>;\n"
             "    size?: 'sm'|'md'|'lg';\n"
             "  }\n"
             "  let { open, title, onClose, children, footer, size='md' }: Props = $props();\n"
             "  let dialogEl: HTMLDialogElement | undefined = $state();\n"
             "  $effect(() => {\n"
             "    if (open) {\n"
             "      dialogEl?.showModal();\n"
             "      dialogEl?.focus();\n"
             "    } else {\n"
             "      dialogEl?.close();\n"
             "    }\n"
             "  });\n"
             "  function handleKeydown(e: KeyboardEvent): void {\n"
             "    if (e.key === 'Escape') onClose();\n"
             "  }\n"
             "  function handleBackdropClick(e: MouseEvent): void {\n"
             "    if (e.target === dialogEl) onClose();\n"
             "  }\n"
             "</script>\n"
             "{#if open}\n"
             "  <dialog bind:this={dialogEl} class=\"modal modal-{size}\"\n"
             "          role=\"dialog\" aria-modal=\"true\" aria-labelledby=\"modal-title\"\n"
             "          onkeydown={handleKeydown} onclick={handleBackdropClick}\n"
             "          transition:scale={{duration:200,start:0.95}}>\n"
             "    <header class=\"modal-header\">\n"
             "      <h2 id=\"modal-title\">{title}</h2>\n"
             "      <button onclick={onClose} aria-label=\"Close dialog\" class=\"close-btn\">x</button>\n"
             "    </header>\n"
             "    <div class=\"modal-body\">{@render children()}</div>\n"
             "    {#if footer}\n"
             "      <footer class=\"modal-footer\">{@render footer(onClose)}</footer>\n"
             "    {/if}\n"
             "  </dialog>\n"
             "{/if}"
            ),
            ("ExerciseTitle", "Toast.svelte - Notification System:"),
            ("ExerciseBody",
             "<!-- toasts.svelte.ts - Toast state and actions -->\n"
             "export type ToastType = 'success'|'error'|'warning'|'info';\n"
             "interface Toast { id: string; message: string; type: ToastType; duration: number; }\n"
             "let toasts = $state<Toast[]>([]);\n"
             "export const activeToasts = $derived(toasts);\n"
             "export function toast(message: string, type: ToastType = 'info', duration = 4000): void {\n"
             "  const id = crypto.randomUUID();\n"
             "  toasts = [...toasts, { id, message, type, duration }];\n"
             "  setTimeout(() => { toasts = toasts.filter(t => t.id !== id); }, duration);\n"
             "}\n"
             "export function dismissToast(id: string): void { toasts = toasts.filter(t => t.id !== id); }\n"
             "\n"
             "<!-- ToastContainer.svelte -->\n"
             "<script lang=\"ts\">\n"
             "  import { fly, fade } from 'svelte/transition';\n"
             "  import { flip } from 'svelte/animate';\n"
             "  import { activeToasts, dismissToast } from '$lib/components/toasts.svelte';\n"
             "</script>\n"
             "<div class=\"toast-container\" aria-live=\"polite\" aria-atomic=\"false\">\n"
             "  {#each activeToasts as t (t.id)}\n"
             "    <div class=\"toast toast-{t.type}\" role=\"alert\"\n"
             "         animate:flip={{duration:250}}\n"
             "         in:fly={{y:50,duration:300}} out:fade={{duration:200}}>\n"
             "      <span>{t.message}</span>\n"
             "      <button onclick={() => dismissToast(t.id)} aria-label=\"Dismiss\">x</button>\n"
             "    </div>\n"
             "  {/each}\n"
             "</div>"
            ),
        ],
        styles
    ))

    story.append(spacer(16))

    story.append(checkpoint(
        "Chapter 6 Complete: You have mastered Svelte 5 runes, "
        "component composition with snippets, transitions, actions, stores, and "
        "principal engineer-level patterns for testing and accessibility.",
        styles
    ))

    story.append(HorizontalLine())

    story.append(spacer(16))

    story.append(p(
        "<b>Chapter Summary.</b> Svelte 5 is a compiler-first framework that ships "
        "zero runtime overhead and generates surgical DOM update code at build time. "
        "The rune system ($state, $derived, $effect, $props, $bindable, $inspect) "
        "provides explicit, TypeScript-friendly reactivity that works in both .svelte "
        "and .svelte.ts files. Snippets replace Svelte 4's slot system for type-safe "
        "component composition. Built-in transitions, the animate: directive, and "
        "custom transition functions enable choreographed UI animations with minimal "
        "boilerplate. Actions provide reusable DOM behavior via the use: directive. "
        "Stores and the context API address different scopes of shared state. At the "
        "principal engineer level, this means designing component APIs as public "
        "contracts, building accessible components by default, writing component tests "
        "with Vitest and Testing Library, and architecting state so it is as local "
        "as possible.",
        styles
    ))

    story.append(spacer(8))

    story.append(p(
        "<b>What's Next.</b> Chapter 7 covers SvelteKit in depth \u2014 the official "
        "application framework built on Svelte. You will learn file-based routing, "
        "server-side rendering, API routes, form actions, loading strategies, and "
        "deployment. SvelteKit is where Svelte becomes a full-stack web framework "
        "capable of building production applications.",
        styles
    ))

    story.append(PageBreak())

    return story

