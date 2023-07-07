import unittest
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = CapuletEngine(last_service_date=datetime(2022, 1, 1), current_mileage=40000, last_service_mileage=20000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine(last_service_date=datetime(2023, 1, 1), current_mileage=40000, last_service_mileage=30000)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = SternmanEngine(last_service_date=datetime(2022, 1, 1), warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = SternmanEngine(last_service_date=datetime(2023, 1, 1), warning_light_is_on=False)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(last_service_date=datetime(2022, 1, 1), current_mileage=80000, last_service_mileage=50000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(last_service_date=datetime(2023, 1, 1), current_mileage=80000, last_service_mileage=70000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
