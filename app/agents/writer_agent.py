from app.services.llm_router import (
    generate_llm_response
)

from app.prompts.writer_prompt import (
    get_section_writer_prompt
)


def generate_section(

    topic,

    section,

    previous_context

):

    writer_prompt = (
        get_section_writer_prompt(

            topic,

            section,

            previous_context

        )
    )

    response = generate_llm_response(
        writer_prompt
    )

    return response