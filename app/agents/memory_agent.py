import json


class TutorialMemory:

    def __init__(self):

        self.completed_sections = []

        self.completed_concepts = []

        self.prompt_history = []
        
        

    # -----------------------------------
    # SECTION MEMORY
    # -----------------------------------

    def add_section(
        self,
        section_name
    ):

        if section_name not in self.completed_sections:

            self.completed_sections.append(
                section_name
            )

    def get_completed_sections(self):

        return self.completed_sections

    # -----------------------------------
    # CONCEPT MEMORY
    # -----------------------------------

    def add_concepts(
        self,
        concepts
    ):

        for concept in concepts:
            concept = (concept.replace("-", "").replace("*", "").strip().lower())   

            if (
                concept
                not in self.completed_concepts
            ):

                self.completed_concepts.append(
                    concept
                )

    def get_completed_concepts(self):

        return self.completed_concepts
    def get_concepts(self):
        return self.completed_concepts

    # -----------------------------------
    # PROMPT MEMORY
    # -----------------------------------

    def add_prompt(
        self,
        section,
        prompt
    ):

        self.prompt_history.append(
            {
                "section": section,
                "prompt": prompt
            }
        )

    def get_prompt_history(self):

        return self.prompt_history

    # -----------------------------------
    # EXPORT MEMORY
    # -----------------------------------

    def export_memory(
        self,
        file_name="tutorial_memory.json"
    ):

        memory = {

            "completed_sections":
                self.completed_sections,

            "completed_concepts":
                self.completed_concepts,

            "prompt_history":
                self.prompt_history
        }

        with open(
            file_name,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                memory,
                file,
                indent=4
            )

        return file_name