# Moneydance-Scripts-2026
Moneydance Scripts 2026
These scripts are used by me almost dayly to keep my moneydance Investment accounts up to date.
runScripts.py is a Jython Java swing program that allows you too quickly choose which script you want to run.
You only need a Stockwatch account if you want to down load the Ticker close prices to moneydance.
You run updateDaylyStockwatch.py, manually at the end of the day to get the close prices put into moneydance.
Moneydance only uses dailey times . If you want real time quotes use stockwatch or your Bank.
I want moneydance to tell me how much I lost(or gained) at the end of the day. (updates the Networth)
updateHistoryStockwatch.py will load a years worth of price history into moneydance for a ticker.
You have to manualy download the history files from stockwatch to do this first. (only used if I add a new ticker) Put all the scripts in /opt/moneydance/scripts. Then you can run execfile("runScripts.py") on a jython console. or use the moneydance Developer Console to Open the Script and then Run it.
The Investment Account tranaaction update scripts assume you have downloaded the csv files from the bank and put them in ~/Downloads.
The Investment Account tranaaction scripts are complex because the Bank keeps coming up with new actions.
There are three of these scripts now. Scotia, BMO and CIBC. runScripts runs BMO-Inv-new.py. ScotiaPicker.py or CIBCpicker.py can be run from a console or the moneydance developer console.I have changed the scripts to use import instead of execfile .To be more pythonic. It keeps the local namespace cleaner.
You need to add a securty named FAKE-T to all your investment accounts. It gets used if the transaction has no ticker.
If the action is unrecognized the script will post it as a "Short". After you do the import you need to check for FAKE-T and Shorts and fix them manually. A Short means you have to change the action map in the script because the Bank hit you with a new Action. A FAKE-T means the symbol is missing from your account or is missing from the BMOdescTable. You may need to add a line to the BMOdescTable or just add the symbol to your account.
All transactions get a time stamp put in the memo field. This is used to select all transactions posted during a particular update session. You can then delete them and try again. The csv files get renamed to .csv-done to help keep track of them.You can rename them back to .csv if you need to do it over again. I often use a dummy account "BMO RRSP TEST" to experiment with the upload prior to updating into the real account.
The BMOdescTable came into existamce because some transactions have no ticker. They always have a description however. So you can now look up the ticker if you just have the description.
The BMOdescTable remaps the ticker to what your using in Moneydance like Telus 'T' becomes T-T for the TSX.
The action remaps are handled by the jython scripts and will require some script editing. Most are simple but a few get more complex if shares or amount are involved.
Negative Dividends are a pain in the ... moneydance does not like negative dividends. I have captured them and changed them to MisExp transactions. These occure normaly because a company has made a mistake and issued an incorrect dividend. They will then issue a negative dividend and a new positive one. The account balance will be ok but the preformance gets messed up. So after an import you can track down the MisExp transactions and delete the negative one and its matching positive mistake manually.
After an import session the best indicator that all is well is that the cash balance matches whats on line at your Bank and you don't have any FAKE-T holdings in your Portfolio View. No shorts in the transactions. Stock Splits will show up in the Portfolio View as differences in the number of Shares you hold verses whats shown at the Bank. You need to enter these Splits manually on moneydance.(Stockwatch tracks these too)
update March 11 2026
You need to rename "AccoutNames copy.py" to AccountNames.py and fill it in with your moneydance account names.
You need to rename "PassWords copy.py" to Passwords.py" and fill it in with your Stockwatch user name & password.
You need to have a directory /opt/moneydance/scripts/tmp for updateDaylyStockwatch.py to run
You need to have a directory /opt/moneydance/scripts/tmp/Done for updateDaylyStockwatch.py to runYou/opt/moneydance/You need to have a directory /opt/moneydance/scripts/tmp/StockwatchDay for fetchhtmlDaylyStockwatchIndexs.py
You will need to update definitions.StockPriceHistoryStockwatch with the tickers you want prices for
You will need to update BMOdescTable.py with the Stocks your trading. Keep the description as short as possible.
I use GlobeInvestor Ticker Symbols in moneydance so GRANITE REAL ESTATE INVESTMENT becomes GRT-UN-T instead of GRT.UN
Stockwatch costs $6.95 a month, its well worth it. Nothing in this world is Free. Or if it is it maybe dissappear.
Philosophy: The idea is to take the csv files and load them into moneydance no matter what. You can fix the transactions later. You can roll them back using the timestamp. You can load them into a sandbox Account first.
My sandbox account is called "BMO RRSP TEST" it has every active security account added to it. Also FAKE-T.
In a typical session I may download 50 different tickers from three different banks and 12 different accounts.
Once a month. I run the price history update prior to checking the moneydance Networth and after the TSX is closed for the day. I use moneydances preformance reports frequently. They have a problem with zero dollar buys and sells so you may have to track these down and change them first (add a price and amount and a corresponding cash xfer..its a pain in the bute). Negative dividends are a problem too. They will get changed to MiscExp by the import scripts so you have to track these down too and delete them along with the positive dividend error.
Have fun.

