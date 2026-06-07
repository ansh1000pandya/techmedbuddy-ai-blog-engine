from app.agents.tutorial_generator_agent import (
    TutorialGeneratorAgent
)

plan = {

    "tutorial_title":
        "Understanding BLAST",

    "sections": [

        {
            "id": 1,
            "title":
                "Introduction to BLAST",

            "prompt":
                "Teach beginners what BLAST is."
        },

        {
            "id": 2,
            "title":
                "Sequence Similarity",

            "prompt":
                "Explain sequence similarity."
        }
    ]
}

agent = TutorialGeneratorAgent()

tutorial = agent.generate_tutorial(

    tutorial_title=plan[
        "tutorial_title"
    ],

    selected_sections=plan[
        "sections"
    ]
)

print(tutorial)