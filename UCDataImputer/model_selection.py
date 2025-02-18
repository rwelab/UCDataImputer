import pandas as pd
import joblib

def determine_model(inputs):
    """
    Determine which model to use based on the inputs available.
    
    Returns the filename of the model to be used.
    """
    def is_valid_input(value):
        """
        Check if the value is valid (not None, empty string, or NaN).
        """
        if isinstance(value, str) and value.strip().lower() == "nan":
            return False  # Handle string 'nan'
        return value not in [None, ""] and not pd.isna(value)

    # Evaluate presence of key inputs
    has_crp = is_valid_input(inputs.get('crp'))
    has_endoscopy = is_valid_input(inputs.get('endoscopy'))
    has_stool_freq = is_valid_input(inputs.get('stool_freq'))
    has_rectal_bleed = is_valid_input(inputs.get('rectal_bleed'))

    # Debugging output
    print(f"Raw crp value: {inputs.get('crp')}, Type: {type(inputs.get('crp'))}")

    # Model selection logic
    if has_crp and has_endoscopy and has_stool_freq and has_rectal_bleed:
        model_filename = 'crp + demo + stool + rec + endsps'
    elif has_crp and has_endoscopy and has_stool_freq:
        model_filename = 'crp + stool + demo + endsps'
    elif has_crp and has_endoscopy and has_rectal_bleed:
        model_filename = 'crp + rec + demo + endsps'
    elif has_crp and has_stool_freq and has_rectal_bleed:
        model_filename = 'crp + demo + stool + rec'
    elif has_crp and has_rectal_bleed:
        model_filename = 'crp + demo + rec'
    elif has_crp and has_stool_freq:
        model_filename = 'crp + demo + stool'
    elif has_crp and has_endoscopy:
        model_filename = 'crp + demo + endsps'
    elif has_endoscopy and has_stool_freq and has_rectal_bleed:
        model_filename = 'demo + stool + rec + endsps'
    elif has_endoscopy and has_rectal_bleed:
        model_filename = 'demo + rec + endsps'
    elif has_stool_freq and has_rectal_bleed:
        model_filename = 'demo + stool + rec'
    elif has_endoscopy and has_stool_freq:
        model_filename = 'demo + stool + endsps'
    elif has_stool_freq:
        model_filename = 'demo + stool'
    elif has_endoscopy:
        model_filename = 'demo + endsps'
    elif has_crp:
        model_filename = 'crp + demo'
    elif has_rectal_bleed:
        model_filename = 'demo + rec'
    else:
        raise ValueError("Insufficient information to choose a model.")
    
    # Add the treatment phase to the model filename like 0, 1, 2
    model_filename += f' Phase {inputs["TREATMENT_PHASE"]}.pkl'
    #model_filename += '.pkl'
    model_filename = 'models/' + model_filename

    print('/'*100 ,model_filename)

    return model_filename

def load_model(model_filename):
    """
    Load the machine learning model from the given filename.
    """
    model_path = (model_filename)
    if not (model_path):
        raise FileNotFoundError(f"Model file {model_filename} not found.")

    return joblib.load(model_path)


def adjust_features_based_on_model(model_features, model_filename):
    """
    Adjust the model features based on the model filename by keeping only relevant features.
    Parameters:
    - model_features: List of all possible features in the correct order.
    - model_filename: The filename of the model being used.
    
    Returns:
    - List of relevant features in the same order as model_features.
    """
    # Keywords to identify relevant features from the model filename
    keywords_to_features = {
        'crp': ['CRP_mg/L'],
        'stool': ['STOOLFRQ_score'],
        'rec': ['RECBLEED_score'],
        'endsps': ['ENDSPS'],
        'demo': ['AGE', 'BMI_kg/m2', 'HEIGHT_cm', 'WEIGHT_kg', 
                 'RACE_Asian', 'RACE_Black', 'RACE_Others', 'RACE_White', 
                 'SEX_F', 'SEX_M', 'SMOKING_EX-USER', 'SMOKING_NEVER USED', 'SMOKING_USER']
    }

    # Determine relevant features based on keywords in the model filename
    relevant_features = set()
    for keyword, features in keywords_to_features.items():
        if keyword.lower() in model_filename.lower():  # Case-insensitive matching
            relevant_features.update(features)

    # Always include 'TREATMENT_PHASE' since it is present in every model
    relevant_features.add('TREATMENT_PHASE')

    # Filter the model_features list to keep only relevant features, maintaining the original order
    adjusted_features = [feature for feature in model_features if feature in relevant_features]

    return adjusted_features
