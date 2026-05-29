from app.services.image_service import fetch_images


topic = "AI in Personalized Medicine"

images = fetch_images(topic)

print("\nFETCHED IMAGES:\n")

for img in images:

    print(img)