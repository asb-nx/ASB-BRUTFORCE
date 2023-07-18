import os,sys
logo =("""
\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m BRUT-FORCE
\033[1;32m[-] AUTHOR    :\033[1;32m ASB ASHIS 
\033[1;32m[-] GITHUB    :\033[1;32m asb-nx
\033[1;32m[-] FACEBOOK  :\033[1;32m ASB ASHIS BISWAS
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m I AM NX \033[;0m\033[1;91m═══>\033[1;92m{ASB}""")

    
os.system('clear')
print(logo)
print("\033[1;32m[1]\033[0;93m free[best]")
xx = input("\033[1;34m[+] chose method brute force : \033[0;93m")

if xx in ["1", "01"]:
	os.system("python bf.py")
	