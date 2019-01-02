import pandas as pd
import pickle
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.ensemble import GradientBoostingClassifier
from pipeline import *


class SegmentModel():
    """
    Module containing model fitting code for a web application that implements a
    segmentation classification model.

    When run as a module, this will load a csv dataset, train a segmentation
    model,train a classification model,
    and then pickle the resulting model object to disk.
    """

    def __init__(self):
        ## Gradient Boosting Model Parameters Optimized using Grid Search
        ## in Jupyter Notebook File
        self._classifier = GradientBoostingClassifier(learning_rate = .1,
                                                      max_depth = 1,
                                                      n_estimators = 200,
                                                      subsample = .75)

    def fit(self, X, y):
        """Fit a text classifier model.

        Parameters
        ----------
        X: A numpy array or list of text fragments, to be used as predictors.
        y: A numpy array or python list of labels, to be used as responses.

        Returns
        -------
        self: The fit model object.
        """
        self._classifier.fit(X, y)
        return self


    def _transform_new(self, X_new):
        '''
        Transforms new data to make model predictions
        '''
        # Transforms gender column:
        ## Male: 1
        ## Female: 0
        X_new['PPGENDER'] = X_new['PPGENDER'].apply(lambda x: 1 if x==1 else 0)

        # Transforms Source1 column
        ## Specific sources: 1
        ## Many sources:
        X_new['SOURCE1'] = X_new['SOURCE1'].apply(lambda x: 1 if x==1.0 else 0)

        # Transforms age column
        if X_new['ppagecat'][0] == 1:
            d = {'18-24': [1], '25-34': [0], '35-44': [0], '45-54': [0],
                 '55-64': [0], '65-74': [0], '75+': [0]}
            age_dummies = pd.DataFrame(data = d)

        elif X_new['ppagecat'][0] == 2:
            d = {'18-24': [0], '25-34': [1], '35-44': [0], '45-54': [0],
                 '55-64': [0], '65-74': [0], '75+': [0]}
            age_dummies = pd.DataFrame(data = d)

        elif X_new['ppagecat'][0] == 3:
            d = {'18-24': [0], '25-34': [0], '35-44': [1], '45-54': [0],
                 '55-64': [0], '65-74': [0], '75+': [0]}
            age_dummies = pd.DataFrame(data = d)


        elif X_new['ppagecat'][0] == 4:
            d = {'18-24': [0], '25-34': [0], '35-44': [0], '45-54': [1],
                 '55-64': [0], '65-74': [0], '75+': [0]}
            age_dummies = pd.DataFrame(data = d)


        elif X_new['ppagecat'][0] == 5:
            d = {'18-24': [0], '25-34': [0], '35-44': [0], '45-54': [0],
                 '55-64': [1], '65-74': [0], '75+': [0]}
            age_dummies = pd.DataFrame(data = d)


        elif X_new['ppagecat'][0] == 6:
            d = {'18-24': [0], '25-34': [0], '35-44': [0], '45-54': [0],
                 '55-64': [0], '65-74': [1], '75+': [0]}
            age_dummies = pd.DataFrame(data = d)


        elif X_new['ppagecat'][0] == 7:
            d = {'18-24': [0], '25-34': [0], '35-44': [0], '45-54': [0],
                 '55-64': [0], '65-74': [0], '75+': [1]}
            age_dummies = pd.DataFrame(data = d)


        # Transforms education column
        if X_new['PPEDUCAT'][0] == 1:
            d = {'Less than HS': [1], 'Completed HS': [0], 'Some College': [0],
                 'Bachelors+': [0]}
            edu_dummies = pd.DataFrame(data = d)

        elif X_new['PPEDUCAT'][0] == 2:
            d = {'Less than HS': [0], 'Completed HS': [1], 'Some College': [0],
                 'Bachelors+': [0]}
            edu_dummies = pd.DataFrame(data = d)

        elif X_new['PPEDUCAT'][0] == 3:
            d = {'Less than HS': [0], 'Completed HS': [0], 'Some College': [1],
                 'Bachelors+': [0]}
            edu_dummies = pd.DataFrame(data = d)

        elif X_new['PPEDUCAT'][0] == 4:
            d = {'Less than HS': [0], 'Completed HS': [0], 'Some College': [0],
                 'Bachelors+': [1]}
            edu_dummies = pd.DataFrame(data = d)

        # Transforms Topic Int d column
        if X_new['TOPICINT_d'][0] == 1.0:
            d = {'BusNews: Very Interested': [1],
                 'BusNews: Somewhat Interested': [0],
                 'BusNews: Not Too Interested': [0],
                 'BusNews: Not At All Interested': [0]}
            busnews_dummies = pd.DataFrame(data = d)

        elif X_new['TOPICINT_d'][0] == 2.0:
            d = {'BusNews: Very Interested': [0],
                 'BusNews: Somewhat Interested': [1],
                 'BusNews: Not Too Interested': [0],
                 'BusNews: Not At All Interested': [0]}
            busnews_dummies = pd.DataFrame(data = d)

        elif X_new['TOPICINT_d'][0] == 3.0:
            d = {'BusNews: Very Interested': [0],
                 'BusNews: Somewhat Interested': [0],
                 'BusNews: Not Too Interested': [1],
                 'BusNews: Not At All Interested': [0]}
            busnews_dummies = pd.DataFrame(data = d)

        elif X_new['TOPICINT_d'][0] == 4.0:
            d = {'BusNews: Very Interested': [0],
                 'BusNews: Somewhat Interested': [0],
                 'BusNews: Not Too Interested': [0],
                 'BusNews: Not At All Interested': [1]}
            busnews_dummies = pd.DataFrame(data = d)

        # Transforms Topic Int e column
        if X_new['TOPICINT_e'][0] == 1.0:
            d = {'SciNews: Very Interested': [1],
                 'SciNews: Somewhat Interested': [0],
                 'SciNews: Not Too Interested': [0],
                 'SciNews: Not At All Interested': [0]}
            scinews_dummies = pd.DataFrame(data = d)

        elif X_new['TOPICINT_e'][0] == 2.0:
            d = {'SciNews: Very Interested': [0],
                 'SciNews: Somewhat Interested': [1],
                 'SciNews: Not Too Interested': [0],
                 'SciNews: Not At All Interested': [0]}
            scinews_dummies = pd.DataFrame(data = d)

        elif X_new['TOPICINT_e'][0] == 3.0:
            d = {'SciNews: Very Interested': [0],
                 'SciNews: Somewhat Interested': [0],
                 'SciNews: Not Too Interested': [1],
                 'SciNews: Not At All Interested': [0]}
            scinews_dummies = pd.DataFrame(data = d)

        elif X_new['TOPICINT_e'][0] == 4.0:
            d = {'SciNews: Very Interested': [0],
                 'SciNews: Somewhat Interested': [0],
                 'SciNews: Not Too Interested': [0],
                 'SciNews: Not At All Interested': [1]}
            scinews_dummies = pd.DataFrame(data = d)


        # Transforms Topic Int a column
        if X_new['TOPICINT_a'][0] == 1.0:
            d = {'GovNews: Very Interested': [1],
                 'GovNews: Somewhat Interested': [0],
                 'GovNews: Not Too Interested': [0],
                 'GovNews: Not At All Interested': [0]}
            govnews_dummies = pd.DataFrame(data = d)

        elif X_new['TOPICINT_a'][0] == 2.0:
            d = {'GovNews: Very Interested': [0],
                 'GovNews: Somewhat Interested': [1],
                 'GovNews: Not Too Interested': [0],
                 'GovNews: Not At All Interested': [0]}
            govnews_dummies = pd.DataFrame(data = d)

        elif X_new['TOPICINT_a'][0] == 3.0:
            d = {'GovNews: Very Interested': [0],
                 'GovNews: Somewhat Interested': [0],
                 'GovNews: Not Too Interested': [1],
                 'GovNews: Not At All Interested': [0]}
            govnews_dummies = pd.DataFrame(data = d)

        elif X_new['TOPICINT_a'][0] == 4.0:
            d = {'GovNews: Very Interested': [0],
                 'GovNews: Somewhat Interested': [0],
                 'GovNews: Not Too Interested': [0],
                 'GovNews: Not At All Interested': [1]}
            govnews_dummies = pd.DataFrame(data = d)

        # Transforms Sci Why column
        if X_new['SCIWHY_e'][0] == 1.0:
            d = {'Curious about what\'s happening in science major reason': [1],
                 'Curious about what\'s happening in science minor reason': [0],
                 'Curious about what\'s happening in science not a reason': [0]}
            sciwhy_dummies = pd.DataFrame(data = d)

        elif X_new['SCIWHY_e'][0] == 2.0:
            d = {'Curious about what\'s happening in science major reason': [0],
                 'Curious about what\'s happening in science minor reason': [1],
                 'Curious about what\'s happening in science not a reason': [0]}
            sciwhy_dummies = pd.DataFrame(data = d)

        elif X_new['SCIWHY_e'][0] == 3.0:
            d = {'Curious about what\'s happening in science major reason': [0],
                 'Curious about what\'s happening in science minor reason': [0],
                 'Curious about what\'s happening in science not a reason': [1]}
            sciwhy_dummies = pd.DataFrame(data = d)


        age_dummies.drop(columns = '18-24', axis = 1, inplace = True)
        edu_dummies.drop(columns = 'Less than HS', axis = 1, inplace = True)
        busnews_dummies.drop(columns = 'BusNews: Very Interested', axis = 1,
                            inplace = True)
        scinews_dummies.drop(columns = 'SciNews: Very Interested', axis = 1,
                            inplace = True)
        govnews_dummies.drop(columns = 'GovNews: Very Interested', axis = 1,
                            inplace = True)
        sciwhy_dummies.drop(columns = 'Curious about what\'s happening in science major reason',
                                        axis = 1, inplace = True)


        X_new = pd.concat((X_new, scinews_dummies, age_dummies, edu_dummies,
                           sciwhy_dummies, busnews_dummies, govnews_dummies),
                            axis = 1)

        X_new.drop(labels = ['TOPICINT_e', 'ppagecat', 'PPEDUCAT', 'TOPICINT_d',
                           'SCIWHY_e', 'TOPICINT_a'], axis = 1, inplace = True)

        return X_new




    def predict(self, X):
        """Make predictions on new data."""

        X = self._transform_new(X)
        prediction = self._classifier.predict(X)
        return prediction



def get_data():
    '''
    Load raw data from a refile and returns training data and responses.

    Parameters
    ----------
    None

    Returns
    -------
    X: a pandas data frame containing data formatted for training
    y: a pandas series containing labels

    '''
    path = 'data/2017 Pew Research Center Science and News Survey/Segmentation_data.csv'
    data, segment_data = get_cluster_data(path)
    gm = GaussianMixture(n_components = 3, covariance_type ='spherical',
                        random_state = 20)
    gm.fit(segment_data)
    labels = gm.predict(segment_data)

    data['SEGMENT'] = labels

    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    features = ['PPGENDER', 'TOPICINT_e', 'ppagecat', 'PPEDUCAT', 'SCIWHY_e',
                'TOPICINT_d', 'LIST1_b', 'TOPICINT_a', 'SOURCE1']

    X = X[features]
    # Gender 1: Male 0: Female
    X['PPGENDER'] = X['PPGENDER'].apply(lambda x: 1 if x==1 else 0)
    # Source 1: Specific sources 0: Many sources
    X['SOURCE1'] = X['SOURCE1'].apply(lambda x: 1 if x==1.0 else 0)

    topic_dummies = pd.get_dummies(X['TOPICINT_e'], drop_first = True)
    topic_dummies.rename(columns = {2.0: 'SciNews: Somewhat Interested',
                                   3.0: 'SciNews: Not Too Interested',
                                   4.0: 'SciNews: Not At All Interested'},
                                   inplace = True)

    age_dummies = pd.get_dummies(X['ppagecat'], drop_first = True)
    age_dummies.rename(columns = {2: '25-34', 3: '35-44', 4: '45-54',
                                  5: '55-64', 6: '65-74', 7: '75+'},
                                  inplace = True)


    edu_dummies = pd.get_dummies(X['PPEDUCAT'], drop_first = True)
    edu_dummies.rename(columns = {2: 'Completed HS', 3: 'Some College',
                                  4: 'Bachelors+'}, inplace = True)

    sci_why_dummies = pd.get_dummies(X['SCIWHY_e'], drop_first = True)
    sci_why_dummies.rename(columns = {2.0: 'Curious about what\'s happening in science minor reason',
                                     3.0: 'Curious about what\'s happening in science not a reason'},
                                    inplace = True)

    topicbus_dummies = pd.get_dummies(X['TOPICINT_d'], drop_first = True)

    topicbus_dummies.rename(columns = {2.0: 'BusNews: Somewhat Interested',
                                   3.0: 'BusNews: Not Too Interested',
                                   4.0: 'BusNews: Not At All Interested'},
                                   inplace = True)

    topicgov_dummies = pd.get_dummies(X['TOPICINT_a'], drop_first = True)

    topicgov_dummies.rename(columns = {2.0: 'GovNews: Somewhat Interested',
                               3.0: 'GovNews: Not Too Interested',
                               4.0: 'GovNews: Not At All Interested'},
                               inplace = True)

    X = pd.concat((X, topic_dummies, age_dummies, edu_dummies,
                     sci_why_dummies, topicbus_dummies, topicgov_dummies),
                     axis = 1)

    X.drop(labels = ['TOPICINT_e', 'ppagecat', 'PPEDUCAT', 'TOPICINT_d',
                       'SCIWHY_e', 'TOPICINT_a'], axis = 1, inplace = True)

    return X, y


def get_pickle():
    X, y = get_data()
    sm = SegmentModel()
    sm.fit(X, y)
    with open('model.pkl', 'wb') as f:
        pickle.dump(sm, f)
