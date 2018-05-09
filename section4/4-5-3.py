import pandas as pd
import numpy as np

# 랜덤으로 DataFrame 생성
df = pd.DataFrame(np.random.randint(0, 100, size=(100, 7)), columns=list('ABCDEFG'))
print(df)

df.to_csv('C:\\Users\\User\\workspace\\study-python\\section4\\result_s2.csv', index=False, header=False)
