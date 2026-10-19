# August 2026 · Class 4 — source: Class_04_August_2026_Monthly_Current_Affairs_by_Ashish_Gautam_Sir.pdf
# News content kept as in the PDF (English half, pages 1-7); Static GK boxes and exam traps added on top.
# NSDC facts are from the PDF's Hindi half (the English box is an image); the book's author is from its cover in the PDF.
# Pictures come from the PDF itself (IMG values 'pdf:…', see pdf_images.py).
# Each section: (title, intro, [items]); item = (headline, tag, [facts], gk, trap). k('x') marks a key fact.
S = []

S.append(('Banking, Payments &amp; Insurance', None, [
    ('UPI Payments to Remain Free for Users', 'bank', [
        f'Central Government clarified that users will {k("not be charged")} for UPI payments, amid concerns over the proposed amendment to the {k("Payment and Settlement Systems Act, 2007")}.',
        f'All {k("Person-to-Person (P2P)")} UPI transactions will remain completely free; no charge on normal everyday UPI transactions by citizens.',
        f'If a {k("Merchant Discount Rate (MDR)")} is introduced in future, it will apply only to a {k("limited category of merchant transactions")}, only {k("above a specified threshold")}, at a {k("nominal rate")}, and well below the MDR on debit and credit cards.',
        f'The {k("Taxation and Other Laws (Amendment) Bill, 2026")} proposes to amend {k("Section 10A")} of the PSS Act, 2007.'],
        f'UPI — Launched {k("2016")} · Operated by {k("NPCI")} (National Payments Corporation of India, est. {k("2008")}, HQ {k("Mumbai")}) · MDR = the fee a merchant pays its bank for accepting digital payments',
        'MDR is paid by the <b>merchant</b>, never by the customer. The amendment is to <b>Section 10A</b> of the <b>PSS Act, 2007</b>, through the Taxation and Other Laws (Amendment) Bill, 2026.'),
    ('Bajaj General Insurance Signs MoU with Swiss Re Corporate Solutions', 'bank', [
        f'{k("Bajaj General Insurance")} signed an MoU with {k("Swiss Re Corporate Solutions")} to explore a {k("commercial insurance partnership")} in India.',
        'Commercial insurance protects businesses against risks such as fire and property damage, machinery breakdown, cyber attacks, marine risks, liability claims and business interruption.'],
        f'Bajaj General Insurance — Formerly {k("Bajaj Allianz General Insurance")} · HQ {k("Pune, Maharashtra")} · Swiss Re is a reinsurer headquartered in {k("Zurich, Switzerland")}',
        None),
]))

S.append(('Sports', None, [
    ('Ashmita Chaliha Wins Korea Masters 2026', 'hot', [
        f'Indian shuttler {k("Ashmita Chaliha")} won the {k("women’s singles")} title at the {k("Korea Masters 2026")} — her {k("maiden BWF World Tour title")}.',
        f'She became the {k("first Indian")} to win the Korea Masters women’s singles title.',
        f'Runner-up: {k("Han Qian Xi (China)")}. She is from {k("Assam")}.'],
        f'Badminton World Federation (BWF) — HQ {k("Kuala Lumpur, Malaysia")}',
        'Two “firsts” in one item: her <b>first BWF World Tour title</b>, and the <b>first Indian</b> to win the Korea Masters women’s singles.'),
    ('R. Praggnanandhaa Wins St. Louis Rapid &amp; Blitz Title', 'hot', [
        f'Indian Grandmaster {k("R. Praggnanandhaa")} won the {k("Grand Chess Tour St. Louis Rapid and Blitz")} title in the {k("United States")}.',
        f'He secured it after drawing against Uzbekistan’s GM {k("Javokhir Sindarov")} in the penultimate round.',
        f'Earlier, in {k("June 2026")}, he won {k("Norway Chess 2026")} in {k("Oslo")}.'],
        f'R. Praggnanandhaa — From {k("Chennai, Tamil Nadu")} · FIDE (world chess body) HQ: {k("Lausanne, Switzerland")}',
        'St. Louis is in the <b>USA</b>; Norway Chess was in <b>Oslo</b> (June). The decisive draw was against <b>Sindarov</b> (Uzbekistan).'),
    ('Mohammed Ashfaq Breaks Under-20 National Record at World Athletics Championships', None, [
        f'{k("Mohammed Ashfaq")} broke the {k("Under-20 National Record")} in the men’s {k("400 metres")} at the {k("World Athletics U20 Championships")} in {k("Eugene, United States")}.',
        f'He clocked {k("45.81 seconds")} in the first-round Heat 5, improving his own previous record of {k("46.05 seconds")}.'],
        None,
        'He broke <b>his own</b> record: 46.05 → <b>45.81</b> s. Venue <b>Eugene</b> (USA).'),
    ('John Turner Has Announced His Retirement from Professional Cricket', None, [
        f'England pacer {k("John Turner")} announced his retirement from professional cricket.'],
        None, None),
]))

S.append(('Defence', None, [
    ('France Submits Proposal for 114 Rafale Fighter Jets', 'hot', [
        f'France submitted a detailed technical and commercial proposal to India for {k("114 Rafale fighter aircraft")} for the {k("Indian Air Force")}.',
        f'Estimated deal value: around {k("₹3.25 lakh crore")}.',
        f'Submitted in response to India’s {k("Letter of Request (LoR)")} issued in {k("May 2026")}.',
        f'Proposal: {k("20 jets")} supplied directly in {k("fly-away condition")}; {k("94 jets manufactured in India")}.',
        f'India’s earlier {k("36 Rafales")} for the IAF came in fly-away condition; India has also ordered {k("26 Rafale-Marine")} aircraft for the {k("Indian Navy")}.'],
        f'Rafale — Twin-engine multirole fighter made by {k("Dassault Aviation")} (France) · The 36-jet deal was signed in {k("2016")} · Rafale-M are meant for carrier {k("INS Vikrant")}',
        'Split the numbers: <b>114 = 20 fly-away + 94 made in India</b>. Earlier: <b>36</b> (IAF) and <b>26 Rafale-M</b> (Navy).'),
    ('India Successfully Test-Fires Agni-4 Ballistic Missile', 'hot', [
        f'India successfully test-fired {k("Agni-4")} from the {k("Integrated Test Range (ITR), Chandipur, Odisha")}.',
        f'An indigenously developed {k("surface-to-surface ballistic missile")} with a strike range of up to {k("4,000 km")}.'],
        f'Agni series — Developed by {k("DRDO")} · Agni-5 range {k("5,000 km+")}; Agni-Prime is the new-generation version',
        'Agni-<b>4</b> = <b>4,000 km</b> (easy pairing). Test site: ITR <b>Chandipur</b>, Odisha.'),
    ('HAL Introduces India’s First Satellite-Guided Helicopter Navigation System', None, [
        f'{k("HAL")} introduced India’s {k("first satellite-guided precision navigation system for helicopters")} at its airport in {k("Bengaluru")}.',
        f'Called {k("Required Navigation Performance – Category H (RNP CAT H)")}.',
        'Designed for faster, more precise landing and take-off of helicopters.',
        f'The procedure was developed by the {k("Airports Authority of India (AAI)")}.',
        f'HAL — Founded: {k("22 December 1940")} · HQ: {k("Bengaluru, Karnataka")} · Ministry of Defence.'],
        None,
        'System from <b>HAL</b>, but the procedure was developed by <b>AAI</b>. “H” in RNP CAT H = <b>Helicopter</b>.'),
]))

S.append(('Culture &amp; Media', None, [
    ('India to Host First Global South Film Festival', 'hot', [
        f'India will host the {k("first Global South Film Festival")} in {k("2027")}.',
        f'Announced on the sidelines of the {k("BRICS WAVES Bazaar in Mumbai")}.',
        f'{k("NFDC")} and the {k("National Film Archive of India (NFAI)")} were among the organisations that signed agreements.',
        f'NFDC — Ministry of {k("Information and Broadcasting")} · Founded {k("1975")} · HQ {k("Mumbai, Maharashtra")}.'],
        f'NFAI — Located in {k("Pune")} · WAVES = World Audio Visual &amp; Entertainment Summit (first held in {k("Mumbai, 2025")})',
        None),
]))

S.append(('Important Days &amp; Anniversaries', None, [
    ('Seventh Anniversary of Abrogation of Article 370 Observed on 5 August', 'hot', [
        f'India marks {k("seven years")} since the provisions of {k("Article 370")}, which gave special status to the erstwhile State of {k("Jammu and Kashmir")}, were made inoperative in August 2019.',
        f'The process began on {k("5 August 2019")} (Presidential Order and resolution introduced in Parliament); Parliament completed approval on {k("6 August 2019")}.',
        f'So {k("5 August")} is generally observed as the anniversary.'],
        f'J&amp;K Reorganisation Act, 2019 — Created two UTs, {k("Jammu &amp; Kashmir")} (with legislature) and {k("Ladakh")} (without), from {k("31 October 2019")} · Supreme Court upheld the abrogation on {k("11 December 2023")}',
        'Introduced <b>5 Aug 2019</b>, approved <b>6 Aug 2019</b>; the UTs came into being on <b>31 Oct 2019</b>. 2026 = <b>7th</b> anniversary.'),
    ('World Marks 81 Years since US Dropped Atomic Bomb on Japan', None, [
        f'{k("Hiroshima Day")} is observed on {k("6 August")} for the 1945 atomic bombing of Hiroshima.',
        f'On {k("6 and 9 August 1945")} the US detonated two atomic bombs over {k("Hiroshima and Nagasaki")} during World War II.',
        f'{k("“Little Boy”")} — enriched {k("uranium")}, gun-type; {k("“Fat Man”")} — {k("plutonium")}, implosion-type.',
        f'A US {k("B-29 bomber")} dropped “Little Boy” on 6 August 1945.'],
        f'Bombers — “Little Boy” was dropped by the B-29 {k("Enola Gay")} (Hiroshima); “Fat Man” by {k("Bockscar")} (Nagasaki)',
        '<b>L</b>ittle Boy = <b>U</b>ranium = Hiroshima (6 Aug). Fat Man = Plutonium (<b>Pu</b>) = Nagasaki (9 Aug).'),
    ('Nagasaki Marks 81st Anniversary of Atomic Bombing', None, [
        f'Nagasaki marked the {k("81st anniversary")} of the US atomic bombing on {k("9 August 2026")}.',
        f'The annual {k("Peace Memorial Ceremony")} was held at the {k("Peace Park")} in Nagasaki.',
        'The bombing came three days after Hiroshima (6 August 1945).',
        f'Japan announced its surrender on {k("15 August 1945")}, ending World War II in Asia.'],
        None, None),
    ('International Day of Awareness of the Special Development Needs and Challenges of Landlocked Developing Countries — 6 August', None, [
        f'The {k("United Nations")} observes {k("6 August")} every year for the special needs and challenges of {k("Landlocked Developing Countries (LLDCs)")}.',
        'A landlocked country has no direct coastline or access to an ocean or sea.'],
        f'LLDCs — The UN group has {k("32")} landlocked developing countries · India’s landlocked neighbours: {k("Nepal, Bhutan")} (also Afghanistan)',
        'Same date as <b>Hiroshima Day (6 Aug)</b> — don’t mix them up.'),
    ('India Observes 12th National Handloom Day', 'hot', [
        f'{k("National Handloom Day")} is celebrated every year on {k("7 August")}, since {k("2015")}, to honour handloom weavers and textile traditions.',
        f'2026 marks the {k("12th")} National Handloom Day.',
        f'On {k("7 August 1905")} the {k("Swadeshi Movement")} was formally launched at {k("Calcutta Town Hall")} against the Partition of Bengal.'],
        f'First National Handloom Day — Inaugurated by PM Narendra Modi in {k("Chennai")}, 2015 · Ministry of {k("Textiles")}',
        'Date chosen to mark the <b>Swadeshi Movement</b> (7 Aug 1905). 2015 = 1st, so 2026 = <b>12th</b>.'),
    ('National Javelin Day Is Observed Every Year on 7 August', 'hot', [
        f'Commemorates {k("Neeraj Chopra")}’s gold in the men’s javelin throw at the {k("Tokyo Olympics 2020")}, and promotes the sport.',
        f'2026 marks the {k("5th")} National Javelin Day.',
        f'Declared by the {k("Athletics Federation of India (AFI)")} in {k("2021")}.'],
        f'Neeraj Chopra — Tokyo gold throw {k("87.58 m")} on {k("7 August 2021")} · India’s first Olympic gold in {k("athletics")}',
        'Same date (7 Aug) as <b>National Handloom Day</b>. Declared by <b>AFI</b> (not the Sports Ministry).'),
    ('International Day of the World’s Indigenous Peoples Is Observed on 9 August', None, [
        f'Observed every year on {k("9 August")} to raise awareness about the rights, cultures and challenges of Indigenous Peoples.',
        f'Theme 2026: “{k("Honouring Indigenous Midwives: Safeguarding Life and Well-being")}”.'],
        f'Origin — Declared by the {k("UN General Assembly in 1994")}; the date marks the first meeting of the UN Working Group on Indigenous Populations (1982)',
        None),
]))

S.append(('Health, Science &amp; Space', None, [
    ('IPC Recognised as WHO-SEARN Regional Centre of Excellence', 'hot', [
        f'The {k("Indian Pharmacopoeia Commission (IPC)")} took part in the {k("10th Anniversary Meeting")} of the {k("South-East Asia Regulatory Network (SEARN)")} in {k("Kathmandu, Nepal")}.',
        f'IPC received two recognitions: {k("WHO-SEARN Regional Centre of Excellence in Pharmacovigilance")} and {k("WHO-SEARN Technical Centre in Quality")}.',
        'It establishes IPC as an important regional institution for the quality and safety of medicines across South-East Asia.'],
        f'IPC — Autonomous body under the {k("Ministry of Health and Family Welfare")} · HQ {k("Ghaziabad, Uttar Pradesh")} · Publishes the {k("Indian Pharmacopoeia")} and runs the Pharmacovigilance Programme of India',
        'Two titles: <b>Centre of Excellence</b> = Pharmacovigilance; <b>Technical Centre</b> = Quality. Meeting in <b>Kathmandu</b>.'),
    ('IIA Director Wins COSPAR Vikram Sarabhai Medal', 'hot', [
        f'{k("Annapurni Subramaniam")}, Director of the {k("Indian Institute of Astrophysics (IIA)")}, received the {k("COSPAR Vikram Sarabhai Medal 2026")}.',
        f'Presented at the {k("46th COSPAR General Assembly")} in {k("Florence, Italy")}.',
        f'She is the {k("first Indian woman")} and the {k("fourth Indian")} to receive it. Previous Indian winners: {k("U R Rao (1996)")}, {k("Gurbax Singh Lakhina (2014)")}, {k("Anil Bhardwaj (2024)")}.',
        f'Recognises outstanding contributions to space research in {k("developing countries")}; awarded {k("jointly by ISRO and COSPAR")}, {k("once every two years")}, in honour of {k("Vikram Sarabhai")}, Father of the Indian Space Programme.'],
        f'COSPAR — {k("Committee on Space Research")}, set up in {k("1958")} · HQ {k("Paris")} · IIA is in {k("Bengaluru")}',
        'She is the <b>4th Indian</b> but the <b>1st Indian woman</b>. The medal is <b>biennial</b> and joint <b>ISRO–COSPAR</b>.'),
    ('SpaceX Falcon 9 Upper Stage Crashes into the Moon', None, [
        f'A discarded {k("second stage")} of a {k("SpaceX Falcon 9")} rocket crashed into the Moon on {k("5 August 2026")}.',
        f'{k("NASA’s JPL")} had tracked the object, designated {k("2025-010D")}, and predicted the impact.',
        f'The Falcon 9 was launched on {k("15 January 2025")} carrying two commercial lunar landers: {k("Blue Ghost Mission 1 (Firefly Aerospace)")} and {k("Hakuto-R Mission 2 / Resilience (ispace)")}.',
        'After deploying the landers, the upper stage stayed in space until its orbit led it to the Moon.'],
        f'JPL — {k("Jet Propulsion Laboratory")}, NASA centre in {k("Pasadena, California")} · ispace is a {k("Japanese")} company',
        None),
    ('Astrobase Unveils India’s First Private Reusable Rocket Engine Technology', 'hot', [
        f'Bengaluru-based {k("Astrobase Space Technologies")} unveiled India’s {k("first privately built 800 kN rocket engine")} — India’s first private reusable rocket engine technology.',
        f'The engine is named {k("EVEREST")}; it is a {k("Full-Flow Staged Combustion (FFSC)")} engine.',
        f'Astrobase says it is the {k("fourth commercial company globally")} to develop a high-thrust FFSC engine.'],
        f'IN-SPACe — {k("Indian National Space Promotion and Authorisation Centre")}, the single-window regulator for private space companies (HQ {k("Ahmedabad")})',
        'Engine name <b>EVEREST</b>, thrust <b>800 kN</b>, cycle <b>FFSC</b>; company <b>Astrobase</b> (Bengaluru).'),
]))

S.append(('Education &amp; Skills', None, [
    ('IIT Madras Global Partners with Indonesia for Higher Education and Deep-Tech Cooperation', None, [
        f'Indonesia’s {k("Ministry of Higher Education, Science and Technology")} has partnered with {k("IIT Madras Global Research Foundation (IITM Global)")}.',
        'Focus areas: higher education, research and innovation, deep technology, entrepreneurship and talent development.'],
        f'Indonesia — Capital {k("Jakarta")} (new capital {k("Nusantara")} being built) · Currency {k("Rupiah")} · President {k("Prabowo Subianto")}',
        None),
    ('IIT Hyderabad Launched ANUGYAN Nuclear Technology Training Programme', 'hot', [
        f'{k("IIT Hyderabad")}, with {k("Crimson Energy Experts Pvt. Ltd. (CEEPL)")}, launched {k("ANUGYAN – Nuclear Technology Orientation Programme (NTOP)")}.',
        f'Described as India’s {k("first industry–academia residential programme")} for the {k("civil nuclear energy")} sector.',
        f'Part of an MoU between IIT Hyderabad, {k("Dassault Systèmes")} and Crimson Energy Experts, signed at {k("Bharat Innovate 2026 in Nice, France")}, for a {k("Centre of Design Excellence in Nuclear Engineering")}.',
        f'Supports India’s vision of about {k("100 GWe nuclear capacity by 2047")}, up from about {k("8.8 GWe")} now.'],
        None,
        'Nuclear target: <b>100 GWe by 2047</b> (from ~<b>8.8 GWe</b>). MoU signed in <b>Nice, France</b>.'),
    ('NSDC Partners with AVPL International to Set Up 350 Drone Skill Centres across India', 'hot', [
        f'The {k("National Skill Development Corporation (NSDC)")} partnered with {k("AVPL International")} to set up {k("350 Advanced Skill Centres for Drone Technology")} over the {k("next three years")}.',
        'Aims to build a future-ready workforce through industry-oriented training in drone and allied technologies.',
        f'Rollout begins with {k("75 centres in the first year")}, in private universities and engineering colleges.',
        f'NSDC — Established {k("2008")} by the {k("Ministry of Finance")} as a {k("Public-Private Partnership")} · HQ {k("New Delhi")} · Government holds {k("49%")} (through the Ministry of Skill Development and Entrepreneurship); the private sector holds {k("51%")}.'],
        None,
        '<b>350</b> centres in 3 years, <b>75</b> in year one. NSDC is <b>51% private</b>, 49% government.'),
]))

S.append(('Aviation', None, [
    ('Pawan Hans Partners with Norway’s Noemi Aerospace for Electric Seaplanes', None, [
        f'Government-owned helicopter operator {k("Pawan Hans Limited")} signed an MoU with Norway-based {k("Noemi Aerospace")} (formerly {k("Elfly AS")}) on sustainable aviation and {k("electric seaplane")} technology.',
        f'Signed in the presence of Union Civil Aviation Minister {k("Kinjarapu Ram Mohan Naidu")}.',
        f'Pawan Hans — {k("Mini Ratna-I")} PSU under the {k("Ministry of Civil Aviation")} · Founded {k("15 October 1985")} · HQ {k("Noida, Uttar Pradesh")}.'],
        None,
        'Partner is <b>Norwegian</b> (Noemi, ex-Elfly); Pawan Hans HQ is <b>Noida</b>, not Delhi.'),
]))

S.append(('Books', None, [
    ('Book: Bringing the Cheetah Back to India', None, [
        f'Book “{k("Bringing the Cheetah Back to India")}” — subtitle “How Diplomacy Made Conservation’s Big Mission Possible”.',
        f'Author: {k("Prashant Agrawal")} (as shown on the cover in the PDF).'],
        f'Project Cheetah — Launched {k("17 September 2022")} at {k("Kuno National Park, Madhya Pradesh")} · First cheetahs from {k("Namibia")}, then {k("South Africa")} · World’s first intercontinental large-carnivore translocation',
        None),
]))

QUIZ = [
    ('Which Act’s Section 10A is proposed to be amended, and by which Bill?', 'PSS Act, 2007; Taxation and Other Laws (Amendment) Bill, 2026'),
    ('Will P2P UPI payments be charged?', 'No — P2P and everyday UPI stay free; any MDR only for some merchant payments above a threshold'),
    ('Korea Masters 2026 women’s singles winner and her state?', 'Ashmita Chaliha; Assam (beat Han Qian Xi)'),
    ('Praggnanandhaa’s two 2026 titles?', 'GCT St. Louis Rapid & Blitz (USA); Norway Chess (Oslo, June)'),
    ('Mohammed Ashfaq’s new U20 400 m national record?', '45.81 s (was 46.05 s), Eugene'),
    ('Rafale proposal: total jets and the split?', '114 = 20 fly-away + 94 made in India; ~₹3.25 lakh crore'),
    ('Agni-4 range and test site?', '4,000 km; ITR Chandipur, Odisha'),
    ('HAL’s helicopter navigation system name, and who developed the procedure?', 'RNP CAT H; AAI'),
    ('First Global South Film Festival — host and year?', 'India, 2027 (announced at BRICS WAVES Bazaar, Mumbai)'),
    ('Why is 5 August observed for Article 370?', 'The Presidential Order and resolution were introduced on 5 Aug 2019'),
    ('“Little Boy” vs “Fat Man”?', 'Little Boy = uranium gun-type (Hiroshima); Fat Man = plutonium implosion (Nagasaki)'),
    ('National Handloom Day — date, since when, and what it marks?', '7 August, since 2015; Swadeshi Movement 1905'),
    ('Who declared National Javelin Day, and which edition is 2026?', 'AFI (2021); 5th'),
    ('Theme 2026 of International Day of the World’s Indigenous Peoples?', 'Honouring Indigenous Midwives: Safeguarding Life and Well-being'),
    ('IPC’s two WHO-SEARN recognitions?', 'Regional Centre of Excellence in Pharmacovigilance; Technical Centre in Quality'),
    ('First Indian woman to win the COSPAR Vikram Sarabhai Medal?', 'Annapurni Subramaniam (IIA Director), 4th Indian'),
    ('Name and type of Astrobase’s engine?', 'EVEREST; 800 kN Full-Flow Staged Combustion'),
    ('What is ANUGYAN?', 'IIT Hyderabad + CEEPL nuclear technology orientation programme'),
    ('NSDC–AVPL drone centres: total and first year?', '350 in 3 years; 75 in year one'),
    ('Pawan Hans’ electric-seaplane partner?', 'Noemi Aerospace (Norway), formerly Elfly AS'),
    ('Author of “Bringing the Cheetah Back to India”?', 'Prashant Agrawal'),
]

RAPID = [
    'UPI P2P stays free · MDR only for some merchants above a threshold · PSS Act 2007 Sec 10A (Taxation & Other Laws Bill 2026).',
    'Bajaj General Insurance + Swiss Re Corporate Solutions (commercial insurance MoU).',
    'Ashmita Chaliha (Assam): Korea Masters, first Indian winner · Pragg: St. Louis R&B + Norway Chess · Ashfaq 45.81 s U20 400 m · John Turner retires.',
    'Rafale 114 = 20 fly-away + 94 in India, ₹3.25 lakh cr · Agni-4 4,000 km, Chandipur · HAL RNP CAT H (AAI procedure).',
    'Global South Film Festival 2027 (India) · NFDC 1975, Mumbai.',
    'Days: 5 Aug Art. 370 (7 yrs) · 6 Aug Hiroshima + LLDCs · 7 Aug Handloom (12th) + Javelin (5th) · 9 Aug Nagasaki + Indigenous Peoples.',
    'IPC: WHO-SEARN CoE Pharmacovigilance + Technical Centre Quality (Kathmandu).',
    'COSPAR Vikram Sarabhai Medal: Annapurni Subramaniam (1st woman, 4th Indian) · Falcon 9 stage hits Moon 5 Aug.',
    'Astrobase EVEREST 800 kN FFSC · IITM Global + Indonesia · ANUGYAN (IIT-H) · NSDC + AVPL 350 drone centres.',
    'Pawan Hans + Noemi Aerospace (Norway) e-seaplanes · Book: Bringing the Cheetah Back to India — Prashant Agrawal.',
]

# Memory-aid pictures taken from the class PDF itself: 'pdf:pPAGE_INDEX|caption' (see pdf_images.py)
IMG = {
    'UPI Payments': 'pdf:p01_03|UPI',
    'Bajaj General': 'pdf:p07_07|Swiss Re × Bajaj General',
    'Ashmita Chaliha': 'pdf:p01_01|Ashmita Chaliha',
    'Praggnanandhaa': 'pdf:p02_03|R. Praggnanandhaa',
    'Mohammed Ashfaq': 'pdf:p02_04|Mohammed Ashfaq',
    'John Turner': 'pdf:p02_02|John Turner',
    'Rafale': 'pdf:p02_01|Rafale',
    'Agni-4': 'pdf:p03_02|Agni-4 launch',
    'HAL Introduces': 'pdf:p03_04|HAL helicopter',
    'Global South Film': 'pdf:p03_03|BRICS WAVES Bazaar',
    'Article 370': 'pdf:p03_01|Article 370',
    'World Marks 81 Years': 'pdf:p04_03|Hiroshima Peace Memorial',
    'Nagasaki Marks': 'pdf:p05_05|Nagasaki Peace Park',
    'Landlocked': 'pdf:p04_02|Landlocked countries',
    'Handloom Day': 'pdf:p04_01|Handloom',
    'Javelin Day': 'pdf:p04_04|National Javelin Day',
    'Indigenous Peoples': 'pdf:p05_03|Indigenous Peoples',
    'IPC Recognised': 'pdf:p05_02|WHO',
    'COSPAR': 'pdf:p05_04|Annapurni Subramaniam',
    'Falcon 9': 'pdf:p05_01|Falcon 9 launch',
    'Astrobase': 'pdf:p06_02|EVEREST engine',
    'IIT Madras Global': 'pdf:p06_01|India–Indonesia partnership',
    'ANUGYAN': 'pdf:p06_04|ANUGYAN',
    'NSDC Partners': 'pdf:p07_05|NSDC',
    'Pawan Hans': 'pdf:p07_01|Electric seaplane',
    'Cheetah': 'pdf:p07_03|Book cover',
}
