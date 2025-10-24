import os
import sqlite3
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, dash_table

def build_dash_app(db_path: str):
    app = Dash(__name__, suppress_callback_exceptions=True)
    app.title = "Book Analytics Dashboard"

    # load distinct genres & year range
    conn = sqlite3.connect(db_path)
    genres_df = pd.read_sql_query("SELECT genre_name FROM genres ORDER BY genre_name;", conn)
    year_df = pd.read_sql_query("SELECT MIN(publication_year) as miny, MAX(publication_year) as maxy FROM books;", conn)
    conn.close()

    genres = genres_df['genre_name'].tolist()
    min_year, max_year = int(year_df['miny'][0]), int(year_df['maxy'][0])

    # Layout: filters + charts
    app.layout = html.Div([
        html.H1("Book Analytics Dashboard"),
        html.Div([
            html.Div([
                html.Label("Select Genres"),
                dcc.Dropdown(options=[{'label': g, 'value': g} for g in genres],
                             value=genres, # default all selected
                             multi=True,
                             id='genre-filter'),
            ], style={'width': '45%', 'display': 'inline-block', 'verticalAlign': 'top'}),
            html.Div([
                html.Label("Publication Year Range"),
                dcc.RangeSlider(min=int(min_year), max=int(max_year), 
                                value=[int(min_year), int(max_year)], # default full range
                                marks={y: str(y) if y % 10 == 0 else '' for y in range(min_year, max_year+1)},
                                id='year-range'),
                html.Div(id='year-range-output', style={'marginTop': 10})
            ], style={'width': '50%', 'display': 'inline-block', 'paddingLeft': '20px'})
        ], style={'marginBottom': 30}),

        # 1st row: Average rating by genre and revenue vs votes
        html.Div([
            html.Div([dcc.Graph(id='avg-rating-genre')], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([dcc.Graph(id='revenue-vs-votes')], style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
        ]),

        # 2nd row: Book count by genre over years
        html.Div([
            dcc.Graph(id='count-genre-years')
        ], style={'marginTop': 30}),

        # 3rd row: Top-rated books by year selection
        html.Div([
            html.H3("Top-rated books"),
            html.Div([
                html.Label("Select Year for Top Books"),
                dcc.Dropdown(options=[{'label': 'All Years', 'value': 'ALL'}] + 
                             [{'label': str(y), 'value': str(y)} for y in range(min_year, max_year+1)],
                             value='ALL',
                             id='top-year-dropdown'),
            ], style={'width': '30%'}),
            html.Div(id='top-books-table', style={'marginTop': 10})
        ], style={'marginTop': 30, 'marginBottom': 60})
    ], style={'width': '95%', 'margin': 'auto'})

    # Callback: update text for year range
    @app.callback(
        Output('year-range-output', 'children'),
        Input('year-range', 'value')
    )
    def update_year_text(year_range):
        return f"Showing books published between {year_range[0]} and {year_range[1]}"

    # Callback: avg rating by genre
    @app.callback(
        Output('avg-rating-genre', 'figure'),
        Input('genre-filter', 'value'),
        Input('year-range', 'value'),
    )
    def update_avg_rating(genres_selected, year_range):
        conn = sqlite3.connect(db_path)
        q = f"""
        SELECT g.genre_name AS genre, AVG(b.rating) AS avg_rating, COUNT(*) AS cnt
        FROM books b
        JOIN genres g ON b.genre_id = g.genre_id
        WHERE g.genre_name IN ({','.join('?' for _ in genres_selected)})
          AND b.publication_year BETWEEN ? AND ?
        GROUP BY g.genre_name
        ORDER BY avg_rating DESC;
        """
        params = genres_selected + [year_range[0], year_range[1]]
        df = pd.read_sql_query(q, conn, params=params)
        conn.close()
        fig = px.bar(df, x='genre', y='avg_rating', text='cnt',
                     labels={'avg_rating': 'Average Rating', 'genre': 'Genre'},
                     title="Average Book Rating by Genre")
        fig.update_traces(texttemplate='%{text}', textposition='outside')
        fig.update_layout(yaxis=dict(range=[0, 5]))
        return fig

    # Callback: revenue vs votes scatter
    @app.callback(
        Output('revenue-vs-votes', 'figure'),
        Input('genre-filter', 'value'),
        Input('year-range', 'value'),
    )
    def update_revenue_vs_votes(genres_selected, year_range):
        conn = sqlite3.connect(db_path)
        q = f"""
        SELECT b.title, g.genre_name as genre, b.publication_year, b.revenue_millions as revenue, b.votes
        FROM books b JOIN genres g ON b.genre_id = g.genre_id
        WHERE g.genre_name IN ({','.join('?' for _ in genres_selected)}) AND b.publication_year BETWEEN ? AND ?
        LIMIT 5000;
        """
        params = genres_selected + [year_range[0], year_range[1]]
        df = pd.read_sql_query(q, conn, params=params)
        conn.close()
        fig = px.scatter(df, x='votes', y='revenue',
                         labels={'votes': 'Votes', 'revenue': 'Revenue (Millions)'},
                         title="Revenue vs Votes")
        # fig.update_layout(xaxis_type='log')
        return fig

    # Callback: book count by genre over years
    @app.callback(
        Output('count-genre-years', 'figure'),
        Input('genre-filter', 'value'),
        Input('year-range', 'value'),
    )
    def update_count_genre_years(genres_selected, year_range):
        conn = sqlite3.connect(db_path)
        q = f"""
        SELECT b.publication_year as year, g.genre_name as genre, COUNT(*) as cnt
        FROM books b JOIN genres g ON b.genre_id = g.genre_id
        WHERE g.genre_name IN ({','.join('?' for _ in genres_selected)}) AND b.publication_year BETWEEN ? AND ?
        GROUP BY g.genre_name, b.publication_year
        ORDER BY b.publication_year;
        """
        params = genres_selected + [year_range[0], year_range[1]]
        df = pd.read_sql_query(q, conn, params=params)
        conn.close()
        fig = px.line(df, x='year', y='cnt', color='genre',
                      labels={'cnt': 'Book Count', 'year': 'Publication Year'},
                      title="Book Count by Genre Over Years")
        return fig

    # Callback: top-rated books by year
    @app.callback(
        Output('top-books-table', 'children'),
        Input('top-year-dropdown', 'value'),
        Input('genre-filter', 'value'),
        Input('year-range', 'value'),
    )
    def update_top_books(selected_year, genres_selected, year_range):
        conn = sqlite3.connect(db_path)
        params = []
        where_parts = []
        # genres filter
        if genres_selected:
            where_parts.append(f"g.genre_name IN ({','.join('?' for _ in genres_selected)})")
            params.extend(genres_selected)
        # year filter: either specific year or within range
        if selected_year != 'ALL':
            where_parts.append("b.publication_year = ?")
            params.append(int(selected_year))
        else:
            where_parts.append("b.publication_year BETWEEN ? AND ?")
            params.extend([year_range[0], year_range[1]])
        where_clause = " AND ".join(where_parts)
        q = f"""
        SELECT b.title, g.genre_name as genre, b.publication_year as year, b.rating, b.votes, b.revenue_millions as revenue
        FROM books b JOIN genres g ON b.genre_id = g.genre_id
        WHERE {where_clause}
        ORDER BY b.rating DESC, b.votes DESC
        LIMIT 20;
        """
        df = pd.read_sql_query(q, conn, params=params)
        conn.close()
        if df.empty:
            return html.Div("No books found for the selected filters.")
        # Build a Dash DataTable
        table = dash_table.DataTable(
            columns=[{"name": c, "id": c} for c in df.columns],
            data=df.to_dict('records'),
            page_size=10,
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left', 'padding': '5px'},
            style_header={'fontWeight': 'bold'},
        )
        return html.Div([
            html.H4(f"Top {len(df)} books (by rating)"),
            table
        ])

    return app


def main():
    DB_DIR = "outputs"
    # os.makedirs(DB_DIR, exist_ok=True)
    db_path = os.path.join(DB_DIR, "books.db")

    # 4) start dash app
    app = build_dash_app(db_path)
    print("Starting Dash server at http://127.0.0.1:8050")
    app.run(debug=True)

if __name__ == "__main__":
    main()
