dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dict4 = {}
for i in (dic1, dic2, dic3):
    print('i', i)
    dict4.update(i)
print(dict4)