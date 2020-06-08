import requests
import os
from time import sleep

token = os.getenv('TOKEN')
chat_id = None

def getRecentMsg():
  updateURL = f'https://api.telegram.org/bot{token}/getUpdates'
  updates = requests.get(updateURL).json()

  # 가장 최근 메시지만 선택
  recent_msg = updates["result"][-1]["message"]
  return recent_msg

def 답문_보내기(text):
  sendURL = f'https://api.telegram.org/bot{token}/sendMessage'
  updates = requests.get(
    sendURL,
    params= {"chat_id": chat_id, "text": text}
  )

def sendReaction(chat_id):
  sendURL = f'https://api.telegram.org/bot{token}/sendPhoto'
  updates = requests.get(
    sendURL,
    params= {"chat_id": chat_id, "photo": "https://lh3.googleusercontent.com/proxy/o47vvw1Pzt4NapQ5fYP5B7EXG56240NBhnDxikSlEHJfns-_elDQ9B9z0UBOprWAPOQM_pCjzWLtGYZg-9iynWOtM0YgyY60T7Monyf3iCKYQIgOD5VkYroNRDNc8eoJy0xml4tzjM4sbC71rQ2sca4pVFxwx0M74Dx0CNJlDQa6gbVz0z4g0dPQFx3Jh8kQ"}
  )

def init(text_callback):
  global chat_id
  recent_msg_id = None

  while True:
    sleep(1)
    # 가장 최근 메시지만 선택
    recent_msg = getRecentMsg()

    # 이미 응답을 보낸 메시지 인지 체크
    if recent_msg_id == recent_msg["message_id"]:
      continue
    # 새로운 메시지 라면 응답을 보내기 
    recent_msg_id = recent_msg["message_id"]
    chat_id=recent_msg["chat"]["id"]
    if "text" in recent_msg:
      text_callback(recent_msg["text"])
    else:
      text_callback()

    
