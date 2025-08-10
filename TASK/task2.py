#1
principal_Amount=input("Enter Principal Amount:")
p=int(principal_Amount)
rate=input("Enter Rate(%):")
r=int(rate)
time=input("Enter Time(years):")
t=int(time)
calculate=(p*r*t)/100
print(f"Simple Interest is:{calculate}")


#2
temperature_C=25
temperature_F=78
print(temperature_C)
print(temperature_F)


#Celsius to Fahrenheit
fah=(78*9/5)+32
print(f"{temperature_C}°C in Fahrenheit is {fah}°F")
#convert to Celsis
cel=(temperature_F-32)*5/9
print(f"{temperature_F}°F in Celsius is {cel}°C")


#3
num_1=288
num_2=345
num_3=599
print(num_1,num_2,num_3)
average=(num_1+num_2+num_3)/3
print(f"The average of {num_1},{num_2},{num_3}is={average}")


#4
r=5
pie=22/7
area=pie*r**2
print(f"The area of the circle with radius {r} is {area}")