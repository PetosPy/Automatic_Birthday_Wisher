import random
import pandas as pd
from smtplib import SMTP
import datetime as dt
##################### Extra Hard Starting Project ######################

PLACEHOLDER = "[NAME]"
MY_EMAIL = "petospy21@gmail.com"
PASSWORD = "Tempo@290"


def letters():
	# Selects which message to send and adds the receipeints name
	num = random.randint(1,4)
	with open(f"./letter_templates/letter_{num}.txt", "r") as letter:
		contents = letter.read()
		updated_text = contents.replace(PLACEHOLDER, name)
	# Sends the email
	with SMTP("smtp.gmail.com", 587) as connection:
		connection.starttls()
		connection.login(MY_EMAIL,PASSWORD)
		connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{updated_text}")

# Current date
now = dt.datetime.now()
month_now = now.month
day_now = now.day

# Opens and reads from the csv file that cointains personal info
data = pd.read_csv("birthdays.csv")
person_data = data.to_dict(orient="records")
for dicts in person_data:
	if dicts["month"] == month_now and dicts["day"] == day_now:
		name = dicts["name"]
		email = dicts["email"]
		letters()


