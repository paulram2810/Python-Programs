age = eval(input("Enter the age of the candidate : "))
if (age>=18):
    print("\nCandidate is eligible for voting.")
else:
    print("\nCandidate is not eligible for voting. Will be eligible for voting in ",(18-age)," year(s).")
