## req library

import os
import scipy as sc
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sqlalchemy import create_engine, text, inspect, Table, Column, Integer, String, MetaData, ForeignKey
from scipy.stats import chi2_contingency
from scipy.stats.contingency import association
from dotenv import load_dotenv
from scipy import stats

## All functions file

def age_group(row):
    if row < 18:
        return "teenager"
    elif row <35:
        return "young_adult"
    elif row <50:
        return "adult"
    elif row <65:
        return "old_adult"
    else:
        return "elder"
    
def hist_box_plot(df, check):
    for i in check:
        plt.figure(dpi=400, figsize=(20, 2))
        plt.subplot(1,2,1)
        print(f"----- DISPLAYING {i} ------------ ")
        sns.histplot(df, x=i)
        plt.subplot(1,2,2)
        sns.boxplot(df, x=i)
        plt.show()
        
def categorical_display(df, column_name):
    type1 = df[column_name].value_counts().reset_index()
    type1.columns = [column_name, 'count']  # Rename columns
    sns.barplot(data=type1, x=column_name, y='count', hue=column_name)
    plt.show()
    
def categorical_comparison(df, column_1, column_2):
    type1 = df.groupby([column_1])[column_2].mean().reset_index()

    type1.columns = [column_1,column_2]  # Rename columns
    type1
    sns.barplot(data=df, x=column_1, y=column_2, hue=column_1)
    plt.show()
    
def order_group(row):
    if row == "teenager":
        return 0
    elif row == "young_adult":
        return 3
    elif row == "adult":
        return 6
    elif row == "old_adult":
        return 9
    elif row == "elder":
        return 12
    else:
        return "error"
    
def order_gender(row):
    if row == "U":
        return 0
    elif row == "M":
        return 1
    elif row == "F":
        return 2
    else:
        return "error"
    
def clean_data(df, df_name):
    struct = {
        'client_id': [],
        'visit_id': [],
        'variation': [],
        'start_date': [],
        'step_1_date': [],
        'step_2_date': [],
        'step_3_date': [],
        'confirm_date': [],
        'error': [],  # Existing error field (for same step updates)
        'step_reversions': [],  # New field for counting step reversions
        'last_step': []  # New field to track the last completed step numerically
    }

    df_name = pd.DataFrame(struct)

    # Define a mapping for process steps to their corresponding date columns and numerical value
    process_mapping = {
        'start': ('start_date', 0),
        'step_1': ('step_1_date', 1),
        'step_2': ('step_2_date', 2),
        'step_3': ('step_3_date', 3),
        'confirm': ('confirm_date', 4)
    }

    # Iterate over the rows in df to update or append dates
    for index, row in df.iterrows():
        client_id = row['client_id']
        visit_id = row['visit_id']
        date_time = row['date_time']
        variation = row['Variation']
        process_step = row['process_step']

        # Initialize visit_id entry if not already present
        if visit_id not in struct['visit_id']:
            struct['visit_id'].append(visit_id)
            struct['variation'].append(variation)
            struct['client_id'].append(client_id)
            struct['error'].append(0)  # Start with 0 errors for duplicate updates
            struct['step_reversions'].append(0)  # Start with 0 step reversions
            struct['last_step'].append(-1)  # No step completed yet (-1)
            for key, _ in process_mapping.values():
                struct[key].append(pd.NaT)  # Initialize all date columns as NaT

        # Get the index for the visit_id in the structure
        current_index = struct['visit_id'].index(visit_id)

        # Update the appropriate date column based on process_step
        if process_step in process_mapping:
            date_column, step_number = process_mapping[process_step]

            # **Error Check (Same Step Update)**:
            # If the step already has a non-NaT value, it's an error (duplicate update)
            if not pd.isna(struct[date_column][current_index]):
                struct['error'][current_index] += 1  # Increment error for duplicate updates

            # **Step Reversion Check**:
            # If the current step is lower than the last_step, it's a step reversion
            if step_number < struct['last_step'][current_index]:
                struct['step_reversions'][current_index] += 1  # Increment step reversion

            # Update the date if it's NaT (don't overwrite existing values)
            if pd.isna(struct[date_column][current_index]):
                struct[date_column][current_index] = date_time

            # Update the last step with the highest step number reached so far
            struct['last_step'][current_index] = max(struct['last_step'][current_index], step_number)

    # Create a DataFrame from the structure
    df_name = pd.DataFrame(struct)

    return df_name

def tukeys_test_outliers(data, method="show"):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    
    # Define bounds for the outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Identify the outliers
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    
    if method== "show":
        return outliers
    
    elif method == "replace":
        median = data.median()
        data[outliers.index] = median
        return data
        
    elif method == "delete":
        index_drop = outliers.index
        data_no_outliers = data.drop(index_drop)
        
        return data_no_outliers
    

def ordered_grouped(row):
    if row == "start":
        return 0
    elif row == "step_1":
        return 100
    elif row == "step_2":
        return 200
    elif row == "step_3":
        return 300
    elif row == "confirm":
        return 400
    else:
        return "error"