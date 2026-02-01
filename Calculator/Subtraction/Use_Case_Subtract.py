from Factory.Factory_Operation import Factory_Operation
from mediatr import Mediator
from Subtraction.Subtract_Command import Subtract_Command

@Mediator.handler
class Use_Case_Subtract():
    
    def __init__(self):
        factory = Factory_Operation();
        self.operation = factory.Get_Subtract();

    def handle(self, request:Subtract_Command):
        self.operation.operate(request.numer1, request.numer2);