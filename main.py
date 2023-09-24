##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import datetime as dt
import pandas
import random

data= pandas.read_csv("birthdays.csv")
data_dict= {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

now= dt.datetime.now()
today= (now.month, now.day)



if today in data_dict:
    birthday_person= data_dict[today]
    file_path= f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        text= file.read()
        text= text.replace("[NAME]", birthday_person["name"])

    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 465) as server:
        server.login("68c121aa0a1a53", "abb73078ffc83d")
        server.sendmail(
            sender,
            birthday_person["email"],
            f"Subject: Happy Birthday, {birthday_person['name']}\n\n{text}"
        )
    print("Email sent!")

# birthday-wisher
