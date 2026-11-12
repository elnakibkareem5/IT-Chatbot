import sqlite3
DB_NAME = "tickets.db"


def init_db() :
	conn = sqlite3.connect(DB_NAME)
	Cursor = conn.cursor()
	cursor.execute(CREATE TABLE IF NOT EXIST tickets (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		user_email TEXT NOT NULL,
		subject TEXT NOT NULL,
		description TEXT NOT NULL,
		status TEXT DEFAULT 'Open',
		Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
		))

	conn.commit()
	