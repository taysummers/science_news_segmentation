import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from database_col_names import *

def get_cluster_data(filepath, segment_variables = ['ENJOY', 'KNOWLEDGE', 'SCIOFTEN', 'TOPICS1']):
    '''
    Pipeline for reading, cleaning, and breaking data
    into total data and segmentation datasets used for building the segmentation
    and analyzing the segmentation solution.

    INPUTS
    ------
    filepath: A path to the csv data
    segment_variables: A list of variables to be used for segmentation

    OUTPUTS
    -------
    data: Pandas DataFrame holding the full, clean dataset
    scaled_data: Pandas DataFrame holding the clean and scaled dataset
    with only the relevant data used in building the segmentation.

    '''
    ## Reads in data from csv file
    data = pd.read_csv(filepath, index_col= 'CaseID')

    ## Filter Out Questionnaire Duration < 5 minutes
    data = data[data['duration'] >= 5]

    ## Labels not used in analysis
    labels_to_drop = ['duration', 'weight', 'HOBBY2_1', 'HOBBY2_2', 'HOBBY2_3',
                            'GREATPAST_OE1', 'GREATPAST_OE2', 'GREATPAST_OE3',
                            'GREATFUTURE_OE1', 'GREATFUTURE_OE2',
                            'GREATFUTURE_OE3','FAKE_OE1','FAKE_OE2', 'FAKE_OE3',
                           'DISAG_OE1', 'DISAG_OE2', 'DISAG_OE3',
                           'DECIS_OE1', 'DECIS_OE2', 'DECIS_OE3',
                           'tm_start', 'tm_finish',
                           'XSPANISH', 'PPT01_COL', 'PPT25_COL', 'PPT612_COL',
                            'PPT1317_COL', 'PPT18OV_COL',
                           'DOV_FORM', 'ppcm0160', 'DOV_ACSLANG', 'ppagect4',
                           'PPHHHEAD', 'ppreg9', 'AGE']

    data.drop(labels = labels_to_drop, axis = 1, inplace = True)

    # Groups the smaller work industries into 'Other' as 1.0
    data['IND1'] = data['IND1'].replace(to_replace = [17.0, 20.0, 3.0, 11.0,
                                    6.0, 21.0, 2.0, 13.0, 14.0], value = 1.0)

    # Groups HH Size >6 as 6
    data['PPHHSIZE'] = data['PPHHSIZE'].replace(to_replace = [6, 7, 8, 9, 10],
                                                value = 6)

    # Groups the income brackets into larger ranges
    data['PPINCIMP'] = data['PPINCIMP'].map({1: 1.0, 2: 1.0,
                    3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0,
                     7: 2.0, 8: 2.0, 9: 2.0, 10: 2.0,
                     11: 3.0, 12: 3.0,
                     13: 4.0, 14: 4.0,
                     15: 5.0, 16: 5.0,
                     17: 6.0, 18: 6.0,
                     19: 7.0, 20: 8.0,
                     21: 8.0})

    # Makes smaller age groupings
    data['ppagecat_short'] = data['ppagecat'].map({1: 1, 2: 1, 3: 2, 4: 2,
                                                    5: 3, 6: 3, 7: 4})

    # Groups Topic Int questions into Top 2 Box and Bottom 2 Box
    data['TOPICINT_a_t2b'] = data['TOPICINT_a'].map({1.0: 1, 2.0: 1,
                                                    3.0: 2, 4.0: 2})

    data['TOPICINT_b_t2b'] = data['TOPICINT_b'].map({1.0: 1, 2.0: 1,
                                                    3.0: 2, 4.0: 2})

    data['TOPICINT_c_t2b'] = data['TOPICINT_c'].map({1.0: 1, 2.0: 1,
                                                    3.0: 2, 4.0: 2})

    data['TOPICINT_d_t2b'] = data['TOPICINT_d'].map({1.0: 1, 2.0: 1,
                                                    3.0: 2, 4.0: 2})

    data['TOPICINT_e_t2b'] = data['TOPICINT_e'].map({1.0: 1, 2.0: 1,
                                                    3.0: 2, 4.0: 2})

    data['TOPICINT_f_t2b'] = data['TOPICINT_f'].map({1.0: 1, 2.0: 1,
                                                    3.0: 2, 4.0: 2})

    # Groups NEWSFACTS questions inot T2B (almost all of the time,
    # more than half)
    data['NEWSFACTS_a_t2b'] = data['NEWSFACTS_a'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 3, 5.0: 3, 6.0: 4})

    data['NEWSFACTS_b_t2b'] = data['NEWSFACTS_b'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 3, 5.0: 3, 6.0: 4})

    data['NEWSFACTS_c_t2b'] = data['NEWSFACTS_c'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 3, 5.0: 3, 6.0: 4})

    data['NEWSFACTS_d_t2b'] = data['NEWSFACTS_d'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 3, 5.0: 3, 6.0: 4})

    data['NEWSFACTS_e_t2b'] = data['NEWSFACTS_e'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 3, 5.0: 3, 6.0: 4})

    data['NEWSFACTS_f_t2b'] = data['NEWSFACTS_f'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 3, 5.0: 3, 6.0: 4})

    data['NEWSFACTS_g_t2b'] = data['NEWSFACTS_g'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 3, 5.0: 3, 6.0: 4})

    data['NEWSFACTS_h_t2b'] = data['NEWSFACTS_h'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 3, 5.0: 3, 6.0: 4})

    data['NEWSFACTS_i_t2b'] = data['NEWSFACTS_i'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 3, 5.0: 3, 6.0: 4})

    # Create t2b of shows watched
    data['ENTCRIM1_t2b'] = data['ENTCRIM1'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 2})

    data['ENTHOSP1_t2b'] = data['ENTHOSP1'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 2})

    data['ENTSCIFI1_t2b'] = data['ENTSCIFI1'].map({1.0: 1, 2.0: 1,
                                                3.0: 2, 4.0: 2})


    ## Changes the -1 responses to Null (-1 in dataset represents 'refused')
    data = data.replace(-1, np.NaN)
    data = data.replace('-1', np.NaN)

    ## Drops null values in all data, the -1 means they
    ## Didn't respond or refused to respond to a question
    data = data.dropna()

    ## Assigns segment data based on segment variables
    ## Segment varaibles were tested and scored in Jupyter Notebook
    segment_data = data[segment_variables]

    ## Scales the segmentation data to be on a scale from 1-2 to standardize
    ## For segmentation
    scaler = MinMaxScaler((1,2))
    scaled = scaler.fit_transform(segment_data)
    scaled_data = pd.DataFrame(scaled, index = segment_data.index,
                                columns=segment_data.columns)

    return data, scaled_data


def get_dummies(data, dummy_cols, column_names):
    '''
    Makes dummy variables for list of columns
    '''
    dummy_database = pd.DataFrame()
    for col in dummy_cols:
        dummies = pd.get_dummies(data[col])
        dummies.rename(columns = column_names[col], inplace = True)
        dummy_database = pd.concat([dummy_database, dummies], axis = 1,\
                                    sort = False)

    return dummy_database

def get_seg_size_df(db):
    '''
    Returns a database with the sum of responses for each question groupped
    by the segments
    '''
    segments = list(db['Segment'].unique())
    segments.sort()
    sizes = []
    sum_table = db.groupby(by = ['Segment']).sum()

    for seg in segments:
        seg_size = sum_table['SEGMENT {}'.format(seg)].max()
        sum_table.drop(columns = 'SEGMENT {}'.format(seg), inplace = True)
        sizes.append(seg_size)

    sum_table['SEGMENT SIZE'] = sizes
    return sum_table

def get_database(db):
    '''
    A pipeline for returning a database to analyze a segment solution across
    all variables in the survey
    '''
    dummy_column_names, column_names, dummy_columns = get_database_columns()
    ## Gets dummy columns from get dummy function
    dummy_data = get_dummies(db, dummy_columns, dummy_column_names)
    ## Drops the dummy data columns from database passed in
    db.drop(columns = dummy_columns[:-1], inplace = True)
    ## Renames the columns in original data base using mapped
    db.rename(columns=column_names, inplace = True)

    ## Creates database by combining dummy data and renamed columns
    database = pd.concat((db, dummy_data), axis = 1)

    database_df = get_seg_size_df(database)

    ## Transpose so the segments are in the columns
    database_df = database_df.T
    segment_sizes = database_df.loc['SEGMENT SIZE']
    ## To get column percentages for the segments
    database_df = database_df.div(segment_sizes, axis=1)
    ## To get percentages
    database_df = database_df*100
    ## Reassigns the segment sizes, otherwise all 1's
    database_df.loc['SEGMENT SIZE'] = segment_sizes

    database_df= database_df.round(decimals = 2)

    return database_df
