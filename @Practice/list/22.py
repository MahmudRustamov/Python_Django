"""Masala: Listda har xil ma'lumotlar berilgan. Ushbu listda stringlarni 
alohida TEXT nomli listga yozing va o'sish tartibida saralang va chiqaring,
 qolganlarni OTHER nomli listga joylashtiring va kamayish tartibida saralang."""


list1=['salom',123,True,'Hayr','world',3.14,'7214']

text, other = list(), list()

for i in list1:
    if type(i) == str:
        text.append(i)
    else:
        other.append(i)
text.sort()
other.sort()
print(text)
print(other)