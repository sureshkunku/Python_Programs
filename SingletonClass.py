class SingletonClass:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

# Usage
obj1 = SingletonClass()
obj2 = SingletonClass()

print(obj1 is obj2)  # Output: True
