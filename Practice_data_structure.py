##question one
class Queue:    
        def __init__(self):
            self.List = []
        def enqueue(self):
            try:
                Adding = input("Enter the queue here: ")
            except ValueError:
                print("This is not the right input")

            self.List.append(Adding)
            print("Added person:", Adding)
            return self.List        
        def dequeue(self):
            if len(self.List)==0:
                print("No item to remove.")  
                return None          
            Remove = input("Leave the queue from here: ")
            if Remove in self.List:
                self.List.remove(Remove)
                print(f"This is what we are removing: {Remove}")
                return self.List
            else:
                print("Nothing to remove")
            return self.List       
        def peek(self):
            if len(self.List)==0:
                print("No items to see here")
                return None
            print("First item:", self.List[0])
            return self.List[0]        
        def empty(self):
            if len(self.List) == 0:
                print("There is nothing to see here.Try adding tasks to the queue.")
            else:
                print("Items:" ,self.List)          
        def view(self):
            if len(self.List) ==0:
                print("The queue is empty.")
            else:
                print("This is the queue:", self.List)            
  
#part (b)
class Stack:
    def __init__(self):
         self.pile = []
    def push(self):
        add = input("Please enter the stack here: ")
        self.pile.append(add)
        print("Addeded: ", add)
        return self.pile
    def pop(self):
        if len(self.pile) == 0:
            print("There is nothing to remove")
            return None
        else:
           self.pile.remove[0]
           print("The removed item: ", self.pile.pop[0]) 
    def peek(self):
        if len(self.pile) == 0:
            print("There is nothing to see here.")
            return None
        else:
            self.pile[-1]
            print("First item: ", self.pile[-1])
            return 
    def view(self):
        if len(self.pile)==0:
            print("nothing here")
        else:
            return self.pile
    def empty(self):
        if len(self.pile) ==0:
            return self.pile
        else:
            return False
print("\n Main Table")
while True:
    try:
        print("\n 1. Queue \n 2. Stacks")
        DTP = int(input("Which DataType do you want to use: "))
    except ValueError:
        print("Enter right value!")
    if DTP == 1:
        call = Queue()
        while True:        
            print("\n 1. Add item\n 2. Remove item\n 3. Take a peek\n 4.Check whether empty\n 5.Exit")
            SELECTION = int(input("Make your queue selection here: "))
            if SELECTION == 1:
                call.enqueue()
            elif SELECTION ==2:
                call.dequeue()
            elif SELECTION == 3:
                call.peek()
            elif SELECTION == 4:
                call.empty()
            elif SELECTION == 6:
                call.view()
            elif SELECTION == 5:
                print("Exiting queue")
                break
            else:
                print("Not valid entry.")
    elif DTP ==2:
        stack_call = Stack()
        while True:
            print("\n 1. Push an item\n 2. Pop item\n 3. Take a peek\n 4.Check whether empty\n 5.View Stack \n 6.EXIT")
            SELECTION = int(input("Make your queue selection here: "))
            if SELECTION == 1:
                stack_call.push()
            elif SELECTION ==2:
                stack_call.pop()
            elif SELECTION == 3:
                stack_call.peek()
            elif SELECTION == 4:
                stack_call.empty()
            elif SELECTION == 5:
                stack_call.view()
            elif SELECTION == 6:
                print("Exiting queue. . . . ")
                break
    else:
        print("Not valid entry.")





