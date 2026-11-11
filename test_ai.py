
from backend.ai_agent import search_products

query = (
    "Find en ny gaming-PC med RTX 5070, "
    "32 GB RAM og mindst 1 TB SSD "
    "til under 10.000 kr. i Danmark. "
    "Den skal være på lager."
)

print("PrisMentor søger på nettet...\n")

result = search_products(query)

print(result)
