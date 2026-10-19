# Saarthi Alpha · Class 5 — from the class PDF (102250_4832496_lc.doc.pdf, 60 slides, all images).
CLASS = 5
TITLE = 'Types of Banks & All India Financial Institutions'
FULL = 'Types of Banks – Scheduled Commercial Banks, PSBs, private, foreign, RRBs, SFBs, Payments Banks, Local Area Banks, Co-operative Banks, Land Development Banks; All India Financial Institutions – NABARD, NHB, SIDBI, EXIM Bank, NaBFID; IFCI'
COVERS = 'Types of Banks + AIFIs (NABARD, NHB, SIDBI, EXIM, NaBFID) and IFCI – the planned Class 4 topic, not “All about RBI”'
NOTE = ('The class plan lists “All about RBI” for Class 5, but this PDF covers <b>Types of Banks</b> and the <b>All India Financial Institutions</b> '
        '(the AIFI topic planned for Class 4). RBI should come in the next PDF.')

S = [
 ('Types of Banks', 'बैंकों के प्रकार – the four families, then each kind of commercial bank.', [
  dict(h='Four types of banks', tag='hot', pics=[('c5-types-banks', 'Types of banks')], facts=[
     '1. ' + k('Central Bank (RBI)') + ' – केंद्रीय बैंक',
     '2. ' + k('Commercial Bank') + ' – वाणिज्यिक बैंक',
     '3. ' + k('Specialised Bank') + ' – विशिष्ट बैंक (e.g. EXIM Bank, NABARD, SIDBI, NHB)',
     '4. ' + k('Co-operative Bank') + ' – सहकारी बैंक',
  ]),
  dict(h='Scheduled Commercial Bank (SCB)', hi='अनुसूचित वाणिज्यिक बैंक', tag='hot', facts=[
     'Scheduled commercial banks are banks included in the ' + k('Second Schedule of the RBI Act, 1934') + ' that carry out the normal business of banking – accepting deposits, giving loans and other banking services.',
     'To be included in this Schedule, a bank must satisfy the conditions in ' + k('Section 42(6)(a) of the RBI Act') + '.',
     'Every SCB gets two main facilities: ' + k('eligibility to borrow from the RBI') + ', and ' + k('automatic membership of the clearing house') + ', which allows cheque clearing.',
     'SCBs include: ' + k('Public Sector Banks, Private Sector Banks, Foreign Banks, Regional Rural Banks (RRBs), Scheduled Payments Banks, Scheduled Small Finance Banks and Scheduled Co-operative Banks') + '.',
  ], add=[
     'Section 42(6)(a) asks for paid-up capital and reserves of at least <b>₹5 lakh</b>, and that the bank’s affairs are not run against depositors’ interests. A scheduled bank must keep its CRR with RBI (Section 42(1)).',
     'A bank <b>not</b> in the Second Schedule is a <b>non-scheduled bank</b> (e.g. some Local Area Banks).',
  ]),
  dict(h='Public Sector Bank', hi='सार्वजनिक क्षेत्र का बैंक', tag='bank', facts=[
     'Public Sector Banks are owned (' + k('majority stake of 51% or more') + ') by the ' + k('Government of India') + '.',
     'They are established under the ' + k('State Bank of India Act, 1955') + ' and the ' + k('Banking Companies (Acquisition and Transfer of Undertakings) Acts of 1970 & 1980') + '.',
  ]),
  dict(h='The 12 Public Sector Banks', table=(['No.', 'Bank', 'No.', 'Bank'], [
     ['1', 'Bank of Baroda', '7', 'Indian Overseas Bank'],
     ['2', 'Bank of India', '8', 'Punjab & Sind Bank'],
     ['3', 'Bank of Maharashtra', '9', 'Punjab National Bank'],
     ['4', 'Canara Bank', '10', 'State Bank of India'],
     ['5', 'Central Bank of India', '11', 'UCO Bank'],
     ['6', 'Indian Bank', '12', 'Union Bank of India'],
  ]), facts=['There are ' + k('12 Public Sector Banks') + ' functioning in India (alphabetical list from the slide).']),
  dict(h='Private Sector Bank', hi='निजी क्षेत्र का बैंक', facts=[
     'Owned (' + k('majority stake of 51% or more') + ') by ' + k('private individuals or companies') + '.',
     'Licensed under the ' + k('Banking Regulation Act, 1949') + '.',
  ]),
  dict(h='Foreign Bank', hi='विदेशी बैंक', facts=[
     'Foreign banks are ' + k('headquartered outside India') + ' but operate branches in India.',
     'They must follow the rules of the ' + k('Reserve Bank of India') + ' and the regulations of their ' + k('parent bank abroad') + '.',
  ]),
  dict(h='Regional Rural Banks (RRBs)', hi='क्षेत्रीय ग्रामीण बैंक', tag='bank', facts=[
     'Established under the ' + k('Regional Rural Banks Act, 1976') + '.',
     'Meant to provide credit to ' + k('farmers, rural workers and small entrepreneurs') + '.',
  ], add=[
     'The first RRBs were set up on <b>2 October 1975</b> by ordinance (Narasimham Working Group). The first was <b>Prathama Bank</b>, Moradabad (sponsored by Syndicate Bank).',
     'Shareholding: <b>Centre 50% · Sponsor bank 35% · State 15%</b>. RRBs are regulated by RBI and supervised by NABARD. RRBs are taught in detail in Class 6.',
  ]),
  dict(h='Small Finance Banks & Payments Banks', facts=[
     'Both are ' + k('licensed under the Banking Regulation Act, 1949') + '.',
     'Both are ' + k('set up to promote financial inclusion') + '. (Full rules: <a href="Class-03.html">Class 3</a>.)',
  ]),
  dict(h='Local Area Banks (LABs)', hi='स्थानीय क्षेत्र बैंक', tag='hot', pics=[('c5-lab-addresses', 'Addresses of the two LABs (slide)')], facts=[
     'Local Area Banks were introduced in ' + k('1996') + ' to operate in ' + k('2–3 contiguous districts') + ', mobilise rural savings and improve local credit availability.',
     'The ' + k('Local Area Bank Scheme') + ' was introduced in ' + k('August 1996') + '. The Finance Minister referred to new private local banks with jurisdiction over two or three contiguous districts.',
     'He observed this would let local institutions mobilise rural savings and make them available for investment in the local areas.',
     'RBI announced guidelines for setting up LABs in the private sector on ' + k('24 August 1996') + '.',
     k('Coastal Bank') + ' is the ' + k('first Local Area Bank') + ' licensed by RBI, in ' + k('1999') + '; it began operations on ' + k('27 December 1999') + '. Address: Coastal Local Area Bank Ltd, Vijayawada (Andhra Pradesh).',
     k('KBS Bank') + ' (' + k('Krishna Bhima Samruddhi Local Area Bank') + ') is one of the LABs operating now. Address: Mahabubnagar, Telangana.',
     'RBI ' + k('cancelled the licence') + ' of Maharashtra-based ' + k('Subhadra Local Area Bank') + '.',
     k('Capital Small Finance Bank') + ' started operations as India’s ' + k('1st Small Finance Bank') + ' on ' + k('24 April 2016') + ', after conversion from ' + k('Capital Local Area Bank') + '.',
     'Before conversion, Capital Local Area Bank had been ' + k('India’s largest LAB') + ' since ' + k('14 January 2000') + '.',
  ], add=['Minimum capital for a LAB was ₹5 crore. Finance Minister in 1996: P. Chidambaram (Budget speech, July 1996).'],
   trap='Coastal = <b>first LAB</b> (1999). Capital LAB = <b>largest LAB</b>, later the <b>first SFB</b> (2016). Subhadra = licence <b>cancelled</b>. KBS = still running.'),
  dict(h='Co-operative Banks', hi='सहकारी बैंक', tag='bank', facts=[
     'Co-operative banks are ' + k('owned and managed by their members') + ', set up mainly to provide ' + k('rural and small-scale credit') + '.',
     'They are registered under the ' + k('Co-operative Societies Act, 1912') + ' (in India, under the State Co-operative Societies Acts).',
     'They are regulated by the ' + k('Reserve Bank of India') + ' and ' + k('NABARD') + ' under the relevant banking laws.',
     'They come under RBI’s regulatory ambit under two laws: the ' + k('Banking Regulation Act, 1949') + ' and the Banking Laws (Co-operative Societies) Act.',
     'The co-operative banking system came into being to ' + k('promote saving and investment habits') + ', especially in rural parts of the country.',
     'Broadly, co-operative banks are divided into two categories – ' + k('Urban and Rural') + '.',
     'Rural co-operatives are sub-divided into ' + k('State Co-operative Banks, District Central Co-operative Banks and Primary Agricultural Credit Societies') + '.',
     k('Urban Co-operative Banks (UCBs)') + ' are of two kinds – ' + k('Multi-State') + ' and those operating in a ' + k('single state') + '.',
     'Three tiers named on the slide: ' + k('Primary Credit Societies') + ' → ' + k('Central Co-operative Bank') + ' → ' + k('State Co-operative Bank') + '.',
  ], trap='The slide writes “Banking Laws (Co-operative Societies) Act, <b>1955</b>”. The real Act is the <b>Banking Laws (Application to Co-operative Societies) Act, 1965</b>. Pick 1965 if both appear.'),
  dict(h='Structure of Co-operative Credit Institutions (RBI chart)', pics=[('c5-coop-chart', 'Chart IV.1 – Structure of Co-operative Credit Institutions')], facts=[
     'Co-operative Credit Institutions → ' + k('Urban Co-operative Banks') + ' and ' + k('Rural Co-operative Credit Institutions') + '.',
     'Rural → ' + k('Short-term structure') + ': State Co-operative Banks → (District) Central Co-operative Banks → Primary Agricultural Credit Societies (PACS).',
     'Rural → ' + k('Long-term structure') + ': State Co-operative Agriculture and Rural Development Banks (SCARDBs) → Primary Co-operative Agriculture and Rural Development Banks (PCARDBs).',
  ]),
  dict(h='Land Development Bank (LDB)', facts=[
     'A Land Development Bank (LDB) is a ' + k('special kind of bank') + ' in India.',
     'Its main objective is to promote the ' + k('development of land, agriculture') + ' and increase agricultural production.',
     'The first LDB was started at ' + k('Jhang in Punjab in 1920') + '.',
  ], add=['LDBs give long-term loans and are the old name of the long-term co-operative structure (today’s SCARDBs and PCARDBs). Jhang is now in Pakistan.']),
 ]),
 ('All India Financial Institutions (AIFIs)', 'अखिल भारतीय वित्तीय संस्थान – the five RBI-regulated development finance institutions.', [
  dict(h='What AIFIs are and why they were created', tag='hot', pics=[('c5-aifi', 'All India Financial Institutions')], facts=[
     'AIFIs are ' + k('specialised financial institutions') + ' set up by the Government of India to provide ' + k('long-term finance') + ' to ' + k('specific sectors of the economy') + '.',
     'They ' + k('do not perform full commercial banking') + ', like accepting regular deposits from the public.',
     'Objectives: provide ' + k('long-term credit') + ' · support ' + k('priority and development sectors') + ' · promote ' + k('economic and financial development') + ' · ' + k('fill gaps not served by commercial banks') + '.',
     'The five AIFIs: ' + k('EXIM Bank, NABARD, NHB, SIDBI and NaBFID') + '.',
  ]),
 ]),
 ('NABARD', 'National Bank for Agriculture and Rural Development.', [
  dict(h='NABARD – what it is', tag='hot', pics=[('c5-nabard-logo', 'NABARD'), ('c5-nabard-mindmap', 'NABARD at a glance')], facts=[
     'NABARD is an ' + k('apex regulatory body') + ' for overall regulation of ' + k('regional rural banks and apex co-operative banks') + ' in India.',
     'It is under the jurisdiction of the ' + k('Ministry of Finance') + ', Government of India.',
     'Established in ' + k('1982') + ' under an ' + k('Act of Parliament') + ' to promote sustainable and equitable agriculture and rural development.',
     'It is a ' + k('fully owned Government of India entity') + '.',
     k('Formation: 12 July 1982') + ' · ' + k('Headquarters: Mumbai, Maharashtra') + ' · ' + k('Chairman: Shaji K V') + '.',
  ], add=['Set up under the <b>NABARD Act, 1981</b>, on the recommendation of the CRAFICARD (below). It took over the agricultural credit work of RBI and the Agricultural Refinance and Development Corporation.']),
  dict(h='CRAFICARD – the committee behind NABARD', pics=[('c5-craficard', 'Formation of CRAFICARD')], facts=[
     'The Government formed a Committee to Review the Arrangements for Institutional Credit for Agriculture and Rural Development (' + k('CRAFICARD') + ').',
     'It was set up on ' + k('30 March 1979') + ' under the chairmanship of ' + k('B. Sivaraman') + ', former Member of the Planning Commission.',
  ]),
  dict(h='NABARD’s subsidiaries', tag='hot', pics=[('c5-nabard-subs', 'NABARD’s subsidiaries')], facts=[
     k('NABKISAN · NABSAMRUDDHI · NABFINS · NABFOUNDATION · NABCONS · NABVENTURES · NABSanrakshan') + ' (7 subsidiaries).',
  ], add=[
     'NABKISAN – credit to farmer producer organisations · NABSAMRUDDHI – non-farm sector finance · NABFINS – microfinance · NABFOUNDATION – development projects (not-for-profit) · NABCONS – consultancy · NABVENTURES – venture capital fund · NABSanrakshan – credit guarantee trustee (e.g. for FPOs).',
  ]),
  dict(h='NABARD’s capital and RBI’s exit', tag='hot', pics=[('c5-nabard-capital', 'NABARD’s capital evolution'), ('c5-nabard-divest', 'Divestment of RBI’s stake in NABARD')], facts=[
     'Its ' + k('initial paid-up capital') + ' was ' + k('₹100 crore') + '.',
     'The Government raised NABARD’s ' + k('authorised capital') + ' by ' + k('six times to ₹30,000 crore') + '.',
     'RBI’s stake was divested in two phases: RBI held ' + k('72.5%') + ' worth ' + k('₹1,450 crore') + '.',
     k('71.5%') + ', worth ' + k('₹1,430 crore') + ', was divested in ' + k('October 2010') + '.',
     'The ' + k('residual shareholding') + ' (₹20 crore) was divested on ' + k('26 February 2019') + '.',
  ]),
 ]),
 ('National Housing Bank (NHB)', 'राष्ट्रीय आवास बैंक', [
  dict(h='NHB', tag='hot', pics=[('c5-nhb-logo', 'National Housing Bank'), ('c5-nhb-mindmap', 'NHB at a glance')], facts=[
     'NHB is the ' + k('apex regulatory body') + ' for overall regulation and licensing of ' + k('housing finance companies') + ' in India.',
     'It is under the jurisdiction of the ' + k('Ministry of Finance') + ', Government of India.',
     'It was set up on ' + k('9 July 1988') + ' under the ' + k('National Housing Bank Act, 1987') + '.',
     'It was set up on the recommendation of the ' + k('C. Rangarajan Committee') + '.',
     'RBI had ' + k('100% shareholding') + ' in NHB, which was divested for ' + k('₹1,450 crore') + '.',
     'The ' + k('Finance Act, 2019') + ' amended the NHB Act, 1987. The amendment gives the powers of ' + k('regulation of Housing Finance Companies (HFCs) to the RBI') + '.',
     k('Founded: 9 July 1988') + ' · ' + k('Headquarters: New Delhi') + ' · ' + k('Managing Director: Sanjay Shukla') + '.',
  ], trap='Since 2019 RBI <b>regulates</b> HFCs; NHB still <b>supervises</b> them and refinances housing loans. Older books still say “NHB regulates HFCs”. Also: NHB HQ is <b>New Delhi</b>; NABARD and EXIM are in <b>Mumbai</b>.'),
 ]),
 ('SIDBI', 'Small Industries Development Bank of India.', [
  dict(h='SIDBI', tag='hot', pics=[('c5-sidbi-logo', 'SIDBI'), ('c5-sidbi-pie', 'SIDBI shareholding pattern')], facts=[
     'SIDBI is the ' + k('apex regulatory body') + ' for overall licensing and regulation of ' + k('micro, small and medium enterprise finance companies') + ' in India.',
     'It was set up on ' + k('2 April 1990') + ' under an Act of Indian Parliament.',
     'It is under the jurisdiction of the ' + k('Ministry of Finance') + ', Government of India.',
     'SIDBI was established by the Government of India as a ' + k('wholly owned subsidiary of IDBI') + ' Bank.',
     'It was ' + k('delinked from IDBI') + ' with effect from ' + k('27 March 2000') + '.',
     k('Formed: 2 April 1990') + ' · ' + k('Headquarters: Lucknow, Uttar Pradesh') + ' · ' + k('Chairman and Managing Director: Manoj Mittal') + '.',
     'Shareholding: ' + k('Government of India 20.85%') + ' · State Bank of India 15.65% · LIC 13.33% · NABARD 9.36% · others 40.81%.',
  ], trap='The English slide wrongly prints “Headquarters: Manoj Mittal”. The Hindi slide has it right: HQ is <b>Lucknow</b>. Manoj Mittal is the CMD.'),
 ]),
 ('EXIM Bank', 'Export-Import Bank of India.', [
  dict(h='EXIM Bank', tag='hot', facts=[
     'Export-Import Bank of India (Exim Bank) is a ' + k('specialised financial institution') + ' established in ' + k('1982') + '.',
     'The ' + k('Export-Import Bank of India Act') + ' was passed in ' + k('September 1981') + ', and the bank commenced operations in ' + k('March 1982') + '.',
     'Its primary function is to ' + k('finance, facilitate and promote India’s international trade') + '.',
     'EXIM Bank is a ' + k('wholly-owned subsidiary of the Indian Government') + '.',
     k('Founded: 1982') + ' · ' + k('Managing Director: Harsha Bangari') + ' · ' + k('Headquarters: Mumbai, Maharashtra') + '.',
  ], add=['EXIM Bank gives Lines of Credit (LoCs) to other countries on behalf of the Government. Harsha Bangari is its first woman MD.']),
 ]),
 ('NaBFID', 'National Bank for Financing Infrastructure and Development – the newest AIFI.', [
  dict(h='NaBFID – basics', tag='hot', pics=[('c5-nabfid', 'NaBFID – founded 19 April 2021'), ('c5-nabfid-infra', 'Long-term infrastructure finance')], facts=[
     'NaBFID is a ' + k('Development Finance Institution (DFI)') + ' in India, founded on ' + k('19 April 2021') + '.',
     'It was set up to support the development of ' + k('long-term infrastructure financing in India') + '.',
     'It is established under the ' + k('National Bank for Financing Infrastructure and Development Act, 2021') + '. Established: 2021 · ' + k('Headquarters: Mumbai') + '.',
     'NaBFID is regulated and supervised by RBI as an ' + k('All India Financial Institution (AIFI)') + ' under ' + k('Sections 45L and 45N of the RBI Act, 1934') + '.',
     'It is the ' + k('fifth AIFI') + ', after EXIM Bank, NABARD, NHB and SIDBI.',
  ]),
  dict(h='NaBFID – leadership', pics=[('c5-kamath', 'Chairman K. V. Kamath'), ('c5-rajkiran', 'MD Rajkiran Rai G')], facts=[
     k('Chairman: K. V. Kamath') + ' · ' + k('Managing Director: Rajkiran Rai G') + '.',
     'The Chairperson, MD and Deputy MDs hold office for ' + k('not more than five years') + ', and can be re-appointed subject to an overall term ' + k('not exceeding ten years') + '.',
  ]),
  dict(h='NaBFID – capital structure', tag='hot', facts=[
     'Initially, the Government of India infused capital of ' + k('₹20,000 crore') + '.',
     'The ' + k('entire shareholding') + ' is currently held by the ' + k('Government of India') + '.',
     'The ' + k('authorised share capital') + ' is ' + k('₹1 lakh crore') + ', divided into ten thousand crore fully paid-up shares of ten rupees each.',
     'The Central Government granted (contributed) ' + k('₹5,000 crore') + ' to the institution.',
     'Shares may be held by the Central Government, multilateral institutions, sovereign wealth funds, pension funds, insurers, financial institutions, banks, and others as prescribed.',
     'The Central Government shall hold ' + k('at least 26%') + ' of the shares at all times.',
  ], trap='Three NaBFID money figures: <b>₹20,000 crore</b> initial capital · <b>₹5,000 crore</b> grant · <b>₹1 lakh crore</b> authorised capital. Government floor: <b>26%</b>.'),
 ]),
 ('IFCI', 'Industrial Finance Corporation of India – India’s first DFI, not an AIFI today.', [
  dict(h='IFCI Ltd', facts=[
     'IFCI Ltd was established in ' + k('1948') + ' as a ' + k('statutory corporation') + ' (then called Industrial Finance Corporation of India) to provide ' + k('medium- and long-term finance to industries') + '.',
     'In ' + k('1993') + ', after the Industrial Finance Corporation Act was repealed, IFCI became a ' + k('Public Limited Company') + ' registered under the ' + k('Companies Act, 1956') + '.',
     'Today IFCI is registered with RBI as a ' + k('Systemically Important Non-Deposit Taking NBFC (NBFC-ND-SI)') + ', and is a ' + k('Public Financial Institution (PFI)') + ' under ' + k('Section 2(72) of the Companies Act, 2013') + '.',
     k('Headquarters: New Delhi') + '.',
  ], trap='IFCI (1948) is the <b>first</b> development finance institution of India, but it is now an <b>NBFC</b>, not one of the five RBI-regulated AIFIs.'),
  dict(h='The five AIFIs side by side', sort=True, table=(['AIFI', 'Set up', 'Act', 'HQ', 'Head (as taught)'], [
     ['EXIM Bank', '1982 (Act Sep 1981)', 'EXIM Bank Act, 1981', 'Mumbai', 'MD Harsha Bangari'],
     ['NABARD', '12 July 1982', 'NABARD Act, 1981', 'Mumbai', 'Chairman Shaji K V'],
     ['NHB', '9 July 1988', 'NHB Act, 1987', 'New Delhi', 'MD Sanjay Shukla'],
     ['SIDBI', '2 April 1990', 'SIDBI Act, 1989', 'Lucknow', 'CMD Manoj Mittal'],
     ['NaBFID', '19 April 2021', 'NaBFID Act, 2021', 'Mumbai', 'Chairman K. V. Kamath · MD Rajkiran Rai G'],
  ])),
 ]),
]

SORT_OPTS = ['NABARD', 'NHB', 'SIDBI', 'EXIM', 'NaBFID']
SORT_Q = 'Quick check – which AIFI is it?'
SORT = [('Headquartered in Lucknow', 'SIDBI'), ('CRAFICARD / B. Sivaraman', 'NABARD'), ('C. Rangarajan Committee', 'NHB'), ('Fifth AIFI, set up 2021', 'NaBFID'),
        ('Delinked from IDBI in 2000', 'SIDBI'), ('Promotes India’s international trade', 'EXIM'), ('Subsidiaries NABFINS, NABCONS…', 'NABARD'),
        ('RBI’s 100% stake sold for ₹1,450 crore', 'NHB'), ('Government must hold at least 26%', 'NaBFID'), ('MD Harsha Bangari', 'EXIM')]

FLASH = [
 ('Scheduled bank', 'Listed in the Second Schedule of the RBI Act, 1934 (conditions: Section 42(6)(a)); can borrow from RBI and is a clearing-house member.'),
 ('Local Area Bank', 'Private bank for 2–3 contiguous districts; scheme Aug 1996; first: Coastal LAB (1999).'),
 ('Land Development Bank', 'Special bank for land and agricultural development; first at Jhang, Punjab, 1920.'),
 ('AIFI', 'Govt-set specialised institution giving long-term finance to specific sectors; no regular public deposits. Five: EXIM, NABARD, NHB, SIDBI, NaBFID.'),
 ('NABARD', '12 July 1982, Mumbai; CRAFICARD (B. Sivaraman); regulates RRBs & apex co-op banks; 7 subsidiaries.'),
 ('NHB', '9 July 1988, New Delhi; NHB Act 1987; Rangarajan Committee; HFC regulation moved to RBI in 2019.'),
 ('SIDBI', '2 April 1990, Lucknow; was IDBI subsidiary, delinked 27 March 2000; MSME finance.'),
 ('NaBFID', '19 April 2021, Mumbai; infrastructure DFI; ₹20,000 cr initial capital; govt ≥ 26%.'),
]

QUIZ = [
 ('Name the four types of banks taught.', 'Central Bank (RBI), Commercial Bank, Specialised Bank, Co-operative Bank.'),
 ('In which schedule of which Act are scheduled banks listed?', 'Second Schedule of the RBI Act, 1934.'),
 ('Which section lays down the conditions for inclusion in the Second Schedule?', 'Section 42(6)(a) of the RBI Act.'),
 ('What two facilities does a scheduled commercial bank get?', 'Eligibility to borrow from RBI, and automatic clearing-house membership.'),
 ('Under which Acts were the public sector banks established?', 'SBI Act, 1955, and the Banking Companies (Acquisition and Transfer of Undertakings) Acts of 1970 & 1980.'),
 ('Under which Act are private banks, SFBs and payments banks licensed?', 'Banking Regulation Act, 1949.'),
 ('Under which Act were RRBs set up, and for whom?', 'Regional Rural Banks Act, 1976 – credit to farmers, rural workers and small entrepreneurs.'),
 ('How many districts can a Local Area Bank cover?', 'Two or three contiguous districts.'),
 ('Which was the first Local Area Bank, and when did it start?', 'Coastal Local Area Bank – licensed 1999, operations from 27 December 1999.'),
 ('Which LAB became India’s first small finance bank?', 'Capital Local Area Bank → Capital Small Finance Bank, 24 April 2016.'),
 ('Where and when was the first Land Development Bank started?', 'Jhang, Punjab, 1920.'),
 ('Name the three tiers of the rural short-term co-operative structure.', 'State Co-operative Bank → District Central Co-operative Bank → Primary Agricultural Credit Society.'),
 ('Which committee led to NABARD, and who chaired it?', 'CRAFICARD, chaired by B. Sivaraman (set up 30 March 1979).'),
 ('NABARD: formation date, HQ and chairman?', '12 July 1982; Mumbai; Shaji K V.'),
 ('What was NABARD’s initial paid-up capital and its raised authorised capital?', '₹100 crore; ₹30,000 crore.'),
 ('When did RBI sell its last stake in NABARD?', '26 February 2019 (₹20 crore); the first 71.5% went in October 2010.'),
 ('Which Act moved HFC regulation from NHB to RBI?', 'Finance Act, 2019.'),
 ('Where is SIDBI headquartered, and from which institution was it delinked?', 'Lucknow; delinked from IDBI on 27 March 2000.'),
 ('Which institution holds the largest single stake in SIDBI?', 'Government of India – 20.85%.'),
 ('When did EXIM Bank start operations?', 'March 1982 (Act passed September 1981).'),
 ('Under which sections of the RBI Act is NaBFID regulated as an AIFI?', 'Sections 45L and 45N.'),
 ('What minimum stake must the Centre hold in NaBFID?', '26%.'),
 ('What is IFCI today?', 'An NBFC-ND-SI registered with RBI, and a Public Financial Institution under Section 2(72) of the Companies Act, 2013.'),
]

RAPID = [
 'Types: Central (RBI) · Commercial · Specialised · Co-operative.',
 'Scheduled bank = RBI Act 1934 Second Schedule, Sec 42(6)(a); gets RBI borrowing + clearing-house membership.',
 'PSB: govt ≥ 51% (SBI Act 1955; Acquisition Acts 1970 & 1980) · Private: ≥ 51% private, BR Act 1949 · Foreign: HQ abroad, follows RBI + parent.',
 'RRB Act 1976 · SFB & PB: BR Act 1949, financial inclusion · LAB: Aug 1996, 2–3 districts; Coastal first (27 Dec 1999); Capital LAB → first SFB (24 Apr 2016).',
 'Co-op: members own; Co-operative Societies Act 1912; RBI + NABARD; urban (multi-state / single-state) vs rural (StCB → DCCB → PACS; long-term SCARDB → PCARDB). LDB: Jhang 1920.',
 'AIFIs (5): EXIM 1982 Mumbai · NABARD 12 Jul 1982 Mumbai · NHB 9 Jul 1988 New Delhi · SIDBI 2 Apr 1990 Lucknow · NaBFID 19 Apr 2021 Mumbai.',
 'NABARD: CRAFICARD (B. Sivaraman, 30 Mar 1979); ₹100 cr → ₹30,000 cr; RBI exit Oct 2010 + 26 Feb 2019; 7 subsidiaries.',
 'NHB: Rangarajan Committee; RBI 100% sold for ₹1,450 cr; HFC regulation → RBI (Finance Act 2019).',
 'NaBFID: Sec 45L & 45N; ₹20,000 cr + ₹5,000 cr grant; authorised ₹1 lakh cr; govt ≥ 26%; Kamath / Rajkiran Rai G; term ≤ 5 yrs (max 10).',
 'IFCI 1948 → company 1993 → NBFC-ND-SI + PFI (Sec 2(72), Companies Act 2013), HQ New Delhi.',
]
