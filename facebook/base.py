from bot_service.resrc_service import get_facebook_user


class Facebook:
    def __init__(self, driver_type, driver_path, facebook_id):
        self.driver_type = driver_type
        self.driver_path = driver_path
        self.cookie = None
        self.facebook_id = facebook_id
        self.username = None
        self.action_script = None
        self.facebook_action_list = []

    def get_action_script(self):
        # get action list
        pass

    def exe_action_script(self):
        for action in self.facebook_action_list:
            # exc
            pass
        pass

    def update_status_to_server(self):
        pass

    def logging_account(self):
        pass

    def login(self):
        pass

    def logout(self):
        pass

    def export_cookie_to_file(self, save_path):
        pass

    def update_cookie_to_server(self):
        pass

    def get_facebook_user_account(self):
        data_user = get_facebook_user()
        if data_user['is_email']:
            self.username = data_user['email']
        else:
            self.username = data_user['phone']

        self.cookie = data_user['cookie']






