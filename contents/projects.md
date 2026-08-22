### Project Highlights

Welcome to my portfolio of projects where I harness advanced machine learning and artificial intelligence technologies to tackle complex real-world problems. Here's a glimpse into some of the innovative work I've been involved in.

#### Unified Learning with AI

*Aug 2025 - Feb 2026*

A structured tutoring platform built on professionally curated knowledge graphs and predefined learning paths, so that guidance is constrained by syllabus-aligned data, prerequisite mappings, and expert-defined pathways rather than free-form model output. Curated knowledge graphs encode concept relationships and prerequisites; an agentic tutor stays grounded in verified curriculum source material rather than open-ended chat; the platform is multilingual (English / Hindi / Marathi) and multi-board (SSC / CBSE / ICSE) across classes 5-10; and an expert-in-the-loop curation portal means humans curate the graph, not the model. Designed and built end to end. Currently deployed with 150 users.

[Visit unifiedlearning.world](https://www.unifiedlearning.world)

#### ClareAI — Designing AI that Cares

Full title: *Designing AI that Cares: Empathetic Conversational Agents as Virtual Companions to Address Loneliness*. Published at AMCIS 2026 (Americas Conference on Information Systems), SIGHCI track. Authors: Armin Abazari, Samir Chatterjee, Nayana Bose, Parzon Eyzadpur Faridani.

The research was designed and led by others; I built the entire system — taking a non-technical team's product vision through to a working, evaluated, published artefact. The architecture: **Hume AI** (multimodal affect recognition) → **Gemini Flash 2.5** (persona and therapeutic-strategy retrieval) → **GPT-4** (response generation) → **AWS DynamoDB** (rolling conversational memory) → **HeyGen** (embodied avatar with synchronised speech and expression).

Evaluation: N = 13, within-person pre/post with seven days of naturalistic use. Loneliness fell significantly at 7 days (t(12) = 2.54, *p* = .026, d_z = 0.70) but not immediately post-session (*p* = .198). Social presence M = 5.42, trust M = 5.64 — the null immediate-effect result is reported alongside the significant one. Funded by the Blais Challenge Grant, Claremont Graduate University.

[View Paper](https://aisel.aisnet.org/amcis2026/sig_hci/sig_hci/17/)

#### C-SCLC Prognosis and Survival Prediction

*May 2024 - present (validation & clinical translation phase)*

First author. SEER staging systems changed across the 2004–2020 window (AJCC 6th → 7th → SEER Combined → EOD 2018), so naive longitudinal modelling silently mixes incompatible labels. This study restricted to AJCC 6th (2004–2015) to hold label semantics constant. Dataset: 1,619 records, cleaned to 863. Built an ensemble of models with PyTorch, TensorFlow, and Scikit-learn; the best model, an SVM, achieved 81% recall on the high-risk (under 9 months survival) class, AUC 0.79. Research through to production, pair-programmed with Kaijie Yu, second author.

[View on GitHub](https://github.com/Parzon/C-SCLC-PrognosisML)

#### Quant Research Platform

*Apr 2026 - present*

An internal research platform covering a survivorship-bias-free, point-in-time universe of Indian equities reconstructed from seven historical NSE indices — roughly 745 symbols in the research pool, 251 in the live universe (NIFTY 100 + MIDCAP 150). Infrastructure: 31 GB of Hive-partitioned Parquet (23 GB minute bars), a DuckDB analytical store, a PostgreSQL OLTP sidecar, and Backblaze B2 cloud archival, plus a full Indian cost model (STT, brokerage, slippage, intraday-vs-delivery classification, per-financial-year tax computation with loss set-off, ex-date dividend crediting). A paper-trading engine runs 16 strategies on cron with reconciliation, corporate-action handling, delisting watch, kill switches, and Slack health alerts three times a day. Research reads a nightly read-only snapshot, deliberately isolated from the money path.

> Internal research platform. Not an investment product, not investment advice, and no client capital is involved.

#### Soundlence

*Jul 2026 - present*

AI platform design for a professional audio software company: multilingual semantic search and automated metadata organisation for large professional sound libraries. Engagement beginning 2026, covering end-to-end solution architecture.

---

#### Skills and Technologies

- **Programming Languages:** Python, SQL.
- **AI/ML:** LLM orchestration, Retrieval-Augmented Generation, agentic architectures, knowledge graphs, context engineering.
- **Data:** data pipelines, PostgreSQL, DuckDB.
- **Cloud:** AWS.
- **Areas of Expertise:**
  - Generative AI Development
  - Fine-Tuning and Training Large Language Models (LLMs)
  - Natural Language Processing
  - Data Mining and Knowledge Discovery
  - Machine Learning
  - Product & Project Management — roadmapping, scoping, delivery, and stakeholder management
