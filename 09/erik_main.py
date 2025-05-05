import taipy.gui.builder as tgb
from taipy.gui import Gui
from utils.cons import DATA_DIRECTORY
import pandas as pd
from frontend.charts import create_municpality_bar

df = pd.read_excel(
    DATA_DIRECTORY / "resultat-ansokningsomgang-2024.xlsx",
    sheet_name="Tabell 3",
    skiprows=5,
)


def filter_df_municipality(df, educational_area="Data/IT"):
    return (
        df.query("Utbildningsområde == @educational_area")["Kommun"]
        .value_counts()
        .reset_index()
        .rename({"count": "Ansökta utbildningar"}, axis=1)
    )


def filter_data(state):
    df_municipality = filter_df_municipality(
        state.df, educational_area=state.selected_educational_area
    )

    state.municipality_chart = create_municpality_bar(
        df_municipality.head(state.number_municipalities),
        ylabel="KOMMUN",
        xlabel="ANSÖKTA UTBILDNINGAR",
    )

    state.municipalities_title = state.number_municipalities
    state.educational_area_title = state.selected_educational_area


df_municipality = filter_df_municipality(df)


municipality_chart = create_municpality_bar(
    df_municipality.head(9), ylabel="KOMMUN", xlabel="ANSÖKTA UTBILDNINGAR"
)


number_municipalities = 5
municipalities_title = number_municipalities

selected_educational_area = "Data/IT"
educational_area_title = selected_educational_area

with tgb.Page() as page:
    with tgb.part(class_name="container card stack-large"):
        with tgb.part(class_name="card"):
            tgb.text("# MYH dashboard 2024", mode="md")
            tgb.text(
                "En dashboard för att visa statistik och information om ansökningsomgång 2024",
                mode="md",
            )

            with tgb.layout(columns="2 1"):
                with tgb.part(class_name="card") as column_chart:
                    tgb.text(
                        "## Antalet ansökta YH utbildningar per kommun (topp {municipalities_title}) för {educational_area_title}",
                        class_name="title-chart",
                        mode="md",
                    )
                    tgb.chart(figure="{municipality_chart}")

                with tgb.part(class_name="card") as column_filters:
                    tgb.text("## Filtrera data", mode="md")
                    tgb.text("Filtrera antalet kommuner", mode="md")

                    tgb.slider(
                        value="{number_municipalities}",
                        min=5,
                        max=len(df_municipality),
                        continuous=False,
                    )

                    tgb.text("Välj utbildningsområde", mode="md")
                    tgb.selector(
                        value="{selected_educational_area}",
                        lov=df["Utbildningsområde"].unique(),
                        dropdown=True,
                    )

                    tgb.button(
                        "FILTRERA DATA", on_action=filter_data, class_name="plain"
                    )

            with tgb.part(class_name="card"):
                tgb.text("## Rådata", mode = "md")
                tgb.table("{df}")

Gui(page, css_file="assets/main.css").run(dark_mode=False, use_reloader=True, port=8080)
