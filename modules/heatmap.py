def selector(prix_min ,prix_max, df, cat_select) :
    # select only the rows between the 2 prices
    df_hm_filtre = df[(df['prix_m2']>prix_min)&(df['prix_m2']<prix_max)]
    for cat in cat_select:
        df_hm_filtre = df_hm_filtre[(df_hm_filtre[cat]>1)]
    return df_hm_filtre
