"""Minimal calculator with existing public functions and behavior."""

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

class Calculator:
    def __init__(self):
        self.history=[]
    def evaluate(self, operation, a, b):
        operations={'add':add,'subtract':subtract,'multiply':multiply}
        if operation not in operations:
            raise ValueError('unsupported operation: '+str(operation))
        result=operations[operation](a,b)
        self.history.append((operation,a,b,result))
        return result
