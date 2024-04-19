# Import the libraries - only relevant!!! 
import dash
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from dash import dash_table
import dash_bootstrap_components as dbc
import pandas as pd 
import plotly.express as px

# Read in your super clean csv!
df_monthly_agg = pd.read_csv('./data/all_monthly_agg_data.csv')
df_geo2 = pd.read_csv('./data/all_yearly_agg_data.csv')
df_temp = pd.read_csv('./data/df_temp_daily_data.csv')

# Create some masks - one for each city and one for all combined
df_berlin = df_monthly_agg[df_monthly_agg['city']=='Berlin']
df_berlin = df_berlin[['year','city', 'country', 'lat', 'lon','month_of_year', 'month_year', 'avg_temp_c', 'max_temp_c', 'min_temp_c']]
df_tokyo = df_monthly_agg[df_monthly_agg['city']=='Tokyo']
df_tokyo = df_tokyo[['year','city', 'country', 'lat', 'lon','month_of_year', 'month_year', 'avg_temp_c', 'max_temp_c', 'min_temp_c']]
df_wellington = df_monthly_agg[df_monthly_agg['city']=='Wellington']
df_wellington = df_wellington[['year','city', 'country', 'lat', 'lon','month_of_year', 'month_year', 'avg_temp_c', 'max_temp_c', 'min_temp_c']]
df_cities =df_monthly_agg[df_monthly_agg['city'].isin(['Berlin', 'Tokyo', 'Wellington'])]

# Create a table for Berlin - TO USE
table1 = dash_table.DataTable(df_berlin.to_dict('records'),
                                  [{"name": i, "id": i} for i in df_berlin.columns],
                               style_data={'color': '#fd7e14','backgroundColor': "#060606"},
                              style_header={
                                  'backgroundColor': 'rgb(210, 210, 210)',
                                  'color': 'black','fontWeight': 'bold'}, 
                                     style_table={ 
                                         'minHeight': '500px', 'height': '500px', 'maxHeight': '500px',
                                         'minWidth': '900px', 'width': '900px', 'maxWidth': '900px',
                                         'marginLeft': 'auto', 'marginRight': 'auto',
                                         'marginTop': 0, 'marginBottom': "20"}
                                     )

# Create a bar graph for Berlin
fig1 = px.bar(df_berlin,
              x='month_year',
              y='avg_temp_c',
              color='avg_temp_c',
              color_continuous_scale='Peach',
              title='Average Monthly Temperature in Berlin - April 2023 to April 2024',
              height=500,
              width=1100)

# Adjust temperature scale
fig1.update_traces(marker_coloraxis=None)  # Remove automatic coloring of bars based on temperature

# Add legend for avg_temp_c
fig1.update_traces(name='Temperature (°C)')

# Change y-axis scale
fig1.update_yaxes(tickvals=[2023, 2024], ticktext=["2023", "2024"], dtick=1)  # Change y-axis ticks to display only 2023 and 2024 and set dtick to 1

# Update x-axis labels rotation
fig1.update_xaxes(tickangle=45)  # Rotate x-axis labels by 45 degrees

# Update layout for better readability
fig1.update_layout(
    plot_bgcolor="#060606",
    paper_bgcolor="#060606",
    font_color="#fd7e14",
    #margin=dict(l=80, r=20, t=20, b=20)  # Adjust margin to provide more space for y-axis labels
)

graph1 = dcc.Graph(figure=fig1)

# Create a table for Tokyo - TO USE
table2 = dash_table.DataTable(df_tokyo.to_dict('records'),
                                  [{"name": i, "id": i} for i in df_tokyo.columns],
                               style_data={'color': '#fbc02d','backgroundColor': "#060606"},
                              style_header={
                                  'backgroundColor': 'rgb(210, 210, 210)',
                                  'color': 'black','fontWeight': 'bold'}, 
                                     style_table={ 
                                         'minHeight': '500px', 'height': '500px', 'maxHeight': '500px',
                                         'minWidth': '900px', 'width': '900px', 'maxWidth': '900px',
                                         'marginLeft': 'auto', 'marginRight': 'auto',
                                         'marginTop': 0, 'marginBottom': "20"}
                                     )

# Create a bar graph for Tokyo
fig2 = px.bar(df_tokyo,
              x='month_year',
              y='avg_temp_c',
              color='avg_temp_c',
              color_continuous_scale='Peach',
              title='Average Monthly Temperature in Tokyo - April 2023 to April 2024',
              height=500,
              width=1100)

# Adjust temperature scale
fig2.update_traces(marker_coloraxis=None)  # Remove automatic coloring of bars based on temperature

# Add legend for avg_temp_c
fig2.update_traces(name='Temperature (°C)')

# Change y-axis scale
fig2.update_yaxes(tickvals=[2023, 2024], ticktext=["2023", "2024"], dtick=1)  # Change y-axis ticks to display only 2023 and 2024 and set dtick to 1

# Update x-axis labels rotation
fig2.update_xaxes(tickangle=45)  # Rotate x-axis labels by 45 degrees

# Update layout for better readability
fig2.update_layout(
    plot_bgcolor="#060606",
    paper_bgcolor="#060606",
    font_color="#fbc02d",
    #margin=dict(l=80, r=20, t=20, b=20)  # Adjust margin to provide more space for y-axis labels
)

graph2 = dcc.Graph(figure=fig2)

# Create a table for Wellington - TO USE
table3 = dash_table.DataTable(df_wellington.to_dict('records'),
                                  [{"name": i, "id": i} for i in df_wellington.columns],
                               style_data={'color': '#ffcc80','backgroundColor': "#060606"},
                              style_header={
                                  'backgroundColor': 'rgb(210, 210, 210)',
                                  'color': 'black','fontWeight': 'bold'}, 
                                     style_table={ 
                                         'minHeight': '500px', 'height': '500px', 'maxHeight': '500px',
                                         'minWidth': '900px', 'width': '900px', 'maxWidth': '900px',
                                         'marginLeft': 'auto', 'marginRight': 'auto',
                                         'marginTop': 0, 'marginBottom': "20"}
                                     )

# Create a bar graph for Wellington
fig3 = px.bar(df_wellington,
              x='month_year',
              y='avg_temp_c',
              color='avg_temp_c',
              color_continuous_scale='Peach',
              title='Average Monthly Temperature in Wellington - April 2023 to April 2024',
              height=500,
              width=1100)

# Adjust temperature scale
fig3.update_traces(marker_coloraxis=None)  # Remove automatic coloring of bars based on temperature

# Add legend for avg_temp_c
fig3.update_traces(name='Temperature (°C)')

# Change y-axis scale
fig3.update_yaxes(tickvals=[2023, 2024], ticktext=["2023", "2024"], dtick=1)  # Change y-axis ticks to display only 2023 and 2024 and set dtick to 1

# Update x-axis labels rotation
fig3.update_xaxes(tickangle=45)  # Rotate x-axis labels by 45 degrees

# Update layout for better readability
fig3.update_layout(
    plot_bgcolor="#060606",
    paper_bgcolor="#060606",
    font_color="#ffcc80",
    #margin=dict(l=80, r=20, t=20, b=20)  # Adjust margin to provide more space for y-axis labels
)

graph3 = dcc.Graph(figure=fig3)

# Barplot of average daily temperature for all three cities 
fig4 = px.bar(df_temp,
              x='date',
              y='avg_temp_c',
              color='city',
              color_discrete_map={'Berlin': '#fd7e14', 'Tokyo': '#fbc02d', 'Wellington': '#ffcc80'},
              range_y=[-10, 70],
              title='Average Daily Temperatures in all locations - April 2023 to April 2024',
              height=600,
              width=1100)
fig4 = fig4.update_layout(
        plot_bgcolor="#060606", paper_bgcolor="#060606", font_color="white"
    )
graph4 = dcc.Graph(figure=fig4)

# Create a line graph for ALL locations - TO USE
fig5 = px.line(df_cities, 
              x='month_year', 
              y='avg_temp_c', 
              height=500,
              width=1100,
              title="Average Monthly Temperatures: April 2023 - April 2024, All Locations", 
              markers=True,
              color='city',
              color_discrete_map={'Berlin': '#fd7e14', 'Tokyo': '#fbc02d', 'Wellington': '#ffcc80'}
             )
fig5 = fig5.update_layout(
        plot_bgcolor="#060606", paper_bgcolor="#060606", font_color="white"
    )
graph5 = dcc.Graph(figure=fig5)

# All locations in a scatterplot - TO USE
fig6 = px.scatter(df_cities, 
                 x='month_year', 
                 y='max_temp_c',
                 size = 'max_temp_c',
                 height=400,
                 width=1100,
                 color='city',
                 color_discrete_map={'Berlin': '#fd7e14', 'Tokyo': '#fbc02d', 'Wellington': '#ffcc80'},
                 title="Maximum Monthly Temperatures: Berlin, Tokyo, Wellington"
             )
fig6 = fig6.update_layout(
        plot_bgcolor="#060606", paper_bgcolor="#060606", font_color="white"
    )
graph6 = dcc.Graph(figure=fig6)

# Animated scatterplot for average temperatures

# Sort DataFrame by month_year
df_cities = df_cities.sort_values('month_year')

# Create animated scatter plot
fig7 = px.scatter(df_cities, 
                 x="month_year", 
                 y="avg_temp_c", 
                 animation_frame="month_of_year",
                 animation_group="month_year",  # Use month_year to slow down the animation and progress chronologically
                 size="avg_temp_c", 
                 color='city',
                 color_discrete_map={'Berlin': '#fd7e14', 'Tokyo': '#fbc02d', 'Wellington': '#ffcc80'},
                 range_y=[-15, 40],
                 title="Average Monthly Temperatures: April 2023 - April 2024, All Locations",
                 height=500, 
                 width=1100)

# Customize x-axis ticks
fig7 = fig7.update_xaxes(ticktext=df_cities['month_year'], #.dt.strftime('%b %Y'),  # Format tick labels as abbreviated month and year
                 tickangle=45)  # Rotate tick labels by 45 degrees
fig7 = fig7.update_layout(
        plot_bgcolor="#060606", paper_bgcolor="#060606", font_color="white")

graph7= dcc.Graph(figure=fig7)

# Scatter_mapbox for avg, max and min temp

fig8 = px.scatter_mapbox(df_geo2,
                        lat='lat', 
                        lon='lon', 
                        custom_data=['avg_temp_c', 'max_temp_c','min_temp_c', 'city'],
                        hover_data={'lat': False, 'lon':False,'avg_temp_c':True, 'max_temp_c':True, 'min_temp_c': True, 'city': False}, #to customise the data shown while hovering
                        size_max=30,
                        hover_name='city', 
                        size='avg_temp_c',
                        color='city',
                        color_discrete_map={'Berlin': '#fd7e14', 'Tokyo': '#fbc02d', 'Wellington': '#ffcc80'},
    
                        # start location and zoom level
                        zoom=4, 
                        center={'lat': 51.1657, 'lon': 10.4515}, 
                        mapbox_style='carto-positron',
                        height=500, 
                        width=1100)

fig8 = fig8.update_layout(
        plot_bgcolor="#060606", paper_bgcolor="#060606", font_color="white")

graph8 = dcc.Graph(figure=fig8)

# Creating my dash app - the skeleton

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
app.layout = html.Div([
    html.H1('Week 08 - Project Challenge - Weather API', style={'textAlign': 'center', 'color': '#e65100'}),
    html.Div(html.H3("Liam Clowes"), style={'textAlign': 'center', 'color': '#636EFA'}),
    html.Div(html.P("Checking weather in Berlin, Tokyo and Wellington to identify ideal time to organise an outside event"), style={'textAlign': 'center'}),
    html.Div([
        html.Div('Berlin', style={'backgroundColor': '#fd7e14', 'color': 'black', 'width': '900px', 'marginLeft': 'auto', 'marginRight': 'auto'}),
        table1,
        graph1,
    ]),
    html.Div([
        html.Div('Tokyo', style={'backgroundColor': '#fbc02d', 'color': 'black', 'width': '900px', 'marginLeft': 'auto', 'marginRight': 'auto'}),
        table2,
        graph2,
    ]),
    html.Div([
        html.Div('Wellington', style={'backgroundColor': '#ffcc80', 'color': 'black', 'width': '900px', 'marginLeft': 'auto', 'marginRight': 'auto'}),
        table3,
        graph3,
    ]),
    graph4,
    graph5,
    graph6,
    graph7,
    graph8
])

if __name__ == '__main__':
    app.run_server()