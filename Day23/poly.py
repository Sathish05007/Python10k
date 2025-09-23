# #POLYMORPHISAM ====> MANY FORMS 

# class Dog:
#     def speak(self):
#         return "Woof!!"
    
# class Cat:
#     def speak(self):
#         return "Meow!!"
# class Tiger:
#     def speak(self):
#         return "Rore!!"

# def animal_sounds(animals):
#     print(animals.speak())

# dog= Dog()
# cat= Cat()
# tiger= Tiger()

# animal_sounds(dog)
# animal_sounds(cat)
# animal_sounds(tiger)


class Send_meg:
    def send(self,message):
        print(f"Sms sent: {message}")

class Send_email:
    def send(self,message):
        print(f"Email sent: {message}")

class Notifier:
    def send(self,message):
        print(f"Notifier sent: {message}")

def sendMesg(sender,message):
    sender.send(message)

sendMesg(Send_meg(),"Hi your otp is 123")
sendMesg(Send_email(),"you selected for tcs drive")
sendMesg(Notifier(),"Virus Alert")


from abc import ABC, abstractmethod

# class WaterFilter(ABC):
#     # @abstractmethod
#     # # def 

# class CoolWater(WaterFilter):
#     def waterPasser(self):
#         print("Cool water Served")
# class HotWater(WaterFilter):
#     def waterPasser(self):
#         print("Hot water Served")
# class NormalWater(WaterFilter):
#     def waterPasser(self):
#         print("Normal water Served")    

# c=CoolWater
# h=HotWater
# n=NormalWater

# c.waterPasser()
# h.waterPasser()
# n.waterPasser()

