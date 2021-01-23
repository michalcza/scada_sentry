

#Import packages
import RPi.GPIO as GPIO
import smtplib
import time
from datetime import datetime
dateTimeObj = datetime.now()

# Configure logging
# TODO $filename.py = $filename.log
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='REV14_SCADA.log', level=logging.DEBUG)
logging.info('PROGRAM STARTED')

# Check for voltage at GPIO pin 11
pin = 11
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING)
GPIO.setup(pin, GPIO.IN)
input_value = GPIO.input(pin)
GPIO.input(pin)

# Send Email alert if voltage is present
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

# Main loop
while True:

    if GPIO.input(pin) == 1:
        sendTo = 'Dispatch@provopower.org'
        emailSubject = "SCADA alarm"
        emailContent = "SCADA alarm dateTimeObj"
        sender.sendmail(sendTo, emailSubject, emailContent) 
        logging.info('MESSAGE SENT')

    # Alarm signal goes high/low. Quick loop to catch signal when high.
    time.sleep(0.001)
