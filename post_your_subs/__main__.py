import argparse

from . import cli

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sub", help="your little sub (r/your_sub)")

    args = parser.parse_args()

    cli(args.sub)
