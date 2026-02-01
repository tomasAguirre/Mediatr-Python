from Addition.Add import Add
from Subtraction.Subtract import Subtract

class Factory_Operation():

    def Get_Add(self):
        add = Add();
        return add;

    def Get_Subtract(self):
        sustract = Subtract()
        return sustract;
