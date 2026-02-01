import sys
import os

from mediatr import Mediator
from Addition.Addition_command import Addition_command
from Addition.Use_Case_Add import Use_Case_Add

if __name__ == "__main__":
    
    root_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(root_path)

    mediator = Mediator()

    command = Addition_command(numer1=2, numer2=4);    
    mediator.send(command)