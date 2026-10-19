# Saarthi Alpha · Class 2 — from the class PDF (document (1).pdf, 30 slides).
CLASS = 2
TITLE = 'BSBD Account, Bank & Types of Deposit'
FULL = 'No-Frills / BSBD Account (rest of Class 1), Indian Banking System Part 1 – Definition of Bank, Types of Deposit'
NOTE = 'The class plan also lists History of Bank, Nationalisation and Merger of Banks; those slides are not in this PDF.'

DEPOSIT_TREE = '''<figure class="diagram"><svg viewBox="0 0 640 250" role="img" aria-label="Types of deposit: demand deposit (saving, current) and term deposit (recurring, fixed)">
<rect class="bx" x="230" y="10" width="180" height="44" rx="6"/><text class="b" x="320" y="38" text-anchor="middle">Types of Deposit</text>
<path class="ln" d="M320 54 V80 H160 V104 M320 80 H480 V104"/>
<rect class="bx ac" x="70" y="104" width="180" height="50" rx="6"/><text class="b" x="160" y="126" text-anchor="middle">Demand Deposit</text><text class="mut" x="160" y="145" text-anchor="middle">माँग जमा · any time</text>
<rect class="bx or" x="390" y="104" width="180" height="50" rx="6"/><text class="b" x="480" y="126" text-anchor="middle">Term Deposit</text><text class="mut" x="480" y="145" text-anchor="middle">मियादी जमा · fixed period</text>
<path class="ln" d="M160 154 V176 H90 V196 M160 176 H230 V196 M480 176 H410 V196 M480 154 V176 H550 V196"/>
<rect class="bx" x="30" y="196" width="120" height="44" rx="6"/><text x="90" y="216" text-anchor="middle">Saving A/c</text><text class="mut" x="90" y="233" text-anchor="middle">बचत खाता</text>
<rect class="bx" x="170" y="196" width="120" height="44" rx="6"/><text x="230" y="216" text-anchor="middle">Current A/c</text><text class="mut" x="230" y="233" text-anchor="middle">चालू खाता</text>
<rect class="bx" x="350" y="196" width="120" height="44" rx="6"/><text x="410" y="216" text-anchor="middle">Recurring (RD)</text><text class="mut" x="410" y="233" text-anchor="middle">आवर्ती जमा</text>
<rect class="bx" x="490" y="196" width="120" height="44" rx="6"/><text x="550" y="216" text-anchor="middle">Fixed (FD)</text><text class="mut" x="550" y="233" text-anchor="middle">सावधि जमा</text>
</svg><figcaption>Then test yourself in the quick check below: is each account demand or term?</figcaption></figure>'''

S = [
 ('No-Frills Account → BSBD Account', 'The bank account built for financial inclusion (continues from Class 1).', [
  dict(h='No-Frills Account', hi='नो-फ्रिल्स खाता', tag='bank', pics=[('c2-nofrills-icon', 'No-frills account'), ('c2-field-account', 'Opening accounts in a village')], facts=[
     'A no-frills account in India is a ' + k('basic savings account') + ' designed for ' + k('financial inclusion') + '.',
     'It is an account with ' + k('zero or very low minimum balance') + '.',
     'Introduced by the ' + k('Reserve Bank of India (RBI) in 2005') + '.',
     'It targets ' + k('low-income and underserved groups') + '.',
  ]),
  dict(h='2012: renamed Basic Savings Bank Deposit Account (BSBDA)', tag='hot', facts=[
     'In ' + k('2012') + ', RBI renamed “no-frills accounts” to ' + k('“Basic Savings Bank Deposit Accounts” (BSBDA)') + ' to improve financial inclusion.',
  ], trap='Two years to keep apart: no-frills account <b>introduced 2005</b>; renamed BSBDA in <b>2012</b>.'),
  dict(h='RBI Kehta Hai – the BSBD awareness campaign', pics=[('c2-rbi-kehta-hai', 'RBI Kehta Hai! – a public awareness initiative of RBI'), ('c2-no-min-balance', '“Don’t want to keep minimum balance?”'), ('c2-bsbd-ad', 'BSBD ad: KL Rahul & Umesh Yadav')], facts=[
     k('RBI Kehta Hai') + ' is a ' + k('public awareness initiative of RBI') + '.',
     'Its BSBD message: “Don’t want to keep minimum balance in your account? Open BSBD Account.”',
     'The ad “Banking becomes easy” says: open a BSBD account, no minimum balance required, easy to open with just ' + k('Aadhaar Card and PAN Card or Form No. 60') + '.',
     'The ad features cricketers <b>KL Rahul</b> and <b>Umesh Yadav</b> (both captioned “Indian Cricketer and RBI Employee”).',
  ], add=['Form 60 is the declaration a person gives when they do not have a PAN.']),
  dict(h='BSBD Account – features (RBI Kehta Hai notice)', tag='hot', pics=[('c2-bsbd-notice-1', 'RBI notice on BSBD – part 1'), ('c2-bsbd-notice-2', 'RBI notice on BSBD – part 2')], facts=[
     'Can be opened by ' + k('any individual') + ', irrespective of his/her ' + k('age or income') + '.',
     'Can be opened ' + k('without any initial deposit') + '. No need to maintain a ' + k('minimum balance') + '.',
     'A regular savings bank account can be ' + k('converted into a BSBD account') + ' at the request of the customer.',
     'Basic facilities like an ' + k('ATM-cum-Debit Card') + ' are given ' + k('free of charge') + '.',
     'There is ' + k('no limit on the number of deposits') + '.',
     'Holders get a maximum of ' + k('four withdrawals free of charge in a month') + ', counting ATM withdrawals, RTGS / NEFT / clearing / internet debits, standing instructions, EMIs, etc.',
     'BSBD holders ' + k('cannot have a regular savings bank account in the same bank') + '.',
  ]),
  dict(h='BSBD Account – rules and limits', tag='hot', pics=[('c2-piggy-laptop', 'Saving in a basic account')], facts=[
     'The holder of a BSBD account is ' + k('not eligible to open any other savings bank account in the same bank') + '.',
     'If the customer already has a savings account in that bank, it must be ' + k('closed within 30 days') + ' from the date of opening the BSBD account.',
     'Total ' + k('credits') + ' in such accounts should not exceed ' + k('₹1 lakh in a year') + '.',
     'The ' + k('maximum balance') + ' should not exceed ' + k('₹50,000 at any time') + '.',
     'Total ' + k('debits') + ' by way of cash withdrawals and transfers will not exceed ' + k('₹10,000 in a month') + '.',
  ], table=(['Limit', 'Amount', 'Period'], [
     ['Total credits (money coming in)', '₹1,00,000', 'per year'],
     ['Balance at any time', '₹50,000', 'any time'],
     ['Debits (cash withdrawals + transfers)', '₹10,000', 'per month'],
     ['Free withdrawals', '4', 'per month'],
     ['Close other SB account in same bank', 'within 30 days', 'of opening BSBDA'],
  ]), trap='Watch the wording. In RBI’s rules these three ceilings (₹1 lakh a year, ₹50,000 balance, ₹10,000 a month) belong to a <b>Small Account</b>, a BSBD account opened with relaxed (simplified) KYC. Write the numbers as taught; if a question says “Small Account”, these are the figures.'),
 ]),
 ('Banking in India – what is a Bank?', 'Indian Banking System, Part 1.', [
  dict(h='Definition of Bank', hi='बैंक', tag='bank', pics=[('c2-bank-illus', 'Banking in India')], facts=[
     'A bank is a ' + k('financial institution') + ' which ' + k('accepts deposits') + ' and provides ' + k('loans & advances') + ' and other financial services.',
     'A bank is a ' + k('licensed') + ' financial institution that accepts money from people and businesses (as deposits) and then ' + k('uses that money to give loans') + ' and other credit facilities.',
  ], add=[
     'Legal definition – <b>Banking Regulation Act, 1949, Section 5(b)</b>: “banking” means accepting, for the purpose of lending or investment, deposits of money from the public, repayable on demand or otherwise, and withdrawable by cheque, draft, order or otherwise.',
     'Banks get their licence from <b>RBI</b> under <b>Section 22</b> of the Banking Regulation Act.',
  ]),
  dict(h='Accounts a bank offers', pics=[('c2-deposit-bag', 'Deposits are the bank’s raw material')], facts=[
     'Banks offer various accounts where people can park their money safely: ' + k('savings accounts') + ', ' + k('current (business) accounts') + ' and ' + k('fixed / term deposits') + '.',
     'In return the bank may ' + k('pay interest') + ' on these deposits and issue a ' + k('passbook, cheque book or ATM card') + '.',
  ]),
 ]),
 ('Types of Deposit', 'जमा के प्रकार – the two families of deposit and their four accounts.', [
  dict(h='The deposit family tree', html='DEPOSIT_TREE', facts=[
     k('Demand Deposit') + ' (माँग जमा) → ' + k('Saving Account') + ' (बचत खाता) and ' + k('Current Account') + ' (चालू खाता).',
     k('Term Deposit') + ' (मियादी जमा) → ' + k('Recurring Deposit Account') + ' (आवर्ती जमा खाता) and ' + k('Fixed Deposit Account') + ' (सावधि जमा खाता).',
  ], sort=True),
  dict(h='Demand Deposits', hi='माँग जमा', facts=[
     'These offer ' + k('high liquidity') + ' for everyday use, with ' + k('no fixed maturity') + '.',
     'Ideal for ' + k('transactions') + ' but earn ' + k('lower interest') + '.',
  ], add=[
     'A <b>current account</b> is for businesses with many transactions; banks normally pay <b>no interest</b> on it and give an overdraft facility.',
     'Savings + current deposits together are called <b>CASA</b> – cheap money for a bank, so a high CASA ratio is good for it.',
  ]),
  dict(h='Term Deposits', hi='सावधि / मियादी जमा', facts=[
     'Term deposits are ' + k('interest-bearing') + ' bank accounts where you deposit a ' + k('lump sum (FD) or instalments (RD)') + ' for a ' + k('fixed period (term)') + ' until maturity.',
     'They earn ' + k('higher interest than demand deposits') + '.',
  ], add=[
     '<b>FD</b> = one lump sum for a fixed term (minimum tenure is usually 7 days). <b>RD</b> = a fixed amount every month for a fixed term.',
     'Deposits in a bank are insured by <b>DICGC</b> up to <b>₹5 lakh</b> per depositor per bank (principal + interest).',
  ]),
  dict(h='Demand vs Term – the comparison table', tag='hot', table=(['Feature', 'Demand Deposits', 'Term Deposits'], [
     ['Description', 'Deposits that can be ' + k('withdrawn at any time without prior notice') + '.', 'Deposits held at a financial institution that have a ' + k('fixed term') + ' and typically offer higher interest rates than demand deposits.'],
     ['Accessibility', 'High accessibility with ' + k('no restrictions') + ' on withdrawal timing.', 'Restricted by the term of the deposit. ' + k('Early withdrawal may result in penalties') + '.'],
     ['Interest rates', 'Generally ' + k('lower') + ' than term deposits.', k('Higher') + ' than demand deposits, to compensate for the lack of accessibility.'],
     ['Suited for', 'Day-to-day transactions and immediate access to funds.', 'Saving money over a longer period for higher interest earnings.'],
  ])),
  dict(h='One-glance summary', table=(['Type', 'Examples', 'Accessibility', 'Interest rate'], [
     ['Demand Deposit', 'Savings, Current', 'Anytime withdrawal', k('Lower')],
     ['Term Deposit', 'Fixed, Recurring', 'Locked till maturity', k('Higher')],
  ]), trap='A <b>Recurring</b> Deposit is a <b>term</b> deposit even though you pay into it every month: the money is locked till maturity. Don’t put RD under demand deposits.'),
 ]),
]

SORT = [('Saving Account', 'Demand'), ('Recurring Deposit', 'Term'), ('Current Account', 'Demand'), ('Fixed Deposit', 'Term')]

FLASH = [
 ('No-frills account', 'Basic savings account with zero / very low minimum balance, introduced by RBI in 2005 for financial inclusion.'),
 ('BSBDA', 'Basic Savings Bank Deposit Account – the 2012 name for no-frills accounts.'),
 ('BSBD free withdrawals', 'Maximum 4 free withdrawals a month (ATM, NEFT/RTGS, clearing, internet debits, SI, EMIs).'),
 ('Bank', 'A licensed financial institution that accepts deposits and gives loans & advances and other financial services.'),
 ('Demand deposit', 'Withdrawable any time without notice; high liquidity, lower interest (Savings, Current).'),
 ('Term deposit', 'Locked for a fixed term; higher interest, penalty on early withdrawal (FD, RD).'),
 ('RBI Kehta Hai', 'Public awareness initiative of the RBI.'),
]

QUIZ = [
 ('Who introduced no-frills accounts, and when?', 'The Reserve Bank of India, in 2005.'),
 ('In which year were no-frills accounts renamed, and to what?', '2012 – Basic Savings Bank Deposit Accounts (BSBDA).'),
 ('What minimum balance does a BSBD account need?', 'None – zero minimum balance and no initial deposit.'),
 ('Who can open a BSBD account?', 'Any individual, irrespective of age or income.'),
 ('How many free withdrawals does a BSBD holder get per month?', 'Maximum four, including ATM withdrawals and RTGS/NEFT/clearing/internet debits, SIs, EMIs.'),
 ('Is there a limit on the number of deposits in a BSBD account?', 'No.'),
 ('A customer with a savings account opens a BSBDA in the same bank. What must they do?', 'Close the other savings account within 30 days of opening the BSBDA.'),
 ('BSBD limits taught in class: total credits per year, maximum balance, debits per month?', '₹1 lakh a year; ₹50,000 at any time; ₹10,000 a month.'),
 ('Which documents does the BSBD ad say are enough to open the account?', 'Aadhaar Card and PAN Card, or Form No. 60.'),
 ('What is “RBI Kehta Hai”?', 'A public awareness initiative of the RBI.'),
 ('Define a bank.', 'A financial institution that accepts deposits and provides loans & advances and other financial services.'),
 ('Name the two types of deposit and their examples.', 'Demand deposit (savings, current) and term deposit (fixed, recurring).'),
 ('Which deposit offers higher liquidity, and which offers higher interest?', 'Demand deposits – higher liquidity; term deposits – higher interest.'),
 ('What may happen if you withdraw a term deposit early?', 'You may pay a penalty.'),
 ('Is a Recurring Deposit a demand or term deposit?', 'Term deposit.'),
 ('What does a bank give a depositor besides interest?', 'A passbook, cheque book or ATM card.'),
]

RAPID = [
 'No-frills account: RBI <b>2005</b>, zero/low balance, for low-income groups → renamed <b>BSBDA in 2012</b>.',
 'BSBDA: anyone, any age/income · no initial deposit · no minimum balance · free ATM-cum-debit card · unlimited deposits · <b>4 free withdrawals/month</b>.',
 'BSBDA holder: no other SB account in same bank; close existing one within <b>30 days</b>.',
 'Limits taught: credits ≤ ₹1 lakh/yr · balance ≤ ₹50,000 · debits ≤ ₹10,000/month.',
 'RBI Kehta Hai = RBI’s public awareness initiative; BSBD ad: Aadhaar + PAN or Form 60.',
 'Bank = accepts deposits + gives loans & advances (+ other services); licensed by RBI.',
 'Demand deposit = Savings + Current: any-time withdrawal, high liquidity, low interest.',
 'Term deposit = FD + RD: fixed term, higher interest, penalty on early withdrawal.',
]
