import io
import os

import pandas as pd


def pre_process():
    with open(r"C:\code\src\python\autoQAG\data\ipre_data\test\sent_test.txt", "r",
              encoding="utf-8") as original_file:
        content = original_file.read()
    content = content.replace('" ', "")
    sent_test = pd.read_csv(io.StringIO(content), sep='\t', header=None)
    sent_test.to_csv(r"C:\code\src\python\autoQAG\data\ipre_data\test\merged_sent_test.csv", sep=',', header=False,
                     index=False)


def distribute():
    relation2id = pd.read_csv(r"C:\code\src\python\autoQAG\data\ipre_data\relation2id.txt", sep='\t', header=None)
    relation_dict = {}
    relation_map = {}

    for index, row in relation2id.iterrows():
        key = str(row[1])
        relation_map[key] = row[0]
        relation_dict[key] = []

    sent_relation_train = pd.read_csv(r"C:\code\src\python\autoQAG\data\ipre_data\test\sent_relation_test.txt",
                                      sep='\t', header=None)
    for index, row in sent_relation_train.iterrows():
        for i in str(row[1]).split(' '):
            relation_dict[i].append(row[0])

    sent_train = pd.read_csv(r"C:\code\src\python\autoQAG\data\ipre_data\test\merged_sent_test.csv", sep=',',
                             header=None)
    sent_train.set_index(0, inplace=True)
    outFile = r"C:\code\src\python\autoQAG\data\ipre_data\test\category"
    for key, value in relation_dict.items():
        key_df = sent_train.loc[value, [1, 2, 3]].copy()
        key_df[4] = 'NAN' if key == "0" else relation_map.get(key, 'NAN')
        key_df.to_csv(outFile + r"\\" + str(key) + ".txt", sep='\t', header=False, index=False)
        print(f"{key}轮结束")


couple = ['1', '2', '3', '4', '5', '6']  # {'1': 536, '2': 12, '3': 13, '4': 296, '5': 3, '6': 10}
teacher = ['33', '34']  # {'33': 201, '34': 11}

brother = ['16', '17', '18', '19']  # {'16': 43, '17': 39, '18': 9, '19': 23}


# def dataRate():
#     directory_path = r"C:\code\src\python\autoQAG\data\ipre_data\test\category"
#     file_line_counts = {}
#     for filename in couple:
#         file_path = os.path.join(directory_path, filename + '.txt')
#         if os.path.isfile(file_path):
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 lines = file.readlines()
#                 file_line_counts[filename] = len(lines)
#
#     print(file_line_counts)

def not_in_list(temp: list, num: int):
    directory_path = r"C:\code\src\python\autoQAG\data\ipre_data\test\category"
    num_per_file = num // (34 - len(temp))
    df_list = []
    for file in os.listdir(directory_path):
        filename = file.split('.')[0]
        if filename not in temp:
            if os.stat(os.path.join(directory_path, file)).st_size == 0:
                continue
            df = pd.read_csv(os.path.join(directory_path, file), sep='\t', header=None)
            if len(df) > num_per_file:
                sampled_df = df.sample(n=num_per_file)
            else:
                sampled_df = df
            df_list.append(sampled_df)
    result_df = pd.concat(df_list, ignore_index=True)
    return result_df


def make_test_dataSet(temp: list,num:int):
    directory_path = r"C:\code\src\python\autoQAG\data\ipre_data\test\category"
    new_df = pd.DataFrame()
    for filename in temp:
        pf = pd.read_csv(os.path.join(directory_path, filename + '.txt'), sep='\t', header=None)
        if len(pf) < num:
            new_df = pd.concat([new_df, pf], ignore_index=True)
        else:
            sampled_pf = pf.sample(n=int(num))
            new_df = pd.concat([new_df, sampled_pf], ignore_index=True)
    return new_df


def make_test(temp:list,name:str):

    num = 300//(len(temp)+1)
    new_df = pd.DataFrame()
    new_df = pd.concat([new_df, make_test_dataSet(couple, num)], ignore_index=True)
    new_df = pd.concat([new_df, not_in_list(couple, num)], ignore_index=True)
    new_df.to_csv(rf"C:\code\src\python\autoQAG\data\ipre_data\test\test_{name}.csv", sep=',', header=False, index=False)


if __name__ == "__main__":
    # 其后为测试集的分布
    couple = ['1', '2', '3', '4', '5', '6']  # {'1': 536, '2': 12, '3': 13, '4': 296, '5': 3, '6': 10}
    # 训练集分布
    # {'1': 8142, '2': 218, '3': 183, '4': 5544, '5': 245, '6': 69}
    teacher = ['33', '34']  # {'33': 201, '34': 11}
    # {'33': 2911, '34': 547}
    brother = ['16', '17', '18', '19']  # {'16': 43, '17': 39, '18': 9, '19': 23}
    # {'16': 1673, '17': 637, '18': 532, '19': 805}
    # pre_process()
    # distribute()
    make_test(brother,'brother')
