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
    story.extend(h1("6.1 Why Svelte 5?", styles))
    story.extend(p(
        "React and Vue ship a runtime library to the browser that interprets your component code at runtime. "
        "Svelte takes a radically different approach: it is a <b>compiler</b>. Your .svelte files are compiled "
        "at build time into tight, vanilla JavaScript with no framework overhead in the bundle.",
        styles
    ))
    story.extend(analogy_box(
        "Factory vs. Shipping Crew",
        "React is like hiring a skilled crew that shows up to your job site every day (the browser) with a "
        "full tool truck (the runtime). They're great, but every client pays for that truck. Svelte is like "
        "a factory that pre-fabricates your walls, cabinets, and wiring off-site. By the time anything "
        "reaches the browser, it's already purpose-built vanilla JS — no tool truck needed.",
        styles
    ))
    story.extend(p("Key advantages of Svelte 5 over its predecessors and competitors:", styles))
    story.extend(bullet("No virtual DOM diffing — direct DOM mutations generated at compile time", styles))
    story.extend(bullet("Smaller bundles — only the code your component uses is emitted", styles))
    story.extend(bullet("Runes system — explicit, fine-grained reactivity replacing the magic $: label syntax", styles))
    story.extend(bullet("Snippets — reusable markup fragments replacing slots", styles))
    story.extend(bullet("First-class TypeScript support throughout", styles))
    story.extend(bullet("Performance on par with or exceeding hand-written DOM code", styles))
    story.extend(p(
        "Svelte 5 introduced <b>runes</b> — compiler-understood function calls (prefixed with $) that "
        "declare reactive state, derived values, and side effects. They replace the implicit reactivity "
        "of Svelte 3/4 with something explicit and composable.",
        styles
    ))
    story.extend(principal_box(
        "PE Principle: Choose the right abstraction level",
        "Svelte's compiler approach means the abstraction cost is paid at build time, not runtime. "
        "For performance-critical UIs — trading dashboards, real-time data grids — this matters. "
        "A principal engineer chooses tools whose costs align with where they can afford to pay them.",
        styles
    ))

    # ── 6.2 First Component ───────────────────────────────────────────────────
    story.extend(h1("6.2 Your First Svelte 5 Component", styles))
    story.extend(p(
        "A .svelte file has three optional sections: a script block, markup, and a style block. "
        "Each component is a self-contained unit — styles are scoped by default.",
        styles
    ))
    story.extend(analogy_box(
        "The Self-Contained Room",
        "A Svelte component is like a hotel room: it has its own furniture (markup), its own decor "
        "rules (scoped styles), and its own logic (script). Guests in room 201 can't accidentally "
        "move furniture in room 202 — style scoping prevents collisions.",
        styles
    ))
    story.extend(code_block(
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
    story.extend(p(
        "Notice <b>lang=\"ts\"</b> on the script tag — TypeScript works out of the box. "
        "Event handlers use the new <b>onclick</b> attribute (no on:click in Svelte 5). "
        "The <b>class:</b> directive conditionally applies CSS classes.",
        styles
    ))

    # ── 6.3 Runes ─────────────────────────────────────────────────────────────
    story.extend(h1("6.3 Runes — The Reactivity System", styles))
    story.extend(p(
        "Runes are special compiler-recognized calls that express reactive intent. "
        "They look like function calls but are transformed at compile time.",
        styles
    ))

    story.extend(h2("$state — The Whiteboard", styles))
    story.extend(analogy_box(
        "$state — The Whiteboard",
        "Think of $state as a whiteboard in the office. Anyone can look at it, and whenever "
        "you erase and rewrite it, everyone who was watching automatically updates their understanding. "
        "The compiler wires up exactly who watches which whiteboard.",
        styles
    ))
    story.extend(code_block(
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

    story.extend(h2("$derived — The Calculator", styles))
    story.extend(analogy_box(
        "$derived — The Calculator",
        "A $derived value is like a calculator display: you never manually set it. "
        "You change the inputs, and the display updates itself. Try to write to it and "
        "the compiler stops you — calculators don't take input on their display.",
        styles
    ))
    story.extend(code_block(
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

    story.extend(h2("$effect — The Watchdog", styles))
    story.extend(analogy_box(
        "$effect — The Watchdog",
        "A $effect is a watchdog process. Every time state it reads changes, it runs again. "
        "It can also clean up after itself — like a guard who locks the previous door before "
        "moving to the next post. Return a cleanup function and Svelte calls it automatically.",
        styles
    ))
    story.extend(code_block(
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

    story.extend(h2("$props and $bindable", styles))
    story.extend(code_block(
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

    story.extend(h2("$inspect — Debug Utility", styles))
    story.extend(code_block(
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
    story.extend(mistake_box(
        "Svelte 4 vs Svelte 5 Syntax",
        "Never mix Svelte 4 and Svelte 5 syntax. In Svelte 5: use $state() not let x = 0 for "
        "reactive variables, use onclick not on:click, use $props() not export let, and use "
        "snippets not slots. Mixing causes confusing compiler errors.",
        styles
    ))

    # ── 6.4 Component Composition ─────────────────────────────────────────────
    story.extend(h1("6.4 Component Composition", styles))
    story.extend(p(
        "Svelte 5 replaces slots with <b>snippets</b> — named, typed, reusable markup fragments "
        "that can receive arguments. This is strictly more powerful than slot-based composition.",
        styles
    ))
    story.extend(code_block(
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
    story.extend(code_block(
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
    story.extend(p(
        "Callback props replace event forwarding. Pass functions as props instead of "
        "dispatching custom events — this is more TypeScript-friendly and explicit.",
        styles
    ))

    # ── 6.5 Control Flow ──────────────────────────────────────────────────────
    story.extend(h1("6.5 Control Flow", styles))
    story.extend(code_block(
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
    story.extend(principal_box(
        "Always key your {#each} blocks",
        "Without a key, Svelte patches DOM nodes in place. With a key like (item.id), "
        "Svelte knows exactly which node to move, update, or remove. Unkeyed lists cause "
        "subtle bugs with animations, inputs retaining wrong values, and O(n) unnecessary work.",
        styles
    ))

    # ── 6.6 Bindings ──────────────────────────────────────────────────────────
    story.extend(h1("6.6 Bindings", styles))
    story.extend(code_block(
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
    story.extend(h1("6.7 Lifecycle with $effect", styles))
    story.extend(p(
        "In Svelte 5, $effect replaces onMount and onDestroy for most use cases. "
        "Effects run after the DOM is updated and return an optional cleanup function.",
        styles
    ))
    story.extend(code_block(
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
    story.extend(mistake_box(
        "Avoid reading reactive state you don't intend to track",
        "Every $state variable read inside an $effect body creates a subscription. "
        "If you read a value for a one-time setup but don't want re-runs, use "
        "untrack(() => myState) from 'svelte' to opt out of tracking for that read.",
        styles
    ))

    # ── 6.8 Stores & Shared State ─────────────────────────────────────────────
    story.extend(h1("6.8 Stores & Shared State", styles))
    story.extend(code_block(
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
    story.extend(code_block(
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

    story.extend(h2("Context API — Component-Scoped Globals", styles))
    story.extend(code_block(
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
    story.extend(principal_box(
        "Store vs Context vs Runes — When to Use What",
        "Use $state in a .svelte.ts file (a 'rune module') for app-level state that benefits "
        "from the compiler's fine-grained tracking. Use stores when you need store contracts "
        "(subscribe/set/update) for interop. Use context for component-tree-scoped data "
        "where you don't want prop drilling but also don't want global state.",
        styles
    ))

    # ── 6.9 Transitions ───────────────────────────────────────────────────────
    story.extend(h1("6.9 Transitions & Animations", styles))
    story.extend(analogy_box(
        "Choreographed Entrance",
        "Transitions are like a choreographed entrance at a gala. Each guest (element) "
        "knows their cue — fade in, slide from left, scale up. The director (Svelte) "
        "coordinates so nothing collides. The `in:` and `out:` directives let you specify "
        "different choreography for entering vs leaving.",
        styles
    ))
    story.extend(code_block(
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
    story.extend(h1("6.10 Actions (use: Directive)", styles))
    story.extend(analogy_box(
        "USB Dongle",
        "An action is like a USB dongle — a self-contained capability you plug into any DOM node. "
        "The node doesn't need to know about the action; it just gains new powers: "
        "click-outside detection, tooltip behavior, intersection observation.",
        styles
    ))
    story.extend(code_block(
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
    story.extend(code_block(
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
    story.extend(h1("6.11 Advanced Patterns", styles))

    story.extend(h2("Dynamic Components & Special Elements", styles))
    story.extend(code_block(
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

    story.extend(h2("Recursive Components", styles))
    story.extend(code_block(
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

    story.extend(h2("class: and style: Directives", styles))
    story.extend(code_block(
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
    story.extend(h1("6.12 Svelte at Principal Engineer Level", styles))

    story.extend(h2("Performance", styles))
    story.extend(bullet("Prefer $derived over redundant $effect chains — derived values are synchronous and skip the microtask queue", styles))
    story.extend(bullet("Use {#key expr} to force full remount when identity changes (e.g., navigating between user profiles)", styles))
    story.extend(bullet("Virtualize long lists with svelte-virtual or a custom action — the DOM is the bottleneck, not Svelte", styles))
    story.extend(bullet("Lazy-load heavy components with dynamic import() inside {#await} blocks", styles))

    story.extend(h2("State Management at Scale", styles))
    story.extend(code_block(
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

    story.extend(h2("Component Library Design", styles))
    story.extend(bullet("Use $props() with explicit TypeScript interfaces — never use any or unknown for prop types", styles))
    story.extend(bullet("Export prop types alongside components for consumers: export type { ButtonProps }", styles))
    story.extend(bullet("Design for composition: accept snippets for customizable regions instead of boolean flags", styles))
    story.extend(bullet("Use CSS custom properties (variables) for theming — consumers override at root, not in your code", styles))

    story.extend(h2("Testing", styles))
    story.extend(code_block(
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

    story.extend(h2("Accessibility (a11y)", styles))
    story.extend(bullet("Svelte's compiler warns on a11y violations at build time — treat them as errors, not warnings", styles))
    story.extend(bullet("Use role, aria-label, and aria-live for dynamic content like price tickers", styles))
    story.extend(bullet("Test with keyboard navigation — all interactive elements must be reachable and operable via keyboard", styles))
    story.extend(bullet("Provide prefers-reduced-motion alternatives for all transitions and animations", styles))
    story.extend(code_block(
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
    story.extend(principal_box(
        "PE Principle: Svelte's compiler is your first reviewer",
        "Treat every Svelte compiler warning as a code review comment from a senior engineer. "
        "The a11y warnings, unused CSS selectors, missing keys — these are the compiler "
        "catching real bugs before they ship. A principal engineer configures CI to fail "
        "on warnings, not just errors.",
        styles
    ))

    # ── Checkpoint ────────────────────────────────────────────────────────────
    story.extend(checkpoint(
        "Chapter 6 Checkpoint",
        [
            "You understand why Svelte's compiler approach differs from runtime frameworks",
            "You can create .svelte components with TypeScript using lang=\"ts\"",
            "You can declare reactive state with $state, $derived, and $effect",
            "You can compose components using $props() and snippets with {@render}",
            "You can use control flow: {#if}, {#each} with keys, {#await}",
            "You can bind form inputs with bind:value, bind:checked, bind:group",
            "You can use stores (writable/readable/derived) and auto-subscribe with $",
            "You can add transitions (fade/fly/slide) and animate list reordering with flip",
            "You can write and apply actions with the use: directive",
            "You understand context API and when to use it vs stores vs rune modules",
        ],
        styles
    ))
    story.append(PageBreak())

    # ── Exercises ─────────────────────────────────────────────────────────────
    story.extend(h1("Chapter 6 Exercises", styles))

    story.extend(exercise(
        1,
        "Rebuild TradeBoard Stock Table as Svelte Component",
        [
            "Create StockTable.svelte with typed props: stocks: Stock[]",
            "Use {#each stocks as stock (stock.symbol)} with key",
            "Add a sort-by-column feature using $derived and $state for sortKey and sortDir",
            "Style with scoped CSS — alternating row colors, positive/negative change color",
            "Add a search/filter input bound with bind:value that filters the list in real-time",
        ],
        styles,
        star_level=1
    ))

    story.extend(exercise(
        2,
        "StockCard Component with Typed Props",
        [
            "Create StockCard.svelte with interface Props { symbol, price, change, onSelect?: () => void }",
            "Display symbol, formatted price, change with color-coded badge",
            "Add click handler that calls onSelect callback prop",
            "Export a 'selected' $bindable prop so parent can two-way bind selection state",
            "Add transition:scale when the card mounts using in:scale={{ duration: 200 }}",
        ],
        styles,
        star_level=2
    ))

    story.extend(exercise(
        3,
        "Complete Watchlist with localStorage and Derived Stats",
        [
            "Create stores/watchlist.svelte.ts rune module exporting a WatchlistStore class",
            "Persist watchlist to localStorage via $effect in the store class",
            "Add $derived stats: totalValue, bestPerformer, worstPerformer, avgChange",
            "Build WatchlistPanel.svelte that shows the list and stats",
            "Add ability to add/remove symbols with animated list transitions using fly and flip",
        ],
        styles,
        star_level=3
    ))

    story.extend(exercise(
        4,
        "Real-Time Price Ticker with WebSocket Simulation",
        [
            "Create a PriceFeed action (use:priceFeed) that simulates a WebSocket with setInterval",
            "The action dispatches custom 'priceupdate' events with { symbol, price, change }",
            "Build TickerTape.svelte: a horizontal scrolling list of live prices",
            "Use $effect to subscribe to price events and update $state",
            "Add flash animation (green/red) when price changes using class: and $effect",
        ],
        styles,
        star_level=4
    ))

    story.extend(exercise(
        5,
        "Full Component Library: Button, Input, Modal, Toast, DataTable",
        [
            "Button.svelte: variants (primary/secondary/danger), sizes (sm/md/lg), loading state with spinner",
            "Input.svelte: label, error message, bind:value via $bindable, validation callback prop",
            "Modal.svelte: backdrop click to close via clickOutside action, focus trap, svelte:head for scroll lock",
            "Toast.svelte + ToastContainer.svelte: context-based toast system, auto-dismiss with $effect timer",
            "DataTable.svelte: snippet-based headers and rows, sortable columns, pagination, empty state snippet",
            "Export all from lib/index.ts with full TypeScript types. Write tests for each with @testing-library/svelte",
        ],
        styles,
        star_level=5
    ))

    story.append(PageBreak())
    return story


if __name__ == "__main__":
    print("Chapter 6 module loaded successfully.")
    print("Export: build_chapter_6(styles)")
