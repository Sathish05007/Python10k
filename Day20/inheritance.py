# #INHARITENCE :-CREATING NEW CLASS FROM ALRADY EXISTING  CLASS IS KNOWN  INHARITENCE 
# #WE USE EXTERT KEY WORD FOR THIS PROCESS,but IN PYTHON WE USE THE PARENT CLASS NAME AS A PARAMETER IN CHILD CLASS
# #TYPES:-
# #--->SINGLE
# #--->MULTIPIUL
# #--->HYBIRED
# #--->MULTI-LEVEL
# #--->HIERACHICAL

# #SINGLE:-IF WE DRIVE ONE CHILD CLASS FORM SINGLE PARENT CLASS THEN IT IS A SINGLE INHARITENCE

# #WE CREATE A PARENT CLASS
# class Parent():
#     def Pmethode(self):
#      print("Im a methode from parent class")
#     def Pmethode_2(self):
#        print("Iam a second methode from parent class") 

# #WE CREATE A CHILD CLASS
# class Child(Parent): # WE CALLING PARENT CLASS BY USING THE PARENT CLASS NAME(PARENT)
#    def Cmethode(self):
#       print("Iam a methode from child class")
#       #WE ACCESSING THE PARENT METHODE IN CHILD CLASS WE USE SUPER KEY WORD
#       super().Pmethode_2()

# obj1=Child() #WE STORED CHILD CLASS IN A VARIBLE
# #WE ARE CALLING THE ALL CLASS LIKE CHILD,PARENT
# obj1.Cmethode()
# # obj1.Pmethode()     
# # obj1.Pmethode_2() 


# #EXAMPLE:-
# class User:
#    def __init__(self,name,email):
#       self.name=name
#       self.email=email

# class Student(User):
#    def __init__(self,name,email,enrolled_cource):
#       super().__init__(name,email)
#       self.enrolled_cource=enrolled_cource  

#    def get_cource(self): 
#         print(f"{self.name} is learning {self.enrolled_cource}")

#    def remove_cource(self,cource):
#       self.enrolled_cource.remove(cource)
#       self.get_cource()

#    def add_cource(self,cource):
#       self.enrolled_cource.extend(cource)
#       self.get_cource()   
          

# class Tranner(User):
#    def __init__(self,name,email,cources_training):
#       super().__init__(name,email)
#       self.cources_training= cources_training

#    def get_cource(self): 
#         print(f"{self.name} is teaching {self.cources_training}")   

#    def remove_cource(self,cource):
#       self.cources_training.remove(cource)
#       self.get_cource()
#    def add_cource(self,cource):
#       self.cources_training.extend(cource)
#       self.get_cource()    
           

# sathish_obj=Student("sathish","sathish@gmail.com",["html","css","js","node"])
# sathish_obj.get_cource()
# #remove skills
# sathish_obj.remove_cource("html")
# #Add skills
# sathish_obj.add_cource(["html","react","mongodb"])

# harish_obj=Tranner("Harish","harish@gmail.com",["frontend","backend","aws"])
# harish_obj.get_cource()
# harish_obj.remove_cource("aws")
# harish_obj.add_cource(["sql","powerBi","java"])



# # MULTI:-IF WE DRIVE ONE CHILD CLASS FORM MORE THAN ONE PARENT CLASS THEN IT IS A MULTI INHARITENCE
# class Parent1:
#     def P1methode(self):
#         print("Iam methode from Parent1")

# class parent2:
#     def p2methode(self):
#         print("Iam methode form Parent2")

# class Child(Parent1,parent2):
#     def Cmethode(self):
#         print("Iam a methode from Child")
        
#         super().p2methode()

# obj1=Child()
# obj1.Cmethode()
# obj1.P1methode()
# obj1.p2methode()


# # class Parent_Actor:
    
# #     def __init__(self,Pname,Pworth):
# #         self.Pname=Pname
# #         self.Pworth=Pworth
# #         print(f"{self.Pname} is the parent")

# #     def P_assets(self):
# #         print(f"{self.Pname} assets are {self.Pworth} cr")

# # class Child_Actor(Parent_Actor):
    
# #     def __init__(self,Pname,Cname,Pworth):
# #         super(). __init__(Pname,Pworth)
# #         self.Cname=Cname
# #         print(f"{self.Cname} is came by the ref of {self.Pname}")

# #     def Cassets(self,Cworth):
# #         self.Cworth=Cworth
# #         print(f"{self.Cname} is having worth of {self.Cworth} cr")

# #     def total(self):
# #         print(f"total assets of {self.Cname} and {self.Pname} is {self.Pworth + self.Cworth}")

# # ram=Child_Actor("chiranjeev","ramcharan",100)
# # ram.Cassets(50)
# # ram.total()
 


class A:
    def display(self):
        print("A class")

class B:
    def display(self):
        print("B class")

class C(A, B):
    def display(self):
        A.display(self)  # pass self explicitly
        print("C class")
        B.display(self)  # pass self explicitly

obj = C()
obj.display()
