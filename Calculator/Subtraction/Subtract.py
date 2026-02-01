from AbsOperation import AbsOperation

class Subtract(AbsOperation):
    def operate(self, num1, num2):
        print("Subtract operation :  ",  (int(num1) - int(num2)))

