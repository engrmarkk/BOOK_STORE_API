from flask import Blueprint, request, jsonify
from api.models import Books, BookGenre
from api.decorator import admin_required
from flask_jwt_extended import jwt_required


books_blp = Blueprint('books', __name__)


@books_blp.route('/books', methods=['POST', 'PATCH', 'DELETE'])
@admin_required
def books():
    try:
        if request.method == 'POST':
            data = request.json

            title = data.get('title')
            author = data.get('author')
            description = data.get('description')
            genre = data.get('genre')

            genre_ = BookGenre.query.filter_by(genre=genre).first()
            if not genre_:
                return jsonify({"message": "Genre does not exist"}), 400

            if not title or not author or not description or not genre:
                return jsonify({"message": "All fields are required"}), 400
            if (
                    not "title" in data or not "author" in data or not "description" in data or not "image" in data or not "category" in data):
                return jsonify({"message": "All fields are required"}), 400
            book = Books(title=title, author=author, description=description, genre=genre)
            book.save()
            return jsonify({"message": "Book added successfully"}), 201
        if request.method == 'PATCH':
            data = request.json
            title = data.get('title')
            author = data.get('author')
            description = data.get('description')
            image = data.get('image')
            category = data.get('category')
            book_id = data.get('book_id')
            if not title or not author or not description or not image or not category or not book_id:
                return jsonify({"message": "All fields are required"}), 400
            if (
                    not "title" in data or not "author" in data or not "description" in data or not "image" in data or not "category" in data or not "book_id" in data):
                return jsonify({"message": "All fields are required"}), 400
            book = Books.query.filter_by(id=book_id).first()
            if not book:
                return jsonify({"message": "Book does not exist"}), 400
            book.title = title
            book.author = author
            book.description = description
            book.image = image
            book.category = category
            book.save()
            return jsonify({"message": "Book updated successfully"}), 201
        if request.method == 'DELETE':
            data = request.json
            book_id = data.get('book_id')
            if not book_id:
                return jsonify({"message": "All fields are required"}), 400
            if not "book_id" in data:
                return jsonify({"message": "All fields are required"}), 400
            book = Books.query.filter_by(id=book_id).first()
            if not book:
                return jsonify({"message": "Book does not exist"}), 400
            book.delete()
            return jsonify({"message": "Book deleted successfully"}), 200
    except KeyError:
        return jsonify({"message": "All fields are required"}), 400
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400


@books_blp.route('/books', methods=['GET'])
def get_books():
    try:
        books = Books.query.all()
        books_list = []
        for book in books:
            books_list.append({
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "description": book.description,
                "image": book.image,
                "category": book.category
            })
        return jsonify({"message": "success", "books": books_list}), 200
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400



list_of_genre = [
    "General",
    "Fiction",
    "Non-fiction",
    "Fantasy",
    "Science fiction",
    "Westerns",
    "Romance",
    "Thriller",
    "Mystery",
    "Detective story",
    "Dystopia",
    "Biographies",
    "Autobiographies",
    "Historical fiction",
    "Horror",
    "Action and adventure",
    "Comedy",
    "Satire",
    "Tragedy",
    "Drama",
    "Mythology",
    "Poetry",
    "Speeches",
    "Science",
    "Travel",
    "Children's",
    "Young adult",
    "Cookbooks",
    "Diaries",
    "Journals",
    "Prayer books",
    "Series",
    "Trilogy",
    "How-to",
    "Art",
    "Photography",
    "Self-help",
    "Health",
    "Fitness",
    "Diets",
    "Spirituality",
    "Religion",
    "History",
    "Math",
    "Anthology",
    "Encyclopedias",
    "Dictionaries",
    "Comics",
    "Magazines",
    "Newspapers",
    "Manuals",
    "Guide books",
    "Almanacs",
    "Atlases",
    "Catalogs",
    "Pamphlets",
    "Brochures",
    "Leaflets",
    "Flyers",
    "Newsletters",
    "Press releases",
    "Yearbooks",
    "Government publications",
    "Reports",
    "Internet",
    "Websites",
    "Blogs",
    "Emails",
    "Text messages",
    "Instant messages",
    "Social media posts",
    "Letters",
    "Essays",
    "Short stories",
    "Novellas",
    "Novels",
    "Poems",
    "Screenplays",
    "Plays",
    "Biographies",
    "Autobiographies",
    "Memoirs",
    "Speeches",
    "Orations",
    "Debates",
    "Sermons",
    "Diaries",
    "Journals",
    "Interviews",
    "Textbooks",
    "Cookbooks",
    "Manuals",
    "Guide books",
    "Retellings",
    "Commentaries",
    "Dictionaries",
    "Encyclopedias"
]


@books_blp.route('/book_genre', methods=['POST'])
@admin_required
def book_genre():
    try:
        print(len(list_of_genre), "length")
        for genre in list_of_genre:
            book_genre_ = BookGenre(genre=genre)
            book_genre_.save() if not BookGenre.query.filter_by(genre=genre).first() else print("genre already exists")
        return jsonify({"message": "Book genre added successfully"}), 201
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400


@books_blp.route('/book_genre', methods=['GET'])
def get_book_genre():
    try:
        book_genre = BookGenre.query.all()
        book_genre_list = []
        for genre in book_genre:
            book_genre_list.append({
                "id": genre.id,
                "genre": genre.genre
            })
        return jsonify({"message": "success", "book_genre": book_genre_list}), 200
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400
