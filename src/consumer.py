from faststream.rabbit import RabbitBroker
from datetime import datetime, timezone

from config import settings, bot

from schemas.messages import OutgoingMessage


broker = RabbitBroker(
    url=f"amqp://{settings.rabbitmq.rabbitmq_user}:{settings.rabbitmq.rabbitmq_password}@{settings.rabbitmq.rabbitmq_host}:{settings.rabbitmq.rabbitmq_port}/"
)

@broker.subscriber(settings.rabbitmq.queue_outgoing)
async def handle_telegram_messages(
        message: OutgoingMessage
):
    # Текущее время в UTC
    current_time = datetime.now(timezone.utc)
    past_time = datetime.fromisoformat(message.date)
    time_difference = current_time - past_time

    print(f"Время: {time_difference}")
    print(message)

    # await bot.send_message(message.chat_id, message.text)
