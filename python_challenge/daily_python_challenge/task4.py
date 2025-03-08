#                   ***** Task 4 *****

#            ***** Even or Odd Checker *****

def user_input():
    print("\n" + "="*50)
    print("Welcome to Even-Odd Number Checker Program!")
    print("This program will help you determine if a number is Even or Odd")
    print("="*50)
    
    while True:
        try:
            print("\nEnter 'q' to quit")
            user_number = input("Enter number: ")
            
            # Check if user wants to quit
            if user_number.lower() == 'q':
                print("\nThank you for using Even-Odd Checker!")
                print("="*50)
                break
                
            user_number = int(user_number)
            if user_number % 2 == 0:
                print(f"{user_number} is even")
            else:
                print(f"{user_number} is odd")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

user_input()


#                 ***** End of Task 4 *****
