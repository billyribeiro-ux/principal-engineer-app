"""Chapter 5: TypeScript — JavaScript with Guardrails"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_5(styles):
    story = []

    story.append(ChapterCoverPage(5, "TypeScript \u2014 JavaScript with Guardrails",
                                  "A Spell-Checker for Your Code", "PART 2: LEVELING UP"))
    story.append(PageBreak())

    # ================================================================
    # 5.1 WHY TYPESCRIPT?
    # ================================================================
    story.append(h1("5.1 Why TypeScript?", styles))
    story.append(analogy_box(
        "Imagine writing an entire novel without a spell-checker. You can do it \u2014 Shakespeare did \u2014 but "
        "you will make mistakes that a machine could have caught instantly. TypeScript is a spell-checker "
        "for your code. It does not change what JavaScript can do (it is still JavaScript underneath), "
        "but it catches typos, wrong argument types, missing properties, and impossible states before "
        "your code ever runs. The spell-checker does not write the novel for you, but it makes sure your "
        "novel does not have embarrassing errors."
    , styles))

    story.append(p(
        "TypeScript is a <b>superset</b> of JavaScript. Every valid JavaScript program is also a valid "
        "TypeScript program. TypeScript adds one thing: a type system that is erased at compile time. "
        "Your browser never sees TypeScript \u2014 it runs the JavaScript that TypeScript compiles to. "
        "The types exist only during development, catching errors before they reach production."
    , styles))

    story.append(p("What TypeScript prevents:", styles))
    story.append(bullet("<b>Typos in property names</b> \u2014 <code>user.naem</code> instead of <code>user.name</code>", styles))
    story.append(bullet("<b>Wrong argument types</b> \u2014 passing a string where a number is expected", styles))
    story.append(bullet("<b>Missing null checks</b> \u2014 accessing <code>.length</code> on something that might be undefined", styles))
    story.append(bullet("<b>Impossible states</b> \u2014 a loading spinner showing while data is already loaded", styles))
    story.append(bullet("<b>Refactoring accidents</b> \u2014 renaming a field but missing 3 of 47 usages", styles))

    story.append(h2("Setting Up TypeScript", styles))
    story.append(code_block(
        '# In a SvelteKit project, TypeScript is built in!\n'
        '# For standalone TypeScript:\n'
        'npm install -D typescript\n'
        'npx tsc --init  # Creates tsconfig.json\n\n'
        '# tsconfig.json essentials:\n'
        '{\n'
        '  "compilerOptions": {\n'
        '    "target": "ES2022",        // Modern JS output\n'
        '    "module": "ESNext",         // ESM modules\n'
        '    "strict": true,             // ALL strict checks on\n'
        '    "noUncheckedIndexedAccess": true,  // Arrays might be undefined\n'
        '    "moduleResolution": "bundler",\n'
        '    "esModuleInterop": true,\n'
        '    "skipLibCheck": true\n'
        '  }\n'
        '}',
        filename="TypeScript Setup", styles=styles
    ))

    story.append(principal_box(
        "Always enable strict mode. Non-strict TypeScript is like a spell-checker that only checks "
        "words longer than 10 letters \u2014 it misses most of the errors. Strict mode enables: "
        "strictNullChecks, noImplicitAny, strictFunctionTypes, and more. If you start without strict "
        "mode, you will eventually want it and face thousands of errors when turning it on."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand why TypeScript exists and how to set it up.", styles))
    story.append(page_break())

    # ================================================================
    # 5.2 BASIC TYPES
    # ================================================================
    story.append(h1("5.2 Basic Types", styles))

    story.append(code_block(
        '// Primitive types\n'
        'let ticker: string = "AAPL";\n'
        'let price: number = 187.44;\n'
        'let isActive: boolean = true;\n'
        'let nothing: null = null;\n'
        'let notDefined: undefined = undefined;\n\n'
        '// Type inference - TypeScript figures it out\n'
        'let symbol = "GOOG";         // TypeScript infers: string\n'
        'let shares = 100;            // TypeScript infers: number\n'
        'let isFavorite = false;      // TypeScript infers: boolean\n\n'
        '// Arrays\n'
        'let tickers: string[] = ["AAPL", "GOOG", "MSFT"];\n'
        'let prices: number[] = [187.44, 141.80, 378.91];\n'
        'let mixed: (string | number)[] = ["AAPL", 187.44];\n\n'
        '// Tuples - fixed-length arrays with specific types per position\n'
        'let stockPair: [string, number] = ["AAPL", 187.44];\n'
        '// stockPair[0] is string, stockPair[1] is number\n\n'
        '// Literal types - exact values\n'
        'let direction: "up" | "down" | "flat" = "up";\n'
        'let httpStatus: 200 | 404 | 500 = 200;',
        filename="Basic Types", styles=styles
    ))

    story.append(h2("Type Annotations vs Type Inference", styles))
    story.append(p(
        "TypeScript can infer types from context. You do not need to annotate everything \u2014 only "
        "annotate when inference is not enough or when you want to be explicit about your intent."
    , styles))

    story.append(code_block(
        '// LET TypeScript infer (preferred when obvious)\n'
        'const name = "Apple Inc.";   // string (inferred)\n'
        'const price = 187.44;        // number (inferred)\n'
        'const stocks = ["AAPL"];     // string[] (inferred)\n\n'
        '// DO annotate function parameters (always required)\n'
        'function formatPrice(amount: number): string {\n'
        '  return `$${amount.toFixed(2)}`;\n'
        '}\n\n'
        '// DO annotate when the type is not obvious\n'
        'const data: Stock[] = JSON.parse(response);  // JSON.parse returns any\n\n'
        '// DO annotate empty collections\n'
        'const watchlist: string[] = [];  // Without annotation: never[]',
        filename="Inference vs Annotations", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You understand primitive types, arrays, tuples, and when to annotate.", styles))
    story.append(page_break())

    # ================================================================
    # 5.3 INTERFACES AND TYPE ALIASES
    # ================================================================
    story.append(h1("5.3 Interfaces and Type Aliases", styles))
    story.append(analogy_box(
        "An interface is like a blueprint for a house. It specifies: the house must have a door (string), "
        "a roof (number of floors), and a garage (boolean). It does not build the house \u2014 it just describes "
        "what a valid house looks like. Any object that has those exact properties qualifies as a 'house' "
        "regardless of how it was built."
    , styles))

    story.append(code_block(
        '// Interface - describes the shape of an object\n'
        'interface Stock {\n'
        '  ticker: string;\n'
        '  name: string;\n'
        '  price: number;\n'
        '  change: number;\n'
        '  changePercent: number;\n'
        '  volume: number;\n'
        '  marketCap: number;\n'
        '}\n\n'
        '// Using the interface\n'
        'const apple: Stock = {\n'
        '  ticker: "AAPL",\n'
        '  name: "Apple Inc.",\n'
        '  price: 187.44,\n'
        '  change: 2.35,\n'
        '  changePercent: 1.27,\n'
        '  volume: 54_000_000,\n'
        '  marketCap: 2_900_000_000_000\n'
        '};\n'
        '// Missing any property = compile error!\n'
        '// Extra properties = compile error!\n\n'
        '// Optional properties with ?\n'
        'interface UserSettings {\n'
        '  theme: "light" | "dark";\n'
        '  language: string;\n'
        '  notifications?: boolean;  // Optional\n'
        '  avatar?: string;          // Optional\n'
        '}\n\n'
        '// Readonly properties\n'
        'interface Trade {\n'
        '  readonly id: string;       // Cannot be changed after creation\n'
        '  readonly timestamp: Date;\n'
        '  ticker: string;\n'
        '  quantity: number;\n'
        '  price: number;\n'
        '}',
        filename="Interfaces", styles=styles
    ))

    story.append(h2("Type Aliases", styles))
    story.append(code_block(
        '// Type aliases can describe anything, not just objects\n'
        'type Ticker = string;\n'
        'type Price = number;\n'
        'type Direction = "up" | "down" | "flat";\n\n'
        '// Union types - this OR that\n'
        'type StockResult = Stock | null;\n'
        'type ApiResponse = SuccessResponse | ErrorResponse;\n\n'
        '// Intersection types - this AND that\n'
        'type StockWithHistory = Stock & {\n'
        '  history: PricePoint[];\n'
        '  fiftyTwoWeekHigh: number;\n'
        '  fiftyTwoWeekLow: number;\n'
        '};\n\n'
        '// When to use interface vs type?\n'
        '// Interface: for object shapes that might be extended\n'
        '// Type: for unions, intersections, mapped types, and primitives\n'
        '// Rule of thumb: use interface for objects, type for everything else',
        filename="Type Aliases", styles=styles
    ))

    story.append(h2("Extending Interfaces", styles))
    story.append(code_block(
        '// Interfaces can extend other interfaces\n'
        'interface BaseEntity {\n'
        '  id: string;\n'
        '  createdAt: Date;\n'
        '  updatedAt: Date;\n'
        '}\n\n'
        'interface Stock extends BaseEntity {\n'
        '  ticker: string;\n'
        '  name: string;\n'
        '  price: number;\n'
        '}\n\n'
        'interface User extends BaseEntity {\n'
        '  email: string;\n'
        '  name: string;\n'
        '  role: "admin" | "user";\n'
        '}\n\n'
        '// Both Stock and User automatically have id, createdAt, updatedAt',
        filename="Extending Interfaces", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can define interfaces, type aliases, unions, intersections, and "
                           "extend interfaces.", styles))
    story.append(page_break())

    # ================================================================
    # 5.4 UNION TYPES AND NARROWING
    # ================================================================
    story.append(h1("5.4 Union Types and Type Narrowing", styles))
    story.append(p(
        "Union types say 'this value could be one of several types.' Type narrowing is how you figure "
        "out which type it actually is at runtime."
    , styles))

    story.append(code_block(
        '// Discriminated unions - the PE pattern for complex state\n'
        'type ApiState<T> =\n'
        '  | { status: "idle" }\n'
        '  | { status: "loading" }\n'
        '  | { status: "success"; data: T }\n'
        '  | { status: "error"; error: string };\n\n'
        '// The "status" field is the discriminant\n'
        'function renderStocks(state: ApiState<Stock[]>) {\n'
        '  switch (state.status) {\n'
        '    case "idle":\n'
        '      return "Click search to begin";\n'
        '    case "loading":\n'
        '      return "Loading...";\n'
        '    case "success":\n'
        '      // TypeScript KNOWS state.data exists here!\n'
        '      return state.data.map(s => s.ticker).join(", ");\n'
        '    case "error":\n'
        '      // TypeScript KNOWS state.error exists here!\n'
        '      return `Error: ${state.error}`;\n'
        '  }\n'
        '}\n\n'
        '// Type narrowing with typeof\n'
        'function formatValue(value: string | number): string {\n'
        '  if (typeof value === "string") {\n'
        '    return value.toUpperCase();  // string methods available\n'
        '  }\n'
        '  return value.toFixed(2);  // number methods available\n'
        '}\n\n'
        '// Narrowing with truthiness\n'
        'function greet(name: string | null): string {\n'
        '  if (name) {\n'
        '    return `Hello, ${name}`;  // name is string here\n'
        '  }\n'
        '  return "Hello, stranger";   // name is null here\n'
        '}',
        filename="Union Types and Narrowing", styles=styles
    ))

    story.append(principal_box(
        "Discriminated unions are the single most powerful TypeScript pattern. They make impossible "
        "states impossible. You cannot access <code>data</code> when the status is 'loading' because "
        "TypeScript knows that variant does not have a <code>data</code> property. Use them for: API "
        "states, form states, authentication states, modal states \u2014 anywhere you have multiple modes."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand union types, discriminated unions, and type narrowing.", styles))
    story.append(page_break())

    # ================================================================
    # 5.5 GENERICS
    # ================================================================
    story.append(h1("5.5 Generics", styles))
    story.append(analogy_box(
        "Generics are like shipping containers. A shipping container does not care what is inside it \u2014 "
        "it could be electronics, furniture, or food. It just guarantees that whatever goes in comes out "
        "the same type. <code>Container&lt;Electronics&gt;</code> means this container holds electronics. "
        "When you open it, you get electronics, not furniture. Generics let you write reusable code "
        "that works with any type while keeping type safety."
    , styles))

    story.append(code_block(
        '// Generic function - works with any type\n'
        'function first<T>(items: T[]): T | undefined {\n'
        '  return items[0];\n'
        '}\n\n'
        'const firstStock = first(["AAPL", "GOOG"]);  // string | undefined\n'
        'const firstPrice = first([187.44, 141.80]);   // number | undefined\n\n'
        '// Generic interface\n'
        'interface ApiResponse<T> {\n'
        '  data: T;\n'
        '  status: number;\n'
        '  message: string;\n'
        '}\n\n'
        '// Usage - T gets replaced with the specific type\n'
        'type StockResponse = ApiResponse<Stock>;\n'
        '// { data: Stock; status: number; message: string; }\n\n'
        'type StockListResponse = ApiResponse<Stock[]>;\n'
        '// { data: Stock[]; status: number; message: string; }\n\n'
        '// Generic with constraints\n'
        'interface HasId {\n'
        '  id: string;\n'
        '}\n\n'
        'function findById<T extends HasId>(items: T[], id: string): T | undefined {\n'
        '  return items.find(item => item.id === id);\n'
        '}\n'
        '// T must have an "id" property - works with Stock, User, Trade, etc.',
        filename="Generics", styles=styles
    ))

    story.append(h2("Utility Types", styles))
    story.append(code_block(
        '// TypeScript\'s built-in utility types\n\n'
        '// Partial<T> - all properties become optional\n'
        'type StockUpdate = Partial<Stock>;\n'
        '// { ticker?: string; name?: string; price?: number; ... }\n\n'
        '// Required<T> - all properties become required\n'
        'type CompleteSettings = Required<UserSettings>;\n\n'
        '// Pick<T, K> - select specific properties\n'
        'type StockSummary = Pick<Stock, "ticker" | "name" | "price">;\n'
        '// { ticker: string; name: string; price: number; }\n\n'
        '// Omit<T, K> - exclude specific properties\n'
        'type PublicUser = Omit<User, "password" | "email">;\n\n'
        '// Record<K, V> - create an object type\n'
        'type StockPrices = Record<string, number>;\n'
        '// { [key: string]: number }\n'
        'const prices: StockPrices = { AAPL: 187.44, GOOG: 141.80 };\n\n'
        '// Readonly<T> - all properties become readonly\n'
        'type FrozenStock = Readonly<Stock>;\n'
        '// Cannot modify any property after creation\n\n'
        '// ReturnType<T> - extract return type of a function\n'
        'type LoadResult = ReturnType<typeof load>;\n'
        '// Whatever the load function returns',
        filename="Utility Types", styles=styles
    ))

    story.append(spacer(8))
    story.append(checkpoint("You can write generic functions, use constraints, and leverage utility types.", styles))
    story.append(page_break())

    # ================================================================
    # 5.6 ADVANCED PATTERNS
    # ================================================================
    story.append(h1("5.6 Advanced TypeScript Patterns", styles))

    story.append(h2("Type Guards", styles))
    story.append(code_block(
        '// Custom type guard functions\n'
        'interface Stock {\n'
        '  type: "stock";\n'
        '  ticker: string;\n'
        '  price: number;\n'
        '}\n\n'
        'interface Crypto {\n'
        '  type: "crypto";\n'
        '  symbol: string;\n'
        '  price: number;\n'
        '  blockchain: string;\n'
        '}\n\n'
        'type Asset = Stock | Crypto;\n\n'
        '// Type guard function\n'
        'function isStock(asset: Asset): asset is Stock {\n'
        '  return asset.type === "stock";\n'
        '}\n\n'
        'function getIdentifier(asset: Asset): string {\n'
        '  if (isStock(asset)) {\n'
        '    return asset.ticker;  // TypeScript knows it\'s Stock\n'
        '  }\n'
        '  return asset.symbol;    // TypeScript knows it\'s Crypto\n'
        '}',
        filename="Type Guards", styles=styles
    ))

    story.append(h2("Mapped Types", styles))
    story.append(code_block(
        '// Create new types by transforming existing ones\n\n'
        '// Make all properties optional and nullable\n'
        'type Nullable<T> = {\n'
        '  [K in keyof T]: T[K] | null;\n'
        '};\n\n'
        'type NullableStock = Nullable<Stock>;\n'
        '// { ticker: string | null; price: number | null; ... }\n\n'
        '// Create event handler types from an interface\n'
        'type EventHandlers<T> = {\n'
        '  [K in keyof T as `on${Capitalize<string & K>}Change`]: (value: T[K]) => void;\n'
        '};\n\n'
        'type StockHandlers = EventHandlers<Pick<Stock, "price" | "volume">>;\n'
        '// { onPriceChange: (value: number) => void;\n'
        '//   onVolumeChange: (value: number) => void; }',
        filename="Mapped Types", styles=styles
    ))

    story.append(h2("Template Literal Types", styles))
    story.append(code_block(
        '// Type-safe string patterns\n'
        'type HTTPMethod = "GET" | "POST" | "PUT" | "DELETE";\n'
        'type APIRoute = `/api/${string}`;\n\n'
        '// Combine for type-safe API calls\n'
        'function fetchAPI(\n'
        '  method: HTTPMethod,\n'
        '  route: APIRoute\n'
        '): Promise<Response> {\n'
        '  return fetch(route, { method });\n'
        '}\n\n'
        'fetchAPI("GET", "/api/stocks");      // OK\n'
        'fetchAPI("POST", "/api/watchlist");   // OK\n'
        '// fetchAPI("GET", "/stocks");        // Error! Missing /api/ prefix\n'
        '// fetchAPI("PATCH", "/api/stocks");  // Error! PATCH not in HTTPMethod',
        filename="Template Literal Types", styles=styles
    ))

    story.append(mistake_box(
        "Do not over-type your code. TypeScript should make your code safer, not harder to read. "
        "If you find yourself writing 50-line type definitions for simple functions, you are probably "
        "over-engineering. Let inference do its job. Annotate function parameters and return types, "
        "but let TypeScript figure out local variables and intermediate computations."
    , styles))

    story.append(spacer(8))
    story.append(checkpoint("You understand type guards, mapped types, and template literal types.", styles))
    story.append(page_break())

    # ================================================================
    # 5.7 TYPESCRIPT WITH THE DOM AND SVELTE
    # ================================================================
    story.append(h1("5.7 TypeScript with the DOM and Svelte", styles))

    story.append(code_block(
        '// DOM type assertions\n'
        'const input = document.querySelector("input");\n'
        '// Type: HTMLInputElement | null\n\n'
        'if (input) {\n'
        '  input.value = "AAPL";  // Safe - we checked for null\n'
        '}\n\n'
        '// Type assertion when you KNOW the type\n'
        'const canvas = document.getElementById("chart") as HTMLCanvasElement;\n'
        'const ctx = canvas.getContext("2d")!;  // ! asserts non-null\n\n'
        '// Event typing\n'
        'document.addEventListener("click", (event: MouseEvent) => {\n'
        '  console.log(event.clientX, event.clientY);\n'
        '});\n\n'
        'input?.addEventListener("input", (event: Event) => {\n'
        '  const target = event.target as HTMLInputElement;\n'
        '  console.log(target.value);\n'
        '});',
        filename="DOM Types", styles=styles
    ))

    story.append(h2("TypeScript in Svelte 5 Components", styles))
    story.append(code_block(
        '<!-- StockCard.svelte -->\n'
        '<script lang="ts">\n'
        '  import type { Stock } from "$lib/types";\n\n'
        '  interface Props {\n'
        '    stock: Stock;\n'
        '    onremove?: (ticker: string) => void;\n'
        '    highlighted?: boolean;\n'
        '  }\n\n'
        '  let { stock, onremove, highlighted = false }: Props = $props();\n\n'
        '  let priceClass = $derived(\n'
        '    stock.change > 0 ? "positive" :\n'
        '    stock.change < 0 ? "negative" : "neutral"\n'
        '  );\n'
        '</script>\n\n'
        '<div class="stock-card" class:highlighted>\n'
        '  <h3>{stock.ticker}</h3>\n'
        '  <p class={priceClass}>${stock.price.toFixed(2)}</p>\n'
        '  {#if onremove}\n'
        '    <button onclick={() => onremove!(stock.ticker)}>Remove</button>\n'
        '  {/if}\n'
        '</div>\n\n'
        '<!-- Shared types file -->\n'
        '<!-- src/lib/types.ts -->\n'
        'export interface Stock {\n'
        '  ticker: string;\n'
        '  name: string;\n'
        '  price: number;\n'
        '  change: number;\n'
        '  changePercent: number;\n'
        '  volume: number;\n'
        '  marketCap: number;\n'
        '}\n\n'
        'export interface User {\n'
        '  id: string;\n'
        '  name: string;\n'
        '  email: string;\n'
        '  role: "admin" | "user";\n'
        '}\n\n'
        'export interface WatchlistItem {\n'
        '  stock: Stock;\n'
        '  addedAt: string;\n'
        '  notes?: string;\n'
        '}',
        filename="TypeScript in Svelte 5", styles=styles
    ))

    story.append(principal_box(
        "Create a central types file (<code>src/lib/types.ts</code>) for your shared interfaces. "
        "Import from it everywhere. This creates a single source of truth for your data shapes. "
        "When the API changes, you update one file and TypeScript shows you every place that needs "
        "updating. This is one of TypeScript's biggest practical wins."
    , styles))

    story.append(spacer(16))

    # ================================================================
    # EXERCISES
    # ================================================================
    story.append(h1("Chapter 5 Exercises", styles))
    story.append(HorizontalLine())
    story.append(spacer(8))

    story.append(exercise(1, "Type the TradeBoard Data Model", [
        ('ExerciseBody', '<b>Task:</b> Create a types.ts file with interfaces for: Stock (ticker, name, '
         'price, change, changePercent, volume, marketCap), User (id, name, email, role), Trade (id, '
         'userId, ticker, action: buy/sell, quantity, price, timestamp), and WatchlistItem (stock, addedAt, '
         'notes?). Create a StockWithHistory type that extends Stock with a history array.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(2, "Discriminated Union API State", [
        ('ExerciseBody', '<b>Task:</b> Create a generic ApiState type with four variants: idle, loading, '
         'success (with data of type T), and error (with error message). Write a function renderState '
         'that takes ApiState&lt;Stock[]&gt; and returns a string description. Use a switch statement '
         'for exhaustive checking. Try adding a new variant and see what TypeScript tells you.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(3, "Generic Utility Functions", [
        ('ExerciseBody', '<b>Task:</b> Write these generic utility functions: (1) groupBy&lt;T&gt;(items: T[], '
         'key: keyof T): Record&lt;string, T[]&gt; that groups items by a property. (2) sortBy&lt;T&gt;'
         '(items: T[], key: keyof T, order: "asc" | "desc"): T[] that sorts items. (3) paginate&lt;T&gt;'
         '(items: T[], page: number, perPage: number): { data: T[]; total: number; pages: number }. '
         'Test with Stock and Trade arrays.'),
    ], styles))
    story.append(spacer(6))

    story.append(exercise(4, "Type-Safe Event System", [
        ('ExerciseBody', '<b>Task:</b> Build a type-safe event emitter. Define an EventMap interface '
         '(e.g., priceUpdate: { ticker: string; price: number }, tradeExecuted: { trade: Trade }). '
         'Create an EventBus class with on(), off(), and emit() methods where the event name and '
         'payload are fully type-checked. emit("priceUpdate", { wrong: true }) should be a type error.'),
    ], styles))

    story.append(spacer(16))
    story.append(checkpoint("You have mastered TypeScript: types, interfaces, generics, discriminated unions, "
                           "utility types, advanced patterns, and Svelte integration.", styles))
    story.append(page_break())

    return story
