
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from zeep import Client, Settings
from zeep.transports import Transport


from requests import Session
import urllib3


import ssl
import certifi

import os
from dotenv import load_dotenv

load_dotenv()


router = Router()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://tracking.russianpost.ru/rtm34?wsdl'
session = Session()
session.verify = False
session.verify = certifi.where()
transport = Transport(session=session)
context = ssl.create_default_context(cafile=certifi.where())

client = Client(
    url,
    transport=transport,
    settings=Settings(strict=False, xml_huge_tree=True)
)


class TrackStates(StatesGroup):
    waiting_for_track_number = State()


@router.callback_query(lambda c: c.data == "create_order_btn")
async def create_order_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Пожалуйста пришлите ваш номер заказа ")

    await state.set_state(TrackStates.waiting_for_track_number)

    await callback.answer()


@router.message(TrackStates.waiting_for_track_number)
async def order_received(message: Message, state: FSMContext):
    track_number = message.text.strip()
    status = None

    try:
        print(f"Отправка запроса для трека: {track_number}")

        response = client.service.getOperationHistory(
            OperationHistoryRequest={
                'Barcode': track_number,
                'MessageType': 0,
                'Language': 'RUS'
            },
            AuthorizationHeader={
                'login': os.getenv('LOGIN_POST'),
                'password': os.getenv('PASS_POST')
            }
        )

        print(f"Получен ответ: {response}")

        if hasattr(response, 'OperationHistoryData'):
            history = response.OperationHistoryData.historyRecord
            if history:
                last_operation = history[-1].OperationParameters
                status = f"""
 Статус отправления {track_number}:
 Операция: {last_operation.OperType.Name}
 Дата: {last_operation.OperDate.strftime('%d.%m.%Y %H:%M')}
                """
            else:
                status = "Информация по этому трек-номеру не найдена"
        else:
            status = "Информация отправлена в терминал"

        if status:
            await message.answer(status)
        else:
            await message.answer("Произошла неизвестная ошибка при обработке запроса")

    except Exception as e:
        error_msg = f"Ошибка: {str(e)}"
        print(error_msg)
        await message.answer("Произошла ошибка при запросе к API Почты России")

    await state.clear()
