from google import genai
import config
import json

client = genai.Client(api_key=config.GEMINI_API_KEY)


def analyze_news(text, link):
    """Create prompt and return json with results"""

    prompt = f"""
    Analise a notícia abaixo sobre cartões de crédito e milhas.
    Retorne SOMENTE um JSON válido, sem texto adicional, com:
    - "resumo": string com 2-3 frases resumindo a notícia
    - "impacto": string com exatamente um destes valores: "Positivo", "Negativo" ou "Neutro"
    - "link": "{link}"

    Notícia: {text}
    """

    response = client.models.generate_content(
        model='gemini-2.-flash',
        contents=prompt
    )

    # Clean Json response
    clean = response.text.strip().removeprefix("```json").removesuffix("```").strip()
    result = json.loads(clean)
    return result