lista = ['red', 'green', 'blue']
listb = ['#FF0000','#008000', '#0000FF']
order = [1,2,0]
ba = [lista[i] for i in order]
bb = [listb[i] for i in order]
dik = dict(zip(ba, bb))
print(dik)