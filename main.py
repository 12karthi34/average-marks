if__name="__main__"
subjects=int(input("Enter the number of subjects:"))
marks=[]
for i in range(subjects):
  mark=int(input("Enter the marks:"))
  marks.append(mark)
  print(marks)
def addition(marks):
    find_mark=0
    for mark in marks:
      find_mark=find_mark+mark
      #print(find_mark)
      return find_mark
def average(find_mark,subjects):
      avg=find_mark/subjects
      return avg
find_mark=addition(marks)
print(find_mark)
avg=average(find_mark,subjects)
print("The average of the marks is:",avg)
      
      
  

            