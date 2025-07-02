import requests
import time
from datetime import datetime

BOT_TOKEN = '7949577548:AAGUFm__OsMUSThx7FHcl5KSxf3H33fXeIE'
CHAT_ID = '1531962333'
NODE_ID = '11702498'

def waktu_sekarang():
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

def kirim_telegram(pesan):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": pesan,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if not response.ok:
            print(f"❌ Gagal kirim ke Telegram: {response.text}")
    except Exception as e:
        print(f"⚠️ ERROR: {e}")

def mulai_ngintip_node():
    print(f"👀 Mulai mantau Node ID {NODE_ID}...\n")
    last_log = ""

    while True:
        try:
            url = f"https://api.nexus.xyz/v1/node/logs?node_id={NODE_ID}&limit=1"
            response = requests.get(url)
            data = response.json()

            if 'logs' in data and len(data['logs']) > 0:
                log = data['logs'][0]
                log_text = log.get("log", "")
                waktu_log = log.get("created_at", "")

                if log_text != last_log:
                    last_log = log_text
                    pesan = f"""🧠 *NEXUS PROOF DETECTED*
                    
`{log_text}`

🆔 *Node ID*: `{NODE_ID}`
⏰ `{waktu_sekarang()}`"""
                    kirim_telegram(pesan)

        except Exception as e:
            print(f"⚠️ Gagal mantau node: {e}")
        
        time.sleep(15)

mulai_ngintip_node()
