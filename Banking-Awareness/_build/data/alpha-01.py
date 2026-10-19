# Saarthi Alpha · Class 1 — from the class PDF (document.pdf, 24 slides).
# Item keys: h (heading), hi (Hindi term), tag ('bank'/'hot'), pics [(img name, caption)],
#   facts [from the PDF], table (headers, rows), add [added for the exam], trap.
CLASS = 1
TITLE = 'Financial Inclusion, BC, Assets & Liability'
FULL = 'Introduction of Batch, Financial Inclusion, Business Correspondent (BC), Definition of Assets and Liability'
NOTE = 'The BSBD Account part of this class continues in Class 2’s PDF, so it is covered there.'

S = [
 ('General Awareness & the 2026 bank exams', 'The opening slides: what GA covers, which exams it is for, the 2026 calendar and the GA pattern of each exam.', [
  dict(h='What “General Awareness (GA)” covers', facts=[
     'GA has three parts: ' + k('Current Affairs') + ', ' + k('Banking / Financial Awareness') + ' and ' + k('Static GK') + '.',
     'This batch (Saarthi) covers the <b>Banking / Financial Awareness</b> part.',
  ]),
  dict(h='Target 2026 – Bank Exams', facts=[
     'Officer & clerk exams: <b>SBI PO, SBI Clerk, RRB PO, RRB Clerk, IBPS PO, IBPS Clerk, LIC / Insurance, RBI Assistant, RBI Grade B</b>.',
     'Regulators & development banks: <b>NABARD, SEBI, SIDBI, NaBFID, EXIM Bank, NHB</b>, plus <b>SBI Apprentice</b>.',
  ], add=['NaBFID = National Bank for Financing Infrastructure and Development (set up under the NaBFID Act, 2021). These institutions are taught in Class 4 (AIFIs).']),
  dict(h='Tentative calendar of Online CRP for PSBs & RRBs (2026-27)', tag='hot', pics=[('c1-crp-calendar', 'CRP calendar slide')], facts=[
     '<b>PSBs</b> – CRP PO/MT-XVI, CRP SPL-XVI & CRP CSA-XVI. <b>RRBs</b> – CRP RRBs-XV (Officers Scale I, II & III) and CRP RRBs-XV (Office Assistants).',
  ], table=(['Exam', 'Preliminary', 'Main / Single'], [
     ['PO / Management Trainee (PSB)', '22 & 23 Aug 2026', k('4 Oct 2026')],
     ['Specialist Officer – SPL (PSB)', '29 Aug 2026', '1 Nov 2026'],
     ['Customer Service Associate – CSA (PSB clerk)', '10 & 11 Oct 2026', k('27 Dec 2026')],
     ['RRB Officer Scale I (PO)', '21 & 22 Nov 2026', k('20 Dec 2026')],
     ['RRB Officer Scale II & III', 'NA', '20 Dec 2026 (single exam)'],
     ['RRB Office Assistant (clerk)', '6, 12 & 13 Dec 2026', k('30 Jan 2027')],
  ])),
  dict(h='Mains dates and the current-affairs window', tag='hot', facts=[
     '<b>IBPS PO</b> Mains – 4 October 2026 → current affairs from ' + k('March 2026') + '.',
     '<b>RRB PO</b> Mains – 20 December 2026 → current affairs from ' + k('June 2026') + '.',
     '<b>IBPS Clerk</b> Mains – 27 December 2026 → current affairs from ' + k('June 2026') + '.',
     '<b>RRB Clerk</b> Mains – 30 January 2027 → current affairs from ' + k('July 2026') + '.',
     'Rule of thumb from the slide: prepare ' + k('7 to 8 months') + ' of current affairs.',
  ]),
  dict(h='GA section pattern in each exam', table=(['Exam', 'Questions', 'Marks', 'Time'], [
     ['SBI PO', '60', '60', '45 min'],
     ['SBI Clerk', '50', '50', '35 min'],
     ['IBPS PO', '35', k('50'), '25 min'],
     ['IBPS Clerk', '40', '50', '20 min'],
     ['RRB PO', '40', '40', k('15 min')],
     ['RRB Clerk', '40', '40', '15 min'],
  ]), trap='In <b>IBPS PO</b> and <b>IBPS Clerk</b> the marks (50) are <b>more</b> than the number of questions (35 / 40). In SBI and RRB exams questions = marks.'),
  dict(h='Saarthi Batch 2026 = Saarthi Alpha + Saarthi Beta', facts=[
     '<b>Saarthi Alpha</b> (21 Jan – 8 Apr 2026, 26 classes): banking & financial concepts – banking system, RBI, NABARD & PSL, monetary policy, inflation, money & capital market, foreign trade, budget, NPA, Basel, PCA, national income.',
     '<b>Saarthi Beta</b> (20 Apr – 10 Jun 2026, 23 classes): RBI schemes & indices, banking terminology, NPCI products and government schemes.',
     'All classes run <b>10:00 – 11:30 AM</b>. The full class-by-class plan is on the <a href="index.html">Alpha overview</a> and the <a href="../Beta/index.html">Beta overview</a>.',
  ]),
 ]),
 ('Financial Inclusion', 'The first “Important Term” of the batch.', [
  dict(h='Financial Inclusion', hi='वित्तीय समावेशन', tag='bank', pics=[('c1-fi-cartoon', 'Bridge to the bank – financial inclusion')], facts=[
     'Financial inclusion is the effort to make financial products and services ' + k('available and affordable') + ' to ' + k('all individuals and businesses') + '.',
  ], add=[
     'Formal definition (Rangarajan Committee, 2008): ensuring access to financial services and timely, adequate credit for vulnerable groups such as weaker sections and low-income groups, at an affordable cost.',
     'Flagship scheme: <b>PMJDY</b> (launched 28 August 2014) – one basic bank account for every household. Taught in Beta Class 9.',
     'RBI measures it with the <b>Financial Inclusion Index (FI-Index)</b>, scored 0–100 on three parts: Access 35%, Usage 45%, Quality 20%. Taught in Beta Class 1.',
  ]),
  dict(h='Unserved vs Served – who financial inclusion is for', pics=[('c1-unserved-served', 'Unserved vs Served slide')], table=(['Unserved (excluded)', 'Served (included)'], [
     ['Have ' + k('no basic bank account'), 'Have a ' + k('transaction account')],
     ['Have no (or restricted) access to financial services', 'Use a broad range of financial services'],
     ['Rely on a ' + k('cash economy'), 'Pay and receive digitally (the slide shows a farmer paying with a card machine)'],
  ])),
 ]),
 ('Business Correspondents (BC)', 'The second “Important Term”: how banks reach villages that have no branch.', [
  dict(h='Business Correspondents', hi='व्यवसाय संवाददाता', tag='bank', pics=[('c1-bc-agents', 'A BC serving villagers'), ('c1-bc-farmer', 'BC agent with a customer (slide 18)')], facts=[
     'Business Correspondents are ' + k('retail agents') + ' engaged by banks for providing banking services at locations ' + k('other than a bank branch / ATM') + '.',
     'BCs let a bank ' + k('expand its outreach') + ' and offer a ' + k('limited range') + ' of banking services at ' + k('low cost') + '.',
     'Why: setting up a <b>brick-and-mortar branch</b> may not be viable in all cases.',
  ], add=[
     'RBI allowed banks to use the BC (and Business Facilitator) model in <b>January 2006</b>.',
     'BCs are popularly called <b>Bank Mitra</b>. They work with a hand-held device or micro-ATM, often using Aadhaar-based payments (AePS).',
     'Typical BC services: opening accounts, small deposits and withdrawals, remittances, balance enquiry, and collecting loan documents.',
  ], trap='<b>BC vs BF:</b> a Business <b>Correspondent</b> can do cash transactions on behalf of the bank. A Business <b>Facilitator</b> only refers or helps customers (spreading awareness, collecting applications) and does not handle cash.'),
  dict(h='Branch vs BC – the picture on slide 17', pics=[('c1-old-branch', 'Brick-and-mortar branch'), ('c1-digital-branch', 'Branch on a phone')], facts=[
     'Left picture: the old <b>brick-and-mortar branch</b>, costly to open in every village.',
     'Right picture: banking reaching people through agents and phones, which is the BC idea.',
  ]),
 ]),
 ('Assets and Liability', 'Two accounting words you need before the banking-system classes.', [
  dict(h="What is an 'Asset'?", hi='संपत्ति / परिसंपत्ति', pics=[('c1-asset-icon', 'Asset'), ('c1-asset-house', 'A house is an asset')], facts=[
     'Assets are ' + k('things you own that you can sell for money') + '.',
     'In accounting, an asset is ' + k('any resource that a business owns or controls') + '.',
     "It's anything that could be sold for money.",
  ]),
  dict(h="What is 'Liability'?", hi='देनदारी / दायित्व', pics=[('c1-liability-icon', 'Liability – a burden you carry'), ('c1-liability-dash', 'Liability')], facts=[
     'A liability is an ' + k('obligation to pay money') + ' to other people or businesses ' + k('in the future') + '.',
     'Liability usually means you are responsible for something. It can also mean you ' + k('owe someone money or services') + '.',
  ], add=[
     'Balance-sheet rule: <b>Assets = Liabilities + Owner’s equity (capital)</b>.',
  ], trap='Think from the <b>bank’s</b> side: your <b>deposit</b> is money the bank owes you, so it is the bank’s <b>liability</b>. The <b>loan</b> the bank gives you will be repaid to it, so it is the bank’s <b>asset</b>. Exams love this reversal.'),
 ]),
]

FLASH = [
 ('Financial Inclusion', 'Making financial products and services available and affordable to all individuals and businesses.'),
 ('Business Correspondent', 'A retail agent engaged by a bank to give banking services at places other than a branch / ATM.'),
 ('Why BCs?', 'Wider outreach and a limited range of services at low cost, where a brick-and-mortar branch is not viable.'),
 ('Asset', 'A thing you own that can be sold for money; any resource a business owns or controls.'),
 ('Liability', 'An obligation to pay money (or give services) to others in the future.'),
 ('Unserved', 'No basic bank account, little or no access to financial services, relies on cash.'),
]

QUIZ = [
 ('Name the three parts of General Awareness.', 'Current Affairs, Banking / Financial Awareness and Static GK.'),
 ('Define financial inclusion.', 'The effort to make financial products and services available and affordable to all individuals and businesses.'),
 ('What is a Business Correspondent?', 'A retail agent engaged by a bank to provide banking services at locations other than a bank branch or ATM.'),
 ('Why do banks use BCs instead of opening branches everywhere?', 'BCs expand outreach and give limited services at low cost; a brick-and-mortar branch may not be viable everywhere.'),
 ('Which of these can do cash transactions for a bank – Business Correspondent or Business Facilitator?', 'Business Correspondent. A Business Facilitator only refers / assists customers.'),
 ('For a bank, is a customer’s deposit an asset or a liability?', 'A liability (the bank owes it back to the customer).'),
 ('For a bank, is a loan given to a customer an asset or a liability?', 'An asset.'),
 ('What is an asset in accounting?', 'Any resource that a business owns or controls; anything that could be sold for money.'),
 ('IBPS PO Mains 2026 is on which date, and current affairs from which month?', '4 October 2026; current affairs from March 2026.'),
 ('RRB Clerk (Office Assistant) Mains date?', '30 January 2027 (current affairs from July 2026).'),
 ('How many questions and marks does the GA section of IBPS PO Mains carry?', '35 questions for 50 marks in 25 minutes.'),
 ('How many GA questions are there in SBI PO Mains, and in how much time?', '60 questions, 60 marks, 45 minutes.'),
 ('In which year did RBI allow banks to use Business Correspondents?', 'January 2006.'),
 ('Name two signs that a person is “unserved” financially.', 'Any two of: no basic bank account, no or restricted access to financial services, reliance on a cash economy.'),
]

RAPID = [
 'GA = Current Affairs + Banking/Financial Awareness + Static GK.',
 'Financial inclusion = financial services <b>available + affordable</b> to all.',
 'BC = retail agent of a bank, works <b>outside branch/ATM</b>; low-cost outreach; allowed by RBI in 2006; also called Bank Mitra.',
 'BC handles cash; BF (facilitator) does not.',
 'Asset = owned & sellable; Liability = obligation to pay in future.',
 'For a bank: deposits = liability, loans = asset.',
 'Mains 2026: IBPS PO 4 Oct · RRB PO 20 Dec · IBPS Clerk 27 Dec · RRB Clerk 30 Jan 2027.',
 'GA pattern: SBI PO 60Q/45 min · SBI Clerk 50Q/35 min · IBPS PO 35Q=50 marks/25 min · IBPS Clerk 40Q=50 marks/20 min · RRB PO & Clerk 40Q/15 min.',
]
