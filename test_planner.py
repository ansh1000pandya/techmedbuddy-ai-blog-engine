from app.agents.planner_agent import (
    generate_tutorial_plan
)

plan = generate_tutorial_plan(
    "blast",
)

print(plan)