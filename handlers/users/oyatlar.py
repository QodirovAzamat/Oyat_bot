from loader import db, dp
from aiogram import types
from keyboards.default.oyat_button import back_button,oyat_button 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from states.Oyat_state import Oyat_gurup
import requests

@dp.message_handler(text="Oyatlar")
async def make_cots(message:types.Message):
    await message.answer("Oʻzingizga kerakli suraning raqamini kiriting, nomini yozing yoki tugmalardan foydalaning",reply_markup=oyat_button())
    await Oyat_gurup.quran_name.set()

@dp.message_handler(state=Oyat_gurup.quran_name)
async def make_cot(message:types.Message, state:FSMContext):
    quran_name = int(message.text[0])
    name_sura = message.text
    url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json'
    respons = requests.get(url=url).json()
    son = respons["quran"]
    len_son = []
    for i in son:
        if int(i["chapter"]) == quran_name:
            len_son.append(i["verse"])
    await message.answer(f"""  {message.text[2::]} surasi {len_son[-1]} ta oyatdan iborat

o'qimoqchi bo'lgan oyatingizning raqamini kiriting

yoki ko'proq oyat o'qimoqchi bo'lsangiz oyatlarni quyidagi ko'rinishda kiriting

➡️  2.5.12.{len_son[-1]} ....

Yoki

➡️  1-5 ko'rinishida xabar jo'nating

Suraning barcha oyatlarni o'qish uchun 1-{len_son[-1]} deb xabar jo'nating  """)
    await state.update_data(data={"quran_name":quran_name})
    await state.update_data(data={"name_sura":name_sura})
    await state.update_data(data={"len_son":len_son[-1]})
    await Oyat_gurup.verse_son.set() 
      


@dp.message_handler(state=Oyat_gurup.verse_son)
async def make_quron(message:types.Message,state: FSMContext):
    data = await state.get_data()
    quron_name = data.get("quran_name") 
    name_sura = data.get("name_sura")
    len_son = data.get("len_son")
    if message.text.__contains__("-"):
        verse = message.text.split("-")
        boshi = verse[0]
        oxiri = verse[1]
        if len(verse) == 2 and verse[0].isdigit() and verse[1].isdigit() and boshi < oxiri:
            
            url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json'
            respons = requests.get(url=url).json()
            son = respons["quran"]
            for i in son:
                if i["chapter"] == quron_name:
                    for n in range(int(boshi),int(oxiri)+1):
                        if i['verse'] == n: 
                            await message.answer(f"{name_sura} surasi {i['verse']}-oyat\n\n{i['text']}",reply_markup=back_button)
            
        else:
             await message.answer("Noto'g'ri kiritingiz qayta kiriting!")


    elif message.text.isdigit() and len(message.text) >= 1 and int(message.text) <= len_son or message.text.__contains__("."):
            boshi = message.text.split(".")
            url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json'
            respons = requests.get(url=url).json()
            son = respons["quran"]
            for n in boshi:
                for i in son:
                    if i["chapter"] == quron_name:
                            if i['verse'] == int(n): 
                                await message.answer(f"{name_sura} surasi {i['verse']}-oyat\n\n{i['text']}",reply_markup=back_button)
                                
                                          
    else:
        await message.answer(f"{name_sura} surasida {len_son} oyat bor qayta kiriting !!!")
    


     





