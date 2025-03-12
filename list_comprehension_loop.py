cars = ['merc', 'bmw', 'marcielago', 'ev6']
old_list = []

for b in cars : 
  if 'm' in b :
    old_list.append(b)
    
print(old_list)

older_list = [n for n in old_list if len(n) <= 4]

print(older_list)
