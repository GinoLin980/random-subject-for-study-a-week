import random
subjects = ["國文","數學","英文","地理","歷史","公民"]
week =["週日","週一","週二","週三","週四","週五","週六"]
result =[]
def sr():
  return random.choice(subjects)
  
def days():
  a = [sr(), sr()]
  if a[0] == a[1]:
    return days()
  return a
  
def final():
  arr = []
  global count
  count ={}
  for i in range(7):
    arr.append(days())
  for item in subjects:
    count[item] = sum(v.count(item) for v in arr)
  for j in count:
    if count[j] >3 or count[j] ==0: #最多多少
      return final()
  return arr

result = final()
first =[]
second=[]
for i in range(7):
  first.append(result[i][0])
  second.append(result[i][1])

print(" ".join(week))
print("")
print(" ".join(first))
print(" ".join(second))
print("")
for j in count:
  print(j,count[j], "百分比：{:.2%}".format(count[j]/(2*7)))

