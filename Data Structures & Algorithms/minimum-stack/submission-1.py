class MinStack:

    def __init__(self):
        self.stack = []
        # pushes a new minimum element onto this stack when a new minimum element is initialized
        # note the top of the stack contains the current minimum element. 
        self.min_stack = [] 

    def push(self, val: int) -> None:
        # first adds element to unordered stack
        self.stack.append(val)
        # if we find a new minimum element, push it onto "min_stack"
        if self.min_stack:
            if (val <= self.min_stack[len(self.min_stack) - 1]):
                self.min_stack.append(val)
        else: # if there are no elements on min_stack, then push the current value onto there
            self.min_stack.append(val) 

        return None

    def pop(self) -> None:
        val_popped = self.stack.pop()
        # now check if the minimum element was popped. If so, then pop it off "min_stack"
        if val_popped == self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.pop()
        
        return None

    def top(self) -> int:
        # check in case there are no elements in the stack. ERROR CONDITION WILL NOT RUN        
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        
        return self.min_stack[len(self.min_stack) - 1]
