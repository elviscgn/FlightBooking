import unittest
from passenger import Passenger

class TestPassengerBasics(unittest.TestCase):

    def test_create_passenger(self):
        p = Passenger("Nothando", "P123", 500)
        self.assertEqual(p.name, "Nothando")
        self.assertEqual(p.passport_id, "P123")
        self.assertEqual(p.balance, 500)

    def test_passenger_repr_str(self):
        p = Passenger("Nothando", "P123", 500)
        self.assertIn("Nothando", repr(p))
        self.assertIn("P123", str(p))

    def test_passenger_eq(self):
        p1 = Passenger("Nothando", "P123", 500)
        p2 = Passenger("Paris", "P123", 300)
        p3 = Passenger("Nothando", "P456", 500)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_passenger_balance_setter(self):
        p = Passenger("Nothando", "P123", 500)
        p.balance = 300
        self.assertEqual(p.balance, 300)
        # Should raise if negative balance (student implements)
        with self.assertRaises(ValueError):
            p.balance = -50
