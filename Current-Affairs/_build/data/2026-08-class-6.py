# August 2026 · Class 6 — source: Class_06_August_2026_Monthly_Current_Affairs_by_Ashish_Gautam_Sir.pdf
# News content kept as in the PDF (English half, pages 1-4); Static GK boxes and exam traps added on top.
# From outside the English text: RRB weaker-section credit (₹3.49 lakh crore, p5) and Tata Steel/NYK 74:26 (p6)
# are English lines inside the Hindi half; the TReDS timeline (2017 / Nov 2018 / Nov 2024 / 30 June 2026) is an image on p4.
# Pictures come from the PDF itself (IMG values 'pdf:…', see pdf_images.py).
# Each section: (title, intro, [items]); item = (headline, tag, [facts], gk, trap). k('x') marks a key fact.
S = []

S.append(('Banking, Finance &amp; Payments', None, [
    ('YES Bank Launches YES Essence Credit Card', 'bank', [
        f'{k("YES Bank")} has launched the {k("YES Essence Credit Card")}.',
        f'It is a {k("women-focused")} credit card that combines spending rewards with {k("health and lifestyle")} benefits.'],
        f'YES Bank — Founded {k("2004")} · HQ {k("Mumbai")}',
        None),
    ('IDFC FIRST Bank Raises $500 Million Through Maiden International Bond Issue', 'bank', [
        f'{k("IDFC FIRST Bank")} raised {k("$500 million")} through its {k("maiden three-year fixed-rate senior notes")}, due in {k("2029")}.',
        f'The notes were issued through the bank’s {k("IFSC Banking Unit at GIFT City")} and carry a fixed coupon rate of {k("5.625%")}.',
        f'The bonds were placed with investors outside the United States under {k("Regulation S")}.',
        f'This is the bank’s {k("first international bond issuance")}, marking its entry into the global debt capital markets.',
        f'The bank also received a {k("‘BBB-’")} long-term issuer credit rating with {k("Stable Outlook")} from {k("S&amp;P Global Ratings")}.'],
        f'IDFC FIRST Bank — Formed {k("December 2018")} by the merger of {k("IDFC Bank")} and {k("Capital First")} · HQ {k("Mumbai")}',
        'Compare with Class 5: <b>SBI</b> raised $500 mn via its <b>London</b> branch (5 yr, 5.25%); <b>IDFC FIRST</b> raised $500 mn via <b>GIFT City IBU</b> (3 yr, <b>5.625%</b>). Both are Reg S.'),
    ('Regional Rural Banks’ Loans Rise 10.3% to ₹5.78 Lakh Crore in FY 2025-26', 'bank', [
        f'{k("Regional Rural Banks (RRBs)")} recorded gross loans outstanding growth of {k("10.3%")} in {k("FY 2025-26")}.',
        f'Gross loans rose from {k("₹5.24 lakh crore")} (FY 2024-25) to {k("₹5.78 lakh crore")} (FY 2025-26).',
        f'RBI prescribes an overall {k("Priority Sector Lending (PSL)")} target of {k("75% of ANBC")} (Adjusted Net Bank Credit) for RRBs; RRBs achieved an average of {k("91.7%")} of ANBC.',
        f'Credit to agriculture and allied activities: {k("₹3.78 lakh crore")}, i.e. {k("77%")} of total PSL. Farm credit was nearly {k("98%")} of agricultural lending.',
        f'RRB credit to the {k("MSME")} sector reached {k("₹66,978 crore")} ({k("13.6%")} of total PSL).',
        f'RRBs provided {k("₹3.49 lakh crore")} of credit to {k("weaker sections")} in FY 2025-26.'],
        f'RRBs — Est. {k("2 October 1975")} (RRB Act {k("1976")}) on the Narasimham Working Group’s advice · First RRB {k("Prathama Bank")} (Moradabad, UP) · Ownership Centre {k("50%")} : Sponsor bank {k("35%")} : State {k("15%")} · {k("28")} RRBs after “One State, One RRB” (1 May 2025)',
        'PSL target: <b>75%</b> of ANBC for <b>RRBs</b> (and Small Finance Banks), but <b>40%</b> for ordinary commercial banks.'),
    ('RBI Imposes ₹59.20 Lakh Penalty on IndusInd Bank', 'bank', [
        f'{k("RBI")} imposed a monetary penalty of {k("₹59.20 lakh")} on {k("IndusInd Bank")}.',
        f'Reason: violating RBI rules on {k("Interest Rate on Deposits")} and {k("Securitisation of Standard Assets")}.'],
        f'IndusInd Bank — Founded {k("1994")} · HQ {k("Mumbai")}',
        None),
    ('PhonePe Leads UPI Transactions in July 2026', 'hot', [
        f'{k("PhonePe")} processed {k("10.86 billion")} UPI transactions in {k("July 2026")}.',
        f'Share by volume: {k("45.89%")}. Payments worth {k("₹14.44 lakh crore")}, a {k("48.33%")} share by value.',
        f'{k("Google Pay")} was second (32.33% by volume, 33.51% by value, per the PDF’s chart).'],
        f'PhonePe — Founded {k("2015")} · HQ {k("Bengaluru")} · Owned by {k("Walmart")}',
        'Two PhonePe numbers: <b>45.89%</b> by <b>volume</b>, <b>48.33%</b> by <b>value</b>. Don’t swap them.'),
]))

S.append(('Economy &amp; Reports', None, [
    ('India Ratings Projects India’s GDP Growth at 6.8% in FY 2026-27', 'hot', [
        f'{k("India Ratings &amp; Research (Ind-Ra)")} projected India’s GDP growth at {k("6.8%")} for {k("FY 2026-27")}.',
        f'The {k("RBI")} also revised its FY 2026-27 GDP growth forecast upward, to {k("6.7%")}.',
        f'Ind-Ra is a {k("SEBI")}-registered credit rating agency, recognised by SEBI and the RBI; HQ {k("Mumbai")}.',
        f'Ind-Ra is a {k("100%")} owned subsidiary of the {k("Fitch Group")}.'],
        None,
        'Ind-Ra <b>6.8%</b> vs RBI <b>6.7%</b>. Parent: <b>Fitch</b> (not Moody’s, which owns ICRA; not S&amp;P, which owns CRISIL).'),
]))

S.append(('Business &amp; Corporate', None, [
    ('Razorpay Launches AI-Powered Payments Foundation Model ‘Vulcan’', None, [
        f'Fintech company {k("Razorpay")} launched {k("Razorpay Vulcan")}, an AI-powered foundation model designed specifically for {k("digital payments")}.',
        f'Razorpay calls it {k("India’s first transformer-based AI foundation model")} built for payments.',
        f'Built using technology from {k("NVIDIA")} and {k("Amazon Web Services (AWS)")}.'],
        f'Razorpay — Founded {k("2014")} by {k("Harshil Mathur")} and {k("Shashank Kumar")} · HQ {k("Bengaluru")}',
        None),
    ('CCI Approves Tata Steel’s Additional 23% Stake in TM International Logistics', None, [
        f'The {k("Competition Commission of India (CCI)")} approved {k("Tata Steel")}’s acquisition of an additional {k("23%")} equity stake in {k("TM International Logistics Ltd (TMILL)")}.',
        f'Tata Steel will buy the entire 23% stake held by {k("IQ Martrade")} in the joint venture.',
        f'After the deal: Tata Steel {k("74%")}, {k("NYK Europe")} {k("26%")}.'],
        f'CCI — Est. {k("14 October 2003")} under the {k("Competition Act, 2002")} · HQ {k("New Delhi")} · Tata Steel founded {k("1907")}, HQ {k("Mumbai")}',
        'Seller = <b>IQ Martrade</b>; the remaining partner = <b>NYK Europe</b> (26%).'),
    ('ONGC Gets US Licence to Resume Full Operations in Venezuela', None, [
        f'State-owned {k("ONGC")} secured a licence from the US Treasury’s {k("Office of Foreign Assets Control (OFAC)")}.',
        f'It can now resume {k("full operations in Venezuela")} after years of restricted activity due to {k("US sanctions")}.'],
        f'ONGC — Est. {k("14 August 1956")} · HQ {k("New Delhi")} · Maharatna; overseas arm {k("ONGC Videsh")} · Venezuela capital {k("Caracas")}',
        'The licence came from <b>OFAC</b> (US <b>Treasury</b>), not the US State Department.'),
]))

S.append(('Government, Schemes &amp; Policy', None, [
    ('EPFO Launches ‘VISHWAS, 2026’ to Settle Damages and Penalty Disputes', 'hot', [
        f'{k("EPFO")} launched {k("VISHWAS, 2026")}, a {k("one-time settlement scheme")} for {k("employers")}.',
        f'It settles old disputes related to {k("damages and penalties")}.',
        f'In effect from {k("29 June 2026")}; open for {k("6 months")}.',
        'Aims: reduce litigation, encourage voluntary compliance and settle old cases faster through a fully digital, time-bound process.',
        f'Reduced penalty rates for defaults before {k("14 June 2024")}: up to 2 months’ delay → {k("0.25%")} per month; more than 2 months → {k("0.50%")} per month; more than 4 months → {k("1%")} per month.'],
        f'EPFO — {k("Employees’ Provident Fund Organisation")} · Under the {k("Ministry of Labour and Employment")} · Formed {k("4 March 1952")} · HQ {k("New Delhi")}',
        'VISHWAS is for <b>employers</b> (not employees). Cut-off for old defaults: <b>14 June 2024</b>; scheme start: <b>29 June 2026</b>.'),
    ('Government Makes TReDS Mandatory for CPSE Payments to MSMEs', 'bank', [
        f'The {k("Ministry of MSME")} made it mandatory for all operating {k("Central Public Sector Enterprises (CPSEs)")} to settle invoices of their MSME suppliers through RBI-authorised {k("TReDS")} platforms.',
        f'Aim: tackle {k("delayed payments to MSMEs")} and improve their access to {k("working capital")}.',
        'MSME invoices for goods and services supplied to CPSEs will be routed through the Trade Receivables Discounting System (TReDS).',
        f'Once an invoice is approved, the MSME can get paid {k("before the due date")} by having it discounted by participating {k("banks and NBFCs")}.',
        f'TReDS: an {k("RBI-regulated")} electronic platform, operational since {k("2017")}, for MSMEs to finance receivables from corporates, government departments and PSUs.',
        f'{k("Five")} TReDS platforms operate: {k("RXIL")}, {k("M1xchange")}, {k("Invoicemart")}, {k("C2treds")} and {k("DTX")}.',
        f'Timeline (PDF chart): 2017 TReDS goes live → Nov 2018 companies with turnover above ₹500 crore and all CPSEs must onboard → Nov 2024 threshold cut to {k("₹250 crore")} → {k("30 June 2026")} settlement through TReDS mandatory for CPSEs.'],
        f'MSMED Act, 2006 — buyers must pay MSME suppliers within {k("45 days")} (Section 15) · Ministry of MSME formed {k("2007")}',
        'Earlier rules only required CPSEs to <b>register/onboard</b> on TReDS; the 2026 rule makes <b>settling invoices</b> through TReDS mandatory.'),
]))

IMG = {
    'YES Essence': 'pdf:p01_06|YES Bank',
    'IDFC FIRST': 'pdf:p01_03|IDFC FIRST international bond',
    'Regional Rural Banks': 'pdf:p02_05|RRB branch',
    'IndusInd': 'pdf:p02_02|IndusInd Bank',
    'PhonePe': 'pdf:p02_01|UPI payment',
    'India Ratings': 'pdf:p02_03|GDP growth',
    'Razorpay': 'pdf:p03_03|Razorpay',
    'Tata Steel': 'pdf:p03_02|Tata Steel',
    'ONGC': 'pdf:p03_07|ONGC',
    'VISHWAS': 'pdf:p03_01|VISHWAS 2026',
    'TReDS': 'pdf:p04_05|Invoice discounting',
}

QUIZ = [
    ('YES Essence credit card is aimed at whom?', 'Women — rewards plus health and lifestyle benefits'),
    ('IDFC FIRST Bank’s maiden international bond — amount, tenure, coupon, where issued?', '$500 million; 3 years (due 2029); 5.625%; IFSC Banking Unit, GIFT City'),
    ('Which agency rated IDFC FIRST Bank ‘BBB-’ (Stable)?', 'S&amp;P Global Ratings'),
    ('RRB gross loans in FY 2025-26 and growth?', '₹5.78 lakh crore, up 10.3% (from ₹5.24 lakh crore)'),
    ('PSL target for RRBs, and what they achieved in FY26?', '75% of ANBC; achieved 91.7%'),
    ('RBI penalty on IndusInd Bank — amount and rules violated?', '₹59.20 lakh; interest rate on deposits and securitisation of standard assets'),
    ('PhonePe’s UPI share in July 2026 by volume and by value?', '45.89% by volume (10.86 bn txns), 48.33% by value (₹14.44 lakh crore)'),
    ('Ind-Ra’s and RBI’s FY 2026-27 GDP growth forecasts?', 'Ind-Ra 6.8%, RBI 6.7%'),
    ('Ind-Ra is a subsidiary of which group?', 'Fitch Group (100%)'),
    ('What is Razorpay Vulcan, and whose technology does it use?', 'India’s first transformer-based AI foundation model for payments; NVIDIA and AWS'),
    ('Tata Steel’s stake in TMILL after the deal, and who sold the 23%?', '74% (NYK Europe 26%); seller IQ Martrade'),
    ('Which US body licensed ONGC to resume operations in Venezuela?', 'OFAC — US Treasury’s Office of Foreign Assets Control'),
    ('VISHWAS, 2026 — whose scheme, for whom, start date and duration?', 'EPFO; employers; from 29 June 2026; open 6 months'),
    ('Under VISHWAS, penalty rate for a delay of more than 4 months?', '1% per month (defaults before 14 June 2024)'),
    ('Name the five TReDS platforms.', 'RXIL, M1xchange, Invoicemart, C2treds, DTX'),
]

RAPID = [
    'YES Essence card (women-focused) · IDFC FIRST $500 mn maiden bond: 3 yr, 5.625%, GIFT City IBU, Reg S, S&amp;P ‘BBB-’ Stable.',
    'RRBs FY26: loans ₹5.78 lakh cr (+10.3%) · PSL target 75% ANBC, achieved 91.7% · agri ₹3.78 lakh cr (77% of PSL) · MSME ₹66,978 cr (13.6%) · weaker sections ₹3.49 lakh cr.',
    'RBI fined IndusInd ₹59.20 lakh · PhonePe July: 10.86 bn txns, 45.89% volume, 48.33% value (₹14.44 lakh cr).',
    'GDP FY27: Ind-Ra 6.8% (Fitch-owned, Mumbai) · RBI 6.7%.',
    'Razorpay Vulcan: first transformer-based payments AI model (NVIDIA + AWS) · CCI OKs Tata Steel +23% in TMILL (from IQ Martrade → 74:26 with NYK Europe) · ONGC gets OFAC licence for Venezuela.',
    'EPFO VISHWAS 2026: employers’ one-time settlement, from 29 June 2026 for 6 months; old defaults (before 14 June 2024) at 0.25% / 0.50% / 1% per month.',
    'TReDS mandatory for CPSE payments to MSMEs (30 June 2026) · 5 platforms: RXIL, M1xchange, Invoicemart, C2treds, DTX · TReDS live since 2017.',
]

# Exam-style mock test (builds YYYY-MM-Month-Class-N-Quiz.html).
# (question, correct option, [4 wrong options], explanation) — options are shuffled at build time.
MCQ = [
    ('YES Bank\'s new "YES Essence" credit card is aimed at:',
     'Women, combining rewards with health and lifestyle benefits', ['Senior citizens, with healthcare benefits', 'Students, with zero annual fee', 'MSMEs, with business expense tracking', 'Frequent flyers, with lounge access'],
     'YES Essence is a women-focused card with health and lifestyle benefits. YES Bank: founded 2004, HQ Mumbai.'),
    ('IDFC FIRST Bank raised $500 million through its maiden international bond issue via:',
     'Its IFSC Banking Unit at GIFT City', ['Its London branch', 'Its Singapore branch', 'Its Dubai (DIFC) branch', 'The India INX in Mumbai'],
     'Issued through the GIFT City IBU. (SBI\'s $500 mn in Class 5 was via its London branch.)'),
    ('What are the tenure and coupon of IDFC FIRST Bank\'s maiden $500 million senior notes?',
     '3 years at 5.625%', ['5 years at 5.25%', '3 years at 5.25%', '5 years at 5.625%', '10 years at 6.125%'],
     'Three-year fixed-rate senior notes due 2029, coupon 5.625%, under Regulation S.'),
    ('Which rating did S&P Global Ratings give IDFC FIRST Bank (long-term issuer credit rating)?',
     'BBB- with Stable Outlook', ['BBB with Positive Outlook', 'BB+ with Stable Outlook', 'A- with Stable Outlook', 'BBB- with Negative Outlook'],
     '\'BBB-\' with Stable Outlook from S&P Global Ratings.'),
    ('Gross loans outstanding of Regional Rural Banks grew 10.3% in FY 2025-26 to:',
     '₹5.78 lakh crore', ['₹5.24 lakh crore', '₹3.78 lakh crore', '₹6.24 lakh crore', '₹3.49 lakh crore'],
     'From ₹5.24 lakh crore (FY25) to ₹5.78 lakh crore (FY26).'),
    ('RBI\'s overall Priority Sector Lending target for Regional Rural Banks is:',
     '75% of ANBC', ['40% of ANBC', '18% of ANBC', '60% of ANBC', '91.7% of ANBC'],
     '75% of ANBC for RRBs (and SFBs); 40% for ordinary commercial banks. RRBs achieved an average 91.7%.'),
    ('RRB credit to agriculture and allied activities in FY 2025-26 was ₹3.78 lakh crore. What share of total PSL is this?',
     '77%', ['98%', '75%', '91.7%', '13.6%'],
     '77% of total PSL; farm credit was ~98% of agricultural lending; MSME share 13.6% (₹66,978 crore).'),
    ('How much credit did RRBs provide to weaker sections in FY 2025-26?',
     '₹3.49 lakh crore', ['₹3.78 lakh crore', '₹66,978 crore', '₹5.24 lakh crore', '₹2.49 lakh crore'],
     '₹3.49 lakh crore to weaker sections.'),
    ('RBI imposed a monetary penalty on IndusInd Bank for violating rules on Interest Rate on Deposits and Securitisation of Standard Assets. The amount was:',
     '₹59.20 lakh', ['₹95.20 lakh', '₹52.90 lakh', '₹59.20 crore', '₹1.48 crore'],
     '₹59.20 lakh on IndusInd Bank.'),
    ('PhonePe processed how many UPI transactions in July 2026?',
     '10.86 billion', ['23.66 billion', '14.44 billion', '7.62 billion', '8.16 billion'],
     '10.86 billion transactions worth ₹14.44 lakh crore. (Total UPI in July: 23.66 bn — Class 1.)'),
    ('PhonePe\'s share of UPI transactions in July 2026 by VOLUME was:',
     '45.89%', ['48.33%', '32.33%', '33.51%', '50.12%'],
     'Volume share 45.89%; value share 48.33%. Google Pay was second.'),
    ('PhonePe, the UPI market leader, is owned by:',
     'Walmart', ['Alphabet (Google)', 'Amazon', 'Paytm (One97)', 'Tata Group'],
     'PhonePe: founded 2015, HQ Bengaluru, owned by Walmart.'),
    ('India Ratings & Research (Ind-Ra) has projected India\'s GDP growth for FY 2026-27 at:',
     '6.8%', ['6.7%', '6.5%', '7.0%', '6.4%'],
     'Ind-Ra 6.8%; RBI revised its forecast to 6.7%.'),
    ('India Ratings & Research (Ind-Ra) is a 100% owned subsidiary of:',
     'Fitch Group', ['Moody\'s', 'S&P Global', 'CARE Ratings', 'Morningstar'],
     'Fitch. (ICRA → Moody\'s; CRISIL → S&P Global.)'),
    ('Razorpay\'s AI foundation model built specifically for digital payments is named:',
     'Vulcan', ['Titan', 'Atlas', 'Orion', 'Muse Glimmer'],
     'Razorpay Vulcan — India\'s first transformer-based AI foundation model for payments.'),
    ('Razorpay Vulcan was built using technology from:',
     'NVIDIA and Amazon Web Services', ['Google Cloud and Intel', 'Microsoft Azure and OpenAI', 'Meta and AMD', 'NVIDIA and Microsoft Azure'],
     'Built with NVIDIA and AWS technology.'),
    ('CCI approved Tata Steel\'s acquisition of an additional 23% stake in TM International Logistics from:',
     'IQ Martrade', ['NYK Europe', 'Tata Sons', 'Mitsui & Co', 'Adani Logistics'],
     'IQ Martrade sells its entire 23%. After the deal: Tata Steel 74%, NYK Europe 26%.'),
    ('After acquiring IQ Martrade\'s stake, what will be Tata Steel\'s stake in TM International Logistics Ltd?',
     '74%', ['51%', '23%', '77%', '100%'],
     'Tata Steel 74% : NYK Europe 26%.'),
    ('ONGC secured a licence to resume full operations in Venezuela from:',
     'Office of Foreign Assets Control (OFAC), US Treasury', ['US State Department', 'US Department of Commerce (BIS)', 'OPEC Secretariat', 'Government of Venezuela\'s PDVSA'],
     'OFAC, under the US Treasury. Venezuela\'s capital: Caracas.'),
    ('EPFO\'s "VISHWAS, 2026" is a one-time settlement scheme for:',
     'Employers, to settle disputes over damages and penalties', ['Employees, to settle pending PF withdrawals', 'Pensioners, to settle pension arrears', 'Employers, to waive all PF dues', 'Banks, to settle EPFO deposit disputes'],
     'For employers; in effect from 29 June 2026, open for 6 months.'),
    ('Under VISHWAS, 2026, the reduced penalty rates apply to defaults that occurred before:',
     '14 June 2024', ['29 June 2026', '1 April 2025', '4 March 2024', '31 December 2023'],
     'Defaults before 14 June 2024: 0.25%/month (≤2 months delay), 0.50% (>2 months), 1% (>4 months).'),
    ('Under VISHWAS, 2026, what is the reduced damages rate for a delay of up to 2 months?',
     '0.25% per month', ['0.50% per month', '1% per month', '2% per month', '0.75% per month'],
     'Up to 2 months → 0.25%; more than 2 months → 0.50%; more than 4 months → 1% per month.'),
    ('The Ministry of MSME has made it mandatory for all operating CPSEs to:',
     'Settle MSME suppliers\' invoices through RBI-authorised TReDS platforms', ['Pay MSMEs within 15 days through GeM', 'Register on the Udyam portal', 'Buy 50% of goods from MSMEs', 'Route MSME payments through CBDC wallets'],
     'From 30 June 2026, settlement through TReDS is mandatory for CPSEs (earlier only onboarding was required).'),
    ('How many TReDS platforms operate in India?',
     'Five', ['Three', 'Four', 'Six', 'Seven'],
     'RXIL, M1xchange, Invoicemart, C2treds and DTX.'),
    ('In November 2024, the turnover threshold for companies that must onboard on TReDS was reduced to:',
     '₹250 crore', ['₹500 crore', '₹100 crore', '₹1,000 crore', '₹50 crore'],
     'Nov 2018: above ₹500 crore + all CPSEs; Nov 2024: threshold cut to ₹250 crore.'),
]
