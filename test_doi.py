from app.services.doi_service import fetch_doi_metadata

doi = "10.1038/s41591-021-01614-0"

paper = fetch_doi_metadata(doi)

print(paper)