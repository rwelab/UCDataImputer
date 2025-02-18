# 🏥 UCDataImputer - Clinical Data Processing & MAYO Score Calculation

**UCDataImputer** is a Python package designed to **compute MAYO scores from simple clinical data**. It validates patient records, maps clinical values correctly, and allows both **command-line execution and Python integration**.

---

## **📦 Installation**
🚧 *We haven't uploaded the package to PyPI yet* 🚧  
Once available, you can install it using:

```sh
pip install UCDataImputer
```

For now, you can install directly from GitHub:

```sh
pip install git+https://github.com/rwelab/UCDataImputer.git
```

---

## **🚀 How To Use?**
### **1️⃣ Run as a Command-Line Tool**
After installation, you can execute the package from the terminal:

```sh
UCDataImputer --input path/to/input.csv --output path/to/output.csv
```

**Example:**
```sh
UCDataImputer --input ~/Desktop/synthetic_data.csv --output ~/Desktop/mayo_scores_output.csv
```

This processes the **input CSV** and saves the **MAYO scores** to the output file.

---

### **2️⃣ Use in Python Scripts**
You can also **import and use it within Python**:

```python
from UCDataImputer.main import main

# Run with input and output file paths
main("input.csv", "output.csv")
```

---

## **📝 Expected Input Format**
The input **CSV file** must contain the following columns:

| Column Name      |                 Description                        |
|------------------|----------------------------------------------------|
| `AGE`            | Patient's age                                      |
| `BMI_kg/m2`      | Body Mass Index                                    |
| `HEIGHT_cm`      | Height in cm                                       |
| `WEIGHT_kg`      | Weight in kg                                       |
| `RACE`           | Patient's race (`White`, `Asian`, `Black`, `Other`)|
| `SEX`            | Biological sex (`M`, `F`)                          |
| `endoscopy`      | Mucosal appearance at endoscopy(`0`, `1`, `2`, `3`)|
| `stool_freq`     | Stool frequency (`0`, `1`)                         |
| `rectal_bleed`   | Rectal bleeding (`0`, `1`)                         |
| `SMOKING`        | Smoking status (`user`, `never`, `ex-user`)        |
| `crp`            | C-reactive protein level                           |
| `TREATMENT_PHASE`| Treatment phase (`0`, `1`, `2`)                    |

### **🔍 Endoscopy Scoring**
| Score |                              Description                                        |
|-------|---------------------------------------------------------------------------------|
| `0` | Normal or inactive disease                                                        |
| `1` | Mild disease (erythema, decreased vascular pattern, mild friability)              |
| `2` | Moderate disease (marked erythema, absent vascular pattern, friability, erosions) |
| `3` | Severe disease (spontaneous bleeding, ulceration)                                 |

### **🩺 Stool Frequency & Rectal Bleeding**
| Column        |              Description                 |
|--------------|-------------------------------------------|
| `stool_freq` | `0`: Normal, `1`: Abnormal                |
| `rectal_bleed` | `0`: No bleeding, `1`: Bleeding present |

### **⏳ Treatment Phases**
| Phase | Description |
|-------|-------------|
| `0` | 0-8 weeks of treatment |
| `1` | 8-52 weeks of treatment |
| `2` | 52+ weeks of treatment |

---

## **🧪 Example Output**
After running the script, the **output CSV** will include the calculated MAYO score:

| AGE | BMI_kg/m2 | HEIGHT_cm | ... | MAYO_score |
|-----|----------|----------|-----|------------|
| 34  | 24.5     | 175      | ... | 5.2        |
| 45  | 27.3     | 168      | ... | 6.1        |

---

## **💡 Features**
✅ **Validates patient data** to ensure correctness  
✅ **Maps clinical values to the correct format**  
✅ **Calculates MAYO scores based on validated clinical inputs**  
✅ **Works as both a CLI tool and a Python library**  

---

## **📄 License**
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## **📞 Contact**
For questions or issues, reach out via:
📧 **Email**: goktug.onal@ucsf.edu  
🔗 **GitHub Issues**: [Report a Bug](https://github.com/rwelab/UCDataImputer/issues)

---

## **📌 TODO**
🔹 Upload to PyPI  

```

---
