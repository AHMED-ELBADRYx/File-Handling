import sqlite3

def connect():
    return sqlite3.connect("application.db")

def initialize_db():
    with connect() as db:
        cr = db.cursor()
        cr.execute("""
            CREATE TABLE IF NOT EXISTS skills (
                skill TEXT,
                progress INTEGER,
                user_id INTEGER
            )
        """)
        db.commit()

def fetch_skills(user_id):
    with connect() as db:
        cr = db.cursor()
        cr.execute("SELECT * FROM skills WHERE user_id = ?", (user_id,))
        return cr.fetchall()

def skill_exists(skill, user_id):
    with connect() as db:
        cr = db.cursor()
        cr.execute("SELECT 1 FROM skills WHERE skill = ? AND user_id = ?", (skill, user_id))
        return cr.fetchone() is not None

def add_skill(skill, progress, user_id):
    with connect() as db:
        cr = db.cursor()
        cr.execute("INSERT INTO skills (skill, progress, user_id) VALUES (?, ?, ?)", (skill, progress, user_id))
        db.commit()

def update_skill(skill, progress, user_id):
    with connect() as db:
        cr = db.cursor()
        cr.execute("UPDATE skills SET progress = ? WHERE skill = ? AND user_id = ?", (progress, skill, user_id))
        db.commit()

def delete_skill(skill, user_id):
    with connect() as db:
        cr = db.cursor()
        cr.execute("DELETE FROM skills WHERE skill = ? AND user_id = ?", (skill, user_id))
        db.commit()