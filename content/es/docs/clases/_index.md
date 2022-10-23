---
title: "Clases"
date: 2022-10-16T21:07:31+02:00
linkTitle: "Clases"
weight: 60
date: 2021-09-15
description: >
  Clases en py
draft: false
docs: >
   https://aviadr1.github.io/learn-advanced-python/11_db_access/exercise/basic_db_access-solutions.html
   https://datacarpentry.org/python-ecology-lesson/
   
---

{{% pageinfo %}}
### Objetivos:
* Creación de objetos con clases definidas por el usuario
  
Tienes este documento como un [notebook](Introducción_a_las_clases.ipynb) si quieres practicar con él (*usa guardar como en el enlace para descargarlo*).
{{% /pageinfo %}}




## What are classes?
Classes are the foundation of object-oriented
programming. Classes represent real-world things
you want to model in your programs: for example
dogs, cars, and robots. You use a class to make
objects, which are specific instances of dogs, cars,
and robots. A class defines the general behavior that
a whole category of objects can have, and the
information that can be associated with those objects.
Classes can inherit from each other – you can
write a class that extends the functionality of an
existing class. This allows you to code efficiently for a
wide variety of situations.

## Creating a class
Consider how we might model a car. What information
would we associate with a car, and what behavior would it
have? The information is stored in variables called
attributes, and the behavior is represented by functions.
Functions that are part of a class are called methods.

**The Car class**
```python
class Car:
"""A simple attempt to model a car."""
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0
    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")
```    

## Using a class

```python

# Creating an object from a class
my_car = Car('audi', 'a4', 2016)

# Accessing attribute values

print(my_car.make)
print(my_car.model)
print(my_car.year)

# Calling methods

my_car.fill_tank()
my_car.drive()

# Creating multiple objects

my_car = Car('audi', 'a4', 2019)
my_old_car = Car('subaru', 'outback', 2015)
my_truck = Car('toyota', 'tacoma', 2012)
```

## Modifying attributes

You can modify an attribute's value directly, or you can
write methods that manage updating values more carefully.
 
```python
my_new_car = Car('audi', 'a4', 2019)

# Modifying an attribute directly
my_new_car.fuel_level = 5

# Writing a method to update an attribute's value
def update_fuel_level(self, new_level):
    """Update the fuel level."""
    if new_level <= self.fuel_capacity:
        self.fuel_level = new_level
    else:
        print("The tank can't hold that much!")

# Writing a method to increment an attribute's value
def add_fuel(self, amount):
    """Add fuel to the tank."""
    if (self.fuel_level + amount <= self.fuel_capacity):
        self.fuel_level += amount
        print("Added fuel.")
    else:
        print("The tank won't hold that much.")
```

## Naming conventions

In Python class names are written in CamelCase and object
names are written in lowercase with underscores. Modules
that contain classes should be named in lowercase with
underscores.

## Class inheritance

If the class you're writing is a specialized version of another
class, you can use inheritance. When one class inherits
from another, it automatically takes on all the attributes and
methods of the parent class. The child class is free to
introduce new attributes and methods, and override
attributes and methods of the parent class.
To inherit from another class include the name of the
parent class in parentheses when defining the new class.

```python
# The __init__() method for a child class

class ElectricCar(Car):
    """A simple model of an electric car."""
    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)
        # Attributes specific to electric cars.
        # Battery capacity in kWh.
        self.battery_size = 75
        # Charge level in %.
        self.charge_level = 0

        # Nuevo método de la clase hija
        def charge(self):
            """Fully charge the vehicle."""
            self.charge_level = 100
            print("The vehicle is fully charged.")

# Using child methods and parent methods
my_ecar = ElectricCar('tesla', 'model s', 2019)
my_ecar.charge()
my_ecar.drive()

```

### Sobreescribiendo métodos de la clase madre
  
```python

class ElectricCar(Car):
  --snip--
  def fill_tank(self):
      """Display an error message."""
      print("This car has no fuel tank!")
```


## Instances as attributes

A class can have objects as attributes. This allows classes
to work together to model complex situations.

```python
# A Battery class
class Battery:
    """A battery for an electric car."""
    def __init__(self, size=75):
        """Initialize battery attributes."""
        # Capacity in kWh, charge level in %.
        self.size = size
        self.charge_level = 0
    def get_range(self):
        """Return the battery's range."""
        if self.size == 75:
            return 260
        elif self.size == 100:
            return 315
  
# Using an instance as an attribute
# Modifica el ElectricCar
class ElectricCar(Car):
  --snip--
    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)
        # Attribute specific to electric cars.
        self.battery = Battery()
    def charge(self):
        """Fully charge the vehicle."""
        self.battery.charge_level = 100
        print("The vehicle is fully charged.")

# Using the instance
my_ecar = ElectricCar('tesla', 'model x', 2019)
my_ecar.charge()
print(my_ecar.battery.get_range())
my_ecar.drive()
```

## Understanding self
People often ask what the self variable represents. The
self variable is a reference to an object that's been
created from the class.

The self variable provides a way to make other variables
and objects available everywhere in a class. The self
variable is automatically passed to each method that's
called through an object, which is why you see it listed first
in every method definition. Any variable attached to self is
available everywhere in the class.

## Understanding `__init__()`
The __init__() method is a function that's part of a class,
just like any other method. The only special thing about
__init__() is that it's called automatically every time you
make a new object from a class. If you accidentally misspell
__init__(), the method will not be called and your object
may not be created correctly.