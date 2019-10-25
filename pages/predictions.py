import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from joblib import load
pipeline = load('assets/pipeline.joblib')
ufc_fighter1 = pd.read_csv('assets/ufc_fighter1.csv')
ufc_fighter2 = pd.read_csv('assets/ufc_fighter2.csv')

from app import app


column1 = dbc.Col(
    [
        dcc.Markdown(
        '## Predictions', className='mb-5'
        ),
        

        dcc.Markdown('##### First Fighter'),
        dcc.Input(
        id='fighter1',
        placeholder="Enter a fighter's name",
        # fighter_match = ufc_fighter1[ufc_fighter1['fighter1'].str.match(id)],
        type='text',
        value='',
        className='mb-3'
),
        dcc.Markdown('##### Second Fighter'),
        dcc.Input(
        id='fighter2',
        placeholder="Enter a fighter's name",
        type='text',
        value='',
        className='mb-3'
        ),


        dcc.Markdown('##### Is this a title fight?'),
        dcc.Dropdown(
        id='title',
        options=[
        {'label': 'Yes', 'value': 't'},
        {'label': 'No', 'value': 'f'},
        ],
        className='mb-3',
    value='f'
),

        dcc.Markdown("##### What's the weight class?"),
        dcc.Dropdown(
        id='weightclass',
        options=[
        {'label': 'Featherweight', 'value': 'Featherweight'},
        {'label': 'Lightweight', 'value': 'Lightweight'},
        {'label': 'Welterweight', 'value': 'Welterweight'},
        {'label': 'Middleweight', 'value': 'Middleweight'},
        {'label': 'Light Heavyweight', 'value': 'Light Heavyweight'},
        {'label': 'Heavyweight', 'value': 'Heavyweight'}
        ],
        className='mb-3',
    value='Middleweight'
) 
 

    ],
    md=4,
)

column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1, column2])