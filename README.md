
Use a gmail account for notifications. Program still prone to some exceptions and does not handle:
- connection issues
- other issues which may be caused by the json returned from bittrex

Usage:

Create a login.conf in the same directory as main.py and you MUST put your information in this order
- [login email]
- [password]


Tools so far include:
1) dec_ind - Decrease indicator which notifies you of sharp drops in small intervals so you can quickly catch market corrections for ~10% profit
- not too reliable right now as you have to look at the order book and make good judgement
- another flaw is that it will consistently send emails about coins that were pumped recently and are on negative trends which won't go back up for a while

2) inc_ind - Increase indicator or pump indicator will notify you of ongoing pumps so you can ride steep increases in short intervals.
- high risk method for quick gains
- pumps don't happen for high volume coins that often
- pumps are (usually) immediately followed by dumps which could result in you losing a large portion of your balance

3) vol_ind - Detects both of the above but cannot differentiate between the two and also when volume is decreasing
- set to run at a high frequency
- much more effective at finding pumps or dips

4) fetch_data and plot - Constantly gets volume info of every coin at 30 min intervals and can be graphed
- graphing part won't be implemented until i find it more convenient than printing

4) buy_analyzer - supposed to notify you when large buy orders are set, same principle can apply to sells
- havent done this yet
