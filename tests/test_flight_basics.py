import unittest
from flight import Flight

class TestFlightBasics(unittest.TestCase):

    def test_create_flight(self):
        flight = Flight("AB123", 100, 150)
        self.assertEqual(flight.flight_number, "AB123")
        self.assertEqual(flight.capacity, 100)
        self.assertEqual(flight.price, 150)
        self.assertEqual(flight.passengers, [])

    def test_available_seats(self):
        flight = Flight("AB123", 2, 150)
        self.assertEqual(flight.available_seats, 2)
        # After booking dummy passenger
        flight.passengers.append("dummy")
        self.assertEqual(flight.available_seats, 1)

    def test_flight_repr_str(self):
        flight = Flight("AB123", 100, 150)
        self.assertIn("AB123", repr(flight))
        self.assertIn("AB123", str(flight))

    def test_flight_eq(self):
        flight1 = Flight("AB123", 100, 150)
        flight2 = Flight("AB123", 50, 100)
        flight3 = Flight("CD456", 100, 150)
        self.assertEqual(flight1, flight2)
        self.assertNotEqual(flight1, flight3)
