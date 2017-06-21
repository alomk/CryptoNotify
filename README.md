
Use a gmail account for notifications. Program still prone to some exceptions and does not handle:
- connection issues
- other issues which may be caused by the json returned from bittrex

Usage:

Create a login.conf in the same directory as main.py and you MUST put your information in this order
- [login email]
- [password]


Our tools so far include:
1) dec_ind - Decrease indicator which notifies you of sharp drops in small intervals so you can quickly catch market corrections for ~10% profit
- not too reliable right now as you have to look at the order book and make good judgement
- another flaw is that it will consistently send emails about coins that were pumped recently and are on negative trends which won't go back up for a while

2) inc_ind - Increase indicator or pump indicator will notify you of ongoing pumps so you can ride steep increases in short intervals.
- high risk method for quick gains
- pumps don't happen for high volume coins that often
- pumps are (usually) immediately followed by dumps which could result in you losing a large portion of your balance
