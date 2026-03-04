import scraper
import database
import ai_analyzer

print("Starting data extration...")
news = scraper.extract_last_news()

print(f"{len(news)} news found. Saving into database...")
database.save_news_on_db(news)

print("Fetching pending news for AI analysing...")
pending = database.fetch_pending_news()

print(f"{len(pending)} pending news. Starting AI Analysing...")
for article in pending:
    result = ai_analyzer.analyze_news(article['texto_completo'], article['link'])
    database.update_news(article['id'], result['resumo'], result['impacto'])
    print(f"Analyzed: {article['link']} - Impact: {result['impacto']}")

print("Process finished!")