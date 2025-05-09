


import plotly.express as px
import taipy.gui.builder as tgb
from taipy.gui import Gui
import pandas as pd

import duckdb

nordic_size = pd.read_csv("nordic_size.csv")
df_ranking = pd.read_csv("nordic_company_rankings.csv")

df_industry = duckdb.query(
    """--sql

    SELECT  

    Company,
    "Revenue (billion $)" AS Revenue,
    Industry,
    
    FROM df_ranking

    ORDER BY Revenue DESC


"""
).df()


with tgb.Page() as page:
    with tgb.part(class_name="container card"): # Stack ger space mellan korten
        tgb.text("Dashboard for largest Nordic companies", mode="md")
        
    with tgb.layout(columns= "2 1"):    
        with tgb.part():
            tgb.table("{df_industry}")




            







Gui(page).run( use_reloader=True, port=8080)


