from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.engine_components = []

    def add_engine_component(self, component):
        self.engine_components.append(component)

    def needs_service(self):
        for component in self.engine_components:
            if component.needs_service():
                return True
        return False


class EngineComponent(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
