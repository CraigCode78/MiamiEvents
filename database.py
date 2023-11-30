import sqlite3

DATABASE_FILENAME = 'events.db'

def init_db():
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            audience TEXT,
            commercial_potential TEXT,
            partnership_opportunities TEXT
            -- Add other fields as per your scorecard
        )
    ''')
    conn.commit()
    conn.close()

def insert_event(form_data):
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO events (name, type, audience, commercial_potential, partnership_opportunities)
        VALUES (?, ?, ?, ?, ?)
    ''', (form_data['name'], form_data['type'], form_data['audience'], form_data['commercial_potential'], form_data['partnership_opportunities']))
    conn.commit()
    conn.close()
