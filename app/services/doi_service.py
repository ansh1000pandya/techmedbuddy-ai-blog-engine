import requests


def fetch_doi_metadata(doi):
    """
    Fetch scientific paper metadata using DOI
    """

    url = f"https://api.crossref.org/works/{doi}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        item = data["message"]

        title = item.get("title", ["No Title"])[0]

        journal = item.get("container-title", ["Unknown Journal"])[0]

        abstract = item.get("abstract", "Abstract Not Available")

        authors = item.get("author", [])

        author_names = []

        for author in authors:
            given = author.get("given", "")
            family = author.get("family", "")
            author_names.append(f"{given} {family}")

        return {
            "doi": doi,
            "title": title,
            "journal": journal,
            "abstract": abstract,
            "authors": author_names
        }

    except Exception as e:
        return {
            "error": str(e)
        }