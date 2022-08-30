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

   text = message.text
   generated_text = text_gen(text, 80)
   await message.answer(generated_text)

#keep_alive()
aiogram.executor.start_polling(dp, skip_updates=True)
