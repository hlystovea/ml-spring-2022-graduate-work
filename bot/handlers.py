import io
import time

from aiogram import Dispatcher, types


async def processing_image(image):
    start = time.time()
    # write the processing code here
    return image, time.time() - start


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
    image = io.BytesIO()
    await message.photo[-1].download(destination_file=image)
    upscale_image, elapsed_time = await processing_image(image)
    await message.answer_photo(
        photo=upscale_image,
        caption=f'Затраченное время: {elapsed_time:+.3f} с',
        disable_notification=True,
    )
