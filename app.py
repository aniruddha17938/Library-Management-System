from flask import Flask, jsonify, request, render_template
from data_structures import LibraryGraph, Book

app = Flask(__name__)

# Initialize Library Graph
library = LibraryGraph()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-category", methods=["POST"])
def add_category():
    data = request.json
    category_name = data.get("name")
    library.add_category(category_name)
    return jsonify({"message": f"Category '{category_name}' added successfully."})

@app.route("/add-book", methods=["POST"])
def add_book():
    data = request.json
    category_name = data.get("category")
    title = data.get("title")
    author = data.get("author")

    if category_name in library.categories:
        book = Book(id=len(library.categories[category_name].list_books()) + 1, title=title, author=author)
        library.categories[category_name].add_book(book)
        return jsonify({"message": f"Book '{title}' added to '{category_name}'."})
    else:
        return jsonify({"error": f"Category '{category_name}' does not exist."}), 400

@app.route("/list-books", methods=["GET"])
def list_books():
    return jsonify(library.get_all_books())

@app.route("/search-books", methods=["GET"])
def search_books():
    query = request.args.get("query", "").lower()
    results = []
    for category in library.categories.values():
        current = category.head
        while current:
            if query in current.book.title.lower():
                results.append(vars(current.book))
            current = current.next
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
