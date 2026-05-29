import requests


def validate_references(references):

    validated = []

    for ref in references:

        doi = ref.get("doi")

        # Skip if DOI missing
        if not doi:
            continue

        try:

            doi_url = f"https://doi.org/{doi}"

            response = requests.get(
                doi_url,
                timeout=5
            )

            # DOI resolves successfully
            if response.status_code == 200:

                ref["verified"] = True

                validated.append(ref)

        except Exception:

            continue

    return validated