from shiny import App, ui

app_ui = ui.page_navbar(
    ui.nav_panel("Menu", "Welcome to my dashboard!"),
    ui.nav_panel(
        "Page 1",
        ui.layout_sidebar(
            ui.sidebar("Sidebar"),
            "Main Page 1", 
            ui.markdown("example *markdown*"),
            ui.layout_columns(
                ui.card(ui.card_header("Title"), "Graph 1"),
                ui.card(ui.card_header("Title"), "Table 1")
            ),
             ui.layout_columns(
                ui.card(ui.card_header("Title"), "Graph 2"),
                ui.card(ui.card_header("Title"), "Table 2")
            )
        )
    ),
    ui.nav_panel(
        "Page 2",
        ui.layout_sidebar(
            ui.sidebar("Sidebar"),
            "Main Page 2"
        ),
    ),
    title=ui.div(
        ui.span("Malu, the Economist", style="font-weight:600;"),
        style="display:flex; align-items:center;"
    ),
    bg="black",
    inverse=True,
    window_title="Malu, the economist",
    sidebar=ui.sidebar( "Global side bar")
)

def server(input, output, session):
    ...

app = App(app_ui, server)
