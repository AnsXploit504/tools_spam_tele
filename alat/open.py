import requests, time, os, sys

# WARNA ANSI
R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
B = '\033[34m'
C = '\033[36m'
M = '\033[35m'
W = '\033[0m'

# Efek ketik ala typing
def ketik(teks, delay=0.003):
    for char in teks:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Clear & Header
os.system("clear")
ketik(f"""{C}
╔══════════════════════════════════════════════════════════╗
║{M}       ⛧ A N S X P L O I T   -   T E L E G R A M   S P A M M E R{C}       ║
╠══════════════════════════════════════════════════════════╣
║   {Y}Made by:{W} FRIANS504             {Y}Mode:{W} Group Spam via Bot           {C}║
╚══════════════════════════════════════════════════════════╝
""", 0.002)

# Input keren
def input_box(label):
    ketik(f"{Y}╔═[ {B}{label}{Y} ]")
    return input(f"{Y}╚═══▶ {W}")

# Ambil input
TOKEN   = input_box("TOKEN BOT TELEGRAM")
GROUPID = input_box("ID GRUP (cth: -1001234567890)")
PESAN   = input_box("ISI PESAN SPAM")
JUMLAH  = int(input_box("JUMLAH PESAN"))
JEDA    = float(input_box("JEDA (DETIK) ANTAR PESAN"))

# Konfirmasi sebelum spam
os.system("clear")
ketik(f"""{M}
╔════════════════════════════════════════╗
║       {C}K O N F I R M A S I   T A R G E T{M}       ║
╠════════════════════════════════════════╣
║  {Y}Group ID  :{W} {GROUPID}
║  {Y}Jumlah    :{W} {JUMLAH}
║  {Y}Jeda      :{W} {JEDA} detik
║  {Y}Pesan     :{W} {PESAN[:35]}{'...' if len(PESAN)>35 else ''}
╚════════════════════════════════════════╝{W}
""", 0.002)

time.sleep(1)
ketik(f"{C}⇒ Memulai pengiriman pesan...{W}\n", 0.01)

# URL API
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Mulai spam
for i in range(1, JUMLAH + 1):
    res = requests.post(url, data={
        "chat_id": GROUPID,
        "text": PESAN
    })

    if res.status_code == 200:
        print(f"{G}[{i}] ✔️ Terkirim ke group ID: {GROUPID}{W}")
    else:
        print(f"{R}[{i}] ✘ Gagal! Error: {res.text}{W}")

    time.sleep(JEDA)

# Penutup
ketik(f"""{C}
╔═══════════════════════════════════════╗
║    ✓ Semua pesan berhasil dikirim!    ║
║    Tool: {M}AnsXploit Telegram Spammer{C}     ║
╚═══════════════════════════════════════╝{W}
""", 0.01)