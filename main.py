#Owen Hobbs Efuneral coding challenge
#Imports
import csv
from datetime import datetime
from twilio.rest import Client

#function uses datetime to check that a date is valid
def is_valid_date(date_str, date_format="%m/%d/%Y"):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False

#function to check if the persons birthdate matches the current month
def is_birthday_this_month(dob, current_month):
    try:
        date_of_birth = datetime.strptime(dob, "%m/%d/%Y")
        return date_of_birth.month == current_month
    except ValueError:
        return False

#function uses twilio to send a messsage and then print the SID for confirmation
def send_text_message(client, to_phone, message):
    from_phone = "+15153254937"
    sent_message = client.messages.create(
        body=message,
        from_=from_phone,
        to=to_phone
    )
    print(sent_message.sid)


account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

#Open the CSV in read mode
current_month = datetime.now().month
with open("addressBook.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)

    #Iterate through the CSV file
    for row in csv_reader:
        phone_number = row[3]
        dob = row[8]

        #Check the length of the phone number to make sure it's valid and if DOB is valid
        if len(phone_number) == 10 and dob.strip() and is_valid_date(dob):
            if is_birthday_this_month(dob, current_month):
                #if valid format the phone number and create a message to send through our function
                formatted_phone_number = f"+1{phone_number}"
                message = f"Happy Birthday {row[0]} from Owen Hobbs! Call me at 515-564-9004 to plan a lunch sometime."
                send_text_message(client, formatted_phone_number, message)


