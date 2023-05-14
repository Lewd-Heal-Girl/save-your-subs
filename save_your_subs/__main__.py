import argparse

from . import cli

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sub", help="your little sub (r/your_sub)")
    
    parser.add_argument(
        '-e', '--export',
        action="store_true",
        help="Exports the downloaded backup, to a csv file."
    )

    args = parser.parse_args()

    cli(args.sub, export=args.export)
