import sys
from importlib import reload

def main():
    
    while(1):
	    menu = int(input("Menu:\n1. Sembunyikan Pesan\n2. Ekstraksi Pesan\n3. Hitung PSNR\n4. Keluar\nPilih Menu:"))
	    if (menu == 1):
	    	if ('hide' not in sys.modules):
	    		import hide
	    	else:
	    		hide = reload(hide)
	    elif (menu == 2):
	    	if ('extract' not in sys.modules):
	    		import extract
	    	else:
	    		extract = reload(extract)
	    elif (menu == 3):
	    	if ('psnr' not in sys.modules):
	    		import psnr
	    	else:
	    		psnr = reload(psnr)
	    elif (menu == 4):
	    	break
	    else:
	        raise Exception("Enter correct input")
main()
