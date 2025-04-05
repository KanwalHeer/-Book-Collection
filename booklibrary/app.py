class Calculator:
    def __init__(self):
        num1 = 0
        num2 = 0

    def get_input(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def add(self):
        result = self.num1 + self.num2 
        print(f"The result of addition is: {result}.")

    def subtract(self):
        result = self.num1 - self.num2 
        print(f"The result of addition is: {result}.")

    def multiply(self):
        result = self.num1 * self.num2
        print(f"The result of multiplication is: {result}")

    def divide(self):
        result = self.num1 / self.num2
        print(f"The result od division is: {result}") 


    def start_calculator(self):

        while True: 
            print("*********** Welcome to Simple Calculator Project**************")
            print("Which operation do you want to perform?")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            user_choice = input("Choose the number from (1-4): ")
        
            if user_choice in ["1","2","3","4"]:
               self.get_input()
            if user_choice == "1":
                self.add()
            elif user_choice == "2":
                  self.subtract()
            elif user_choice == "3":
                  self.multiply()
            elif user_choice == "4":
                  if self.num2 == 0:
                      print("Cannot be divided by zero!")
                  else:
                      self.divide()
            elif user_choice == "5":
                  print("Thanks for using my calculator!")
                  break
            else:
               print("Invalid choice! Try again.")
                                       
if __name__ == "__main__":
    calc = Calculator()
    calc.start_calculator()


        

