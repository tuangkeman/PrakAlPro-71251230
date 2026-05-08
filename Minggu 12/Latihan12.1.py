dictionary = {1:10,2:20,3:30,4:40,5:50,6:60}
urutan = 0
print("key ", "value ", "item ")
for key , value in dictionary.items():
    urutan += 1
    print(f"{key}    {value}      {urutan}")