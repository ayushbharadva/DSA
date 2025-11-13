'''
python:
1. None = null
2. elif = elseIf
3. and = &&
4. or = ||
5. not = !
6. Max/Min Int:float('int)/float('-inf)
7. Python numbers are infinite so they never overflow
  example: print(math.pow(2, 200))
           print(math.pow(2, 200) < float('inf')) -> True
8. Arrays:

'''

n1 = [1,2,3]
n2 = [4,5,6]
n3 = zip(n1, n2)
print(list(n3))