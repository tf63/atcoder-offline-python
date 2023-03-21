from atcoder_offline import notion


def test_notion_post():
    notion.notion_post("abc212_a", "灰")


def test_notion_exist_data():
    assert notion.notion_exist_data("abc290_a") is True
    assert notion.notion_exist_data("afa") is False


def test_notion_get_from_status():
    notion.notion_get_from_status()


def test_notion_update_status():
    notion.notion_update_status()


if __name__ == "__main__":
    # test_notion_post()
    # test_notion_exist_data()
    # test_notion_get_from_status()
    test_notion_update_status()
