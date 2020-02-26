color=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
while True:
    print("#############################################")
    print("##                                         ##")
    print("##  4 Band Resistor Color Code Calculator  ##")
    print("##                                         ##")
    print("#############################################")
    print("")
    print("By neon-l")
    print("")
    input1=input("# Enter the color of the first band : ").lower()
    input2=input("# Enter the color of the second band : ").lower()
    input3=input("# Enter the color of the multiplier : ").lower()
    input4=input("# Enter the color of tolerance : ").lower()
    if input3=="silver":
        a=str(color.index(input1))
        b=str(color.index(input2))
        c=0.01
        result=(int(a+b))*c

    elif input3=="gold":
        a=str(color.index(input1))
        b=str(color.index(input2))
        c=0.1
        result=(int(a+b))*c
    else:
        a=str(color.index(input1))
        b=str(color.index(input2))
        c=int(color.index(input3))
        result=(int(a+b))*10**c

    if input4=="brown":
        tol=1

    elif input4=="red":
        tol=2

    elif input4=="green":
        tol=0.5

    elif input4=="blue":
        tol=0.25

    elif input4=="violet":
        tol=0.1

    elif input4=="grey":
        tol=0.05

    elif input4=="gold":
        tol=5

    elif input4=="silver":
        tol=10

    elif input4=="none" or "missing" or "missing band" or "nothing" or "no band" or "no":
        tol=20
    print("--> The resistance of the resistor is {} ohms and the tolerance is {} percent.".format(round(result,5),tol))