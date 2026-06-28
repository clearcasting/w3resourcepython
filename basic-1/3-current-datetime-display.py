"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime as dt

now = dt.datetime.now()
format = "%Y-%m-%d %H:%M:%S"

formatted_date = now.strftime(format)
print(f"Current date and time :\n{formatted_date}")
print(f"{now:%Y-%m-%d %H:%M:%S}")
