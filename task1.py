def A():
 print("Hello")
def B():
 print("How are you")
def C():
  print("Hi")

num = input("Enter one of the Capital letters A, B, or C: ")
if num  == "A":
    A()
elif num == "B":
    B()
elif num == "C":
    C()
else:
    print("Emter a valid letter")
