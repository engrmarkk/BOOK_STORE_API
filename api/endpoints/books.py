from flask import Blueprint, request, jsonify
from api.models import Books, BookGenre
from api.decorator import admin_required
from flask_jwt_extended import jwt_required

books_blp = Blueprint('books', __name__)


@books_blp.route('/books', methods=['POST'])
@jwt_required()
@admin_required
def books():
    try:
        data = request.json

        title = data.get('title')
        author = data.get('author')
        description = data.get('description')
        genre = data.get('genre')
        quantity = data.get('quantity')

        # check the instance of the quantity
        if not isinstance(quantity, int):
            return jsonify({"message": "Quantity must be an integer"}), 400

        genre_ = BookGenre.query.filter_by(genre=genre).first()
        if not genre_:
            return jsonify({"message": "Genre does not exist"}), 400

        if not title or not author or not description or not genre:
            return jsonify({"message": "All fields are required"}), 400

        book = Books(title=title, author=author, description=description, genre=genre, quantity=quantity)
        book.save()
        return jsonify({"message": "Book added successfully"}), 201
    except KeyError:
        return jsonify({"message": "All fields are required"}), 400
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400


@books_blp.route('/books', methods=['GET'])
@jwt_required()
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
                "genre": book.genre
            })
        return jsonify({"message": "success", "books": books_list}), 200
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400


# operation on a single book
@books_blp.route('/books/<book_id>', methods=['GET', 'PATCH', 'DELETE'])
@admin_required
def get_single_book(book_id):
    try:
        book = Books.query.filter_by(id=book_id).first()
        if not book:
            return jsonify({"message": "Book does not exist"}), 400
        if request.method == 'GET':
            return jsonify({
                "message": "success",
                "book": {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "description": book.description,
                    "image": book.image,
                    "genre": book.genre
                }
            }), 200
        elif request.method == 'PATCH':
            data = request.json

            title = data.get('title')
            author = data.get('author')
            description = data.get('description')
            genre = data.get('genre')
            quantity = data.get('quantity')

            genre_ = BookGenre.query.filter_by(genre=genre).first()
            if not genre_:
                return jsonify({"message": "Genre does not exist"}), 400

            book.title = title if title else book.title
            book.author = author if author else book.author
            book.description = description if description else book.description
            book.genre = genre if genre else book.genre
            book.quantity = quantity if quantity else book.quantity
            book.update()
            return jsonify({"message": "Book updated successfully"}), 200
        elif request.method == 'DELETE':
            book.delete()
            return jsonify({"message": "Book deleted successfully"}), 200
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
