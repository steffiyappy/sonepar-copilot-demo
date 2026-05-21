# Sonepar Demo — Copy-Paste Prompt Library

All prompts below are ready to paste into Microsoft 365 Copilot, Agent Builder, or Copilot Studio during the live demo. Order follows the 30-45 min demo flow.

---

## ACT 1 — Microsoft 365 Copilot (10 min)

### 1.1 Finance — Month-End Variance Analysis (Copilot in Excel)
Open `files/month-end-variance.xlsx` (or the Markdown version) in Excel, then ask Copilot:

> Analyse the FY2026 May actuals vs budget in this workbook. Highlight the top 5 variances by absolute value, classify each as Favourable or Adverse, and propose a one-sentence root cause for the three largest adverse variances. Output as a markdown table with columns: GL Account, Budget, Actual, Variance (RM), Variance %, F/A, Likely Driver.

Follow-up:

> Now draft a 150-word executive commentary for the Sonepar APAC CFO summarising the month — lead with cash flow impact and the most material adverse variance. Tone: confident, concise, board-ready.

### 1.2 HR — Job Description & CV Screen (Copilot in Word + Chat)
In Copilot Chat (work mode):

> Draft a job description for a "Senior Inventory Planner" based at Sonepar Malaysia, reporting to the Head of Supply Chain. Responsibilities should include SKU-level demand forecasting across 50,000+ products, working with Dynamics 365 Supply Chain, and partnering with 6 warehouse managers. Include must-have skills, nice-to-have, and a section on what makes this role exciting at Sonepar (group is €33.6B, A Sonepar Company benefits). Format: Markdown ready for SharePoint posting.

Then upload a CV (any sample PDF) and ask:

> Compare this CV against the Senior Inventory Planner JD above. Score the candidate 1–10 on each must-have, list 3 strengths, 2 gaps, and recommend "Proceed / Phone screen / Reject" with one-line rationale.

### 1.3 Customer Service — Email Triage (Copilot in Outlook)
Open any customer email and ask:

> Summarise this email in 2 bullets, identify the customer's primary intent (order status / quote / complaint / technical / billing), classify urgency (Low/Medium/High), and draft a reply that confirms next steps within 4 working hours. Sign off as "Sonepar Customer Care Team".

### 1.4 Supply Chain — PO Review (Copilot in Word/PDF)
Open `files/purchase-orders.csv` or the PDF version and ask:

> Review these 12 open POs to supplier ABB Malaysia. Flag any with: (a) delivery date past today, (b) value above RM 250,000 without a contract reference, or (c) quantity variance >10% versus the originating sales order. Output as a markdown table with PO #, Issue, Risk Level, Suggested Action.

---

## ACT 2 — Agent Builder in Copilot Chat (10 min)

Agent Builder lets users create declarative agents from a single natural-language prompt. Use the prompts below verbatim in Copilot Chat → **Create agent** → **Describe your agent**.

### 2.1 Inventory Insight Agent (Supply Chain)
Prompt:

> Create an agent called **"Sonepar Inventory Insight"** that helps Sonepar buyers and branch managers answer questions about SKU stock levels, reorder points, and slow-moving inventory. The agent should ground answers in our product catalog (SharePoint site: Sonepar-Inventory) and the file `inventory-sample.csv`. When asked about stockouts, always show the SKU, current quantity on hand, reorder point, lead time in days, and the nearest warehouse with available stock. If asked about slow movers, define slow as "no sales in 90 days" and recommend whether to mark down, transfer, or write off. Tone: concise, data-first, no marketing fluff. Never invent stock numbers — if data is missing, say so and suggest the buyer check Dynamics 365 Supply Chain.

Suggested test questions to ask the agent live:
- "What's the on-hand qty for SKU ABB-XT2N-160?"
- "Show me all slow movers in the KL warehouse."
- "Which warehouse has the most stock of Schneider iC60N MCB?"

### 2.2 Order Status Buddy (Operations / Customer Service)
Prompt:

> Build an agent called **"Order Status Buddy"** for the Sonepar Customer Service desk. It looks up order status from `files/orders-sample.csv`, returns the order header, line items, current status (Confirmed / Picked / Despatched / Delivered / Backorder), expected delivery date, and the carrier tracking link. When the customer's promised date has slipped, the agent should apologise, give a new ETA, and offer to escalate to a CSR if the slip is more than 2 working days. The agent must never expose other customers' orders — always confirm the customer's account number before sharing details. Greeting: "Hi! I'm your Sonepar Order Status Buddy — what's your order or PO number?"

### 2.3 (Optional bonus) HR Policy Helper
Prompt:

> Create an agent called **"Sonepar HR Helper"** grounded only on the Sonepar Malaysia Employee Handbook (SharePoint: HR-Policies). It answers questions about leave, claims, code of conduct, and benefits. If a question is outside policy or involves a personal HR matter, the agent should reply "Please reach out to your HRBP — I can't advise on individual cases" and offer to book a Teams meeting with HR.

---

## ACT 3 — Microsoft Copilot Studio (15–25 min)

See `copilot-studio-guide.html` for the full clickable walkthrough. The core agent being built live is:

**Agent name:** Sonepar Customer Service Agent
**Description:** A 24/7 customer-facing agent that handles order tracking, stock availability, technical document Q&A, and intelligent escalation for Sonepar Malaysia's 7,000+ industrial customers.

### Generative orchestration instructions (paste into the agent's Instructions field)
> You are the Sonepar Customer Service Agent. You serve industrial and electrical customers of Sonepar Malaysia (a Sonepar Company). Your job is to (1) check order status, (2) check stock availability across 6 warehouses, (3) answer product-spec questions from the technical document library, and (4) escalate complex issues to a human CSR via Teams. Always verify the caller's customer account number before sharing order details. Be concise, professional, and bilingual EN/BM if the user writes in Malay. Never quote prices — direct pricing questions to the account manager. If you don't know, say so and offer to log a callback.

### Sample Topic triggers
1. **Trigger:** "Where is my order?" / "Track order" / "ETA"
   - **Action:** call `LookupOrderStatus` (HTTP/Power Automate to Dynamics 365)
2. **Trigger:** "Stock check" / "Is X in stock?" / "Available?"
   - **Action:** call `CheckInventory`
3. **Trigger:** "Spec sheet" / "Datasheet" / "Manual" / "How do I install"
   - **Action:** generative answer grounded in the SharePoint product-library knowledge source
4. **Trigger:** "Speak to a human" / "Talk to someone" / "Complaint"
   - **Action:** escalate via Teams to the on-duty CSR group

### Demo conversation script
- "Hi, where's my order SO-MY-2026-04221?"
- "Got it — what's your customer account number?"
- (user provides) → agent returns status, ETA, carrier link
- "Is the ABB XT2N 160 in stock at KL warehouse?"
- "Can you send me the datasheet?"
- "I want to speak to a person." → handover

---

## ROI Recap Prompt (Copilot in PowerPoint)
At the end of the demo:

> Generate a 3-slide closing summary for Sonepar Malaysia: Slide 1 — the demo scenario we just walked through; Slide 2 — quantified ROI across the 5 departments we covered (use the figures from `files/roi-summary.md`); Slide 3 — recommended 90-day next steps (M365 Copilot rollout to Finance + CS, Agent Builder pilot for Supply Chain, Copilot Studio production agent for Customer Service).
