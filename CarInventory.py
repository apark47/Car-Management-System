# CarInventory.py
from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None

    def _addCar(self, new_node, curr_node):
        if new_node.make < curr_node.make: # left subtree
            if curr_node.left != None:
                self._addCar(new_node, curr_node.left)
            else:
                temp_node = CarInventoryNode(new_node)
                curr_node.left = temp_node
                temp_node.parent = curr_node

                
        
        if new_node.make > curr_node.make: # right subtree
            if curr_node.right != None:
                self._addCar(new_node, curr_node.right)
            else:
                temp_node = CarInventoryNode(new_node)
                curr_node.right = temp_node
                temp_node.parent = curr_node


        if new_node.model < curr_node.model and new_node.make == curr_node.make: # left subtree, if makes are equal
            if curr_node.left != None:
                self._addCar(new_node, curr_node.left)
            else:
                temp_node = CarInventoryNode(new_node)
                curr_node.left = temp_node
                temp_node.parent = curr_node
                
        if new_node.model > curr_node.model and new_node.make == curr_node.make: # right subtree, if makes are equal
            if curr_node.right != None:
                self._addCar(new_node, curr_node.right)
            else:
                temp_node = CarInventoryNode(new_node)
                curr_node.right = temp_node
                temp_node.parent = curr_node
                
        if new_node.model == curr_node.model and new_node.make == curr_node.make: # if makes and models are equal
            curr_node.cars.append(new_node)
            


    def addCar(self, car): # similar to put()
        if self.root:
            self._addCar(car, self.root)
        else:
            self.root = CarInventoryNode(car)

        
    def _preOrder(self, node):
        ret = ""
        if node != None:
            ret += str(node) # visits node
            ret += self._preOrder(node.getLeft())
            ret += self._preOrder(node.getRight())

        return ret
  

    def preOrder(self):
        if self.root:
            return self._preOrder(self.root)
        else:
            return ""
        
    def _inOrder(self, node):
        ret = ""
        if node != None:
            ret += self._inOrder(node.getLeft())
            ret += str(node)
            ret += self._inOrder(node.getRight())

        return ret

    def inOrder(self):
        if self.root:
            return self._inOrder(self.root)
        else:
            return ""

    def _postOrder(self, node):
        ret = ""
        if node != None:
            ret += self._postOrder(node.getLeft())
            ret += self._postOrder(node.getRight())
            ret += str(node)

        return ret

    def postOrder(self):
        if self.root:
            return self._postOrder(self.root)
        else:
            return ""
        
    def doesCarExist(self, car):
        if car:
            currentNode = self._doesCarExist(car.make.upper(), car.model.upper(), self.root)
            if currentNode:
                for i in currentNode.cars:
                    if i == car:
                        return True

        return False

    def _doesCarExist(self, make, model, carNode = None):
        if not carNode:
            return None
        
        elif make.upper() == carNode.make and model.upper() == carNode.model:
            return carNode
        
        elif make.upper() < carNode.make or (make.upper() == carNode.make and model.upper() < carNode.model):
            return self._doesCarExist(make, model, carNode.getLeft())
        
        else:
            return self._doesCarExist(make, model, carNode.getRight())


    def getBestCar(self, make, model):
        return self._getBestCar(make, model, self.root)
         
    
    def _getBestCar(self, make, model, carNode):
        if not carNode:
            return None

        elif make.upper() == carNode.make and model.upper() == carNode.model:
            best = carNode.cars[0]

            for i in carNode.cars:
                if i > best:
                    best = i

            return best

        elif carNode.make > make.upper():
            return self._getBestCar(make, model, carNode.left)

        elif carNode.make < make.upper():
            return self._getBestCar(make, model, carNode.right)

        elif carNode.make == make.upper() and carNode.model > model.upper():
            return self._getBestCar(make, model, carNode.left)

        elif carNode.make == make.upper() and carNode.model < model.upper():
            return self._getBestCar(make, model, carNode.right)
        
       
    def getWorstCar(self, make, model):
        return self._getWorstCar(make, model, self.root)

    def _getWorstCar(self, make, model, carNode):
        if not carNode:
            return None

        elif make.upper() == carNode.make and model.upper() == carNode.model:
            worst = carNode.cars[0]

            for i in carNode.cars:
                if i < worst:
                    worst = i

            return worst

        elif carNode.make > make.upper():
            return self._getWorstCar(make, model, carNode.left)

        elif carNode.make < make.upper():
            return self._getWorstCar(make, model, carNode.right)

        elif carNode.make == make.upper() and carNode.model > model.upper():
            return self._getWorstCar(make, model, carNode.left)

        elif carNode.make == make.upper() and carNode.model < model.upper():
            return self._getWorstCar(make, model, carNode.right)


    def _getTotalInventoryPrice(self, node):
        total = 0
      
        if node != None:            
            for i in node.cars:
                total += i.price
            total += self._getTotalInventoryPrice(node.getLeft())
            total += self._getTotalInventoryPrice(node.getRight())

        return total

    
    def getTotalInventoryPrice(self): # similar to traversals
        if self.root:
            return self._getTotalInventoryPrice(self.root)
        else:
            return 0





    
    def getSuccessor(self, make, model):
        # create the car based on make and model
        # get the car node from the inventory
        # check if the node exists, if not return None
        # check if  node has right child -> go as far left as possible
        # check if node has parrent and go far up enough that you find the parent that is bigger than your node and return node
        # or reach the root and return None
        
        car = Car(make, model, 0, 0)
        
        retrieved_car_node = self._doesCarExist(make, model, self.root)

        if retrieved_car_node != None: # if the car exists, try to find the successor
            
            succ = None

            # Case 2: Node has a right child and successor is in right subtree as far left as possible
            if retrieved_car_node.getRight() != None:
                succ = retrieved_car_node.right.findMin()
                return succ
             
            # Case 3: Node doesn't have a right child, successor is higher up in the tree in one of the parents
            #         (first parent we see that is larger than our node)
            else:
            
                while retrieved_car_node.parent != None and (retrieved_car_node.parent.make < retrieved_car_node.make or (retrieved_car_node.parent.make == retrieved_car_node.make and retrieved_car_node.parent.model < retrieved_car_node.model)):
                    retrieved_car_node = retrieved_car_node.parent
                succ = retrieved_car_node.parent
                return succ
                
        return None

        

    def removeCar(self, make, model, year, price):
        car = Car(make, model, year, price)
        currentNode = self._doesCarExist(make, model, self.root)

        if self.root == None:
            return False
        
        if self.root != None:
            if currentNode == None:
                return False
     
            if currentNode != None: # removes the car from the list
                for index, i in enumerate(currentNode.cars):
                    if i == car:
                        currentNode.cars.pop(index)

                
            if len(currentNode.cars) == 0: # if list is empty after removing car, we remove the node from the BST
                    
                # Case 1: node to remove is a leaf
                if (currentNode.left == None and currentNode.right == None):
                    if currentNode.parent != None:
                        if currentNode == currentNode.parent.left: # currentNode is the left child
                            currentNode.parent.left = None
                        else: # currentNode is the right child
                            currentNode.parent.right = None
                    else: # when currentNode is the root
                        self.root = None
                        currentNode = None    

                    
                # Case 2: node to remove has two children:
                elif currentNode.getLeft() != None and currentNode.getRight() != None:
                     # Need to find the successor, remove successor, and replace
                     # currentNode with successor's data/payload
                    succ = self.getSuccessor(make, model)
                    succ.spliceOut(make, model) # removes it from BST
                    currentNode.cars = succ.cars # replaces currentNode with successor's data/payload
                    currentNode.make = succ.make
                    currentNode.model = succ.model


                # Case 3: node to remove has one child:
                else:

                    # if the node has a left child
                    if currentNode.getLeft() != None:
                        if currentNode.parent != None:
                            if currentNode.parent.left == currentNode: # if the node is a left child
                                currentNode.left.parent = currentNode.parent
                                currentNode.parent.left = currentNode.left

                            elif currentNode.parent.right == currentNode:
                                currentNode.left.parent = currentNode.parent
                                currentNode.parent.right = currentNode.left

                        else: # currentNode is the root
                            self.root = currentNode.left
                            self.root.parent = None
                                
                    # if the node has a right child
                    else:
                        if currentNode.parent != None:
                            if currentNode.parent.left == currentNode: # if the node is a left child
                                currentNode.right.parent = currentNode.parent
                                currentNode.parent.left = currentNode.right

                            elif currentNode.parent.right == currentNode:
                                currentNode.right.parent = currentNode.parent
                                currentNode.parent.right = currentNode.right

                        else: # currentNode is the root
                            self.root = currentNode.right
                            self.root.parent = None
        return True
