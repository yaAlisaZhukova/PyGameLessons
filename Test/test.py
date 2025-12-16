toxic = input()
toxic2 = input()

listUm = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
listYad = [toxic, toxic2]

while True:
    print(listUm)
    input('Какую хочешь сьесть?')
    eat = input()
    if eat == listYad[0] or eat == listYad[1]:
        print("TOXIC!")
        break
    listUm.remove(eat)