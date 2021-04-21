# 8. Write a Python program to check a list is empty or not.

def is_empty(sample_list):
    if len(sample_list) == 0:
        return True
    else:
        return False


# sample_list = []
sample_list = list(range(5))
print(is_empty(sample_list))
