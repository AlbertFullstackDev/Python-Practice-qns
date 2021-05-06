# 8. Write a Python script to merge two Python dictionaries.

dic1 = dict(x=1, y=2, z=3)
dic2 = dict(a=10, b=11, c=13)

conc_dict = {}

for d in (dic1, dic2):
    conc_dict.update(d)


print(conc_dict)
