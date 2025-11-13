test_case = {
  "input": {
    "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "target": 15
  },
  "output": 5
}

def linear_search(list, target):
  position = 0
  while position < len(list):
    if list[position] == target:
      return position
    position += 1
  return -1

index = linear_search(**test_case['input'])
print('index', index);

'''
write an evaluate_test_cases function in below format:
Test Case #0:
Input:
{'list': [3, -1, -9, 13, 5], target: 13}
Expected Output:
3
Actual Output:
3
Execution Time:
0.003 ms
Test Result:
PASSED

Summary
Total: 9, Passes: 9, Failed: 0
'''