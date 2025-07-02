def get_input():
    print("Enter a number to see its multiplication table:")
    num = input()
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input. Please enter a positive number.")
        return get_input()

def print_table(n):
    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")

def main():
    number = get_input()
    print_table(number)

if __name__ == "__main__":
    main()
    print("helllo!!!")
    print("helllo!!!")
    print("helllo!!!")

    print("helllo!!!")
    
    print("helllo!!!")
    print("gitg")