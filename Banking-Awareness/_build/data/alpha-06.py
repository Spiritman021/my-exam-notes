# Saarthi Alpha · Class 6 — from the class PDF (102250_4814071_lc.doc.pdf, 48 slides, all images).
CLASS = 6
TITLE = 'All about RBI'
FULL = 'All about RBI – History of RBI, Central & Local Boards, Governors, Subsidiaries, Printing Presses, Mints, RBI Functions, Training Establishments, Institutes Funded by the Bank, Minimum Reserve System'
COVERS = 'All about RBI (the planned Class 5 topic)'
NOTE = ('The class plan lists “NABARD and PSL Part 1” for Class 6, but this PDF covers <b>All about RBI</b> – the topic planned for Class 5. '
        'The PDFs are running one class behind the plan, so this page keeps your numbering.')

TIMELINE = '''<ol class="tl">
<li><span class="y">1920s</span><b>Hilton-Young Commission</b> (Royal Commission on Indian Currency and Finance) set up</li>
<li><span class="y">1926</span>The commission recommends a <b>central bank</b> for India</li>
<li><span class="y">1934</span><b>RBI Act, 1934</b> passed → RBI is a <b>statutory body</b></li>
<li><span class="y">1 Apr 1935</span>RBI starts operations · paid-up capital <b>₹5 crore</b> · central office in <b>Calcutta</b> · Governor Osborne Smith</li>
<li><span class="y">1937</span>Central office moves permanently to <b>Mumbai</b></li>
<li><span class="y">1943</span><b>C. D. Deshmukh</b> – first Indian Governor</li>
<li><span class="y">1 Jan 1949</span>RBI <b>nationalised</b> – privately owned until then</li>
</ol>'''

S = [
 ('History of the RBI', 'भारतीय रिज़र्व बैंक – from a Royal Commission to a nationalised central bank.', [
  dict(h='Timeline', html='TIMELINE'),
  dict(h='How RBI came into being', tag='hot', pics=[('c6-rbi-timeline', 'RBI history table (slide)')], facts=[
     'The ' + k('Hilton-Young Commission') + ' was the ' + k('Royal Commission on Indian Currency and Finance') + ', set up by the British Government of India in the 1920s.',
     'In ' + k('1926') + ', this commission recommended that the government ' + k('create a central bank') + ' in the country.',
     'RBI started its operations from ' + k('1 April 1935') + '.',
     'It was established via the ' + k('RBI Act, 1934') + ', so it is also known as a ' + k('statutory body') + '.',
     'RBI was established in 1935 with an ' + k('initial paid-up capital of ₹5 crore') + '.',
     'Initially the central office was in ' + k('Calcutta') + ', but it ' + k('permanently moved to Mumbai in 1937') + '.',
     'RBI was ' + k('nationalised on 1 January 1949') + '. Initially it was ' + k('privately owned') + ', then it was owned by the Government of India.',
  ], add=[
     'Nationalisation was done under the <b>Reserve Bank of India (Transfer to Public Ownership) Act, 1948</b>.',
     'RBI’s emblem shows a <b>tiger and a palm tree</b>. Its financial year has run <b>April–March</b> since 2020-21 (it was July–June before).',
  ]),
  dict(h='RBI offices', pics=[('c6-rbi-offices', 'RBI offices across India')], facts=[
     'RBI has ' + k('34 offices') + ' (regional offices and sub-offices) across India.',
  ]),
 ]),
 ('Central Board & Local Boards', 'केंद्रीय बोर्ड और स्थानीय बोर्ड – who runs the RBI.', [
  dict(h='Central Board of Directors', hi='केंद्रीय निदेशक बोर्ड', tag='hot', facts=[
     'The Reserve Bank’s affairs are governed by a ' + k('Central Board of Directors') + '.',
     'The board is ' + k('appointed by the Government of India') + ' in keeping with the RBI Act.',
     'Directors are appointed / nominated for a period of ' + k('four years') + '.',
     'The Central Board has ' + k('21 members') + ':',
     '— ' + k('Governor – 1') + ' · ' + k('Deputy Governors – maximum 4'),
     '— ' + k('10 Directors nominated by the Government') + ' · ' + k('2 Government officials') + ' · ' + k('4 Directors from the Local Boards'),
     'Governor and Deputy Governors are ' + k('full-time') + ': term ' + k('up to 5 years') + ', ' + k('eligible for reappointment') + '.',
  ], table=(['Member', 'Number'], [['Governor', '1'], ['Deputy Governors (max.)', '4'], ['Directors nominated by Govt', '10'], ['Government officials', '2'], ['Directors from Local Boards', '4'], ['<b>Total</b>', '<b>21</b>']]),
   add=['The board is appointed under <b>Section 8</b> of the RBI Act, 1934. The two government officials are usually from the Ministry of Finance (e.g. the Secretary, Department of Economic Affairs, and the Secretary, Department of Financial Services).']),
  dict(h='Who is who today', tag='hot', facts=[
     k('Governor: Sanjay Malhotra') + ' – the ' + k('26th Governor') + '.',
     k('Deputy Governors (4)') + ': ' + k('T. Rabi Sankar') + ', ' + k('Swaminathan J') + ', ' + k('Poonam Gupta') + ', ' + k('Shirish Chandra Murmu') + '.',
  ], add=['Sanjay Malhotra took charge on 11 December 2024, succeeding Shaktikanta Das (25th).']),
  dict(h='Local Boards', hi='स्थानीय बोर्ड', facts=[
     'Constituted for the ' + k('Western, Eastern, Northern and Southern Areas') + '.',
     'They ' + k('consist of five members each') + '.',
     'Members are ' + k('appointed by the Central Government') + ' and hold office for a term of ' + k('four years') + '.',
     k('4 Local Boards') + ': ' + k('Delhi, Mumbai, Chennai, Kolkata') + '.',
  ], trap='Two different “4”s: <b>4 Local Boards</b> (Delhi, Mumbai, Chennai, Kolkata) and <b>4 Directors from Local Boards</b> on the Central Board – one from each. Directors serve <b>4 years</b>; Governor/DGs up to <b>5 years</b>.'),
 ]),
 ('Governors of RBI', 'आरबीआई के गवर्नर – the three firsts.', [
  dict(h='The first three Governors', tag='hot', table=(['No.', 'Governor', 'Term', 'Note'], [
     ['1st', k('Sir Osborne Arkell Smith'), '1 April 1935 – 30 June 1937', 'An ' + k('Australian banker') + ' – the first Governor'],
     ['2nd', k('Sir James Braid Taylor'), '1 July 1937 – 17 February 1943', 'Held office until his ' + k('death')],
     ['3rd', k('Sir Chintaman Dwarakanath Deshmukh'), '11 August 1943 – 30 June 1949', 'Indian civil servant; ' + k('first Indian Governor') + ', appointed in 1943 by the British Raj'],
  ]), add=['C. D. Deshmukh later became India’s Finance Minister. Manmohan Singh (15th Governor) is the only Governor who also became Prime Minister.'],
   trap='C. D. Deshmukh was Governor when RBI was <b>nationalised</b> (1 January 1949), so he is also the first Governor of the nationalised RBI.'),
 ]),
 ('Subsidiaries of RBI', 'पूर्ण स्वामित्व वाली सहायक कंपनियाँ – five wholly owned subsidiaries.', [
  dict(h='The five wholly owned subsidiaries', tag='hot', sort=False, facts=[
     k('DICGC') + ' – Deposit Insurance and Credit Guarantee Corporation',
     k('BRBNMPL') + ' – Bharatiya Reserve Bank Note Mudran Private Limited',
     k('ReBIT') + ' – Reserve Bank Information Technology Private Limited',
     k('IFTAS') + ' – Indian Financial Technology and Allied Services',
     k('RBIH') + ' – Reserve Bank Innovation Hub',
  ], table=(['Subsidiary', 'Set up', 'HQ', 'Role'], [
     ['DICGC', k('15 July 1978'), 'Mumbai', 'Insures principal + interest up to ' + k('₹5 lakh')],
     ['BRBNMPL', k('3 February 1995'), k('Bengaluru'), 'Runs 2 note presses – ' + k('Mysore') + ' (Karnataka) and ' + k('Salboni') + ' (West Bengal)'],
     ['ReBIT', k('2016'), 'Navi Mumbai (as taught)', 'RBI’s ' + k('IT and cyber security') + ' needs'],
     ['IFTAS', k('February 2015'), 'Mumbai', 'Designs, deploys & supports ' + k('IT services for RBI, banks and FIs')],
     ['RBIH', k('March 2022'), k('Bengaluru'), k('Section 8 company') + ' (Companies Act 2013), ' + k('₹100 crore') + ' initial capital, to nurture financial innovation'],
  ]), add=['DICGC was formed by merging the Deposit Insurance Corporation (1962) and the Credit Guarantee Corporation of India (1971). The ₹5 lakh cover applies from 4 February 2020 (it was ₹1 lakh before).']),
 ]),
 ('Note Printing Presses, Mints & Currency Issue', 'नोट मुद्रण प्रेस – who prints, who mints, who issues.', [
  dict(h='Four note printing presses', hi='नोट मुद्रण प्रेस', tag='hot', facts=[
     'Indian currency notes are printed at ' + k('four') + ' secure presses managed by ' + k('SPMCIL and BRBNMPL') + ': Nashik (Maharashtra), Dewas (Madhya Pradesh), Mysore (Karnataka), Salboni (West Bengal).',
     'Two presses are owned by the ' + k('Government of India (SPMCIL)') + ' and two by the ' + k('Reserve Bank') + ' through its wholly owned subsidiary BRBNMPL.',
     k('Government-owned') + ': ' + k('Nashik') + ' (Western India) and ' + k('Dewas') + ' (Central India).',
     k('RBI-owned') + ': ' + k('Mysore') + ' (Southern India) and ' + k('Salboni') + ' (Eastern India).',
  ]),
  dict(h='Who issues what', tag='hot', sort=True, facts=[
     k('Government of India') + ' issues ' + k('coins and the ₹1 note') + '.',
     k('Reserve Bank of India') + ' issues ' + k('₹2 and above') + ' notes.',
     'RBI can issue bank notes up to a ' + k('maximum denomination of ₹10,000') + ' as per the RBI Act, 1934.',
     'As per the ' + k('Coinage Act, 2011') + ', coins can be of a ' + k('maximum denomination of ₹1,000') + '.',
  ], add=['The ₹1 note is signed by the <b>Finance Secretary</b>; all other notes by the <b>RBI Governor</b>. RBI issues notes under <b>Section 22</b> of the RBI Act.'],
   trap='Notes up to <b>₹10,000</b> (RBI Act 1934) vs coins up to <b>₹1,000</b> (Coinage Act 2011). Don’t swap the Acts.'),
  dict(h='SPMCIL', hi='भारत प्रतिभूति मुद्रण एवं निर्माण निगम', facts=[
     'Security Printing & Minting Corporation of India Ltd is a ' + k('Central Public Sector Enterprise (CPSE)') + ' under the ' + k('Ministry of Finance') + '.',
     k('Founded: 13 January 2006') + ' · ' + k('Headquarters: New Delhi') + '.',
     'It operates ' + k('9 production units') + ': ' + k('4 mints') + ', ' + k('2 currency note presses') + ', ' + k('2 security printing presses') + ' and ' + k('1 security paper mill') + '.',
     'Coins are minted in ' + k('four mints') + ' owned by the Government: ' + k('Mumbai') + ' (Maharashtra), ' + k('Kolkata') + ' (West Bengal), ' + k('Hyderabad') + ' (Telangana), ' + k('Noida') + ' (Uttar Pradesh).',
     k('India Security Press (ISP)') + ' – Nashik, Maharashtra · ' + k('Security Printing Press (SPP)') + ' – Hyderabad, Telangana · ' + k('Security Paper Mill') + ' – ' + k('Narmadapuram') + ', Madhya Pradesh.',
  ], add=['The two SPMCIL currency note presses are the Currency Note Press, Nashik and the Bank Note Press, Dewas. Narmadapuram was earlier called Hoshangabad.']),
 ]),
 ('RBI’s Functions', 'आरबीआई के कार्य – seven roles.', [
  dict(h='Seven functions', tag='hot', pics=[('c6-functions', 'RBI’s functions')], facts=[
     k('Maker of Monetary Policy') + ' · ' + k('Issuer of Currency') + ' · ' + k('Banker to the Government') + ' · ' + k('Banker to Banks') + ' · ' + k('Foreign Exchange Management') + ' · ' + k('Controller of Credit') + ' · ' + k('Lender of Last Resort (LOLR)') + '.',
  ]),
  dict(h='Maker of Monetary Policy', facts=[
     'Under the RBI Act, 1934 (' + k('as amended in 2016') + '), RBI conducts monetary policy with the primary objective of ' + k('price stability') + ' while keeping in mind the objective of ' + k('growth') + '.',
     k('Fiscal policy') + ' is formulated by the ' + k('Ministry of Finance') + ', Government of India.',
  ], add=['The 2016 amendment brought in flexible inflation targeting (CPI 4% ± 2%) and the Monetary Policy Committee – taught in the Monetary Policy classes.']),
  dict(h='Issuer of Currency', facts=[
     'The Reserve Bank is the nation’s ' + k('sole note issuing authority') + '.',
     'The Government of India is the ' + k('issuing authority of coins') + ' and supplies coins to RBI on demand.',
     'RBI ' + k('puts the coins into circulation') + ' on behalf of the Central Government.',
  ]),
  dict(h='Banker to the Government', tag='hot', facts=[
     'RBI is the banker of the ' + k('Central Government') + ':',
     '— ' + k('Section 20') + ': RBI must accept and hold the Central Government’s money.',
     '— ' + k('Section 21') + ': RBI can make payments and manage all banking work for the Government.',
     'RBI is the banker of the ' + k('State Governments / UTs') + ':',
     '— ' + k('Section 21A') + ': RBI acts as banker to State Governments ' + k('by agreement') + '.',
     '— All States / UTs use RBI as banker ' + k('except Sikkim') + '.',
  ]),
  dict(h='Banker to Banks', facts=[
     'The current accounts of banks are opened in ' + k('e-Kuber') + ' (the ' + k('CBS of RBI') + ').',
     'RBI gives ' + k('short-term loans and advances') + ' to select banks, when necessary, to facilitate lending to specific sectors and purposes.',
  ]),
  dict(h='Foreign Exchange Management', facts=[
     'RBI issues licences to banks and other institutions to act as ' + k('Authorised Dealers') + ' in the foreign exchange market.',
     'RBI is the ' + k('custodian of the country’s foreign exchange reserves') + ' and manages their investment.',
  ], add=['RBI manages forex under <b>FEMA, 1999</b> (which replaced FERA, 1973).']),
  dict(h='Controller of Credit', facts=[
     'RBI uses monetary-policy tools to ' + k('regulate money supply, control inflation and foster growth') + '.',
     k('Quantitative') + ' methods: ' + k('repo rate, CRR') + ' · ' + k('Qualitative / selective') + ' measures: ' + k('margin requirements, moral suasion') + '.',
  ]),
  dict(h='Lender of Last Resort (LOLR)', facts=[
     'RBI is called the ' + k('lender of last resort') + ' for banks.',
     'If a bank is ' + k('healthy but faces a temporary cash shortage') + ', RBI gives ' + k('emergency funds') + '.',
     'This help is given ' + k('when no other bank is willing to lend') + '.',
     'Purpose: to ' + k('protect depositors’ money') + '. It ' + k('prevents the bank from failing') + ' and protects the banking system and financial stability.',
  ]),
 ]),
 ('Training Establishments & Institutes Funded', 'प्रशिक्षण संस्थान और बैंक द्वारा वित्तपोषित संस्थान', [
  dict(h='Five training establishments', tag='hot', facts=[
     'RBI has ' + k('five training establishments') + '.',
     k('Four') + ' are part of the Reserve Bank: ' + k('RBI Academy') + ', ' + k('College of Agricultural Banking') + ', ' + k('Reserve Bank of India Staff College') + ' and ' + k('College of Supervisors') + '.',
     'One is ' + k('autonomous') + ' (self-governed but connected to RBI): ' + k('Institute for Development and Research in Banking Technology (IDRBT)') + '.',
  ], add=['Locations: RBI Academy – Mumbai · College of Agricultural Banking – Pune · RBI Staff College – Chennai · College of Supervisors – Mumbai · IDRBT – Hyderabad.']),
  dict(h='Institutes funded by the Bank', tag='hot', pics=[('c6-institutes', 'Institutes funded by the Bank')], table=(['Institute', 'Full name', 'RBI role', 'Main purpose'], [
     [k('CAFRAL'), 'Centre for Advanced Financial Research and Learning', k('Fully funded by RBI'), 'Advanced financial research & training of senior bankers'],
     [k('IGIDR'), 'Indira Gandhi Institute of Development Research', k('Fully funded by RBI'), 'Economic and development research'],
     [k('IIBM'), 'Indian Institute of Bank Management', 'RBI is a ' + k('sponsor') + ' along with other banks and FIs', 'Training and management development of bank officers'],
     [k('NIBM'), 'National Institute of Bank Management', 'RBI is an ' + k('ordinary member') + ' along with other banks and FIs', 'Banking education, training and research'],
  ]), add=['Locations: CAFRAL – Mumbai · IGIDR – Mumbai · IIBM – Guwahati · NIBM – Pune.']),
 ]),
 ('Minimum Reserve System', 'न्यूनतम भण्डारण प्रणाली – the backing for currency RBI issues.', [
  dict(h='Minimum Reserve System', tag='hot', facts=[
     'Under this system, RBI should have a ' + k('minimum reserve of ₹200 crore') + '.',
     'Of which ' + k('gold ₹115 crore') + ' and ' + k('₹85 crore in foreign exchange') + '.',
     'RBI ' + k('issues currency on the basis of the Minimum Reserve System') + '.',
  ], add=['India adopted the Minimum Reserve System in <b>1957</b>, replacing the Proportional Reserve System (1935–1956). The rule is in <b>Section 33</b> of the RBI Act.'],
   trap='₹200 crore = ₹115 crore gold + ₹85 crore forex. Don’t mix with RBI’s ₹5 crore initial paid-up capital.'),
 ]),
]

SORT_OPTS = ['Government', 'RBI']
SORT_Q = 'Quick check – who issues it?'
SORT = [('₹1 note', 'Government'), ('₹2 note', 'RBI'), ('₹10 coin', 'Government'), ('₹500 note', 'RBI'), ('₹1,000 coin (max. under Coinage Act)', 'Government'), ('₹10,000 note (max. under RBI Act)', 'RBI')]

FLASH = [
 ('Hilton-Young Commission', 'Royal Commission on Indian Currency and Finance; recommended a central bank in 1926.'),
 ('RBI basics', 'RBI Act 1934 · operations 1 April 1935 · ₹5 crore paid-up · Calcutta → Mumbai 1937 · nationalised 1 Jan 1949.'),
 ('Central Board', '21 members: Governor 1, DGs max 4, 10 govt-nominated, 2 govt officials, 4 from Local Boards.'),
 ('RBI subsidiaries', 'DICGC, BRBNMPL, ReBIT, IFTAS, RBIH.'),
 ('Note presses', 'Govt (SPMCIL): Nashik, Dewas · RBI (BRBNMPL): Mysore, Salboni.'),
 ('Mints', 'Mumbai, Kolkata, Hyderabad, Noida (all Govt / SPMCIL).'),
 ('LOLR', 'RBI lends emergency funds to a healthy bank short of cash when no other bank will lend.'),
 ('Minimum Reserve System', '₹200 crore: ₹115 crore gold + ₹85 crore forex.'),
]

QUIZ = [
 ('Which commission recommended a central bank for India, and when?', 'The Hilton-Young Commission (Royal Commission on Indian Currency and Finance), 1926.'),
 ('Under which Act was RBI set up, and when did it start operations?', 'RBI Act, 1934; 1 April 1935.'),
 ('What was RBI’s initial paid-up capital?', '₹5 crore.'),
 ('Where was RBI’s central office first, and when did it move to Mumbai?', 'Calcutta; 1937.'),
 ('When was RBI nationalised?', '1 January 1949.'),
 ('How many members are on RBI’s Central Board? Break it up.', '21 – Governor 1, Deputy Governors up to 4, 10 government-nominated directors, 2 government officials, 4 directors from Local Boards.'),
 ('Term of Central Board directors vs Governor?', 'Directors 4 years; Governor and Deputy Governors up to 5 years, eligible for reappointment.'),
 ('Name the four Local Boards and their size.', 'Delhi, Mumbai, Chennai, Kolkata – five members each, four-year term.'),
 ('Who is RBI’s current Governor and which number?', 'Sanjay Malhotra, 26th Governor.'),
 ('Name the four Deputy Governors.', 'T. Rabi Sankar, Swaminathan J, Poonam Gupta, Shirish Chandra Murmu.'),
 ('Who was RBI’s first Governor, and his nationality?', 'Sir Osborne Arkell Smith, an Australian banker (1935–37).'),
 ('Who was the first Indian Governor of RBI?', 'Sir C. D. Deshmukh (11 August 1943 – 30 June 1949).'),
 ('Name RBI’s five wholly owned subsidiaries.', 'DICGC, BRBNMPL, ReBIT, IFTAS, RBIH.'),
 ('DICGC: established when, and what cover does it give?', '15 July 1978; principal + interest up to ₹5 lakh.'),
 ('Where are RBI’s own note presses?', 'Mysore (Karnataka) and Salboni (West Bengal), via BRBNMPL.'),
 ('Where are the Government’s note presses?', 'Nashik (Maharashtra) and Dewas (Madhya Pradesh), via SPMCIL.'),
 ('Name India’s four mints.', 'Mumbai, Kolkata, Hyderabad, Noida.'),
 ('What is the maximum denomination of a note and of a coin?', 'Note ₹10,000 (RBI Act 1934); coin ₹1,000 (Coinage Act 2011).'),
 ('When was SPMCIL founded and how many units does it run?', '13 January 2006; 9 units – 4 mints, 2 currency note presses, 2 security printing presses, 1 security paper mill.'),
 ('Which sections make RBI banker to the Centre and to the States?', 'Sections 20 and 21 (Centre); Section 21A (States, by agreement).'),
 ('Which state does not use RBI as its banker?', 'Sikkim.'),
 ('What is e-Kuber?', 'RBI’s Core Banking Solution, where banks’ current accounts are held.'),
 ('Which RBI training establishment is autonomous?', 'IDRBT – Institute for Development and Research in Banking Technology.'),
 ('Which institutes are fully funded by RBI?', 'CAFRAL and IGIDR.'),
 ('Under the Minimum Reserve System, how much reserve must RBI keep, and in what form?', '₹200 crore – ₹115 crore gold and ₹85 crore foreign exchange.'),
]

RAPID = [
 'Hilton-Young Commission (1926) → RBI Act 1934 → operations 1 Apr 1935, ₹5 cr capital, Calcutta → Mumbai 1937 → nationalised 1 Jan 1949. Statutory body. 34 offices.',
 'Central Board 21 = 1 Governor + 4 DGs + 10 nominated + 2 govt officials + 4 from Local Boards; directors 4 yrs, Governor/DG ≤ 5 yrs.',
 'Local Boards (5 members, 4 yrs): Delhi, Mumbai, Chennai, Kolkata.',
 'Governor Sanjay Malhotra (26th); DGs T. Rabi Sankar, Swaminathan J, Poonam Gupta, Shirish Chandra Murmu.',
 'Governors: Osborne Smith (Australian, 1935–37) · James Braid Taylor (1937–43, died in office) · C. D. Deshmukh (first Indian, 1943–49).',
 'Subsidiaries: DICGC 15 Jul 1978 Mumbai ₹5 lakh · BRBNMPL 3 Feb 1995 Bengaluru (Mysore, Salboni) · ReBIT 2016 · IFTAS Feb 2015 Mumbai · RBIH Mar 2022 Bengaluru ₹100 cr.',
 'Presses: Govt Nashik + Dewas; RBI Mysore + Salboni. Mints: Mumbai, Kolkata, Hyderabad, Noida. ISP Nashik, SPP Hyderabad, paper mill Narmadapuram. SPMCIL 13 Jan 2006, New Delhi, 9 units.',
 'Govt: coins + ₹1 note; RBI: ₹2 and above. Max note ₹10,000 (RBI Act 1934); max coin ₹1,000 (Coinage Act 2011).',
 'Functions: monetary policy · currency · banker to govt (Sec 20, 21, 21A; all but Sikkim) · banker to banks (e-Kuber) · forex · credit control · LOLR.',
 'Training: RBI Academy, College of Agricultural Banking, RBI Staff College, College of Supervisors + autonomous IDRBT. Funded: CAFRAL & IGIDR fully; IIBM sponsor; NIBM ordinary member.',
 'Minimum Reserve System: ₹200 cr = ₹115 cr gold + ₹85 cr forex.',
]
