from app.services.pubmed_service import get_verified_references

refs = get_verified_references(
    "AI in Personalized Medicine",
    required_count=5
)

for ref in refs:
    print(ref)