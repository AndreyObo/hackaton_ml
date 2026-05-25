import pandas as pd


def merge_data(df_left_name, df_right_name, on_key):
    print('Начало работы...')
    df_left = pd.read_csv(df_left_name)
    print('Первый df загружен')
    df_right = pd.read_csv(df_right_name)
    print('Второй df загружен')
    print('Идет merge...')
    df_merge = pd.merge(df_left, df_right, how='inner', on=on_key)
    print('Сохранение...')
    file_name = './data/merged.pkl'
    df_merge.to_pickle(file_name)
    return file_name