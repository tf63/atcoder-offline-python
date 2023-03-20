import atcoder_offline
from atcoder_offline import api


def test_env():
    assert api.get_env() is not None
    print(api.get_env())


if __name__ == "__main__":
    test_env()
