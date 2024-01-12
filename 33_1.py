import dash
from dash import dash_table
import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html
import KRM.sorce

df=KRM.sorce.extract()
df