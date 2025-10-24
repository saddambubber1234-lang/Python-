# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 15:57:36 2025

@author: Malik
"""

import pandas as pd
import numpy as np

def prepare_m8_dataset():
    """
    Template function to prepare the M-8 dataset
    You would need to replace this with your actual data loading
    """
    # This is a template - replace with your actual data sources
    
    # Example structure of the required data
    data_structure = {
        'country': ['USA', 'China', 'India', 'Germany', 'Japan', 'UK', 'France', 'South Korea'],
        'year': list(range(2003, 2022)),  # 2003-2021
        'RETI': 'Renewable Energy Technology Innovations (from IRENA)',
        'DigEco': 'Digital Economy Index (PCA composite)',
        'FinS': 'Financial Structure Index (from World Bank GFD)',
        'Gov': 'Governance Index (from WGI)',
        'GDP': 'GDP per capita (constant 2015 US$)',
        'Ind': 'Tertiary industry value-added (% of GDP)',
        'MineralRents': 'Mineral resource rents (% of GDP)',
        'FinTech': 'Financial technology indicators'
    }
    
    print("Data structure required for the analysis:")
    for key, value in data_structure.items():
        print(f"{key}: {value}")
    
    return pd.DataFrame(data_structure)

# Data sources as mentioned in the paper:
def get_data_sources():
    """
    Returns the data sources mentioned in the paper
    """
    sources = {
        'RETI': 'International Renewable Energy Agency (IRENA)',
        'Digital Economy Indicators': 'World Bank (WDI), UN (ITU, EPI)',
        'Financial Structure': 'Global Financial Development (World Bank)',
        'Governance Indicators': 'Worldwide Governance Indicators (WGI)',
        'GDP and Industry Structure': 'World Bank (WDI)'
    }
    
    print("\nData Sources from the Paper:")
    for variable, source in sources.items():
        print(f"{variable}: {source}")

# Run data preparation info
get_data_sources()