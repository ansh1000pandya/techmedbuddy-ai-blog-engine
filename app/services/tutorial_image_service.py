from duckduckgo_search import DDGS


def fetch_tutorial_images(topic):

    image_urls = []

    try:

        with DDGS() as ddgs:

            results = ddgs.images(

                keywords=topic,

                max_results=5

            )

            for result in results:

                if "image" in result:

                    image_urls.append(
                        result["image"]
                    )

    except Exception as e:

        print(
            f"Image Fetch Error: {e}"
        )

    return image_urls