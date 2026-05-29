import requests


def fetch_references(topic):

    references = []

    sample_refs = [
        f"https://scholar.google.com/scholar?q={topic.replace(' ', '+')}",
        f"https://pubmed.ncbi.nlm.nih.gov/?term={topic.replace(' ', '+')}",
        f"https://arxiv.org/search/?query={topic.replace(' ', '+')}&searchtype=all",
        "https://www.nature.com/",
        "https://www.sciencedirect.com/",
        "https://jamanetwork.com/",
        "https://www.nih.gov/",
        "https://www.who.int/",
        "https://www.ncbi.nlm.nih.gov/",
        "https://pmc.ncbi.nlm.nih.gov/"
    ]

    # Validate URLs
    for url in sample_refs:

        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                references.append(url)

        except:
            pass

    return references