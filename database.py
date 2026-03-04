import mysql.connector 
import config

def connect_database():
    """Connection with database"""
    try:
        con = mysql.connector.connect(
            host=config.DB_HOST,
            database=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
        )
        return con
    except mysql.connector.Error as e:
        print(f"Error trying connect with database {e}")

def save_news_on_db(news):
    """Save all news in database"""
    try:
        con = connect_database()
        cursor = con.cursor()

        for article in news:
            cursor.execute("""
                INSERT IGNORE INTO noticias_financeiras
                (titulo, link, data_publicacao, texto_completo)
                VALUES (%s, %s, %s, %s)
""", (article['titulo'], article['link'], article['data_publicacao'], article['texto_completo']))
        con.commit()
        cursor.close()
        con.close()
    
    except mysql.connector.Error as e:
        print(f"Error saving data on db: {e}")

def fetch_pending_news():
    """Fetch all pending"""
    try:
        con = connect_database()
        cursor = con.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, texto_completo, link
            FROM noticias_financeiras
            WHERE status_processamento = 'PENDENTE'
        """)

        pending_news = cursor.fetchall()
        cursor.close()
        con.close()
        return pending_news
    
    except mysql.connector.Error as e:
        print(f"Error fetching pending news: {e}")
        return []

def update_news(id, summary, impact):
    """Update fields on database"""
    try:
        con = connect_database()
        cursor = con.cursor()

        cursor.execute("""
            UPDATE noticias_financeiras
            SET resumo_ia = %s, impacto_ia = %s, status_processamento = 'PROCESSADO'
            WHERE id = %s
        """, (summary, impact, id))

        con.commit()
        cursor.close()
        con.close()
    
    except mysql.connector.Error as e:
        print(f"Error updating news: {e}")