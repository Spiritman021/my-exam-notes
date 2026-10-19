# Saarthi Alpha · Class 3 — from the class PDF (102250_4814068_lc.doc.pdf, 34 slides, all images).
CLASS = 3
TITLE = 'Loans & Advances, Payments Bank & Small Finance Bank'
FULL = 'Loans and Advances – Cash Credit, Overdraft, Bill Discounted (rest of Class 2); Indian Banking System Part 2 – Payment Bank and Small Finance Bank'
NOTE = 'The first part of this PDF (Loans and Advances) finishes Class 2’s topic “Types of Deposit and Advances”.'

S = [
 ('Loans and Advances', 'ऋण और अग्रिम – what a bank does with the deposits it collects.', [
  dict(h='Where deposit money goes', tag='bank', pics=[('c3-loan', 'Loan'), ('c3-business-loan', 'Business loan')], facts=[
     'The money collected through deposits is used ' + k('to give loans') + ' like ' + k('personal, home, car, education and business loans') + '.',
     'Banks charge interest on these loans. The ' + k('difference between interest earned and interest paid') + ' is a ' + k('major source of profit') + '.',
  ], add=[
     'That difference is called the bank’s <b>spread</b>. Net interest income divided by earning assets is the <b>Net Interest Margin (NIM)</b>.',
  ]),
  dict(h='Types of Advances', hi='अग्रिमों के प्रकार', tag='hot', facts=[
     'Three types taught: ' + k('Cash Credit') + ' (नकद साख), ' + k('Overdraft') + ' (अधिविकर्ष) and ' + k('Bill Discounted') + ' (बिल बट्टा).',
  ]),
 ]),
 ('Cash Credit (CC)', 'नकद साख – a working-capital limit for businesses.', [
  dict(h='Cash Credit', hi='नकद साख', tag='bank', facts=[
     'Cash Credit is an arrangement whereby the bank allows the borrower to ' + k('withdraw amount up to a certain specified limit') + '.',
     'Interest is charged on the ' + k('amount actually withdrawn') + ' (not on the whole limit).',
     'Cash Credit is granted as per ' + k('terms and conditions agreed with the customer') + '.',
     'It is a ' + k('short-term loan') + ' approved by banks for ' + k('businesses, financial institutions and companies') + ' to meet their ' + k('working capital requirements') + '.',
     'CC is a source of short-term finance for businesses and companies.',
     'Cash credits are also called ' + k('working capital loans') + ', as they fund the instant cash requirements of organisations or the purchase of ' + k('current assets') + '.',
     'Cash credit is available for a shorter period of time and at a ' + k('significantly lower interest rate than overdrafts') + '.',
  ], add=[
     '<b>Hypothecation</b> = the stock / inventory is the security, but it stays with the borrower (the bank holds only a charge on it).',
  ]),
 ]),
 ('Overdraft (OD)', 'अधिविकर्ष – drawing more than you have in your account.', [
  dict(h='Overdraft', hi='अधिविकर्ष', tag='bank', facts=[
     'Overdraft is also a ' + k('credit facility granted by a bank') + '.',
     'A customer who has a ' + k('current account') + ' with the bank is allowed to ' + k('withdraw more than the credit balance') + ' in the account.',
     'Overdraft is an ' + k('extension of credit') + ' to ' + k('current and savings account holders') + ' in cases where the total balance of the account ' + k('becomes zero') + '.',
  ], add=[
     'Example: PMJDY accounts carry an overdraft facility of up to ₹10,000.',
  ]),
  dict(h='Cash Credit vs Overdraft', tag='hot', table=(['Basis', 'Cash Credit (CC)', 'Overdraft (OD)'], [
     ['Interest rate', 'Interest rate is ' + k('lower') + ' compared to overdraft', 'Interest rate is ' + k('comparatively higher')],
     ['Security / basis', 'Availed on ' + k('hypothecation of stocks and inventory'), 'Availed based on ' + k('credit history, bank relationship and securities') + ' like FDs, insurance policies, etc.'],
     ['Purpose', 'Can be used ' + k('only for business purposes'), 'Can be used for ' + k('any purpose') + ', including business'],
     ['Loan amount determination', 'Based on ' + k('volume / value of stocks and inventory'), 'Based on ' + k('financial statements and security deposit')],
     ['Account requirement', k('New cash credit account') + ' needs to be opened', 'Facility is given on an ' + k('existing bank account')],
     ['Tenure', 'Generally sanctioned for a ' + k('minimum of 1 year'), 'Can be for ' + k('shorter tenure') + ' (month / quarter), ' + k('maximum 1 year')],
     ['Eligible borrowers', 'Individuals, retailers, traders, manufacturers, distributors, companies, partnerships, sole proprietors, LLPs, etc.', k('Only account holders') + ' of the respective bank'],
     ['Sanction basis', 'Based on ' + k('business performance and market situation'), 'Based on ' + k('financial statements and credit history')],
  ]), trap='CC = <b>business only</b>, secured by <b>stock</b>, <b>cheaper</b>, new account, minimum 1 year. OD = <b>any purpose</b>, on an <b>existing</b> account, <b>costlier</b>, maximum 1 year.'),
 ]),
 ('Bill Discounted (BD)', 'बिल बट्टा – getting the money for a bill before its due date.', [
  dict(h='Bill Discounting', hi='बिल बट्टा', tag='bank', facts=[
     'Banks provide ' + k('short-term finance') + ' by discounting bills: they pay the amount ' + k('before the due date') + ' of the bills, after ' + k('deducting a certain rate of discount') + '.',
     'The party gets the funds ' + k('without waiting for the due date') + ' of the bills.',
     'If any bill is ' + k('dishonoured on the due date') + ', the bank can ' + k('recover the amount from the customer') + '.',
  ]),
  dict(h='Process of Bill Discounting – 7 steps', pics=[('c3-bill-process', 'Process of Bill Discounting')], facts=[
     '<b>1 Supply</b> – goods / services delivered.',
     '<b>2 Invoice</b> – raised by the seller.',
     '<b>3 Acceptance</b> – buyer acknowledges the invoice.',
     '<b>4 Application</b> – seller approaches a financial institution.',
     '<b>5 Verification</b> – the institution checks the buyer’s credit.',
     '<b>6 Disbursement</b> – funds given to the seller ' + k('minus the discount') + '.',
     '<b>7 Repayment</b> – the ' + k('buyer pays the institution on the due date') + '.',
  ], add=[
     'For MSMEs, RBI runs online invoice-discounting platforms called <b>TReDS</b> (Trade Receivables Discounting System).',
  ]),
 ]),
 ('Payments Bank', 'भुगतान बैंक – Indian Banking System, Part 2.', [
  dict(h='Payments Bank – what it can and cannot do', hi='भुगतान बैंक', tag='hot', pics=[('c3-payments-bank', 'Payments bank'), ('c3-airtel-pb', 'Airtel Payments Bank – the first one')], facts=[
     'Payments Bank ' + k('can accept a Demand Deposit (CASA)') + '.',
     'It ' + k('cannot accept a Term Deposit') + ' (written “RAFA” on the slide – i.e. fixed / recurring deposits).',
     'It can accept deposits of ' + k('up to ₹2 lakh per customer') + '.',
     'Payments Bank ' + k('cannot give loans') + '.',
     'It provides a ' + k('Debit Card (ATM card)') + '.',
     k('Minimum capital') + ' required to open this bank is ' + k('₹100 crore') + '.',
     k('25%') + ' of a Payments Bank’s branches must be in the ' + k('unbanked rural area') + '.',
     k('Foreign shareholding') + ' is permitted as per the ' + k('rule for FDI in private banks') + '.',
  ], add=[
     'Recommended by the <b>Nachiket Mor Committee</b>; RBI issued the guidelines in <b>November 2014</b>.',
     'The deposit limit was <b>₹1 lakh</b> at the start and was raised to <b>₹2 lakh</b> in 2021.',
     'It <b>cannot issue credit cards</b>, and must keep at least <b>75%</b> of its demand deposits in government securities / treasury bills (SLR securities).',
  ], trap='Payments bank: <b>debit card yes, credit card no</b>; <b>savings & current yes, FD/RD no</b>; <b>loans no</b>.'),
  dict(h='Payments Bank – feature table', table=(['Feature', 'Details'], [
     ['Acceptance of Demand Deposit (CASA)', k('Yes')],
     ['Acceptance of Term Deposit', k('No')],
     ['Maximum deposit limit per customer', k('₹2 lakh')],
     ['Loan provision', k('Not allowed')],
     ['Provision of Debit Card (ATM card)', 'Yes'],
     ['Minimum capital requirement', k('₹100 crore')],
     ['Branches in unbanked rural areas', 'At least ' + k('25%') + ' of total branches'],
     ['Foreign shareholding', 'Permitted, as per FDI rules in private banks'],
  ])),
  dict(h='The 6 Payments Banks', tag='hot', table=(['S. No.', 'Payments Bank'], [
     ['1', k('Airtel Payments Bank Ltd')],
     ['2', k('India Post Payments Bank Ltd')],
     ['3', 'FINO Payments Bank Ltd'],
     ['4', 'Paytm Payments Bank Ltd'],
     ['5', 'Jio Payments Bank Ltd'],
     ['6', 'NSDL Payments Bank Limited'],
  ]), add=[
     'Airtel Payments Bank was the <b>first</b> to start operations (2017). India Post Payments Bank is fully owned by the Government (Department of Posts).',
     'FINO and Paytm are highlighted on the slide. Paytm Payments Bank has been barred by RBI from taking fresh deposits since <b>March 2024</b>.',
  ]),
 ]),
 ('Small Finance Bank (SFB)', 'लघु वित्त बैंक – deposits and loans for small borrowers.', [
  dict(h='Small Finance Bank – the rules', hi='लघु वित्त बैंक', tag='hot', facts=[
     k('Eligibility') + ': ' + k('10 years’ experience in banking') + '.',
     'Small banks ' + k('offer deposits as well as provide loans') + '.',
     k('Minimum capital') + ' to open this bank is ' + k('₹300 crore') + '.',
     'Foreign shareholding is permitted as per the rule for FDI in private banks.',
     k('25%') + ' of an SFB’s branches must be in the ' + k('unbanked rural area') + '.',
     'SFBs have to lend ' + k('60% of their credit to the Priority Sector') + '.',
  ], add=[
     'Also from RBI’s 2014 guidelines. At least <b>50%</b> of an SFB’s loan portfolio must be loans of up to <b>₹25 lakh</b>.',
     'The first SFB to start was <b>Capital Small Finance Bank</b> (2016).',
  ], trap='Capital: Payments Bank <b>₹100 crore</b>, Small Finance Bank <b>₹300 crore</b> (as taught). Older books may show ₹100 crore or ₹200 crore for SFBs, from earlier RBI rules. Use the class figure, but if an option says “₹200 crore”, remember it comes from the 2019 rules.'),
  dict(h='Small Finance Bank – feature table', table=(['Feature', 'Details'], [
     ['Eligibility', '10 years’ experience in banking'],
     ['Services offered', k('Deposits and loans')],
     ['Minimum capital requirement', k('₹300 crore')],
     ['Foreign shareholding', 'Permitted, as per FDI rules in private banks'],
     ['Branches in unbanked rural areas', 'At least 25% of total branches'],
     ['Mandatory credit allocation to Priority Sector', k('60% of their credit')],
  ])),
  dict(h='The 11 Small Finance Banks', tag='hot', table=(['S. No.', 'Small Finance Bank'], [
     ['1', 'Au Small Finance Bank Ltd'], ['2', 'Capital Small Finance Bank Ltd'], ['3', 'Equitas Small Finance Bank Ltd'],
     ['4', 'ESAF Small Finance Bank Ltd'], ['5', 'Suryoday Small Finance Bank Ltd'], ['6', 'Ujjivan Small Finance Bank Ltd'],
     ['7', 'Utkarsh Small Finance Bank Ltd'], ['8', 'Slice Small Finance Bank Ltd'], ['9', 'Jana Small Finance Bank Ltd'],
     ['10', 'Shivalik Small Finance Bank Ltd'], ['11', 'Unity Small Finance Bank Ltd'],
  ]), add=[
     '<b>Slice SFB</b> is the former North East Small Finance Bank (merged with the fintech slice). <b>Shivalik</b> was the first urban co-operative bank to become an SFB. <b>Unity SFB</b> took over the failed PMC Bank.',
  ]),
  dict(h='Payments Bank vs Small Finance Bank – side by side', sort=True, table=(['Point', 'Payments Bank', 'Small Finance Bank'], [
     ['Deposits', 'Demand deposits (CASA) only, up to ₹2 lakh', 'All deposits'],
     ['Loans', k('No'), k('Yes')],
     ['Minimum capital', '₹100 crore', '₹300 crore'],
     ['Unbanked rural branches', '25%', '25%'],
     ['Priority-sector lending', '— (no loans)', '60% of credit'],
     ['Foreign shareholding', 'As per private-bank FDI rules', 'As per private-bank FDI rules'],
  ])),
 ]),
]

SORT_OPTS = ['Payments Bank', 'SFB', 'Both']
SORT_Q = 'Quick check – Payments Bank, Small Finance Bank, or both?'
SORT = [('Can give loans', 'SFB'), ('Deposit cap of ₹2 lakh per customer', 'Payments Bank'), ('25% branches in unbanked rural areas', 'Both'),
        ('Minimum capital ₹100 crore', 'Payments Bank'), ('Must lend 60% to priority sector', 'SFB'), ('Foreign shareholding as per private-bank FDI rules', 'Both'),
        ('Can accept fixed deposits', 'SFB'), ('Minimum capital ₹300 crore', 'SFB')]

FLASH = [
 ('Cash Credit', 'Short-term working-capital limit for businesses; withdraw up to a limit; interest only on amount used; secured by stock.'),
 ('Overdraft', 'Credit facility to withdraw more than the balance in an existing current/savings account.'),
 ('Bill Discounting', 'Bank pays a bill before its due date after deducting a discount; recovers from customer if dishonoured.'),
 ('Payments Bank', 'CASA only (≤ ₹2 lakh), no loans, debit card yes, capital ₹100 crore, 25% unbanked rural branches.'),
 ('Small Finance Bank', 'Deposits + loans, capital ₹300 crore, 60% PSL, 25% unbanked rural branches, 10 years’ banking experience.'),
 ('Spread', 'Interest earned on loans minus interest paid on deposits – a bank’s main profit.'),
]

QUIZ = [
 ('What are the three types of advances taught?', 'Cash Credit, Overdraft and Bill Discounted.'),
 ('In cash credit, interest is charged on what amount?', 'Only on the amount actually withdrawn.'),
 ('Cash credits are also called what, and why?', 'Working capital loans – they fund instant cash needs or the purchase of current assets.'),
 ('Which is cheaper – cash credit or overdraft?', 'Cash credit (lower interest rate).'),
 ('What security backs a cash credit?', 'Hypothecation of stocks and inventory.'),
 ('Which facility can be used for any purpose – CC or OD?', 'Overdraft. Cash credit is for business purposes only.'),
 ('Which facility needs a new account to be opened?', 'Cash credit. Overdraft is given on an existing account.'),
 ('Tenure: CC vs OD?', 'CC – generally a minimum of 1 year; OD – shorter (month/quarter), maximum 1 year.'),
 ('In bill discounting, what happens if the bill is dishonoured?', 'The bank recovers the amount from the customer.'),
 ('In the bill-discounting process, who repays the institution on the due date?', 'The buyer (step 7).'),
 ('Can a payments bank accept fixed deposits or give loans?', 'No to both. It accepts only demand deposits (CASA).'),
 ('Maximum deposit per customer in a payments bank?', '₹2 lakh.'),
 ('Minimum capital for a payments bank and a small finance bank (as taught)?', '₹100 crore and ₹300 crore.'),
 ('What share of branches must payments banks and SFBs have in unbanked rural areas?', 'At least 25%.'),
 ('What share of credit must an SFB give to the priority sector?', '60%.'),
 ('Eligibility to promote an SFB?', '10 years’ experience in banking.'),
 ('Name the six payments banks.', 'Airtel, India Post, FINO, Paytm, Jio and NSDL Payments Bank.'),
 ('How many small finance banks are listed in the class? Name any four.', '11 – e.g. AU, Capital, Equitas, ESAF, Suryoday, Ujjivan, Utkarsh, Slice, Jana, Shivalik, Unity.'),
]

RAPID = [
 'Bank profit = interest earned on loans − interest paid on deposits (spread).',
 'Advances: Cash Credit · Overdraft · Bill Discounted.',
 'CC: business only, stock hypothecation, lower rate, new account, ≥ 1 year, interest on amount withdrawn.',
 'OD: any purpose, existing CA/SA, higher rate, ≤ 1 year, based on credit history / FDs / policies.',
 'Bill discounting: paid before due date minus discount; dishonour → recovered from customer. 7 steps: supply → invoice → acceptance → application → verification → disbursement → repayment.',
 'Payments Bank: CASA only, ≤ ₹2 lakh, no loans, debit card yes, ₹100 crore capital, 25% unbanked rural branches, FDI as private banks. 6 banks: Airtel, India Post, FINO, Paytm, Jio, NSDL.',
 'SFB: deposits + loans, ₹300 crore capital (as taught), 60% PSL, 25% unbanked rural branches, 10 years’ banking experience. 11 banks.',
]
