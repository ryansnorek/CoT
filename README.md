# CoT

Commitments of Traders Financial Futures report

Requires PostgreSQL
(password for ConfigDB available on request)

This program compares trader positioning from the most recent Commitment of Traders (CoT) report to historical averages. 
The output is the current number of traders in a given security/asset, the average number of traders in that security/asset, and the percent change.
The purpose is to see where Asset Managers and Leveraged Funds are putting their money.

The user selects which year to compare to OR the 5 yr average. Then the user selects the range for the percent filter, i.e., the minimum % change.
For example, by entering 250 it will only print out changes from the average that are greater or less than 250%.

INSTRUCTIONS
1. Contact me for password
2. Add the password on ConfigDB.py
3. Run printReport.py
4. Type the full report name, e.g., cotreport2020
5. Type a percent filter, e.g., 200

Recommended filter is 100 to 250

Enjoy!
