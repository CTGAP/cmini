import random
from discord import Message

RESTRICTED = False

def exec(message: Message):
    res = random.choices(
        population=['Heads', 'Tails', 'Mail'],
        weights=   [    .49,     .49,    .02],
        k=1
    )[0]

    return f'You got `{res}`!'
