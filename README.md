# ✈️ Flight Booking System

## 🧱 Overview

This project simulates the core logic of an airline booking app.  
Users can:
- Create flights  
- Register passengers  
- Make and cancel bookings  
- Handle edge cases like overbooked flights and duplicate reservations  

The catch: 🧩 **You start with failing tests.**  
Your job is to implement the code to make them pass — learning **clean OOP**, **Python magic methods**, and **TDD** in the process.

---

## 🎯 Learning Objectives

By completing this project, you’ll understand and apply **nearly every major Python concept**:

| Concept | Where You’ll See It |
|----------|--------------------|
| **Classes & Objects** | Every major entity (Flight, Passenger, Booking, BookingSystem) |
| **Encapsulation** | Private attributes and getters/setters for internal state |
| **Inheritance & Composition** | BookingSystem manages Flights and Passengers as composed objects |
| **Dunder Methods (`__eq__`, `__str__`, `__repr__`)** | For comparing, printing, and debugging classes |
| **Class & Static Methods** | Used for object creation or validation logic |
| **OOP Decorators (`@property`, `@classmethod`, `@staticmethod`)** | To manage computed attributes and alternate constructors |
| **Custom Exceptions** | To handle invalid bookings or overcapacity gracefully |
| **Unit Testing (`unittest`)** | To verify behavior and prevent regressions |
| **TDD (Test-Driven Development)** | Write code only to make tests pass |
| **Type Hints** | For cleaner, modern Python |
| **Equality and Hashing (`__eq__`, `__hash__`)** | To make passengers or flights comparable and usable in sets/dicts |
| **Docstrings and Clean Code** | To document each class and function professionally |

By the end, you’ll basically know how to architect a mini system like **Uber, Expedia, or Airbnb** in pure Python.

---

## 🧩 Core Components

### 🛫 `Flight`
Represents a flight that passengers can book.

**Attributes**
- `flight_number` — unique string (e.g., `"EK202"`)
- `origin`, `destination` — where the flight goes
- `capacity` — total seats available
- `_booked_passengers` — internal list of passengers (encapsulated)

**Key Methods**
- `add_booking(passenger)` — adds a passenger if not full  
- `is_full()` — returns `True` when no seats left  
- `available_seats()` — calculates seats dynamically  
- `__eq__()` — compares two flights by flight number  
- `__str__()` — readable output like `"Flight EK202: Dubai → New York (Seats left: 2)"`

---

### 🧍 `Passenger`
Represents a person who can book flights.

**Attributes**
- `name`
- `passport_number`
- `_bookings` — list of `Booking` objects linked to this passenger

**Key Methods**
- `add_booking(flight)` — adds a flight to passenger’s list  
- `cancel_booking(flight)` — removes a flight if exists  
- `__eq__()` — passengers compared by passport number  
- `__repr__()` — for debugging  
- `@property` — computed properties like total flights booked  

---

### 📦 `Booking`
Represents a connection between a `Passenger` and a `Flight`.

**Attributes**
- `passenger`
- `flight`
- `status` — e.g. `"Confirmed"` or `"Cancelled"`

**Key Methods**
- `confirm()` — links both sides (adds passenger to flight, flight to passenger)
- `cancel()` — rolls back the link  
- `__str__()` — `"Alice booked EK202 (Confirmed)"`

---

### 🧠 `BookingSystem`
Central brain coordinating everything.

**Attributes**
- `flights` — dictionary `{flight_number: Flight}`
- `passengers` — dictionary `{passport_number: Passenger}`
- `bookings` — list of all active bookings

**Key Methods**
- `add_flight(...)`
- `register_passenger(...)`
- `make_booking(flight_number, passport_number)`
- `cancel_booking(flight_number, passport_number)`
- `find_passenger(passport_number)` and `find_flight(flight_number)`
- `__len__()` — total bookings in system  
- `__iter__()` — iterate through all bookings easily  

---

## 🧪 Tests

This project is **TDD-based**. You’ll begin with failing tests in `/tests/`.

To run:
```bash
python3 -m unittest discover -s tests
