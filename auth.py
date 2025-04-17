import csv
import admin, user, petugas

def register():
    filename = "users.csv"

    # Hitung jumlah baris data (exclude header)
    with open(filename, mode="r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        new_id = sum(1 for _ in reader) + 1

    with open(filename, mode="a", newline="") as f:
        writer = csv.writer(f)
        print("=============== REGISTER ===============")
        email = input("Email: ")
        username = input("Username: ")
        password = input("Password: ")
        password2 = input("Confirm Password: ")
        role = input("Role (member/admin/petugas): ")
        phone = input("Phone Number (08xx): ")

        if password == password2:
            writer.writerow([new_id, email, username, password, role, phone])
            print(f"Registration successful!")
        else:
            print("Passwords do not match.")

def login():
    print("=============== LOGIN ===============")
    username = input("Username: ")
    password = input("Password: ")

    with open("users.csv", mode="r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if row[2] == username and row[3] == password:
                print("Login successful!")
                if row[4] == "admin": # kalau login sebagai admin akan ke page admin
                    print("Welcome, Admin!")
                    admin.admin()
                elif row[4] == "member": # kalau login sebagai member akan ke page member
                    print("Welcome, Member!")
                    user.member()
                elif row[4] == "petugas": # kalau login sebagai petugas akan ke page petugas
                    print("Welcome, Petugas!")
                    petugas.petugas()
                # print("ID: ", row[0])
                # print("Email: ", row[1])
                # print("Username: ", row[2])
                # print("Password: ", row[3])
                # print("Role: ", row[4])
                # print("Phone: ", row[5])
                return True

    print("Login failed. Incorrect username or password.")
    return False

# register()
# login()