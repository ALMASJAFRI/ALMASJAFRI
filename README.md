<div align="center">

<img src="./banner.svg" width="100%" alt="Almas Jafri" />

<a href="https://github.com/ALMASJAFRI">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=19&duration=3000&pause=900&color=38BDF8&center=true&vCenter=true&width=720&height=40&lines=Backend+and+Full-Stack+Developer;Python+%7C+Django+%7C+.NET+Core+%7C+AI+Agents;7+Months+of+Internship+Experience;190%2B+LeetCode+Problems+Solved" alt="Typing SVG" />
</a>

<br/><br/>

<a href="https://linkedin.com/in/almasjafri"><img src="https://img.shields.io/badge/LinkedIn-almasjafri-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="https://github.com/ALMASJAFRI"><img src="https://img.shields.io/badge/GitHub-ALMASJAFRI-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="mailto:almasjafri12@gmail.com"><img src="https://img.shields.io/badge/Email-almasjafri12%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>

<sub>📍 Lucknow, UP, India</sub>

</div>

<br/>

## 👋 Professional Summary

> Backend and Full-Stack Developer with **7 months of internship experience** building **.NET Core APIs**, **SQL Server stored procedures**, and **Python automation systems**, alongside **3+ production Django and AI applications**. Proven track record in scaling authentication endpoints using in-memory **Bloom filters (0.01% false positive rate)**, enforcing single sign-in via **JWT token versioning**, and building multi-agent **LangGraph CLI tools with hybrid RAG retrieval**. Solved **190+ LeetCode problems** demonstrating strong data structures and algorithms proficiency.

<br/>

## 💼 Work Experience

<table width="100%">
<tr>
<td>

### Backend Developer Intern · Brainpan Innovation
<img src="https://img.shields.io/badge/Apr%202026%20%E2%80%93%20Present-0ea5e9?style=flat-square" /> <img src="https://img.shields.io/badge/.NET%20Core-512BD4?style=flat-square&logo=dotnet&logoColor=white" /> <img src="https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white" /> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />

- 🔐 Engineered authentication and logging APIs in **.NET Core**, enforcing single sign-in across active sessions via **JWT token versioning** assigned at user registration and verified through custom middleware on **100% of incoming requests**.
- ⚡ Scaled the user login API by registering an in-memory **Bloom filter** on server startup to track unique emails with a **0.01% false positive tolerance**, filtering out **99.99%** of non-existent email lookups before hitting the database.
- 🧱 Developed **10+ RESTful Admin APIs** in .NET Core for the **SDA Saharanpur portal** to manage dynamic homepage UI components, writing end-to-end SQL Server stored procedures and multi-table joins to reduce query execution overhead.
- 🛡 Implemented binary file validation for uploaded notice documents by inspecting the first **11 bytes (magic bytes)** of each file stream, blocking **100% of spoofed file extensions** prior to storage.
- 🏛 Constructed a digital PDF signature API using **iTextSharp** and **BouncyCastle** that consumes official **Digital Signature Certificate (DSC)** payloads from an upstream endpoint to cryptographically sign official government PDFs.
- 🤖 Automated dashboard reporting workflows using **Python** and **RapidOCR**, capturing live automation screenshots and generating structured Excel reports in a separate background thread to maintain zero main-thread blocking.

</td>
</tr>
</table>

<table width="100%">
<tr>
<td>

### Full-Stack Python Developer · Open Source & Freelance
<img src="https://img.shields.io/badge/Sep%202025%20%E2%80%93%20Mar%202026-0ea5e9?style=flat-square" /> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" /> <img src="https://img.shields.io/badge/DRF-A30000?style=flat-square&logo=django&logoColor=white" /> <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />

- 🏗 Architected **3+ full-stack web applications** using Django and Django REST Framework (DRF) featuring custom email and OTP authentication, role-based access control, and automated request validation.
- 🚀 Optimized database query performance and reduced API latency by implementing **Redis caching layers**, Django ORM query analysis, and concurrent data ingestion pipelines into **Pinecone** vector indexes.
- ☁️ Deployed production applications across **Render, PythonAnywhere, and Railway** with Cloudinary CDN integration for optimized media delivery and SHA-512 cryptographic hashing for secure payment processing.

</td>
</tr>
</table>

<br/>

## 🧠 Projects

<table width="100%">
<tr>
<td>

### 💻 Docmaker & Docmaker-CLI — Autonomous CLI Agent & DaaS Platform
<img src="https://img.shields.io/badge/Nov%202025-0ea5e9?style=flat-square" />
<sub>Python · LangGraph · LangChain · ChromaDB · Pinecone · BM25 · Tree-sitter · NetworkX · Pydantic · Textual · Playwright · Django · Redis · Celery</sub>

- Created an autonomous local CLI developer agent using **LangGraph** (boss orchestrator and specialist subagents) to generate **7 types of evidence-backed technical PDF reports** including security audits, API specifications, and module architectures.
- Programmed a multi-language repository scanner and AST parser using **Tree-sitter** alongside a **NetworkX** symbol, call, and import graph with delta file detection to re-index 100% of modified files without full-repo crawls.
- Configured a **hybrid RAG retrieval pipeline** combining semantic vector search (ChromaDB and Pinecone) with lexical search (BM25), merging results via **Reciprocal Rank Fusion (RRF)** for accurate code context retrieval.
- Built **6+ custom agent tools** (symbol lookups, AST outlines, caller/callee traversal, grep search, and token-trimmed scratchpads) validated by strict **Pydantic** schemas inside an interactive **Textual TUI** with Playwright and ReportLab PDF rendering.

</td>
</tr>
</table>

<table width="100%">
<tr>
<td valign="top" width="50%">

### 🛒 Project Nexus AI
**AI-Powered E-Commerce Marketplace**
<img src="https://img.shields.io/badge/Sep%202025-0ea5e9?style=flat-square" />
<sub>Django · DRF · PostgreSQL · Redis · LangChain · ReportLab · Cloudinary · PayU · Render</sub>

- Launched a full-stack e-commerce marketplace featuring custom email authentication, dynamic multi-variant product pricing, inventory tracking, and **Cloudinary CDN** asset management.
- Integrated the **PayU payment gateway** with SHA-512 transaction hashing and automated error recovery workflows to process customer checkouts securely.
- Formulated an automated codebase documentation pipeline using LangChain, ReportLab, Redis caching, and Python **ThreadPoolExecutor** multithreading to reduce PDF generation response times.

</td>
<td valign="top" width="50%">

### 💼 Business VEN
**Inventory & Financial Management System**
<img src="https://img.shields.io/badge/Oct%202025-0ea5e9?style=flat-square" />
<sub>Django · SQLite · Redis · HTML5 · CSS3 · Context Processors · PythonAnywhere</sub>

- Structured a normalized relational database schema with **composite indexing** and foreign key constraints to manage real-time stock tracking, order lifecycles, and financial dashboards.
- Accelerated page load speeds by integrating **Redis view caching**, custom Django context processors, and automated email notification triggers for order status updates.

</td>
</tr>
</table>

<br/>

## 🛠 Skills

<div align="center">
<img src="https://skillicons.dev/icons?i=py,cs,dotnet,django,js,html,css,redis,postgres,sqlite&perline=10&theme=dark" alt="Core stack" />
</div>

<br/>

| | |
|:--|:--|
| 🧑‍💻 **Languages** | Python, C# (.NET Core), SQL, JavaScript, HTML5, CSS3 |
| 🧩 **Backend & APIs** | .NET Core Web API, Django, Django REST Framework (DRF), RESTful APIs, Custom Middleware, JWT Token Versioning, Single Sign-In (SSO), Bloom Filters, Magic Bytes File Validation, iTextSharp, BouncyCastle (DSC Signing), Celery |
| 🗄 **Databases & Caching** | Microsoft SQL Server (Stored Procedures, Joins), PostgreSQL, SQLite, Django ORM, Redis Caching |
| 🤖 **AI, Agents & OCR** | LangGraph, LangChain, Autonomous CLI Agents, Hybrid RAG, ChromaDB, Pinecone, BM25, Reciprocal Rank Fusion (RRF), Tree-sitter (AST), NetworkX, Pydantic, RapidOCR, Playwright, ReportLab |
| 🎯 **Core Competencies** | Authentication Systems, Digital PDF Signatures (DSC), Dashboard Automation, Multithreading (ThreadPoolExecutor), Payment Gateways (PayU, Stripe), Data Structures & Algorithms (190+ LeetCode) |

<br/>

## 🎓 Education

<table width="100%">
<tr>
<td width="60%">

**Bachelor of Technology (B.Tech) in Computer Science Engineering**
BBDNIIT (Dr. A.P.J. Abdul Kalam Technical University), Lucknow, UP
<img src="https://img.shields.io/badge/Aug%202024%20%E2%80%93%20May%202028-0ea5e9?style=flat-square" />

</td>
<td width="40%">

**Academic Performance**
Class 12 (ISC): **90%** · Class 10 (ICSE): **91%**
Competitive Programming: **190+ LeetCode problems solved**

</td>
</tr>
</table>

<br/>
<img src="./footer.svg" width="100%" alt="footer" />
