import csv
from datetime import datetime

db_users = "databases/users.csv"
db_loans = "databases/loans.csv"
db_devices = "databases/devices.csv"

def member():
    print("=============== USER ===============")
    print("1. Peminjaman Console")
    print("2. Cek Status Peminjaman")

    choice = input("Select an option: ")

    if choice == "1":
        peminjaman_console()
        # menu_console()
    elif choice == "2":
        cek_status_peminjaman()
    else:
        print("Invalid choice. Please try again.")
        member()

def peminjaman_console():
    # Hitung jumlah baris data (exclude header)
    with open(db_loans, mode="r", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        new_id = sum(1 for _ in reader) + 1

    # Ambil console yang Ready
    ready_devices = []
    with open(db_devices, mode="r", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[5].lower() == "ready":
                ready_devices.append(row)

    if not ready_devices:
        print("Maaf, semua console sedang dipinjam.")
        return

    print("\n=========== PEMINJAMAN CONSOLE ===========")
    nama = input("Nama Peminjam: ").strip()
    print("Daftar Console Tersedia:")

    for i, device in enumerate(ready_devices, start=1):
        print(f"{i}. {device[1]} ({device[2]}) - Harga Member: Rp{device[4]}")

    pilih = int(input("Pilih nomor console: ")) - 1
    if pilih < 0 or pilih >= len(ready_devices):
        print("Pilihan tidak valid.")
        return

    selected = ready_devices[pilih]
    nama_console = selected[1] + " (" + selected[2] + ")"

    tanggalPinjam = input("Tanggal Pinjam (format DD-MM-YYYY): ")
    tanggalKembali = input("Tanggal Kembali (format DD-MM-YYYY): ")

    with open(db_loans, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_id, nama, nama_console, tanggalPinjam, tanggalKembali])
        print(f"\nPeminjaman oleh '{nama}' berhasil dicatat dengan ID {new_id}.\n")


def cek_status_peminjaman():
    print("asd")