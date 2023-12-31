import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_encoded = pd.concat([pd.Series(1, index=data.index, name='whoAmI'),
                             pd.get_dummies(data['whoAmI'])], axis=1)
one_hot_encoded = one_hot_encoded.astype(int)
data_one_hot = pd.concat([data, one_hot_encoded], axis=1)
data_one_hot = data_one_hot.drop('whoAmI', axis=1)

data_one_hot.head()
print(data)
print()
print(data_one_hot)