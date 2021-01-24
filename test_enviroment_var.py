import os 

user_name = os.environ.get('SCADA_sentry_username')
password = os.environ.get('SCADA_sentry_password')

print(user_name, password)
