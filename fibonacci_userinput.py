def fibonacci():
    #Create i to keep looping through until the input is valid
    i = 0
    while i < 1:
        try:
            #Get user input
            n = input("Enter the nth term in the Fibonacci sequence that you want to know: ")
            user_input = int(n)
            seed1 = 0
            seed2 = 1
            if user_input < 1:
                print("You didn't enter a positive integer, try again")
                continue
            if user_input == 1:
                print("The first number of the Fibonacci sequence is: 0")
                break
            elif user_input == 2:
                print("The second number of the Fibonacci sequence is: 1")
                break
            else:
                #Calculate Fibonacci terms larger than 2
                start = 2
                while start < user_input:
                    result = seed1 + seed2
                    seed1 = seed2
                    seed2 = result
                    start += 1
            i += 1
            if user_input >= 2:
                print(f"The value of your chosen Fibonacci sequence is: {result}")
        except ValueError:
            print("You didn't enter a positive integer, try again")

fibonacci()
