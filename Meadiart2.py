from abc import ABC, abstractmethod
from mediatr import Mediator 

class AbsCita(ABC):
    @abstractmethod
    def agendar_cita(self):
        pass
    
# La "Petición" es un objeto simple de datos
class AgendarCitaRequest:
    def __init__(self, cita: AbsCita):
        self.cita = cita

class CitaMedica(AbsCita):

    def agendar_cita(self):
        print("Cita médica agendada exitosamente.")

class CitaDientes(AbsCita):
    def agendar_cita(self):
        print("Cita dientes agendada")

@Mediator.handler
class CasoDeUsoAgendarCita:
    # El handler ahora depende de la petición, pero procesa la abstracción
    def handle(self, request: AgendarCitaRequest):
        request.cita.agendar_cita()

if __name__ == "__main__":
    mediator = Mediator()

    # Puedes pasar cualquier cosa que herede de AbsCita
    nueva_cita = CitaMedica()
    cita_dientes = CitaDientes()

    peticion = AgendarCitaRequest(nueva_cita)
    peticion_cita_dientes = AgendarCitaRequest(cita_dientes)
    
    mediator.send(peticion)
    mediator.send(peticion_cita_dientes)