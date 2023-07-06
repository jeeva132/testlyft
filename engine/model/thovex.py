from datetime import datetime
from car import Car
from willoughby_engine import WilloughbyEngine


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.add_engine_component(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage))

    def needs_service(self):
        return super().needs_service() or self.engine_components[0].needs_service()
