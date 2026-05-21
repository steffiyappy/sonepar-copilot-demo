"""
Sonepar — Industrial & Electrical Distribution
==============================================

Drop-in industry definition for the Zava Copilot Demo Hub
(repo: steffiyappy/zava-copilot-demo).

How to integrate:
1. Copy the `ind(...)` block below into one of the `ind_batchN.py` files
   (recommended: `ind_batch12.py`, which appears to be the latest batch).
2. Append the entry to the `INDUSTRIES_12` list (or whichever list the
   batch file exposes).
3. Re-run `gen_hub.py` to regenerate `data.js` and `hub.html`.
4. Commit and push — GitHub Pages will rebuild the hub automatically.

Notes:
- This entry follows the existing `ind()` signature defined in `util.py`:
    ind(id, sectorId, name, icon, color, accent, company, tagline,
        scenario, files, tools, ..., relevantDepts=None, storyboard=None,
        personas=None, geo='MY')
- All 30 use cases are surfaced as prompts in the `tools` argument so they
  appear inside the industry's prompt panel in the hub.
- A `storyboard` block defines the 3-act demo flow (M365 Copilot →
  Agent Builder → Copilot Studio) for the live 30–45 min demo.
- Personas reflect the five demo characters used in the standalone
  Sonepar demo site at https://<your-org>.github.io/sonepar-copilot-demo/
"""

import sys; sys.path.insert(0, '.')
from util import *  # noqa: F401,F403  -- ind, esc, etc.

# ─── INDUSTRIAL & ELECTRICAL DISTRIBUTION (SONEPAR) ──────────────────────
SONEPAR_INDUSTRY = ind(
    'industrial_electrical_distribution',     # id
    'distribution_wholesale',                  # sectorId  (new sector; reuse 'manufacturing' if hub doesn't have it)
    'Industrial & Electrical Distribution',    # name
    '⚡',                                       # icon
    '#005EB8',                                 # color  (Sonepar brand blue)
    '#0078D4',                                 # accent
    'Sonepar Malaysia (A Sonepar Company)',    # company
    'Aishah, Head of Operations, has 90 minutes to clear May month-end variances, 3 risky backorders, a customer quote, and a new Senior Inventory Planner hire.',  # tagline / scenario hook
    # ── scenario (long description) ──
    'Sonepar is the world\'s largest B2B distributor of electrical products, solutions and related services — €33.6B in 2025 revenue across 170 operating companies. Sonepar Malaysia (formerly KVC Industrial Supplies, now A Sonepar Company) serves 7,000+ industrial and construction customers across Malaysia from 6 warehouses and 20+ branches, stocking 50,000+ SKUs from ABB, Schneider, Siemens, Philips, Legrand, Rockwell, Eaton, Wago, Prysmian, Hager, Omron and 100+ other brands. Sonepar Group has invested €1B+ in digital transformation built on Microsoft Dynamics 365, Azure AI, and the Spark omnichannel platform; AI now spans order automation, inventory optimisation, dynamic pricing, and personalised customer journeys. The Malaysia entity has a 30 use-case AI portfolio worth RM 45M+ in estimated annual value across Finance, Procurement, Operations, Sales, Customer Service, Maintenance, HR and IT — and is ready to pilot.',
    # ── files (sample data referenced by the prompts) ──
    [
        {'name': 'inventory-sample.csv', 'kind': 'csv',
         'desc': '30 SKUs × 6 warehouses — stock, reorder points, lead times'},
        {'name': 'orders-sample.csv', 'kind': 'csv',
         'desc': '15 in-flight customer orders across 8 industrial customers'},
        {'name': 'purchase-orders.csv', 'kind': 'csv',
         'desc': '12 open POs to ABB Malaysia with contract / variance flags'},
        {'name': 'customer-tickets.csv', 'kind': 'csv',
         'desc': '10 unassigned customer service tickets across channels'},
        {'name': 'month-end-variance.md', 'kind': 'md',
         'desc': 'FY2026 May Trial Balance vs Budget — for variance analysis'},
        {'name': 'product-catalog.md', 'kind': 'md',
         'desc': '10-SKU catalog extract — grounding for product Q&A'},
        {'name': 'roi-summary.md', 'kind': 'md',
         'desc': 'RM 25–43M ROI across the 5 demo departments'},
    ],
    # ── tools / prompts (all 30 use cases) ──
    [
        # ── Finance ──
        {'dept': 'finance', 'tool': 'M365 Copilot (Excel)',
         'title': 'Month-End Variance Analysis',
         'prompt': 'Analyse the FY2026 May actuals vs budget in this workbook. Highlight the top 5 variances by absolute value, classify each as Favourable or Adverse, and propose a one-sentence root cause for the three largest adverse variances. Output as a Markdown table with columns: GL Account, Budget, Actual, Variance (RM), Variance %, F/A, Likely Driver.'},
        {'dept': 'finance', 'tool': 'M365 Copilot (Word)',
         'title': 'CFO Commentary',
         'prompt': 'Draft a 150-word executive commentary for the Sonepar APAC CFO summarising the month — lead with cash-flow impact and the most material adverse variance. Tone: confident, concise, board-ready.'},
        {'dept': 'finance', 'tool': 'Power BI Copilot',
         'title': '13-Week Cash Flow Forecast',
         'prompt': 'Forecast Sonepar Malaysia weekly cash position for the next 13 weeks using the AR aging, AP commitments, and historical payment patterns in this workbook. Flag any week where projected balance falls below RM 8M and recommend specific actions.'},
        {'dept': 'finance', 'tool': 'M365 Copilot',
         'title': 'AP Fraud / Anomaly Scan',
         'prompt': 'Scan the past 30 days of supplier payments for the top 20 risk patterns: duplicate invoices, round amounts, after-hours approvals, new bank accounts, payments above PO, same-day reverse+reissue. Output a ranked table with risk score 1–10 and rationale.'},
        {'dept': 'finance', 'tool': 'Dynamics 365 Finance + Azure ML',
         'title': 'Customer Credit Risk Scoring',
         'prompt': 'Score the top 100 customers by AR exposure using 24 months of payment history. For each: risk tier (Low/Medium/High), recommended credit limit, recommended payment terms, rationale. Flag tier changes in the last 90 days.'},
        # ── Procurement / Supply Chain ──
        {'dept': 'procurement', 'tool': 'M365 Copilot + Power BI',
         'title': 'Supplier Q1 Scorecard',
         'prompt': 'Generate a Q1 FY2026 supplier scorecard for the top 20 suppliers by spend. Score across price competitiveness, on-time delivery, quality (RMA rate), ESG rating, financial health. Rank, highlight any with a score drop >15% QoQ, and draft a 100-word negotiation brief for the bottom 3.'},
        {'dept': 'procurement', 'tool': 'Agent Builder',
         'title': 'Inventory Insight Agent',
         'prompt': 'Create an agent called "Sonepar Inventory Insight" grounded on inventory-sample.csv and the SharePoint product catalog. When asked about stockouts, show SKU, qty on hand, reorder point, lead time, nearest warehouse with stock. For slow movers (no sales in 90 days), recommend markdown / transfer / write-off. Never invent stock numbers.'},
        {'dept': 'procurement', 'tool': 'M365 Copilot',
         'title': 'Demand & Reorder Plan',
         'prompt': 'For the 30 SKUs in inventory-sample.csv, calculate projected stockout date if current velocity continues, vs supplier lead time. Flag any SKU where stockout < lead time as Critical. Suggest PO qty using 30-day forward cover + 1× lead-time safety stock.'},
        {'dept': 'procurement', 'tool': 'M365 Copilot (Word)',
         'title': 'Supplier Contract Review',
         'prompt': 'Review this ABB Malaysia supply contract. Extract: parties, effective date, term, auto-renewal, payment terms, price-change mechanism, liability cap, indemnification, exclusivity, force majeure, termination notice, ESG clauses. Flag deviations from the Sonepar Group Standard Terms. Draft a 5-point negotiation brief.'},
        {'dept': 'procurement', 'tool': 'Power BI Copilot',
         'title': 'Maverick Spend Detection',
         'prompt': 'Analyse the last 12 months of procurement spend. Identify the top 10 maverick spend categories (>RM 10,000 from non-contracted suppliers), estimate consolidation savings if redirected to preferred suppliers, rank by opportunity size.'},
        # ── Operations ──
        {'dept': 'operations', 'tool': 'Agent Builder',
         'title': 'Order Status Buddy',
         'prompt': 'Build an agent called "Order Status Buddy" for the Sonepar CS desk. Look up status from orders-sample.csv; return header, lines, status, ETA, tracking. Verify account number before sharing. Slip >2 working days → apologise + new ETA + offer CSR escalation. Greeting: "Hi! I\'m your Sonepar Order Status Buddy — what\'s your order or PO number?"'},
        {'dept': 'operations', 'tool': 'M365 Copilot',
         'title': 'Open-PO Risk Triage',
         'prompt': 'Review the 12 open POs to ABB Malaysia. Flag any with: (a) delivery date past today, (b) value above RM 250,000 without a contract reference, or (c) quantity variance >10% versus the originating sales order. Output: Markdown table with PO #, Issue, Risk Level, Suggested Action.'},
        {'dept': 'operations', 'tool': 'Azure Maps + M365 Copilot',
         'title': 'KL Delivery Route Optimisation',
         'prompt': 'Optimise tomorrow\'s KL-area delivery routes for 32 stops across 6 trucks. Constraints: 2-hour delivery windows, 3.5T payload limit, prioritise VIPs (Petronas, Tenaga, YTL) first. Output: per-truck route sequence with ETA per stop, total km vs baseline.'},
        {'dept': 'operations', 'tool': 'Power BI + Azure Digital Twins',
         'title': 'Warehouse Slotting Recommendation',
         'prompt': 'Using 90 days of pick data, identify top 50 SKUs by pick frequency in KL-Main. Recommend whether to move closer to packing (high frequency) or further (low). Estimate total travel-distance reduction (metres/day).'},
        {'dept': 'operations', 'tool': 'M365 Copilot',
         'title': '30-Day QC Defect Summary',
         'prompt': 'Generate a 30-day Quality Control summary across the 6 warehouses. List top defect categories, frequency, suppliers and SKUs involved, financial impact (replacement value + freight). Recommend which 3 SKUs need urgent supplier engagement.'},
        # ── Sales & Marketing ──
        {'dept': 'sales', 'tool': 'Dynamics 365 Sales Copilot',
         'title': 'Top-10 Opportunity Prioritisation',
         'prompt': 'Score my open opportunities (>RM 50k) on stage, days since last activity, customer industry, historical win rate, competitor presence. Rank top 10 by close probability for this quarter; draft a 1-sentence "next best action" for each.'},
        {'dept': 'sales', 'tool': 'Azure AI Recommendation',
         'title': 'Cross-Sell Recommendations — Petronas',
         'prompt': 'For customer ACC-001245 (Petronas Refinery Melaka), review the past 24 months of orders. Recommend 5 cross-sell products they have not purchased, with a 1-sentence rationale tied to their buying pattern. Estimate incremental annual revenue per recommendation.'},
        {'dept': 'sales', 'tool': 'Azure ML + Customer Insights',
         'title': 'Churn-Risk Customers',
         'prompt': 'List the top 25 customers showing churn signals in the past 90 days: declining order frequency, declining basket, increased complaints, payment delays. For each, suggest the most impactful retention play.'},
        {'dept': 'sales', 'tool': 'Customer Insights + Azure OpenAI',
         'title': 'Personalised Campaign Variants',
         'prompt': 'Draft 3 personalised email variants for an upcoming Schneider Electric MCB promotion: one for MRO buyers, one for construction, one for infrastructure. Each leads with the most relevant value proposition for the segment.'},
        # ── Customer Service ──
        {'dept': 'service', 'tool': 'Copilot Studio',
         'title': 'Sonepar Customer Service Agent (live build)',
         'prompt': 'Create a customer service agent for Sonepar Malaysia (a Sonepar Company) handling: (1) order tracking, (2) stock availability across 6 warehouses, (3) product spec Q&A grounded in the SharePoint product catalog, and (4) escalation to a human CSR via Teams. Always verify customer account number before sharing order details. Bilingual EN/BM. Never quote prices. Greeting: "Hi! I\'m Sonepar Malaysia\'s Customer Service Agent. How can I help today?"'},
        {'dept': 'service', 'tool': 'Dynamics 365 CS Copilot',
         'title': 'Ticket Triage & First-Response Drafts',
         'prompt': 'Review the 10 unassigned tickets in customer-tickets.csv. Classify each into the correct queue, set priority (P1/P2/P3) based on customer tier and sentiment, draft a 2-sentence first response.'},
        {'dept': 'service', 'tool': 'Azure AI Language',
         'title': '30-Day Voice of Customer Report',
         'prompt': 'Summarise the past 30 days of customer interactions (email, chat, survey) into a Voice of Customer report. Output: top 5 themes by mention volume + sentiment, top 3 emerging issues, 3 positive themes, 5 concrete improvement actions for leadership.'},
        {'dept': 'service', 'tool': 'Power Pages + Azure OpenAI',
         'title': 'Self-Service Portal Walkthrough',
         'prompt': '(Live demo) Show the Copilot Studio agent embedded in the Power Pages customer portal handling order lookup, datasheet retrieval, and stock checks for an authenticated customer.'},
        # ── Maintenance ──
        {'dept': 'maintenance', 'tool': 'Azure IoT + Azure ML',
         'title': '7-Day Predictive Maintenance Forecast',
         'prompt': 'Forecast equipment failures for the 24 forklifts across 6 warehouses for the next 7 days. List equipment ID, predicted failure type, confidence %, recommended action (inspect / replace / OK), estimated downtime cost if ignored.'},
        {'dept': 'maintenance', 'tool': 'Dynamics 365 Field Service',
         'title': 'Technician Schedule Optimisation',
         'prompt': 'Optimise tomorrow\'s schedule for 8 maintenance technicians across 22 work orders. Constraints: certification matching (LV vs MV), parts availability at branch, SLA windows, max 90 min travel. Output: per-technician assignment list with reasoning.'},
        {'dept': 'maintenance', 'tool': 'Azure ML + Microsoft Fabric',
         'title': 'Spare Parts 90-Day Forecast',
         'prompt': 'Forecast spare-parts consumption for the next 90 days across 6 warehouses based on equipment maintenance history and age profile. Highlight 5 parts at highest stockout risk and 5 currently overstocked.'},
        {'dept': 'maintenance', 'tool': 'Microsoft Sustainability Manager',
         'title': 'Q1 ESG / Energy Report',
         'prompt': 'Generate a Q1 FY2026 sustainability and energy report for Sonepar MY: total kWh by site, intensity per RM revenue, top 3 energy-saving actions, progress vs the group SBTi commitment. Format for the parent-company quarterly pack.'},
        # ── HR ──
        {'dept': 'hr', 'tool': 'M365 Copilot (Word)',
         'title': 'Senior Inventory Planner — JD',
         'prompt': 'Draft a job description for a "Senior Inventory Planner" at Sonepar Malaysia, reporting to the Head of Supply Chain. Responsibilities: SKU-level demand forecasting across 50,000+ products, Dynamics 365 Supply Chain, partnering with 6 warehouse managers. Include must-have / nice-to-have, plus what makes this role exciting at Sonepar (€33.6B group). Markdown for SharePoint posting.'},
        {'dept': 'hr', 'tool': 'M365 Copilot',
         'title': 'CV Screening Scorecard',
         'prompt': 'Compare this CV against the Senior Inventory Planner JD. Score 1–10 on each must-have, list 3 strengths, 2 gaps, recommend "Proceed / Phone screen / Reject" with one-line rationale.'},
        {'dept': 'hr', 'tool': 'Microsoft Viva Learning',
         'title': 'Personalised 12-Month Dev Plan',
         'prompt': 'Build a 12-month personalised learning plan for Aishah Rahman (Senior Buyer, 4 yrs, targeting Procurement Manager in 18 months). Include 3 technical courses (Dynamics 365 Supply Chain certs), 2 leadership modules (Viva Learning), 1 stretch project, quarterly check-in goals. Markdown table.'},
        # ── IT & Security ──
        {'dept': 'it', 'tool': 'Microsoft Copilot for Security',
         'title': '24-Hour Incident Briefing',
         'prompt': 'Review the past 24 hours of security alerts. Group related alerts into incidents, prioritise by impact and confidence, draft a 5-bullet executive briefing for the CISO. Highlight any alerts touching supplier financial data or executive accounts.'},
        {'dept': 'it', 'tool': 'Copilot Studio',
         'title': 'Sonepar IT Helper Agent',
         'prompt': 'Create an agent called "Sonepar IT Helper" for tier-1 IT requests: password reset, MFA reset, software install, VPN troubleshoot, printer setup, new-joiner onboarding checklist. Verify employee ID before any provisioning. Escalate any request involving production OT systems to the SOC.'},
    ],
    # ── extra metadata ──
    companyID='Sonepar Malaysia · A Sonepar Company',
    taglineID='Aishah, Head of Operations, has 90 minutes...',
    subsector='Electrical & Industrial Distribution',
    relevantDepts=['finance', 'procurement', 'operations', 'sales', 'service', 'maintenance', 'hr', 'it'],
    # ── 3-act storyboard for the 30-45 min live demo ──
    storyboard=[
        {'ex': 1, 'title': 'Act 1 — Microsoft 365 Copilot', 'minutes': 10, 'mode': 'show',
         'summary': 'Productivity wins: Finance variance, HR JD & screen, CS email triage, Supply Chain PO review.',
         'tasks': [
             {'n': '1.1', 'tool': 'Excel', 'verb': 'Variance', 'mode': 'show', 'label': 'Top 5 May variances'},
             {'n': '1.2', 'tool': 'Word', 'verb': 'Draft JD', 'mode': 'show', 'label': 'Senior Inventory Planner'},
             {'n': '1.3', 'tool': 'Outlook', 'verb': 'Triage', 'mode': 'show', 'label': 'Customer email'},
             {'n': '1.4', 'tool': 'M365 Copilot', 'verb': 'PO Review', 'mode': 'show', 'label': '12 open POs'},
         ]},
        {'ex': 2, 'title': 'Act 2 — Agent Builder', 'minutes': 10, 'mode': 'build',
         'summary': 'Build two declarative agents from a single prompt — Inventory Insight + Order Status Buddy.',
         'tasks': [
             {'n': '2.1', 'tool': 'Copilot Chat', 'verb': 'Create agent', 'mode': 'build', 'label': 'Inventory Insight'},
             {'n': '2.2', 'tool': 'Copilot Chat', 'verb': 'Create agent', 'mode': 'build', 'label': 'Order Status Buddy'},
         ]},
        {'ex': 3, 'title': 'Act 3 — Copilot Studio', 'minutes': 20, 'mode': 'build',
         'summary': 'Build the Sonepar Customer Service Agent live: topics, knowledge, action, channels.',
         'tasks': [
             {'n': '3.1', 'tool': 'Copilot Studio', 'verb': 'Create', 'mode': 'build', 'label': 'Agent from description'},
             {'n': '3.2', 'tool': 'Copilot Studio', 'verb': 'Add knowledge', 'mode': 'build', 'label': 'SharePoint catalog'},
             {'n': '3.3', 'tool': 'Copilot Studio', 'verb': 'Build topic', 'mode': 'build', 'label': 'Track my order'},
             {'n': '3.4', 'tool': 'Power Automate', 'verb': 'Build action', 'mode': 'build', 'label': 'LookupOrderStatus'},
             {'n': '3.5', 'tool': 'Copilot Studio', 'verb': 'Publish', 'mode': 'build', 'label': 'Teams + Web'},
         ]},
    ],
    # ── personas (5 demo characters) ──
    personas=[
        {'name': 'Aishah Rahman',  'role': 'Head of Operations · Sonepar MY',           'acct': 'aishah.rahman@sonepar.my',  'lic': 'Microsoft 365 Copilot',      'color': '#10B981'},
        {'name': 'Lim Wei Han',    'role': 'CFO · Sonepar MY',                          'acct': 'lim.wh@sonepar.my',         'lic': 'Microsoft 365 Copilot',      'color': '#0EA5E9'},
        {'name': 'Priya Devi',     'role': 'Head of HR · Sonepar MY',                   'acct': 'priya.devi@sonepar.my',     'lic': 'Microsoft 365 Copilot',      'color': '#6366F1'},
        {'name': 'Faisal Ibrahim', 'role': 'Customer Service Lead · Sonepar MY',        'acct': 'faisal.i@sonepar.my',       'lic': 'Microsoft 365 Copilot',      'color': '#8B5CF6'},
        {'name': 'Tan Mei Ling',   'role': 'Senior Buyer · Procurement · Sonepar MY',   'acct': 'tan.ml@sonepar.my',         'lic': 'Microsoft 365 Copilot',      'color': '#F59E0B'},
    ],
    geo='MY',
)

# Convenience: a list other batch files can import from.
INDUSTRIES_SONEPAR = [SONEPAR_INDUSTRY]


# ─── README INTEGRATION SNIPPET ──────────────────────────────────────────
# To add this entry to an existing batch file (e.g. ind_batch12.py):
#
#     from sonepar_industry import SONEPAR_INDUSTRY
#     INDUSTRIES_12.append(SONEPAR_INDUSTRY)
#
# Then run:
#     python gen_hub.py
# from the repo root to regenerate data.js + hub.html.
