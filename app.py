from flask import Flask, render_template

app = Flask(__name__)

articles = [
    {"Id": 1, "Title": "Article 1", "Content": "Full article"},
]


@app.route("/")
def index():
    return render_template("index.html", articles=articles)


@app.route("/article/<int:article_id>")
def article(article_id):
    try:
        article = next((a for a in articles if a["Id"] == article_id), None)
        if article:
            return render_template("article.html", article=article)
        else:
            return "Article not found", 404
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(debug=True)
