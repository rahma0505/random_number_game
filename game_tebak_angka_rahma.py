import random
from getpass import getpass
import login_Anthony
import highscore_Anthony

#==============================================================================

myMenu = []
credentials = login_Anthony.Credentials()
high_score = highscore_Anthony.Highscore()

#==============================================================================

def menu_utama():     
    print(25 * "=" , "Tebak Angka" , 25 * "=")
    print(63 * "=")
    print("Daftar Menu")
    print("[1] Main")
    print("[2] Daftar")
    print("[3] High Score")
    print("[0] Keluar")
    print(63 * "=")
    pilih_menu()

def pilih_menu():
    opsi=input("Ketik pilihan angka pada daftar menu: ")
    if opsi == '1':
        hasil = credentials.login()
        if (hasil != False):
             print ("Score awal anda saat ini 100")
             main(hasil)
             high_score.save()
        else:
             print ("user password salah")
             menu_utama()
           
    elif opsi == '2':
        print(10*'*'+'Daftar User baru'+10*'*')
        username=input('Daftar Username : ').lower()
        password=getpass('Password : ')
        credentials.daftar(username,password)

    elif opsi == '3':
        high_score.show()

    elif opsi == '0':
          print('Terimakasih. Sampai jumpa :)')
          exit()
        
menu_utama()

#==============================================================================

def main ():
    rand_num = random.randint( 0, 100)
    guess = 11
    tebakan_bnr = False
    score = 100
    
    print("*" * 60)
    print("GAME TEBAK ANGKA\n")
    print("Tebaklah angka 1 sampai 100")
    print("Score akan berkurang 10 jika tebakanmu salah")
    print("Jika kamu beri jawaban selain angka, score dikurangi 20\n")
    print("*" * 60)

    while score>0 and guess != rand_num:
        print("Score mu saat ini ", score, "\n")
        try:
            guess = int(input("Angka tebakan: "))
            if guess == rand_num:
                tebakan_bnr = True
            elif guess > rand_num:
                score -= 10
                print("angka terlalu besar\n")
            else:
                score -= 10
                print("angka terlalu kecil\n")
        except ValueError:
            score -= 20
            print("itu bukan angka\n")
        
    if tebakan_bnr:
        print("selamat kamu benar! score kamu ", score)
        return score
    else:
        print("Permainan selesai! Score kamu : ", score)
        return score   
main()

#==============================================================================

