def main():
    text = input('Ingrese un texto para saber si es polindromo -> ')
    print(palindrome(text))


palindrome = lambda text: text == text[::-1]


if __name__ == '__main__':
    main()