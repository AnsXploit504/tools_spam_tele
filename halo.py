#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime

# 🎨 Warna ANSI
C51   = "\033[38;5;51m"    # Cyan
C201  = "\033[38;5;201m"   # Pink
C214  = "\033[38;5;214m"   # Orange
C196  = "\033[38;5;196m"   # Merah
C226  = "\033[38;5;226m"   # Kuning
C46   = "\033[38;5;46m"    # Hijau
RESET = "\033[0m"
WHITE = "\033[38;5;15m"

# 📂 Folder tempat file spam
FOLDER_SPAM = "alat"

# 🔗 Sosial Media
TIKTOK   = "tiktok.com/@ansxploit"
GITHUB   = "github.com/AnsXploit504"
TELEGRAM = "t.me/olla098"

# Efek ketik
def ketik(teks, delay=0.002):
    for char in teks:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Bersihkan layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Banner
def banner():
    clear()
    now = datetime.now()

    # Hari & Bulan Indonesia
    hari_list = {
        "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu",
        "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu", "Sunday": "Minggu"
    }
    bulan_list = {
        "January": "Januari", "February": "Februari", "March": "Maret",
        "April": "April", "May": "Mei", "June": "Juni",
        "July": "Juli", "August": "Agustus", "September": "September",
        "October": "Oktober", "November": "November", "December": "Desember"
    }

    hari    = hari_list[now.strftime("%A")]
    tanggal = now.strftime("%d")
    bulan   = bulan_list[now.strftime("%B")]
    tahun   = now.strftime("%Y")
    jam     = now.strftime("%H:%M:%S")

    ketik(f"{C51}╔════════════════════════════════════════════════════════════╗{RESET}")
    ketik(f"{C51}║{C201}          ✦ TOOLS SPAM PESAN BOT TELEGRAM V01.00 ✦          {C51}║{RESET}")
    ketik(f"{C51}║{C214}Tools ini dibuat oleh AnsXploit pada hari {hari}, {tanggal} {bulan} {tahun} pukul {jam}{C51}║{RESET}")
    ketik(f"{C51}╚════════════════════════════════════════════════════════════╝{RESET}")
    
    ketik(f"{C51}╔═══════════════════════ INFO KONTAK ═══════════════════╗{RESET}")
    ketik(f"{C51}║{C214} TikTok  : {TIKTOK.ljust(44)}{C51}║{RESET}")
    ketik(f"{C51}║{C214} GitHub  : {GITHUB.ljust(44)}{C51}║{RESET}")
    ketik(f"{C51}║{C214} Telegram: {TELEGRAM.ljust(44)}{C51}║{RESET}")
    ketik(f"{C51}╚══════════════════════════════════════════════════════╝{RESET}")

# Menu
def menu():
    ketik(f"{C51}╔══════════════════════════════════════════════════════╗{RESET}")
    ketik(f"{C51}║ {C196}[1]{WHITE} 📩 Spam Tele V1{' ' * 32}{C51}║{RESET}")
    ketik(f"{C51}║ {C226}[2]{WHITE} ⚡ Spam Tele V2{' ' * 32}{C51}║{RESET}")
    ketik(f"{C51}║ {C46}[3]{WHITE} 🚀 Spam Tele V3{' ' * 32}{C51}║{RESET}")
    ketik(f"{C51}║ {C196}[0]{WHITE} ❌ Keluar Tools{' ' * 31}{C51}║{RESET}")
    ketik(f"{C51}╚══════════════════════════════════════════════════════╝{RESET}")

# Loading
def loading(teks="Memuat...", durasi=1.4):
    clear()
    ketik(teks, delay=0.004)
    for i in range(25):
        filled = "█" * (i + 1)
        empty = "-" * (25 - i - 1)
        pct = int((i + 1) / 25 * 100)
        warna = C51 if i % 2 == 0 else C201
        sys.stdout.write(f"\r{warna}[{filled}{empty}] {pct}%{RESET}")
        sys.stdout.flush()
        time.sleep(durasi / 25)
    print("\n")

# Jalankan file sesuai pilihan
def run_choice(path):
    target = os.path.join(FOLDER_SPAM, path)
    if not os.path.isfile(target):
        ketik(f"{C196}File tidak ditemukan: {target}{RESET}")
        time.sleep(1.2)
        return
    os.system(f"{sys.executable} \"{target}\"")

# Main loop
def main():
    while True:
        banner()
        menu()
        pilihan = input(f"{WHITE}Pilih menu: {RESET}").strip().lower()

        if pilihan == "1":
            loading("Memuat Spam Tele V1...")
            run_choice("open.py")
        elif pilihan == "2":
            loading("Memuat Spam Tele V2...")
            run_choice("spamtel.py")
        elif pilihan == "3":
            loading("Memuat Spam Tele V3...")
            run_choice("tele.py")
        elif pilihan == "0":
            ketik(f"{C196}Keluar... Terima kasih.{RESET}")
            break
        else:
            ketik(f"{C196}Pilihan tidak valid — coba lagi.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()