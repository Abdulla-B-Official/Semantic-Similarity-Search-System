from flask import Flask, jsonify, request, send_from_directory

from backend.config import HOST, PORT, DEBUG, TOP_RESULTS_COUNT
from backend.search.search_engine import search_documents


app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")


@app.route("/css/<path:filename>")
def serve_css(filename):
    return send_from_directory("frontend/css", filename)


@app.route("/js/<path:filename>")
def serve_js(filename):
    return send_from_directory("frontend/js", filename)


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "online",
        "model": "FastText",
        "documents_loaded": True
    })


@app.route("/api/search", methods=["POST"])
def search():
    request_data = request.get_json()

    if not request_data or not request_data.get("query"):
        return jsonify({
            "error": "Please enter a search query."
        }), 400

    search_query = request_data["query"].strip()

    search_results = search_documents(
        search_query,
        TOP_RESULTS_COUNT
    )

    return jsonify({
        "query": search_query,
        "results": search_results
    })


if __name__ == "__main__":
    print(f"Starting Semantic Similarity Search System...")
    print(f"Open: http://{HOST}:{PORT}")

    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )