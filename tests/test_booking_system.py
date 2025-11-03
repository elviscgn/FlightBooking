import unittest
from flight_booking.booking_system import BookingSystem
from flight_booking.flight import Flight
from flight_booking.passenger import Passenger

class TestBookingSystem(unittest.TestCase):

    def setUp(self):
        self.system = BookingSystem()
        self.flight1 = Flight("AB123", 2, 100)
        self.flight2 = Flight("CD456", 3, 200)
        self.passenger = Passenger("Nothando", "P123", 500)
        self.system.add_flight(self.flight1)
        self.system.add_flight(self.flight2)

    def test_add_find_flight(self):
        found = self.system.find_flight("AB123")
        self.assertEqual(found, self.flight1)

    def test_get_passenger_manifest(self):
        self.system.book("AB123", self.passenger)
        manifest = self.system.get_passenger_manifest("AB123")
        self.assertIn(self.passenger, manifest)

    def test_system_total_revenue(self):
        self.system.book("AB123", self.passenger)
        self.system.book("CD456", Passenger("Paris", "P456", 500))
        total = self.system.total_revenue()
        self.assertEqual(total, self.flight1.price + self.flight2.price)



# BookingSystem
# -> 