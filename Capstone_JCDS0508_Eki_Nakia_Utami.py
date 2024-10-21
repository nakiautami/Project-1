# Nama              : Eki Nakia Utami
# Kelas             : JCDS0805
# CAPSTONE MODUL 1  : DATA NILAI SISWA MATA PELAJARAN KIMIA SEMSTER GANJIL TAHUN 2024

#========================================================================================================================================================================
from tabulate import tabulate
from prettytable import PrettyTable
import os

# Fungsi untuk membersihkan layar console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# DATABASE USER
user_data = {
    "admin": {"password": "12345", "role": "admin"}, # Admin bisa tambah, edit, dan hapus
    "guru": {"password": "12345", "role": "guru"} # guru bisa tambah data
}

# DATABASE DATA SISWA
list_dict_data = [
    {
        'NIS': 2923059,
        'Nama': 'Lembayung Senja',
        'Kelas': '11',
        'Semester': 'Ganjil',
        'NilaiTugas': 87,
        'NilaiUTS': 92,
        'NilaiUAS': 89
    },
    {
        'NIS': 2923214,
        'Nama': 'Cesa Adriani',
        'Kelas': '11',
        'Semester': 'Ganjil',
        'NilaiTugas': 82,
        'NilaiUTS': 69,
        'NilaiUAS': 81
    },
    {
        'NIS': 2923228,
        'Nama': 'Katon Bagaskara',
        'Kelas': '11',
        'Semester': 'Ganjil',
        'NilaiTugas': 63,
        'NilaiUTS': 70,
        'NilaiUAS': 76
    },
    {
        'NIS': 2923115,
        'Nama': 'Bumi Ayu',
        'Kelas': '11',
        'Semester': 'Ganjil',
        'NilaiTugas': 88,
        'NilaiUTS': 87,
        'NilaiUAS': 79
    },
    {
        'NIS': 2923307,
        'Nama': 'Ginan Prambudi',
        'Kelas': '11',
        'Semester': 'Ganjil',
        'NilaiTugas': 63,
        'NilaiUTS': 78,
        'NilaiUAS': 56
    }
]

# KKM (Kriteria Ketuntasan Minimal)
KKM = 75 

# Fungsi untuk memvalidasi panjang digit input
def validate_input(prompt, max_digits):
    while True:
        try:
            value = input(prompt)
            if len(value) > max_digits:
                raise ValueError(f"Input tidak boleh lebih dari {max_digits} digit.")
            return int(value)
        except ValueError as e:
            print(f"Error: {e}. Silakan coba lagi.")

# Fungsi untuk memvalidasi panjang digit input PIN
def validate_pin(prompt, max_digits):
    while True:
        pin = input(prompt).strip()  
        if len(pin) > max_digits:
            print(f"PIN tidak boleh lebih dari {max_digits} digit. Silakan coba lagi.")
        else:
            return pin

# Fungsi untuk menampilkan data siswa dengan indeks
def tampilkan_siswa_dengan_index():
    """Menampilkan daftar siswa dengan indeks."""
    if not list_dict_data:
        print("Tidak ada data siswa untuk ditampilkan.")
        return
    
    # Menambahkan kolom indeks di awal
    for index, siswa in enumerate(list_dict_data, start=1):
        siswa_with_index = {'Index': index}  
        siswa_with_index.update(siswa) 
        list_dict_data[index - 1] = siswa_with_index

    # Menampilkan tabel
    print(tabulate(list_dict_data, headers="keys", tablefmt="pretty"))

# Fungsi untuk menampilkan data siswa
def read_menu():
    clear_console()
    print("="*50)
    print("Menampilkan seluruh data Siswa")
    print("="*50)
    
    if not list_dict_data:
        print("Tidak ada data siswa untuk ditampilkan.")
    else:
        print(tabulate(list_dict_data, headers="keys", tablefmt="pretty"))
    input("\nTekan Enter untuk kembali ke menu utama.")
    clear_console()

# Fungsi untuk menambahkan data siswa (hanya untuk Guru)
def add_menu_guru():
    clear_console()
    print("="*50)
    print("Menambahkan Data Siswa Baru (GURU)")
    print("="*50)

    try:
        nis = validate_input("Masukkan NIS (maksimal 8 digit): ", 8)

        if any(siswa['NIS'] == nis for siswa in list_dict_data):
            print("\nNIS ini sudah terdaftar. Silakan masukkan NIS yang lain.")
            input("\nTekan Enter untuk kembali ke menu utama.")
            clear_console()
            return

        nama = input("Masukkan Nama: ")
        kelas = input("Masukkan Kelas: ")
        semester = input("Masukkan Semester: ")
        nilai_tugas = validate_input("Masukkan Nilai Tugas (maksimal 3 digit 0-100): ", 3)
        nilai_uts = validate_input("Masukkan Nilai UTS (maksimal 3 digit 0-100): ", 3)
        nilai_uas = validate_input("Masukkan Nilai UAS (maksimal 3 digit 0-100): ", 3)

        # Konfirmasi sebelum menambahkan data
        confirm = input("\nAnda yakin ingin menambahkan data ini? (ya/tidak): ").strip().lower()
        if confirm == 'ya':
            list_dict_data.append({
                'NIS': nis,
                'Nama': nama,
                'Kelas': kelas,
                'Semester': semester,
                'NilaiTugas': nilai_tugas,
                'NilaiUTS': nilai_uts,
                'NilaiUAS': nilai_uas
            })
            print("\nData siswa berhasil ditambahkan. Jika ada perubahan, silakan hubungi Admin.")
        else:
            print("\nPenambahan data dibatalkan.")
    except ValueError:
        print("\nInput tidak valid. Pastikan Anda memasukkan angka yang benar.")
    input("\nTekan Enter untuk kembali ke menu utama.")
    clear_console()

# FUNGSI MENU UNTUK GURU
def main_menu_guru():
    while True:
        clear_console()
        print("="*50)
        print("SISTEM INFORMASI NILAI SISWA (GURU)")
        print("="*50)

        print('''
        1. Tampilkan Data Siswa
        2. Tambah Data Siswa
        3. Informasi Transkrip Nilai Siswa
        4. Keluar
        ''')

        choice = input("Silakan pilih menu (1-4): ").strip()

        if choice == '1':
            read_menu()
        elif choice == '2':
            add_menu_guru()
        elif choice == '3':
            count_menu()
        elif choice == '4':
            return
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            input("\nTekan Enter untuk melanjutkan.")

# Fungsi untuk menambahkan data siswa
def add_menu():
    """
    Memungkinkan pengguna untuk menambahkan data siswa baru ke database,
    dengan konfirmasi sebelum menambahkan.
    """
    clear_console()
    print("="*50)
    print("Menambahkan Data Siswa Baru")
    print("="*50)
    
    try:
        nis = validate_input("Masukkan NIS (maksimal 8 digit): ", 8)
        
        # Pengecekan apakah NIS sudah terdaftar
        if any(siswa['NIS'] == nis for siswa in list_dict_data):
            print("\nNIS ini sudah terdaftar. Silakan masukkan NIS yang lain.")
            input("\nTekan Enter untuk kembali ke menu utama.")
            clear_console()
            return

        nama = input("Masukkan Nama: ")
        kelas = input("Masukkan Kelas: ")
        semester = input("Masukkan Semester: ")
        nilai_tugas = validate_input("Masukkan Nilai Tugas (maksimal 3 digit 0-100): ", 3)
        nilai_uts = validate_input("Masukkan Nilai UTS (maksimal 3 digit 0-100): ", 3)
        nilai_uas = validate_input("Masukkan Nilai UAS (maksimal 3 digit 0-100): ", 3)

        # Konfirmasi sebelum menambahkan data
        confirm = input("\nAnda yakin ingin menambahkan data ini? (ya/tidak): ").strip().lower()
        if confirm == 'ya':
            list_dict_data.append({
                'NIS': nis,
                'Nama': nama,
                'Kelas': kelas,
                'Semester': semester,
                'NilaiTugas': nilai_tugas,
                'NilaiUTS': nilai_uts,
                'NilaiUAS': nilai_uas
            })
            print("\nData siswa berhasil ditambahkan.")
        else:
            print("\nPenambahan data dibatalkan.")
    except ValueError:
        print("\nInput tidak valid. Pastikan Anda memasukkan angka yang benar.")
    input("\nTekan Enter untuk kembali ke menu utama.")
    clear_console()

# Fungsi untuk mengubah data siswa berdasarkan kolom tertentu
def change_menu():
    """
    Mengubah data siswa yang sudah ada berdasarkan NIS, 
    dengan konfirmasi sebelum menyimpan perubahan.
    """
    clear_console()
    print("="*50)
    print("Mengubah Data Siswa")
    print("="*50)
    
    try:
        nis = validate_input("Masukkan NIS siswa yang ingin diubah (maksimal 8 digit): ", 8)
        for siswa in list_dict_data:
            if siswa['NIS'] == nis:
                print("\nPilih data yang ingin diubah:")
                print("1. Nama")
                print("2. Kelas")
                print("3. Semester")
                print("4. Nilai Tugas")
                print("5. Nilai UTS")
                print("6. Nilai UAS")
                
                pilihan = input("\nMasukkan pilihan (1-6): ")
                
                if pilihan == '1':
                    siswa['Nama'] = input("Masukkan Nama baru: ")
                elif pilihan == '2':
                    siswa['Kelas'] = input("Masukkan Kelas baru: ")
                elif pilihan == '3':
                    siswa['Semester'] = input("Masukkan Semester baru: ")
                elif pilihan == '4':
                    siswa['NilaiTugas'] = validate_input("Masukkan Nilai Tugas baru (maksimal 3 digit 0-100): ", 3)
                elif pilihan == '5':
                    siswa['NilaiUTS'] = validate_input("Masukkan Nilai UTS baru (maksimal 3 digit 0-100): ", 3)
                elif pilihan == '6':
                    siswa['NilaiUAS'] = validate_input("Masukkan Nilai UAS baru (maksimal 3 digit 0-100): ", 3)
                else:
                    print("Pilihan tidak valid. Tidak ada perubahan yang dilakukan.")
                    input("\nTekan Enter untuk kembali ke menu utama.")
                    clear_console()
                    return
                
                # Konfirmasi sebelum menyimpan perubahan
                confirm = input("\nAnda yakin ingin menyimpan perubahan ini? (ya/tidak): ").strip().lower()
                if confirm == 'ya':
                    print("\nData siswa berhasil diubah.")
                else:
                    print("\nPerubahan data dibatalkan.")
                break
        else:
            print("Siswa dengan NIS tersebut tidak ditemukan.")
    except ValueError:
        print("\nInput tidak valid. Pastikan Anda memasukkan angka yang benar.")
    input("\nTekan Enter untuk kembali ke menu utama.")
    clear_console()

# Fungsi untuk menghapus data siswa
def delete_menu():
    """
    Menghapus data siswa berdasarkan NIS yang dimasukkan oleh pengguna,
    dengan konfirmasi sebelum menghapus.
    """
    clear_console()
    print("="*50)
    print("Menghapus Data Siswa")
    print("="*50)
    
    try:
        nis = validate_input("Masukkan NIS siswa yang ingin dihapus (maksimal 8 digit): ", 8)
        for siswa in list_dict_data:
            if siswa['NIS'] == nis:
                # Konfirmasi sebelum menghapus data
                confirm = input(f"\nAnda yakin ingin menghapus data siswa {siswa['Nama']}? (ya/tidak): ").strip().lower()
                if confirm == 'ya':
                    list_dict_data.remove(siswa)
                    print("\nData siswa berhasil dihapus.")
                else:
                    print("\nPenghapusan data dibatalkan.")
                break
        else:
            print("Siswa dengan NIS tersebut tidak ditemukan.")
    except ValueError:
        print("\nInput tidak valid. Pastikan Anda memasukkan angka yang benar.")
    input("\nTekan Enter untuk kembali ke menu utama.")
    clear_console()

# Fungsi untuk menghitung rata-rata dan nilai akhir
def hitung_rata_rata(nilai_tugas, nilai_uts, nilai_uas):
    return (nilai_tugas + nilai_uts + nilai_uas) / 3

def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    bobot_tugas = 0.3  # 30% dari tugas
    bobot_uts = 0.3    # 30% dari UTS
    bobot_uas = 0.4    # 40% dari UAS

    return (nilai_tugas * bobot_tugas) + (nilai_uts * bobot_uts) + (nilai_uas * bobot_uas)

# Fungsi untuk menghitung rata-rata dan nilai akhir seluruh siswa
def tampilkan_rata_rata_dan_index_akhir_semua_siswa():
    hasil_siswa = []
    
    for siswa in list_dict_data:
        rata_rata = hitung_rata_rata(siswa['NilaiTugas'], siswa['NilaiUTS'], siswa['NilaiUAS'])
        index_akhir = hitung_nilai_akhir(siswa['NilaiTugas'], siswa['NilaiUTS'], siswa['NilaiUAS'])
        status = "Lulus" if index_akhir >= KKM else "Tidak Lulus"
        
        hasil_siswa.append({
            'Index': siswa['Index'],
            'Nama': siswa['Nama'],
            'NIS': siswa['NIS'],
            'KKM': KKM,
            'Rata-Rata': f"{rata_rata:.2f}",
            'Nilai Akhir': f"{index_akhir:.2f}",
            'Status': status
        })
    
    # Menampilkan hasil dalam bentuk tabel
    print("\n" + "=" * 80)
    print(f"{'Rata-rata dan Nilai Akhir Semua Siswa':^80}")
    print("=" * 80)
    print(tabulate(hasil_siswa, headers="keys", tablefmt="pretty"))
    print("=" * 80)

# Submenu perhitungan
def count_menu():
    while True:
        clear_console()
        tampilkan_siswa_dengan_index()  # Menampilkan daftar siswa di atas submenu
        print("="*50)
        print("Sub Menu Informasi Nilai Siswa")
        print("="*50)

        print('''
        1. Informasi Rata-rata Nilai Siswa
        2. Informasi Nilai Akhir Siswa Berdasarkan Index
        3. Tampilkan Rata-rata dan Nilai Akhir Semua Siswa
        4. Kembali ke Menu Utama
        ''')

        count_submenu = input('Silakan Pilih Menu (1/2/3/4): ')
        
        if count_submenu == '1':
            search_key = input("Masukkan NIS atau index siswa untuk menghitung rata-rata (maksimal 8 digit): ")
            siswa_ditemukan = False
            
            # Mencari siswa berdasarkan NIS atau Index
            for siswa in list_dict_data:
                if str(siswa['NIS']) == search_key or str(siswa['Index']) == search_key:
                    rata_rata = hitung_rata_rata(siswa['NilaiTugas'], siswa['NilaiUTS'], siswa['NilaiUAS'])
                    status = "Lulus" if rata_rata >= KKM else "Tidak Lulus"
                    
                    # Menampilkan output dalam bentuk tabel menggunakan PrettyTable
                    x = PrettyTable()
                    x.field_names = ["Nama", "NIS", "KKM", "Rata-Rata", "Status"]
                    x.add_row([siswa['Nama'], siswa['NIS'], KKM, f"{rata_rata:.2f}", status])
                    
                    print("\n" + "=" * 60)
                    print(f"{'Rata-rata Nilai Siswa':^60}")
                    print("=" * 60)
                    print(x)
                    print("=" * 60)
                    
                    siswa_ditemukan = True
                    break
            
            if not siswa_ditemukan:
                print("Siswa dengan NIS atau index tersebut tidak ditemukan.")
            input("\nTekan Enter untuk kembali.")
        
        elif count_submenu == '2':
            search_key = input("Masukkan NIS atau index siswa untuk menghitung nilai akhir (maksimal 8 digit): ")
            siswa_ditemukan = False
            
            # Mencari siswa berdasarkan NIS atau Index
            for siswa in list_dict_data:
                if str(siswa['NIS']) == search_key or str(siswa['Index']) == search_key:
                    nilai_akhir = hitung_nilai_akhir(siswa['NilaiTugas'], siswa['NilaiUTS'], siswa['NilaiUAS'])
                    status = "Lulus" if nilai_akhir >= KKM else "Tidak Lulus"
                    
                    # Menampilkan output dalam bentuk tabel menggunakan PrettyTable
                    x = PrettyTable()
                    x.field_names = ["Nama", "NIS", "Nilai Akhir", "Status", "KKM"]
                    x.add_row([siswa['Nama'], siswa['NIS'], f"{nilai_akhir:.2f}", status, KKM])
                    
                    print("\n" + "=" * 60)
                    print(f"{'Nilai Akhir Siswa':^60}")
                    print("=" * 60)
                    print(x)
                    print("=" * 60)
                    
                    siswa_ditemukan = True
                    break
            
            if not siswa_ditemukan:
                print("Siswa dengan NIS atau index tersebut tidak ditemukan.")
            input("\nTekan Enter untuk kembali.")
        
        elif count_submenu == '3':
            tampilkan_rata_rata_dan_index_akhir_semua_siswa()
            input("\nTekan Enter untuk kembali.")
        
        elif count_submenu == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# FUNGSI UNTUK MENAMPILKAN MENU UTAMA
def main_menu_admin():
    while True:
        clear_console()
        print("="*50)
        print("SISTEM INFORMASI NILAI SISWA (ADMIN)")
        print("="*50)

        print('''
        1. Tampilkan Data Siswa
        2. Tambah Data Siswa
        3. Ubah Data Siswa
        4. Hapus Data Siswa
        5. Informasi Transkrip Nilai Siswa
        6. Keluar
        ''')

        choice = input("Silakan pilih menu (1-6): ").strip()

        if choice == '1':
            read_menu()
        elif choice == '2':
            add_menu()  
        elif choice == '3':
            change_menu()
        elif choice == '4':
            delete_menu()
        elif choice == '5':
            count_menu()
        elif choice == '6':
            return
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            input("\nTekan Enter untuk melanjutkan.")

# Fungsi untuk login
def login():
    while True:
        clear_console()
        print("="*50)
        print("=== Menu Login ===")
        print("="*50)

        print('''
        1. LOGIN ADMIN
        2. LOGIN GURU
        3. KELUAR PROGRAM
        ''')

        choice = input("Silakan pilih (1-3): ").strip()

        if choice == '1':
            username = input("Masukkan username: ").strip()  # Menghilangkan whitespace di sekitar input
            password = validate_pin("Masukkan Password (PIN maksimal 5 digit): ", 5)

            if username in user_data and user_data[username]['password'] == password:
                role = user_data[username]['role']
                print(f"\nSelamat datang '{username}' sebagai {role.capitalize()} di dashboard nilai Siswa.")
                input("\nTekan Enter untuk melanjutkan ke dashboard.")
                main_menu_admin()  # Menu untuk Admin
            else:
                print("\nUsername atau Password salah atau tidak ditemukan.")
                input("Tekan Enter untuk mencoba lagi.")

        elif choice == '2':
            username = input("Masukkan username: ").strip()  # Menghilangkan whitespace di sekitar input
            password = validate_pin("Masukkan Password (PIN maksimal 5 digit): ", 5)

            if username in user_data and user_data[username]['password'] == password:
                role = user_data[username]['role']
                print(f"\nSelamat datang '{username}' sebagai {role.capitalize()} di dashboard nilai Siswa.")
                input("\nTekan Enter untuk melanjutkan ke dashboard.")
                main_menu_guru()  # Menu untuk Guru
            else:
                print("\nUsername atau Password salah atau tidak ditemukan.")
                input("Tekan Enter untuk mencoba lagi.")

        elif choice == '3':
            confirm_exit = input("Anda yakin ingin keluar dari program? (ya/tidak): ").strip().lower()
            if confirm_exit == 'ya':
                print("Terima kasih! Program telah dihentikan.")
                exit()  # Keluar dari program
            else:
                continue  # Kembali ke menu login jika tidak yakin

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    login()
