#1 teorema:
#1)это подход, при котором программа рассматривается как набор объектов, взаимодействующих друг с другом
# 2)
# 3)там есть публичный сетод и приватный метод
# 4)
# 5)
# 2 sintaksis
#1) def is_ever(num):
#     if num%2==0:
#         print(True)
#     else:
#         print(False)
# is_ever(3)
# 2)class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#     def display_info(self):
#         return f"Make: {self.make},Model: {self.model},Year: {self.year}"
# b = Car("Bmw","M5 CS",2024)
# print(b.display_info())
# 3)
# def filter_positive_numbers(numbers):
#     num=[]
#     for x in numbers:
#         if x > 0:
#             num.append(x)
#     return num
# print(filter_positive_numbers([-18,-117,-174,5148]))
#
# 4)class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         return f"Hello my name is {self.name},and I am {self.age} years old"
# class Student:
#uyogida yogidim
# 5)
# class Student:
#     def __init__(self,a):
#         self.a=a
#     def greet(self):
#         return self.a
# x=Student("spasibo")
# print(x.greet())
# 3 praktika:
# 1)def name(sirname):
#     return sirname == sirname[::-1]
# if name("232"):
#     print("da")
# else:
#     print("net")
# 2)class BankAccount:
#     def Account(self):
#         self.shotchik=0
#     def deposit(self,x,shotchik):
#         self.shotchik+=x
#     def withdraw(self,):
#         self.shotchik-=a
#     def get_balance(self):
#         return self.shotchik
# bank=BankAccount()
# bank.deposit(50)
# bank.withdraw(15)
# print(bank.get_balance())
# 3)
# string="example"
# result=(string.count("e"),string.count("x"),string.count("a"),string.count("m"),string.count("p"),string.count("l"),)
# print(result)
