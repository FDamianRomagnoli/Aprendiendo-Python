def main():
    # dict = {}

    # for i in range(1,101):
    #     if i%3 != 0:
    #         dict[i] = i**2

    # dict = {i: i**3 for i in range(1,101) if i%3 != 0}

# estructura
# {key: value for value in iterable if condition}


#Reto

    dict = {x: x**0.5 for x in range(1,1001)}

    print(dict)


if __name__ == "__main__":
    main()