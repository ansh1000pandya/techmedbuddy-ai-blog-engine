import markdown


def export_tutorial_to_html(

    tutorial_content,

    output_file="tutorial_output.html"

):

    # ============================================
    # CONVERT MARKDOWN TO HTML
    # ============================================ #

    html_body = markdown.markdown(

        tutorial_content,

        extensions=[

            "fenced_code",

            "tables"

        ]
    )

    # ============================================
    # FULL HTML TEMPLATE
    # ============================================ #

    full_html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>Tutorial Export</title>

<style>

body {{

    font-family: Arial, sans-serif;

    margin: 40px;

    line-height: 1.8;

    background-color: #ffffff;

    color: #222222;
}}

h1, h2, h3 {{

    color: #0f172a;
}}

pre {{

    background-color: #f4f4f4;

    padding: 15px;

    border-radius: 8px;

    overflow-x: auto;
}}

code {{

    font-family: Consolas, monospace;
}}

table {{

    border-collapse: collapse;

    width: 100%;
}}

table, th, td {{

    border: 1px solid #cccccc;

    padding: 10px;
}}

</style>

</head>

<body>

{html_body}

</body>

</html>
"""

    # ============================================
    # WRITE FILE
    # ============================================ #

    with open(

        output_file,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(full_html)

    return output_file