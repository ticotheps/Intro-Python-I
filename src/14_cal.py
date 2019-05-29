"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

args = sys.argv

print(args)



# Collect the input

# If there are no args:
  # If the user doesn't specify any input, your program should
  # print the calendar for the current month. The 'datetime'
  # module may be helpful for this.
# If there is 1 arg: 
  # Do something

month = datetime.today().month
year = datetime.today().year

if len(args) == 1:
    pass
if len(args) == 2:
    month = int(args[1])
elif len(args) == 3:
    month = int(args[1])
    year = int(args[2])
else: 
    print("Error: Must be in format [month] [year]")
    exit()

calendar.TextCalendar().prmonth(year,month)


