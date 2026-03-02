#!/usr/bin/env python
# coding: utf8
# version 2/19/2025

from __future__ import print_function
from __future__ import absolute_import
#
# see updateHistoryStockwatch.py for info on some of the lists stored here 
global definitions

class definitions:

   import sys

# not used by BMO_Inv_new.py maybe Scotia-Inv-new.py
# definitions is now only used by updateDaylyStockwatch.py and updateHistoryStockwatch.py

# just list the symbols that are not on the TSX
# its a python dictionary
# not used by BMO_INV_new anymore the Symbol remapping is done with the BMOdescTable now.
# still use by Scotia_Inv_new
   ExchangeTable = {
   'KMB-T':'KMB-N', # Kimberly Clark is on the New York Exchange
   'MHYB-T':'MHYB-NEO',
   'VST-T':'VST-N'     # Vista Energy Corp
#   'FCD-UN-T':'FCD-UN-X' # the venture exchange
   }

   
# info from stockwatch site ->US mutual fund data is received from the Nasdaq feed, 
# therefore the symbols conform to the Nasdaq standard. 
# Each fund has a five letter symbol of which the last letter is always X. The exchange code is Q. 
# Canadian mutual fund Symbols
# info from stockwatch->Canadian mutual fund symbols are of the form GGG*FFF where GGG represents the fund group, and FFF represents the specific fund.
# the list below is the result of different companies using different symbols for the Canadian mutual funds.
# example TML202 (Fundserv Code) = BIF*CDN (Stockwatch) = id=53895 (GlobeInvestor)
# TML202 is recognized by many web sites but BIF*CDN seems to be only used by stockwatch 
# used to look up the fundserv ticker symbol given the name used by www.stockwatch.com or vice versa
# mutual funds only.. used by updateHistoryStockwatch.py and updateDaylyStockwatch.py
# still used by Scotia-Inv-new.py for historical reasons ... not used by BMO_Inv_new.py
# its a python dictionary
   StockwatchMutualFundSymbols = {
   'TML202-T':'BIF*CDN', # Franklin Bissett Canadian Equity Fund Series A-F     did great
   'MFC738-T':'CUN*SSC', # Mackenzie Cundill Canadian Security Fund A - FE      did great
   'BIP151-T':'BRN*GLO', # Brandes Global Equity Fund Series A - FE             did ok
   'FID281-T':'FSB*CAA', # Fidelity Canadian Asset Allocation Fund Ser B -      did great
   'BNS744-T':'BNA*SAG', # Scotia Selected Maximum Growth Portfolio - Adv Ser - did great
   'BNS361-T':'BNS*MOR', # Scotia Mortgage Income Fund Series A                 dog
   'BNS741-T':'BNA*SIG', # Scotia Selected Balanced Growth Portfolio - Adv Sr   did ok
   'BNS357-T':'BNS*MMF', # Scotia Money Market Fund Series A 
   'BMO146-T':'BOM*DIV', # BMO Dividend Fund Series A                           did ok
   'BMO471-T':'BME*TFP'  # BMO SelectTrust Fixed Income Portfolio Series A ..   dog
#   'GOC309-T':'Canoe Canadian Asset Allocation Class-Z'    # missing from stockwatch looks like stockwatch makes up their own names for Canadian mutual funds
   }

# used for exchange rate update. used by updateDaylyStockwatch.py
# Currency Exchange Rates to Canadian Dollars
# its a python dictionary
   StockwatchIndexs = {
   'AUD':'FX$AUD/CAD',  # Australia $  
   'BGN':'FX$BGN/CAD',  #? Bulgarian Lev     
   'BMD':'FX$BMD/CAD',  # Bermudian $     
   'BRL':'FX$BRL/CAD',  # Brazilian Real     
   'BSD':'FX$BSD/CAD',  # Bahamian $     
   'CHF':'FX$CHF/CAD',  # Swiss Franc   
   'CLP':'FX$CLP/CAD',  # Chilean Pesos   
   'CNH':'FX$CNY/CAD',  # Chinese YUAN Renminbi
   'CRC':'FX$CRC/CAD',  # Costa Rica Colon
   'DKK':'FX$DKK/CAD',  # Danish Krone
   'EGP':'FX$EGP/CAD',  # Egyption Pound
   'EUR':'FX$EUR/CAD',  # Euro 
   'FJD':'FX$FJD/CAD',  # Fijian Dollar 
   'GBP':'FX$GBP/CAD',  # British Pound    
   'HKD':'FX$HKD/CAD',  # Hong Kong $
   'IDR':'FX$IDR/CAD',  # Indonesian Rupiah
   'ILS':'FX$ILS/CAD',  # Israeli New Shekel
   'INR':'FX$INR/CAD',  # Indian Rupee
   'ISK':'FX$ISK/CAD',  # Icelandic Krona   
   'JMD':'FX$JMD/CAD',  # Jamaican Dollar   
   'JOD':'FX$JOD/CAD',  # Jordonian Dollar   
   'JPY':'FX$JPY/CAD',  # Japan YEN * 100 looks wrong but FX$CAD/JPY looks right
   'KPW':'FX$KPW/CAD',  # North Korean Won 
   'KRW':'FX$KRW/CAD',  # South Korean Won
   'LBP':'FX$LBP/CAD',  # Lebanese Pound 
   'MYR':'FX$MYR/CAD',  # Malaysian Ringgit 
   'MXN':'FX$MXN/CAD',  # Mexican Pesos 
   'NOK':'FX$NOK/CAD',  # Norwegian Kroner 
   'NZD':'FX$NZD/CAD',  # New Zealand $
   'PHP':'FX$PHP/CAD',  # Philippines Peso
   'PKR':'FX$PKR/CAD',  # Pakistani Rupee
   'RON':'FX$RON/CAD',  # Romanian Leu   
   'SAR':'FX$SAR/CAD',  # Saudi Arabian Riyal   
   'SDG':'FX$SDG/CAD',  # Sudan Pound   
   'SGD':'FX$SGD/CAD',  # Singapore Dollars      
   'SEK':'FX$SEK/CAD',  # Swedish Krona   
   'THB':'FX$THB/CAD',  # Thai Baht   
   'TRY':'FX$TRY/CAD',  # Turkish Lira 
   'TTD':'FX$TTD/CAD',  # Trinidad and Tobago Dollar  
   'TWD':'FX$TWD/CAD',  # Taiwan Dollars   
   'USD':'FX$USD/CAD',  # US $
   'VEF':'FX$VEF/CAD',  # Venezuelan Bolivar
   'ZAR':'FX$ZAR/CAD',  # South African RAND
   'ZMW':'FX$ZMW/CAD'   # Zambian Kwacha
     
   }

   
# stockwatch shows TSX, NEO ATS, Omega, Pure, Chi-X, CX2, CXD, TriAct, CS2 and has both the date and time.
# Does Canadian Mutual Funds and Stocks. Has USA stocks and funds too. 
# also has international currency/exchange rates.
# its used by updateDaylyStockwatch.py .. if your ticker isn't in this table the stockwatch close price will not get updated '
# its a python dictionary
#################################################################################################################the list
   StockPriceHistoryStockwatch = { 
#   'MID436-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MID*IIF&region=C',     cannot find it on stockwatch
#   'TML202':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BIF*CDN&region=C',
#   'MFC738':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CUN*SSC&region=C',
#   'BIP151':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BRN*GLO&region=C',
#   'FID281':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FSB*CAA&region=C', 
#   'BNS744':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNA*SAG&region=C',
#   'BNS361':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNS*MOR&region=C',
#   'BNS741':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNA*SIG&region=C',
#   'BNS357':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNS*MMF&region=C',
#   'BMO146':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BOM*DIV&region=C', 
#   'BMO471':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BME*TFP&region=C', # ...............................end of the mutual funds
#   'AC-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AC&region=C',   #Air Canada  
   'AI-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AI&region=C',   #Atrium mortgage  
   'ARX-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ARX&region=C', # ARC Resources
#   'ABX-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ABX&region=C', # Barrick Gold    
#   'AD-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AD&region=C',    # Alaris Royalty Corp
   'AD-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AD.UN&region=C',    # Alaris Equity Trust
   'ALA-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ALA&region=C', # AltaGas Ltd
   'APR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=APR.UN&region=C', # Automotive Properties REIT
   'AP-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AP.UN&region=C', # Allied Properties REIT
   'AQN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AQN&region=C', # Algonquin Power and Utilities Corp
#   'AW-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AW.UN&region=C', 
#   'AX-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AX.UN&region=C', # Artis REIT
   'BEP-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BEP.UN&region=C', #Brookfield Renewables   
   'BEPC-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BEPC&region=C', #Brookfield Renewables corp      
   'BGI-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BGI.UN&region=C', #Brookfield Global Infrastructure   
#   'BPY-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BPY.UN&region=C', #Brookfield Property Ppartners   
#   'BR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BR&region=C', # Big Rock on TSX
   'BTB-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BTB.UN&region=C', # BTB REIT
   'BNE-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNE&region=C',       # Bonterra Energy
#   'BPF-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BPF.UN&region=C', # Boston Pizza TSX   
#   'CCO-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CCO&region=C', # cameco
#   'CGAA-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CGAA&region=C', # CI First Asset .. was SKG.UN Skylon  
   'CHP-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CHP.UN&region=C', # choice REIT   
   'CSH-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CSH.UN&region=C', # CHARTWELL Retirement Residences   
   'CHR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CHR&region=C', # Chorus Aviation 
   'CRR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CRR.UN&region=C', # Crombie REIT
   'CRT-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CRT.UN&region=C', # Canadian Tire REIT 
   'CTC-A-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CTC.A&region=C', # Canadian Tire    
#   'CNR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CNR&region=C',       # The Railway
   'CPX-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CPX&region=C',       # Capital Power
#   'CIQ-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CIQ.UN&region=C',  # Canadian Hi Income TSX
#   'CJR-B-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CJR.B&region=C',  # Corus   
   'CU-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CU&region=C',  # Canadian Utility TSX
   'CU-PR-F-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CU.PR.F&region=C',  # Canadian Utility TSX
#   'DS-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=DS&region=C', # Quadvest div select corp   
#   'DR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=DR&region=C',  #dog ass holes
   'EIT-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=EIT.UN&region=C', # Canoe ETF
   'EIF-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=EIF&region=C', # Exchange Income Corp
   'EMA-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=EMA&region=C', # Emera Energy 
   'ENB-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ENB&region=C', # Enbridge
   'ENS-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ENS&region=C', # E Split Corp Middlefield Enbridge   
#   'ENF-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ENF&region=C', # Enbridge Fund was ENF.UN now ENB
#   'EXE-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=EXE.UN&region=C', # Extendicare
   'FC-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FC&region=C',      # Firm Capital Mortgage Investment Corp 
   'FCD-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FCD.UN&region=C', # Firm Capital Property Trust its on the venture exchange ?
#   'FFN-PR-A-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FFN.PR.A&region=C', # Quadravest FINANCIAL 15 SPLIT CORP
#   'FFI-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FFI.UN&region=C', # FLAHERTY CRUMRINE INVEST GRADE PREF INC - http://www.bromptongroup.com
#   'FTN-PR-A-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FTN.PR.A&region=C', # Quadravest FINANCIAL 15 SPLIT CORP
   'FN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FN&region=C',  # FIRST NATIONAL FINANCIAL CORP
#   'FLI-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FLI&region=C', # CI US&CND LifeCo Fund   
#   'FPR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FPR&region=C', # CI Preffered Share Fund   
#   'FIG-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FIG&region=C', # CI FA INVESTMENT GRADE BOND 
   'FTS-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FTS&region=C', # Fortis  
#   'GDG-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=GDG.UN&region=C', # global dividend growers
   'GEI-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=GEI&region=C', # Gibsons Energy
#   'G-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=G&region=C', # goldcorp
   'GRT-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=GRT.UN&region=C', # Granite REIT  
   'GWO-PR-S-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=GWO.PR.S&region=C', # Great West Life TSX   
   'HR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=HR.UN&region=C', # H&R REIT
#   'H-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=H&region=C', # Hydro One
   'HHL-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=HHL&region=C', # Health Care Leaders (Harvest Portfolios)
#   'IDR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=IDR.UN&region=C',
#   'IDR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=IDR.UN&region=C', # Middlefield fund of REITs renamed
   'MREL-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MREL&region=C', # Middlefield Real Estate DIVID
#   'IPL-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=IPL&region=C', #INTER PIPELINE LTD
#   'INC-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=INC.UN&region=C', #dog
   'INE-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=INE&region=C',   # INNERGEX Renewable Energy  
#   'JE-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=JE&region=C', # Just Energy
#   'K-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=K&region=C', # Kinross
#   'KEG-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=KEG.UN&region=C',
   'KEY-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=KEY&region=C', # Keyera Corp
#   'KMB-N':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=KMB&region=U', # use Kimberly Clark to test New York Exchange
#   'KWH-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=KWH.UN&region=C', # was Cruise Energy
#   'LFE-PR-B-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=LFE.PR.B&region=C', # Quadravest Life split  
#   'MFR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MFR.UN&region=C', # manulife 
#   'MFT-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MFT&region=C', # MACKENZIE FLOATING RATE INCOME ETF
   'MHYB-NEO':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MHYB&region=C', # MACKENZIE GLOBAL HIGH YIELD FIXED INCOME ETF 
#   'MID-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MID.UN&region=C',  # Mint Income TSX middlefield
#   'MUB-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MUB&region=C', # MACKENZIE UNCONSTRAINED BOND ETF
   'MR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MR.UN&region=C',# MELCOR REIT       
   'MTL-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MTL&region=C',# Mullen Trucking       
#   'MRT-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MRT.UN&region=C', #  MORGUARD REIT
#   'MMP-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MMP.UN&region=C', # PRECIOUS METALS AND MINING TRUST
   'NPI-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=NPI&region=C',       # Northland Power  
#   'NPF-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=NPF.UN&region=C', # NORTH AMERICAN PREFERRED SHARE FUND UNIT 
#   'NWH-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=NWH.UN&region=C', # NORTHWEST HEALTHCARE PROP REIT
   'PEY-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PEY&region=C',   # PEYTO EXPLORATION AND DVLPMNT CORP.
   'PBY-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PBY.UN&region=C', # Canso Credit   
   'PIC-A-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PIC.A&region=C', # Premium Income Corp   
#   'PCD-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PCD.UN&region=C',#    PATHFINDER INCOME FUND
#   'PGI-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PGI.UN&region=C',# PIMCO GLOBAL INC OPPORTUNITIES FUND
   'PKI-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PKI&region=C',  # Parkland Fuel TSX
   'PMZ-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PMZ.UN&region=C', # Primaris REIT spin off from HR.UN
#   'PLZ-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PLZ.UN&region=C', # PLAZA RETAIL REIT
   'PPL-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PPL&region=C', # PEMBINA PIPELINE CORPORATION
#   'PR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PR&region=C',  # LYSANDER SLATER PREF SHARE ACTIV ETF
#   'PGF-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PGF&region=C',# PENGROWTH ENERGY CORPORATION
#   'RBN-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=RBN.UN&region=C', # Blue Ribbon Brompton Funds    
#   'REI-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=REI.UN&region=C', # RIOCAN REAL EST UN
#   'REF-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=REF.UN&region=C',   Canadian REIT now CHP.UN
#   'RIT-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=RIT&region=C',  # CI FA CANADIAN REIT ETF FirstAsset
   'RS-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=RS&region=C',  # Middlefield REIT Split Corp
   'RSI-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=RSI&region=C',  # Rogers Sugar
   'SBC-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SBC&region=C',     # Brompton Split Bank Corp
#   'SCW-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SCW.UN&region=C', defunked
#   'SIN-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SIN.UN&region=C', defunked
   'SGY-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SGY&region=C', # Surge Energy
   'SIS-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SIS&region=C', # Savaria Corp
#   'SJR-B-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SJR.B&region=C', # Shaw Communications Inc.
#   'SKG-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SKG.UN&region=C',  # Skylon 
   'SGR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SGR.UN&region=C',  # SLate Grocery REIT 
   'SOBO-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SOBO&region=C',  # South Bow .. spin off from Trans Canada Pipe
   'SPB-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SPB&region=C',  # SUPERIOR PLUS CORP. Propane 
#   'S-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=S&region=C', # Sherrit
   'SMU-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SMU.UN&region=C', # Summit Industrial REIT
   'SRU-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SRU.UN&region=C', # SMARTCENTRES REIT
#   'SRV-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SRV.UN&region=C',# SIR ROYALTY INCOME FUND 
#   'SSF-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SSF.UN&region=C',# Brompton SYMPHONY FLOATING RATE SR LOAN FD
#   'SU-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SU&region=C', # Sun core
#   'TECK-A-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TECK.A&region=C', # Teck
   'T-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=T&region=C', # Telus
   'TNT-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TNT.UN&region=C', # TRUE NORTH COMMERCIAL REIT
   'TRP-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TRP&region=C', # Trans Canada Pipe Lines   
   'TF-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TF&region=C', #Timber creek Financial
#   'TOG-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TOG&region=C', #Torc Oil and Gas merger with whitecap
   'TXF-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TXF&region=C', #CI Tech Giants
#   'TA-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TA&region=C', # TransAlta
#   'UTE-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=UTE.UN&region=C', # CANADIAN UTILITIES TELECOM INC FD strathbridge
   'VDY-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=VDY&region=C', # VanGuard FTSE CDN HIGH DIV
   'VET-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=VET&region=C', # Vermillion Energy
#   'VST-N':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=VST&region=N', # Vista Energy
#   'WJA-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=WJA&region=C', # West Jet
   'WCP-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=WCP&region=C', # Whitecap Resources
   'WJX-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=WJX&region=C', # Wajax   
   'XTC-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=XTC&region=C', # EXCO Technologies   
   'ZWB-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ZWB&region=C', # BMO CND Banks
#   'ZWE-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ZWE&region=C', # BMO Europe
#   'ZWU-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ZWU&region=C', # BMO Utilities
   'AUD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$AUD/CAD&region=U', # exchange rates start..only used as a filter to pick which rate we're interested in
#   'BGN':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$BGN/CAD&region=U', 
#   'BMD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$BMD/CAD&region=U', 
#   'BRL':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$BRL/CAD&region=U', 
#   'BSD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$BSD/CAD&region=U', 
#   'CHF':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$CHF/CAD&region=U',     
#   'CLP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$CLP/CAD&region=U',     
#   'CNH':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$CNH/CAD&region=U',   
#   'CRC':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$CRC/CAD&region=U',   
#   'DKK':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$DKK/CAD&region=U',   
#   'EGP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$EGP/CAD&region=U',   
   'EUR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$EUR/CAD&region=U',
#   'FJD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$FJD/CAD&region=U',
   'GBP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$GBP/CAD&region=U', 
#   'HKD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$HKD/CAD&region=U',   
#   'IDR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$IDR/CAD&region=U',   
#   'ILS':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$ILS/CAD&region=U',   
#   'INR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$INR/CAD&region=U',   
#   'ISK':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$ISK/CAD&region=U',   
#   'JMD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$JMD/CAD&region=U', 
#   'JOD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$JOD/CAD&region=U', 
#   'JPY':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$JPY/CAD&region=U', 
#   'KPW':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$KPW/CAD&region=U', 
#   'KRW':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$KRW/CAD&region=U', 
#   'LBP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$LBP/CAD&region=U', 
#   'MYR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$MYR/CAD&region=U', 
#   'MXN':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$MXN/CAD&region=U',    
#   'NOK':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$NOK/CAD&region=U',      
#   'NZD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$NZD/CAD&region=U',   
#   'PHP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$PHP/CAD&region=U',   
#   'PKR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$PKR/CAD&region=U',   
#   'RON':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$RON/CAD&region=U',      
#   'SAR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$SAR/CAD&region=U',
#   'SDG':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$SDG/CAD&region=U',
#   'SGD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$SGD/CAD&region=U',   
#   'SEK':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$SEK/CAD&region=U',
#   'THB':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$THB/CAD&region=U',
#   'TRY':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$TRY/CAD&region=U',
#   'TTD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$TTD/CAD&region=U',
#   'TWD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$TWD/CAD&region=U',
   'USD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$USD/CAD&region=U',
#   'VEF':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$VEF/CAD&region=U',   
#   'ZAR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$ZAR/CAD&region=U',
   'ZMW':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$ZMW/CAD&region=U'
     
   }
   
