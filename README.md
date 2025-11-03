# Flight Booking – Python OOP Project 2

We'll be implementing a mini flight booking system with python oop. Same with uber I've written tests already that you will have to pass.

---

## Phased Learning & Test Guide

| Phase                             | Test File                       | Concepts Covered                                                                   | Learning Goal                                              |
| --------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **1 – Core OOP**                  | `test_flight_basics.py`         | Classes, attributes, `@property`, dunder methods (`__eq__`, `__repr__`, `__str__`) | Learn class creation, encapsulation, basic object behavior |
|                                   | `test_passenger_basics.py`      | Classes, attributes, property setter/getter, dunder methods                        | Learn balance validation, object comparison                |
| **2 – Booking & System**          | `test_booking_basic.py`         | Composition, method interactions, exception handling                               | Implement booking/cancellation logic, handle errors        |
|                                   | `test_booking_system.py`        | Collections, manifests, revenue calculation                                        | Manage multiple flights and passengers                     |
| **3 – Decorators**                | `test_functional_decorators.py` | Functional decorators, stacking                                                    | Enforce business rules via decorators                      |
|                                   | `test_oop_decorators.py`        | `@staticmethod`, `@classmethod`, `@property`                                       | Apply decorators to class methods and attributes           |
| **4 – Dunder Methods & Advanced** | `test_dunder_methods.py`        | Sorting (`__lt__`), membership (`__contains__`), length (`__len__`)                | Advanced object behavior, collections interface            |
| **Optional**                      | `test_persistence.py`           | JSON persistence, save/load                                                        | Practice file I/O and object serialization                 |

---

## Core Classes

### Flight

Represents a flight with:

- `flight_number`
- `capacity`
- `price`
- `passengers` list

**Key Methods/Properties**:

- `available_seats` property
- `__eq__`, `__repr__`, `__str__`
- `__lt__`, `__contains__`, `__len__`

---

### Passenger

Represents a passenger with:

- `name`
- `passport_id`
- `balance`

**Key Methods/Properties**:

- Balance setter validates non-negative balance
- `__eq__`, `__repr__`, `__str__`

---

### BookingSystem

Manages flights and bookings:

- Add/find flights
- Book/cancel passengers
- Get passenger manifests
- Calculate total revenue

**Key Features**:

- Uses composition (flights + passengers)
- Implements class/staticmethods for system-wide actions

---

### Decorators

Functional decorators enforce rules:

- `@requires_balance` → ensures passenger has enough balance to book
- `@apply_discount` → applies VIP or off-peak discounts
- `@log_transaction` → logs bookings/cancellations

OOP decorators are also used:

- `@classmethod` → get flight by flight number
- `@staticmethod` → calculate discounted price
- `@property` → manage available seats and balance

---

## Learning Goals

By the end of this project you should be able to:

1. Learn encapsulation, properties, and dunder methods
2. Implement composition and system-level interactions
3. Understand decorators, both functional and OOP
4. Apply exception handling and business rules
5. Optionally practice persistence with JSON
6. Learn to write test-driven code

To check ur code
`python -m unittest tests/blah.py`

x0 O/
