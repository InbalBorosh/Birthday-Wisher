import smtplib
import datetime as dt
import pandas as pd
import random
import os

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

df = pd.read_csv("birthdays.csv")
b_year = df["year"]
b_month = df["month"]
b_day = df["day"]
name = df["name"][(b_year == year) & (b_month == month) & (b_day == day)].tolist()
email = df["email"][(b_year == year) & (b_month == month) & (b_day == day)].tolist()

rn_letter = random.choice(os.listdir("letter_templates"))

try:
    replacements = [('[NAME]', name[0]), ('Angela', 'Inbal')]
except IndexError:
    print("Today is no one's birthday.")
else:
    with open(f"letter_templates/{rn_letter}", 'r') as file:
        file_content = file.read()
    for target_word, replacement_word in replacements:
        file_content = file_content.replace(target_word, replacement_word)
    my_email = "inbal.borosh@gmail.com"
    password = "123456"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email[0],
                     msg=f"subject: HAPPY BIRTHDAY!\n\n {file_content}")
    connection.close()




