import mysql.connector
import json
import torch
from transformers import BertTokenizer, BertModel


student_infos = []
# 建立数据库连接
mydb = mysql.connector.connect(
    host="192.144.133.50",  # 数据库服务器地址，通常为 localhost
    user="root",  # 数据库用户名
    password="abu0418",  # 数据库密码
    database="dormitory"  # 要使用的数据库名称
)

# 创建游标对象
mycursor = mydb.cursor()

# 执行 SQL 查询语句获取 user 表数据
sql = "SELECT id, details FROM users"
mycursor.execute(sql)

# 获取查询结果
results = mycursor.fetchall()

# 打印结果
for row in results:
    details_dict = json.loads(row[1])  # 将字符串转换为字典
    gender = details_dict.get('gender', 'Not Found')  # 获取 gender 值，如果不存在则返回 'Not Found'
    # print(f"ID: {row[0]},details: {row[1]}, Gender: {gender}")
    student_infos.append((row[0], row[1], gender))


def preprocess_text(text):
    # 这里可以进行一些简单的文本预处理，比如去除特殊字符、转换为小写等
    return text

def get_embedding(text, tokenizer, model):
    text = preprocess_text(text)
    encoded_input = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**encoded_input)
    return outputs.last_hidden_state.mean(dim=1)

def calculate_similarity(embedding1, embedding2):
    # 将二维张量展平为一维
    embedding1 = embedding1.view(-1)
    embedding2 = embedding2.view(-1)
    # 计算余弦相似度
    dot_product = torch.dot(embedding1, embedding2)
    norm1 = torch.norm(embedding1)
    norm2 = torch.norm(embedding2)
    similarity = dot_product / (norm1 * norm2)
    return similarity

# 假设我们有一个函数来模拟计算每个宿舍的满意度
def calculate_satisfaction(room, embeddings):
    total_similarity = 0
    for i in range(len(room)):
        for j in range(i + 1, len(room)):
            total_similarity += calculate_similarity(embeddings[room[i]], embeddings[room[j]])
    average_similarity = total_similarity / (len(room) * (len(room) - 1) / 2)
    return average_similarity

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 分别存储男生和女生的信息
male_student_infos = [info for info in student_infos if info[2] == '男']
female_student_infos = [info for info in student_infos if info[2] == '女']

male_embeddings = []
female_embeddings = []

for student_info in male_student_infos:
    male_embeddings.append(get_embedding(student_info[1], tokenizer, model))

for student_info in female_student_infos:
    female_embeddings.append(get_embedding(student_info[1], tokenizer, model))

# 用于存储已经分配宿舍的学生索引
assigned_male_students = []
assigned_female_students = []

# 分配男生宿舍
allocated_male_rooms = []
for i in range(len(male_student_infos) // 4):
    room = []
    max_similarity = -1
    for j, embedding in enumerate(male_embeddings):
        if j not in assigned_male_students:
            total_similarity = 0
            for k in room:
                total_similarity += calculate_similarity(embedding, male_embeddings[k])
            if len(room) == 0:
                total_similarity = 0
            avg_similarity = total_similarity / len(room) if len(room) > 0 else 0
            if avg_similarity > max_similarity:
                max_similarity = avg_similarity
                selected_student = j
    room.append(selected_student)
    assigned_male_students.append(selected_student)
    for j, embedding in enumerate(male_embeddings):
        if j not in assigned_male_students:
            total_similarity = 0
            for k in room:
                total_similarity += calculate_similarity(embedding, male_embeddings[k])
            avg_similarity = total_similarity / len(room)
            if len(room) < 4 and avg_similarity > max_similarity / 2:  # 可以根据实际情况调整这个阈值
                room.append(j)
                assigned_male_students.append(j)
    allocated_male_rooms.append(room)

# 分配女生宿舍
allocated_female_rooms = []
for i in range(len(female_student_infos) // 4):
    room = []
    max_similarity = -1
    for j, embedding in enumerate(female_embeddings):
        if j not in assigned_female_students:
            total_similarity = 0
            for k in room:
                total_similarity += calculate_similarity(embedding, female_embeddings[k])
            if len(room) == 0:
                total_similarity = 0
            avg_similarity = total_similarity / len(room) if len(room) > 0 else 0
            if avg_similarity > max_similarity:
                max_similarity = avg_similarity
                selected_student = j
    room.append(selected_student)
    assigned_female_students.append(selected_student)
    for j, embedding in enumerate(female_embeddings):
        if j not in assigned_female_students:
            total_similarity = 0
            for k in room:
                total_similarity += calculate_similarity(embedding, female_embeddings[k])
            avg_similarity = total_similarity / len(room)
            if len(room) < 4 and avg_similarity > max_similarity / 2:  # 可以根据实际情况调整这个阈值
                room.append(j)
                assigned_female_students.append(j)
    allocated_female_rooms.append(room)

sql = """
CREATE TABLE dormitory (
    gender VARCHAR(10),
    dormitory_number INT,
    student_ids VARCHAR(255),
    satisfaction FLOAT
)
"""

# 执行创建表的 SQL 语句
mycursor.execute(sql)

# 提交更改
mydb.commit()

# 打印分配结果和满意度
print("男生宿舍分配:")
for i, room in enumerate(allocated_male_rooms):
    student_ids = [male_student_infos[j][0] for j in room]
    satisfaction = calculate_satisfaction(room, male_embeddings)
    print(f"宿舍 {i + 1}: {student_ids}, 满意度: {satisfaction}")
    sql_insert_male = "INSERT INTO dormitory (gender, dormitory_number, student_ids, satisfaction) VALUES (%s, %s, %s, %s)"
    values_male = ("Male", i + 1, str(student_ids), satisfaction)
    mycursor.execute(sql_insert_male, values_male)

print("女生宿舍分配:")
for i, room in enumerate(allocated_female_rooms):
    student_ids = [female_student_infos[j][0] for j in room]
    satisfaction = calculate_satisfaction(room, female_embeddings)
    print(f"宿舍 {i + 1}: {student_ids}, 满意度: {satisfaction}")
    sql_insert_female = "INSERT INTO dormitory (gender, dormitory_number, student_ids, satisfaction) VALUES (%s, %s, %s, %s)"
    values_female = ("Female", i + 1, str(student_ids), satisfaction)
    mycursor.execute(sql_insert_female, values_female)


mydb.commit()

# 关闭游标和数据库连接
mycursor.close()
mydb.close()