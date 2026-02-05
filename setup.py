from setuptools import setup, find_packages

setup(
    name='my-telegram-bot',
    version='1.0.0',
    description='Мой телеграм бот для тестирования',
    install_requires=[
        'pyTelegramBotAPI==4.15.1',
    ],
    packages=find_packages(),
)
