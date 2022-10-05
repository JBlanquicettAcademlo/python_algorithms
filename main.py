




#Sebas Aguero
# def current_speed(d,t):
#     v= d/t 
#     if (int(v)<=30) :
#         return 'el automovil va lento'
#     elif (int(v)>30 and int(v)<=70): 
#         return 'el automovil va normal'
#     else: 
#         return 'el automovil va muy rápido'

# print(current_speed(300,20))

#Jorge Lopez
def speed_car(distance, time):
    v = distance * time

    if (v == 2000):
        print("Too fast")

    elif (v > 1000 and v < 2000): #refactor
        print("Normal")

    else:
        print("Too slow")
speed_car(100, 15)

#Billy Campagnoly
def current_speed(D, T):
    V = D/T
    if (V >= 100):
        print("Slow down")
    elif (V == 80):
        print("continue")
    else:
        print("Speed up")

current_speed(100, 5)