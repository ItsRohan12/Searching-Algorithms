#!/usr/bin/env python
# coding: utf-8

# In[8]:


def binarySearch(array, x):
    low = 0
    high = len(array)-1
    #To check wheather the array is sorted or not
    while low<=high:
         # To find the midpoint of arr
        mid = low + (high - low) //2
        mid_value = array[mid]
        if mid_value == x:
            return mid
        # If mid is greater than the x so it will shift high value to mid minus 1
        elif x < mid_value:
            high = mid - 1
            # If not mid will shift 1 place right
        else:
            low = mid + 1
            
    return None
array_1 = [2,4,6,8,9,10,12,14,16,18,20]
x_a = 18
print(binarySearch(array_1, x_a))
        


# In[ ]:




