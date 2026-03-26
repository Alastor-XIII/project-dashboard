import pandas as pd

def load_projects():
    return pd.read_excel("data/projects.xlsx")

def load_activities():
    return pd.read_excel("data/activities.xlsx")

def load_milestones():
    return pd.read_excel("data/milestones.xlsx")

def load_resources():
    return pd.read_excel("data/resources.xlsx")
