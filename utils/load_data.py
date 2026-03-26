import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_projects():
    return pd.read_csv(BASE_DIR / "data/projects.csv")

def load_activities():
    return pd.read_csv(BASE_DIR / "data/activities.csv")

def load_milestones():
    return pd.read_csv(BASE_DIR / "data/milestones.csv")

def load_resources():
    return pd.read_csv(BASE_DIR / "data/resources.csv")
