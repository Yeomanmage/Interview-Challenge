# eFuneral Interview Challenge
Greetings!  We wanted to first thank you for sharing your experiences with us as part of this interview.  The following is a brief work challenge that will allow us to work side by side with you and understand our fit together.  Our goal isn’t to trick you.  If there is anything that is unclear, please ask.

## Challenge
We are looking to develop a tool that can send text messages to multiple contacts in our address book.  We want to be able to schedule a service to run at the beginning of the month to text messages all of our friends at the beginning of their birthday month wishing them a happy birthday.

---

## The Text Message

When the message is sent it should say:

> Happy Birthday {{RecipientsFirstName}} from {{YourFirstName}} {{YourLastName}}! Call me at {{YourPhoneNumber}} to plan a lunch sometime.

### Message Parameters
Parameter Name | Value
------------ | -------------
{{RecipientsFirstName}}  | First name from the address book dataset
{{YourFirstName}} | Your first name
{{YourLastName}}  | Your last name
{{YourPhoneNumber}} | Your Actual Mobile Phone number (not the one being used in the challenge) formatted 999-999-9999

---

## The Address Book
Our addressBook.csv file contains the following data elements:
* First Name
* Last Name
* Home Phone
* Mobile Phone
* Street Address
* City
* State
* Zip
* Date of Birth

### Data validation
- Text messages can only be sent to mobile phone numbers
- Text messages should only be sent to people with valid birthdates
---

## Twilio
For this challenge you will be using Twilio to send the messages.  They have impressive API capabilities!

We went ahead and already setup a test account and number.  Those values should have been provided in the email sent to you.

**Important: When uploading your commits to your repository, please do not include the Auth Token**

### Additional Twilio Information

For more information about how to [Authenticate with Twilio](https://www.twilio.com/docs/usage/your-request-to-twilio#credentials)

Information abou the [API resource](https://www.twilio.com/docs/sms/api/message)
