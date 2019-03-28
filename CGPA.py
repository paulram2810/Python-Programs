ca1 = input("Enter marks for First CA (max 30) : ")
ca2 = input("Enter marks for Second CA (max 30) : ")
mid = input("Enter marks for Mid Term (max 40) : ")
end = input("Enter marks for End Term (max 70) : ")
att = input("Enter marks for Attendence (max 5) : ")
ca = ((int(ca1)+int(ca2))*25)/60
mid = int(mid)/2
end = (int(end)*5)/7
att = int(att)
marks = ca+mid+end+att
print("Total marks obtained (max 100) : ",int(marks))
cgpa = marks/9.8
cgpa = int((cgpa * 100) + 0.5) / 100.0
print("CGPA : ",cgpa)
if cgpa > 9:
  print("Grade : O")
elif cgpa > 8 and cgpa <= 9:
  print("Grade : A+")
elif cgpa > 7 and cgpa <= 8:
  print("Grade : A")
elif cgpa > 6 and cgpa <= 7:
  print("Grade : B")
elif cgpa > 5 and cgpa <= 6:
  print("Grade : C")
elif cgpa > 4 and cgpa <= 5:
  print("Grade : D")
else:
  print("Grade : E")
