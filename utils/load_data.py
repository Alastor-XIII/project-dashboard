import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_projects():
    return pd.read_excel(BASE_DIR / "data/projects.xlsx")

def load_activities():
    return pd.read_excel(BASE_DIR / "data/activities.xlsx")

def load_milestones():
    return pd.read_excel(BASE_DIR / "data/milestones.xlsx")

def load_resources():
    return pd.read_excel(BASE_DIR / "data/resources.xlsx")
