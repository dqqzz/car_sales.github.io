
from dash import Dash,html
import dash_bootstrap_components as dbc
from layout import create_layout

app = Dash(external_stylesheets=[dbc.themes.COSMO])
app.title = "Car Sales Data"
app._favicon = "assets/favicon.ico"

app.layout = create_layout(app)
if __name__ == "__main__":
    app.run_server(debug=True)







