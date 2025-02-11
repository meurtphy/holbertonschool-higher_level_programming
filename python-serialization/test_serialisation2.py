#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object
new_obj = CustomObject.deserialize("object.pkl")

if new_obj:
    print("\nDeserialized Object:")
    new_obj.display()
else:
    print("\nFailed to deserialize the object.")
