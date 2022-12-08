def selector(min_price ,max_price, df, cat_select, type_local) :
    # select only the rows between the 2 prices
    if type_local==0:
        df_hm_filtered = df[(df['prix_m2']>min_price) & (df['prix_m2']<max_price)]
    else:
        df_hm_filtered = df[(df['prix_m2']>min_price) & (df['prix_m2']<max_price) & (df['code_type_local']==type_local)]

    # checks if there is at least 1 feature of the category
    for cat in cat_select:
        df_hm_filtered = df_hm_filtered[(df_hm_filtered[cat]>1)]

    return df_hm_filtered
