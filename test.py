from transformers import BertTokenizer, BertModel  
import torch  
import numpy as np  
  
def calc_similarity(s1, s2):  
    # 加载预训练的中文BERT模型和分词器  
    tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')  
    model = BertModel.from_pretrained('bert-base-chinese')  
  
    # 对句子进行分词，并添加特殊标记  
    inputs = tokenizer([s1, s2], return_tensors='pt', padding=True, truncation=True)  
  
    # 将输入传递给BERT模型，并获取输出  
    with torch.no_grad():  
        outputs = model(**inputs)  
        embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()  # 取[CLS]标记的嵌入作为句子嵌入  
  
    # 计算余弦相似度  
    sim = np.dot(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))  
    return sim  
  
# 示例句子  
sentence1 = "我喜欢吃苹果。"  
sentence2 = "苹果是我最喜欢的水果。"  
  
# 计算相似度  
similarity = calc_similarity(sentence1, sentence2)  
print(f"相似度: {similarity:.4f}")