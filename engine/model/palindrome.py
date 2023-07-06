from datetime import datetime
from car import Car
from sternman_engine import SternmanEngine


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.add_engine_component(SternmanEngine(last_service_date, warning_light_is_on))

    def needs_service(self):
        return super().needs_service() or self.engine_components[0].needs_service()
