print("Hello World")

#Import packages
import RPi.GPIO as GPIO
import smtplib
import time
###################################
#Check for voltage at GPIO pin 26

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(21, GPIO.IN)

input_value = GPIO.input(21)

GPIO.input(21)
print(GPIO.input(21))

#**************************
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(21, GPIO.FALLING)
#******************************

###################################
#Send Email alert if voltage is present
SMTP_SERVER = 'smtp.gmail.com' #Email server
SMTP_PORT = 587 #Server Port
GMAIL_USERNAME = 'sendalert90@gmail.com'
GMAIL_PASSWORD = 'Dispatch'

class Emailer:
    def sendmail(self, recipient, subject, content):
        headers = ["From: " +GMAIL_USERNAME, "Subject: " + subject, "To: " +recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        
        #Connect to Gmail server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
        
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers +"\r\n\r\n" + content)
        session.quit
        
sender = Emailer()
###############################################################

#******************************************************8
'''
while True:

    if GPIO.event_detected(21):
        sendTo = 'seriousbritt@gmail.com'
        emailSubject = "HELLO World"
        emailContent = "Can you see me now??"
        sender.sendmail(sendTo, emailSubject, emailContent)
        print("Email Sent")
        
    time.sleep(0.1)
'''
    
#********************************************************
while True:

    if GPIO.input(21) == 1:
        sendTo = 'seriousbritt@gmail.com'
        emailSubject = "HELLO World"
        emailContent = "Can you see me now???????????"
 #       sender.sendmail(sendTo, emailSubject, emailContent) 
        print("Email Sent")
    else: 
        print("Not Sent")
        
    time.sleep(1.1)
