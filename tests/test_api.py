import atcoder_offline
from atcoder_offline import api


def test_folder_id():
    assert api.get_folder_id() is not None
    print(api.get_folder_id())


if __name__ == "__main__":
    test_folder_id()
