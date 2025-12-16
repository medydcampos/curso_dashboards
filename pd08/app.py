# libraries
from shiny import App, render, ui

# User interface
app_ui = ui.page_navbar(
    ui.nav_panel("Page 1", "Page Content 1"),
    ui.nav_panel("Page 2", "Page Content 2"),
    #ui.nav_control(ui.a("My website", href = "https://sites.google.com/view/marialuizacampos/home")) ## Including a link directly in the navigation bar
    ui.nav_menu(
        "Know more",
        ui.nav_control(ui.a("My website", href = "https://sites.google.com/view/marialuizacampos/home")),
        ui.nav_control(ui.a("My last blog", href = "https://malutheeconomist.substack.com/p/econometrics-revisited-when-sexy"))
    ),
     title=ui.div(
        ui.span("Malu, the Economist", style="font-weight:600;"),
        style="display:flex; align-items:center;"
    ),
    bg = "black",
    inverse = True,
    window_title = "Malu, the economist"
)

# server 
def server(input, output, session):
    ...

# app shiny/dashboard shiny
app = App(app_ui, server)
