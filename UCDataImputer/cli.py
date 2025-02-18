import argparse
from UCDataImputer.main import main

def cli():
    """
    Command-line interface for processing the input CSV and saving MAYO scores.
    """
    parser = argparse.ArgumentParser(description="Process a CSV file and calculate MAYO scores.")
    parser.add_argument("--input", required=True, help="Path to the input CSV file")
    parser.add_argument("--output", required=True, help="Path to save the output CSV file")
    
    args = parser.parse_args()
    main(args.input, args.output)

if __name__ == "__main__":
    cli()
