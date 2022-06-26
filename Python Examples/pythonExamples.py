# Rock-Paper-Scissors

def RockPaperScissors(player1, player2):
    while True:
        print("\nÇıkmak için -1'e basınız...\n")
        input1 = input("Lütfen bir seçim yapınız(Taş-Kağıt-Makas): ")
        input2 = input("Lütfen bir seçim yapınız(Taş-Kağıt-Makas): ")

        if input1 == "-1" or input2 == "-1":
            break

        if input1 == "Taş":
            if input2 == "Taş":
                print("Berabere...")
            elif input2 == "Kağıt":
                print("{} isimli oyuncu kazandı..." .format(player2))
            elif input2 == "Makas":
                print("{} isimli oyuncu kazandı..." .format(player1))    
            else:
                print("Yanlış giriş!!! Tekrar deneyin") 

        elif input1 == "Kağıt":
            if input2 == "Taş":
                print("{} isimli oyuncu kazandı..." .format(player1)) 
            elif input2 == "Kağıt":
                print("Berabere...")
            elif input2 == "Makas":
                print("{} isimli oyuncu kazandı..." .format(player2))    
            else:
                print("Yanlış giriş!!! Tekrar deneyin")    

        elif input1 == "Makas":
            if input2 == "Taş":
                print("{} isimli oyuncu kazandı..." .format(player2))
            elif input2 == "Kağıt":
                print("{} isimli oyuncu kazandı..." .format(player1)) 
            elif input2 == "Makas":
                print("Berabere...")      
            else:
                print("Yanlış giriş!!! Tekrar deneyin")    

        else:
            print("Yanlış giriş!!! Tekrar deneyin")  

player1 = input("Lutfen isminizi giriniz: ")
player2 = input("Lutfen isminizi giriniz: ")        
RockPaperScissors(player1, player2)                  

# Number Prediction Game

import random
def NumberPredictionGame(userPrediction):
    produceNumber = random.randint(1,9)
    counter = 0

    while produceNumber != userPrediction:
        counter += 1 
        userPrediction = int(input("Lütfen 1-9 arası bir sayı tahmininde bulunun: "))

        if produceNumber < userPrediction:
            print("Azaltın...")
        elif produceNumber > userPrediction:
            print("Artırın...")
        else:
            print("Tebrikler!!! {} defada doğru bildiniz..." .format(counter))   

userPrediction = 0
NumberPredictionGame(userPrediction)

# List Overlap Comprehensions

def ListOverlapComprehensions(common):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    for i in a:
        for j in b:
            if i == j:
                common.add(i)
    print(common)            

common = set()
ListOverlapComprehensions(common)

# Prime Number

def IsItPrime():

    userNumber = int(input("Lütfen bir sayı giriniz: ")) 
    i = 1

    while i != (userNumber / 2):
        i += 1    
        
        if userNumber % i == 0:
            print("Sayı asal değil")
            break
        else:
            return 0  

IsItPrime()            

# Reverse Word Order

word = input("Lütfen birden fazla kelimeden oluşan bir cümle yazınız ve aralarında boşluk bırakınız: ")
wordList = list(word.split(" "))

i = -1
print("Tersi:", end=" ")
while True:
    print(wordList[i], end=" ")
    i -= 1