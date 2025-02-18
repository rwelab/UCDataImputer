from GoktugTest.model_selection import adjust_features_based_on_model
import pandas as pd

def calculate_mayo_score(inputs, model, model_filename):
    """
    Use the model to calculate the MAYO score based on the inputs.
    Parameters:
    - inputs: The dictionary of patient inputs.
    - model: The machine learning model to use for prediction.
    - model_filename: Name of the model to determine relevant features.
    Returns:
    - The predicted MAYO score.
    """
    # Convert inputs to a DataFrame for one-hot encoding
    input_df = pd.DataFrame([inputs])

    input_df.to_csv('input_df_columns.csv')

    # Apply one-hot encoding for categorical columns without adding prefixes
    input_df = pd.get_dummies(input_df, 
                              columns=['RACE', 'SEX', 'SMOKING'], 
                              prefix='', 
                              prefix_sep='')

    # Use DataFrame.map for specific columns that need conversion
    input_df = input_df.apply(lambda col: col.map(lambda x: int(x) if isinstance(x, bool) else x) if col.dtypes == 'bool' else col)

    input_df.to_csv('input_df.csv')

    # Define the full list of features in the correct order (as expected by the model)
    model_features = [
        'ENDSPS', 'AGE', 'CRP_mg/L', 'BMI_kg/m2', 'HEIGHT_cm', 'WEIGHT_kg', 'STOOLFRQ_score', 'RECBLEED_score', 
        'RACE_Asian', 'RACE_Black', 'RACE_Others', 'RACE_White', 'SEX_F', 'SEX_M', 'SMOKING_EX-USER', 
        'SMOKING_NEVER USED', 'SMOKING_USER', 'TREATMENT_PHASE'
    ]

    # Rename columns to match adjusted features (if necessary)
    rename_mapping = {
        'crp': 'CRP_mg/L',
        'stool_freq': 'STOOLFRQ_score',
        'rectal_bleed': 'RECBLEED_score',
        'endoscopy': 'ENDSPS',
        'SEX_Male': 'SEX_M',
        'Male': 'SEX_M',
        'M': 'SEX_M',
        'SEX_Female': 'SEX_F',
        'Female': 'SEX_F',
        'F': 'SEX_F',
        'm': 'SEX_M',
        'f': 'SEX_F',
        'White': 'RACE_White',
        'Black': 'RACE_Black',
        'Asian': 'RACE_Asian',
        'Other': 'RACE_Others',
        'white': 'RACE_White',
        'black': 'RACE_Black',
        'asian': 'RACE_Asian',
        'other': 'RACE_Others'
    }
    input_df.rename(columns=rename_mapping, inplace=True)

    # Adjust features based on the model being used
    adjusted_features = adjust_features_based_on_model(model_features, model_filename)

    # Filter input DataFrame to keep only adjusted features, filling missing features with 0
    filtered_df = input_df.reindex(columns=adjusted_features, fill_value=0)
    filtered_df.to_csv('filtered_df.csv')

    # Calculate the MAYO score using the provided model
    mayo_score = model.predict(filtered_df)

    return mayo_score[0]  # Return the predicted score

