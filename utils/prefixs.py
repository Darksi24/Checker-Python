from aiogram.filters import Filter
from aiogram.types import Message

class CustomCommand(Filter):
    def __init__(self, name: str, prefixes: tuple = ("/", ".", "!", "?", "$")):
        self.name = name.lower()
        self.prefixes = prefixes

    async def __call__(self, message: Message) -> bool:
        if not message.text:
            return False
        text = message.text.strip()
        if text.startswith(self.prefixes):
            command = text[1:].split()[0].lower()
            return command == self.name
        return False