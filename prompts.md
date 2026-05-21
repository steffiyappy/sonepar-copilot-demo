# Sonepar × Microsoft 365 Copilot — 30-min Demo Prompt Library

A focused 30-minute demo of **Microsoft 365 Copilot only** — Word, Excel, PowerPoint, Researcher, Analyst, **Copilot Cowork**. Pure M365 Copilot the team already has, plus the new autonomous AI-coworker layer (Frontier program, Claude-powered).

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

## ⏱ 21–25 min · Copilot Chat — Grounded Answers + Live Copilot Page

**Where:** Microsoft 365 Copilot Chat (work mode) → toggle "Work" + Web grounding · **Files in scope:** Outlook, Teams chats, SharePoint, [`sonepar-ops-workbook.xlsx`](files/sonepar-ops-workbook.xlsx), [`variance-memo.docx`](files/variance-memo.docx)

```
Search across my Outlook, Teams chats and SharePoint for everything in the last 14 days about: ABB price increases, the 3 ABB ACS580 VFD backorders, Petronas Melaka Refinery SO-44218, Top Glove SO-44219 and UMW Toyota SO-44226.

Then in one combined answer:
1. Summarise what the buyer and the customer have already said about each of the 3 backorders (with email dates and Teams message timestamps).
2. Flag any commitments my team has made — promised dates, prices, discounts.
3. Cross-reference with the Orders sheet of sonepar-ops-workbook.xlsx and tell me where the team's commitment does NOT match the system status.
4. Ground the ABB price discussion in public sources from the last 30 days (web).
5. Suggest 3 follow-up questions I should ask my procurement lead this afternoon.

When done, turn this whole answer into a new Copilot Page titled "Backorder situation 21-May" and share it to the #sonepar-ops-leads channel so Razif and Mei Ling can edit alongside me.
```

✅ **Outcome:** One grounded answer pulling email + Teams + SharePoint + workbook + public web → promoted to a **live Copilot Page** the team co-edits in real time. The "single pane of work knowledge" moment.

**Demo cue:** show the inline citations (📎 Outlook, 📎 Teams, 📎 SharePoint, 🌐 web) AND the "Create Page" button — this is how chat becomes shared collaboration.

---

## ⏱ 25–30 min · Copilot Cowork — The Autonomous AI Coworker

**Where:** Microsoft 365 Copilot → Cowork (Frontier program, Claude-powered) · **Files attached:** [`variance-memo.docx`](files/variance-memo.docx) · [`sonepar-ops-workbook.xlsx`](files/sonepar-ops-workbook.xlsx) · [`exec-brief-template.pptx`](files/exec-brief-template.pptx)

> **What's different:** unlike Copilot Chat where you give step-by-step prompts, Cowork takes a single **goal** and plans the workflow itself. The task dashboard streams each step (📋 *Reading workbook…* → 📋 *Drafting email…* → ⏸ *Awaiting your approval*). Sensitive actions (sending email, scheduling a meeting) pause for your approval.

```
Goal — get me ready for the MD's Monday review by 9am tomorrow.

Context: I am Aishah, Head of Operations at Sonepar Malaysia. The MD's Monday review is at 9am 22-May-2026. You have access to my variance-memo.docx, sonepar-ops-workbook.xlsx, exec-brief-template.pptx, Outlook, Teams, SharePoint and OneDrive.

Plan and execute the following — show me each step in the task dashboard, and pause for my approval before any external send:
1. Read the variance-memo.docx and the Orders + Variance_May2026 sheets in sonepar-ops-workbook.xlsx. Produce a 5-bullet "What the MD needs to know".
2. Identify the 3 ABB VFD backorders, look up the responsible buyer in Outlook, and prepare a draft email to ABB Helsinki requesting a Singapore IBC cross-ship — hold for my approval.
3. Build the MD board deck from the exec-brief-template.pptx using the variance numbers and the Researcher market brief in this chat. Save to SharePoint > Sonepar MY > Board.
4. Schedule a 30-min "Backorder war-room" in Teams for today 4pm with @Procurement, @Sales, @Aishah. Hold the invite for my approval.
5. Open a Loop checklist with the 5 follow-ups (FX cover, carrier renegotiation, credit tightening, June pull-forward, surcharge), assigned to the right owners.
6. Draft a Teams message to the MD that links to the deck and the Loop list, and includes the single RM exposure number. Hold for my approval.

Use the Frontier Claude model. Stop and ask me if any step needs a decision. When done, summarise what you did, what is queued, and what is waiting on me.
```

✅ **Outcome:** Task dashboard runs 6 steps live — deck saved to SharePoint, war-room invite drafted, Loop checklist created, 2 emails + 1 Teams message waiting on Aishah's approval. One goal → end-to-end Monday prep done, in 4 minutes of clock time.

**Demo cue:** point to the dashboard as it streams steps and to the ⏸ approval popups — this is the "AI coworker" moment, not chat.

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
