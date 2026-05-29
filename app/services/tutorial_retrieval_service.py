import requests
from bs4 import BeautifulSoup


TRUSTED_SOURCES = {

    "python": [

        "https://www.w3schools.com/python/",

        "https://www.geeksforgeeks.org/python-programming-language-tutorial/",

    ],

    "bioinformatics": [

        "https://rosalind.info/problems/locations/",

        "https://www.biostars.org/",

    ],

    "clinical informatics": [

        "https://www.ncbi.nlm.nih.gov/home/tutorials/",

    ]

}


def retrieve_tutorial_sources(topic):

    topic_lower = topic.lower()

    matched_links = []

    for key in TRUSTED_SOURCES:

        if key in topic_lower:

            matched_links.extend(
                TRUSTED_SOURCES[key]
            )

    tutorial_context = ""

    for url in matched_links:

        try:

            response = requests.get(
                url,
                timeout=10
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            paragraphs = soup.find_all("p")

            extracted_text = ""

            for p in paragraphs[:10]:

                extracted_text += (
                    p.get_text() + "\n"
                )

            tutorial_context += f"""

            SOURCE:
            {url}

            CONTENT:
            {extracted_text}

            """

        except Exception as e:

            print(
                f"Tutorial Retrieval Error: {e}"
            )

    return tutorial_context