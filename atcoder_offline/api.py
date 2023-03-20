import json


class API:
    """
    設定ファイルconfig/env.jsonからAPIキーなどを取得する
    """

    data = {}
    with open("config/env.json", mode="r") as f:
        data = json.load(f)

    @staticmethod
    def get_notion_token():
        """
        getter
        """
        return API.data["TOKEN_NOTION"]

    @staticmethod
    def get_notion_database_id():
        """
        getter
        """
        return API.data["DATABASE_ID"]

    @staticmethod
    def get_folder_id_from_color(color):
        """
        getter
        """
        return API.data["COLOR_TO_DIR"][color]

    @staticmethod
    def get_tag_from_color(color):
        """
        getter
        """
        return API.data["COLOR_TO_TAG"][color]

    @staticmethod
    def get_url_atcoder_problem():
        """
        getter
        """
        return API.data["URL_ATCODER_PROBLEM"]

    @staticmethod
    def get_url_notion():
        """
        getter
        """
        return API.data["URL_NOTION"]

    @staticmethod
    def get_folder_id():
        """
        getter
        """
        return API.data["FOLDER_ID"]
