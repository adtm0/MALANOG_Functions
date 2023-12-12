def main():
    print(f"""1: Find the smallest factor of a number
2: Find the prime numbers within a given range
3: Do Both""")
    user_input = input("What do you want to do?: ")

    if user_input == '1':
        print("\nSmallest factor of a number:\n")
        s_fact()
    elif user_input == '2':
        print("\nPrime numbers within a given range:\n")
        prime_range()
    elif user_input == '3':
        print("\nSmallest factor of a number:\n")
        s_fact()
        print("\nPrime numbers within a given range:")
        prime_range()
    else:
        print("Invalid input.")
        main()
        
def s_fact():
    num = int(input("Enter an integer >= 2: "))
    
    while bool(num >= 2) == False:
        print("Invalid input. Enter a number greater than 2.")
        num = int(input("Enter an integer >= 2: "))
        
    if num >= 2:
        for i in range(2, num + 1):
            if num % i == 0:
                break
            else:
                i += 1
        print(f"The smallest factor other than 1 for {num} is {i}.")
    
def prime_range():
    n_start = eval(input("Enter a number [start]: "))

    if n_start == 0:
        print("Program terminated.")
        exit()

    while (n_start < 0):
        print("Enter a non-negative number.")
        n_start = eval(input("\nEnter a number [start]: "))
     
    n_end = eval(input("Enter a number [end]: "))

    while (n_end < n_start):
        print(f"Enter a number greater than {n_start}.")
        n_end = eval(input("\nEnter a number [end]: "))

    prime_list = []
    for i in range(n_start, n_end + 1):
    
        if i == 1:
            continue
    
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
                prime_list.append(i)
            
    print(f"\nPrime numbers between {n_start} and {n_end} are: {str(prime_list).strip('[],').replace(',','')}")
    
main()