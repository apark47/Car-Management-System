# testFile.py
from Car import Car
from CarInventory import CarInventory
from CarInventoryNode import CarInventoryNode


def test_car():
    a = Car("Ferrari", "Prius", 2001, 7000)
    b = Car("Tesla", "Portofino", 2004, 9000)    
    c = Car("Toyota", "Model3", 2010, 1100)
    c2 = Car("Toyota", "Model3", 2010, 1100)
    
    
    assert a.__str__() == "Make: FERRARI, Model: PRIUS, Year: 2001, Price: $7000"
    assert b.__str__() == "Make: TESLA, Model: PORTOFINO, Year: 2004, Price: $9000"    
    assert c.__str__() == "Make: TOYOTA, Model: MODEL3, Year: 2010, Price: $1100"

    assert (a < b) == True
    assert (c < b) == False
    assert (a < c) == True

    assert (b > a) == True
    assert (c > a) == True
    assert (a > c) == False

    
    assert (a == b) == False
    assert (b == c) == False
    assert (c == c2) == True


def test_carNode():

    car1 = Car("Ferrari", "Prius", 2001, 7000)
    car2 = Car("Tesla", "Portofino", 2004, 9000)
    car3 = Car("Toyota", "Model3", 2010, 1100)
    carNode = CarInventoryNode(car1)

    assert str(carNode) == \
"Make: FERRARI, Model: PRIUS, Year: 2001, Price: $7000\n"

    carNode.cars.append(car2)

    assert str(carNode) == \
"Make: FERRARI, Model: PRIUS, Year: 2001, Price: $7000\n\
Make: TESLA, Model: PORTOFINO, Year: 2004, Price: $9000\n"


    carNode.cars.append(car3)
    assert str(carNode) == \
"Make: FERRARI, Model: PRIUS, Year: 2001, Price: $7000\n\
Make: TESLA, Model: PORTOFINO, Year: 2004, Price: $9000\n\
Make: TOYOTA, Model: MODEL3, Year: 2010, Price: $1100\n"






def test_carInventory():

    bst = CarInventory()

    car1 = Car("Ferrari", "Prius", 2001, 7000)
    car2 = Car("Toyota", "Model3", 2010, 1100)
    car3 = Car("Tesla", "Portofino", 2004, 9000)
    car4 = Car("Tesla", "Sprinter", 2016, 20000)
    car5 = Car("Tesla", "Sprinter", 2021, 25000)


    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)



    assert bst.inOrder() == \
"""\
Make: FERRARI, Model: PRIUS, Year: 2001, Price: $7000
Make: TESLA, Model: PORTOFINO, Year: 2004, Price: $9000
Make: TESLA, Model: SPRINTER, Year: 2016, Price: $20000
Make: TESLA, Model: SPRINTER, Year: 2021, Price: $25000
Make: TOYOTA, Model: MODEL3, Year: 2010, Price: $1100
"""


    assert bst.preOrder() == \
"""\
Make: FERRARI, Model: PRIUS, Year: 2001, Price: $7000
Make: TOYOTA, Model: MODEL3, Year: 2010, Price: $1100
Make: TESLA, Model: PORTOFINO, Year: 2004, Price: $9000
Make: TESLA, Model: SPRINTER, Year: 2016, Price: $20000
Make: TESLA, Model: SPRINTER, Year: 2021, Price: $25000
"""

    assert bst.postOrder() == \
"""\
Make: TESLA, Model: SPRINTER, Year: 2016, Price: $20000
Make: TESLA, Model: SPRINTER, Year: 2021, Price: $25000
Make: TESLA, Model: PORTOFINO, Year: 2004, Price: $9000
Make: TOYOTA, Model: MODEL3, Year: 2010, Price: $1100
Make: FERRARI, Model: PRIUS, Year: 2001, Price: $7000
"""

    assert bst.getTotalInventoryPrice() == 62100




    assert bst.getBestCar("Ferrari", "Prius") == car1
    assert bst.getBestCar("TESLA", "Sprinter") == car5
    assert bst.getBestCar("Honda", "Odyssey") == None
    
    assert bst.getWorstCar("Ferrari", "Prius") == car1
    assert bst.getWorstCar("Tesla", "Sprinter") == car4
    assert bst.getBestCar("Toyota", "Corolla") == None

   



def test_doesCarExist():
    car1 = Car("Ferrari", "Prius", 2001, 7000)
    car2 = Car("Tesla", "Portofino", 2004, 9000)
    car3 = Car("Lexus", "Camry", 1994, 8000)
    car4 = Car("Ford", "Truck", 2000, 1200)

   

    bst = CarInventory()
    bst.addCar(car1)
    bst.addCar(car2)

    bst2 = CarInventory()
    bst2.addCar(car3)



    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car2) == True
    assert bst.doesCarExist(car3) == False
    assert bst.doesCarExist(Car("a", "b", 1, 2)) == False

    assert bst2.doesCarExist(car4) == False
    bst2.addCar(car4)
    assert bst2.doesCarExist(car4) == True


# ---------------------------------------------------------------

def test_successor():
    bst = CarInventory()
    
    car1 = Car("FORD", "A", 2001, 20000)
    car2 = Car("HONDA", "CIVIC", 2019, 30000)
    car3 = Car("TESLA", "A", 2017, 10000)
    car4 = Car("TESLA", "B", 2016, 40000)
    car5 = Car("TESLA", "C", 2015, 10000)
    car6 = Car("TESLA", "D", 2002, 87000)
    car7 = Car("TESLA", "E", 2009, 90000)
    car8 = Car("TESLA", "F", 2002, 40000)
    car9 = Car("TESLA", "G", 2001, 5000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    bst.addCar(car7)
    bst.addCar(car8)
    bst.addCar(car9)


    assert bst.inOrder() == \
"\
Make: FORD, Model: A, Year: 2001, Price: $20000\n\
Make: HONDA, Model: CIVIC, Year: 2019, Price: $30000\n\
Make: TESLA, Model: A, Year: 2017, Price: $10000\n\
Make: TESLA, Model: B, Year: 2016, Price: $40000\n\
Make: TESLA, Model: C, Year: 2015, Price: $10000\n\
Make: TESLA, Model: D, Year: 2002, Price: $87000\n\
Make: TESLA, Model: E, Year: 2009, Price: $90000\n\
Make: TESLA, Model: F, Year: 2002, Price: $40000\n\
Make: TESLA, Model: G, Year: 2001, Price: $5000\n"


    a = bst.getSuccessor("HONDA", "CIVIC") # has 2 children
    assert a.make == "TESLA"
    assert a.model == "A"

    b = bst.getSuccessor("TESLA", "G") # has left child, largest value, no successor
    assert b == None

    c = bst.getSuccessor("TESLA", "D") # this is the root
    assert c.make == "TESLA"
    assert c.model == "E"

    d = bst.getSuccessor("FORD", "A") # leaf that is a left child
    assert d.make == "HONDA"
    assert d.model == "CIVIC"

    e = bst.getSuccessor("TESLA", "F") # leaf that is a right child
    assert e.make == "TESLA"
    assert e.model == "G"

    f = bst.getSuccessor("TESLA", "A") # has a right child
    assert f.make == "TESLA"
    assert f.model == "B"



    

    bst.removeCar("HONDA", "CIVIC", 2019, 30000) 
    assert bst.inOrder() == \
"\
Make: FORD, Model: A, Year: 2001, Price: $20000\n\
Make: TESLA, Model: A, Year: 2017, Price: $10000\n\
Make: TESLA, Model: B, Year: 2016, Price: $40000\n\
Make: TESLA, Model: C, Year: 2015, Price: $10000\n\
Make: TESLA, Model: D, Year: 2002, Price: $87000\n\
Make: TESLA, Model: E, Year: 2009, Price: $90000\n\
Make: TESLA, Model: F, Year: 2002, Price: $40000\n\
Make: TESLA, Model: G, Year: 2001, Price: $5000\n"
    
    bst2 = CarInventory()
    bst2.addCar(car1)
    bst2.removeCar("FORD", "A", 2001, 20000)
    assert bst2.inOrder() == ""




    bst3 = CarInventory() 
    assert bst3.removeCar('t', 'c', 2006, 20000) == False
    bst3.addCar(Car('t', 'c', 2006, 20000))
    bst3.addCar(Car('a','b', 1, 2))
    bst3.addCar(Car('b', 'a', 2, 3))
    bst3.addCar(Car('a','a', 1, 2))
    bst3.addCar(Car('d', 'a', 1,2))

    g = bst3.getSuccessor('a', 'b')
    assert g.make == "B"
    assert g.model == "A"

    h = bst3.getSuccessor('b','a')
    assert h.make == "D"
    assert h.model == "A"




def test_remove():
    bst = CarInventory() 
    bst.addCar(Car('t', 'c', 2006, 20000))
    bst.addCar(Car('a','b', 1, 2))
    bst.addCar(Car('b', 'a', 2, 3))
    bst.addCar(Car('a','a', 1, 2))
    bst.addCar(Car('d', 'a', 1,2))


    assert bst.inOrder() == "\
Make: A, Model: A, Year: 1, Price: $2\n\
Make: A, Model: B, Year: 1, Price: $2\n\
Make: B, Model: A, Year: 2, Price: $3\n\
Make: D, Model: A, Year: 1, Price: $2\n\
Make: T, Model: C, Year: 2006, Price: $20000\n"
    
    bst.removeCar('A', 'B', 1, 2) # remove node with 2 children, successor is 2 levels below
    
    assert bst.inOrder() == "\
Make: A, Model: A, Year: 1, Price: $2\n\
Make: B, Model: A, Year: 2, Price: $3\n\
Make: D, Model: A, Year: 1, Price: $2\n\
Make: T, Model: C, Year: 2006, Price: $20000\n"


    bst.removeCar('t', 'c', 2006, 20000) # remove root w/ left child
    assert bst.inOrder() == "\
Make: A, Model: A, Year: 1, Price: $2\n\
Make: B, Model: A, Year: 2, Price: $3\n\
Make: D, Model: A, Year: 1, Price: $2\n"


    bst2 = CarInventory() # remove root where root is the only node
    bst2.addCar(Car('a', 'a', 0, 0))
    bst2.removeCar('a', 'a', 0, 0)
    assert bst2.inOrder() == ""


    bst3 = CarInventory() # remove root w/ right child
    bst3.addCar(Car('a', 'a', 0, 0))
    bst3.addCar(Car('b', 'b', 0, 0))
    bst3.removeCar('a', 'a', 0, 0)
    assert bst3.inOrder() == "Make: B, Model: B, Year: 0, Price: $0\n"


    bst4 = CarInventory() # remove node with a right child
    bst4.addCar(Car('a', 'a', 0, 0))
    bst4.addCar(Car('b', 'b', 0, 0))
    bst4.addCar(Car('c', 'c', 0, 0))
    bst4.removeCar('b', 'b', 0, 0)
    assert bst4.inOrder() == "\
Make: A, Model: A, Year: 0, Price: $0\n\
Make: C, Model: C, Year: 0, Price: $0\n"


    bst5 = CarInventory() # remove node with a left child
    bst5.addCar(Car('c', 'c', 0, 0))
    bst5.addCar(Car('b', 'b', 0, 0))
    bst5.addCar(Car('a', 'a', 0, 0))
    bst5.removeCar('b', 'b', 0, 0)
    assert bst5.inOrder() == "\
Make: A, Model: A, Year: 0, Price: $0\n\
Make: C, Model: C, Year: 0, Price: $0\n"



    bst6 = CarInventory() # remove node with two child, successor 1 level below
    bst6.addCar(Car('a', 'a', 0, 0))
    bst6.addCar(Car('b', 'b', 0, 0))
    bst6.addCar(Car('c', 'c', 0, 0))
    bst6.addCar(Car('a', 'b', 0, 0))

    bst6.removeCar('b', 'b', 0, 0)
    assert bst6.inOrder() == "\
Make: A, Model: A, Year: 0, Price: $0\n\
Make: A, Model: B, Year: 0, Price: $0\n\
Make: C, Model: C, Year: 0, Price: $0\n"
