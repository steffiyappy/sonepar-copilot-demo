# Sonepar × Microsoft Copilot Demo

A self-contained, demo-ready microsite for the Sonepar Malaysia AI Transformation pitch — covering all 30 use cases from Finance to IT, with a live 30–45 minute demo path from **Microsoft 365 Copilot → Agent Builder → Copilot Studio**.

> **Customer:** Sonepar Malaysia (A Sonepar Company)
> **Parent:** Sonepar Group · €33.6B revenue · 170 OpCos
> **Industry:** Industrial & Electrical Distribution
> **Audience:** Sonepar executive team (Ops, Finance, HR, CS, IT)
> **Format:** Live, single-presenter demo · 30–45 min

## 🚀 Quick start (local)

```powershell
# Just open the entry page in a browser:
Start-Process .\index.html

# Or serve over a tiny HTTP server (so the agent guides can load files):
python -m http.server 8000
# then browse to http://localhost:8000/
```

Password for the gated entry page: **`SoneparDemo2026`**

## 📁 What's in here

```
sonepar-demo/
├── index.html                   ← Password gate (SoneparDemo2026)
├── hub.html                     ← Main demo hub — 30 use cases by department
├── copilot-studio-guide.html    ← Step-by-step live build of the Customer Service Agent
├── agent-builder-guide.html     ← Single-prompt recipes for 3 declarative agents
├── prompts.md                   ← All M365 Copilot prompts (copy-paste during demo)
├── files/                       ← Realistic sample data referenced by every prompt
│   ├── inventory-sample.csv         (30 SKUs × 6 warehouses)
│   ├── orders-sample.csv            (15 in-flight customer orders)
│   ├── purchase-orders.csv          (12 open POs to ABB Malaysia)
│   ├── customer-tickets.csv         (10 unassigned CS tickets)
│   ├── month-end-variance.md        (FY2026 May Trial Balance vs Budget)
│   ├── product-catalog.md           (10-SKU catalog extract for Q&A grounding)
│   └── roi-summary.md               (RM 25–43M ROI across 5 demo depts)
├── zava-hub-integration/
│   └── sonepar_industry.py      ← Drop-in ind() block for the Zava Copilot Demo Hub
└── README.md                    ← (this file)
```

## 🎬 Demo flow (30–45 min)

| Time | Act | Tool | What happens |
|---|---|---|---|
| 0–3 min | Intro | — | Sonepar context, scenario (Aishah's 90-min morning), agenda |
| 3–13 min | **Act 1** | Microsoft 365 Copilot | Finance variance · HR JD + screen · CS email triage · Supply Chain PO review |
| 13–23 min | **Act 2** | Agent Builder (Copilot Chat) | Build "Inventory Insight" + "Order Status Buddy" from a single prompt |
| 23–40 min | **Act 3** | Microsoft Copilot Studio | Live build: Sonepar Customer Service Agent — topics, knowledge, action, Teams + web channels |
| 40–45 min | Close | — | ROI recap, 90-day next steps, Q&A |

## 💰 ROI footprint (full programme)

| Department | Use cases | Est. annual savings |
|---|---|---|
| Finance | 5 | RM 6.3 – 10.5 M |
| Procurement & Supply Chain | 4 | RM 8.5 – 14.5 M |
| Operations | 5 | RM 6.5 – 11.5 M |
| Sales & Marketing | 4 | RM 9.0 – 16.5 M |
| Customer Service | 4 | RM 3.1 – 5.5 M |
| Maintenance | 4 | RM 3.4 – 6.2 M |
| HR | 2 | RM 0.7 – 1.4 M |
| IT & Security | 2 | RM 1.4 – 3.8 M |
| **Total (30 use cases)** | **30** | **RM 38.9 – 69.9 M / year · headline RM 45M+** |

## 🔌 Zava Hub integration

The full Sonepar industry entry is in [`zava-hub-integration/sonepar_industry.py`](./zava-hub-integration/sonepar_industry.py). To add Sonepar to the Zava Copilot Demo Hub:

1. Copy `sonepar_industry.py` into the Zava hub repo root.
2. In one of the `ind_batchN.py` files (recommend `ind_batch12.py`), add:
   ```python
   from sonepar_industry import SONEPAR_INDUSTRY
   INDUSTRIES_12.append(SONEPAR_INDUSTRY)
   ```
3. Re-run `python gen_hub.py` to regenerate `data.js` + `hub.html`.
4. Commit & push — GitHub Pages will rebuild automatically.

The entry follows the existing `ind()` signature in `util.py`, includes a 3-act storyboard matching the live demo flow, all 30 use-case prompts, 5 personas, and 7 sample files.

## 🎨 Industry positioning

Sonepar fits a new industry in the Zava hub: **Industrial & Electrical Distribution** (sector: `distribution_wholesale`). It's distinct from existing Zava verticals (Banking, Oil & Gas, Healthcare, Manufacturing, Telco, Retail, GLC, Power & Utilities, Property) because it sits at the B2B distribution layer — supplying the customers of every other industry. If a sector match is required, `manufacturing` is the closest existing fit.

## 🛠 Built with

- Microsoft 365 Copilot
- Microsoft Copilot Studio
- Agent Builder (in Copilot Chat)
- Azure AI Document Intelligence
- Azure OpenAI Service
- Azure Machine Learning
- Dynamics 365 (Finance, Supply Chain, Sales, Customer Service, Field Service)
- Microsoft Fabric
- Power Platform (Power Automate, Power BI, Power Pages)

## 📞 Contact

Prepared by **Microsoft** for **Sonepar Malaysia** · Confidential
