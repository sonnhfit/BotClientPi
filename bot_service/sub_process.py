from config.action_config import FacebookAction
from facebook.base import Facebook

facebook_accout_run = {}


def run_facebook_process(message_data):
    global facebook_accout_run
    # phân tích action mà server gửi về rồi thực hiện nó
    if message_data["action"] == FacebookAction.LOGIN.value:
        cookie = message_data["data"]["cookie"]
        fb = Facebook(cookie=cookie)
        fb.login()
        fb_id = message_data["facebook_id"]
        facebook_accout_run[fb_id] = fb

    if message_data["action"] == FacebookAction.LOGOUT.value:
        fb_id = message_data["facebook_id"]
        fb = facebook_accout_run[fb_id]
        fb.logout()

    if message_data["action"] == FacebookAction.LIKE.value:
        try:
            id_post = message_data["data"]["id_post"]
            fb_id = message_data["facebook_id"]
            fb = facebook_accout_run[fb_id]
            fb.like_facebook_post_by_id(id_baiviet=id_post)
        except:
            cookie = message_data["data"]["cookie"]
            fb = Facebook(cookie=cookie)
            fb.login()
            fb_id = message_data["facebook_id"]
            facebook_accout_run[fb_id] = fb

            id_post = message_data["data"]["id_post"]
            fb_id = message_data["facebook_id"]
            fb = facebook_accout_run[fb_id]
            fb.like_facebook_post_by_id(id_baiviet=id_post)

    if message_data["action"] == FacebookAction.NEW_FEED.value:
        try:

            fb_id = message_data["facebook_id"]
            fb = facebook_accout_run[fb_id]
            if fb.flag == False:
                fb.flag = True
            else:
                fb.flag = False

            fb.new_feed_scoll(s=30)
        except:
            fb.new_feed_scoll(s=30)

    if message_data["action"] == FacebookAction.COMMENT.value:
        pass




def run_youtube_process():
    pass


def run_tiktok_process():
    pass
