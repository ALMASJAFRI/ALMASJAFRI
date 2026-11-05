<div align="center">

# Hi, I'm Almas Jafri 👋

### Backend & AI Systems Engineer · .NET Core · Python · LangGraph

Backend and full-stack developer with **7 months of professional experience** building secure .NET Core APIs, SQL Server stored procedures and Python automation, plus **3+ production Django and AI applications**. I care about authentication, performance and agent systems that actually ship.

<a href="https://github.com/ALMASJAFRI">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=2196F3&center=true&vCenter=true&width=600&lines=Backend+%26+Full-Stack+Developer;.NET+Core+%26+Python+Engineer;AI+%26+LangGraph+Agent+Builder;190%2B+LeetCode+Problems+Solved" alt="Typing SVG" />
</a>

<br />

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/almasjafri)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ALMASJAFRI)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:YOUR_EMAIL@EXAMPLE.COM)

</div>

---

## 📌 At a Glance

| | |
|---|---|
| 💼 **Experience** | 7 months · Backend Developer Intern @ Brainpan Innovation (Apr 2026 – Present) |
| 📍 **Location** | Lucknow, Uttar Pradesh, India |
| 🎓 **Education** | B.Tech, Computer Science Engineering (2024 – 2028) · BBDNIIT (AKTU) |
| 🧩 **Focus** | Scalable backends, secure auth, multi-agent AI, .NET/Python integrations |
| ⚡ **DSA** | 190+ LeetCode problems solved |

---

## 🛠 Tech Stack

**Languages**
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=c-sharp&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)

**Backend & APIs**
![.NET](https://img.shields.io/badge/.NET%20Core-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-A30000?style=flat-square&logo=django&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white)

**AI, Agents & RAG**
![LangGraph](https://img.shields.io/badge/LangGraph-FF4F00?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-4F46E5?style=flat-square)
![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=flat-square)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)

**Databases & Caching**
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logo=microsoft-sql-server&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

**Security & Identity:** `JWT Token Versioning` · `Single Sign-In (SSO)` · `Magic Bytes Validation` · `iTextSharp / Bouncy Castle (DSC)` · `OAuth`

**Also used:** `Tree-sitter` · `NetworkX` · `BM25 + RRF` · `Playwright` · `ReportLab` · `Textual` · `RapidOCR` · `Bloom Filters`

---

## 💼 Experience

### Backend Developer Intern — Brainpan Innovation
**Apr 2026 – Present · 7 months · Lucknow, UP, India**

| Area | What I built | Impact |
|---|---|---|
| 🔐 **Auth & SSO** | .NET Core authentication APIs with custom middleware and JWT token versioning | Strict single sign-in enforced across all active sessions |
| ⚡ **Performance** | In-memory **Bloom filter** loaded on server startup to track unique emails (0.01% false-positive rate) | Filters out 99.99% of invalid lookups before they reach the database |
| 🛡 **Upload security** | Binary file validation that inspects the first 11 magic bytes of each upload stream | Blocks 100% of spoofed file extensions before storage |
| 🏛 **GovTech** | Digital PDF signature API using iTextSharp and Bouncy Castle, driven by upstream DSC payloads | Cryptographically signs official government PDFs |
| 🗄 **Data & Reporting** | 10+ RESTful Admin APIs on SQL Server stored procedures; Python + RapidOCR background reporting workflows | Automated dashboard reporting end to end |

---

## 🧠 Featured Projects

### 💻 Docmaker & Docmaker-CLI — Autonomous Docs-as-a-Service Agent
A local CLI developer agent that scans a codebase and writes technical PDF reports.

- **Multi-agent design:** LangGraph orchestrator with sub-agents generating **7 report types** (security audits, architecture and more).
- **Smart repo scanning:** Multi-language scanner using **Tree-sitter** and a **NetworkX** graph, with delta detection so only modified files are re-indexed.
- **Hybrid RAG:** Semantic search (ChromaDB, Pinecone) combined with lexical **BM25**, merged via **Reciprocal Rank Fusion**.
- **Tooling & TUI:** 6+ custom agent tools validated by strict **Pydantic** schemas, inside an interactive **Textual** TUI with Playwright and ReportLab rendering.

`LangGraph` `Tree-sitter` `NetworkX` `ChromaDB` `Pinecone` `BM25` `Pydantic` `Textual`

### 🛒 Project Nexus AI — AI-Powered E-Commerce Marketplace
- Full-stack marketplace with custom authentication, dynamic multi-variant pricing and Cloudinary CDN media management.
- **PayU** integration using SHA-512 transaction hashing, with automated error recovery.
- Codebase documentation pipeline (LangChain, ReportLab, Redis, `ThreadPoolExecutor`) that cuts PDF generation response times through concurrency.

`Django` `Redis` `LangChain` `Cloudinary` `PayU`

### 📊 Business VEN — Inventory & Financial Management System
- Normalized relational schema with composite indexes and foreign-key constraints for real-time tracking and dashboards.
- Faster page loads through Redis view caching and custom Django context processors.

`Django` `PostgreSQL` `Redis`

## 🎓 Education

- **B.Tech, Computer Science Engineering** (2024 – 2028) — BBDNIIT (AKTU)
- **Class 12 (ISC):** 90% · **Class 10 (ICSE):** 91%

---

<p align="center">
  <em>⚡ Currently focused on scalable backend architectures, multi-agent AI systems, and high-performance .NET/Python integrations.</em>
</p>
