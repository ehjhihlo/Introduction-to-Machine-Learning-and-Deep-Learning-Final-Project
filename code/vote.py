import pandas as pd
from scipy import stats

# 幾個結果最好的預測結果
file1 = pd.read_csv('./ensemble/predict_ML_final (39).csv')
file2 = pd.read_csv('./ensemble/predict_ML_final (42).csv')
file3 = pd.read_csv('./ensemble/predict_ML_final (44).csv')
# file4 = pd.read_csv('./ensemble/predict_ML_final (42).csv')

# 將結果進行投票，再輸出csv檔
ans = []
for i in range(len(file1['Name'])):
  nums = []
  nums.append(file1['Type'][i])
  nums.append(file2['Type'][i])
  nums.append(file3['Type'][i])
  # nums.append(file4['Type'][i])

  ans.append(stats.mode(nums)[0][0])

with open('predict_final_ensemble2.csv', 'w') as f:
    f.write('Name,Type\n')
    for i, y in enumerate(ans):
        f.write('{},{}\n'.format(file1['Name'][i], y))