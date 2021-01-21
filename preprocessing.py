"""
File: preprocessing.py
Class: CIS 422
Date: January 20, 2021
Team: The Nerd Herd
Head Programmer: Logan Levitre
Version 0.1.01

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
    :return: returns DataFrame object declared time_series
    """
    time_series = pd.read_csv(input_file)
    return time_series


def write_to_file(output_file, ts):
    """
    --wrapper function--
    Takes Series and outputs the data into the output_file
    :param output_file: file to store data in
    :param ts: time_series to be stored
    :return: None
    """
    ts.to_csv(output_file)


def denoise(time_series):
    """
    Removes noise from a time series. Produces a time series with less noise than
    the original one.
    :param time_series: Time series data
    :return: returns a Time Series without noise
    """
    pass


def impute_missing_data(time_series):
    """
    Corrects missing data entries inside time_series
    takes value to the right and uses that as placeholder
    for the data missing - if multiple entries are missing - skip
    :param time_series: Time series data
    :return: time series with filled in missing values
    """
    # Possibly use .shape - Return a tuple representing the dimensionality of the DataFrame.
    for value in time_series:
        if value.isna():
            time_series[value].fillna(time_series[value + 1])


def impute_outliers(time_series):
    """
    Find and remove outliers within the Time series
    - similar to impute_missing_data functions -
    :param time_series: Time series data
    :return: concise Time series without outliers
    """
    pass


def longest_continuous_run(time_series):
    """
    Isolates the most extended portion of the time series without
    missing data.
    :param time_series: Time series data
    :return: a time series without any missing data or outliers
    """
    pass


def clip(time_series, starting_date, final_date):
    """
    clips the time series to the specified period’s data.
    :param time_series: Time series data
    :param starting_date: first day to be included in new TS
    :param final_date: last date to be included in  new TS
    :return: a portion of the time series from start_date to final_date
    """
    pass


def assign_time(time_series, start, increment):
    """
    If we do not have the times associated with a sequence of readings.
    Start at a specific time and increment for the following entry.
    :param time_series: Time series data
    :param start: beginning of the timestamp
    :param increment: difference to add to next timestamp
    :return: time_series with timestamps assigned to each entry
    """
    pass


def difference(time_series):
    """
    Takes the time series data and transforms each entry
    as the difference between it and the next entry
    :param time_series: Time series data
    :return: time series containing the difference between each original entry
    """
    pass


def scaling(time_series):
    """
    Produces a time series whose magnitudes are scaled so that the resulting
    magnitudes range in the interval [0,1].
    :param time_series: Time series data
    :return:
    """
    pass


def standardize(time_series):
    """
    Produces a time series whose mean is 0 and variance is 1.
    :param time_series: Time series data
    :return: a Time series with mean of 0/variance is 1
    """
    pass


def logarithm(time_series):
    """
    scales the time series, all entries become log_10 values of initial
    values within the Time Series.
    :param time_series: Time series data
    :return: returns scaled time series containing log_10 results of generates
     a version of previous values
    """
    for idx in time_series:
        time_series[idx] = math.log10(time_series[idx])


def cubic_roots(time_series):
    """
    scales the time series where all entries are
    the cubic root of the initial values.
    :param time_series: Time series data
    :return: time series with entries being the cubic root of previous values
    """
    for idx in time_series:
        # re-look at pandas API - access looks to be tuples not linear array ?
        time_series[idx] = math.pow(time_series[idx], 1 / 3)


def split_data(time_series, perc_training, perc_valid, perc_test):
    """
    Splits a time series into
    training, validation, and testing according to the given percentages.
    :param time_series: Time series data
    :param perc_training: percentage of time series data to be used for training
    :param perc_valid: percentage of time series data to be used for validation
    :param perc_test: percentage of time series data to be used for testing
    :return: multiple csv files holding training, valid, test values
    """
    pass


def design_matrix(time_series, input_index, output_index):
    """
    Creates a matrix of time series data
    :param time_series: Time series data
    :param input_index: Unknown as of 1/20
    :param output_index: Unknown as of 1/20
    :return: Matrix of time series data
    """
    pass


def design__matrix(time_series, m_i, t_i, m_0, t_0):
    """
    Creates a Matrix up to certain position of Time series
    depends on m_i & t_i
    :param time_series: Time series data
    :param m_i: magnitude at index I
    :param t_i: timestamp at index I
    :param m_0: magnitude of index 0
    :param t_0: timestamp of index 0
    :return: Matrix of time series data up to m_i & t_i
    """
    pass


def ts2db(input_file, perc_training, perc_valid, perc_test, input_index,
          output_index, output_file):
    """
    combines reading a file, splitting the
    data, converting to database, and producing the training databases.
    :param input_file: file to be read and split
    :param perc_training: percentage of data to be split into training data
    :param perc_valid: percentage of data to be split into valid data
    :param perc_test: percentage of the data to be split into test data
    :param input_index: initial index for matrix
    :param output_index: index to take data from
    :param output_file: file for data to be written into
    :return: multiple csv files and a matrix
    """
    pass
