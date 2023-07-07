import unittest
from datetime import datetime
from engine.battery import NubbinBattery, SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        battery = NubbinBattery(last_service_date=datetime(2022, 1, 1))
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        battery = NubbinBattery(last_service_date=datetime(2023, 1, 1))
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        battery = SpindlerBattery(last_service_date=datetime(2022, 1, 1))
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        battery = SpindlerBattery(last_service_date=datetime(2023, 1, 1))
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
