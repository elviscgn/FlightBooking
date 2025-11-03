import unittest
from flight_booking.decorators import requires_balance, apply_discount, log_transaction
from flight_booking.passenger import Passenger
from flight_booking.flight import Flight

class TestFunctionalDecorators(unittest.TestCase):

    def test_requires_balance_blocks_booking(self):
        p = Passenger("Nothando", "P123", 50)
        flight = Flight("AB123", 2, 100)

        @requires_balance
        def book(f, passenger):
            f.passengers.append(passenger)

        with self.assertRaises(Exception):  # Student decides exact exception
            book(flight, p)

    def test_requires_balance_allows_booking(self):
        p = Passenger("Nothando", "P123", 200)
        flight = Flight("AB123", 2, 100)

        @requires_balance
        def book(f, passenger):
            f.passengers.append(passenger)
            passenger.balance -= f.price

        book(flight, p)
        self.assertIn(p, flight.passengers)
        self.assertEqual(p.balance, 100)

    def test_apply_discount_vip(self):
        p = Passenger("VIP Nothando", "P123", 200)
        flight = Flight("AB123", 2, 100)

        @apply_discount
        def price(f, passenger):
            return f.price

        discounted = price(flight, p)
        self.assertLess(discounted, flight.price)
