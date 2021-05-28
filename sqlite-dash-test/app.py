import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import data

income_category = data.income_category()
education_category = data.education_category()

app = dash.Dash(__name__)

# Income Category Chart
def income_chart():
    df = income_category
    trace1 = go.Bar(x=df.index,
                        y=df['Credit_Limit'],
                        name='Credit Limit',
                        yaxis='y1')
    trace2 = go.Bar(x=df.index,
                        y=df['Total_Revolving_Bal'],
                        name='Total Revolving Balance',
                        yaxis='y1')
    trace3 = go.Scatter(x=df.index,
                    y=df['Avg_Utilization_Ratio'],
                    name='Utilization Ratio',
                    mode='lines+markers',
                    yaxis='y2'
                    )
    data = [trace1, trace2,trace3]
    layout = go.Layout(title='By Income Category',
                       yaxis=dict(title='$'),
                       yaxis2=dict(title='Utilization Ratio',
                                   overlaying='y',
                                   side='right'))
    return go.Figure(data=data, layout=layout)

# Education Level Chart
def education_chart():
    df = education_category
    trace1 = go.Bar(x=df.index,
                        y=df['Credit_Limit'],
                        name='Credit Limit',
                        yaxis='y1')
    trace2 = go.Bar(x=df.index,
                        y=df['Total_Revolving_Bal'],
                        name='Total Revolving Balance',
                        yaxis='y1')
    trace3 = go.Scatter(x=df.index,
                    y=df['Avg_Utilization_Ratio'],
                    name='Utilization Ratio',
                    mode='lines+markers',
                    yaxis='y2'
                    )
    data = [trace1, trace2,trace3]
    layout = go.Layout(title='By Education Level',
                       yaxis=dict(title='$'),
                       yaxis2=dict(title='Utilization Ratio',
                                   overlaying='y',
                                   side='right'))
    return go.Figure(data=data, layout=layout)


# app layout
app.layout = html.Div(

    children=[

        html.H1(children="Consumer Credit Card Analysis",),

        html.P(
            children="""Analyze composition of a consumer credit
            card portfolio.""",
        ),

        dcc.Graph(figure=income_chart()),
        dcc.Graph(figure=education_chart())

    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)