import sys
if len(sys.argv)!=3 :
  print("usage : python script.py <salary> <bonus>")
  exit(1)
salary=sys.argv[0]
bonus=sys.argv[1]
print("salary is ",salary)
print("bonus is ",bonus)
total=(salary * bonus/100)+salary
print("total salary is is ",total)
