import numpy as np
import pandas as pd
import plotly
import plotly.figure_factory as ff
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import math



########### Define your variables
beers=['Mouse Stout', 'Mouse Dog IPA', 'Mouse Porter', 'Mouse Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='lightblue'
color2='darkgreen'
mytitle='test'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
githublink='https://github.com/vickymei/flying-dog-beers'
sourceurl='https://nlrcareers.com/'
#############################

df = pd.read_csv('data.csv')
loc = pd.read_csv('locations.csv')

map = go.Figure(data=go.Choropleth(
    locations=df['code'],  # Spatial coordinates
    z=df['number'],  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='blues',
    name='',
    text=df['state'],
    colorbar_title="Number of CPA in state",
))

size = [8 * (int(math.log(x)) + 1) for x in loc['size']]

map.add_trace(go.Scattergeo(
    lat=loc['lat'],
    lon=loc['lon'],
    # locationssrc = loc['city'],
    # locations = loc['city'],
    marker={
        "line": {"width": 1}, "size": size
    },
    mode="markers+ text",
    # hoverinfo = ['text','name'],
    text=['', '', '<b>Boston', '', '', '', '<b>Chicago', '', '', '<b>Denver',
          '', '', '', '<b>Los Angeles', '', '', '<b>New York', '<b>Palo Alto',
          '', '<b>Philadelphia', '<b>Portland', '', '', '<b>Redwood City',
          '', '', '', '', '<b>San Francisco', '', '<b>Seattle', '',
          '', '', '', '<b>San Diego'],
    textfont={
        'color': 'LightSalmon',
        'size': 12
    },
    textposition=['top center', 'top center', 'top center', 'top center', 'top center', 'top center', 'top center',
                  'top center',
                  'top center', 'top center', 'top center', 'top center', 'top center', 'top center', 'top center',
                  'top center',
                  'top left', 'middle left', 'top center', 'top center', 'top center', 'top center', 'top center',
                  'bottom center',
                  'top center', 'top center', 'top center', 'top center', 'top center', 'top center', 'top center',
                  'top center',
                  'top center', 'top center', 'top center', 'top center'],
    hoverinfo='text',
    name='',
    hovertext=['Armonk<br><br>' + 'Reynolds + Rowella, LLP: 2 openings',
               'Baltimore<br><br>' + 'Miles & Stockbridge: 3 openings',
               'Boston<br><br>' + 'Baker Newman Noyes: 10 openings<br>Blum Shapiro: 7 openings<br>Cooley: 4 openings<br>DGC (DiCicco, Gulman & Company): 2 openings',
               'Braintree<br><br>' + 'Kevin P. Martin & Associates, P.C.:2 openings',
               'Carlisle<br><br>' + 'Smith Elliot Kerns & Company, LLC (SEKC): 1 opening',
               'Chambersburg<br><br>' + 'Smith Elliot Kerns & Company, LLC (SEKC): 1 opening',
               'Chicago<br><br>' + 'Apercen Partners LLC: 3 openings<br>BDO USA, LLP - NW Region: 1 opening<br>FGMK LLC: 5 openings<br>Topel Forman, L.L.C.: 2 openings',
               'Clifton<br><br>' + 'Sax LLP: 4 openings',
               'Cranston<br><br>' + 'Blum Shapiro: 2 openings',
               'Denver<br><br>' + 'Topel Forman, L.L.C.: 2 openings',
               'Encino<br><br>' + 'Gelfand, Rennert & Feldman, LLC: 2 openings',
               'Irvine<br><br>' + 'Windes: 2 openings',
               'Long Beach<br><br>' + 'Windes: 2 openings',
               'Los Angeles<br><br>' + 'Gelfand, Rennert & Feldman, LLC: 2 openings<br>Jeffer Mangels Butler & Mitchell LLP (JMBM): 3 openings<br>SheppardMullin: 1 opening',
               'Manchester<br><br>' + 'Baker Newman Noyes: 5 openings',
               'Menlo Park<br><br>' + 'McDermott Will & Emery : 1 opening',
               'New York<br><br>' + 'Apercen Partners LLC: 4 openings<br>Cooley: 6 openings<br>Garvey Schubert Barer: 1 opening<br>Mintz Levin Cohn Ferris Glovsky and Popeo PC: 1 opening',
               'Palo Alto<br><br>' + 'Apercen Partners LLC: 2 openings<br>Cooley: 6 openings<br>Jones Day: 2 openings<br>SheppardMullin: 1 opening<br>Sutter Hill Ventures: 2 openings<br>Wilson Sonsini Goodrich & Rosati: 8 openings',
               'Pasadena<br><br>' + 'Apercen Partners LLC: 2 openings',
               'Philadelphia<br><br>' + 'Drucker & Scaccetti: 4 openings',
               'Portland<br><br>' + 'Apercen Partners LLC: 2 openings<br>Baker Newman Noyes: 5 openings',
               'Portsmouth<br><br>' + 'Baker Newman Noyes: 4 openings',
               'Quincy<br><br>' + 'Blum Shapiro: 3 openings',
               'Redwood City<br><br>' + 'Seiler LLP: 10 openings',
               'Ridgefield<br><br>' + 'Reynolds + Rowella, LLP: 3 openings',
               'San Jose<br><br>' + 'BDO USA, LLP - NW Region: 1 opening<br>Seiler LLP: 3 openings',
               'Santa Rosa<br><br>' + 'BPM LLP: 2 openings',
               'Sacramento<br><br>' + 'Apercen Partners LLC: 1 opening',
               'San Francisco<br><br>' + 'Apercen Partners LLC: 2 openings<br>BDO USA, LLP - NW Region: 4 openings<br>Cooley: 5 openings<br>Eisner Amper: 4 openings<br>Lindquist, von Husen & Joyce LLP: 3 openings<br>Seiler LLP: 12 openings<br>SheppardMullin: 1 opening<br>Wilson Sonsini Goodrich & Rosati: 3 openings',
               'West Hardford<br><br>' + 'Blum Shapiro: 4 openings',
               'Seattle<br><br>' + 'BDO USA, LLP - NW Region: 1 opening',
               'Shelton<br><br>' + 'Blum Shapiro: 4 openings',
               'White Plains<br><br>' + 'Gelfand, Rennert & Feldman, LLC: 2 openings',
               'Timonium<br><br>' + 'Katz Abosch: 3 openings',
               'Wilmington<br><br>' + 'Gelfand, Rennert & Feldman, LLC: 2 openings',
               'San Diego<br><br>' + 'Wilson Sonsini Goodrich & Rosati: 1 opening<br>Cooley: 2 openings'
               ],
    showlegend=False
    # textfont = {"size":10}
))

map.update_layout(
    title_text='<b>2019 Certified Public Accountants by State',
    geo_scope='usa',  # limite map scope to USA

)
#############################


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='2019 Certified Public Accountants by State'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=map,
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source bleongs to', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
