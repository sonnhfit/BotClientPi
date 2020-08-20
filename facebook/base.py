
class Facebook:
    def __init__(self, driver_type, driver_path, cookie, facebook_id, username, action_script):
        self.driver_type = driver_type
        self.driver_path = driver_path
        self.cookie = cookie
        self.facebook_id = facebook_id
        self.username = username
        self.action_script = action_script
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




