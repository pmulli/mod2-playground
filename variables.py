class MyClass:
    myClassVariable = ["Hello"]

    def __init__(self):
        self.myInstanceVariable = [1,2,3]

objectOne = MyClass()
objectTwo = MyClass()

objectOne.myInstanceVariable.append(4)

print(objectOne.myInstanceVariable)
print(objectTwo.myInstanceVariable)
