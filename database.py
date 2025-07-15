import sqlite3
import json

def init_db():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            type TEXT,
            status TEXT,
            rating REAL,
            publicReview TEXT,
            categories TEXT,
            submittedAt TEXT,
            guestName TEXT,
            listingName TEXT,
            approved INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def insert_reviews(reviews):
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    for review in reviews:
        categories = json.dumps(review['reviewCategory'])
        c.execute('''
            INSERT OR REPLACE INTO reviews (id, type, status, rating, publicReview, categories, submittedAt, guestName, listingName, approved)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            review['id'], review['type'], review['status'], review['rating'],
            review['publicReview'], categories, review['submittedAt'],
            review['guestName'], review['listingName'], 0
        ))
    conn.commit()
    conn.close()

def get_reviews():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reviews')
    rows = c.fetchall()
    conn.close()
    return [
        {
            'id': r[0], 'type': r[1], 'status': r[2], 'rating': r[3],
            'publicReview': r[4], 'categories': r[5], 'submittedAt': r[6],
            'guestName': r[7], 'listingName': r[8], 'approved': r[9]
        } for r in rows
    ]

def update_review_approval(review_id, approved):
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('UPDATE reviews SET approved = ? WHERE id = ?', (approved, review_id))
    conn.commit()
    conn.close()