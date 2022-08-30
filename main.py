#from webserver import keep_alive
from gen_config import txt_generate_conf
from bot_config import bot_conf
import aiogram


def text_gen(text, max_length):
   input_ids = tokenizer.encode(text, return_tensors="pt")
   out = model.generate(input_ids, max_length, do_sample=True)
   return list(map(tokenizer.decode, out))[0]

bot, dp = bot_conf()

tokenizer, model = txt_generate_conf()

@dp.message_handler(lambda message: message.text)
async def start(message: aiogram.types.Message):
   #txt_value = []
   #for i in range(10):
   text = message.text
   generated_text = text_gen(text, 80)
      #txt_value.append(generated_text)
   await message.answer(generated_text)
   #with open('values.txt', 'w', encoding="utf-8") as f:
      #for i in txt_value:
         #f.write(f"{i}\n")
   #await message.answer_document(open(r'values.txt', 'rb'))


#keep_alive()
aiogram.executor.start_polling(dp, skip_updates=True)