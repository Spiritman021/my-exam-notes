# August 2026 · Class 5 — source: Class_05_August_2026_Monthly_Current_Affairs_by_Ashish_Gautam_Sir.pdf
# News content kept as in the PDF (English half, pages 1-16); Static GK boxes and exam traps added on top.
# PDF slips fixed: "Jammu & Kashmit" → Kashmir; Zhu Rongji "She was 97" → he.
# Pictures come from the PDF itself (IMG values 'pdf:…', see pdf_images.py).
# Each section: (title, intro, [items]); item = (headline, tag, [facts], gk, trap). k('x') marks a key fact.
S = []

S.append(('Banking, Finance &amp; Insurance', None, [
    ('SBI Raises $500 Million Overseas', 'bank', [
        f'{k("State Bank of India (SBI)")} raised {k("$500 million")} through a {k("Regulation S bond")} issue.',
        f'The bonds were issued through SBI’s {k("London branch")}.',
        f'Tenure: {k("5 years")} · Coupon rate: {k("5.25%")}.',
        f'Regulation S bond: an international bond offered mainly to investors {k("outside the US")}.'],
        f'SBI — Est. {k("1 July 1955")} (from the Imperial Bank of India) · HQ {k("Mumbai")} · India’s largest bank',
        'Issued from the <b>London</b> branch; <b>Reg S</b> = sold to investors <b>outside the US</b>. 5 years at <b>5.25%</b>.'),
    ('Bank of America to Acquire Up to 49.9% Stake in Jio Credit', 'bank', [
        f'{k("Jio Financial Services Ltd (JFSL)")} and {k("Bank of America")} announced a strategic partnership.',
        f'Bank of America will acquire up to {k("49.9%")} stake in {k("Jio Credit Limited (JCL)")}, currently a wholly owned {k("NBFC")} subsidiary of JFSL.',
        f'Total proposed investment: up to {k("₹18,268 crore")} (about {k("$1.9 billion")}).',
        f'Initially Bank of America gets about {k("26.5%")} equity; it can later rise to 49.9%.'],
        f'Bank of America — HQ {k("Charlotte, North Carolina, USA")} · Jio Financial Services HQ {k("Mumbai")}',
        'Two numbers: <b>26.5%</b> at first, up to <b>49.9%</b> later. The target is <b>Jio Credit</b> (the NBFC), not JFSL itself.'),
    ('SBI Uses AI to Underwrite Nearly ₹1 Lakh Crore MSME Loans in FY 2025-26', 'bank', [
        f'SBI used {k("Artificial Intelligence")} to underwrite nearly {k("₹1 lakh crore (₹1 trillion)")} of {k("MSME")} loans in {k("FY 2025-26")}.',
        f'Shared by SBI MD {k("Rama Mohan Rao Amara")} at the {k("FICCI–IBA Conference")} in {k("Mumbai")}.',
        f'AI-based underwriting covered individual MSME loans of up to {k("₹5 crore")}.',
        'Loan underwriting = evaluating a borrower’s creditworthiness and repayment capacity before approving a loan.'],
        f'IBA — {k("Indian Banks’ Association")}, est. {k("1946")}, HQ {k("Mumbai")} · FICCI est. {k("1927")}, HQ {k("New Delhi")}',
        'Loan cap for AI underwriting: <b>₹5 crore</b> each; total ≈ <b>₹1 lakh crore</b>.'),
    ('EazyDiner and IndusInd Bank Launch Lifetime-Free Credit Card Linked to UPI', 'bank', [
        f'{k("IndusInd Bank")} and dining platform {k("EazyDiner")} launched the {k("EazyDiner IndusInd Bank Platinum RuPay Credit Card")}.',
        f'The card is {k("lifetime free")}.',
        f'Being on the {k("RuPay")} network, it can be linked with supported {k("UPI")} apps.'],
        f'IndusInd Bank — Founded {k("1994")} · HQ {k("Mumbai")} · RuPay launched by {k("NPCI")} in {k("2012")}',
        'Only <b>RuPay</b> credit cards can be linked to UPI — that is why the card is on RuPay.'),
    ('SBI Life Insurance Ties Up with Jammu &amp; Kashmir Bank', 'bank', [
        f'{k("SBI Life Insurance")} entered a strategic {k("corporate agency")} partnership with {k("Jammu &amp; Kashmir Bank")}.',
        f'J&amp;K Bank customers can buy SBI Life products through the bank’s {k("1,000-plus branches")}.'],
        f'J&amp;K Bank — Est. {k("1938")} · HQ {k("Srinagar")}',
        'Arrangement type: <b>corporate agency</b> (bancassurance).'),
]))

S.append(('Economy &amp; Reports', None, [
    ('India’s WPI Inflation Eases to 9.78% in July 2026', 'hot', [
        f'WPI inflation fell to {k("9.78%")} in July, from {k("9.87%")} in June.',
        f'The {k("first month-on-month drop")} under the new WPI series with base year {k("2022-23")}.',
        f'Compiled by the {k("Office of the Economic Adviser (OEA)")}, {k("DPIIT")}, {k("Ministry of Commerce and Industry")}.',
        'Measures prices at the wholesale/bulk level, not prices paid by consumers.',
        f'Items: {k("957")} — Primary Articles {k("129")}, Fuel &amp; Power {k("25")}, Manufactured Products {k("803")}.'],
        None,
        'WPI → <b>OEA/DPIIT</b> (Commerce); CPI → <b>NSO/MoSPI</b>. Don’t swap the ministries. WPI base <b>2022-23</b>, CPI base <b>2024</b>.'),
    ('India’s Retail Inflation Rises to 4.45% in July 2026', 'hot', [
        f'CPI (retail) inflation rose to {k("4.45%")} in July 2026, from {k("4.38%")} in June.',
        f'{k("Second consecutive month")} above the RBI’s {k("4%")} target.',
        f'Current CPI series: {k("2024 = 100")}; base revised from {k("2012 to 2024")} in {k("February 2026")}.',
        f'Weighted items: {k("358")} (Goods {k("308")} + Services {k("50")}).',
        f'Compiled by the {k("National Statistical Office (NSO)")}, {k("MoSPI")}; released monthly on the {k("12th")} of the next month.',
        'The new series was first released (for January 2026) on 12 February 2026.'],
        f'Inflation target — RBI targets CPI inflation of {k("4% ± 2%")} (band {k("2–6%")}), set by the government; the {k("Monetary Policy Committee")} has {k("6")} members',
        'Count trap: CPI <b>358</b> items, WPI <b>957</b> items.'),
    ('Unemployment Rate Rises to 5.4% in April–June 2026', None, [
        f'Unemployment rate (age {k("15+")}) rose to {k("5.4%")} in the {k("April–June 2026")} quarter, from {k("5.0%")} in January–March.',
        'An increase of 0.4 percentage points.',
        f'Source: {k("Periodic Labour Force Survey (PLFS)")}, released by {k("MoSPI")}.'],
        None, None),
    ('Ambani Family Retains No. 1 for Third Year: Hurun-Barclays List', 'hot', [
        f'{k("Barclays Private Clients Hurun India")} released the {k("2026 Most Valuable Family Businesses")} list.',
        f'India’s top {k("300")} family businesses are worth about {k("₹138 lakh crore ($1.46 trillion)")}, up about {k("27.5%")} since 2024 — about {k("₹4,076 crore")} added per day.',
        f'{k("Ambani family")} retained No. 1 ({k("third consecutive year")}) at about {k("₹25.83 lakh crore")}; flagship {k("Reliance Industries")}.',
        f'First-generation group: {k("Adani family")} leads (₹19.6 lakh crore), then {k("Sunil Bharti Mittal")} family (₹12.1 lakh crore) and {k("Dilip Shanghvi")} family (₹4.55 lakh crore).'],
        None,
        'Ambani = No. 1 overall; <b>Adani</b> = No. 1 among <b>first-generation</b> families.'),
]))

S.append(('Government, Schemes &amp; Policy', None, [
    ('Government Launches CBDC-Based DBT under PMGKAY', 'bank', [
        f'CBDC-based {k("Direct Benefit Transfer")} under {k("PMGKAY")} launched on {k("14 August 2026")} in {k("Chandigarh")} and {k("Dadra &amp; Nagar Haveli")}.',
        f'These became the {k("first UT areas")} to cover all eligible PMGKAY beneficiaries through programmable {k("Digital Rupee")} food-subsidy transfers.',
        f'Earlier: subsidy → normal bank account. Now: subsidy → {k("Digital Rupee (e₹)")} → beneficiary’s {k("CBDC wallet")}, used to buy foodgrains from empanelled merchants.',
        f'Earlier pilots of CBDC food subsidy: {k("Puducherry")} and {k("Gujarat")}.',
        f'PMGKAY gives free foodgrains to beneficiaries under the {k("National Food Security Act (NFSA), 2013")}; continued for {k("5 years from 1 January 2024")}.',
        f'Covers two ration-card categories: {k("Antyodaya Anna Yojana (AAY)")} and {k("Priority Households (PHH)")}.'],
        f'e₹ (Digital Rupee) — India’s CBDC, issued by the {k("RBI")} · Wholesale pilot {k("1 November 2022")}, retail pilot {k("1 December 2022")}',
        'Launch UTs: <b>Chandigarh</b> + <b>Dadra &amp; Nagar Haveli</b>. Pilots were in <b>Puducherry</b> and <b>Gujarat</b> — don’t mix them.'),
    ('PM E-DRIVE Scheme Extended Till FY 2027-28', 'hot', [
        f'The {k("Ministry of Heavy Industries (MHI)")} extended {k("PM E-DRIVE")} till {k("31 March 2028")} (runs 1 April 2024 – 31 March 2028).',
        f'Total outlay: {k("₹11,900 crore")}. Aims: faster EV adoption, charging infrastructure, EV manufacturing ecosystem.',
        f'e-2W allocation raised by nearly ₹1,000 crore to {k("₹2,767 crore")}, for up to {k("45,79,120")} vehicles; max ex-factory price {k("₹1.5 lakh")}.',
        f'e-2W subsidy: {k("₹2,500 per kWh")} of battery, capped at {k("₹5,000")} per vehicle.',
        f'{k("EMPS-2024")} (1 April – 30 September 2024) has been {k("subsumed")} into PM E-DRIVE.'],
        f'PM E-DRIVE — {k("PM Electric Drive Revolution in Innovative Vehicle Enhancement")} · Earlier EV scheme: {k("FAME")} (Faster Adoption and Manufacturing of (Hybrid &amp;) Electric Vehicles)',
        'Ministry is <b>Heavy Industries</b>, not Road Transport. Subsidy ₹2,500/kWh but max <b>₹5,000</b>.'),
    ('Vande Mataram Bill Becomes Law', 'hot', [
        f'President {k("Droupadi Murmu")} gave assent to the {k("Prevention of Insults to National Honour (Amendment) Bill, 2026")}.',
        f'{k("Vande Mataram")} now gets the same legal protection as {k("Jana Gana Mana")}: intentionally stopping its singing, or disturbing an assembly where it is sung, is an offence.',
        f'Earlier the {k("Prevention of Insults to National Honour Act, 1971")} covered only the National Anthem.',
        f'Punishment: up to {k("3 years")} imprisonment, or fine, or both; second or later conviction: minimum {k("1 year")}.'],
        f'Vande Mataram — Written by {k("Bankim Chandra Chattopadhyay")}, part of his novel {k("Anandamath")} (1882) · Adopted as National Song on {k("24 January 1950")} (same day as Jana Gana Mana)',
        'Amends the <b>1971</b> Act. Max <b>3 years</b>; repeat offence minimum <b>1 year</b>.'),
    ('TRAI Begins Rollout of 1601-Series Numbers for Trusted Service Calls', None, [
        f'{k("TRAI")} began a phase-wise rollout of the {k("1601-series")} numbering system for {k("service and transactional")} voice calls.',
        'Meant for entities outside the BFSI sector and government organisations.',
        f'Number series allotted by the {k("Department of Telecommunications (DoT)")}.',
        f'Helps consumers identify genuine business calls; {k("cannot be used for promotional")} or marketing calls.',
        f'TRAI — set up under {k("Section 3 of the TRAI Act, 1997")} · Formed {k("20 February 1997")} · HQ {k("New Delhi")} · Chairperson {k("Anil Kumar Lahoti")}.'],
        None,
        'TRAI <b>rolls out</b>, but the series is <b>allotted by DoT</b>. Promotional calls are <b>not</b> allowed on 1601.'),
    ('India Post Delivers Tiranga by Drone in Himachal Pradesh', None, [
        f'In a first-of-its-kind initiative, {k("India Post")} delivered the National Flag by {k("drone")} in {k("Himachal Pradesh")}.',
        f'Route: {k("Mandi Head Post Office")} → {k("Rehardhar Branch Post Office")}, on the eve of Independence Day 2026.',
        f'Virtually inaugurated by {k("Jyotiraditya M. Scindia")}, Union Minister for Communications and DoNER.',
        'The Tiranga was handed over to an Army veteran.'],
        f'India Post — Department of Posts, {k("Ministry of Communications")} · Founded {k("1854")}',
        None),
    ('BHASHINI and NITI Aayog Sign Statement of Intent on Multilingual AI', None, [
        f'{k("Digital India BHASHINI Division (DIBD)")} and {k("NITI Aayog")} signed a {k("Statement of Intent (SoI)")}.',
        f'Goal: {k("multilingual, voice-first AI")} for governance, access to services and communication with citizens in their own languages.',
        f'Implemented through the {k("“BHASHINI for Seva/Sanchalan”")} initiative; BHASHINI tech will be built into NITI Aayog’s platforms.'],
        f'BHASHINI — {k("Bhasha Interface for India")} · Launched {k("2022")} under {k("MeitY")} (National Language Translation Mission) · NITI Aayog est. {k("1 January 2015")}, replacing the Planning Commission',
        'It is a <b>Statement of Intent</b>, not an MoU.'),
    ('MakeMyTrip Partners with Ministry of Tourism for Guided Tours', None, [
        f'{k("MakeMyTrip")} partnered with the {k("Ministry of Tourism")} to offer {k("350+ guided tours")} across {k("60+ cities")}.',
        'Bookable on MakeMyTrip from Independence Day.',
        f'Aligned with {k("Incredible India")} and {k("Dekho Apna Desh")}.'],
        None, None),
    ('DPIIT and MSME Ministry Sign MoU to Take India’s GI Products Global', 'hot', [
        f'The {k("Ministry of MSME")} and {k("DPIIT")} signed an MoU to boost commercialisation and market reach of {k("Geographical Indication (GI)")} products.',
        f'GI collectives and authorised users will be onboarded on {k("ONDC")} (Open Network for Digital Commerce) and {k("GeM")} (Government e-Marketplace).',
        f'GI products will be promoted under a dedicated {k("“Bharat GI”")} banner.'],
        f'GI — Governed by the {k("Geographical Indications of Goods (Registration and Protection) Act, 1999")} · GI Registry in {k("Chennai")} · India’s first GI: {k("Darjeeling Tea")} (2004)',
        'Banner name: <b>Bharat GI</b>. Platforms: <b>ONDC + GeM</b>.'),
]))

S.append(('Technology &amp; AI', None, [
    ('L&amp;T to Build India’s Largest NVIDIA B300 AI Factory', 'hot', [
        f'{k("Larsen &amp; Toubro (L&amp;T)")} won a “Mega” order to build India’s {k("largest single-cluster AI infrastructure")} — its entry into the AI Factory business.',
        f'Hosted at {k("Vyoma’s Chennai")} data-centre campus, Tamil Nadu; capacity for {k("10,000 NVIDIA B300 GPUs")}.',
        f'Executed for {k("Together AI")}, a US-based AI cloud company.',
        f'Developed through {k("Vyoma.AI")} (L&amp;T’s AI cloud and hyperscale data-centre business) and {k("LTN Compute")} (Vyoma.AI’s AI-infrastructure subsidiary).',
        'GPU = Graphics Processing Unit; GPUs give the computing power modern AI models need.'],
        f'L&amp;T — Founded {k("1938")} · HQ {k("Mumbai")} · NVIDIA HQ {k("Santa Clara, California")}',
        'Client is <b>Together AI</b> (US); site is <b>Chennai</b>; chips are <b>B300</b>.'),
    ('Meta Launches Open-Weight AI Model ‘Muse Glimmer’', None, [
        f'{k("Meta")} launched {k("Muse Glimmer")}, an {k("open-weight")} AI model built mainly for {k("agentic AI")} tasks (multi-step tasks with limited human help).',
        f'Smaller than leading frontier models; runs on a Mac or PC with a {k("single GPU")}.',
        f'Chinese AI models: {k("Kimi K3")} – Moonshot AI · {k("Qwen3.8-Max")} – Alibaba · {k("V4-Flash")} – DeepSeek.'],
        None,
        'Match model to maker: Kimi → <b>Moonshot AI</b>, Qwen → <b>Alibaba</b>, V4-Flash → <b>DeepSeek</b>.'),
    ('IISc SPIRE Lab Releases SraVaani Speech AI Model for 65 Indian Languages', 'hot', [
        f'{k("IISc Bengaluru’s SPIRE Lab")}, with {k("ARTPARK")} and support from {k("Google")}, released {k("SraVaani")}, a multilingual {k("Automatic Speech Recognition (ASR)")} model.',
        f'Supports {k("65")} Indian languages and dialects: {k("20 Scheduled Languages")} + {k("45")} regional languages and dialects.',
        'Converts speech to text and automatically identifies the spoken language.',
        f'Built on data from {k("Project Vaani")}, a large multilingual speech dataset of how people actually speak across India.'],
        f'IISc — {k("Indian Institute of Science")}, founded {k("1909")}, Bengaluru · The Eighth Schedule lists {k("22")} languages',
        '<b>65 = 20 + 45</b>. Dataset: <b>Project Vaani</b>.'),
]))

S.append(('Environment &amp; Wildlife', None, [
    ('Gujarat’s Deesa to Get Asia’s First Desert-Themed Night Safari &amp; Zoo', 'hot', [
        f'{k("Deesa")} ({k("Banaskantha district, Gujarat")}) will host {k("Asia’s first desert-themed")} drive-through night safari and zoological park.',
        f'Area about {k("103 hectares")}; estimated cost {k("₹542.14 crore")}.',
        f'Approved by the {k("Central Zoo Authority")}.',
        f'Central Zoo Authority — oversees zoos · est. {k("1992")} under the {k("Wildlife (Protection) Act, 1972")} · statutory body under {k("MoEFCC")} · HQ {k("New Delhi")} · affiliate member of {k("WAZA")}.'],
        None,
        'CZA was set up in <b>1992</b> under the <b>1972</b> Act — two different years.'),
    ('Ladakh Hosts First-Ever Black-Necked Crane Festival', None, [
        f'{k("Ladakh")} held its first-ever {k("Black-necked Crane Festival")}; the crane is the {k("State Bird of Ladakh")}.',
        f'{k("Changthang Cold Desert Wildlife Sanctuary")} is its only breeding place in India.',
        f'Scientific name {k("Grus nigricollis")} · IUCN status {k("Near Threatened")}.'],
        None, None),
    ('India Donates Five Peacocks to UN Office at Geneva', None, [
        f'India donated {k("five peacocks")} to the {k("United Nations Office at Geneva (UNOG)")}.',
        f'Handed over by India’s Permanent Representative in Geneva, {k("Arindam Bagchi")}; received by UNOG Director-General {k("Tatiana Valovaya")}.',
        f'Scientific name {k("Pavo cristatus")}.'],
        f'Indian peafowl — National Bird of India since {k("1963")} · Protected under {k("Schedule I")} of the Wildlife (Protection) Act, 1972',
        None),
]))

S.append(('Appointments &amp; Elections', None, [
    ('Gyanesh Bharti Appointed Chief Secretary of Andaman &amp; Nicobar Islands', 'hot', [
        f'The {k("Ministry of Home Affairs")} appointed {k("Gyanesh Bharti")} as Chief Secretary of {k("Andaman and Nicobar Islands")}.',
        f'He was serving as {k("Deputy Election Commissioner")} in the Election Commission of India.',
        f'A&amp;N Islands: formed {k("1 November 1956")} · capital {k("Sri Vijaya Puram")} (Port Blair) · Lieutenant Governor {k("Devendra Kumar Joshi")}.',
        f'National parks include Mahatma Gandhi Marine, {k("Mount Harriet (now Mount Manipur)")}, Saddle Peak, North/Middle/South Button Island, Rani Jhansi Marine, Campbell Bay, Galathea.'],
        None,
        'Port Blair is now <b>Sri Vijaya Puram</b>; Mount Harriet is now <b>Mount Manipur</b>.'),
    ('Dr Bhooma VG Selected as Vice-Chancellor of AIPSI, Mauritius', None, [
        f'{k("Dr Bhooma VG")} was selected Vice-Chancellor of the {k("Atal Bihari Vajpayee Institute of Public Service and Innovation (AIPSI)")} in {k("Mauritius")}.',
        f'Announced by India’s {k("Ministry of External Affairs")}.'],
        f'Mauritius — Capital {k("Port Louis")} · Currency {k("Mauritian rupee")}',
        None),
    ('Indriya Names Krithi Shetty Southern Brand Ambassador', None, [
        f'{k("Indriya")}, the jewellery brand of the {k("Aditya Birla Group")}, named actor {k("Krithi Shetty")} its Brand Ambassador for southern markets.',
        f'Announced ahead of the {k("Varalakshmi")} festival (Varalakshmi campaign).'],
        None, None),
    ('3 Indian Sanchar Mitras Selected as ITU Generation Connect Youth Envoys', None, [
        f'{k("DoT")} facilitated the selection of three Sanchar Mitras — {k("Ankit Kumar Pal")}, {k("Manish Kumar Mandal")}, {k("Susmita Sain")} — as {k("Generation Connect Youth Envoys (GCYE)")}.',
        f'An initiative of the {k("International Telecommunication Union (ITU)")}, letting young people join discussions on ICTs, digital transformation, connectivity and emerging tech.',
        f'ITU: UN specialised agency for ICT · formed {k("17 May 1865")} · HQ {k("Geneva")} · Secretary-General {k("Doreen Bogdan-Martin")}.'],
        None,
        'ITU (1865) is <b>older than the UN</b> itself; HQ <b>Geneva</b>.'),
    ('András Baka Elected President of Hungary', None, [
        f'Hungary’s Parliament elected former Supreme Court chief {k("András Baka")} as President.',
        f'Backed by the governing {k("TISZA Party")}, led by Prime Minister {k("Péter Magyar")}.',
        f'Hungary: capital {k("Budapest")} · currency {k("Forint")}.'],
        None, None),
]))

S.append(('International', None, [
    ('Lebanon Becomes First Arab Country to Abolish Death Penalty', 'hot', [
        f'Lebanon’s Parliament abolished the death penalty, replacing it with {k("life imprisonment with aggravated hard labour")}.',
        f'Lebanon is the {k("first Arab country")} to formally abolish capital punishment.',
        f'{k("Venezuela")} was the first country in the world to permanently abolish the death penalty for all crimes.'],
        f'Lebanon — Capital {k("Beirut")} · Currency {k("Lebanese pound")}',
        'First <b>Arab</b> country = Lebanon; first country <b>in the world</b> = Venezuela.'),
    ('India Attends Côte d’Ivoire’s 66th Independence Day', None, [
        f'MoS External Affairs {k("Kirti Vardhan Singh")} attended Côte d’Ivoire’s {k("66th")} Independence Day in {k("Abidjan")}.',
        f'Observed on {k("7 August")}, marking independence from {k("France")} in {k("1960")}.'],
        f'Côte d’Ivoire — Official capital {k("Yamoussoukro")}; Abidjan is the economic capital · Currency {k("West African CFA franc")}',
        'Celebrations were in <b>Abidjan</b>, but the official capital is <b>Yamoussoukro</b>.'),
    ('RBI Governor Co-Chairs BRICS Finance Meeting in Jaipur', 'bank', [
        f'FM {k("Nirmala Sitharaman")} and RBI Governor {k("Sanjay Malhotra")} co-chaired the {k("BRICS Finance Ministers and Central Bank Governors (FMCBG)")} meeting in {k("Jaipur, Rajasthan")}.',
        f'The {k("first FMCBG meeting")} under {k("India’s BRICS Chairship 2026")}.'],
        f'BRICS — Began as BRIC in {k("2009")}; South Africa joined in {k("2010")} · New Development Bank HQ {k("Shanghai")}',
        None),
]))

S.append(('Sports', None, [
    ('Canadian Open 2026: Swiatek and Shelton Win Singles Titles', 'hot', [
        f'Officially the {k("National Bank Open presented by Rogers")}.',
        f'Women: {k("Iga Swiatek (Poland)")} won in {k("Toronto")}; runner-up {k("Elena Rybakina (Kazakhstan)")}.',
        f'Men: {k("Ben Shelton (USA)")} won in {k("Montreal")}; runner-up {k("Brandon Nakashima (USA)")}.'],
        None,
        'Women’s event in <b>Toronto</b>, men’s in <b>Montreal</b>. Both men’s finalists were American.'),
    ('India Wins Commonwealth Fencing Championship 2026', 'hot', [
        f'India was overall champion at the {k("Commonwealth Fencing Championship 2026")} in {k("Lagos, Nigeria")}.',
        f'Total {k("35 medals")} (Under-23 + Senior): {k("13 gold")}, {k("8 silver")}, {k("14 bronze")}.',
        f'India also won the {k("Wilkinson Sword Trophy")}, given by the {k("Commonwealth Fencing Federation (CFF)")} for the best overall performance.',
        f'Per the Fencing Association of India, India’s {k("first")} Commonwealth Overall Championship title.'],
        f'Nigeria — Capital {k("Abuja")} (Lagos is the largest city) · Currency {k("Naira")}',
        'More <b>bronze (14)</b> than gold (13). Trophy name: <b>Wilkinson Sword</b>.'),
    ('Sports Ministry Suspends Recognition of TTFI', None, [
        f'The {k("Ministry of Youth Affairs and Sports")} suspended recognition of the {k("Table Tennis Federation of India (TTFI)")} over governance issues.',
        f'Main reason: failure to {k("hold elections")} on time.',
        f'The {k("Indian Olympic Association (IOA)")} has been asked to form an {k("Ad-hoc Committee")} to run table tennis.',
        f'IOA: founded {k("1927")} · HQ {k("New Delhi")} · President {k("P T Usha")}.'],
        None, None),
]))

S.append(('Defence', None, [
    ('Reliance and Rolls-Royce to Co-Develop Engine for AMCA', 'hot', [
        f'{k("Reliance Industries")} and UK-based {k("Rolls-Royce")} will jointly develop an indigenous combat-aircraft engine for the {k("Advanced Medium Combat Aircraft (AMCA)")}.',
        f'AMCA: India’s proposed {k("fifth-generation stealth, twin-engine")} fighter for the {k("IAF")}.',
        f'The initial AMCA version is planned to use the US-made {k("GE F414")} engine.'],
        f'AMCA — Designed by the {k("Aeronautical Development Agency (ADA)")} under {k("DRDO")}',
        'New engine partner: <b>Rolls-Royce (UK)</b>; early AMCA uses <b>GE F414 (US)</b>.'),
    ('HAL Partners with Adani Defence and BEML for Prachand Fuselages', 'hot', [
        f'{k("HAL")} partnered with {k("Adani Defence Systems and Technologies (ADSTL)")} and {k("BEML")} to make fuselages for the {k("Light Combat Helicopter (LCH) ‘Prachand’")}.',
        f'{k("BEML → 48")}, {k("Adani Defence → 42")}; total {k("90")} fuselage structures.'],
        f'LCH Prachand — Built by {k("HAL")} · Inducted into the IAF in {k("October 2022")} · BEML HQ {k("Bengaluru")}',
        'BEML makes <b>more</b> (48) than Adani (42).'),
    ('Defence Ministry Signs ₹1,577 Crore Contracts for Loitering Munitions', None, [
        f'{k("MoD")} signed contracts worth {k("₹1,577 crore")} for {k("Loitering Munition Systems")} for the {k("Indian Army")}.',
        f'Contracts with {k("Tata Advanced Systems Ltd (TASL)")} and {k("NIBE Private Ltd")}, in the presence of Defence Secretary {k("Rajesh Kumar Singh")}.',
        'A loitering munition flies over an area, searches for and identifies a target, then attacks it directly.'],
        None, None),
    ('INS Sudarshini Reaches the Azores during Lokayan 2026', None, [
        f'Sail training ship {k("INS Sudarshini")} entered {k("Ponta Delgada, Azores (Portugal)")} as part of {k("Lokayan 2026")}.',
        f'Arrived after a {k("19-day")} trans-Atlantic voyage from {k("Boston, USA")} — its {k("second Atlantic crossing")}.',
        f'Lokayan: {k("10 months")}, {k("22,000 nautical miles")}, {k("13 countries")}, {k("18 ports")}.',
        f'Built by {k("Goa Shipyard Limited")}.'],
        None,
        'Lokayan numbers: <b>10</b> months · <b>22,000</b> nm · <b>13</b> countries · <b>18</b> ports.'),
    ('GRSE Launches Second Next Generation OPV ‘Shruti’', None, [
        f'{k("Garden Reach Shipbuilders &amp; Engineers (GRSE)")} launched its second {k("Next Generation Offshore Patrol Vessel (NGOPV)")}, {k("‘Shruti’")}.',
        f'The first was {k("‘Sanghmitra’")}, launched in May 2026.',
        'GRSE is a PSU under the Ministry of Defence.'],
        f'GRSE — HQ {k("Kolkata")}',
        'First NGOPV <b>Sanghmitra</b>, second <b>Shruti</b>.'),
    ('Bhawana Kanth Becomes First Woman to Complete IAF’s Fighter Combat Leader Course', 'hot', [
        f'Squadron Leader {k("Bhawana Kanth")} became the {k("first woman")} IAF fighter pilot to complete the {k("Fighter Combat Leader (FCL) Course")}.',
        f'Conducted at the {k("Tactics and Air Combat Development Establishment (TACDE), Gwalior")}.',
        f'She is from {k("Darbhanga, Bihar")}; part of India’s first batch of women fighter pilots with {k("Avani Chaturvedi")} and {k("Mohana Singh")}.',
        f'First woman fighter pilot in the {k("Republic Day Parade (2021)")}; also in the Republic Day Flypast 2024.'],
        f'First women fighter pilots — Commissioned in {k("June 2016")}',
        'Course venue: <b>TACDE Gwalior</b>. Home town: <b>Darbhanga</b> (Bihar).'),
    ('India and Malaysia Hold Air Exercise Udara Shakti 2026', 'hot', [
        f'The {k("IAF")} and {k("Royal Malaysian Air Force")} held {k("Udara Shakti 2026")} at {k("Subang Air Base, Malaysia")}.',
        f'India–Malaysia exercises: Army → {k("Harimau Shakti")} · Navy → {k("Samudra Laksamana")} · Air Force → {k("Udara Shakti")}.'],
        f'Malaysia — Capital {k("Kuala Lumpur")} · Currency {k("Ringgit")}',
        'Udara = air, Harimau = tiger (army), Samudra = sea (navy).'),
    ('Indian Navy–US Navy EOD Exercise 2026 Begins in Kochi', None, [
        f'The {k("Indian Navy–US Navy Explosive Ordnance Disposal (EOD) Exercise 2026")} is under way at the {k("Southern Naval Command, Kochi")}.',
        f'Edition: {k("8th")}. Joint salvage and EOD exercises have been held since {k("2005")}.'],
        None, None),
]))

S.append(('Important Days', None, [
    ('World Lion Day — 10 August', 'hot', [
        f'Observed every year on {k("10 August")} for lion conservation, habitat protection and threats to wild lions.',
        f'Scientific name {k("Panthera leo")} · IUCN status {k("Vulnerable")}.',
        f'India has the {k("Asiatic Lion")}; main habitat the {k("Greater Gir Landscape, Gujarat")}; {k("Gir National Park and Wildlife Sanctuary")} is the core.',
        f'{k("Project Lion")}: announced by PM Modi on {k("15 August 2020")}.',
        f'Asiatic lion population (2025): {k("891")}; range nearly {k("35,000 sq km")} across {k("11 districts")}.'],
        None,
        'Same date (10 Aug) as <b>World Biofuel Day</b>. Lion count 2025 = <b>891</b>.'),
    ('World Biofuel Day — 10 August', None, [
        f'Observed every year on {k("10 August")} to promote biofuels as clean, renewable alternatives to fossil fuels.',
        f'First observed by the {k("Ministry of Petroleum and Natural Gas")} in {k("August 2015")}.',
        f'Commemorates {k("Sir Rudolf Diesel")} running an engine on {k("peanut oil")} on {k("9 August 1893")}.'],
        f'National Policy on Biofuels — Notified in {k("2018")}',
        'The day is <b>10 Aug</b>, but Diesel’s experiment was on <b>9 Aug 1893</b>.'),
    ('International Youth Day — 12 August', None, [
        f'Observed every year on {k("12 August")}.',
        f'2026 theme: “{k("Different Contexts, Common Aspirations")}”.',
        f'India’s {k("National Youth Day")} is {k("12 January")}, birth anniversary of {k("Swami Vivekananda")}; declared in {k("1984")}, first celebrated in {k("1985")}.'],
        None,
        'International = <b>12 Aug</b>; National (India) = <b>12 Jan</b>.'),
    ('World Elephant Day — 12 August', 'hot', [
        f'Observed every year on {k("12 August")} for Asian and African elephants.',
        f'India has about {k("60%")} of the world’s Asian elephants — {k("27,312")} (2017 census) — and {k("138")} identified elephant corridors.',
        f'{k("Project Elephant")}: centrally sponsored scheme launched in {k("February 1992")}.',
        f'Asian elephant IUCN status: {k("Endangered")}.',
        f'Declared India’s {k("National Heritage Animal")} on {k("22 October 2010")}.'],
        None,
        'Elephant = National <b>Heritage</b> Animal (2010); the National Animal is the tiger.'),
    ('World Organ Donation Day — 13 August', None, [
        f'Observed every year on {k("13 August")} to raise awareness about organ and tissue donation and honour donors and their families.'],
        None, None),
    ('Partition Horrors Remembrance Day — 14 August', 'hot', [
        f'Observed every year on {k("14 August")} in India.',
        'Remembers those who lost their lives, were forced from their homes, or suffered violence and displacement in the 1947 Partition.',
        f'The Government decided in {k("2021")} to observe the day.'],
        None, None),
]))

S.append(('Science, Space &amp; Awards', None, [
    ('Physicist Deepak Dhar Wins 2026 Dirac Medal', 'hot', [
        f'Indian theoretical physicist {k("Deepak Dhar")} is a co-recipient of the {k("2026 Dirac Medal")}.',
        f'Awarded by the {k("Abdus Salam International Centre for Theoretical Physics (ICTP)")}, {k("Trieste, Italy")}; first given in {k("1985")}.',
        f'Named after {k("Paul A. M. Dirac")}, who shared the {k("1933")} Physics Nobel with {k("Erwin Schrödinger")}.',
        f'Other recipients: {k("Bernard Derrida")}, {k("Marc Mezard")}, {k("Haim Sompolinsky")}.'],
        None,
        'ICTP is in <b>Trieste, Italy</b> (not Geneva). Medal since <b>1985</b>.'),
    ('NASA Invites ISRO to Join ‘Moon Base’ Programme', 'hot', [
        f'{k("NASA")} invited {k("ISRO")} to join its {k("Moon Base")} programme for a long-term human presence on the Moon, near the {k("lunar South Pole")}.',
        f'Invitation made at the {k("9th India–US Civil Space Joint Working Group")} meeting at {k("ISRO HQ, Bengaluru")}.',
        f'Part of NASA’s broader {k("Artemis")} programme: habitation, research infrastructure, communication and power systems.'],
        f'NASA — Est. {k("1958")} · HQ {k("Washington, D.C.")} · India signed the {k("Artemis Accords")} in {k("June 2023")}',
        None),
    ('Dr Padma Gurmet Honoured with UT Ladakh State Award 2025', None, [
        f'{k("Dr Padma Gurmet")}, Director of the {k("National Institute of Sowa-Rigpa (NISR), Leh")}, received the {k("UT Ladakh State Award 2025")}.',
        'Honoured for preserving, promoting and developing Sowa-Rigpa in Ladakh.',
        f'Presented by Ladakh LG {k("Vinai Kumar Saxena")}.',
        f'{k("Sowa-Rigpa")}: traditional medicine of the Himalayan region, also called the {k("Tibetan system of medicine")}.'],
        f'Sowa-Rigpa — Recognised as an AYUSH system in {k("2010")}',
        None),
]))

S.append(('Obituaries &amp; Books', None, [
    ('Historian Sumit Sarkar Passes Away at 87', None, [
        f'Eminent Marxist historian of modern India {k("Sumit Sarkar")} passed away at {k("87")}.',
        'Known for work on the national movement, colonial India and social history.',
        f'Books: {k("Swadeshi Movement in Bengal, 1903–1908")} (1973), {k("Modern India")} (1989), {k("Writing Social History")} (1998).'],
        None, None),
    ('Former Nuclear Scientist M. P. Parameswaran Passes Away', None, [
        f'{k("M. P. Parameswaran")}, former nuclear scientist, writer and people’s-science activist, passed away.',
        f'Worked at the {k("Bhabha Atomic Research Centre (BARC)")}, Mumbai.',
        f'Known for his {k("“Fourth World”")} theory, set out in “{k("Fourth World: Dream and Reality")}”.'],
        None, None),
    ('Former Chinese Premier Zhu Rongji Passes Away at 97', None, [
        f'{k("Zhu Rongji")}, Premier of China from {k("1998 to 2003")} under President {k("Jiang Zemin")}, died at 97.',
        f'Earlier: Vice-Premier, {k("Governor of the People’s Bank of China")}, and {k("Mayor of Shanghai")}.'],
        None, None),
    ('PM Modi Releases Ram Nath Kovind’s Autobiography', 'hot', [
        f'PM Narendra Modi released former President {k("Ram Nath Kovind")}’s autobiography, “{k("Triumph of the Indian Republic: My Life, My Struggles")}”.',
        f'Kovind was the {k("14th President")} of India ({k("2017–2022")}); succeeded {k("Pranab Mukherjee")}, succeeded by {k("Droupadi Murmu")}.'],
        f'Ram Nath Kovind — Earlier {k("Governor of Bihar")}',
        None),
]))

QUIZ = [
    ('SBI’s $500 million bond — type, branch, tenure and coupon?', 'Regulation S bond via London branch; 5 years at 5.25%'),
    ('Bank of America’s stake in Jio Credit — initial and maximum?', '26.5% initially, up to 49.9% (up to ₹18,268 crore)'),
    ('Up to what loan size did SBI use AI underwriting for MSMEs?', '₹5 crore per loan (≈ ₹1 lakh crore total in FY26)'),
    ('Which network is the EazyDiner IndusInd card on, and why does it matter?', 'RuPay — so it can be linked to UPI'),
    ('WPI inflation July 2026, base year and compiling office?', '9.78%; 2022-23; Office of the Economic Adviser, DPIIT'),
    ('CPI inflation July 2026, base year and number of items?', '4.45%; 2024 = 100; 358 items (308 goods + 50 services)'),
    ('Unemployment rate Apr–Jun 2026 and its survey?', '5.4% (from 5.0%); PLFS, MoSPI'),
    ('Who tops the Hurun-Barclays family list, and who leads first-generation families?', 'Ambani family (₹25.83 lakh cr); Adani family'),
    ('Where was CBDC-based DBT under PMGKAY launched on 14 Aug 2026?', 'Chandigarh and Dadra & Nagar Haveli'),
    ('PM E-DRIVE: ministry, new end date and max e-2W subsidy?', 'Ministry of Heavy Industries; 31 March 2028; ₹5,000 (₹2,500/kWh)'),
    ('Which Act was amended to protect Vande Mataram, and the max punishment?', 'Prevention of Insults to National Honour Act, 1971; 3 years'),
    ('Who allotted the 1601 number series?', 'Department of Telecommunications (DoT); TRAI is rolling it out'),
    ('India Post drone Tiranga route?', 'Mandi HO → Rehardhar BO, Himachal Pradesh'),
    ('Banner for GI products on ONDC and GeM?', '“Bharat GI”'),
    ('L&T AI factory — location, GPUs and client?', 'Vyoma’s Chennai campus; 10,000 NVIDIA B300; Together AI'),
    ('SraVaani supports how many languages, and from which dataset?', '65 (20 scheduled + 45 others); Project Vaani'),
    ('Asia’s first desert-themed night safari — where?', 'Deesa, Banaskantha district, Gujarat (₹542.14 crore)'),
    ('Only breeding place of the Black-necked Crane in India?', 'Changthang Cold Desert Wildlife Sanctuary, Ladakh'),
    ('New Chief Secretary of A&N Islands and his previous post?', 'Gyanesh Bharti; Deputy Election Commissioner'),
    ('First Arab country to abolish the death penalty?', 'Lebanon (first in the world for all crimes: Venezuela)'),
    ('Canadian Open 2026 singles winners?', 'Iga Swiatek (women, Toronto); Ben Shelton (men, Montreal)'),
    ('India’s medals and trophy at the Commonwealth Fencing Championship?', '35 (13-8-14); Wilkinson Sword Trophy; Lagos'),
    ('Who will co-develop the AMCA engine with Reliance?', 'Rolls-Royce (UK)'),
    ('Prachand fuselage split between BEML and Adani Defence?', 'BEML 48 + Adani 42 = 90'),
    ('INS Sudarshini’s port in Portugal, and Lokayan’s length?', 'Ponta Delgada, Azores; 10 months, 22,000 nm, 13 countries, 18 ports'),
    ('First woman to complete IAF’s Fighter Combat Leader course, and where?', 'Sqn Ldr Bhawana Kanth; TACDE Gwalior'),
    ('India–Malaysia exercises for Army, Navy and Air Force?', 'Harimau Shakti; Samudra Laksamana; Udara Shakti'),
    ('Where was the first BRICS FMCBG meeting under India’s 2026 Chairship?', 'Jaipur, Rajasthan'),
    ('Asiatic lion population (2025) and Project Lion announcement date?', '891; 15 August 2020'),
    ('Why is World Biofuel Day on 10 August?', 'Marks Rudolf Diesel’s peanut-oil engine run (9 Aug 1893); first observed 2015'),
    ('International Youth Day 2026 theme?', 'Different Contexts, Common Aspirations'),
    ('When was the elephant declared National Heritage Animal?', '22 October 2010'),
    ('Who awards the Dirac Medal, and where is it based?', 'ICTP, Trieste, Italy'),
    ('Where was NASA’s Moon Base invitation to ISRO made?', '9th India–US Civil Space JWG, ISRO HQ Bengaluru'),
    ('Title of Ram Nath Kovind’s autobiography?', 'Triumph of the Indian Republic: My Life, My Struggles'),
]

RAPID = [
    'SBI $500 mn Reg S bond (London, 5 yr, 5.25%) · BofA up to 49.9% of Jio Credit (26.5% first, ₹18,268 cr) · SBI AI MSME loans ≈ ₹1 lakh cr (≤ ₹5 cr each).',
    'EazyDiner IndusInd RuPay card, lifetime free, UPI-linked · SBI Life + J&K Bank corporate agency (1,000+ branches).',
    'WPI 9.78% (base 2022-23, 957 items, OEA/DPIIT) · CPI 4.45% (base 2024, 358 items, NSO/MoSPI) · Unemployment 5.4% (PLFS).',
    'Hurun-Barclays: Ambani No. 1 (3rd year, ₹25.83 lakh cr); first-gen: Adani → Mittal → Shanghvi.',
    'CBDC DBT under PMGKAY: Chandigarh + DNH (14 Aug) · PM E-DRIVE to 31 Mar 2028, ₹11,900 cr, e-2W ₹2,500/kWh max ₹5,000.',
    'Vande Mataram protected like Jana Gana Mana (1971 Act; 3 yrs) · TRAI 1601 series (DoT-allotted, no promos) · India Post drone Tiranga, Mandi.',
    'BHASHINI + NITI Aayog SoI · MakeMyTrip + Tourism 350 tours, 60 cities · MSME + DPIIT GI MoU — “Bharat GI” on ONDC/GeM.',
    'L&T AI factory: 10,000 NVIDIA B300, Chennai, for Together AI · Meta Muse Glimmer · IISc SraVaani 65 languages (Project Vaani).',
    'Deesa (Gujarat) desert night safari, CZA 1992 · Ladakh Black-necked Crane fest (Changthang) · 5 peacocks to UNOG.',
    'Gyanesh Bharti CS of A&N · Bhooma VG VC of AIPSI Mauritius · Krithi Shetty for Indriya · 3 ITU youth envoys · András Baka President of Hungary.',
    'Lebanon first Arab country to end death penalty · Côte d’Ivoire 66th I-Day (7 Aug) · BRICS FMCBG Jaipur.',
    'Swiatek (Toronto) + Shelton (Montreal) · India Commonwealth Fencing champion, 35 medals, Wilkinson Sword (Lagos) · TTFI suspended.',
    'Reliance + Rolls-Royce AMCA engine · Prachand fuselages BEML 48 + Adani 42 · ₹1,577 cr loitering munitions (TASL, NIBE).',
    'INS Sudarshini at Azores (Lokayan) · GRSE NGOPV Shruti · Bhawana Kanth FCL course (TACDE Gwalior) · Udara Shakti (Subang) · EOD 8th ed. Kochi.',
    'Days: 10 Aug Lion + Biofuel · 12 Aug Youth + Elephant · 13 Aug Organ Donation · 14 Aug Partition Horrors.',
    'Deepak Dhar Dirac Medal (ICTP Trieste) · NASA invites ISRO to Moon Base · Padma Gurmet Ladakh award (Sowa-Rigpa).',
    'Died: Sumit Sarkar (87), M. P. Parameswaran, Zhu Rongji (97) · Book: Kovind — “Triumph of the Indian Republic”.',
]

# Memory-aid pictures taken from the class PDF itself: 'pdf:pPAGE_INDEX|caption' (see pdf_images.py)
IMG = {
    'SBI Raises': 'pdf:p01_04|SBI',
    'Jio Credit': 'pdf:p01_01|Jio Finance × Bank of America',
    'SBI Uses AI': 'pdf:p02_04|SBI',
    'EazyDiner': 'pdf:p02_03|EazyDiner IndusInd RuPay card',
    'SBI Life Insurance Ties': 'pdf:p02_01|SBI Life × J&amp;K Bank',
    'WPI Inflation': 'pdf:p02_06|Wholesale market',
    'Retail Inflation': 'pdf:p03_01|Retail prices',
    'Unemployment': 'pdf:p03_02|Unemployment',
    'Ambani Family': 'pdf:p04_03|Ambani family',
    'CBDC-Based DBT': 'pdf:p04_01|Digital Rupee',
    'PM E-DRIVE': 'pdf:p05_02|Electric two-wheelers',
    'Vande Mataram': 'pdf:p06_01|Vande Mataram',
    'TRAI Begins': 'pdf:p07_01|TRAI',
    'Tiranga by Drone': 'pdf:p06_06|Tiranga by drone',
    'BHASHINI': 'pdf:p06_04|BHASHINI × NITI Aayog',
    'MakeMyTrip': 'pdf:p15_05|MakeMyTrip',
    'GI Products': 'pdf:p15_01|GI handicraft',
    'NVIDIA B300': 'pdf:p03_05|AI data centre',
    'Muse Glimmer': 'pdf:p04_04|Meta AI',
    'SraVaani': 'pdf:p13_01|Multilingual speech AI',
    'Deesa': 'pdf:p05_01|Night safari',
    'Black-Necked Crane': 'pdf:p14_03|Black-necked cranes',
    'Peacocks': 'pdf:p14_02|Indian peafowl',
    'Bhooma VG': 'pdf:p08_04|Dr Bhooma VG',
    'Krithi Shetty': 'pdf:p08_03|Indriya',
    'Youth Envoys': 'pdf:p08_02|ITU Youth Envoys',
    'András Baka': 'pdf:p09_03|András Baka',
    'Lebanon': 'pdf:p07_03|Death penalty abolished',
    'Côte d’Ivoire': 'pdf:p10_05|Côte d’Ivoire celebrations',
    'BRICS': 'pdf:p12_03|BRICS',
    'Canadian Open': 'pdf:p09_07|Iga Swiatek',
    'Commonwealth Fencing': 'pdf:p09_02|Commonwealth Fencing, Lagos',
    'TTFI': 'pdf:p09_01|Table tennis',
    'AMCA': 'pdf:p10_04|AMCA model',
    'Prachand': 'pdf:p10_01|LCH Prachand',
    'Loitering': 'pdf:p10_06|Loitering munition',
    'Sudarshini': 'pdf:p11_04|INS Sudarshini',
    'Shruti': 'pdf:p11_03|NGOPV Shruti',
    'Bhawana Kanth': 'pdf:p11_02|Sqn Ldr Bhawana Kanth',
    'Udara Shakti': 'pdf:p11_01|Udara Shakti 2026',
    'EOD Exercise': 'pdf:p12_05|EOD exercise, Kochi',
    'World Lion Day': 'pdf:p12_02|World Lion Day',
    'World Biofuel Day': 'pdf:p12_01|World Biofuel Day',
    'International Youth Day': 'pdf:p13_08|International Youth Day',
    'World Elephant Day': 'pdf:p13_06|Asian elephants',
    'Organ Donation': 'pdf:p13_02|World Organ Donation Day',
    'Partition Horrors': 'pdf:p13_07|Partition Horrors Remembrance Day',
    'Deepak Dhar': 'pdf:p14_01|Deepak Dhar',
    'Moon Base': 'pdf:p15_02|Moon Base',
    'Padma Gurmet': 'pdf:p14_06|Dr Padma Gurmet',
    'Zhu Rongji': 'pdf:p16_04|Zhu Rongji',
    'Kovind': 'pdf:p16_01|Ram Nath Kovind with PM Modi',
}
