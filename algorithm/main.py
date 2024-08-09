import pandas as pd  
  
# 读取Excel文件  
file_path = 'old_student.xlsx'  
try:  
    df = pd.read_excel(file_path)  
except FileNotFoundError:  
    print(f"文件 {file_path} 未找到。")  
    exit(1)  
  
# 假设gender_column是性别列，且索引为7（从0开始计数）  
# 假设最后一列包含题目  
gender_column = df.iloc[:, 7]  
last_column = df.iloc[:, -1]  
  
# 检查gender_column是否包含有效的性别信息  
if not gender_column.isin(['男', '女']).all():  
    print("性别列包含无效值，请检查数据。")  
    exit(1)  
  
# 使用groupby按性别分组，并计算每个性别下题目的出现频率  
grouped = df.groupby(gender_column)[last_column.name].value_counts(normalize=True).mul(100).reset_index(name='Percentage')  
grouped.columns = ['Gender', 'Question', 'Percentage']  
  
# 打印结果  
print(grouped)  
  
# 如果你想要分别打印男生和女生的统计信息  
male_stats = grouped[grouped['Gender'] == '男']  
female_stats = grouped[grouped['Gender'] == '女']  
  
print("男生题目统计：")  
print(male_stats)  
  
print("女生题目统计：")  
print(female_stats)