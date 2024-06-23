import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
new_data = []
for index, items in data.iterrows():
    if items['whoAmI'] == 'human':
      new_data.append({'human':True, 'robot':False})
      
    else:
      new_data.append({'human':False, 'robot':True})
new_data = pd.DataFrame(new_data)
new_data.head()
