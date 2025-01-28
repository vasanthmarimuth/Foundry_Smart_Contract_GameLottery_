import argparse


def center_text_in_box(text, width=30):
    """Center the provided text inside a box of specified width."""
    padding = (width - len(text)) // 2
    return f"{' ' * padding}{text}{' ' * (width - len(text) - padding)}"


def print_boxed_text(text, width=30):
    """Print the boxed text with the custom centered text, using asterisks ('*')."""
    top_bottom_border = '*' * width
    centered_text = center_text_in_box(text, width)
    print(f"/*{top_bottom_border}*/")
    print(f"/*{centered_text}*/")
    print(f"/*{top_bottom_border}*/")


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Print custom text in a centered box.")
    parser.add_argument('custom_text', type=str, help="The custom text to display.")
    return parser.parse_args()


def main():
    """Main entry point of the program."""
    args = parse_arguments()
    print_boxed_text(args.custom_text)


if __name__ == "__main__":
    main()
