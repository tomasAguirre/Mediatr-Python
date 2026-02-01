from Factory.Factory_Operation import Factory_Operation
from mediatr import Mediator
from Addition.Addition_command import Addition_command

@Mediator.handler
class Use_Case_Add():
    def __init__(self):
        factory = Factory_Operation();
        self.operation = factory.Get_Add();
    
    # El handler ahora depende de la petición, pero procesa la abstracción
    def handle(self, request: Addition_command):
        self.operation.operate(request.numer1, request.numer2)