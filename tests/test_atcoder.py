from atcoder_offline import atcoder


def test_get_difficulty():
    diff = atcoder.get_difficulty("abc293", ["a", "b", "c", "d", "e", "f"])
    print(diff)


if __name__ == "__main__":
    test_get_difficulty()
