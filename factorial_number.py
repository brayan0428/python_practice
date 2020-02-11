def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)

def run():
    number = int(input("Ingrese un numero: "))
    result = fact(number)
    print('El factorial es ' , result)

if __name__ == '__main__':
    run()
