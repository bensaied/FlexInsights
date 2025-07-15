import json
import sqlite3
from flask import Flask, jsonify, render_template
from dash import Dash, html, dcc, dash_table, Input, Output, State
import plotly.express as px
import pandas as pd
from database import init_db, insert_reviews, get_reviews, update_review_approval

# Flask and Dash setup
server = Flask(__name__)
app = Dash(__name__, server=server, external_stylesheets=['/static/css/tailwind.css'], url_base_pathname='/')
app.title = 'FlexInsights'

# Load mock data
with open('mock_data.json', 'r') as f:
    mock_data = json.load(f)

# Initialize database and insert mock data
init_db()
insert_reviews(mock_data['result'])

# Flask route for Hostaway API
@server.route('/api/reviews/hostaway', methods=['GET'])
def get_hostaway_reviews():
    reviews = get_reviews()
    normalized_reviews = [
        {
            'id': r['id'],
            'type': r['type'],
            'status': r['status'],
            'rating': r['rating'],
            'publicReview': r['publicReview'],
            'categories': json.loads(r['categories']),
            'submittedAt': r['submittedAt'],
            'guestName': r['guestName'],
            'listingName': r['listingName'],
            'approved': r['approved']
        } for r in reviews
    ]
    return jsonify({'status': 'success', 'result': normalized_reviews})

# Dash Manager Dashboard Layout
app.layout = html.Div(className='container mx-auto p-4 bg-gray-100', children=[

    # Logo and Title 
    html.Div(className='mb-8', style={'textAlign': 'center'}, children=[
        html.Div(children=[
            html.Img(
                src='/static/images/flex_living_logo.png',
                style={
                    'height': '120px',
                    'objectFit': 'contain',
                    'display': 'block',
                    'marginLeft': 'auto',
                    'marginRight': 'auto'
                },
                alt='Flex Living Logo'
            )
        ]),
        html.H1('FlexInsights', className='text-3xl font-bold mt-0 text-[#035656]')
    ]),


    # Filters container
    html.Div(className='mb-8', children=[
        dcc.Dropdown(
            id='listing-filter',
            options=[{'label': 'All Listings', 'value': 'all'}] + [
                {'label': name, 'value': name} for name in set(r['listingName'] for r in get_reviews())
            ],
            value='all',
            className='mb-4 bg-white border border-gray-300 rounded-md p-2 text-gray-800 focus:border-teal-500 focus:ring focus:ring-teal-200'
        ),
        dcc.Dropdown(
            id='category-filter',
            options=[
                {'label': 'All Categories', 'value': 'all'},
                {'label': 'Cleanliness', 'value': 'cleanliness'},
                {'label': 'Communication', 'value': 'communication'},
                {'label': 'Respect House Rules', 'value': 'respect_house_rules'}
            ],
            value='all',
            className='bg-white border border-gray-300 rounded-md p-2 text-gray-800 focus:border-teal-500 focus:ring focus:ring-teal-200'
        )
    ]),

    # Table with spacing
    html.Div(style={'marginTop': '150px'}, children=[
        dash_table.DataTable(
            id='reviews-table',
            columns=[
                {'name': 'ID', 'id': 'id'},
                {'name': 'Listing', 'id': 'listingName'},
                {'name': 'Guest', 'id': 'guestName'},
                {'name': 'Review', 'id': 'publicReview'},
                {'name': 'Cleanliness', 'id': 'cleanliness'},
                {'name': 'Communication', 'id': 'communication'},
                {'name': 'Respect Rules', 'id': 'respect_house_rules'},
                {'name': 'Date', 'id': 'submittedAt'},
                {'name': 'Approved', 'id': 'approved', 'type': 'text', 'presentation': 'dropdown'}
            ],
            data=[],
            editable=True,
            style_table={'overflowX': 'auto', 'backgroundColor': '#FFFFFF', 'borderRadius': '0.5rem', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'},
            style_cell={'textAlign': 'left', 'padding': '0.75rem', 'color': '#1F2937'},
            style_header={'backgroundColor': '#335755', 'color': '#FFFFFF', 'fontWeight': '600', 'padding': '0.75rem'},
            style_data_conditional=[
                {'if': {'row_index': 'odd'}, 'backgroundColor': '#F9FAFB'},
                {'if': {'state': 'active'}, 'backgroundColor': '#2DD4BF', 'color': '#FFFFFF'}
            ],
            dropdown={
                'approved': {
                    'options': [
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ]
                }
            }
        )
    ]),

    # Chart
    html.H2('Performance Trends', className='text-2xl font-bold mt-6 mb-4 text-[#335755] text-center'),
    dcc.Graph(id='rating-trend', className='bg-white rounded-lg shadow p-4')
])



# Dash callbacks
@app.callback(
    [Output('reviews-table', 'data'),
     Output('rating-trend', 'figure')],
    [Input('listing-filter', 'value'),
     Input('category-filter', 'value')]
)
def update_dashboard(listing, category):
    reviews = get_reviews()
    df = pd.DataFrame([
        {
            'id': r['id'],
            'listingName': r['listingName'],
            'guestName': r['guestName'],
            'publicReview': r['publicReview'],
            'cleanliness': next((c['rating'] for c in json.loads(r['categories']) if c['category'] == 'cleanliness'), None),
            'communication': next((c['rating'] for c in json.loads(r['categories']) if c['category'] == 'communication'), None),
            'respect_house_rules': next((c['rating'] for c in json.loads(r['categories']) if c['category'] == 'respect_house_rules'), None),
            'submittedAt': r['submittedAt'],
            'approved': r['approved']
        } for r in reviews
    ])
    
    if listing != 'all':
        df = df[df['listingName'] == listing]
    if category != 'all':
        df = df[df[category].notnull()]
    
    table_data = df.to_dict('records')
    
    trend_fig = px.line(
        df.groupby('listingName').mean(numeric_only=True).reset_index(),
        x='listingName',
        y=['cleanliness', 'communication', 'respect_house_rules'],
        title='Average Ratings by Listing',
        color_discrete_sequence=['#335755', '#2DD4BF', '#FEF3C7'] 
    )
    trend_fig.update_layout(
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='#FFFFFF',
        font_color='#1F2937'
    )
    
    return table_data, trend_fig

@app.callback(
    Output('reviews-table', 'data', allow_duplicate=True),
    Input('reviews-table', 'data'),
    prevent_initial_call=True
)
def update_approval(data):
    for row in data:
        update_review_approval(row['id'], row['approved'])
    return data

# Flask route for public review display
@server.route('/reviews/<listing>')
def reviews_page(listing):
    reviews = get_reviews()
    approved_reviews = [
        {
            'id': r['id'],
            'guestName': r['guestName'],
            'publicReview': r['publicReview'],
            'submittedAt': r['submittedAt'],
            'reviewCategory': json.loads(r['categories'])
        } for r in reviews if r['approved'] and r['listingName'] == listing
    ]
    return render_template('reviews.html', listing=listing, reviews=approved_reviews)

# Flask route to serve Dash app at root
@server.route('/')
def index():
    return app.index()

if __name__ == '__main__':
    server.run(debug=True)