import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json
import os
from facebook.base import Facebook
from config.action_config import TypeControl, WebsiteType
from bot_service.sub_process import run_facebook_process, run_youtube_process

fb = None


def on_message(ws, message):
    global fb
    print(message)
    jso = json.loads(message)

    if jso["type_control"] == TypeControl.APP.value:
        # điều khiển app ở đây

        if jso["app"] == WebsiteType.FACEBOOK.value:
            run_facebook_process(jso)

        if jso["app"] == WebsiteType.YOUTUBE.value:
            run_youtube_process()

        if jso["app"] == WebsiteType.TIKTOK.value:
            pass

    if jso["type_control"] == TypeControl.HARDWARE.value:

        # điều khiển phần cứng ở đây
        pass


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    pass


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8000/ws/chat/son/",
                                on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


a = """
{
  "type": 1,
  "app": "facebook",
  "action": 1,
  "facebook_id": "R123123123132"
  "data": {
    "cookie": "sonnh",
  }
}
data:
    id_post : id post dùng để like với action like 

"""


