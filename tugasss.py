import random

print("=" * 32)
print("""
    Selamat Datang Di 
    game tebak angka
""")
print("=" * 32)

player = int(input("Masukkan Angka 1-20 : "))
com = random.randint(1, 20)

if player == com:
    print("selamat Anda Benar")
elif player != com:
    print("maaf anda salah")