from config import construct_config
from sender import Sender
from utils import parse_args, read_file


def main():
    args = parse_args()
    config = construct_config(args.config)
    records = read_file(config.file, config.delimiter)
    sender = Sender(config.target, config.port, records, config.thread_count)
    sender.run()


if __name__ == "__main__":
    main()
