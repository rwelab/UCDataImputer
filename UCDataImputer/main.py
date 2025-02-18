import pandas as pd
from GoktugTest.input_processing import ask_for_inputs_from_csv
from GoktugTest.model_selection import determine_model, load_model
from GoktugTest.mayo_score import calculate_mayo_score

def main(input_csv, output_csv):
    """
    Main function to process all rows from the input CSV and calculate MAYO scores.
    """
    # Load the input data
    input_data = pd.read_csv(input_csv)

    # Rename columns to match expected format
    input_data.rename(columns={
        'AGE': 'AGE',
        'BMI': 'BMI_kg/m2',
        'HEIGHT': 'HEIGHT_cm',
        'WEIGHT': 'WEIGHT_kg',
        'RACE': 'RACE',
        'SEX': 'SEX',
        'ENDSPS': 'endoscopy',
        'STOOLFRQ': 'stool_freq',
        'RECBLEED': 'rectal_bleed',
        'SMOKING': 'SMOKING',
        'CRP_mg/L': 'crp',  # Ensure lowercase for consistency
        'TREATMENT_PHASE': 'TREATMENT_PHASE'
    }, inplace=True)

    # Validate required columns
    required_columns = ['AGE', 'BMI_kg/m2', 'HEIGHT_cm', 'WEIGHT_kg', 'RACE', 'SEX', 'endoscopy', 
                        'stool_freq', 'rectal_bleed', 'SMOKING', 'crp', 'TREATMENT_PHASE']
    missing_columns = [col for col in required_columns if col not in input_data.columns]
    if missing_columns:
        raise ValueError(f"Input file is missing required columns: {missing_columns}")

    # Create a results DataFrame to store outputs
    results = input_data.copy()  # Copy the original data to include inputs
    results['MAYO_score'] = None  # Add a column for MAYO scores

    # Iterate over each row and process
    for index, row in input_data.iterrows():
        try:
            row_dict = row.to_dict()  # Convert the row to a dictionary
            inputs = ask_for_inputs_from_csv(row_dict)
            
            # Determine model and calculate MAYO score
            model_filename = determine_model(inputs)
            model = load_model(model_filename)
            mayo_score = calculate_mayo_score(inputs, model, model_filename)
            
            # Save the MAYO score and model filename in the results DataFrame
            results.at[index, 'MAYO_score'] = mayo_score
        except Exception as e:
            # Log the error in the results DataFrame for the corresponding row
            results.at[index, 'MAYO_score'] = f"Error: {e}"

    # Save the results to a new CSV file
    results.to_csv(output_csv, index=False)

    print(f"Results saved to {output_csv}")

if __name__ == '__main__':
    main()

