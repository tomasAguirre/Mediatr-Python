from AbsOperation import AbsOperation

class Add(AbsOperation):
    def operate(self, num1, num2):
        print("Add operation :  ",  (int(num1) + int(num2)))

    