import os
import sys
import time
import random
import string
import imaplib
import email
from email.header import decode_header
import platform
import base64
import subprocess
import requests


# ===== COLORS =====
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
N = '\x1b[0m'


# ===== KEY SYSTEM (from mahin.py) =====
def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)

def notice():
    runtxt("\n\033[0;91m🧞‍♀️ YOU ARE NOT PREMIUM USER ")
    runtxt("\033[0;93m 🔇 SENT THIS KEY TO ADMIN >> %s%s"%(G,basesplit))
    runtxt("\033[0;92m ADMIN🧞‍♀️ WHATSAPP >> +923040827647")


plist = (platform.uname())[2]
basex = plist.encode('ascii')
basex2 = base64.b64encode(basex)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')

def check_key():
    try:
        plr = requests.get('https://github.com/Shahzada302/Ayesha/blob/main/approval.txt').text
        if basesplit in plr:
            print(f"{G}[✓] PREMIUM USER DETECTED")
            print(f"{G}Your Key : {basesplit}")
            return True
        else:
            print(f"{R}[×] KEY NOT APPROVED")
            notice()
            return False
    except requests.exceptions.ConnectionError:
        print(f"{R}[!] NO INTERNET CONNECTION")
        sys.exit()


# ===== LOGO / BANNER =====
 LOGO = """
\033[1;32m
  _           
 \033[1;31m   /\                  | |          
 \033[1;32m  /  \  _   _  ___  ___| |__   __ _ 
 \033[1;31m / /\ \| | | |/ _ \/ __| '_ \ / _` |
 \033[1;32m/ ____ \ |_| |  __/\__ \ | | | (_| |
 \033[1;31m/_/    \_\__, |\___||___/_| |_|\__,_|
 \033[1;32m          __/ |                      
 \033[1;31m         |___/                       

\033[1;37m--------------------------------------------------
\033[1;37m[•] AUTHOR     : \033[1;32mAYESHA
\033[1;37m[•] FACEBOOK   : \033[1;32m@AYESHA CREATOR
\033[1;37m[•] CONTACT    : \033[1;32m03040827647
\033[1;37m[•] TOOL TYPE  : \033[1;32mTEMPMAIL
\033[1;37m[•] STATUS     : \033[1;32mPREMIUM
\033[1;37m--------------------------------------------------
\033[1;37m[•] VERSION    : \033[1;32m1.0
\033[1;37m--------------------------------------------------
\033[1;37m[•] ENTER YOUR REQUIREMENTS BELOW
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_logo():
    print(LOGO)

def generate_random_alias(domain="rssa.gy"):
    length = random.randint(5, 10)
    alias = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return f"{alias}@{domain}"


def main_tool():
    domain = "rssa.gy"
    username = "raza@rssa.gy"
    password = "xxx#1122"
    imap_server = "mail.gandi.net"

    while True:
        temp_email = generate_random_alias(domain)
        clear_screen()
        show_logo()
        print("\nGenerated Temporary Email:", temp_email)

        mail_received = False

        while not mail_received:
            imap = imaplib.IMAP4_SSL(imap_server)
            imap.login(username, password)
            imap.select("INBOX")

            status, messages = imap.search(None, "UNSEEN")
            mail_ids = messages[0].split()

            clear_screen()
            show_logo()
            print(f"Checking for mails to {temp_email}")

            for mail_id in mail_ids[::-1]:
                status, msg_data = imap.fetch(mail_id, "(RFC822)")
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        to_ = msg.get("To", "")
                        if temp_email in to_:
                            subj, encoding = decode_header(msg["Subject"])[0]
                            if isinstance(subj, bytes):
                                subj = subj.decode(encoding if encoding else "utf-8")
                            sender = msg.get("From")
                            clear_screen()
                            show_logo()
                            print(f"\nSubject: {subj}")
                            print(f"From: {sender}")

                            if msg.is_multipart():
                                for part in msg.walk():
                                    ctype = part.get_content_type()
                                    disp = str(part.get("Content-Disposition"))
                                    if ctype == "text/plain" and "attachment" not in disp:
                                        body = part.get_payload(decode=True).decode(errors="ignore")
                                        print(body)
                            else:
                                body = msg.get_payload(decode=True).decode(errors="ignore")
                                print(body)
                            print("="*50)

                            mail_received = True

            imap.logout()

            if not mail_received:
                print("No new mail yet. Checking again in 5 seconds...")
                time.sleep(5)

        input("Mail receive ho gaya hai. Agla tempmail generate karne ke liye Enter dabayen...")


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    if check_key():
        main_tool()
    else:
        sys.exit()
