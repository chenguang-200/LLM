from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)
CORS(app)

checkpoint_path = "/home/llm/wjy/training/training-model/SFT/4/result"
device="cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(checkpoint_path)
model = AutoModelForCausalLM.from_pretrained(checkpoint_path,device_map="auto")

@app.route('/chat', methods=['GET','POST'])

def chat():
    data = request.json
    user_input = data['user_input']

    inputs = tokenizer.encode(user_input, return_tensors='pt').to(device)
    attention_mask = torch.ones(
        inputs.shape,
        dtype=torch.long,
        device=model.device
    )

    reply_ids = model.generate(
        inputs,
        do_sample=True,
        attention_mask=attention_mask,
        max_length=300,
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.8,  # 调整温度
        top_k=50,  # 调整 Top-K 参数
        top_p=0.9,  # 调整 Top-P 参数
        no_repeat_ngram_size=3,  # 设置不重复的 n 元组大小
        num_return_sequences=1  # 控制返回的生成序列数量
    ).to(device)

    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200)
