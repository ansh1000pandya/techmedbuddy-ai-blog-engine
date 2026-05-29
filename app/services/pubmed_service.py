from Bio import Entrez
import requests
import time

# ------------------------------------------------ #
# CONFIG
# ------------------------------------------------ #

Entrez.email = "pandya.ansh1000@gmail.com"


# ------------------------------------------------ #
# DOI VALIDATION
# ------------------------------------------------ #

def validate_doi(doi):

    try:

        clean_doi = doi.strip()

        url = f"https://doi.org/{clean_doi}"

        response = requests.get(
            url,
            timeout=10
        )

        return response.status_code == 200

    except:
        return False


# ------------------------------------------------ #
# FETCH PAPERS FROM PUBMED
# ------------------------------------------------ #

def fetch_pubmed_papers(
    topic,
    max_results=50
):

    try:

        search_handle = Entrez.esearch(
            db="pubmed",
            term=topic,
            retmax=max_results
        )

        search_results = Entrez.read(
            search_handle
        )

        ids = search_results["IdList"]

        papers = []

        for pubmed_id in ids:

            try:

                fetch_handle = Entrez.efetch(
                    db="pubmed",
                    id=pubmed_id,
                    rettype="medline",
                    retmode="text"
                )

                paper_text = fetch_handle.read()

                papers.append(paper_text)

                time.sleep(0.2)

            except:
                continue

        return papers

    except Exception as e:

        print("PubMed Fetch Error:", e)

        return []


# ------------------------------------------------ #
# EXTRACT PAPER DATA
# ------------------------------------------------ #

def extract_reference_data(paper_text):

    lines = paper_text.split("\n")

    title = ""
    journal = ""
    year = ""
    doi = ""

    for line in lines:

        if line.startswith("TI  -"):
            title = line.replace(
                "TI  -",
                ""
            ).strip()

        elif line.startswith("JT  -"):
            journal = line.replace(
                "JT  -",
                ""
            ).strip()

        elif line.startswith("DP  -"):
            year = line.replace(
                "DP  -",
                ""
            ).strip()

        elif "doi" in line.lower():

            doi = line.strip()

    return {
        "title": title,
        "journal": journal,
        "year": year,
        "doi": doi
    }


# ------------------------------------------------ #
# VERIFIED REFERENCES ENGINE
# ------------------------------------------------ #

def get_verified_references(
    topic,
    max_results=20
):

    papers = fetch_pubmed_papers(
        topic,
        max_results=100
    )

    verified_references = []

    seen_titles = set()

    for paper in papers:

        try:

            data = extract_reference_data(
                paper
            )

            title = data["title"]
            journal = data["journal"]
            year = data["year"]
            doi = data["doi"]

            # Skip incomplete references

            if not title:
                continue

            if title in seen_titles:
                continue

            # Validate DOI if exists

            if doi:

                possible_doi = doi.split()[-1]

                valid = validate_doi(
                    possible_doi
                )

                if not valid:
                    continue

            formatted_reference = (
                f"{title}. "
                f"{journal}. "
                f"{year}. "
                f"{doi}"
            )

            verified_references.append(
                formatted_reference
            )

            seen_titles.add(title)

            # Stop when bucket full

            if len(verified_references) >= max_results:
                break

        except:
            continue

    return verified_references