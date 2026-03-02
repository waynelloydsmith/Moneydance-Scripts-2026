# Moneydance-Scripts-2026
Moneydance Scripts 2026
These scripts are used by me almost dayly to keep my moneydance Investment accounts up to date. 
runScripts.py is a Jython Java swing program that allows you too quickly choose which script you want to run. 
I put dummy Accounts in AccountNames.py The account names must match what ever your using in moneydance. 
You need to put your stockwatch user name and password in Passwords.py.
You only need a Stockwatch account if you want to run UpdateDaylyStockwatch.py. 
You run it manually at the end of the trading day to get the close prices put into moneydance. 
Moneydance only uses dailey times . If you want real time quotes use stockwatch. 
I only want moneydance to tell me how much I lost(or gained) at the end of the day. (update the Networth)
updateHistoryStockwatch.py will load a years worth of price history into moneydance for a ticker. 
You have to manualy download the history files from stockwatch to do this first. (only used if I add a new ticker) Put all the scripts in /opt/moneydance/scripts. Then you could run execfile("runScripts.py") on a jython console. or use the moneydance Developer Console to Open the Script and then Run it. 
The Investment Account tranaaction update scripts assume you have downloaded the csv files from the bank and put them in ~/Downloads. 
The Investment Account tranaaction scripts are complex because the Bank keeps coming up with new actions. 
There are three of these scripts now. Scotia, BMO and CIBC. runScripts runs BMO-Inv-new.py. ScotiaPicker.py or CIBCpicker.py can be run from a console or the moneydance developer console. Feb 26 2026 I have changed the scripts to use import instead of execfile .To be more pythonic. It keeps the local namespace cleaner.later I will include some scipts that I have written to pull tranactions out of pdf statements. I have one credit card (Amazon) that has no other way of providing me with data. I also have some credit cards that only provide 3 months of on line data. 
You need to add a securty named FAKE-T to all your investment accounts. It gets used if the transaction has no ticker.
If the action is unrecognized the script will post it as a "Short". After you do the import you need to check for FAKE-T or Shorts and fix them manually. A Short means you have to change the action map in the script because the Bank hit you with a new Action. A FAKE-T means the symbol is missing from your account or is missing from the BMOdescTable. You may need to add a line to the BMOdescTable or just add the symbol to your account.
All transactions get a time stamp put in the memo field. This is used to select all transactions posted during a particular update. You can then delete them and try again. The csv files get renamed to .csv-done to help keep track of them.You can rename them back to .csv if you need to do it over again. I often use a dummy account "BMO RRSP TEST" to experiment with the upload prior to updating the real account. 
The BMOdescTable came into existamce because some transactions have no ticker. They always have a description however. So you can look up the ticker if you just have the description.
The BMOdescTable remaps the ticker to what your using in Moneydance like Telus 'T' becomes T-T for the TSX.
The action remaps are handled by the jython scripts and will require some script editing. Most are simple but a few get more complex if shares or amount are involved. 
Negative Dividends are a pain in the ... moneydance does not like negative dividends. I have captured them and changed them to MisExp transactions. These occure normaly because a company has made a mistake and issued an incorrect dividend. They will then issue a negative dividend and a new positive one. The account balance will be ok but the preformance gets messed up. So after an import you can track down the MisExp transactions and delete the negative one and its matching positive mistake manually. 
After an import the best indicator that all is well is that the cash balance matches whats on line and you don't have any FAKE-T holdings in your Portfolio View. Stock Splits will show up in the Portfolio View as errors in the number of Shares you hold verses whats shown on line. You need to enter these Splits manually on moneydance.

