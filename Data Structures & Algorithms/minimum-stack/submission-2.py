class MinStack:

    def __init__(self):
        self.stack = []
        # pushes a new minimum element onto this stack when a new minimum element is initialized
        # note the top of the stack contains the current minimum element. 
        self.min_stack = [] 

    def push(self, val: int) -> None:
        # first adds element to unordered stack
        self.stack.append(val)
        # push the current minimum element onto min_stack (after pushing some elt onto the stack)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val)) 
        else:
            self.min_stack.append(val)

        return None

    def pop(self) -> None:
        val_popped = self.stack.pop()
        self.min_stack.pop()
        
        return None

    def top(self) -> int:
        # check in case there are no elements in the stack. ERROR CONDITION WILL NOT RUN        
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.min_stack[-1]
