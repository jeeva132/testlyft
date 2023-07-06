from datetime import datetime
from car import Car
from willoughby_engine import WilloughbyEngine


class Glissade(Car):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.add_engine_component(WilloughbyEngine(last_service_date, 0, 0))

    def needs_service(self):
        return super().needs_service() or datetime.today().date().year - self.last_service_date.year >= 3
