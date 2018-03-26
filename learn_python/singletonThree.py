class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kw):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kw)
    return cls._instances[cls]
class MyClass(metaclass=Singleton):
  pass
