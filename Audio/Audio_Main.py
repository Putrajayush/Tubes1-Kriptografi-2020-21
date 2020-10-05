def main():
    
    menu = int(input("Menu:\n1. Sembunyikan Pesan\n2. Ekstraksi Pesan\n3. Hitung PSNR\nPilih Menu:"))
    if (menu == 1):
        import hide
    elif (menu == 2):
        import extract
    elif (menu == 3):
        import psnr
    else:
        raise Exception("Enter correct input")

main()
