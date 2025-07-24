class multiplefunctions():
    def OddEven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print('Even number')
            message='Even number'
        else:
            print('Odd number')
            message='Odd number'
        return message
    def AgeCategory():
        age=int(input("Enter the age:"))
        if(age<18):
            print("Children")
            cate='Children'
        elif(age<35):
            print("Adult")
            cate="Adult"
        elif(age<59):
            print("Citizen")
            cate='Citizen'
        else:
            print("Senior Citizen")
            cate='Senior Citizen'
        return cate