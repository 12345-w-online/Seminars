import os
import pandas as pd
import numpy as np


my_dir_path = './'
data = None
names_column = None
for dirpath, dirnames, files in os.walk(my_dir_path, topdown=False):
    for file in files:
        if file.endswith('.log'):
            with open(f'{dirpath}\{file}', 'r+') as f:
                f = f.readlines()
                if names_column is None:
                    names_column = ['File_name'] + f[58 - 1].split()
                if data is None:
                    data = np.concatenate((np.array([file]), np.array(f[59 - 1].split())))
                else:
                    z = np.concatenate(([file], np.array(f[59 - 1].split())))
                    data = np.vstack((data, z))

list_sum = np.array([])
list_mean = np.array([])
list_std = np.array([])
frame = pd.DataFrame(data, columns=names_column)
for name_column in names_column[1::]:
    list_measur = np.array(frame[name_column], dtype=float)
    list_sum = np.append(list_sum, [list_measur.sum()], axis=0)
    list_mean = np.append(list_mean, [list_measur.mean()], axis=0)
    list_std = np.append(list_std, [list_measur.std()], axis=0)
print(os.getcwd())
try:
    os.chdir('./2_term/week1')
    print("if_goin_dir")
except FileNotFoundError:
    print('Save in your directory')
frame.loc[len(frame.index)] = np.append(np.array(['Sum']), list_sum, axis=0)
frame.loc[len(frame.index)] = np.append(np.array(['Mean']), list_mean, axis=0)
frame.loc[len(frame.index)] = np.append(np.array(['Std']), list_std, axis=0)
frame.to_csv('./table_of_data.csv')
