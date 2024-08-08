import pandas as pd  
  
# 读取Excel文件  
file_path = 'old_student.xlsx'  
try:  
    df = pd.read_excel(file_path)  
except FileNotFoundError:  
    print(f"文件 {file_path} 未找到。")  
    exit(1)  
  
# 假设最后一列包含题目  
last_column = df.iloc[:, -1]  
  
# 计算值频数  
value_counts = last_column.value_counts()
  
# 计算总行数  
total_count = len(df)  
  
# 打印每个题目及其出现的百分比  
for number, count in value_counts.items():  
    percentage = (count / total_count) * 100  
    print(f"题目 {number} 出现了 {count} 次，占总数据的 {percentage:.2f}%")