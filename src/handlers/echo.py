from aiogram.types import Message

from consumer import broker

from config import settings


async def echo_handler(message: Message) -> None:
    try:
        await broker.publish(
            queue=settings.rabbitmq.queue_incoming,
            message={
                "chat_id": message.chat.id,
                "user_id": message.from_user.id,
                "user_name": message.from_user.full_name,
                "text": message.text,
                "date": message.date,
            }
        )
    except Exception as e:
        await message.answer(f"Error send message: {e}")
