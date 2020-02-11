def palindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    return False

if __name__=='__main__':
    word = str(input("Ingresa una palabra: "))
    result = palindrome(word)
    if result:
        print("Es palindrome")
    else:
        print("No es palindrome")