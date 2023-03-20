from atcoder_offline import atcoder


def test_get_difficulty():
    diff = atcoder.get_difficulty("abc293", ["a", "b", "c", "d", "e", "f"])
    print(diff)


def test_get_url_from_explain():
    url = atcoder.get_url_from_explain("abc293", "abc293_a")
    print(url)


if __name__ == "__main__":
    test_get_difficulty()
    test_get_url_from_explain()
