

def filter_df_municipality(df, industry_area="Banking"):
    return (
        df.query("Industri == @educational_area")["Company"]
        .value_counts()
        .reset_index()
        .rename({"count": "Ansökta utbildningar"}, axis=1) # Renaming count to ansökta utbildningar
    )


def filter_data(state):
    df_municipality = filter_df_municipality(
        state.df, educational_area=state.selected_educational_area
    )