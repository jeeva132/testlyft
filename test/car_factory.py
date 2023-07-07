class SpindlerBattery:
    def __init__(self, manufacture_year):
        self.manufacture_year = manufacture_year

    def requires_service(self, current_year):
        years_passed = current_year - self.manufacture_year
        return years_passed >= 3


class CarFactory:
    @staticmethod
    def service_carrigan_tires(tire_wear):
        return any(wear >= 0.9 for wear in tire_wear)

    @staticmethod
    def service_octoprime_tires(tire_wear):
        return sum(tire_wear) >= 3

import unittest

class TestCarFactory(unittest.TestCase):
    def test_spindler_battery_service(self):
        battery = SpindlerBattery(manufacture_year=2020)
        self.assertFalse(battery.requires_service(current_year=2022))
        self.assertTrue(battery.requires_service(current_year=2023))

    def test_carrigan_tire_service(self):
        self.assertTrue(CarFactory.service_carrigan_tires([0.5, 0.9, 0.7, 0.8]))
        self.assertFalse(CarFactory.service_carrigan_tires([0.5, 0.8, 0.7, 0.8]))

    def test_octoprime_tire_service(self):
        self.assertTrue(CarFactory.service_octoprime_tires([0.8, 0.9, 0.6, 0.7]))
        self.assertFalse(CarFactory.service_octoprime_tires([0.8, 0.8, 0.7, 0.7]))

if __name__ == '__main__':
    unittest.main()
