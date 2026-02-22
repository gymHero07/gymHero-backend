from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

launch_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Launch ValhallaRunner",
        web_app=WebAppInfo(url="https://runner-frontend.vercel.app/")
    )]
])