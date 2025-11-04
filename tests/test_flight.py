import unittest
from flight import Flight
from passenger import Passenger
from exceptions import FlightFullError

class TestFlight(unittest.TestCase):
    """Tests for Flight: state, capacity, equality, and string output."""

    def test_create_flight(self):
        f = Flight("EK202", "Dubai", "New York", capacity=3)
        self.assertEqual(f.flight_number, "EK202")
        self.assertEqual(f.origin, "Dubai")
        self.assertEqual(f.destination, "New York")
        self.assertEqual(f.capacity, 3)
        self.assertEqual(len(f.booked_passengers), 0)

    def test_add_booking_until_full(self):
        f = Flight("EK203", "Nairobi", "Lagos", capacity=2)
        p1 = Passenger("Alice", "P001")
        p2 = Passenger("Bob", "P002")
        p3 = Passenger("Carol", "P003")
        f.add_booking(p1)
        f.add_booking(p2)
        self.assertTrue(f.is_full())
        with self.assertRaises(FlightFullError):
            f.add_booking(p3)

    def test_available_seats(self):
        f = Flight("EK204", "Joburg", "Cairo", capacity=2)
        self.assertEqual(f.available_seats, 2)
        p = Passenger("Dave", "P004")
        f.add_booking(p)
        self.assertEqual(f.available_seats, 1)

    def test_eq_same_flight_number(self):
        f1 = Flight("EK205", "A", "B", capacity=10)
        f2 = Flight("EK205", "C", "D", capacity=5)
        f3 = Flight("ZZ999", "A", "B", capacity=10)
        self.assertEqual(f1, f2)
        self.assertNotEqual(f1, f3)

    def test_str_representation(self):
        f = Flight("EK206", "X", "Y", capacity=2)
        s = str(f)
        self.assertIn("EK206", s)
        self.assertIn("Seats", s)
