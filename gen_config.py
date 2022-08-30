from transformers import AutoTokenizer, AutoModelForCausalLM

def txt_generate_conf():
  model_name_or_path = "sberbank-ai/rugpt3large_based_on_gpt2"
  tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
  model = AutoModelForCausalLM.from_pretrained(model_name_or_path)
  return tokenizer, model