# -*- coding: utf-8 -*-
"""week3_assignment2_problem

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RhK2f0_7t2ZGWFEk_DPDbtbztZQ19iBI
"""

def calculate_h_index(citations):
    citations = bubble_sort(citations)
    n = len(citations)
    h_index = 0
    for i in range(n):
        if citations[i] > i + 1:
            h_index = i + 1
        else:
            break 
    return h_index

def bubble_sort(list):
    n = len(list)
    if n == 1:
        return list
    for i in range(n-1):
      if list[i] < list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
    list = bubble_sort(list[:-1]) + list[-1:]
    return list

#### Do not edit here ####
import random
random_length = random.randint(1, 30)
random_list = [random.randint(0, 30) for _ in range(random_length)]
print(f'Initial Random List is: {random_list}')

h_index = calculate_h_index(random_list)
print(f'Researcher\'s h-index is: {h_index}\n')