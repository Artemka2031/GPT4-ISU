import os

from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "./models/vicuna-13b-v1.5"
OFFLOAD_FOLDER = "./offload_weights"

# Создайте директорию для оффлоадинга, если её нет
os.makedirs(OFFLOAD_FOLDER, exist_ok=True)

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    device_map="auto",
    offload_folder=OFFLOAD_FOLDER  # Указываем директорию для оффлоадинга
)
print("Model loaded successfully.")


def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_length=512, do_sample=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
