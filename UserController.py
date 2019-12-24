from models.UserModel import UserModel

user = UserModel()

def get():
    global user
    print("Menampilkan Semua Data User Yang Ada")
    print("-----------------")
    print(user.get())

def find():
    global user
    print("Mencari User Sesuai ID User")
    print("-----------------")
    id = input("Masukkan ID: ")
    user = user.find(id)
    if len(user):
        print(f"Data {user[1]} {user[2]} ditemukan!") 
        print("-----------------")
        print(user)       

def select():
    global user
    print("Mencari User Dengan Kata Kunci")
    print("-----------------")
    key = input("Masukkan Kata Kunci(id,name,username,gender,address): ")
    value = input(f"Masukkan {key}: ")
    if key == "name":
        values = value.split()
        if len(values) == 2:
            user = user.select().where("firstname","like",values[0]).andwhere("lastname","like",values[1]).one()
        else:
            user = user.select().where("firstname","like",values[0]).one()
    else:
        user = user.select().where(key,"like",value).one()

    if user != None:
        print(f"Data {value} ditemukan!") 
        print("-----------------")
        print(user)   
    else:
        print(f"Data {value} tidak ditemukan!")

def create():
    global user
    print("Membuat User Baru")
    print("-----------------")

    firstname = input("Nama Depan: ")
    if firstname == "":
        print("Nama Depan tidak boleh kosong")
        firstname = input("Nama Depan: ")

    lastname = input("Nama Belakang: ")
    if lastname == "":
        print("Nama Belakang tidak boleh kosong")
        lastname = input("Nama Belakang: ")

    username = input("Username: ")
    if username == "":
        print("Username tidak boleh kosong")
        username = input("Username: ")

    password = input("Password: ")
    if password == "":
        print("Password tidak boleh kosong")
        password = input("Password: ")

    gender = input("Jenis Kelamin(Pria/Wanita): ")
    if gender == "":
        print("Jenis Kelamin tidak boleh kosong")
        gender = input("Jenis Kelami(Pria/Wanita): ")

    address = input("Alamat: ")
    if address == "":
        print("Alamat tidak boleh kosong")
        address = input("Alamat: ")

    data = {
        "firstname":firstname,
        "lastname":lastname,
        "username":username,
        "password":password,
        "gender":gender,
        "address":address,
    }

    user = user.create(data).execute()

    if user:
        print("Berhasil!")
    else:
        print("Gagal!")


def main():
    actions = ("(1) Menampilkan Semua Data User","(2) Mencari User berdasarkan ID","(3) Mencari User berdasarkan kata kunci","(4) Membuat User Baru")
    action = input(f"Apa yang ingin anda lakukan? {actions} : ")
    action = int(action)
    if action == 1:
        get()
    elif action == 2:
        find()
    elif action == 3:
        select()
    elif action == 4:
        create()
    else:
        print("Perintah yang anda masukkan tidak bisa diproses!")

main()