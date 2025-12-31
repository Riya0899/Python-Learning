from random import randint

class train:
    
    def __init__(self,trainno):
        self.trainno=trainno
        
    def book(self,fro,to):
        print(f"ticket is booked in train no {self.trainno} from {fro} to {to}")
    
    def getstatus(self,fro,to):
        print(f"trainno {self.trainno} is running successfully")
        
    def getfare(self,fro,to):
        print(f"ticket fare in trainno: {self.trainno} from {fro} to {to}")
        
ride=train(12234)
ride.book("rampur","delhi")
ride.getstatus("rampur","delhi")
ride.getfare("rampur","delhi")