from aiogram import Router, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command

router = Router()

# Comando que envía el mensaje con botones
@router.message(Command(commands=["cmds", "start"]))
async def cmds_handler(msg: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="𝑮𝑨𝑻𝑬𝑺", callback_data="show_cmds"),
            InlineKeyboardButton(text="𝑻𝑶𝑶𝑳𝑺", callback_data="tools")
        ]
    ])
    photo_url = "https://imgur.com/a/8Zxhoug.jpg"
    await msg.answer_photo(photo_url, caption="📜 WELCOME!!", reply_markup=keyboard)

# Callback que edita el mensaje original
@router.callback_query(F.data == "show_cmds")
async def show_cmds_callback(callback: types.CallbackQuery):
    await callback.message.edit_caption(
        caption=(
        "★-★-★-★-★-★-★-★-★-★-★\n"
        "⟨⟨ *Stripe Auth* ⟩⟩\n"
        "⟨⟨ *Status:* On ✅ ⟩⟩\n"
        "⟨⟨ *Use:* /auth CC|M|Y|CVV ⟩⟩\n"
        "★-★-★-★-★-★-★-★-★-★-★\n"
        "⟨⟨ *Square* ⟩⟩\n"
        "⟨⟨ *Status:* off 🚫⟩⟩\n"
        "⟨⟨ *Use:* /sq CC|M|Y|CVV ⟩⟩\n"
        "★-★-★-★-★-★-★-★-★-★-★\n"
        ),
        parse_mode="Markdown",
        reply_markup=None  # Quita los botones después
    )
    await callback.answer()  # Para evitar el "loading..." eterno