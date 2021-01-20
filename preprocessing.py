"""
File: preprocessing.py
Class: CIS 422
Date: January 18, 2021
Team: The Nerd Herd
Head Programmer: Logan Levitre
Version 0.1.0

Overview: Preprocessing functions to be used with Time Series Data.
    -- Need second opinion for revision of header structure --
"""
import pandas as pd
import math


def read_from_file(input_file):
    """
    Function reads TimeSeries csv file and stores data
    as a DataFrame object
    :param input_file: file passed to function containing Time Series Data
    :return: returns DataFrame object
    """
    time_series = pd.read_csv(input_file)
    return time_series


def write_to_file(output_file, ts):
    """
    Takes Series and outputs the data into the output_file
    :param output_file: file to store data in
    :param ts: time_series to be stored
    :return: None
    """
    ts.to_csv(output_file)


def denoise(time_series):
    pass


def impute_missing_data(time_series):
    """
    Corrects missing data entries inside time_series
    takes value to the right and uses that as placeholder
    for the data missing - if multiple entries are missing - skip
    :param time_series: time series being updated
    :return: time series with filled in missing values
    """
    length = time_series.size
    for values in range(0,length):
        if values.isna():
            time_series[values].fillna(time_series[values+1])


def impute_outliers(time_series):
    pass


def longest_continuous_run(time_series):
    pass


def clip(time_series, starting_date, final_date):
    pass


def assign_time(time_series, start, increment):
    pass


def difference(time_series):
    pass


def scaling(time_series):
    pass


def standardize(time_series):
    pass


def logarithm(time_series):
    """
    scales the time series, all entries become log_10 values of initial
    values within the Time Series.
    :param time_series: time series values to be manipulates
    :return: returns scaled time series containing log_10 results of generates
            a version of previous values
    """
    length = time_series.size
    for idx in range(0, length):
        time_series[idx] = math.log10(time_series[idx])


def cubic_roots(time_series):
    """
    scales the time series where all entries are
    the cubic root of the initial values.
    :param time_series: time series to be manipulates
    :return: time series with entries being the cubic root of previous values
    """
    length = time_series.size
    for idx in range(0, length):
        time_series[idx] = math.pow(time_series[idx], 1/3)


def split_data(time_series, perc_training, perc_valid, perc_test):
    pass


def design_matrix(time_series, input_index, output_index):
    pass


def design__matrix(time_series, m_i, t_i, m_0, t_0):
    pass


def ts2db(input_file, perc_training, perc_valid, perc_test, input_index,
          output_index, output_file):
    pass
