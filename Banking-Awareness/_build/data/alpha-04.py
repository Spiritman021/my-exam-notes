# Saarthi Alpha · Class 4 — from the class PDF (INTRODUCTIONS GENERAL AWARENESS - 102250_4814070_lc.doc.pdf, 31 slides, all images).
CLASS = 4
TITLE = 'History of Banking, Nationalisation & Mergers'
FULL = 'Recap of Payments Bank & Small Finance Bank; History of Banking in India – Presidency Banks, Imperial Bank, SBI and its Associate Banks, first banks; Nationalisation; Merger of Banks'
COVERS = 'Payments Bank & SFB recap, History of Bank, Nationalisation, Merger of Banks (the Class 2 topics), not AIFIs'
NOTE = ('The class plan lists AIFIs (NABARD, SIDBI, NHB, NaBFID, EXIM) for Class 4, but this PDF covers the topics still pending from Class 2: '
        'History of Bank, Nationalisation and Merger of Banks. It opens with a picture recap of <a href="Class-03.html">Class 3</a>.')

TIMELINE = '''<ol class="tl">
<li><span class="y">1770</span><b>Bank of Hindustan</b>, Calcutta (Alexander &amp; Co.) – first bank in India</li>
<li><span class="y">1786</span>General Bank of India</li>
<li><span class="y">1806</span><b>Bank of Calcutta</b> → renamed <b>Bank of Bengal</b> in 1809 (first Presidency Bank)</li>
<li><span class="y">1840</span>Bank of Bombay</li>
<li><span class="y">1843</span>Bank of Madras</li>
<li><span class="y">1894</span><b>Punjab National Bank</b>, Lahore – first bank purely managed by Indians</li>
<li><span class="y">1911</span><b>Central Bank of India</b> – first truly Swadeshi bank</li>
<li><span class="y">1921</span>3 Presidency Banks merged → <b>Imperial Bank of India</b> (private)</li>
<li><span class="y">1946</span>Bank of India opens in <b>London</b> – first Indian bank branch abroad</li>
<li><span class="y">1955</span>Imperial Bank nationalised → <b>State Bank of India</b> (A.D. Gorwala Committee)</li>
<li><span class="y">1959</span>SBI (Subsidiary Banks) Act → <b>8 associate banks</b></li>
<li><span class="y">1963</span>Bikaner + Jaipur → State Bank of Bikaner and Jaipur</li>
<li><span class="y">19 Jul 1969</span><b>14 banks</b> nationalised</li>
<li><span class="y">15 Apr 1980</span><b>6 banks</b> nationalised</li>
<li><span class="y">4 Sep 1993</span>New Bank of India → Punjab National Bank</li>
<li><span class="y">2008</span>State Bank of Saurashtra → SBI</li>
<li><span class="y">2010</span>State Bank of Indore → SBI</li>
<li><span class="y">1 Apr 2017</span>5 associate banks + Bharatiya Mahila Bank → SBI</li>
<li><span class="y">1 Apr 2019</span>Vijaya Bank + Dena Bank → Bank of Baroda</li>
<li><span class="y">1 Apr 2020</span>10 PSBs amalgamated into 4 → <b>12 PSBs</b></li>
</ol>'''

S = [
 ('Recap: Payments Bank & Small Finance Bank', 'The opening slides redraw Class 3 as charts.', [
  dict(h='Payments Bank in three charts', pics=[('c4-pb-flow', 'Deposits flow chart · ₹2 lakh limit · what a payments bank does'), ('c4-pb-mindmap', 'Payments Bank mind map')], facts=[
     'Accepts deposits? → ' + k('Demand deposits') + ' (current & savings accounts) yes; ' + k('term deposits not permitted') + '.',
     'Deposit limit: ' + k('₹2 lakh') + ' per customer.',
     'A payments bank does three things: ' + k('facilitates deposits') + ', gives ' + k('payment services') + ', and gives ' + k('no loans') + '.',
     'Mind map: capital ' + k('₹100 crore') + ' · ' + k('25%') + ' branches in rural areas · debit card yes · loans no · ' + k('FDI – 74%') + '.',
  ], trap='Class 3 said foreign shareholding is “as per FDI rules in private banks”. This slide gives the number: <b>74%</b>, the FDI cap for private-sector banks.'),
  dict(h='Small Finance Bank Structure', pics=[('c4-sfb-structure', 'Small Finance Bank Structure')], facts=[
     k('Operational scope') + ': offer both deposits and loans.',
     k('Capital requirement') + ': a minimum of ' + k('₹300 crore') + ' to open a bank.',
     k('Foreign investment') + ': allowed as per FDI rules.',
     k('Experience requirement') + ': ' + k('10 years') + ' of banking experience.',
     k('Lending mandate') + ': ' + k('60%') + ' of credit must go to the priority sector.',
  ]),
 ]),
 ('History of Banking in India', 'From the first bank (1770) to SBI (1955). Use the timeline as your revision map.', [
  dict(h='Timeline at a glance', html='TIMELINE'),
  dict(h='The first banks', tag='hot', facts=[
     'The ' + k('Bank of Hindustan') + ', established in ' + k('1770') + ' in ' + k('Calcutta') + ' by ' + k('Alexander and Company') + ', is considered the ' + k('first bank in India') + '.',
     'Other early banks like the ' + k('General Bank of India (1786)') + ' followed, but the Bank of Hindustan was the first to start operations.',
     'The first bank ' + k('purely managed by Indians') + ' was ' + k('Punjab National Bank') + ', established in ' + k('Lahore') + ' in ' + k('1894') + '.',
     'The first Indian commercial bank ' + k('wholly owned and managed by Indians') + ' was ' + k('Central Bank of India') + ', established in ' + k('1911') + ' – known as the ' + k('first truly Swadeshi bank') + '.',
     k('Bank of India') + ' was the ' + k('first Indian bank to open a branch outside India') + ' – in ' + k('London') + ', in ' + k('1946') + '.',
  ], trap='Three different “firsts”: <b>PNB (1894)</b> = first <i>managed</i> purely by Indians; <b>Central Bank of India (1911)</b> = first <i>wholly owned and managed</i> by Indians (Swadeshi); <b>Bank of India (1946)</b> = first branch <i>abroad</i>.'),
  dict(h='What were Presidency Banks?', hi='प्रेसिडेंसी बैंक', facts=[
     'Presidency Banks were the ' + k('earliest modern banking institutions') + ' set up in India during ' + k('British colonial rule') + '.',
     'They were called Presidency banks because each was associated with one of the major British administrative regions – the Presidencies (' + k('Bengal, Bombay and Madras') + ').',
  ]),
  dict(h='The three Presidency Banks', tag='hot', table=(['Bank', 'Year', 'Place / note'], [
     [k('Bank of Bengal'), k('1806') + ' as Bank of Calcutta; renamed Bank of Bengal in ' + k('1809'), 'Calcutta – the ' + k('first') + ' of the Presidency Banks'],
     [k('Bank of Bombay'), k('1840'), 'Bombay'],
     [k('Bank of Madras'), k('1843'), 'Madras'],
  ]), trap='The PDF shows Bank of Bengal as <b>1806</b> on one slide and <b>1809</b> on the next. Both are right: it opened as the <b>Bank of Calcutta in 1806</b> and was renamed <b>Bank of Bengal in 1809</b>. If the question says “Bank of Calcutta”, answer 1806.'),
  dict(h='Imperial Bank of India → State Bank of India', tag='bank', facts=[
     'In ' + k('1921') + ', the Presidency Banks were ' + k('merged') + ' to form the ' + k('Imperial Bank of India') + '. It was a ' + k('private entity') + '.',
     'In ' + k('1955') + ', the Imperial Bank of India was ' + k('nationalised') + ' and renamed the ' + k('State Bank of India') + ', on the recommendation of the ' + k('A.D. Gorwala Committee') + '.',
  ], add=[
     'SBI came into being on <b>1 July 1955</b> under the <b>State Bank of India Act, 1955</b>. The Gorwala Committee was the All India Rural Credit Survey Committee.',
     'Until RBI was set up in 1935, the Imperial Bank also did some central-banking work for the Government.',
  ]),
  dict(h='Associate Banks of SBI (1959)', facts=[
     'The ' + k('State Bank of India (Subsidiary Banks) Act of 1959') + ' enabled the formation of ' + k('eight associate banks') + ' as subsidiaries of SBI.',
     'This was done mainly by taking over banks of former ' + k('princely states') + ', to expand ' + k('rural banking') + ' during India’s ' + k('First Five-Year Plan') + '.',
     '8 subsidiaries were attached with SBI in 1959 and named ' + k('Associate Banks of SBI') + ': State Bank of ' + k('Bikaner') + ', ' + k('Jaipur') + ', ' + k('Saurashtra') + ', ' + k('Indore') + ', ' + k('Hyderabad') + ', ' + k('Patiala') + ', ' + k('Mysore') + ' and ' + k('Travancore') + '.',
  ]),
  dict(h='What happened to the associate banks', tag='hot', facts=[
     k('1963') + ' – State Bank of Bikaner and State Bank of Jaipur merged with each other to form ' + k('State Bank of Bikaner and Jaipur (SBBJ)') + '.',
     k('2008') + ' – ' + k('State Bank of Saurashtra') + ' merged into SBI.',
     k('2010') + ' – ' + k('State Bank of Indore') + ' merged into SBI.',
     k('1 April 2017') + ' – the remaining ' + k('5 associate banks') + ' merged into SBI: State Bank of Bikaner and Jaipur, Hyderabad, Mysore, Patiala and Travancore.',
     'Along with them, ' + k('Bharatiya Mahila Bank') + ' was also merged into SBI.',
  ], trap='8 associates in 1959 but only <b>5</b> merged in 2017: Bikaner + Jaipur had already become one bank (1963), and Saurashtra (2008) and Indore (2010) had gone earlier. 8 → 7 → 6 → 5.'),
 ]),
 ('Nationalisation in India', 'भारत में राष्ट्रीयकरण', [
  dict(h='The two rounds of bank nationalisation', tag='hot', table=(['Date', 'Banks', 'Size rule (as on the slide)'], [
     [k('19 July 1969'), k('14 banks'), 'Minimum capital of ' + k('₹50 crore')],
     [k('15 April 1980'), k('6 banks'), 'Minimum capital of ' + k('₹200 crore')],
  ]), add=[
     'The 1969 nationalisation was done by an ordinance under PM <b>Indira Gandhi</b>, followed by the Banking Companies (Acquisition and Transfer of Undertakings) Act, 1970.',
  ], trap='The slide says “minimum <b>capital</b>”. The actual criterion was <b>deposits</b> of ₹50 crore (1969) and ₹200 crore (1980). If an option says “deposits of over ₹50 crore”, that is the correct one.'),
 ]),
 ('Merger of Banks', 'From 27 public sector banks in 2017 to 12 today.', [
  dict(h='Mergers before 2020', facts=[
     k('New Bank of India') + ' was merged into ' + k('Punjab National Bank') + ' on ' + k('4 September 1993') + '.',
     k('Vijaya Bank and Dena Bank') + ' merged with ' + k('Bank of Baroda') + ' on ' + k('1 April 2019') + '.',
  ], add=['New Bank of India (nationalised in 1980) is the only nationalised bank to have been merged into another before 2017.']),
  dict(h='The mega-merger of 1 April 2020', tag='hot', sort=True, pics=[('c4-merger-logos', 'The four 2020 mergers')], facts=[
     k('Ten') + ' public sector banks were amalgamated into ' + k('four') + ' banks from ' + k('1 April 2020') + '.',
     k('Oriental Bank of Commerce (OBC)') + ' and ' + k('United Bank of India') + ' → merged into ' + k('Punjab National Bank') + '.',
     k('Syndicate Bank') + ' → merged into ' + k('Canara Bank') + '.',
     k('Allahabad Bank') + ' → merged with ' + k('Indian Bank') + '.',
     k('Andhra Bank') + ' and ' + k('Corporation Bank') + ' → merged with ' + k('Union Bank of India') + '.',
  ]),
  dict(h='12 PSBs after the mergers', tag='hot', facts=[
     'After the merger there are ' + k('12 PSBs') + ' – ' + k('six merged banks') + ' and ' + k('six independent') + ' public sector banks.',
     k('Six merged banks') + ': SBI, Bank of Baroda, Punjab National Bank, Canara Bank, Union Bank of India, Indian Bank.',
     k('Six independent banks') + ': Indian Overseas Bank, UCO Bank, Bank of Maharashtra, Punjab and Sind Bank, Bank of India, Central Bank of India.',
  ]),
  dict(h='NextGen PSBs (the government slide)', pics=[('c4-nextgen-psbs', 'NextGen PSBs – March 2019 financials')], table=(['Anchor bank', 'Amalgamating bank(s)', 'Business size*', 'PSB rank', 'CBS'], [
     ['Punjab National Bank', 'Oriental Bank of Commerce, United Bank of India', '₹17.94 lakh cr', k('2nd largest'), 'Finacle'],
     ['Canara Bank', 'Syndicate Bank', '₹15.20 lakh cr', '4th largest', 'iFlex'],
     ['Union Bank of India', 'Andhra Bank, Corporation Bank', '₹14.59 lakh cr', '5th largest', 'Finacle'],
     ['Indian Bank', 'Allahabad Bank', '₹8.08 lakh cr', '7th largest', 'BaNCS'],
     ['SBI', 'Amalgamated earlier', '₹52.05 lakh cr', '(largest)', ''],
     ['Bank of Baroda', 'Amalgamated earlier', '₹16.13 lakh cr', '', ''],
  ]), facts=[
     'The consolidated PSBs (for strong national presence & global reach) hold ' + k('82% of PSB business') + ' and ' + k('56% of commercial bank business') + '.',
     '<b>To strengthen national presence</b>: Bank of India (₹9.03 lakh cr), Central Bank of India (₹4.68 lakh cr).',
     '<b>To strengthen regional focus</b>: Indian Overseas Bank (₹3.75 lakh cr), UCO Bank (₹3.17 lakh cr), Bank of Maharashtra (₹2.34 lakh cr), Punjab and Sind Bank (₹1.71 lakh cr).',
     k('27 PSBs in 2017') + ' → ' + k('12 PSBs') + ' post consolidation. (*March 2019 financials)',
  ]),
 ]),
]

SORT_OPTS = ['PNB', 'Canara', 'Union Bank', 'Indian Bank', 'Bank of Baroda', 'SBI']
SORT_Q = 'Quick check – which bank absorbed it?'
SORT = [('Oriental Bank of Commerce', 'PNB'), ('Syndicate Bank', 'Canara'), ('Allahabad Bank', 'Indian Bank'), ('Andhra Bank', 'Union Bank'),
        ('Dena Bank', 'Bank of Baroda'), ('United Bank of India', 'PNB'), ('Corporation Bank', 'Union Bank'), ('Bharatiya Mahila Bank', 'SBI'),
        ('Vijaya Bank', 'Bank of Baroda'), ('New Bank of India', 'PNB'), ('State Bank of Indore', 'SBI')]

FLASH = [
 ('First bank in India', 'Bank of Hindustan, 1770, Calcutta (Alexander & Co.).'),
 ('Presidency Banks', 'Bank of Bengal (1806/1809), Bank of Bombay (1840), Bank of Madras (1843) – merged in 1921 into Imperial Bank of India.'),
 ('SBI', 'Imperial Bank nationalised in 1955 on the A.D. Gorwala Committee’s recommendation.'),
 ('Associate banks', '8 in 1959 (SBI Subsidiary Banks Act); last 5 + Bharatiya Mahila Bank merged into SBI on 1 April 2017.'),
 ('Nationalisation', '14 banks on 19 July 1969; 6 banks on 15 April 1980.'),
 ('2020 mergers', '10 PSBs into 4 on 1 April 2020 → 12 PSBs.'),
 ('First Swadeshi bank', 'Central Bank of India, 1911.'),
]

QUIZ = [
 ('Which was the first bank in India, and who set it up?', 'Bank of Hindustan, 1770, Calcutta – by Alexander and Company.'),
 ('Which bank was the first purely managed by Indians? Where and when?', 'Punjab National Bank – Lahore, 1894.'),
 ('Which is called the first truly Swadeshi bank?', 'Central Bank of India (1911).'),
 ('Which Indian bank first opened a branch abroad, and where?', 'Bank of India – London, 1946.'),
 ('Name the three Presidency Banks with their years.', 'Bank of Bengal 1806 (as Bank of Calcutta; renamed 1809), Bank of Bombay 1840, Bank of Madras 1843.'),
 ('When were the Presidency Banks merged, and into what?', '1921 – Imperial Bank of India (a private entity).'),
 ('On whose recommendation was the Imperial Bank nationalised as SBI, and when?', 'A.D. Gorwala Committee; 1955.'),
 ('Which Act created SBI’s associate banks, and how many?', 'State Bank of India (Subsidiary Banks) Act, 1959 – eight associate banks.'),
 ('Which two associate banks merged with each other in 1963?', 'State Bank of Bikaner and State Bank of Jaipur → SBBJ.'),
 ('Which associate banks merged into SBI in 2008 and 2010?', 'State Bank of Saurashtra (2008) and State Bank of Indore (2010).'),
 ('Which bank merged into SBI along with the five associates on 1 April 2017?', 'Bharatiya Mahila Bank.'),
 ('How many banks were nationalised on 19 July 1969 and on 15 April 1980?', '14 and 6.'),
 ('Which bank merged into PNB on 4 September 1993?', 'New Bank of India.'),
 ('Which banks merged into Bank of Baroda, and when?', 'Vijaya Bank and Dena Bank – 1 April 2019.'),
 ('Which banks merged into Union Bank of India in 2020?', 'Andhra Bank and Corporation Bank.'),
 ('How many PSBs were there in 2017 and after consolidation?', '27 → 12.'),
 ('Name the six independent PSBs.', 'Indian Overseas Bank, UCO Bank, Bank of Maharashtra, Punjab and Sind Bank, Bank of India, Central Bank of India.'),
 ('What is the FDI limit shown for payments banks?', '74% (as for private banks).'),
]

RAPID = [
 '1770 Bank of Hindustan (first) · 1786 General Bank of India · 1806 Bank of Calcutta → 1809 Bank of Bengal · 1840 Bombay · 1843 Madras.',
 '1921 Presidency banks → Imperial Bank of India (private) · 1955 → SBI (A.D. Gorwala Committee).',
 'PNB 1894 Lahore = first managed purely by Indians · Central Bank of India 1911 = first Swadeshi · Bank of India 1946 London = first branch abroad.',
 '1959: 8 associates (Bikaner, Jaipur, Saurashtra, Indore, Hyderabad, Patiala, Mysore, Travancore) · 1963 SBBJ · 2008 Saurashtra · 2010 Indore · 1 Apr 2017 last 5 + Bharatiya Mahila Bank → SBI.',
 'Nationalisation: 14 banks 19 Jul 1969 (₹50 cr) · 6 banks 15 Apr 1980 (₹200 cr).',
 'Mergers: New Bank of India → PNB (4 Sep 1993) · Vijaya + Dena → BoB (1 Apr 2019) · 1 Apr 2020: OBC + United → PNB, Syndicate → Canara, Allahabad → Indian Bank, Andhra + Corporation → Union.',
 '12 PSBs = 6 merged (SBI, BoB, PNB, Canara, Union, Indian) + 6 independent (IOB, UCO, BoM, P&SB, BoI, Central).',
 'Payments bank FDI 74% · SFB: ₹300 cr, 60% PSL, 10 years’ experience.',
]
