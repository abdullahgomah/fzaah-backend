from twilio.rest import Client
from dotenv import load_dotenv 
import os 
import random 

load_dotenv() 

ACCOUNT_SID = os.getenv("ACCOUNT_SID") 
ACCOUNT_TOKEN = os.getenv("ACCOUNT_TOKEN") 

client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)

def send_otp(to, otp): 
    message = client.messages.create(
                     body=f"مرحباً بكم في موقع فزعة، رمز الدخول هو {otp}",
                     from_='+1 208 443 5313',
                     to=to 
                 )
    
def generate_otp(): 
    return random.randint(10000, 99999)