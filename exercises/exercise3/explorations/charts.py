import plotly.express as px
import duckdb

gapminder = px.data.gapminder()

duckdb.register("gapminder", gapminder)


nordic = gapminder[
    gapminder["country"].isin(["Sweden", "Norway", "Denmark", "Finland", "Iceland"])
    ] #Blir boolean mask


poor = duckdb.query(
    """--sql
    SELECT
    "country",
    "year",
    "lifeExp"
FROM gapminder
WHERE "country" IN (
    SELECT "country"
    FROM gapminder
    WHERE year = 2007
    ORDER BY "lifeExp" ASC
    LIMIT 5
)
ORDER BY "country", "year"

    """

).df()


def create_life_expectancy_plot(df, title):

    fig = px.line(
        df,
        y="lifeExp",
        x="year",
        color = "country",
        title=title
    )

    fig.update_layout(
        plot_bgcolor="#d9d9d9",   # Light gray inside the plot area
        paper_bgcolor="rgba(0,0,0,0)",
        title_font=dict(
        family="Arial, sans-serif",  
        size=24,                          
        color="#d9d9d9"                     
    ),
        hovermode = "x",
            xaxis=dict(
                showgrid=False,
                title=dict(
                    text="",
                ),
                tickfont=dict(
                    family="Arial, sans-serif",
                    size=12,
                    color="#d9d9d9"  # <-- Numbers (ticks) will be gray
                ),
                automargin=True
            ), 
        yaxis=dict(
            showgrid=False,
            title="Life Expectancy [years]",
            title_font=dict(
                size=18,
                family="Arial, sans-serif",  # "Arial Black" makes it look bolder
                color="#d9d9d9"
                ),
                tickfont=dict(
                    family="Arial, sans-serif",
                    size=12,
                    color="#d9d9d9"  # <-- Numbers (ticks) on Y-axis will be gray too
                 )
            
        ),
        #Legends 
        legend=dict(
        bgcolor="rgba(0,0,0,0)", 
        title = "<b>Countries</b>",
        bordercolor="#d9d9d9",                 
        borderwidth=1,                       # border thickness
        font=dict(
            family="Arial, sans-serif",  
            size=10,
            color="#d9d9d9"
        )
        ),

        annotations=[
            dict(
                text="Year",           # <-- Your fake title
                x=0,                   # <-- Far left (0 = left, 1 = right)
                xref="paper",
                y=-0.08,                   # <-- At the bottom
                yref="paper",
                showarrow=False,
                font=dict(
                    size=18,
                    family="Arial, sans-serif",
                    color="#d9d9d9"
                ),
                xanchor="left",         # <-- Anchor it to the left side
                yanchor="top"
            )
        ]
    )

    fig.update_xaxes(
        showspikes = True,
        spikemode = "across",
        spikesnap = "cursor",

    )


    return fig

def scatter(df, title):

    fig = px.scatter(
        df,
        x ="gdpPercap", 
        y = "lifeExp", 
        color = "continent", # Eller country
        animation_frame="year", 
        animation_group="country",
        size="pop",
        size_max=70,
        log_x=True,
        range_y=[25, 90],
        range_x=[100, 100000],
        title = title
        )
    fig.update_layout(
          xaxis_title="GDP per Capita (USD)",
          yaxis_title="Life Expectancy [years]",
          plot_bgcolor="#d9d9d9",   # Light gray inside the plot area
          paper_bgcolor="rgba(0,0,0,0)",
          xaxis=dict(
        showgrid=False
        ),
        yaxis=dict(
        showgrid=False
        ),
        font=dict(
            family="Arial, sans-serif",  
            size=14,
            color="#d9d9d9"
        ),

           legend=dict(
        bgcolor="rgba(0,0,0,0)", 
        title = "<b>Continents</b>",
        bordercolor="#d9d9d9",                 
        borderwidth=1,                       # border thickness
        font=dict(
            family="Arial, sans-serif",  
            size=10,
            color="#d9d9d9"
        )
        ),
                      
                      
                      
    )

    return fig






fig_poor = create_life_expectancy_plot(poor, "Bottom five countries for Life Expectancy [1952 - 2007]")

fig_rich = create_life_expectancy_plot(nordic, "Life Expectancy in the nordic countries [1952 - 2007]")

fig_scatter = scatter(gapminder, "Life expectancy in relation to GDP per capita <br><span style='font-size:75%'>- Filtered by world continents [1952 - 2007]"
)

