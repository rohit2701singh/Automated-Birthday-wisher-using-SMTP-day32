import smtplib
import datetime as dt
import random
import pandas
import os

my_email = "rxxccxcxgh@gmail.com"
passwd = os.environ.get("SMTP_MAIL_PASS")

# reading csv data and creating list of month and days.
data = pandas.read_csv("birthdays.csv")
all_month_list = data.month.to_list()
all_days_list = data.day.to_list()
# print(f"months: {all_month_list}, dates: {all_days_list}")

# checking date and month of today in month and days list.
now = dt.datetime.now()
today_month = now.month
day = now.day
# print(today_month, day)

# store all those indicis whose value matches with today month.
same_month_index_list = []
for (index, value) in enumerate(all_month_list):
    if value == today_month:
        same_month_index_list.append(index)
# print(same_month_index_list)

for indx in same_month_index_list:

    receiver_name = data.name[indx]
    receiver_email = data.email[indx]
    receiver_birthday = data.day[indx]

    if day == receiver_birthday:
        print(indx, receiver_name, receiver_email, receiver_birthday)

        # selecting a random letter from template
        selected_letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        print(selected_letter)

        # reading any selected letter and replacing name
        with open(selected_letter) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", receiver_name)

        # send birthday email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwd)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver_email,
                msg=f"Subject: smtp py birthday wish\n\n{content}"
            )