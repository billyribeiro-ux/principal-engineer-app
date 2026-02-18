"""Chapter 4: JavaScript - Making Things Come Alive"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_4(styles):
    story = []
    story.append(ChapterCoverPage(4, "JavaScript — Making Things Come Alive",
                                  "The Electricity and Plumbing in Your House", "PART 1: FOUNDATIONS"))
    story.append(PageBreak())

    # 4.1
    story.append(h1("4.1 What JavaScript Does", styles))
    story.append(analogy_box(
        "You have built the house (HTML) and decorated it (CSS). JavaScript is the electricity that "
        "powers the lights, the plumbing that makes the faucets work, and the smart home system that "
        "responds when you say 'Hey Siri.' Without JavaScript, your beautiful house is a static model "
        "— pretty to look at, but nothing works."
    , styles))
    story.append(p(
        "JavaScript (JS) is the programming language of the web. Unlike HTML (structure) and CSS (style), "
        "JavaScript adds <b>behavior</b>: responding to clicks, fetching data from servers, updating content "
        "in real time, validating forms, animating elements, and building entire applications."
    , styles))
    story.append(p(
        "JavaScript runs in two environments: the <b>browser</b> (client-side, where it manipulates the DOM "
        "and handles user interactions) and <b>Node.js</b> (server-side, where it handles HTTP requests, "
        "database queries, and file operations). This course focuses primarily on browser JavaScript, with "
        "server-side JS introduced via SvelteKit in Chapter 7."
    , styles))
    story.append(h2("The Script Tag", styles))
    story.append(code_block(
        '&lt;!-- BAD: Blocks HTML parsing --&gt;\n'
        '&lt;script src="app.js"&gt;&lt;/script&gt;\n\n'
        '&lt;!-- GOOD: Waits until HTML is parsed --&gt;\n'
        '&lt;script src="app.js" defer&gt;&lt;/script&gt;\n\n'
        '&lt;!-- Downloads in parallel, executes immediately when ready --&gt;\n'
        '&lt;script src="analytics.js" async&gt;&lt;/script&gt;\n\n'
        '&lt;!-- Modern ES module --&gt;\n'
        '&lt;script type="module" src="app.js"&gt;&lt;/script&gt;',
        filename="Script Loading Strategies", styles=styles))
    story.append(bullet("<b>defer</b> — Downloads in parallel with HTML parsing. Executes after parsing completes. Maintains order. Use this for your app code.", styles))
    story.append(bullet("<b>async</b> — Downloads in parallel, executes immediately when ready. Order not guaranteed. Use for analytics/tracking scripts.", styles))
    story.append(bullet("<b>type=\"module\"</b> — Automatically deferred. Enables import/export. Modern best practice.", styles))

    # 4.2
    story.append(h1("4.2 Variables and Data Types", styles))
    story.append(analogy_box(
        "A variable is a labeled jar on your kitchen shelf. <b>const</b> means you glued the label on — "
        "you cannot relabel the jar. But if the jar contains marbles (an object), you can still add or "
        "remove marbles. <b>let</b> means you can peel off the label and stick it on a different jar entirely. "
        "<b>var</b> is a jar from the 1990s with no label at all — it falls off the shelf, rolls into other "
        "rooms, and causes chaos. Never use var."
    , styles))
    story.append(code_block(
        '// const - cannot be reassigned (use by default)\n'
        'const ticker = "AAPL";\n'
        'const price = 178.52;\n'
        'const isActive = true;\n'
        '// ticker = "MSFT";  // ERROR! Cannot reassign const\n\n'
        '// But const objects/arrays CAN be modified internally\n'
        'const stock = { ticker: "AAPL", price: 178.52 };\n'
        'stock.price = 180.00;  // OK! Modifying property, not reassigning\n\n'
        '// let - can be reassigned (use when value will change)\n'
        'let currentPrice = 178.52;\n'
        'currentPrice = 180.00;  // OK\n\n'
        '// var - NEVER use. Function-scoped, hoisted, causes bugs.\n'
        '// var oldWay = "don\'t do this";',
        filename="Variables: const, let, and why var is dead", styles=styles))

    story.append(h2("Primitive Types", styles))
    story.append(code_block(
        '// string - text\n'
        'const name = "Apple Inc.";\n'
        'const ticker = \'AAPL\';         // single or double quotes\n'
        'const greeting = `Hello ${name}`; // template literal (backticks)\n\n'
        '// number - integers and decimals (no separate int/float)\n'
        'const price = 178.52;\n'
        'const volume = 45_000_000;  // underscores for readability\n'
        'const infinity = Infinity;\n'
        'const notANumber = NaN;     // result of invalid math\n\n'
        '// bigint - for numbers larger than 2^53\n'
        'const marketCap = 2_800_000_000_000n;\n\n'
        '// boolean - true or false\n'
        'const isTrading = true;\n'
        'const isWeekend = false;\n\n'
        '// null - intentionally empty (you set this)\n'
        'const selectedStock = null;\n\n'
        '// undefined - not yet assigned (JS sets this)\n'
        'let watchlist;  // undefined until assigned\n\n'
        '// symbol - unique identifier (advanced, rarely used directly)\n'
        'const id = Symbol("stockId");',
        filename="JavaScript Primitive Types", styles=styles))

    story.append(h2("Type Coercion and Why === Exists", styles))
    story.append(code_block(
        '// == does type coercion (converts types to match)\n'
        '"5" == 5      // true  (string "5" coerced to number 5)\n'
        '"" == false   // true  (empty string is "falsy")\n'
        '0 == false    // true  (0 is "falsy")\n'
        'null == undefined // true (special case)\n\n'
        '// === does NO coercion (strict equality)\n'
        '"5" === 5     // false (string is not number)\n'
        '"" === false  // false\n'
        '0 === false   // false\n\n'
        '// RULE: Always use === and !==. Never use == or !=.',
        filename="Type Coercion", styles=styles))
    story.append(mistake_box(
        "Using == instead of === is the most common JavaScript bug for beginners. "
        "The == operator performs type coercion, which leads to surprising results like "
        "\"\" == false being true. Always use === (strict equality) and !== (strict inequality). "
        "The only exception: checking for null/undefined with == null catches both."
    , styles))

    # 4.3
    story.append(h1("4.3 Operators and Expressions", styles))
    story.append(code_block(
        '// Nullish coalescing (??) - use default only if null/undefined\n'
        'const displayName = stock.name ?? "Unknown";  // "Unknown" only if null/undefined\n'
        '// Different from || which treats 0, "", false as falsy\n'
        'const price = stock.price ?? 0;   // keeps 0 if price is 0\n'
        'const price2 = stock.price || 0;  // replaces 0 with 0 (same here but...)\n'
        'const count = stock.count ?? 10;  // if count is 0, keeps 0\n'
        'const count2 = stock.count || 10; // if count is 0, uses 10! Bug!\n\n'
        '// Optional chaining (?.) - safe property access\n'
        'const ceo = company?.executives?.ceo?.name;  // undefined if any is null\n'
        '// Without ?.: company.executives.ceo.name would THROW if executives is null\n\n'
        '// Template literals - string interpolation\n'
        'const message = `${ticker} is trading at $${price.toFixed(2)}`;\n'
        'const multiline = `\n'
        '  Line 1\n'
        '  Line 2\n'
        '`;',
        filename="Modern Operators", styles=styles))

    story.append(h2("Destructuring", styles))
    story.append(code_block(
        '// Object destructuring - pull properties into variables\n'
        'const stock = { ticker: "AAPL", price: 178.52, change: 2.34 };\n'
        'const { ticker, price, change } = stock;\n'
        'console.log(ticker);  // "AAPL"\n\n'
        '// Rename during destructuring\n'
        'const { ticker: symbol, price: currentPrice } = stock;\n\n'
        '// Default values\n'
        'const { volume = 0, exchange = "NYSE" } = stock;\n\n'
        '// Array destructuring\n'
        'const prices = [178.52, 176.20, 180.10];\n'
        'const [latest, previous, ...rest] = prices;\n'
        'console.log(latest);    // 178.52\n'
        'console.log(rest);      // [180.10]\n\n'
        '// Swap variables without temp\n'
        'let a = 1, b = 2;\n'
        '[a, b] = [b, a];  // a = 2, b = 1',
        filename="Destructuring", styles=styles))

    story.append(h2("Spread and Rest Operators", styles))
    story.append(code_block(
        '// Spread (...) - expand an array or object\n'
        'const watchlist = ["AAPL", "MSFT"];\n'
        'const extended = [...watchlist, "GOOGL", "AMZN"];\n'
        '// ["AAPL", "MSFT", "GOOGL", "AMZN"]\n\n'
        '// Spread for objects (shallow copy + override)\n'
        'const defaults = { exchange: "NYSE", currency: "USD" };\n'
        'const config = { ...defaults, currency: "EUR" };\n'
        '// { exchange: "NYSE", currency: "EUR" }\n\n'
        '// Rest (...) - collect remaining items\n'
        'function logStock(ticker, ...details) {\n'
        '  console.log(ticker);   // "AAPL"\n'
        '  console.log(details);  // [178.52, "Technology"]\n'
        '}\n'
        'logStock("AAPL", 178.52, "Technology");',
        filename="Spread and Rest", styles=styles))

    # 4.4
    story.append(h1("4.4 Control Flow", styles))
    story.append(code_block(
        '// if/else\n'
        'if (change > 0) {\n'
        '  console.log("Stock is up!");\n'
        '} else if (change < 0) {\n'
        '  console.log("Stock is down.");\n'
        '} else {\n'
        '  console.log("No change.");\n'
        '}\n\n'
        '// Ternary operator (for simple conditions)\n'
        'const status = change > 0 ? "up" : "down";\n'
        'const color = change > 0 ? "green" : change < 0 ? "red" : "gray";\n\n'
        '// Early returns - Principal Engineers do not nest 5 levels deep\n'
        'function getStockDisplay(stock) {\n'
        '  if (!stock) return "No stock selected";\n'
        '  if (!stock.price) return "Price unavailable";\n'
        '  if (stock.isDelisted) return `${stock.ticker} (Delisted)`;\n'
        '  return `${stock.ticker}: $${stock.price.toFixed(2)}`;\n'
        '}',
        filename="Control Flow and Early Returns", styles=styles))

    story.append(principal_box(
        "Early returns flatten deeply nested code. Instead of if/else chains that indent five levels deep, "
        "check for error conditions first and return early. The 'happy path' (the main logic) should be at "
        "the lowest indentation level. This is a hallmark of senior and principal engineer code — it is "
        "dramatically easier to read, test, and maintain."
    , styles))

    story.append(h2("Loops", styles))
    story.append(code_block(
        '// for...of - iterate over array VALUES (use this most)\n'
        'const stocks = ["AAPL", "MSFT", "GOOGL"];\n'
        'for (const stock of stocks) {\n'
        '  console.log(stock);  // "AAPL", "MSFT", "GOOGL"\n'
        '}\n\n'
        '// for...in - iterate over object KEYS\n'
        'const prices = { AAPL: 178, MSFT: 415, GOOGL: 174 };\n'
        'for (const ticker in prices) {\n'
        '  console.log(`${ticker}: $${prices[ticker]}`);\n'
        '}\n\n'
        '// Classic for loop (when you need the index)\n'
        'for (let i = 0; i < stocks.length; i++) {\n'
        '  console.log(`${i + 1}. ${stocks[i]}`);\n'
        '}\n\n'
        '// while loop (when you do not know how many iterations)\n'
        'let attempts = 0;\n'
        'while (attempts < 3) {\n'
        '  // try to fetch data...\n'
        '  attempts++;\n'
        '}',
        filename="Loop Types", styles=styles))

    # 4.5
    story.append(h1("4.5 Functions — The Building Blocks", styles))
    story.append(analogy_box(
        "A function is a recipe. You give it ingredients (arguments), it follows steps (the function body), "
        "and it gives you back a dish (the return value). You can reuse the same recipe with different "
        "ingredients every time. A function that always produces the same dish from the same ingredients "
        "is called a 'pure function' — no surprises, ever."
    , styles))

    story.append(code_block(
        '// Function declaration (hoisted - available before definition)\n'
        'function formatPrice(price) {\n'
        '  return `$${price.toFixed(2)}`;\n'
        '}\n\n'
        '// Function expression (NOT hoisted)\n'
        'const formatChange = function(change) {\n'
        '  const sign = change >= 0 ? "+" : "";\n'
        '  return `${sign}${change.toFixed(2)}`;\n'
        '};\n\n'
        '// Arrow function (concise, does not bind its own "this")\n'
        'const formatPercent = (value) => `${(value * 100).toFixed(2)}%`;\n\n'
        '// Arrow with body (for multi-line logic)\n'
        'const formatStock = (stock) => {\n'
        '  const priceStr = formatPrice(stock.price);\n'
        '  const changeStr = formatChange(stock.change);\n'
        '  return `${stock.ticker}: ${priceStr} (${changeStr})`;\n'
        '};\n\n'
        '// Default parameters\n'
        'function fetchStocks(exchange = "NYSE", limit = 10) {\n'
        '  console.log(`Fetching ${limit} stocks from ${exchange}`);\n'
        '}\n'
        'fetchStocks();           // "Fetching 10 stocks from NYSE"\n'
        'fetchStocks("NASDAQ");   // "Fetching 10 stocks from NASDAQ"\n'
        'fetchStocks("LSE", 25); // "Fetching 25 stocks from LSE"',
        filename="Function Types", styles=styles))

    story.append(h2("Closures — The Backpack Analogy", styles))
    story.append(analogy_box(
        "A closure is like a backpack. When you create a function inside another function, the inner "
        "function packs up all the variables from its parent into a backpack. Even after the parent "
        "function finishes and its local variables would normally be garbage collected, the inner function "
        "still carries them in its backpack. It remembers its birthplace."
    , styles))
    story.append(code_block(
        '// Closure example: counter factory\n'
        'function createCounter(initialValue = 0) {\n'
        '  let count = initialValue;  // This goes in the "backpack"\n\n'
        '  return {\n'
        '    increment() { count++; return count; },\n'
        '    decrement() { count--; return count; },\n'
        '    getCount()  { return count; }\n'
        '  };\n'
        '}\n\n'
        'const counter = createCounter(10);\n'
        'console.log(counter.increment()); // 11\n'
        'console.log(counter.increment()); // 12\n'
        'console.log(counter.getCount());  // 12\n'
        '// "count" is private! You cannot access it directly.\n'
        '// Only the returned methods can see it (via the closure backpack).\n\n'
        '// Practical closure: price tracker\n'
        'function createPriceTracker(ticker) {\n'
        '  const history = [];\n\n'
        '  return {\n'
        '    addPrice(price) {\n'
        '      history.push({ price, timestamp: Date.now() });\n'
        '    },\n'
        '    getAverage() {\n'
        '      if (history.length === 0) return 0;\n'
        '      const sum = history.reduce((acc, h) => acc + h.price, 0);\n'
        '      return sum / history.length;\n'
        '    },\n'
        '    getHistory() { return [...history]; }  // Return copy, not original\n'
        '  };\n'
        '}\n\n'
        'const aaplTracker = createPriceTracker("AAPL");\n'
        'aaplTracker.addPrice(178.52);\n'
        'aaplTracker.addPrice(180.10);\n'
        'console.log(aaplTracker.getAverage()); // 179.31',
        filename="Closures", styles=styles))

    # 4.6
    story.append(h1("4.6 Objects and Arrays — Deep Dive", styles))
    story.append(analogy_box(
        "Array methods are like an assembly line in a factory. <b>.map()</b> is a machine that transforms "
        "every item on the belt — raw material in, finished product out. <b>.filter()</b> is quality control "
        "that removes items that do not pass inspection. <b>.reduce()</b> is the machine that takes all items "
        "and combines them into one final product — like melting all the metal scraps into one ingot."
    , styles))
    story.append(code_block(
        'const stocks = [\n'
        '  { ticker: "AAPL", price: 178.52, change: 2.34, sector: "Tech" },\n'
        '  { ticker: "MSFT", price: 415.20, change: -3.10, sector: "Tech" },\n'
        '  { ticker: "JNJ",  price: 156.80, change: 0.45, sector: "Health" },\n'
        '  { ticker: "JPM",  price: 198.30, change: -1.20, sector: "Finance" },\n'
        '  { ticker: "GOOGL", price: 174.85, change: 1.20, sector: "Tech" },\n'
        '];\n\n'
        '// .map() - transform every item\n'
        'const tickers = stocks.map(s => s.ticker);\n'
        '// ["AAPL", "MSFT", "JNJ", "JPM", "GOOGL"]\n\n'
        'const displays = stocks.map(s =>\n'
        '  `${s.ticker}: $${s.price.toFixed(2)}`\n'
        ');\n\n'
        '// .filter() - keep items that pass the test\n'
        'const gainers = stocks.filter(s => s.change > 0);\n'
        '// [AAPL, JNJ, GOOGL]\n\n'
        'const techStocks = stocks.filter(s => s.sector === "Tech");\n\n'
        '// .reduce() - combine all items into one value\n'
        'const totalValue = stocks.reduce((sum, s) => sum + s.price, 0);\n'
        '// 1123.67\n\n'
        'const bySector = stocks.reduce((acc, s) => {\n'
        '  acc[s.sector] = acc[s.sector] || [];\n'
        '  acc[s.sector].push(s);\n'
        '  return acc;\n'
        '}, {});\n'
        '// { Tech: [...], Health: [...], Finance: [...] }\n\n'
        '// .find() - get first match (or undefined)\n'
        'const apple = stocks.find(s => s.ticker === "AAPL");\n\n'
        '// .some() / .every() - boolean checks\n'
        'const anyGainers = stocks.some(s => s.change > 0);   // true\n'
        'const allGainers = stocks.every(s => s.change > 0);  // false\n\n'
        '// Chaining methods\n'
        'const topTechGainers = stocks\n'
        '  .filter(s => s.sector === "Tech")\n'
        '  .filter(s => s.change > 0)\n'
        '  .sort((a, b) => b.change - a.change)\n'
        '  .map(s => s.ticker);\n'
        '// ["AAPL", "GOOGL"]',
        filename="Array Methods — The Assembly Line", styles=styles))

    # 4.7
    story.append(h1("4.7 The DOM — JavaScript Meets HTML", styles))
    story.append(analogy_box(
        "The DOM (Document Object Model) is a family tree that the browser builds from your HTML. "
        "Every HTML element becomes a family member (node) with parents, children, and siblings. "
        "JavaScript can add new family members, remove existing ones, change their appearance, or "
        "rearrange the entire family. The DOM is the bridge between your HTML and your JavaScript."
    , styles))
    story.append(code_block(
        '// Selecting elements\n'
        'const header = document.getElementById("main-header");\n'
        'const firstCard = document.querySelector(".stock-card");\n'
        'const allCards = document.querySelectorAll(".stock-card");\n'
        '// querySelectorAll returns NodeList, not Array\n'
        '// Convert: const cards = [...allCards]; or Array.from(allCards)\n\n'
        '// Modifying elements\n'
        'header.textContent = "TradeBoard Dashboard";  // Set text (safe)\n'
        'header.innerHTML = "<em>TradeBoard</em>";     // Set HTML (XSS risk!)\n'
        'header.classList.add("active");\n'
        'header.classList.remove("loading");\n'
        'header.classList.toggle("dark-mode");\n'
        'header.style.color = "#e94560";\n'
        'header.setAttribute("data-page", "dashboard");\n\n'
        '// Creating elements\n'
        'const card = document.createElement("div");\n'
        'card.className = "stock-card";\n'
        'card.innerHTML = `\n'
        '  <h3>AAPL</h3>\n'
        '  <p class="price">$178.52</p>\n'
        '  <p class="change positive">+1.33%</p>\n'
        '`;\n'
        'document.querySelector(".stock-list").appendChild(card);\n\n'
        '// Removing elements\n'
        'card.remove();\n\n'
        '// Document Fragment (batch operations for performance)\n'
        'const fragment = document.createDocumentFragment();\n'
        'stocks.forEach(stock => {\n'
        '  const row = document.createElement("tr");\n'
        '  row.innerHTML = `<td>${stock.ticker}</td><td>$${stock.price}</td>`;\n'
        '  fragment.appendChild(row);\n'
        '});\n'
        'document.querySelector("tbody").appendChild(fragment);\n'
        '// Only ONE DOM update instead of N updates!',
        filename="DOM Manipulation", styles=styles))

    # 4.8
    story.append(h1("4.8 Events — Responding to User Actions", styles))
    story.append(analogy_box(
        "Event delegation is like having one receptionist for an entire office building instead of one "
        "at every single door. The receptionist (parent element) listens for all visitors (events), "
        "checks which office (child element) they are looking for using event.target, and routes them "
        "accordingly. One listener, handles everything."
    , styles))
    story.append(code_block(
        '// Adding event listeners (the RIGHT way)\n'
        'const searchInput = document.querySelector("#search");\n'
        'searchInput.addEventListener("input", (event) => {\n'
        '  const query = event.target.value.toUpperCase();\n'
        '  filterStockTable(query);\n'
        '});\n\n'
        '// Form submission\n'
        'const form = document.querySelector("#search-form");\n'
        'form.addEventListener("submit", (event) => {\n'
        '  event.preventDefault();  // Stop page reload\n'
        '  const formData = new FormData(form);\n'
        '  const ticker = formData.get("ticker");\n'
        '  searchStock(ticker);\n'
        '});\n\n'
        '// Event delegation - ONE listener for many children\n'
        'const stockTable = document.querySelector("#stock-table tbody");\n'
        'stockTable.addEventListener("click", (event) => {\n'
        '  const row = event.target.closest("tr");\n'
        '  if (!row) return;  // Clicked outside a row\n'
        '  const ticker = row.dataset.ticker;\n'
        '  showStockDetail(ticker);\n'
        '});\n'
        '// Works for existing rows AND rows added later!',
        filename="Events and Event Delegation", styles=styles))

    # 4.9
    story.append(h1("4.9 Asynchronous JavaScript", styles))
    story.append(analogy_box(
        "JavaScript is a single-threaded chef. He can only do ONE thing at a time. But he is smart — "
        "when he puts something in the oven (async operation like a network request), he does not stand "
        "there staring at it. He starts the next task — chopping vegetables, plating a dish — and comes "
        "back when the oven timer dings (the callback/promise resolves). This is the event loop."
    , styles))
    story.append(p(
        "The <b>event loop</b> is how JavaScript handles concurrency with a single thread. It works like this: "
        "synchronous code runs on the <b>call stack</b>. Async operations (setTimeout, fetch, event listeners) "
        "are handed off to the browser's Web APIs. When an async operation completes, its callback goes into "
        "the <b>task queue</b>. The event loop checks: 'Is the call stack empty? If yes, take the next task from "
        "the queue and push it onto the stack.' Promise callbacks go into the <b>microtask queue</b>, which has "
        "higher priority than the regular task queue."
    , styles))

    story.append(h2("Promises and async/await", styles))
    story.append(analogy_box(
        "A Promise is like ordering food delivery. When you place the order, you get a tracking number "
        "(the Promise object). The order will either arrive successfully (resolved/fulfilled) or get "
        "cancelled (rejected). You do not wait at the door — you go about your life and react when "
        "the status updates. .then() is 'when it arrives, do this.' .catch() is 'if it fails, do this.'"
    , styles))
    story.append(code_block(
        '// Fetch API with Promises\n'
        'fetch("https://api.example.com/stocks/AAPL")\n'
        '  .then(response => {\n'
        '    if (!response.ok) throw new Error(`HTTP ${response.status}`);\n'
        '    return response.json();\n'
        '  })\n'
        '  .then(data => {\n'
        '    console.log(data.price);\n'
        '  })\n'
        '  .catch(error => {\n'
        '    console.error("Failed to fetch:", error.message);\n'
        '  });\n\n'
        '// Same thing with async/await (MUCH cleaner)\n'
        'async function getStockPrice(ticker) {\n'
        '  try {\n'
        '    const response = await fetch(\n'
        '      `https://api.example.com/stocks/${ticker}`\n'
        '    );\n'
        '    if (!response.ok) {\n'
        '      throw new Error(`HTTP ${response.status}`);\n'
        '    }\n'
        '    const data = await response.json();\n'
        '    return data.price;\n'
        '  } catch (error) {\n'
        '    console.error(`Failed to fetch ${ticker}:`, error.message);\n'
        '    return null;\n'
        '  }\n'
        '}\n\n'
        '// Using it\n'
        'const price = await getStockPrice("AAPL");\n'
        'console.log(price);  // 178.52\n\n'
        '// Fetch multiple stocks in parallel\n'
        'const tickers = ["AAPL", "MSFT", "GOOGL"];\n'
        'const prices = await Promise.all(\n'
        '  tickers.map(t => getStockPrice(t))\n'
        ');\n'
        '// [178.52, 415.20, 174.85] - all fetched in parallel!\n\n'
        '// Promise.allSettled - get ALL results even if some fail\n'
        'const results = await Promise.allSettled(\n'
        '  tickers.map(t => getStockPrice(t))\n'
        ');\n'
        '// [{status:"fulfilled",value:178.52}, ...]\n\n'
        '// AbortController - cancel requests\n'
        'const controller = new AbortController();\n'
        'const response = await fetch(url, {\n'
        '  signal: controller.signal\n'
        '});\n'
        '// Later: controller.abort();  // Cancels the request',
        filename="Async/Await and Fetch", styles=styles))

    # 4.10
    story.append(h1("4.10 ES Modules", styles))
    story.append(analogy_box(
        "Modules are like separate rooms in a house. Each room has its own stuff, and you only "
        "bring items to other rooms when specifically needed (exports). This keeps your house "
        "organized instead of having everything dumped in one giant room."
    , styles))
    story.append(code_block(
        '// utils/formatters.js - Named exports\n'
        'export function formatPrice(price) {\n'
        '  return `$${price.toFixed(2)}`;\n'
        '}\n\n'
        'export function formatPercent(value) {\n'
        '  return `${(value * 100).toFixed(2)}%`;\n'
        '}\n\n'
        '// utils/api.js - Default export\n'
        'export default class StockAPI {\n'
        '  async getPrice(ticker) { /* ... */ }\n'
        '  async search(query) { /* ... */ }\n'
        '}\n\n'
        '// app.js - Importing\n'
        'import StockAPI from "./utils/api.js";\n'
        'import { formatPrice, formatPercent } from "./utils/formatters.js";\n\n'
        '// Dynamic import (lazy loading)\n'
        'const chartModule = await import("./chart.js");\n'
        'chartModule.renderChart(data);',
        filename="ES Modules", styles=styles))

    # 4.11
    story.append(h1("4.11 Error Handling and Debugging", styles))
    story.append(code_block(
        '// try/catch/finally\n'
        'try {\n'
        '  const data = JSON.parse(rawInput);\n'
        '  processData(data);\n'
        '} catch (error) {\n'
        '  if (error instanceof SyntaxError) {\n'
        '    console.error("Invalid JSON:", error.message);\n'
        '  } else {\n'
        '    throw error;  // Re-throw unexpected errors\n'
        '  }\n'
        '} finally {\n'
        '  hideLoadingSpinner();  // Always runs\n'
        '}\n\n'
        '// Custom error class\n'
        'class StockNotFoundError extends Error {\n'
        '  constructor(ticker) {\n'
        '    super(`Stock not found: ${ticker}`);\n'
        '    this.name = "StockNotFoundError";\n'
        '    this.ticker = ticker;\n'
        '  }\n'
        '}\n\n'
        '// Console methods beyond console.log\n'
        'console.table(stocks);       // Display as table\n'
        'console.group("API Call");   // Group related logs\n'
        'console.log("URL:", url);\n'
        'console.log("Response:", data);\n'
        'console.groupEnd();\n'
        'console.time("fetch");       // Measure time\n'
        'await fetch(url);\n'
        'console.timeEnd("fetch");    // "fetch: 234ms"',
        filename="Error Handling", styles=styles))

    # 4.12
    story.append(h1("4.12 Web APIs You Must Know", styles))
    story.append(code_block(
        '// localStorage - persist data across sessions\n'
        'const watchlist = ["AAPL", "MSFT", "GOOGL"];\n'
        'localStorage.setItem("watchlist", JSON.stringify(watchlist));\n\n'
        'const saved = JSON.parse(localStorage.getItem("watchlist") || "[]");\n'
        'console.log(saved);  // ["AAPL", "MSFT", "GOOGL"]\n\n'
        '// IntersectionObserver - detect when elements enter viewport\n'
        'const observer = new IntersectionObserver((entries) => {\n'
        '  entries.forEach(entry => {\n'
        '    if (entry.isIntersecting) {\n'
        '      entry.target.classList.add("visible");\n'
        '      loadStockData(entry.target.dataset.ticker);\n'
        '    }\n'
        '  });\n'
        '}, { threshold: 0.1 });\n\n'
        '// Observe all stock cards for lazy loading\n'
        'document.querySelectorAll(".stock-card").forEach(card => {\n'
        '  observer.observe(card);\n'
        '});',
        filename="Web APIs: localStorage and IntersectionObserver", styles=styles))

    # 4.13
    story.append(h1("4.13 JavaScript Patterns at Principal Engineer Level", styles))
    story.append(principal_box(
        "At Principal Engineer level, JavaScript is not just about making things work — it is about "
        "making things work reliably for millions of users, maintainably for a team of 20 engineers, "
        "and performantly on devices from flagship phones to budget Chromebooks. You think about "
        "debounce/throttle for performance, pub/sub for decoupling, memory leaks from forgotten event "
        "listeners, XSS vulnerabilities from innerHTML, and bundle size impact of every dependency."
    , styles))
    story.append(code_block(
        '// Debounce - delay execution until user stops typing\n'
        'function debounce(fn, delay = 300) {\n'
        '  let timeoutId;\n'
        '  return (...args) => {\n'
        '    clearTimeout(timeoutId);\n'
        '    timeoutId = setTimeout(() => fn(...args), delay);\n'
        '  };\n'
        '}\n\n'
        'const debouncedSearch = debounce((query) => {\n'
        '  fetchStocks(query);\n'
        '}, 300);\n\n'
        'searchInput.addEventListener("input", (e) => {\n'
        '  debouncedSearch(e.target.value);\n'
        '});\n\n'
        '// Throttle - execute at most once per interval\n'
        'function throttle(fn, interval = 100) {\n'
        '  let lastTime = 0;\n'
        '  return (...args) => {\n'
        '    const now = Date.now();\n'
        '    if (now - lastTime >= interval) {\n'
        '      lastTime = now;\n'
        '      fn(...args);\n'
        '    }\n'
        '  };\n'
        '}\n\n'
        '// Pub/Sub pattern - decouple components\n'
        'class EventBus {\n'
        '  #listeners = new Map();\n\n'
        '  on(event, callback) {\n'
        '    if (!this.#listeners.has(event)) {\n'
        '      this.#listeners.set(event, new Set());\n'
        '    }\n'
        '    this.#listeners.get(event).add(callback);\n'
        '    return () => this.#listeners.get(event).delete(callback);\n'
        '  }\n\n'
        '  emit(event, data) {\n'
        '    this.#listeners.get(event)?.forEach(cb => cb(data));\n'
        '  }\n'
        '}\n\n'
        'const bus = new EventBus();\n'
        'const unsub = bus.on("priceUpdate", (data) => {\n'
        '  updateUI(data);\n'
        '});\n'
        'bus.emit("priceUpdate", { ticker: "AAPL", price: 180.00 });\n'
        'unsub();  // Clean up when done',
        filename="Debounce, Throttle, and Pub/Sub", styles=styles))

    # EXERCISES
    story.append(spacer(12))
    story.append(h1("Chapter 4 Exercises", styles))
    story.append(HorizontalLine())
    story.append(spacer(8))

    story.append(exercise(1, "Real-Time Table Filter", [
        ('ExerciseBody', '<b>Requirements:</b> Add JavaScript to TradeBoard that filters the stock table in real-time as the user types in the search input. Match against ticker symbol and company name (case-insensitive). Hide non-matching rows.'),
        ('ExerciseBody', '<b>Hint:</b> Use addEventListener("input", ...) on the search field and toggle display on each tr.'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(2, "Stock Price Formatter", [
        ('ExerciseBody', '<b>Requirements:</b> Create three functions: formatCurrency(178.5) returns "$178.50", formatChange(2.34) returns "+$2.34" (with sign and color class), formatLargeNumber(2800000000000) returns "2.80T". Handle M (million), B (billion), T (trillion).'),
        ('ExerciseBody', '<b>Solution:</b>'),
        ('Code', 'function formatLargeNumber(n) {\n  if (n >= 1e12) return `${(n/1e12).toFixed(2)}T`;\n  if (n >= 1e9)  return `${(n/1e9).toFixed(2)}B`;\n  if (n >= 1e6)  return `${(n/1e6).toFixed(2)}M`;\n  return n.toLocaleString();\n}'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(2, "localStorage Watchlist System", [
        ('ExerciseBody', '<b>Requirements:</b> Build functions to: addToWatchlist(ticker), removeFromWatchlist(ticker), getWatchlist(), clearWatchlist(). All persist to localStorage. Handle the case where localStorage is unavailable (private browsing).'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(3, "Real-Time Stock Price Simulator", [
        ('ExerciseBody', '<b>Requirements:</b> Create a mock API that returns stock prices after a random delay (200-1000ms). Display prices that update every 2 seconds. Show green for positive changes, red for negative. Handle errors gracefully with a retry mechanism.'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(4, "Infinite Scroll with IntersectionObserver", [
        ('ExerciseBody', '<b>Requirements:</b> Build an infinitely scrolling stock list. Load 20 stocks at a time. Use IntersectionObserver to detect when the user scrolls near the bottom. Add debounced search. Show skeleton loading states. Use AbortController to cancel previous requests when a new search starts.'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(5, "Pub/Sub Event System for TradeBoard", [
        ('ExerciseBody', '<b>Requirements:</b> Build a complete event bus that decouples the data layer from the UI. Events: "priceUpdate", "watchlistChange", "searchResults", "error". Support middleware (logging, error boundaries). Support wildcard subscriptions. Include TypeScript-ready JSDoc types.'),
    ], styles))

    story.append(spacer(16))
    story.append(checkpoint("You can write JavaScript: variables, functions, closures, DOM manipulation, "
                           "events, async/await, fetch, modules, and professional patterns. "
                           "Part 1 is complete. Time to level up with TypeScript.", styles))
    story.append(page_break())
    return story
