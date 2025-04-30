def member():
    print("=============== USER ===============")
    print("1. Peminjaman Console")
    print("2. Cek Status Peminjaman")

    choice = input("Select an option: ")

    if choice == "1":
        print(peminjaman_console())
        # menu_console()
    elif choice == "2":
        print(cek_status_peminjaman())
    else:
        print("Invalid choice. Please try again.")
        member()

def peminjaman_console():
    print("\n=== Peminjaman Console Game ===")
    nama_peminjam = input("Masukkan nama peminjam: ").strip()
    nama_console = input("Masukkan nama console: ").strip()
    tanggal_pinjam = input("Masukkan tanggal pinjam (format DD-MM-YYYY): ").strip()
    tanggal_kembali = input("Masukkan tanggal kembali (format DD-MM-YYYY): ").strip()

    with open("console_loans.txt", "a") as file:
        file.write(f"PEMINJAMAN|{nama_peminjam}|{nama_console}|{tanggal_pinjam}|{tanggal_kembali}\n")

    print(f"\nPeminjaman oleh '{nama_peminjam}' berhasil disimpan.\n")

    return member()

def cek_status_peminjaman():
    print("\n=== Peminjaman Console Game ===")
    nama_peminjam = input("Masukkan nama peminjam: ").strip()
    nama_console = input("Masukkan nama console: ").strip()
    tanggal_pinjam = input("Masukkan tanggal pinjam (format DD-MM-YYYY): ").strip()

    with open("console_loans.txt", "a") as file:
        file.write(f"PEMINJAMAN|{nama_peminjam}|{nama_console}|{tanggal_pinjam}\n")

    print(f"\nPeminjaman oleh '{nama_peminjam}' berhasil disimpan.\n")

    return member()