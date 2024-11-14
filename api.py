#!/usr/bin/env python
import os,sys,requests
from bs4 import BeautifulSoup
os.system("clear")
print("""\33[32;1m
___________ ________           _____           .__  
\\__    ___//  _____/          /  _  \\  ______  |__| 
  |    |  /   \\  ___  ______ /  /_\\  \\ \\____ \\ |  | 
  |    |  \\    \\_\\  \\/_____//    |    \\|  |_> >|  | 
  |____|   \\______  /       \\____|__  /|   __/ |__| 
                  \\/                \\/ |__|         
\33[0;1m           ==++[ A simple script to get your telegram
           ==++[ Api id and hash id..

\33[33;1mBy Alienkrishn\33[0m\n""")
Phone = input("\33[26mEnter your phone number with contry code\n\33[31mExample: +91********09 : \33[0m")

with requests.Session() as req:
    phone_number = Phone
    
    login0 = req.post('https://my.telegram.org/auth/send_password', data={'phone':phone_number})
    if 'Sorry, too many tries. Please try again later.' in login0.text:
        print('Your account has been banned!\n Please try again in 8 hours ')
        exit()
    login_data = login0.json()
    random_hash = login_data['random_hash']
    code = input('Send the code sent in the Telegram account: ')
    
    login_data = {
        'phone': phone_number,
        'random_hash': random_hash,
        'password': code
    }
    
    login = req.post('https://my.telegram.org/auth/login', data=login_data)
    
    apps_page = req.get('https://my.telegram.org/apps')
    soup = BeautifulSoup(apps_page.text, 'html.parser')
    try:
        api_id = soup.find('label', string='App api_id:').find_next_sibling('div').select_one('span').get_text()
        api_hash = soup.find('label', string='App api_hash:').find_next_sibling('div').select_one('span').get_text()
        key = soup.find('label', string='Public keys:').find_next_sibling('div').select_one('code').get_text()
        Pc = soup.find('label', string='Production configuration:').find_next_sibling('div').select_one('strong').get_text()
        time.sleep(3)
        print(f"""
      __    ____  ____
     /__\\  (  _ \\(_  _)
    /(__)\\  )___/ _)(_
   (__)(__)(__)  (____)

    APIs successfully received:

        Api ID: {api_id}
        Api HASH: {api_hash}

        Public Key: {key}
        Production configuration: {Pc}
        """)
    except:
        print ('\33[31mIt is not possible to get APIs for you!\ntry again after 24hr...\33[0m')
