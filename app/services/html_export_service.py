import markdown


def convert_blog_to_html(blog_content):

    html_body = markdown.markdown(

        blog_content,

        extensions=["tables"]

    )

    full_html = f"""
    <!DOCTYPE html>

    <html>

    <head>

        <meta charset="UTF-8">

        <title>TechMedBuddy Blog</title>

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

            code {{

                background-color: #f4f4f4;

                padding: 2px 6px;

                border-radius: 4px;

            }}

            pre {{

                background-color: #f4f4f4;

                padding: 15px;

                overflow-x: auto;

                border-radius: 6px;

            }}

            blockquote {{

                border-left: 4px solid #999;

                padding-left: 15px;

                color: #555;

            }}

        </style>

    </head>

    <body>

        {html_body}

    </body>

    </html>
    """

    return full_html