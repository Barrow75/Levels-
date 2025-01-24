# will try to do every single code with documentation

# Create a program that:
#
# Asks the user for their date of birth in the format YYYY-MM-DD.
# Calculates their age in years based on the current date.
# Outputs their exact age, including years, months, and days.
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

birth_year = int(input("Enter birth year YYYY: "))
birth_month = int(input("Enter birth month MM: "))
birth_day =int(input("Eneter birth day DD: "))
birthday = datetime.date(birth_year, birth_month, birth_day)
current_date = date.today()
print(f"Your birthday is on {birthday}")
print(f"The current date is {current_date}")

age = current_date.year - birth_year
year = current_date.year
month = current_date.month
day = current_date.day


current_years = year - birth_year

birth = date(birth_year, birth_month, birth_day)
age_gap = relativedelta(current_date, birth)

new_year = age_gap.years
new_month = age_gap.months
new_day = age_gap.days


print(f"You are {age} years old as of {current_date}")

#print(current_month)
#print(current_day)
print(f"You were born precisley: {new_year} years {new_month} month(s) {new_day} day(s) ago")
