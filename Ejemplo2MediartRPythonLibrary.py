#pip install mediatr
import asyncio
from mediatr import Mediator


class GetArrayQuery():
    def __init__(self,items_count:int):
        self.items_count = items_count

class SumNumsQuery():
    def __init__(self,num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2

@Mediator.handler
class GetArrayQueryHandler():
    def handle(self,request:GetArrayQuery):
        items = list()
        for i in range(0, request.items_count):
            items.append(i)
        return items
    
@Mediator.handler
class SumNumsQueryHandler():
    def handle(self,request:SumNumsQuery):
        return request.num1 + request.num2
    
# or just Mediator.register_handler(get_array_handler)

mediator = Mediator()

request = GetArrayQuery(5)
result =  mediator.send(request)
print(result)

request2 = SumNumsQuery(2,2)
result =  mediator.send(request2)

print("resultado suma 2 nums ", result)
