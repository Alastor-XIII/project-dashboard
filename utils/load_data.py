import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def load_projects():
    return pd.read_excel(DATA_DIR / "projects.xlsx")

def load_activities():
    return pd.read_excel(DATA_DIR / "activities.xlsx")

def load_milestones():
    return pd.read_excel(DATA_DIR / "milestones.xlsx")

def load_resources():
    return pd.read_excel(DATA_DIR / "resources.xlsx")
