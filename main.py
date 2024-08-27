import argparse
import sys
from utils import *
from rich import *
from beautifying import *
from terminal import *

def main():
    try:
        parser = argparse.ArgumentParser(description="Check if a GitHub repository link is valid.", add_help=False)
        parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit")
        parser.add_argument("-u", "--url", help="The GitHub repository URL to check")
        parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode")
        parser.add_argument("-f", "--file", action="store_true", help="Run in interactive mode")
        args = parser.parse_args()
        
        clear_terminal()
        welcome_banner()

        if args.help:
            display_help_in_panel(parser)
        elif args.interactive:
            interactive_mode(parser)
        elif args.url:
            try:
                if check_url(args.url):
                    analyze_repo(args.url)
                else:
                    rich_warning(f"The repository at {args.url} is not valid or does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}", file=sys.stderr)
                sys.exit(1)
        else:
            display_help_in_panel(parser)
    except KeyboardInterrupt:
        rich_warning("Operation cancelled by user")
        sys.exit(0)

if __name__ == "__main__":
    main()