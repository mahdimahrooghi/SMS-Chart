
from operator import truth
import random
import json
from time import sleep
from tkinter import END
import numpy as np
import matplotlib.pyplot as plt
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import os
# import sys
import re


print("connecting...")

try:
    import requests
    requests.request("POST", "https://google.com")
except:
    print("Failed to connect :(")
    print("Goodby")
    sleep(3)
    quit()

# import send_meseaage
def token(): # give token
        
    url = "https://restfulsms.com/api/Token"

    payload = json.dumps({
    "UserApiKey": "4463f74fd60cae2425d7ead0",
    "SecretKey": "amslwm1385"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return(response.text)

token_key = token()
if ("true" in token_key):
    print("Connected! :) ")
else:
    print("Failed to connect :(")
# =============================
regex = r".............(................................................................................................................................................................................................................................................................)"
matches = re.findall(regex, token_key)
token_key_fainal = matches[0]
# =============================
adad = 1
from_data = input("From Data: ")
to_data = input("To Data: ")
while True:
    
    def imported():
        
        url = f"https://RestfulSms.com/api/ReceiveMessage?Shamsi_FromDate=1400/12/{from_data}&Shamsi_ToDate=1400/12/{to_data}&RowsPerPage=10&RequestedPageNumber=1"


        payload={}
        headers = {
        'x-sms-ir-secure-token': token_key_fainal
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return(response.text)
    codin = imported()
    # =============================
    regex = r"SMSMessageBody...(.)"
    nazarat = re.findall(regex, codin)
    # =============================

    regex_2 = r"MobileNo...(..........)"
    numberphone = re.findall(regex_2 , codin)
    # print(codin)
    one = 0
    
    two = 0
    # tree = 0
    # four= 0

    for x in nazarat:
        try:
            x = int(x)
        except:
            continue
        if x ==1:
            one+=1
        if x ==2:
            two+=1
    #     if x ==3:
    #         tree+=1
    #     if x ==4:
    #         four+=1

    print(f"""
    tedad kol ara = {one+two}
     payan aval = {one}
     payan dovom = {two}
    
    """)
    labels = [" .پایان اول: ثباتی در ایستگاه بماند.", "پایان دوم: ثباتی به شهر بازگردد"]
    persian_labels = [get_display(reshape(label)) for label in labels]
    sizes = [one, two]

    mycolors = ["green", "orange"]
#     if (adad==1 ):
#         plt.pie(sizes, labels=persian_labels, autopct='%1.1f%%' , colors=mycolors )
#         plt.savefig("نمودار نظرسنجی.png", dpi=300)
    adad+=1
    
    print("""which one?
    1.Build a chart
    2.Repeat the loop
    
    """)
    choes=int(input("enter your choice: "))
    os.system('cls')
    if(choes==1):
        plt.pie(sizes, labels=persian_labels, autopct='%1.1f%%' , colors=mycolors )
        plt.savefig("نمودار نظرسنجی.png", dpi=300)
        print("builded!")
    else:
        continue
        
