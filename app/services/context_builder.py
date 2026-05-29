def build_context(

    topic="",
    custom_context="",
    pdf_text="",
    doi_metadata="",
    journal_source=""

):

    context_parts = []

    # ---------------- TOPIC ---------------- #

    if topic:

        context_parts.append(
            f"TOPIC:\n{topic}"
        )

    # ---------------- JOURNAL SOURCE ---------------- #

    if journal_source:

        context_parts.append(
            f"JOURNAL SOURCE:\n{journal_source}"
        )

    # ---------------- CUSTOM CONTEXT ---------------- #

    if custom_context:

        context_parts.append(
            f"CUSTOM CONTEXT:\n{custom_context}"
        )

    # ---------------- DOI METADATA ---------------- #

    if doi_metadata:

        context_parts.append(
            f"DOI METADATA:\n{doi_metadata}"
        )

    # ---------------- PDF CONTENT ---------------- #

    if pdf_text:

        trimmed_pdf = pdf_text[:5000]

        context_parts.append(
            f"PDF CONTENT:\n{trimmed_pdf}"
        )

    # ---------------- FINAL CONTEXT ---------------- #

    final_context = "\n\n".join(
        context_parts
    )

    return final_context