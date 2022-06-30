import asyncio
import io
import time

import numpy as np
from aiogram import Dispatcher, types
from PIL import Image

from utils import predict_hr_image, SRGANNet


async def processing_image(image):
    start = time.time()
    loop = asyncio.get_running_loop()
    hr_image = await loop.run_in_executor(
        None, predict_hr_image, SRGANNet, image)
    return hr_image, time.time() - start


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(image_file_handler, content_types=['photo'])


async def start(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    text = 'Чтобы обработать изображение отправьте его в этот чат'
    await message.answer(
        text,
        parse_mode='Markdown',
        disable_notification=True,
    )


async def image_file_handler(message: types.Message):
    """
    This handler will be called when the user sends a Photo
    """
    original_file = io.BytesIO()
    proccesed_file = io.BytesIO()

    await message.photo[-1].download(destination_file=original_file)

    image = np.array(Image.open(original_file), dtype=np.float32)
    hr_image, elapsed_time = await processing_image(image)
    hr_image.save(proccesed_file, format='JPEG')

    await message.answer_photo(
        photo=proccesed_file.getvalue(),
        caption=f'Затраченное время: {elapsed_time:+.3f} с',
        disable_notification=True,
    )
