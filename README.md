# CoT
Commitments of Traders Financial Futures report
Requires PostgreSQL
Password available on request

This program compares trader positioning from the most recent Commitment of Traders (CoT) report to historical averages. 
The output is the current number of traders in a given security/asset, the average number of traders in that security/asset, and the percent change.
The purpose is to see where Asset Managers and Leveraged Funds are putting their money.

The user selects which year to compare to OR the 5 yr average. Then the user selects the range for the percent filter, i.e., the minimum % change.
For example, by entering 250 it will only print out changes that meet or exceed a 250% change from the average.

Recommended filter is 100 to 250
