import turtle 

  

s = turtle.Screen() 

t = turtle.Turtle() 

s.title("Regular Shape Pattern Maker") 

  

print("0 - Red")  

  

print("1 - Orange")  

  

print("2 - Yellow")  

  

print("3 - Green")  

  

print("4 - Blue")  

  

print("5 - Black")  

  

print("6 - Purple")  

  

   

  

   

  

custom = int(input("Choose a color (relative number): "))  

  

   

  

colorLibraryRaw = ["red", "orange", "yellow", "green", "blue", "black", "purple"]  

  

   

  

colorLibrary = colorLibraryRaw[custom]  

  

   

  

t.color(colorLibrary)  

  

  

sides = int(input("Enter amount of sides: ")) 

  

repeat = int(input("Enter amount of times you want to repeat: ")) 

  

  

for i in range(3, repeat): 

  

    for i in range(sides): 

  

            t.fd(50) 

  

            t.rt(360/sides) 

  

s.mainloop() 
