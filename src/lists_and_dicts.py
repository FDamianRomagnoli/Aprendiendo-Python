from cmath import sqrt


def main():
    # my_list = [1, "Hello", True, 4.5]
    # my_dict = {
    #     "firstname": "Franco",
    #     "lastname": "Garcia"
    # }

    # super_list = [
    #     {
    #     "firstname": "Franco",
    #     "lastname": "Garcia"},
    #     {
    #     "firstname": "Jose",
    #     "lastname": "Garcia"},
    #     {
    #     "firstname": "Pepe",
    #     "lastname": "Garcia"}
    # ]

    # super_dict = {
    #     "natural_nums": [1,2,3,4,5],
    #     "integer_nums": [-1, -2, 0, 1 , 2],
    #     "floating_nums": [1,1, 4.5, 6.43]
    # }

    # for values in super_list:
    #     for key,value in values.items():
    #         print(key,"-",value)
    list = []
    for i in range(100):
        list.append(i ** 2)
    print(list)




if __name__ == '__main__':
    main()