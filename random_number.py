import random

def run():
    random_number = random.randint(0,20)
    number_found = False
    while not number_found:
        number = int(input("Ingrese un numero: "))
        if number == random_number:
            print("Lo encontraste")
            number_found = True
        elif number > random_number:
            print("El numero es menor")
        else: 
            print("El numero es mayor")
            
if __name__ == '__main__':
    run()