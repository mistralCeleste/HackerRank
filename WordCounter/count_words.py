from word_counter import WordCounter
import argparse


def assign_and_parse_arguments() -> argparse.Namespace:
    description = \
        (
            'Counts the number of words in from a file and outputs it to a file with each count,'
            'while preserving the original order.'
        )
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--input', metavar='i', type=str, help='Input file to count from')
    parser.add_argument('--output', metavar='o', type=str, help='output file to write counts to')
    args = parser.parse_args()
    return args


def main() -> None:
    args = assign_and_parse_arguments()
    WordCounter.count_words(args.input, args.output)


if __name__ == "__main__":
    main()
