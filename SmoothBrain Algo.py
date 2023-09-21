#!/usr/bin/env python
# coding: utf-8

# In[20]:


import random

def bogo_sort(a, max_attempts=10):
    attempts = 0
    while not is_sorted(a) and attempts < max_attempts:
        shuffle(a)
        attempts += 1

def is_sorted(a):
    n = len(a)
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range(n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]

# Predetermined answer keys
answer_keys = [3, 1, 5, 2, 4, 12, 4, 21, 12, 10, 90, 23, 910, 22, 40, 23, 79, 290, 89, 102, 123, 2341, 421, 2341]
print("Answer key:", answer_keys)

# initialize Student ID 
student_id = 19200277

for i in range(5000):
    bogo_sort(answer_keys)
    print("Student ID:", student_id, "Student's questions:", answer_keys[:5000])
    student_id += 1 


# 

# In[ ]:





# In[ ]:





# 
