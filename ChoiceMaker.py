import random

choice_list = []

print("Enter your choices one by one. Type END to start generating a choice:")

def choice_maker():
    while True:
        input_string = input("Enter a choice:")
        if input_string == "END":
            try:
                print("Here is your random choice:", choice_list[random.randint(0,len(choice_list))])
            except IndexError:
                print("You must input atleast 1 choice for the program to run.")
            break
        elif all(list_value == input_string for list_value in choice_list):
            print("This choice has already been inputed. Please input a different choice:")
        else:    
            choice_list.append(input_string)




def main():
    choice_maker()
    print(choice_list)


if __name__ == '__main__':
    main()