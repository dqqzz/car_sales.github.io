from dash import Dash,html,dcc
import dash_bootstrap_components as dbc
import pandas as pd
import os
from .util import get_data
from .ids import *


def render(app):
    df = get_data()
    all_cars = df["Manufacturer"].unique()
    car_makes = [{"label":make, "value":make} for make in all_cars]
    return  html.Div(
    [
        dcc.Dropdown(
            options = car_makes,
            placeholder="Choose your car",
            value='BMW',
            className="mb-3",
            id = DROPDOWN,
            multi=False,
        ),
    ])









