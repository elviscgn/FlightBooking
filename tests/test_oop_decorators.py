import unittest
from flight_booking.booking_system import BookingSystem
from flight_booking.flight import Flight

class TestOOPDecorators(unittest.TestCase):

    def test_classmethod_get_flight_by_number(self):
        f1 = Flight("AB123", 2, 100)
        f2 = Flight("CD456", 2, 200)
        system = BookingSystem()
        system.add_flight(f1)
        system.add_flight(f2)

        flight = BookingSystem.get_flight_by_number(system, "AB123")
        self.assertEqual(flight, f1)

    def test_staticmethod_calculate_discounted_price(self):
        flight = Flight("AB123", 2, 100)
        discounted = BookingSystem.calculate_discounted_price(flight.price, 0.1)
        self.assertEqual(discounted, 90)

    def test_property_available_seats(self):
        flight = Flight("AB123", 2, 100)
        self.assertEqual(flight.available_seats, 2)
        flight.passengers.append("dummy")
        self.assertEqual(flight.available_seats, 1)
