from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

launch_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Launch GymHero",
        web_app=WebAppInfo(url="https://gym-hero-frontend.vercel.app/")
    )]
])