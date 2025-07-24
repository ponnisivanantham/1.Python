class ClassAssignmentLibraryAll():
    def Subfields():
        lists = ["Machine Learning","Neural Networks","Vision","Robotics"
             ,"Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for temp in lists:
            print(temp)
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num, "is Even number")
        else:
            print(num, "is Odd number")
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if((gender=="Male") and (age<=21)):
            print("NOT ELIGIBLE")
        elif((gender=="Female") and (age<=18)):
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")
    def percentage():
        m1=int(input("Subject1 ="))
        m2=int(input("Subject2 ="))
        m3=int(input("Subject3 ="))
        m4=int(input("Subject4 ="))
        m5=int(input("Subject5 ="))
        total=m1+m2+m3+m4+m5
        print("Total :",total)
        percent=(total/500)*100
        print("Percentage :",percent)
    def triangle():
        height=int(input("Height ="))
        breadth=int(input("Breadth ="))
        print("Area formula : (Height*Breadth)/2")
        print("Area of Triangle :", ((height*breadth)/2))
        height1=int(input("Height1 ="))
        height2=int(input("Height2 ="))
        breadthp=int(input("Breadthp ="))
        print("Perimeter formula : Height1+Height2+Breadthp")
        print("Perimeter of Triangle :", height1+height2+breadthp)