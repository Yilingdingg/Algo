class Stack:
    def __init__(self,n):
        self.stack=[]
        self.n=n 

        #push funtion
    def push(self,k):
        if len(self.stack)<self.n:
            self.stack.append(k)
        else:
            print("The stack is full.")

        #pop function
    def pop(self):
        if len(self.stack)==0:
            print("The stack is empty.")
        else:
            self.stack.pop(-1)

        #clear function
    def clear(self):
        if len(self.stack)==0:
            print("The stack is empty.")
        else:
            self.stack=[]

        #get the top value
    def top(self):
        if len(self.stack)==0:
            print("The stack is empty.")
        else:
            return self.stack[-1]
        
        #size function
    def size(self):
        if len(self.stack)==0:
            print("The stack is empty")
        else:
            return len(self.stack)
    
        #print the stack
    def display(self):
        if len(self.stack)==0:
            print("The stack is empty")
        else:
            return self.stack

stack=Stack(12)
stack.push(6)
stack.push(15)
stack.push(-19)
stack.push(78)
#return --> use print
print(stack.display())
stack.pop()
print(stack.size())
print(stack.display())
print(stack.top())

print(stack.display())