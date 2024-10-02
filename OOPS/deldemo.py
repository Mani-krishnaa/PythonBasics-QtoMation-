class Animal:
    
    def __init__(self) -> None:
      print("object is created")
      
    def __del__(self):
        print("Destroyed object")
        
anm = Animal()
del anm