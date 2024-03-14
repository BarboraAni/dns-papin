from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description="Cook some delicious DNS packets.")
    parser.add_argument("--config", required=True, type=str)
    return parser.parse_args()


def read_file(path, delimiter=","):
    records = []
    try:
        with open(path, "r") as f:
            for line in f:
                line_ = line.strip("\n").split(delimiter)
                records.append((line_[0], line_[1]))
        return records
    except FileNotFoundError as exc:
        print(exc.strerror)
