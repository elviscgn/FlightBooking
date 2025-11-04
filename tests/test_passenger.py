import unittest
from passenger import Passenger
from flight import Flight

class TestPassenger(unittest.TestCase):
    """Tests for Passenger: creation, booking list, equality, and properties."""

    def test_create_passenger(self):
        p = Passenger("Elvis", "P12345")
        self.assertEqual(p.name, "Elvis")
        self.assertEqual(p.passport_number, "P12345")
        self.assertEqual(len(p.bookings), 0)

    def test_add_and_cancel_booking(self):
        p = Passenger("Paris", "P54321")
        f = Flight("FL100", "CityA", "CityB", capacity=2)
        p.add_booking(f)
        self.assertIn(f, p.bookings)
        p.cancel_booking(f)
        self.assertNotIn(f, p.bookings)

    def test_eq_same_passport(self):
        # Passengers with the same password shld be treated as same irregardless of Name
        p1 = Passenger("Nothando", "P111")
        p2 = Passenger("Different", "P111")
        p3 = Passenger("Nothando", "P222")
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_property_total_bookings(self):
        p = Passenger("Paris", "P777")
        f1 = Flight("FL101", "A", "B", capacity=1)
        f2 = Flight("FL102", "C", "D", capacity=1)
        p.add_booking(f1)
        p.add_booking(f2)
        self.assertEqual(p.total_bookings, 2)

    def test_repr_for_debug(self):
        p = Passenger("Elvis", "P999")
        r = repr(p)
        self.assertIn("Elvis", r)
        self.assertIn("P999", r)
