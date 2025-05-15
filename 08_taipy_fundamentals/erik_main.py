from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px

df = px.data.gapminder()
fig = px.line(df.query("country == 'Sweden'"), x="year", y="pop")

slider_value = 20
selected_fruit = "avocado"
number1= 5
number2= 8
sum_ = number1 + number2

def perform_calculation(state):
    #print(state.number1) 

    state.sum_ = int(state.number1) + int(state.number2)
    # Add divison, multiplication, subtraction

def clear_results(state):
    state.sum_=""

with tgb.Page() as page:
     with tgb.part(class_name="container card"): # Gives it a certain style
        with tgb.layout(columns="1 1 1"): # Divides it into three sections
                with tgb.part() as column_fruit:
                    tgb.text("# Hello there Taipy", mode="md")
                    tgb.text("Welcome to the world of programing")

                    # Binds to slider_value varaible and makes it dynamic
                    tgb.slider(value="{slider_value}", min=1, max=50, step=1, continuous=False)
                    tgb.text("Slider value is at {slider_value}")

                    tgb.text("Select our favourite fruit", mode="md")
                    tgb.selector(
                        value="{selected_fruit}", lov=["tomato", "apple", "avocado", "banana"],
                        dropdown=True,
                        )
                    tgb.text("Yummy {selected_fruit}")
                    tgb.image("assets/{selected_fruit}.jpg")

                with tgb.part() as column_calculator:
                    tgb.text("## Coolu calculatuoru", mode = "md")
                    tgb.text("Type in a number")
                    tgb.input("{number1}", on_change=clear_results)

                    tgb.text("Type in a number")

                    # On change -> this function will run when value is changed
                    tgb.input("{number2}",on_change=clear_results)

                    tgb.text("You have typed in {number1} and {number2}")



                    # On action -> this action will run when button  is clicked
                    tgb.button(label="CALCULATU", class_name="plain", on_action=perform_calculation)

                    tgb.text("{number1} + {number2} = {sum_}")
    
                with tgb.part() as column_data:
                    tgb.table("{df}", page_size=10)
                    tgb.chart(figure = "{fig}")

if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)
