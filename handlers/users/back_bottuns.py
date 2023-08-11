from loader import db, dp
from aiogram import types
from keyboards.default.oyat_button import oyat_button 
from aiogram.dispatcher import FSMContext
from states.Oyat_state import Oyat_gurup

@dp.message_handler(text="⬅️Orqaga",state=Oyat_gurup.verse_son)
async def back_bottuns(message: types.Message,state:FSMContext):
     await message.answer("Siz orqaga qaytingiz!",reply_markup=oyat_button())
     await Oyat_gurup.quran_name.set()