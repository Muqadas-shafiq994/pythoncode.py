# Function for marks calculation
print("calculating student marks")
def stud_marks(m,n,p,q,r):
   total_marks= m+n+p+q+r
   percentage=total_marks/5
   
   if percentage>=90:
      print("you got A+ grade")
   elif percentage >= 80:
      print("you got A grade")
   elif percentage >= 70:
      print("you got B grade")
   elif percentage >=60:
      print("you got C grade")
   elif percentage >=50:
      print("you got D grade")
   else:
      print("you got F grade . means you fail")
   return(total_marks,percentage)
   
result=stud_marks(80,67,79,90,45)
print("____your result is____\n")
print(result)

   