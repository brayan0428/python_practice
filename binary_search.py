def f_binary_search(numbers,number_to_find,low,high):
  if low > high:
    return False
  
  mid = int((low + high) / 2)
  if numbers[mid] == number_to_find:
        return True
  elif numbers[mid] > number_to_find:
        f_binary_search(numbers,number_to_find,0, mid - 1)
  else:
        f_binary_search(numbers,number_to_find,mid + 1, high)

if __name__ == '__main__':
  numbers = [1,3,4,5,6,7,8,9,10,15,23,45,67]
  number_to_find = int(input("Ingrese un numero: "))
  result = f_binary_search(numbers, number_to_find,0, len(numbers) - 1)
  print(result)
  if result is True:
    print("El numero si esta en la lista")
  else:
    print("El numero no esta en la lista")