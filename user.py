import csv
from datetime import datetime
from re import A

db_users = "databases/users.csv"
db_loans = "databases/loans.csv"
db_devices = "databases/devices.csv"

def member(username):
    print("=============== USER ===============")
    print("1. Peminjaman Console")
    print("2. Cek Status Peminjaman")

    choice = input("Select an option: ")

    if choice == "1":
        peminjaman_console(username)
        # menu_console()
    elif choice == "2":
        cek_status_peminjaman()
    else:
        print("Invalid choice. Please try again.")
        member(username)

def peminjaman_console(username):
    # Hitung jumlah baris data (exclude header)
    with open(db_loans, mode="r", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        new_id = sum(1 for _ in reader) + 1

    # Cek status member dari users.csv
    is_member = None
    with open(db_users, mode="r", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[2] == username:
                is_member = row[7]  # Ambil status member (0 = ya, 1 = bukan)
                break

    if is_member is None:
        print("Data user tidak ditemukan.")
        return

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
    print(f"Nama Peminjam (otomatis): {username}")
    print("Daftar Console Tersedia:")

    for i, device in enumerate(ready_devices, start=1):
        harga = device[4] if is_member == "0" else device[3]  # 0 = anggota, 1 = bukan
        print(f"{i}. {device[1]} ({device[2]}) - Harga: Rp{harga}")

    try:
        pilih = int(input("Pilih nomor console: ")) - 1
        if pilih < 0 or pilih >= len(ready_devices):
            print("Pilihan tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    selected = ready_devices[pilih]
    nama_console = f"{selected[1]} ({selected[2]})"

    tanggalPinjam = input("Tanggal Pinjam (format DD-MM-YYYY): ")
    tanggalKembali = input("Tanggal Kembali (format DD-MM-YYYY): ")

    with open(db_loans, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_id, username, nama_console, tanggalPinjam, tanggalKembali])
        print(f"\nPeminjaman oleh '{username}' berhasil dicatat dengan ID {new_id}.\n")

def cek_status_peminjaman():
    print("asd")