import pandas as pd  
  
# 读取Excel文件  
file_path = 'old_student.xlsx'  
try:  
    df = pd.read_excel(file_path)  
except FileNotFoundError:  
    print(f"文件 {file_path} 未找到。")  
    exit(1)  
except Exception as e:  
    print(f"读取文件时发生错误: {e}")  
    exit(1)  
  
# 性别列索引  
gender_column_index = 7  
# 题目列索引，假设是最后一列  
last_column_index = len(df.columns) - 1  
  
# 检查索引是否有效  
if gender_column_index >= len(df.columns) or last_column_index >= len(df.columns):  
    print("索引超出列范围。")  
    exit(1)  
  
# 根据性别和题目进行分组统计  
grouped = df.groupby([df.columns[gender_column_index], df.columns[last_column_index]]).size().reset_index(name='count')  
  
# 为了方便后续计算百分比，给分组后的DataFrame添加列名  
grouped.columns = ['Gender', 'Question', 'Count']  
  
# 计算每个性别的总人数  
gender_totals = df.iloc[:, gender_column_index].value_counts().to_dict()  
  
# 初始化输出文本  
output_text = ""  
  
# 遍历分组结果，计算百分比并添加到输出文本中  
for index, row in grouped.iterrows():  
    gender = row['Gender']  
    question = row['Question']  
    count = row['Count']  
    percentage = (count / gender_totals[gender]) * 100  
    output_text += f"性别: {gender}, 题目: {question}, 出现次数: {count}, 百分比: {percentage:.2f}%\n"  
  
# 将输出文本保存到文件  
with open('output.txt', 'w', encoding='utf-8') as file:  
    file.write(output_text)  
  
print("统计结果已保存到output.txt文件中。")