def calculator():
    print("Welcome to the True Calculator!")
    print("You can enter an expression like '3 + 5 * (2 - 1)'")
    print("Supported operations: +, -, *, /, (), and more.")
    
    while True:
        # Take input from user
        expression = input("\nEnter your mathematical expression (or type 'exit' to quit): ")
        
        if expression.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        try:
            # Evaluate the expression
            result = eval(expression)  # eval() will handle the operator precedence automatically
            print(f"Result: {result}")
        except (SyntaxError, ZeroDivisionError) as e:
            print(f"Error: {e}. Please enter a valid mathematical expression.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

# Run the calculator
calculator()
