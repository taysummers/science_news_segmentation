import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

def _euclidean_distance(x, y):
    '''
    Computes the euclidean distance between two pandas series
    '''
    euc = x-y
    dist = (np.sqrt(sum(euc**2)))
    return dist

def wcss_score(X, labels, centers):
    '''
    Computes the within cluster sum of squares
    '''
    wcss = 0
    X_data = X.copy()
    X_data['labels'] = labels
    X_data = np.asarray(X_data)
    for label in set(X_data[:, -1]):
        #sum of distance squared between all points and centroid in cluster
        for x_i in (X_data[X_data[:, -1] == label]):
            dist = _euclidean_distance(x_i[:-1], centers[int(label)])
            wcss += dist**2

    return wcss

def plot_scores_kmeans(X, k_vals):
    '''
    Plots the within cluster sum of squares and silhoutte scores over a range
    of k-values for a KMeans cluster object
    '''
    wcss_scores = []
    sil_scores = []
    for k in k_vals:
        model = KMeans(n_clusters = k)
        fit_model = model.fit(X)
        labels = fit_model.labels_
        centers = fit_model.cluster_centers_
        wcss = wcss_score(X, labels, centers)
        wcss_scores.append(wcss)
        sil = silhouette_score(X, labels)
        sil_scores.append(sil)

    fig, ax = plt.subplots()
    ax.plot(k_vals, wcss_scores, 'o-')
    ax.set_xlabel("number of clusters")
    ax.set_ylabel("within-cluster sum of squares")

    fig, ax = plt.subplots()
    ax.plot(k_vals, sil_scores, 'o-')
    ax.set_xlabel("number of clusters")
    ax.set_ylabel("silhouette scores")
    print(sil_scores)

    plt.show()

def plot_sil_scores_hclust(X, k_vals, affinity, linkage):
    '''
    Plots the silhoutte scores over a range
    of k-values for a Agglomerative cluster (Hiererarchical) object
    '''
    sil_scores = []
    for k in k_vals:
        model = AgglomerativeClustering(n_clusters = k, affinity =affinity,\
                                        linkage = linkage)
        fit_model = model.fit(X)
        labels = fit_model.labels_
        sil = silhouette_score(X, labels)
        sil_scores.append(sil)

    fig, ax = plt.subplots()
    ax.plot(k_vals, sil_scores, 'o-')
    ax.set_xlabel("number of clusters")
    ax.set_ylabel("silhouette scores")
    ax.set_title('Silhoutte Score: affinity= {}, linkage = {}'.format(affinity,\
                                                                    linkage))
    print(sil_scores)

    plt.show()

def plot_scores_gauss(X, k_vals, cov_type, max_iter = 100):
    '''
    Plots the silhoutte, AIC and BIC scores over a range
    of k-values for a Gaussian Mixture object
    '''

    sil_scores = []
    aic_scores = []
    bic_scores = []
    for k in k_vals:
        model = GaussianMixture(n_components = k,
                                covariance_type= cov_type,
                                max_iter = max_iter)
        fit_model = model.fit(X)
        labels = model.predict(X)
        sil = silhouette_score(X, labels)
        aic = model.aic(X)
        bic = model.bic(X)
        sil_scores.append(sil)
        aic_scores.append(aic)
        bic_scores.append(bic)

    fig, ax = plt.subplots()
    ax.plot(k_vals, sil_scores, 'o-')
    ax.set_xlabel("number of clusters")
    ax.set_ylabel("silhouette scores")
    ax.set_title('Silhoutte Score cov_type = {}'.format(cov_type))
    print(sil_scores)

    fig, ax = plt.subplots()
    ax.plot(k_vals, aic_scores, 'o-')
    ax.set_xlabel("number of clusters")
    ax.set_ylabel("AIC scores")
    ax.set_title('AIC Score cov_type = {}'.format(cov_type))

    fig, ax = plt.subplots()
    ax.plot(k_vals, bic_scores, 'o-')
    ax.set_xlabel("number of clusters")
    ax.set_ylabel("BIC scores")
    ax.set_title('BIC Score cov_type = {}'.format(cov_type))

    plt.show()
