import aiohttp

import requests


class Api:
    def __init__(self, server_address):
        self.bot_api_address = f"http://{server_address}/"

        # 传递Api类的实例引用
        self.botSelfInfo = self.BotSelfInfo(self)
        self.privateService = self.PrivateService(self)
        self.groupService = self.GroupService(self)

    class BotSelfInfo:
        def __init__(self, api_instance):
            self.api = api_instance  # 保存对Api类实例的引用

        def get_login(self):
            """
            获取bot服务端是否在线
            :return: bot服务端返回的信息
            """
            response = requests.get(self.api.bot_api_address)
            return response.text

        def get_login_info(self):
            """
            获取bot自身的登录信息
            :return: bot的QQ号和昵称
            """
            response = requests.get(self.api.bot_api_address + "get_login_info")
            return response.json()

    class PrivateService:
        def __init__(self, api_instance):
            self.api = api_instance  # 保存对Api类实例的引用

        def send_private_msg(self, user_id, message):
            params = {
                "user_id": user_id,
                "message": message
            }
            response = requests.post(self.api.bot_api_address + "send_private_msg", params=params)
            return response.json()

    class GroupService:
        def __init__(self, api_instance):
            self.api = api_instance  # 保存对Api类实例的引用

        def get_group_member_list(self, group_id):
            params = {
                "group_id": group_id
            }
            response = requests.post(self.api.bot_api_address + "get_group_member_list", params=params)
            return response.json()

        def send_group_msg(self, group_id, message):
            params = {
                "group_id": group_id,
                "message": message
            }
            response = requests.post(self.api.bot_api_address + "send_group_msg", params=params)
            return response.json()

        def set_group_ban(self, group_id, user_id, duration):
            params = {
                "group_id": group_id,
                "user_id": user_id,
                "duration": duration  # 禁言时长，单位为秒
            }
            response = requests.post(self.api.bot_api_address + "set_group_ban", params=params)
            return response.json()

        def set_group_kick(self, group_id, user_id):
            params = {
                "group_id": group_id,
                "user_id": user_id,
            }
            response = requests.post(self.api.bot_api_address + "set_group_kick", params=params)
            return response.json()

        def delete_msg(self, message_id):
            params = {
                "message_id": message_id,
            }
            response = requests.post(self.api.bot_api_address + "delete_msg", params=params)
            return response.json()

        def set_group_add_request(self, flag, approve="true", reason=""):
            params = {
                "flag": flag,
                "sub_type": "add",
                "approve": approve,
                "reason": reason
            }
            response = requests.post(self.api.bot_api_address + "set_group_add_request", params=params)
            return response.json()

        def get_group_info(self, group_id):
            params = {
                "group_id": group_id
            }
            response = requests.post(self.api.bot_api_address + "get_group_info", params=params)
            return response.json()

    class MessageService:
        def __init__(self, api_instance):
            self.api = api_instance  # 保存对Api类实例的引用

        def get_msg(self, message_id):
            params = {
                "message_id": message_id,
            }
            response = requests.post(self.api.bot_api_address + "get_msg", params=params)
            return response.json()
