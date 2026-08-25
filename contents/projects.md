#### Unified Learning with AI

*Aug 2025 – Feb 2026 · Education*

An AI tutor that can't make things up. Guidance is constrained by curated knowledge graphs, prerequisite mappings and syllabus-aligned pathways rather than free-form model output — experts define the graph, the model works inside it. Multilingual (English, Hindi, Marathi), multi-board (SSC, CBSE, ICSE), classes 5–10.

Designed and built end to end, alone. Deployed with 150 users; early results show a significant improvement in student outcomes, with a paper forthcoming.

[Visit unifiedlearning.world](https://www.unifiedlearning.world)

#### ClareAI — Designing AI that Cares

*May 2024 – Apr 2025 · Mental health*

An empathetic conversational agent for people experiencing loneliness, published at AMCIS 2026 (SIGHCI). The research was designed and led by others; **I built the entire system**, taking a non-technical team's vision through to a working, evaluated, published artefact.

Five services, one real-time loop: multimodal affect recognition → therapeutic-strategy retrieval → response generation → persistent conversational memory → an embodied avatar with synchronised speech and expression.

Loneliness fell significantly after seven days of use (*p* = .026, d<sub>z</sub> = 0.70) though not immediately post-session (*p* = .198) — both results reported. Social presence 5.42, trust 5.64. Funded by the Blais Challenge Grant, Claremont Graduate University.

Authors: Armin Abazari, Samir Chatterjee, Nayana Bose, Parzon Eyzadpur Faridani.

[View Paper](https://aisel.aisnet.org/amcis2026/sig_hci/sig_hci/17/)

#### C-SCLC Prognosis and Survival Prediction

*May 2024 – present · Oncology · First author*

Cancer staging standards changed four times across the 2004–2020 SEER window, so longitudinal models built on the raw data silently mix incompatible labels. Restricting to a single staging edition kept the label semantics constant — 1,619 records cleaned to 863. The best model, an SVM, reached **81% recall on the high-risk group** (under nine months' survival), AUC 0.79.

Research through to production, pair-programmed with Kaijie Yu. Now in clinical validation and translation.

[View on GitHub](https://github.com/Parzon/C-SCLC-PrognosisML)

#### Quant Research Platform

*Apr 2026 – present · Financial research infrastructure*

A survivorship-bias-free, point-in-time universe of Indian equities rebuilt from seven historical NSE indices — 745 symbols researched, 251 live. 31 GB of Hive-partitioned Parquet over a DuckDB analytical store and a PostgreSQL sidecar, with a full Indian cost and tax model down to per-financial-year loss set-off and ex-date dividend crediting.

A paper-trading engine runs 16 strategies on cron with reconciliation, corporate-action handling, kill switches and thrice-daily health alerts. Research reads a nightly read-only snapshot, deliberately isolated from the money path.

> Internal research platform. Not an investment product, not investment advice, and no client capital is involved.

#### Soundlence

*Jul 2026 – present · Professional audio*

End-to-end solution architecture for a professional audio software company: multilingual semantic search and automated metadata organisation across large sound libraries.

---

#### Skills

- **Product & delivery:** problem definition, scoping and roadmapping, solution architecture, technical project management, client and C-suite stakeholder work
- **AI/ML:** LLM orchestration, retrieval-augmented generation, agentic architectures, MCP, context engineering, knowledge graphs, NLP, fine-tuning
- **Data:** data engineering, pipelines, dimensional modelling, PostgreSQL, DuckDB
- **Languages & cloud:** Python, SQL, AWS
