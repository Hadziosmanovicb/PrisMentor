
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def search_products(query: str):
    response = client.responses.create(
        model="gpt-6-astra",
        tools=[{"type": "web_search"}],
        instructions=(
            "Du er PrisMentor, en dansk AI-shoppingassistent. "
            "Find produkter hos danske butikker. "
            "Kontroller pris, specifikationer og lagerstatus, "
            "hvor det er muligt. "
            "Angiv produktlinks som kilder. "
            "Opfind aldrig priser eller produkter. "
            "Fortæl tydeligt, hvis noget ikke kan bekræftes."
        ),
        input=query
    )

    return response.output_text
