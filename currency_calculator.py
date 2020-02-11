
def convert_ammount(ammount):
    mex_to_col = 145.97
    return mex_to_col * ammount

def run():
    print("C A L C U L A D O R A D E D I V I S A S")
    ammount = float(input("Ingresa la cantidad de pesos mexicanos que quieres convertir: "))
    result = convert_ammount(ammount)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))

if __name__ == '__main__':
    run()