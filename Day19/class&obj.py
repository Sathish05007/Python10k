# class SimpleClass: 
#    --------------
#    --------------
#    --------------
#    --------------

# IT IS A STATICT METHODE OF CREATING CLASS
#CREATING A CLASS
class Person:
    name="sagar"
    age=25
    gender="male"
    cource="MERN"

#CALLING THE CLASS AND STORED IN A VARIBLE
obj1=Person()    
obj2=Person()

#PRINT THE CLASS
print(Person().name)
print(obj1.name,obj1.age,obj1.gender,obj1.cource)
print(obj2.name)

#UPDATING THE VALUES 
obj1.name="sagar ejjagiri" # we update the value in obj1 it don't effect on obj2 and the main(person) class
print(obj1.name)
print(obj2.name)


# IT IS A DYNAMIC METHODE OF CREATING CLASS
class Person():
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

obj1_akhil=Person("akhil","male",25)
obj2_venkey=Person("venkey","male",25)

print(obj1_akhil.name,obj1_akhil.age,obj1_akhil.gender)
print(obj2_venkey.name,obj2_venkey.age,obj2_venkey.gender)
        
class SocialMedia:
    def __init__(self, insta, facebook, youtube, whatsapp):
        self.instagram = insta
        self.facebook = facebook
        self.youtube = youtube
        self.whatsapp = whatsapp

obj_sagar=SocialMedia("sagarr__07","royal_boy","india",8888888888)
obj_laddu=SocialMedia("l@ddu_18","laddu_18","L@ddu_18",9999999999)

print(obj_sagar.facebook,obj_sagar.instagram)
print(obj_laddu.facebook,obj_laddu.whatsapp)

# YOUTUBE,INSTA,BOOKMYSHOW,NETFLEX
#NAME,COLOR,WORK,

class App:
    def __init__(self, name, color, work):
        self.name = name
        self.color = color
        self.work = work

    def display_info(self):
        print(f"\n App Name : {self.name}")
        print(f" Color    : {self.color}")
        print(f" Work     : {self.work}")


youtube = App("YouTube", "Red & White", "Video Streaming")
instagram = App("Instagram", "Purple&Pink", "Photo & Video Sharing")
bookmyshow = App("BookMyShow", "Red & White", "Movie Ticket Booking")
netflix = App("Netflix", "Black & Red", "Web Series & Movie Streaming")

youtube.display_info()
instagram.display_info()
bookmyshow.display_info()
netflix.display_info()
    

# adding methodes/functions/bhevioures in class



