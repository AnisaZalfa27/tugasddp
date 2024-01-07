from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

# class LoginApp(tk.Tk): ini parameter, ga seharusnya diisi argument
class LoginApp:
    # def __init__(self): nambahin root, isi rootnya window baru
    def __init__(self, root):
        # super().__init__() ga butuh super() karena ini bukan inheritence class
        self.root = root
        self.root.title("Login")

        # self.label_username = tk.Label(self, text="Username:") ga butuh tk karena import di awal langsung * (line 1)
        self.label_username = Label(self.root, text="Username:")
        self.label_username.pack()

        self.entry_username = Entry(self.root)
        self.entry_username.pack()

        self.label_password = Label(self.root, text="Password:")
        self.label_password.pack()

        self.entry_password = Entry(self.root, show="*")
        self.entry_password.pack()

        self.tombol_login = Button(self.root, text="Login", command=self.cek_login)
        self.tombol_login.pack()

        self.root.mainloop() # langsung dipanggil di sini

    def cek_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        valid_users = {"ferisha": {
            "password":"123456",
            "nim":"0110223286"
            }, "zalfa": {
                "password":"123456",
                "nim":"0110223269"
            }, "loista": {
                "password":"123456",
                "nim":"0110223271"
            }, "irkham": {
                "password":"123456",
                "nim":"0110223284"
            }}

        # ini bagian pengecekan apakah username tersebut ada dengan cara mengecek nilai key-nya
        if username not in valid_users:
            messagebox.showerror("Login Gagal", "Username atau password salah")
        else:
            if password == valid_users[username]['password']:
                messagebox.showinfo("Login Berhasil", "Selamat datang, " + username)
                self.root.destroy() # ini langsung ngapus window login
                # pengecekan berhasil langsung manggil class jadwalpelajaran, dan ngirim username dan nimnya sebagai argument
                JadwalPelajaranApp(Tk(), username, valid_users[username]['nim'])
            else:
                messagebox.showerror("Login Gagal", "Username atau password salah")

class JadwalPelajaranApp:
    def __init__(self, root, username, nim):
        self.root = root
        self.root.title("Jadwal Pelajaran TI09")

        self.username = username # ngambil usernamenya dari paramter
        self.nim = nim # ini juga

        self.label_nama = Label(self.root, text="Nama : ")
        self.label_nama.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nama = Entry(self.root, width=30)
        self.entry_nama.insert(0, self.username) # memasukkan nilai ke entry
        self.entry_nama.configure(state="disabled") # menjadikan entry tidak bisa diapa-apakan
        self.entry_nama.grid(row=0, column=1, padx=10, pady=10)

        self.label_nim = Label(self.root, text="Nim :")
        self.label_nim.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nim = Entry(self.root, width=30)
        self.entry_nim.insert(0, self.nim) # ini sama aja kayak tadi
        self.entry_nim.configure(state="disabled") # ini juga
        self.entry_nim.grid(row=1, column=1, padx=10, pady=10)

        self.hari = ["senin", "selasa", "rabu", "kamis", "jumat"]

        self.label_hari = Label(self.root, text="Pilih Hari:")
        self.label_hari.grid(row=2, column=0, padx=10, pady=10)
        self.combobox_hari = Combobox(self.root, values=self.hari)
        self.combobox_hari.grid(row=2, column=1, padx=10, pady=10)

        self.tombol_tampilkan = Button(self.root, text="Tampilkan Jadwal", command=self.tampilkan_jadwal)
        self.tombol_tampilkan.grid(row=3, column=0, columnspan=2, pady=10)

        self.label_jadwal = Label(self.root, text="")
        self.label_jadwal.grid(row=4, column=0, columnspan=2, pady=10)

    def tampilkan_jadwal(self):
        nama = self.entry_nama.get()
        nim = self.entry_nim.get()
        hari_terpilih = self.combobox_hari.get()

        jadwal = {
            "senin": " 13.00 - 15.30 = Pemograman web",
            "selasa": " 08.00 - 10.30 = Sistem Operasi \n13.00 - 15.00 = Dasar - dasar pemograman",
            "rabu": "Matematika Komputer",
            "kamis": " 13.00 - 15.30 = Pengantar teknologi Informasi",
            "jumat": "10.00 - 11.30 = Bahasa indonesia,\n13.30 - 15.00 = Pembentukan Karakter \n15.30 - 17.00 = Pendidikan Agama Islam",
        }

        jadwal_terpilih = jadwal.get(hari_terpilih, "Jadwal tidak ditemukan")
        self.label_jadwal.config(text=f"Nama : {nama} \nNim :{nim}\nJadwal anda pada hari {hari_terpilih}:\n{jadwal_terpilih}")

class AppManager:
    def __init__(self):
        self.login_app = LoginApp(Tk()) # isinya TK() nanti di masukkin ke self.root

if __name__ == "__main__":
    app_manager = AppManager()