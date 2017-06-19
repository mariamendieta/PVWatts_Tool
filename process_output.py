import pandas as pd
import numpy as np

def populate_df(data, template=None):
    '''put data into pandas DataFrame using template if provided'''
    if template:
        df = pd.read_csv(template, header=0)
    else:
        df = pd.DataFrame()
    ac_kw = []
    for value in data['ac']:
        ac_kw.append(value/1000)
    df['AC (kW)'] = ac_kw
    return(df)

def kW_per_day(df):
    '''sum hourly data by day;
    only call after populate_df is called!'''
    summed_by_day = []
    for month in range(1,13):
        profile = df.loc[df['Month'] == month, :]
        for day in range(1,32):
            power = profile.loc[profile['Day'] == day, :]
            generation = power['AC (kW)'].sum()
            if generation:
                summed_by_day.append([month, day, generation])
    return(pd.DataFrame(summed_by_day, columns=['Month', 'Day', 'AC (kW)']))

def peak_days(df):
    '''select max, min, and med days);
    only call after populate_df AND kW_per_day are called!'''
    max_day = df.loc[df['AC (kW)'] == df['AC (kW)'].max(), :]
    min_day = df.loc[df['AC (kW)'] == df['AC (kW)'].min(), :]
    med_day = df.loc[df['AC (kW)'] == df['AC (kW)'].median(), :]
    return({'max': max_day, 'min': min_day, 'median': med_day})