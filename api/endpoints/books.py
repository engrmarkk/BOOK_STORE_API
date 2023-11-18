from flask import Blueprint, request, jsonify
from api.models import Books
from api.decorator import admin_required


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
            # image = data.get('image')
            category = data.get('category')
            if not title or not author or not description or not category:
                return jsonify({"message": "All fields are required"}), 400
            if (
                    not "title" in data or not "author" in data or not "description" in data or not "image" in data or not "category" in data):
                return jsonify({"message": "All fields are required"}), 400
            book = Books(title=title, author=author, description=description, image=image, category=category)
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
