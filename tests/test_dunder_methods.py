import unittest
from flight_booking.flight import Flight
from flight_booking.passenger import Passenger

class TestDunderMethods(unittest.TestCase):

    def test_lt_sorting_flights(self):
        f1 = Flight("AB123", 2, 100)
        f2 = Flight("CD456", 2, 200)
        flights = [f2, f1]
        flights.sort()
        self.assertEqual(flights, [f1, f2])

    def test_contains_passenger_in_flight(self):
        f = Flight("AB123", 2, 100)
        p = Passenger("Nothando", "P123", 500)
        f.passengers.append(p)
        self.assertIn(p, f)

    def test_len_flight(self):
        f = Flight("AB123", 2, 100)
        self.assertEqual(len(f), 0)
        f.passengers.append("dummy")
        self.assertEqual(len(f), 1)
