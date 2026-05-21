# Sonepar × Microsoft 365 Copilot — 30-min Demo Prompt Library

A focused 30-minute demo of **Microsoft 365 Copilot only** — Word, Excel, PowerPoint, Researcher, Analyst, Copilot Chat. No Agent Builder, no Copilot Studio, no Azure/D365/Power Platform. Pure M365 Copilot the team already has.

**Demo persona:** Aishah, Head of Operations at Sonepar Malaysia. She has 30 minutes before the MD's Monday review.

---

## ⏱ 0–4 min · Word Copilot — May Variance Memo

**File to open:** blank Word document (output: [`files/variance-memo.docx`](files/variance-memo.docx))

```
Draft a one-page month-end variance memo for the MD of Sonepar Malaysia titled "May 2026 Variance Memo". Use these closed numbers — Revenue actual RM 44.86M vs budget RM 43.30M (−3.6%), Industrial sales −RM 680k (3 projects slipped to June), Commercial sales +RM 645k (datacenter & semicon strong), Inventory purchases over budget by RM 1.18M from FX + ABB 4.2% price increase, last-mile logistics +RM 190k (20% over) from fuel and driver shortage, bad debt RM 190k from Tan Brothers default. Structure: Executive Summary (3 sentences), Key Variances (bullets with RM impact and driver), Recommended Actions (5 specific bullets — FX cover, carrier renegotiation, credit tightening, June pipeline pull-forward, surcharge), Appendix on the 3 ABB VFD backorders. Tone: factual, board-ready, max 350 words.
```

✅ **Outcome:** memo with sections, table, and 5 crisp recommendations — ready to share to Teams.

---

## ⏱ 4–9 min · Excel Copilot — Ops Workbook Analysis

**File to open:** [`files/sonepar-ops-workbook.xlsx`](files/sonepar-ops-workbook.xlsx) (Inventory · Orders · Variance_May2026 · ROI_Summary)

```
I have an Excel workbook with sheets Inventory, Orders, Variance_May2026 and ROI_Summary. Please do all of the following:
1. On Inventory, add a column "DaysOfCover" = OnHand / (estimated average daily demand of 4). Highlight any row where OnHand=0 in red and OnHand<Reorder in amber.
2. List every SKU where OnHand < Reorder AND LeadTime_Days > 30 — these are my critical exposures.
3. On Orders, summarize total RM at risk by Status (BACKORDER, RISK, ON-TIME) and by Sector. Insert a clustered bar chart of "Risk value by Sector".
4. Cross-check: for every BACKORDER or RISK order, does the SKU in the corresponding warehouse have OnHand >= Qty? Output a table "Order, Warehouse, SKU, Qty, OnHand, Shortfall".
5. On Variance_May2026, calculate which 3 line items contribute most to the −RM 1.56M total and what % of the gap each represents.
Give me the answers in chat AND apply formulas/charts to the sheet.
```

✅ **Outcome:** DaysOfCover formula, conditional formatting, sector-risk chart, Shortfall table.

---

## ⏱ 9–15 min · Analyst Agent — Python-Deep Risk Analysis

**Where:** Copilot Chat → @Analyst · **Attach:** [`files/sonepar-ops-workbook.xlsx`](files/sonepar-ops-workbook.xlsx)

```
@Analyst — using the attached sonepar-ops-workbook.xlsx, run a full risk analysis in Python:
(a) Compute SKU-level inventory cover assuming demand = average daily order quantity for that SKU over the last 15 orders. For SKUs with 0 historical orders, use Reorder/30 as a proxy.
(b) Build a "Risk Score" 0–100 for every order = 40×(1 if Status=BACKORDER else 0.5 if RISK else 0) + 30×(1 − OnHand/Qty clipped 0–1) + 30×(LeadTime_Days/60). Output the top 10 riskiest orders ranked.
(c) Cluster customers into 3 groups (kmeans on Value_RM and lateness) and label them Strategic / Standard / At-Risk.
(d) Plot: (i) horizontal bar chart of Risk Score for top 10 orders, (ii) scatter of OnHand vs Reorder per SKU coloured by Brand.
(e) Write a 5-bullet executive summary of the findings — what to escalate to ABB today, which customers to call, and the RM exposure number.
Show me the code, the charts, and the summary.
```

✅ **Outcome:** Python notebook output, 2 charts, ranked risk list, single RM exposure number for the MD.

---

## ⏱ 15–20 min · Researcher Agent — Market Brief

**Where:** Copilot Chat → @Researcher

```
@Researcher — produce a 600-word market brief for the MD of Sonepar Malaysia, dated today (May 2026). Cover, with citations:
1. ABB AG 2026 H1 price actions on low-voltage products globally and any announced surcharges affecting APAC distributors.
2. Malaysia electrical equipment demand outlook for 2026 H2 — datacenter pipeline (TM, YTL, Bridge DC, Princeton Digital), semicon expansions in Penang, EV charging build-out, and impact on MV/LV switchgear and VFD demand.
3. FX outlook: USD/MYR and EUR/MYR consensus for next 90 days, with 3 broker views.
4. Competitor moves: Rexel, WESCO, Sonepar group itself — any 2026 Malaysia announcements (DCs, partnerships, acquisitions).
5. One contrarian insight — what is the market NOT pricing in for an MY electrical distributor.
Format: executive summary (3 bullets), then 5 numbered sections, then a "What this means for Sonepar MY" call-out box. Use only public, citeable sources from the last 90 days.
```

✅ **Outcome:** Fully cited 600-word brief with links — pasted into the board appendix.

---

## ⏱ 20–25 min · PowerPoint Copilot — MD Board Deck

**Files:** [`files/variance-memo.docx`](files/variance-memo.docx) + [`files/exec-brief-template.pptx`](files/exec-brief-template.pptx)

```
Create a 6-slide executive presentation for the MD of Sonepar Malaysia titled "May 2026 Board Update — Variance, Risk, and the Path to RM 45M".
Source content from the attached variance-memo.docx and the Researcher market brief in this chat.
Slide structure:
1. Title — "Sonepar Malaysia · May 2026 Board Update", date 21 May 2026, Sonepar blue (#005EB8) background.
2. May closed — RM 44.86M actual vs RM 43.30M budget, the 3 main drivers (FX+ABB, last-mile, bad debt), and the upside (Commercial +10.4%).
3. The 3 ABB VFD backorders — customer names, RM at risk, mitigation (cross-ship from Singapore IBC).
4. Market context — 3 bullets from Researcher: ABB price action, MY datacenter demand, FX outlook.
5. Recommended actions — 5 bullets (FX cover, carrier renegotiation, credit tightening, June pull-forward, surcharge).
6. The RM 45M opportunity — Copilot transformation across Finance, Supply Chain, Ops, Sales, CS, HR/IT.
Apply the Sonepar brand: dark navy (#0F1C3F) + Sonepar blue (#005EB8) + accent red (#C8102E). Use clean sans-serif (Inter or Calibri). Include speaker notes — 2–3 sentences per slide.
```

✅ **Outcome:** Branded 6-slide deck with speaker notes — Aishah skims, accepts, sends to Teams.

---

## ⏱ 25–30 min · Copilot Chat + Coworker (Teams Page)

**Where:** Microsoft Teams → New Copilot Page

```
Open a new Copilot Pages page in Teams titled "Sonepar — Monday MD Review Prep". Pull in: the variance-memo.docx, the sonepar-ops-workbook.xlsx Order risk analysis, the Researcher market brief in this chat, and the exec-brief-template.pptx outline.
Then act as our team coworker and:
1. Produce a single "What the MD needs to know" 5-bullet summary at the top of the page.
2. Generate a Loop checklist of follow-ups assigned to: @Aishah (decisions), @Procurement (ABB cross-ship), @Sales (TNB quote), @Finance (FX cover), @HR (Senior Planner JD).
3. Draft a Teams message to the MD that links to this page and includes the RM exposure number and the 3 decisions we need.
4. When anyone @-mentions you on this page later, reference the same documents.
Keep me on this page — I will share it to the whole leadership channel.
```

✅ **Outcome:** Loop checklist live in Teams · MD Teams message drafted · single source of truth for the whole leadership channel.

---

## 📂 Demo Files

| File | Purpose |
|---|---|
| `files/sonepar-ops-workbook.xlsx` | Inventory · Orders · Variance · ROI (4 sheets, charts, conditional formatting) |
| `files/variance-memo.docx` | Sample May 2026 variance memo |
| `files/exec-brief-template.pptx` | 4-slide brand template — Title, Why now, Agenda, Outcome |
| `files/customer-rfq.docx` | TNB Bangsar substation RFQ (5 lines) |
| `files/inventory-sample.csv` · `orders-sample.csv` · `purchase-orders.csv` · `customer-tickets.csv` | Raw CSV data |
| `files/product-catalog.md` · `month-end-variance.md` · `roi-summary.md` | Reference content |
