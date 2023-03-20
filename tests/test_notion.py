from atcoder_offline import notion


def test_notion_post():
    notion.notion_post("abc212_a", "灰")


def test_notion_exist_data():
    assert notion.notion_exist_data("abc290_a") is True
    assert notion.notion_exist_data("afa") is False


if __name__ == "__main__":
    test_notion_post()
    test_notion_exist_data()
