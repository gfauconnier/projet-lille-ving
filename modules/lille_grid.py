import pandas as pd
import numpy as np
import geopandas
import shapely.geometry

N_CELLS = 30

def get_cells():
    # total area for the grid
    xmin, ymin, xmax, ymax= [2.972889, 50.601455, 3.121113, 50.656799]

    # getting cells size
    cell_size = (xmax-xmin)/N_CELLS

    # projection of the grid
    crs = "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +a=6371007.181 +b=6371007.181 +units=m +no_defs"

    # create the cells in a loop
    grid_cells = []
    for x0 in np.arange(xmin, xmax+cell_size, cell_size ):
        for y0 in np.arange(ymin, ymax+cell_size, cell_size):
            x1 = x0-cell_size
            y1 = y0+cell_size
            grid_cells.append(shapely.geometry.box(x0, y0, x1, y1))

    cells = geopandas.GeoDataFrame(grid_cells, columns=['geometry'], crs=crs)

    return cells

def get_grid_values(df):
    # creating the GeoDataFrame with only lat and lon from original Dataframe
    df_grid = df.copy()
    gdf = geopandas.GeoDataFrame(df_grid,
            geometry=geopandas.points_from_xy(df.lon, df.lat),
            crs="+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +a=6371007.181 +b=6371007.181 +units=m +no_defs")

    # getting the cells based on gdf
    cells = get_cells()

    # passing on every cell and adding the cell number to gdf
    for cell in range(0,cells.shape[0]):
        pip = gdf.within(cells.loc[cell, 'geometry'])
        gdf.loc[pip, 'cell'] = int(cell)

    # adding default value to cell column if there was an oob value and passing to int
    gdf['cell'].fillna(value=-1, inplace=True)
    gdf['cell'] = gdf['cell'].astype('int')

    # dropping the geometry column
    gdf.drop(columns='geometry', inplace=True)

    return gdf

def get_cell_value(longitude, latitude):
    # create a geometry object from the latitude and longitude
    geometry=geopandas.points_from_xy([longitude], [latitude])

    # getting all the cells
    cells = get_cells()

    # checking in which cell the point is and returns its number
    for cell in range(0,cells.shape[0]):
        if geometry.within(cells.loc[cell, 'geometry']):
            return int(cell)
    # returns -1 if no cell was found
    return -1

def surrounding_cells(cell_number, include_origin=True):
    # the cell numbers surrounding the selected cell
    surrounding_cells = []

    # getting the selected cell coordinates
    cells = get_cells()
    cell_coords = get_cell_coords(cells.loc[cell_number]['geometry'])
    # looping on all cells
    for cell_n in range(0,cells.shape[0]):
        checked_cell = get_cell_coords(cells.loc[cell_n]['geometry'])
        # getting all coordinates matching between selected cell and loop on
        cells_around = [coord for coord in cell_coords if coord in checked_cell]

        # only keeping the cells which have 1 or 2 corresponding corners
        if len(cells_around) == 1 or len(cells_around) == 2 or (len(cells_around) == 4 and include_origin == True):
            surrounding_cells.append(cell_n)

    return surrounding_cells

def get_cell_coords(cell):
    # getting the coordinates of all corners and pairing them
    x, y = cell.boundary.coords.xy
    corner_coords = list(zip(x,y))

    #removing the last coordinate as it the the same as the first
    corner_coords.pop()

    return corner_coords

def get_surround_features(df, df_features):
    # getting all the features by cell and adding them to a dictionary
    dict_features = {}
    for cell in range(0,df.cell.max()):
        features_count = df_features[df_features['cell']==cell]['feature'].value_counts()
        if features_count.shape[0] != 0:
            dict_features[cell] = features_count



    return df

def get_near_features(df_target, df_features):
    df_target.cell.max()
    dict_features = {}
    for cell in range(-1,df_target.cell.max()+1):
        features_count = df_features[df_features['cell']==cell]['Sous_Cat'].value_counts()
        dict_features[cell] = features_count
    for idx, row in df_target.iterrows():
        for feature in dict_features[row['cell']].items():
            df_target.at[idx, feature[0]] = feature[1]
    return df_target
