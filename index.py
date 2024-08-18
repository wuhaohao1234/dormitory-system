import torch
from transformers import BertTokenizer, BertModel

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

# 假设我们有 20 个学生的信息，格式为 (id, details, gender)
student_infos = [
    (1, '性格活泼开朗，喜欢社交，爱好运动，通常 10 点之后睡，对卫生有较高要求', '女'),
    (2, '性格外向积极，热衷社交活动，喜欢旅行，习惯晚睡，在意寝室卫生', '女'),
    (3, '性格较为内向，喜欢安静，作息规律，对卫生要求一般', '女'),
    (4, '性格温和友善，喜欢参加社团活动，睡眠较晚，对卫生比较在意', '女'),
    (5, '性格热情奔放，爱运动，晚上 11 点睡，注重寝室整洁', '女'),
    (6, '性格开朗乐观，喜欢交友，经常晚睡，对卫生要求高', '女'),
    (7, '性格沉稳内敛，爱好阅读，作息规律，卫生习惯良好', '女'),
    (8, '性格活泼好动，喜欢旅游，睡眠较晚，在意宿舍卫生', '女'),
    (9, '性格大方直爽，热衷社交，通常 10 点后睡，对卫生较在意', '女'),
    (10, '性格温柔善良，喜欢参加活动，晚睡，有一定卫生要求', '女'),
    (11, '性格阳光开朗，爱运动旅行，11 点后睡，讲究卫生', '男'),
    (12, '性格安静内向，喜欢独处，早睡早起，卫生方面一般', '男'),
    (13, '性格外向活泼，喜欢聚会，晚睡，重视寝室清洁', '男'),
    (14, '性格随和亲切，爱参加社团，睡眠较晚，对卫生有要求', '男'),
    (15, '性格活泼俏皮，喜欢户外运动，通常 10 点后睡，在意卫生状况', '男'),
    (16, '性格开朗大方，喜欢社交，晚睡，对寝室卫生较关注', '男'),
    (17, '性格沉稳安静，爱好书法，作息规律，卫生标准较高', '男'),
    (18, '性格热情豪爽，爱旅游运动，睡眠较晚，注重宿舍卫生', '男'),
    (19, '性格乐观向上，喜欢交友活动，10 点后睡，对卫生有讲究', '男'),
    (20, '性格直率坦诚，喜欢运动，晚睡，对宿舍卫生较在意', '男')
]

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

# 打印分配结果和满意度
print("男生宿舍分配:")
for i, room in enumerate(allocated_male_rooms):
    student_ids = [male_student_infos[j][0] for j in room]
    satisfaction = calculate_satisfaction(room, male_embeddings)
    print(f"宿舍 {i + 1}: {student_ids}, 满意度: {satisfaction}")

print("女生宿舍分配:")
for i, room in enumerate(allocated_female_rooms):
    student_ids = [female_student_infos[j][0] for j in room]
    satisfaction = calculate_satisfaction(room, female_embeddings)
    print(f"宿舍 {i + 1}: {student_ids}, 满意度: {satisfaction}")