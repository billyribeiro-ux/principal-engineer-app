"""Chapter 1: How the Web Actually Works"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_1(styles):
    story = []

    # Chapter cover
    story.append(ChapterCoverPage(1, "How the Web Actually Works",
                                  "The Restaurant Analogy", "PART 1: FOUNDATIONS"))
    story.append(PageBreak())

    # ================================================================
    # 1.1 THE INTERNET VS THE WEB
    # ================================================================
    story.append(h1("1.1 The Internet vs The Web", styles))
    story.append(p(
        "Before you write a single line of code, you need to understand the stage you are performing on. "
        "Most people use the words 'internet' and 'web' interchangeably. They are not the same thing, and "
        "understanding the difference is your first step toward mastering web development."
    , styles))

    story.append(analogy_box(
        "The internet is the entire road system of a country: highways, streets, dirt roads, and bridges. "
        "The web (World Wide Web) is just one type of business built on those roads — think of it as the "
        "collection of restaurants you can visit. But email is also on those roads (like post offices), "
        "online gaming uses those roads (like arcades), and video streaming does too (like cinemas). "
        "The web is the biggest and most visible business on the internet's roads, but it is not the "
        "roads themselves."
    , styles))

    story.append(p(
        "The <b>internet</b> is a global network of interconnected computers. It was born from ARPANET in 1969, "
        "a US Department of Defense project that connected four university computers. Today it connects billions "
        "of devices worldwide. The internet is infrastructure — cables, routers, satellites, and protocols that "
        "allow machines to send data to each other."
    , styles))
    story.append(p(
        "The <b>World Wide Web</b> was invented by Tim Berners-Lee in 1989 at CERN. It is an application that "
        "runs on top of the internet, using a specific protocol (HTTP) to deliver documents (web pages) that "
        "can link to each other (hyperlinks). The web is just one of many services that use the internet as "
        "its transport layer."
    , styles))

    story.append(h2("How Data Travels: Packets, IP Addresses, and DNS", styles))
    story.append(p(
        "When you send a message across the internet, your data does not travel as one continuous stream. "
        "Instead, it gets broken into small pieces called <b>packets</b>. Each packet is like a postcard: it has "
        "the data payload (the message on the back), a source address, and a destination address. Packets may "
        "take different routes to reach their destination, and they are reassembled upon arrival."
    , styles))

    story.append(analogy_box(
        "Imagine you need to send a 500-page book to a friend across the country. Instead of shipping "
        "the entire book in one huge box, you tear out each page, write the page number and your friend's "
        "address on each one, and drop them all into separate mailboxes. They might arrive out of order — "
        "page 347 might arrive before page 2 — but your friend collects them all and puts them back in order "
        "using the page numbers. That is packet switching."
    , styles))

    story.append(p(
        "Every device on the internet has an <b>IP address</b> — a numerical label that identifies it on the "
        "network. IPv4 addresses look like <font face='Courier'>192.168.1.1</font> (four numbers from 0-255 "
        "separated by dots). Because we are running out of IPv4 addresses (only ~4.3 billion possible), IPv6 "
        "was created with addresses like <font face='Courier'>2001:0db8:85a3:0000:0000:8a2e:0370:7334</font>, "
        "supporting 340 undecillion unique addresses."
    , styles))

    story.append(p(
        "But humans are terrible at remembering numbers. That is where the <b>Domain Name System (DNS)</b> "
        "comes in."
    , styles))

    story.append(analogy_box(
        "DNS is the phone book of the internet. You do not memorize that Google's server is at "
        "142.250.80.46 — you just type 'google.com' and DNS looks up the number for you. When you type "
        "a domain name into your browser, your computer asks a DNS server: 'What IP address does google.com "
        "point to?' The DNS server responds with the number, and your browser connects to that number."
    , styles))

    story.append(h3("The DNS Lookup Process", styles))
    story.append(bullet("Your browser checks its local DNS cache (have I looked this up recently?)", styles))
    story.append(bullet("If not cached, it asks your operating system's DNS resolver", styles))
    story.append(bullet("The resolver asks your ISP's DNS server (the recursive resolver)", styles))
    story.append(bullet("If the ISP does not know, it asks the root DNS servers (13 clusters worldwide)", styles))
    story.append(bullet("The root server directs to the TLD server (.com, .org, .net, etc.)", styles))
    story.append(bullet("The TLD server directs to the authoritative DNS server for that domain", styles))
    story.append(bullet("The authoritative server returns the IP address", styles))
    story.append(bullet("The IP address is cached at every level for future lookups", styles))

    story.append(h3("TCP/IP: The Rules of the Road", styles))
    story.append(p(
        "The internet works because every device follows the same set of rules, called <b>protocols</b>. "
        "The two most fundamental are TCP (Transmission Control Protocol) and IP (Internet Protocol), often "
        "referred to together as TCP/IP."
    , styles))
    story.append(bullet("<b>IP</b> handles addressing and routing — getting packets from point A to point B", styles))
    story.append(bullet("<b>TCP</b> handles reliability — making sure all packets arrive, in order, without corruption", styles))

    story.append(analogy_box(
        "If IP is the postal system that delivers postcards, TCP is the tracking system that confirms "
        "delivery, requests re-sends for lost postcards, and puts everything back in the right order. "
        "IP says 'I will try to get it there.' TCP says 'I guarantee it arrives correctly.'"
    , styles))

    story.append(p(
        "The internet protocol stack has four layers, from bottom to top:"
    , styles))
    story.append(bullet("<b>Network Access Layer</b> — the physical hardware: Ethernet cables, WiFi, fiber optics", styles))
    story.append(bullet("<b>Internet Layer (IP)</b> — addressing and routing packets between networks", styles))
    story.append(bullet("<b>Transport Layer (TCP/UDP)</b> — reliable delivery (TCP) or fast delivery (UDP)", styles))
    story.append(bullet("<b>Application Layer (HTTP, SMTP, FTP)</b> — the protocols apps use to communicate", styles))

    story.append(spacer(8))

    # ================================================================
    # 1.2 CLIENT-SERVER ARCHITECTURE
    # ================================================================
    story.append(h1("1.2 Client-Server Architecture", styles))

    story.append(analogy_box(
        "You (the client) sit at a restaurant table. You look at the menu and decide what you want. "
        "You tell the waiter (the browser) your order (an HTTP request). The waiter walks to the kitchen "
        "(the server), hands over your order, and waits. The kitchen prepares your meal (processes the "
        "request), plates it (formats the response), and hands it back to the waiter. The waiter brings "
        "it to your table (renders the page). You never go into the kitchen yourself — you interact "
        "entirely through the waiter."
    , styles))

    story.append(p(
        "The <b>client-server model</b> is the foundation of how the web works. The client (your browser) "
        "makes requests. The server (a computer somewhere in the world) processes those requests and sends "
        "back responses. This separation is fundamental: the client handles presentation, the server handles "
        "data and logic."
    , styles))

    story.append(h2("What Happens When You Type a URL and Press Enter", styles))
    story.append(p(
        "This is the most important sequence in web development. Every time you load a web page, these "
        "steps execute in roughly this order:"
    , styles))
    story.append(bullet("<b>Step 1:</b> You type <font face='Courier'>https://www.example.com/stocks</font> and press Enter", styles))
    story.append(bullet("<b>Step 2:</b> The browser parses the URL into components: protocol (https), domain (www.example.com), path (/stocks)", styles))
    story.append(bullet("<b>Step 3:</b> The browser checks its DNS cache for the IP address of www.example.com", styles))
    story.append(bullet("<b>Step 4:</b> If not cached, a DNS lookup resolves the domain to an IP address (e.g., 93.184.216.34)", styles))
    story.append(bullet("<b>Step 5:</b> The browser establishes a TCP connection with the server (the 'three-way handshake': SYN, SYN-ACK, ACK)", styles))
    story.append(bullet("<b>Step 6:</b> For HTTPS, a TLS handshake negotiates encryption (certificates, keys, cipher suites)", styles))
    story.append(bullet("<b>Step 7:</b> The browser sends an HTTP GET request: 'Please give me the document at /stocks'", styles))
    story.append(bullet("<b>Step 8:</b> The server receives the request, processes it (runs code, queries databases), and builds a response", styles))
    story.append(bullet("<b>Step 9:</b> The server sends back an HTTP response with a status code (200 OK), headers, and the HTML body", styles))
    story.append(bullet("<b>Step 10:</b> The browser parses the HTML and discovers additional resources (CSS, JS, images)", styles))
    story.append(bullet("<b>Step 11:</b> The browser makes additional HTTP requests for each resource (often in parallel)", styles))
    story.append(bullet("<b>Step 12:</b> As resources arrive, the browser constructs the DOM, applies CSS, executes JavaScript, and paints the page", styles))

    story.append(h2("HTTP Methods: The Verbs of the Web", styles))
    story.append(p(
        "HTTP defines several <b>methods</b> (also called verbs) that describe what action the client wants "
        "the server to take. The four most common map beautifully to CRUD operations:"
    , styles))

    story.append(analogy_box(
        "Back in our restaurant: <b>GET</b> is reading the menu — 'show me what you have.' "
        "<b>POST</b> is placing a new order — 'I would like to create this.' "
        "<b>PUT</b> is changing your entire order — 'replace my order with this new one.' "
        "<b>PATCH</b> is modifying part of your order — 'change just the side dish.' "
        "<b>DELETE</b> is canceling your order — 'I no longer want this.'"
    , styles))

    story.append(bullet("<b>GET</b> — Retrieve data. Should never modify anything on the server. Idempotent (same request, same result).", styles))
    story.append(bullet("<b>POST</b> — Create new data. Submitting a form, creating an account, placing an order.", styles))
    story.append(bullet("<b>PUT</b> — Replace existing data entirely. Update a full user profile.", styles))
    story.append(bullet("<b>PATCH</b> — Partially update existing data. Change just the email address.", styles))
    story.append(bullet("<b>DELETE</b> — Remove data. Delete a post, cancel a subscription.", styles))

    story.append(h2("HTTP Status Codes: The Server's Reply", styles))
    story.append(p("Status codes are three-digit numbers that tell the client what happened with their request.", styles))

    story.append(analogy_box(
        "Status codes are the server's answer to your restaurant order: "
        "<b>200</b> — 'Here is your food, enjoy.' "
        "<b>201</b> — 'Your new order has been created.' "
        "<b>301</b> — 'We moved to a new location. Go there instead.' "
        "<b>304</b> — 'Same food as last time, use what is in your fridge (cache).' "
        "<b>400</b> — 'I cannot understand your order. Please clarify.' "
        "<b>401</b> — 'You need to show your ID first.' "
        "<b>403</b> — 'I see your ID, but you are not allowed in the VIP area.' "
        "<b>404</b> — 'We do not serve that dish. It does not exist.' "
        "<b>429</b> — 'You are ordering too fast. Slow down.' "
        "<b>500</b> — 'The kitchen is on fire. This is our fault, not yours.'"
    , styles))

    story.append(p("Status codes are grouped by their first digit:", styles))
    story.append(bullet("<b>1xx</b> — Informational (hold on, still processing)", styles))
    story.append(bullet("<b>2xx</b> — Success (here is what you asked for)", styles))
    story.append(bullet("<b>3xx</b> — Redirection (go look over there instead)", styles))
    story.append(bullet("<b>4xx</b> — Client Error (you made a mistake in your request)", styles))
    story.append(bullet("<b>5xx</b> — Server Error (we made a mistake on our end)", styles))

    story.append(h2("HTTP Headers: Metadata About the Message", styles))
    story.append(p(
        "Every HTTP request and response includes <b>headers</b> — key-value pairs that carry metadata "
        "about the message. Think of headers as the information written on the outside of an envelope: "
        "who it is from, what format the contents are in, how long it is valid, and security instructions."
    , styles))
    story.append(code_block(
        "GET /stocks/AAPL HTTP/1.1\n"
        "Host: api.tradeboard.com\n"
        "Accept: application/json\n"
        "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...\n"
        "Cache-Control: no-cache\n"
        "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        filename="Example HTTP Request",
        styles=styles
    ))
    story.append(code_block(
        "HTTP/1.1 200 OK\n"
        "Content-Type: application/json; charset=utf-8\n"
        "Content-Length: 1234\n"
        "Cache-Control: max-age=60\n"
        "X-Request-Id: abc-123-def\n\n"
        '{"ticker": "AAPL", "price": 178.52, "change": 2.34}',
        filename="Example HTTP Response",
        styles=styles
    ))
    story.append(spacer(8))

    # ================================================================
    # 1.3 THE BROWSER
    # ================================================================
    story.append(h1("1.3 The Browser — Your Window to the Web", styles))

    story.append(analogy_box(
        "The browser is like a translator who receives a document written in three foreign languages "
        "(HTML, CSS, JavaScript), reads all three simultaneously, and builds a beautiful visual display "
        "for you — complete with interactive buttons, animations, and live-updating content. You never "
        "see the raw code. You see the translated, rendered result."
    , styles))

    story.append(p(
        "A web browser does far more than just 'show websites.' It is a sophisticated piece of software "
        "that performs several major tasks:"
    , styles))
    story.append(bullet("<b>Fetching</b> — Making HTTP requests to servers and downloading HTML, CSS, JS, images, fonts, and other resources", styles))
    story.append(bullet("<b>Parsing</b> — Reading the raw HTML text and converting it into a tree structure (the DOM). Reading CSS and building the CSSOM.", styles))
    story.append(bullet("<b>Rendering</b> — Combining the DOM and CSSOM into a render tree, calculating layout (where everything goes), and painting pixels to the screen", styles))
    story.append(bullet("<b>Executing</b> — Running JavaScript code that can modify the DOM, respond to user interactions, and make additional network requests", styles))

    story.append(h2("The Browser Rendering Pipeline", styles))
    story.append(p("When the browser receives an HTML document, it processes it through a specific pipeline:", styles))
    story.append(bullet("<b>1. DOM Construction</b> — The HTML parser reads the HTML and builds the Document Object Model, a tree of nodes representing every element", styles))
    story.append(bullet("<b>2. CSSOM Construction</b> — The CSS parser reads all CSS and builds the CSS Object Model, a tree of style rules", styles))
    story.append(bullet("<b>3. Render Tree</b> — The browser combines DOM + CSSOM to create the render tree (only visible elements; display:none elements are excluded)", styles))
    story.append(bullet("<b>4. Layout</b> — The browser calculates the exact position and size of every element on the page (also called 'reflow')", styles))
    story.append(bullet("<b>5. Paint</b> — The browser fills in pixels: text, colors, images, borders, shadows", styles))
    story.append(bullet("<b>6. Composite</b> — The browser combines painted layers into the final image you see on screen", styles))

    story.append(h2("Developer Tools — Your X-Ray Vision", styles))
    story.append(p(
        "Every modern browser includes Developer Tools (DevTools), and they are the single most important "
        "tool in a web developer's toolkit. Open them with <font face='Courier'>F12</font> or "
        "<font face='Courier'>Cmd+Option+I</font> (Mac) / <font face='Courier'>Ctrl+Shift+I</font> (Windows/Linux)."
    , styles))
    story.append(bullet("<b>Elements tab</b> — Inspect and modify the DOM in real-time. Click any element on the page to see its HTML and applied CSS. You can edit styles live and see changes instantly.", styles))
    story.append(bullet("<b>Console tab</b> — A JavaScript playground. Type any JavaScript and it executes immediately. Errors and console.log messages appear here.", styles))
    story.append(bullet("<b>Network tab</b> — See every HTTP request the page makes: HTML, CSS, JS, images, API calls. You can see request/response headers, timing, size, and status codes.", styles))
    story.append(bullet("<b>Sources tab</b> — View and debug all loaded source files. Set breakpoints to pause JavaScript execution and step through code line by line.", styles))
    story.append(bullet("<b>Performance tab</b> — Record and analyze page performance: rendering time, scripting time, layout shifts", styles))
    story.append(bullet("<b>Application tab</b> — Inspect localStorage, sessionStorage, cookies, service workers, and other browser storage", styles))

    story.append(mistake_box(
        "Many beginners avoid DevTools because they look intimidating. This is a critical mistake. "
        "DevTools are not optional — they are how you understand what your code is actually doing. "
        "Spend time in the Network tab watching requests flow. Inspect elements to see how CSS is "
        "being applied. Use the Console to test JavaScript snippets. The faster you get comfortable "
        "with DevTools, the faster you grow as a developer."
    , styles))

    story.append(spacer(8))

    # ================================================================
    # 1.4 FILES, FOLDERS, AND YOUR DEV ENVIRONMENT
    # ================================================================
    story.append(h1("1.4 Files, Folders, and Your Development Environment", styles))

    story.append(p(
        "Before you build anything, you need to set up your workspace. A professional development "
        "environment consists of three things: a code editor, a terminal, and an organized file structure."
    , styles))

    story.append(h2("Visual Studio Code (VS Code)", styles))
    story.append(p(
        "VS Code is the most popular code editor in the world, and for good reason. It is free, fast, "
        "extensible, and works on every operating system. Download it from code.visualstudio.com and "
        "install these essential extensions:"
    , styles))
    story.append(bullet("<b>Prettier</b> — Automatic code formatting. Never argue about semicolons or indentation again.", styles))
    story.append(bullet("<b>ESLint</b> — Catches JavaScript/TypeScript errors and enforces coding standards.", styles))
    story.append(bullet("<b>Svelte for VS Code</b> — Syntax highlighting and IntelliSense for Svelte files.", styles))
    story.append(bullet("<b>Live Server</b> — Launches a local web server with live reload for HTML files.", styles))
    story.append(bullet("<b>Auto Rename Tag</b> — Rename paired HTML tags automatically.", styles))

    story.append(h2("The Terminal — Talking Directly to Your Computer", styles))

    story.append(analogy_box(
        "The terminal (also called command line or shell) is like talking directly to your computer's "
        "brain instead of pointing and clicking through its face (the graphical user interface). The GUI "
        "is a friendly face that hides complexity. The terminal gives you direct, unfiltered access to "
        "everything. It is faster, more powerful, and every professional developer uses it daily."
    , styles))

    story.append(p("Essential terminal commands you will use every day:", styles))
    story.append(code_block(
        "pwd                    # Print Working Directory - where am I?\n"
        "ls                     # List files in current directory\n"
        "ls -la                 # List ALL files (including hidden) with details\n"
        "cd projects            # Change Directory - move into 'projects' folder\n"
        "cd ..                  # Move up one directory\n"
        "cd ~                   # Go to home directory\n"
        "mkdir tradeboard       # Make a new directory called 'tradeboard'\n"
        "touch index.html       # Create an empty file called 'index.html'\n"
        "rm oldfile.txt         # Remove (delete) a file\n"
        "rm -r oldfolder        # Remove a directory and everything inside it\n"
        "mv old.txt new.txt     # Move or rename a file\n"
        "cp file.txt backup.txt # Copy a file\n"
        "cat file.txt           # Display file contents in terminal\n"
        "clear                  # Clear the terminal screen",
        filename="Essential Terminal Commands",
        styles=styles
    ))

    story.append(h2("File Paths: Absolute vs Relative", styles))
    story.append(p(
        "Understanding file paths is essential. There are two types:"
    , styles))
    story.append(p(
        "<b>Absolute paths</b> start from the root of the file system. They are like a full street address "
        "including country, state, city, and street: <font face='Courier'>/Users/sarah/projects/tradeboard/index.html</font>"
    , styles))
    story.append(p(
        "<b>Relative paths</b> start from your current location. They are like directions from where you "
        "are standing: <font face='Courier'>./styles/main.css</font> means 'from here, go into the styles "
        "folder, and find main.css.' Two dots (<font face='Courier'>..</font>) means 'go up one level.'"
    , styles))

    story.append(h2("Creating the TradeBoard Project Structure", styles))
    story.append(p("Let us create the folder structure for our course project from the terminal:", styles))
    story.append(code_block(
        "# Create the main project directory\n"
        "mkdir tradeboard\n"
        "cd tradeboard\n\n"
        "# Create the file structure\n"
        "touch index.html\n"
        "mkdir css\n"
        "touch css/styles.css\n"
        "mkdir js\n"
        "touch js/app.js\n"
        "mkdir images\n"
        "mkdir data\n"
        "touch data/stocks.json\n\n"
        "# Verify the structure\n"
        "ls -R\n"
        "# Output:\n"
        "# css/  data/  images/  index.html  js/\n"
        "# css: styles.css\n"
        "# data: stocks.json\n"
        "# js: app.js\n"
        "# images:",
        filename="Terminal: Creating TradeBoard Project",
        styles=styles
    ))

    story.append(h2("Git Basics: Saving Your Work", styles))
    story.append(p(
        "Git is a version control system — it tracks every change you make to your files and lets you "
        "go back to any previous version. Think of it as an unlimited undo system for your entire project."
    , styles))
    story.append(code_block(
        "# Initialize a new Git repository\n"
        "git init\n\n"
        "# Check the status (what files have changed?)\n"
        "git status\n\n"
        "# Stage files for commit (prepare them to be saved)\n"
        "git add index.html\n"
        "git add .            # Stage ALL changed files\n\n"
        "# Commit (save a snapshot with a message)\n"
        "git commit -m \"Initial project structure\"\n\n"
        "# View commit history\n"
        "git log --oneline",
        filename="Git Basics",
        styles=styles
    ))

    story.append(spacer(12))

    # ================================================================
    # EXERCISES
    # ================================================================
    story.append(h1("Chapter 1 Exercises", styles))
    story.append(HorizontalLine())
    story.append(spacer(8))

    story.append(exercise(1, "Trace the Journey of Loading google.com", [
        ('ExerciseBody', '<b>Requirements:</b> Write out, step by step, everything that happens from the moment you type "google.com" into your browser and press Enter until the Google homepage appears on your screen. Include DNS lookup, TCP connection, HTTP request/response, and browser rendering.'),
        ('ExerciseBody', '<b>Hint:</b> Review section 1.2 — there are at least 12 distinct steps.'),
        ('ExerciseBody', '<b>Expected output:</b> A written document with 12+ numbered steps, each with a 1-2 sentence explanation of what happens and why.'),
        ('ExerciseBody', '<b>Level Up Challenge:</b> Open DevTools Network tab, load google.com, and annotate your written steps with actual timing data from the waterfall chart.'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(1, "Make an HTTP Request with curl", [
        ('ExerciseBody', '<b>Requirements:</b> Use the curl command-line tool to make a GET request to a website and read the raw HTML response.'),
        ('ExerciseBody', '<b>Solution:</b>'),
        ('Code', 'curl -v https://example.com'),
        ('ExerciseBody', 'The -v flag (verbose) shows you the full request and response headers. You will see the TCP connection, TLS handshake, HTTP request headers, HTTP response headers, and the HTML body. Study each line.'),
        ('ExerciseBody', '<b>Level Up Challenge:</b> Use curl to make a POST request with JSON data: <font face="Courier">curl -X POST -H "Content-Type: application/json" -d \'{"ticker":"AAPL"}\' https://httpbin.org/post</font>'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(2, "Investigate Network Requests on a News Website", [
        ('ExerciseBody', '<b>Requirements:</b> Open DevTools on a major news website (e.g., bbc.com, nytimes.com). Go to the Network tab. Reload the page and document every type of request you see.'),
        ('ExerciseBody', '<b>Expected output:</b> A categorized list: HTML documents, CSS files, JavaScript files, images, fonts, API/XHR calls, tracking scripts. For each category, note the count and total size.'),
        ('ExerciseBody', '<b>Hint:</b> Use the filter buttons in the Network tab (Doc, CSS, JS, Img, Font, XHR) to isolate each type.'),
        ('ExerciseBody', '<b>Level Up Challenge:</b> Sort requests by size. Which single resource is the largest? Could the page load faster without it? Write your analysis.'),
    ], styles))
    story.append(spacer(8))

    story.append(exercise(2, "Create the TradeBoard Project Structure from Terminal", [
        ('ExerciseBody', '<b>Requirements:</b> Using ONLY the terminal (no file explorer, no VS Code file creation), create the complete TradeBoard project structure with all folders and files.'),
        ('ExerciseBody', '<b>Solution:</b>'),
        ('Code', 'mkdir -p tradeboard/{css,js,images,data}\ntouch tradeboard/index.html\ntouch tradeboard/css/styles.css\ntouch tradeboard/js/app.js\ntouch tradeboard/data/stocks.json\ncd tradeboard\ngit init\ngit add .\ngit commit -m "Initial TradeBoard project structure"'),
        ('ExerciseBody', '<b>Level Up Challenge:</b> Add a .gitignore file that excludes node_modules/, .env, and .DS_Store. Then create a README.md with a project description.'),
    ], styles))

    story.append(spacer(16))
    story.append(checkpoint("You understand how the internet works, how HTTP requests and responses flow, "
                           "how the browser renders pages, and you have your development environment set up. "
                           "You are ready to write your first HTML.", styles))
    story.append(page_break())

    return story
