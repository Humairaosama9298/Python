#                 ***** Task 3 *****

#            ***** Smart Calculator *****

import operator

def smart_calculator():
    print(" Welcome to the Smart Calculator!")
    print(" Choose an operation:")
    print("1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)")
    
    ops = {"1": ("Addition", operator.add), "2": ("Subtraction", operator.sub), 
           "3": ("Multiplication", operator.mul), "4": ("Division", operator.truediv)}
    
    while True:
        choice = input("\n Enter choice (1-4) or 'q' to quit: ").strip()
        
        if choice.lower() == 'q':
            print(" Exiting... Thank you for using Smart Calculator! ")
            break
        
        if choice in ops:
            num1 = input(" Enter first number: ")
            num2 = input(" Enter second number: ")
            
            if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
                print(" Error: Please enter valid numbers!")
                continue
            
            num1, num2 = float(num1), float(num2)
            if choice == "4" and num2 == 0:
                print(" Error: Division by zero is not allowed!")
                continue
            
            operation_name, operation_func = ops[choice]
            print(f" {operation_name} Result: {operation_func(num1, num2)}")
        else:
            print(" Invalid choice. Please enter a number between 1 and 4.")

smart_calculator()

#            ***** End of Task 3 *****