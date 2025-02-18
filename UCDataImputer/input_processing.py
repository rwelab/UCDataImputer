import pandas as pd

def ask_for_inputs_from_csv(data_row):
    """
    Process inputs from a row of CSV data.
    Returns a dictionary with the available features.
    """

    def get_valid_input(value, validation_func, allow_blank=False):
        """
        Validates a given value using the provided function.
        """
        if pd.isna(value):  # Handle NaN values (e.g., missing data in CSV)
            value = ""  # Treat as blank input
        else:
            value = str(value).strip()  # Convert to string and strip whitespace
        
        # Convert float-like values to integers (e.g., 3.0 -> 3)
        if value.replace('.', '', 1).isdigit() and '.' in value:
            value = str(int(float(value)))

        print(f"Validating input: {value},{validation_func}" )  # Debugging line

        if allow_blank and value == "":
            return None  # Allow blank input
        if validation_func(value):
            return value
        else:
            raise ValueError("Validation failed.", value, validation_func)  # Raise an error for invalid input

    def get_valid_crp(value):
        """
        Validates the CRP input.
        """
        value = str(value).strip()  # Convert to string and strip
        if value == "":
            return None  # Allow blank input
        elif ',' in value:
            raise ValueError("CRP value should use a period (.) instead of a comma (,).")
        elif is_valid_number(value):
            return value
        else:
            raise ValueError("CRP must be a valid number.")

    # Validation functions
    def is_valid_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def is_valid_integer(value):
        return value.isdigit()

    def is_valid_race(value):
        valid_races = {'White', 'Asian', 'Black', 'Other', 'Caucasian'}
        return value.lower().title() in valid_races

    def is_valid_sex(value):
        return value.upper() in ['F', 'M', 'MALE', 'FEMALE']

    def is_valid_smoking(value):
        return value.lower().strip() in {'user', 'never', 'ex', 'ex-user', 'never used', 'n'}

    def is_valid_endoscopy(value):
        return value in {'0', '1', '2', '3'}

    def is_valid_binary(value):
        return value in {'0', '1'}

    def is_valid_treatment_phase(value):
        return value in {'0', '1', '2'}

    # Process each input
    try:
        age = get_valid_input(data_row['AGE'], is_valid_number)
        bmi = get_valid_input(data_row['BMI_kg/m2'], is_valid_number)
        height = get_valid_input(data_row['HEIGHT_cm'], is_valid_number)
        weight = get_valid_input(data_row['WEIGHT_kg'], is_valid_number)
        race = get_valid_input(data_row['RACE'], is_valid_race)
        sex = get_valid_input(data_row['SEX'], is_valid_sex)
        smoking = get_valid_input(data_row['SMOKING'], is_valid_smoking)

        endoscopy = get_valid_input(data_row.get('endoscopy', ""), is_valid_endoscopy, allow_blank=True)
        stool_freq = get_valid_input(data_row.get('stool_freq', ""), is_valid_binary, allow_blank=True)
        rectal_bleed = get_valid_input(data_row.get('rectal_bleed', ""), is_valid_binary, allow_blank=True)

        crp = get_valid_crp(data_row.get('crp', ""))
        treatment_phase = get_valid_input(data_row['TREATMENT_PHASE'], is_valid_treatment_phase)

        # Map smoking input
        smoking_mapping = {
            "user": "SMOKING_USER",
            "never": "SMOKING_NEVER USED",
            "ex": "SMOKING_EX-USER",
            "ex-user": "SMOKING_EX-USER",
            "neverused": "SMOKING_NEVER USED",
            "n": "SMOKING_NEVER USED"
        }
        smoking = smoking_mapping.get(smoking.lower())
    
        # Map smoking input
        sex_mapping = {
            "female": "F",
            "male": "M"
        }
        sex = sex_mapping.get(sex.lower())

        # Map race input
        race_mapping = {
            "caucasian": "White"
        }
        race = race_mapping.get(race.lower())

        # Construct the inputs dictionary
        inputs = {
            'AGE': age,
            'BMI_kg/m2': bmi,
            'HEIGHT_cm': height,
            'WEIGHT_kg': weight,
            'RACE': race.title(),
            'SEX': sex.upper(),
            'SMOKING': smoking,
            'endoscopy': endoscopy if endoscopy else None,
            'stool_freq': stool_freq if stool_freq else None,
            'rectal_bleed': rectal_bleed if rectal_bleed else None,
            'crp': crp if crp else None,
            'TREATMENT_PHASE': treatment_phase
        }

        # Remove keys with None values
        inputs = {k: v for k, v in inputs.items() if v is not None}
        return inputs
    except Exception as e:
        raise ValueError(f"Row error: {e}")
