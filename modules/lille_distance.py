import pandas as pd
import numpy as np
from geopy import distance
import geopy

def get_features_density(target_df, features_df, dist=500):
    # copying the target dataframe
    t_df = target_df.copy()

    #looping on both dataframes
    for idx, row in target_df.iterrows():
        coords = (row['lat'], row['lon'])
        for row_f in features_df.iterrows():
            coord_f = (row_f['lat'],row_f['lon'])
            # calculating the distance between target and feature and checking if distance is under dist meters
            if distance.distance(coords,coord_f).meters < dist:
                # incrementing the number of the feature
                target_df.at[idx, row_f['Sous_Cat']] += 1

    return t_df

def get_surrounding_targets(latitude, longitude, target_df, dist=500):
    surround_targets = {}
    coords = (latitude, longitude)
    for idx_t, row_t in target_df.iterrows():
        coord_t = (row_t['lat'],row_t['lon'])
        # calculating the distance between target and feature and checking if distance is under dist meters
        if distance.distance(coords,coord_t).meters < dist:
            surround_targets[idx_t] = distance.distance(coords,coord_t).meters

    # sorting the dictionnary will get the keys with lowest values we take the 10 closest (if possible)
    closest_targets = dict(sorted(surround_targets.items(), key=lambda x:x[1]))
    if len(closest_targets) >= 10:
        closest_targets = list(closest_targets.keys())[:10]

    return closest_targets
