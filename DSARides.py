import collections
from tabulate import tabulate

ride_queues = {
    "Horror Virtual Reality Game": collections.deque(),
    "Interstellar Orbit": collections.deque(),
    "Underwater Safari": collections.deque(),
    "FlightZone X": collections.deque(),
    "Undead Airborne Adventure": collections.deque()
}

def inputdanbayar(jumlah_orang, jenis_tiket, booked_names):
    names = []
    harga_tiket = 0
    if jenis_tiket == "VIP":
        harga_tiket = 500000
    elif jenis_tiket == "reguler":
        harga_tiket = 150000
    
    for idx in range(jumlah_orang):
        nama = input("Ayo, masukkan nama kamu: ")
        print(f"Hallo pengunjung dengan nama {nama}, kamu mendapat antrian untuk booking ticket ke {idx + 1} silahkan antri yaa hehe:)")
        while True:
            pembayaran = int(input(f"Harga tiket {jenis_tiket}: {harga_tiket}. Kamu membayar berapa?: "))
            if pembayaran == harga_tiket:
                names.append(nama)
                booked_names.append((nama, jenis_tiket)) 
                print("Yay, pembayaran kamu sudah diterima! Selamat bersenang-senang!")
                print(f"Wahh {nama} anda telah keluar dari antrian booking ticket nih, sekarang masuk antrian pilih wahana, silahkan antri yaa!")
                break
            else:
                print("Ups, jumlah pembayaran kamu kurang. Yuk, coba lagi.")
    return names


def displaynamaorder(booked_names):
    table_data = [(idx + 1, name, ticket_type) for idx, (name, ticket_type) in enumerate(booked_names)]
    print("Nama dan No antrian yang udah booking ticket:")
    print(tabulate(table_data, headers=["Line Number", "Name", "Ticket Type"], tablefmt="grid"))
    print("Data-data di atas adalah orang orang yang keluar dari dari antrian booking ticket, mau masuk antrian wahana nii hehe")


def tampilkanantrian(antrian):
    print("Antrian:")
    for idx, nama in enumerate(antrian, start=1):
        print(f"{idx}. {nama}")


def masukwahana(nama_orang, pilihan_wahana):
    print("\nSelamat datang di", pilihan_wahana, "!")
    for nama in nama_orang:
        ride_queues[pilihan_wahana].append(nama)
    print(f"Yay {nama_orang} telah memilih wahana {pilihan_wahana}! Selamat menikmati wahana-wahana kami yaa!!.")


def pesantiket(booked_names):
    print("\nYuk, pesan tiket!")
    print("1. Tiket VIP (Rp. 500.000)")
    print("2. Tiket Reguler (Rp. 150.000)")
    pilihan = int(input("Mau pesan yang mana nih? (1-2): "))
    if pilihan == 1:
        jenis_tiket = "VIP"
    elif pilihan == 2:
        jenis_tiket = "reguler"
    else:
        print("Ups, pilihan kamu gak valid nih.")
        return None, pesantiket(booked_names)

    jumlah = int(input("Berapa banyak orang yang akan memesan tiket? "))

    if jumlah == 0:
        print("Wah, kamu belum pesan tiket nih.")
        return None, None  

    names = inputdanbayar(jumlah, jenis_tiket, booked_names)

    return names, jenis_tiket



def menuutama():
    print("\n----------------------------------Menu Utama----------------------------------")
    print("1. Info Seru Tentang Fun World")
    print("2. Pesan Tiket")
    print("3. Masuk dan Nikmati Wahana")
    print("4. Keluar")


def cektiket(booked_names):
    if booked_names:
        return True
    else:
        print("Aduh, kayaknya kamu belum pesan tiket nih. Yuk, pesan dulu! Silahkan pilih menu 2 yaa untuk memesan ticket! :) ")
        return False


def menumasukwahana():
    if cektiket(booked_names):
        print("\n++++++++++\tSelamat datang ke antrian masuk wahana!, silahkan pilih wahana apa yang ingin dinikmati!\t++++++++++")
        return True
    else:
        return False


def pilihanmasukwahana(booked_names):
    if cektiket(booked_names):
        print("\nPengunjung yang telah memesan tiket:")
        tampilkanantrian([nama for nama, _ in booked_names])
        for nama, jenis_tiket in booked_names:
            max_wahana = 5 if jenis_tiket == "VIP" else 3
            print(f"\nHai {nama}, pilih {max_wahana} wahana yang ingin kamu kunjungi:\n Note: ketika anda memilih wahana lebih dari 1x maka hanya akan terdata 1x, maka sebaiknya anda memilih wahana yang berbeda-beda!!, ayo coba semua wahana")
            pilihan_wahana = []
            while len(pilihan_wahana) < max_wahana:
                print("\nIni adalah menu pilihan Wahana, silahkan pilih:")
                idx = 1
                for wahana in ride_queues.keys():
                    print(f"{idx}. {wahana}")
                    idx += 1
                choice = input(f"Pilih wahana ke-{len(pilihan_wahana) + 1} (1-{len(ride_queues)}): ")
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(ride_queues):
                        pilihan_wahana.append(list(ride_queues.keys())[choice - 1])
                    else:
                        print("Wah, pilihannya gak ada nih.")
                except ValueError:
                    print("Wah, pilihannya gak valid nih. Masukin angkanya ya.")
            for wahana_pilihan in pilihan_wahana:
                masukwahana([nama], wahana_pilihan)


def displaystatuswahana(booked_names):
    print("\nStatus Wahana:")
    for wahana, antrian in ride_queues.items():
        print(f"\n{wahana}:")
        nama_terpilih = [nama for nama, _ in booked_names if nama in antrian]
        if nama_terpilih:
            nama_unik = list(set(nama_terpilih))
            for nama in nama_unik:
                print(nama)
        else:
            print("Belum ada pengunjung yang memilih wahana ini.")


booked_names = [] 
while True:
    menuutama()
    pilihan = int(input("Masukkan pilihan kamu: "))
    
    if pilihan == 1:
        print("Informasi Seru Tentang Fun World")
        print ('\t\t-- FUN WORLD --')
        print ('Lokasi : Prov.Sulawesi Utara, Kab.Minahasa Utara, Kec.Airmadidi, Jl.Arnold Mononutu')
        print ('Jam Operasional : Senin-Jumat = 09:00 - 19:00')
        print ('\t\t\t\t Sabtu-Minggu = 07:00 - 19:00')
        print('------------------------------------------------------------------------------------------')
        print ('Syarat dan Ketentuan')
        print ('1. Wajib memesan tiket terlebih dahulu di Website online, Jika tidak maka tidak bisa masuk')
        print ('2. Pengunjung minimal berusia >16 Tahun')
        print ('3. untuk 1 pemesanan tiket hanya bisa diklaim untuk 1 orang')
        print ('4. Tidak boleh membawah makanan dari luar')
        print ('5. Dilarang merokok dan membawah minuman keras')
        print ('6. Dilarang Senjata Tajam dan Senjata Api')
        print ('7. Membawa tumbler dari rumah (bisa di refil di lokasi)')
        print ('--PENGUNJUNG BERTANGGUNG JAWAB ATAS BARANG BAWAAN SENDIRI DAN BERTANGGUNG JAWAB ATAS KEAMANAN PRIBADI MEREKA SELAMA KUNJUNGAN--')
        print ('--Jika terjadi kehilangan barang maka itu diluar tanggung jawab Fun World--')
        print ('--Jika didapati tidak memenuhi syarat dan ketentuan diatas ini maka akan dikenakan denda--')
    elif pilihan == 2:
        nama_orang, jenis_tiket = pesantiket(booked_names)
        if nama_orang:
            print("\nTiket sudah dipesan:")
            displaynamaorder(booked_names)
    elif pilihan == 3:
        if menumasukwahana():
            pilihanmasukwahana(booked_names)
            displaystatuswahana(booked_names)
    elif pilihan == 4:
        print("Terima kasih sudah datang! Datang lagi yaa hehehehe")
        break
    else:
        print("Pilihan kamu gak valid nih. Yuk, pilih lagi.:(")