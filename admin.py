from datetime import datetime

fileusers = "users.csv"
fileloans = "loans.csv"
fileconsoles = "consoles.csv"

def admin():
    print("=============== ADMIN ===============")
    print("1. Menu User")
    print("2. Menu Console")
    print("3. Menu Peminjaman")
    print("4. Keluar")

    choice = input("Select an option: ")

    if choice == "1":
        print("menu_user()")
        # menu_user()
    elif choice == "2":
        print("menu_console()")
        # menu_console()
    elif choice == "3":
        # print("menu_peminjaman()")
        menu_peminjaman()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please try again.")
        admin()



def tambah_peminjaman():
    print("\n=== Tambah Peminjaman Console Game ===")
    nama_peminjam = input("Masukkan nama peminjam: ").strip()
    nama_console = input("Masukkan nama console: ").strip()
    tanggal_pinjam = input("Masukkan tanggal pinjam (format DD-MM-YYYY): ").strip()
    tanggal_kembali = input("Masukkan tanggal kembali (format DD-MM-YYYY): ").strip()

    with open("console_loans.txt", "a") as file:
        file.write(f"PEMINJAMAN|{nama_peminjam}|{nama_console}|{tanggal_pinjam}|{tanggal_kembali}\n")

    print(f"\nPeminjaman oleh '{nama_peminjam}' berhasil disimpan.\n")

def cari_peminjaman():
    print("\n=== Cari Data Peminjaman ===")
    keyword = input("Masukkan nama peminjam yang dicari: ").strip().lower()

    found = False
    with open("console_loans.txt", "r") as file:
        for line in file:
            if line.startswith("PEMINJAMAN"):
                parts = line.strip().split("|")
                if keyword in parts[1].lower():
                    print(f"Nama: {parts[1]}, Console: {parts[2]}, Pinjam: {parts[3]}, Kembali: {parts[4]}")
                    found = True
    if not found:
        print("Data tidak ditemukan.")


def urutkan_peminjaman():
    print("\n=== Urutkan Data Peminjaman ===")
    pilihan = input("Urutkan berdasarkan (1) Nama peminjam atau (2) Tanggal pinjam: ").strip()

    data = []
    with open("console_loans.txt", "r") as file:
        for line in file:
            if line.startswith("PEMINJAMAN"):
                parts = line.strip().split("|")
                data.append(parts)

    if pilihan == "1":
        data.sort(key=lambda x: x[1].lower()) 
    elif pilihan == "2":
        data.sort(key=lambda x: datetime.strptime(x[3], "%d-%m-%Y"))

    for d in data:
        print(f"Nama: {d[1]}, Console: {d[2]}, Pinjam: {d[3]}, Kembali: {d[4]}")


def menu_peminjaman():
    while True:
        print("\n=== Menu Peminjaman Console Game ===")
        print("1. Tambah Peminjaman")
        print("2. Cari Data Peminjaman")
        print("3. Urutkan Data Peminjaman")
        print("4. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_peminjaman()
        elif pilihan == "2":
            cari_peminjaman()
        elif pilihan == "3":
            urutkan_peminjaman()
        elif pilihan == "4":
            print("Kembali ke menu utama.")
            admin()
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    admin()