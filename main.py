import datetime
from twilio.rest import Client
import random

def tampilkan_menu():
    sekarang = datetime.datetime.now()
    jam = sekarang.strftime("%H:%M:%S")
    hari = sekarang.strftime("%A")
    bulan = sekarang.strftime("%B")
    tahun = sekarang.year

    print("BIG BOY")
    print(f"Jam: {jam}")
    print(f"Hari: {hari}")
    print(f"Bulan: {bulan}")
    print(f"Tahun: {tahun}")
    print("-------")
    nomor = input("Masukkan nomor WhatsApp (+62): ")
    print("-------")
    return nomor

def kirim_otp(nomor):
    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    from_whatsapp_number = 'whatsapp:+YOUR_TWILIO_WHATSAPP_NUMBER'

    client = Client(account_sid, auth_token)

    otp = random.randint(100000, 999999)
    pesan = f"Kode OTP Anda adalah: {otp}"

    message = client.messages.create(
        body=pesan,
        from_=from_whatsapp_number,
        to=f'whatsapp:{nomor}'
    )

    print(f"OTP telah dikirim ke {nomor}.")
    return otp

if __name__ == "__main__":
    nomor = tampilkan_menu()
    kirim_otp(nomor)
