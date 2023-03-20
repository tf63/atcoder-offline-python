from atcoder_offline.api import API


def test_get_notion_token():
    assert API.get_notion_token() is not None
    print(API.get_notion_token())


def test_get_folder_id_from_color():
    assert API.get_folder_id_from_color is not None
    print(API.get_folder_id_from_color("灰"))


if __name__ == "__main__":
    test_get_notion_token()
    test_get_folder_id_from_color()
