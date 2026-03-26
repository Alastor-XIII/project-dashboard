import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def load_milestones():
    file = DATA_DIR / "milestones.xlsx"

    if file.exists():
        return pd.read_excel(file)
    else:
        return pd.DataFrame({
            "ProjectID": ["P001"],
            "Milestone": ["Sample Milestone"],
            "Date": ["2026-01-01"],
            "Responsible": ["Manager"]
        })
