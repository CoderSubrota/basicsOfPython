marks = int(input())
if marks >=0 and marks <=100:
     if marks >= 80 and marks <=100:
        print("You have gotten A+")
     elif marks >= 70 and marks < 80:
      print("You have gotten A Grade")
     elif marks >= 60 and marks < 70:
      print("You have gotten A-")
     elif marks >= 50 and marks < 60:
      print("You have gotten B Grade")
     elif marks >= 45 and marks < 50:
      print("You have gotten C Grade")
     elif marks >= 33 and marks < 45:
      print("You have gotten D Grade")
     else:
         print("Failed Good Luck for the next time !!")
else:
    print("Enter valid numbers between 0 to 100 !!")
     