import unittest
from flight import Flight
from passenger import Passenger
from booking import Booking

class TestBooking(unittest.TestCase):
    """Tests for Booking: confirm/cancel and state synchronization."""

    def test_confirm_booking_links_both(self):
        f = Flight("BK100", "A", "B", capacity=2)
        p = Passenger("Alice", "PX1")
        booking = Booking(p, f)
        booking.confirm()
        self.assertIn(p, f.booked_passengers)
        self.assertIn(f, p.bookings)
        self.assertEqual(booking.status, "Confirmed")

    def test_cancel_booking_unlinks_both(self):
        f = Flight("BK101", "A", "B", capacity=2)
        p = Passenger("Bob", "PX2")
        booking = Booking(p, f)
        booking.confirm()
        booking.cancel()
        self.assertNotIn(p, f.booked_passengers)
        self.assertNotIn(f, p.bookings)
        self.assertEqual(booking.status, "Cancelled")

    def test_double_confirm_prevention(self):
        f = Flight("BK102", "A", "B", capacity=2)
        p = Passenger("Carol", "PX3")
        booking = Booking(p, f)
        booking.confirm()
        try:
            booking.confirm()
        except Exception:
            pass
        self.assertEqual(p.bookings.count(f), 1)
        self.assertEqual(f.booked_passengers.count(p), 1)

    def test_str_booking(self):
        f = Flight("BK103", "A", "B", capacity=2)
        p = Passenger("Derek", "PX4")
        booking = Booking(p, f)
        booking.confirm()
        s = str(booking)
        self.assertIn("Derek", s)
        self.assertIn("BK103", s)
        self.assertIn("Confirmed", s)
