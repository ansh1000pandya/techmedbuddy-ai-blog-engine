from app.pipelines.blog_pipeline import generate_blog

topic = "Role of Biostatistics in Drug Discovery"

blog = generate_blog(topic)

print("\nFINAL BLOG:\n")

print(blog)