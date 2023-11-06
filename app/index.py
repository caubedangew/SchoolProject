from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    kw = request.args.get("keyword")
    return render_template('index.html', categories=dao.getCategories(), products=dao.getProducts(kw))


if __name__ == "__main__":
    app.run(debug=True)
