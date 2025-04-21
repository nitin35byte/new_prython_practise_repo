class SingletonMeta(type):
    """
    Metaclass that creates a Singleton instance.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 42

# Usage
singleton_a = Singleton()
singleton_b = Singleton()

print(singleton_a is singleton_b)  # True, both variables refer to the same instance
print(singleton_a.value)           # 42

