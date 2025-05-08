import taipy.gui.builder as tgb
from taipy.gui import Gui
import plotly.express as px

from explorations.charts import fig_rich, fig_poor, fig_scatter

with tgb.Page() as page:
    with tgb.part(class_name="container card stack-large"):
        with tgb.part(class_name="card"):
            tgb.text("## Dashboard showing development of life expectancy in the world", class_name="dashboard-title", mode="md")
            tgb.chart(figure="{fig_scatter}")
        
        
        with tgb.part(class_name="card"):
                tgb.chart(figure="{fig_rich}")
        with tgb.part(class_name="card"):
                tgb.chart(figure="{fig_poor}")




             

Gui(page, css_file="assets/main.css").run(use_reloader=True, port=8080)