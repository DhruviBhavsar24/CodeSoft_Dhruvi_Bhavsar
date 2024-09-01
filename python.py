# python.py

# Step 1: Create a dataset of books with their genres
books = [
    {"title": "Harry Potter", "genre": "Fantasy"},
    {"title": "The Hobbit", "genre": "Fantasy"},
    {"title": "Dune", "genre": "Science Fiction"},
    {"title": "Ender's Game", "genre": "Science Fiction"},
    {"title": "Sherlock Holmes", "genre": "Mystery"},
    {"title": "The Da Vinci Code", "genre": "Mystery"},
]

# Step 2: Function to recommend books based on user preference
def recommend_books(preferred_genre):
    recommendations = [book["title"] for book in books if book["genre"] == preferred_genre]
    return recommendations

# Step 3: Get user preference input
user_preference = input("Enter your favorite genre (Fantasy, Science Fiction, Mystery): ")

# Step 4: Recommend books based on the input
recommended_books = recommend_books(user_preference.capitalize())

# Step 5: Display the recommendations
if recommended_books:
    print(f"\nBased on your preference for {user_preference.capitalize()} books, we recommend:")
    for book in recommended_books:
        print(f"- {book}")
else:
    print(f"\nSorry, we have no recommendations for the genre: {user_preference.capitalize()}")
