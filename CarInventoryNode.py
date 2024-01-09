# CarInventoryNode.py
from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.model = car.model.upper()
        self.make = car.make.upper()
        
        self.left = None
        self.right= None
        self.parent = None

        self.cars = [car]

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right
    
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


    def __str__(self):
        car_str = ""
        for i in self.cars:
            car_str += str(i) + "\n"

        return car_str

    def findMin(self):
        current = self
        while current.getLeft() != None:
            current = current.getLeft()
        return current
    



    def spliceOut(self, make, model):
        if self.parent == None:
            return None
        
        # currNode is a leaf
        if self.left == None and self.right == None:
            if self.parent.left == self:
                   self.parent.left = None
            else:
                   self.parent.right = None

        # currNode is not a leaf node, should only have a right tree      
        else:

            if self.right != None and self.parent != None:
                   if self.parent.left == self:
                      self.parent.left = self.right
                   else:
                      self.parent.right = self.right
                   self.right.parent = self.parent
            else:
                   if self.parent.left == self:
                      self.parent.left = self.right
                   else:
                      self.parent.right = self.right
                   self.right.parent = self.parent


