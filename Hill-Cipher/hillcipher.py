#Nama    : Adrian Jeremia Kurniawan
#NPM     : 140810220047
#Kelas   : A
#Program : Hill Cipher

import numpy as np

def main():
    while True:
        print("\nPilih Operasi:\n")
        print("1. Enkripsi\n2. Dekripsi\n3. Cari Kunci\n4. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan in ['1', '2']:
            ukuran_blok = int(input("\nMasukkan dimensi matriks kunci (n x n): "))
            if ukuran_blok != 2:
                print("Harus matriks 2x2.")
                continue

            matriks_kunci = buat_matriks_kunci(ukuran_blok)
            if matriks_kunci is None:
                continue

            teks = ''
            while len(teks) < ukuran_blok:
                teks = siapkan_teks("Masukkan teks")

            hasil = proses_hill_cipher("enkripsi" if pilihan == '1' else "dekripsi", teks, matriks_kunci, ukuran_blok)
            if hasil:
                print(f"\nHasil {'Enkripsi' if pilihan == '1' else 'Dekripsi'}:")
                print(hasil)

        elif pilihan == '3':
            teks_asli = siapkan_teks("Masukkan plaintxt")
            teks_sandi = siapkan_teks("Masukkan ciphertxt")

            matriks_kunci = temukan_kunci(teks_asli, teks_sandi, 26)
            if matriks_kunci is not None:
                print("\nMatriks Kunci:")
                print(matriks_kunci)

        elif pilihan == '4':
            break

        else:
            print("\nPilihan tidak valid.\n")

def konversi_karakter_ke_indeks(karakter):
    return ord(karakter) - ord('A')

def konversi_indeks_ke_karakter(indeks):
    return chr(indeks + ord('A'))

def hitung_fpb(a, b):
    if a == 0:
        return b, 0, 1
    fpb, x1, y1 = hitung_fpb(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return fpb, x, y

def cari_invers_modulo(a, m):
    fpb, x, _ = hitung_fpb(a, m)
    if fpb != 1:
        return None
    return x % m

def hitung_invers_modular(matriks, modulo):
    determinan = int(round(np.linalg.det(matriks)))
    invers_det = cari_invers_modulo(determinan % modulo, modulo)
    if invers_det is None:
        return None
    invers_matriks = np.round(invers_det * np.linalg.inv(matriks) * determinan).astype(int) % modulo
    return invers_matriks

def validasi_kunci(matriks):
    determinan = int(round(np.linalg.det(matriks)))
    return not (determinan % 2 == 0 or determinan % 13 == 0)

def buat_matriks_kunci(ukuran):
    elemen_kunci = list(map(int, input("Masukkan matriks kunci: ").split()))
    if len(elemen_kunci) != ukuran * ukuran:
        print(f"Jumlah elemen tidak sesuai.")
        return None
    return np.array(elemen_kunci).reshape(ukuran, ukuran) % 26

def siapkan_teks(prompt):
    return input(prompt + ": ").replace(" ", "").upper()

def tentukan_ukuran_blok(teks):
    panjang = len(teks)
    if panjang >= 9:
        return 3 
    elif panjang >= 4:
        return 2 
    else:
        print("Teks terlalu pendek")
        return None

def proses_hill_cipher(operasi, pesan, matriks_kunci, ukuran_blok):
    determinan = int(round(np.linalg.det(matriks_kunci)))

    if determinan % 2 == 0 or determinan % 13 == 0:
        print("Determinan tidak valid")
        return

    if len(pesan) % ukuran_blok != 0:
        pesan += pesan[-1] * (ukuran_blok - len(pesan) % ukuran_blok)

    indeks_pesan = [konversi_karakter_ke_indeks(kar) for kar in pesan]
    matriks_pesan = np.array(indeks_pesan).reshape(-1, ukuran_blok)
    matriks_hasil = np.array([])

    if operasi == 'dekripsi':
        invers_mod_det = cari_invers_modulo(determinan % 26, 26)
        if invers_mod_det is None:
            print("Dekripsi gagal.")
            return
        invers_matriks_kunci = invers_mod_det * np.round(np.linalg.inv(matriks_kunci) * determinan).astype(int) % 26
        print("\nMatriks Kunci untuk Dekripsi:")
        print(invers_matriks_kunci)
        matriks_kunci = invers_matriks_kunci
    else:
        print("\nMatriks Kunci untuk Enkripsi:")
        print(matriks_kunci)

    for baris in matriks_pesan:
        vektor_hasil = np.dot(matriks_kunci, baris) % 26
        matriks_hasil = np.append(matriks_hasil, vektor_hasil)

    pesan_hasil = ''.join([konversi_indeks_ke_karakter(int(num)) for num in matriks_hasil])
    return pesan_hasil

def konversi_teks_ke_matriks(teks, ukuran):
    indeks = [konversi_karakter_ke_indeks(kar) for kar in teks]
    return np.array(indeks).reshape(ukuran, ukuran)

def temukan_kunci(teks_asli, teks_sandi, panjang_kunci):
    if len(teks_asli) != len(teks_sandi):
        print("Panjang plaintxt dan ciphertxt tidak sama")
        return None
    
    masih_mencari = True
    kunci = None
    while len(teks_asli) >= 4 and masih_mencari:
        potongan_asli = teks_asli[:4]
        potongan_sandi = teks_sandi[:4]
        teks_asli = teks_asli[2:]
        teks_sandi = teks_sandi[2:]
        
        matriks_asli = konversi_teks_ke_matriks(potongan_asli, 2).flatten()
        matriks_sandi = konversi_teks_ke_matriks(potongan_sandi, 2).flatten()
        
        matriks_asli2 = np.zeros((2, 2), dtype=int)
        matriks_sandi2 = np.zeros((2, 2), dtype=int)
        
        for i in range(2):
            for j in range(2):
                indeks = i*2 + j
                matriks_asli2[j, i] = matriks_asli[indeks]
                matriks_sandi2[j, i] = matriks_sandi[indeks]
        
        if validasi_kunci(matriks_asli2):
            invers_asli = hitung_invers_modular(matriks_asli2, panjang_kunci)
            if invers_asli is not None:
                kunci = np.matmul(matriks_sandi2, invers_asli) % 26
                masih_mencari = False
    
    if masih_mencari:
        print("Tidak dapat menemukan kunci")
    return kunci

if __name__ == "__main__":
    main()