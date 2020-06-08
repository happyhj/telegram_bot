from telegram import init, 답문_보내기

def 메시지_다루기(text=""):
  print(f"[새로운 메시지 도착] {text}")
  답문_보내기(text)

init(
  text_callback=메시지_다루기
)