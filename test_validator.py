from app.services.pubmed_service import search_pubmed

from app.services.reference_validator import validate_references


topic = "AI in Personalized Medicine"

references = search_pubmed(topic)

validated = validate_references(references)

print("\nVALIDATED REFERENCES:\n")

for i, ref in enumerate(validated, start=1):

    print(f"{i}. {ref['title']}")

    print("Journal:", ref["journal"])

    print("Year:", ref["year"])

    print("DOI:", ref["doi"])

    print("Verified:", ref["verified"])

    print("-" * 50)