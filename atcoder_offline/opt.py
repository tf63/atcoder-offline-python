import argparse


def get_opts():
    parser = argparse.ArgumentParser()

    # parameters
    parser.add_argument(
        "--prefix", required=True, type=str, help="contest type (e.g. abc)"
    )
    parser.add_argument("--begin", required=True, type=int)
    parser.add_argument("--end", required=True, type=int)
    parser.add_argument(
        "--problem",
        required=True,
        nargs="+",
        type=str,
        help="ダウンロードする問題を指定 (e.g. a b c d)",
    )

    parser.add_argument("--clear_done", action="store_true", default=False)

    return parser.parse_args()
