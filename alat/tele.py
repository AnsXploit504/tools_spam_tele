import os
import sys
import time
import random
import requests

# Warna neon
COLORS = [
    "\033[91m", "\033[92m", "\033[93m",
    "\033[94m", "\033[95m", "\033[96m"
]
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def neon_text(text, delay=0.002):
    for char in text:
        sys.stdout.write(random.choice(COLORS) + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def neon_box(title):
    color = random.choice(COLORS)
    length = len(title) + 2
    print(color + "╔" + "═" * length + "╗" + RESET)
    print(color + f"║ {title} ║" + RESET)
    print(color + "╚" + "═" * length + "╝" + RESET)

def progress_bar(progress, total):
    bar_len = 30
    filled_len = int(bar_len * progress // total)
    bar = "█" * filled_len + "-" * (bar_len - filled_len)
    sys.stdout.write(random.choice(COLORS) + f"[{bar}] {int(100 * progress / total)}%\r" + RESET)
    sys.stdout.flush()

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        r = requests.post(url, data=payload, timeout=5)
        return r.status_code == 200 and r.json().get("ok")
    except requests.RequestException:
        return False

def main():
    clear()
    neon_text("""
 █████╗ ███╗   ██╗███████╗██╗  ██╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔══██╗████╗  ██║██╔════╝██║  ██║██║  ██║██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
███████║██╔██╗ ██║███████╗███████║███████║██████╔╝██║     ██║   ██║██║   ██║   
██╔══██║██║╚██╗██║╚════██║██╔══██║██╔══██║██╔═══╝ ██║     ██║   ██║██║   ██║   
██║  ██║██║ ╚████║███████║██║  ██║██║  ██║██║     ███████╗╚██████╔╝██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
                    SPAM TELEGRAM — AnsXploit
""", delay=0.0005)

    neon_box("INPUT DATA")
    token = input(random.choice(COLORS) + "Token Bot     : " + RESET).strip()
    target_id = input(random.choice(COLORS) + "ID Target     : " + RESET).strip()
    message = input(random.choice(COLORS) + "Pesan         : " + RESET).strip()
    jumlah = int(input(random.choice(COLORS) + "Jumlah Kirim  : " + RESET))
    jeda = input(random.choice(COLORS) + "Jeda (d/m/j)  : " + RESET).strip().lower()

    # konversi jeda ke detik
    unit = jeda[-1]
    val = int(jeda[:-1]) if len(jeda) > 1 else 0
    if unit == "d":
        delay_sec = val
    elif unit == "m":
        delay_sec = val * 60
    elif unit == "j":
        delay_sec = val * 3600
    else:
        delay_sec = 0

    for i in range(jumlah):
        clear()
        neon_box("STATUS")
        neon_text("[TENANG BOS BUKAN ERRO PESAN AKAN TETAP TERKIRIM]", delay=0.003)

        sukses = send_message(token, target_id, message)

        clear()
        neon_box("HASIL")
        if sukses:
            neon_text(f"[WANJAYS PESAN DI KIRIM BOOS] ({i+1}/{jumlah})", delay=0.003)
        else:
            neon_text(f"[ASU COK GAGAL TERKIRIM] ({i+1}/{jumlah})", delay=0.003)

        for p in range(31):
            progress_bar(p, 30)
            time.sleep(0.02)
        print()
        time.sleep(delay_sec)

    clear()
    neon_box("SELESAI BOS")
    neon_text("🔥 Semua pesan sudah diproses. Terima kasih telah menggunakan AnsXploit!", delay=0.002)

if __name__ == "__main__":
    main()