from flask import render_template, send_file


def make_endpoints(app, backend):
    """Constructs the endpoints that display content for the wiki."""

    cats = [
        {
            "name": "Slalom Sammy",
            "slug": "slalom-sammy",
            "image": "slalom-sammy"
        },
        {
            "name": "Nefarious Purpuss",
            "slug": "nefarious-purpuss",
            "image": "random-cat-skiing"
        }
    ]

    @app.route("/")
    def home():
        return render_template("home.html", page_name="Cats on Skis", cats=cats)

    @app.route("/about")
    def about():
        return render_template("about.html", page_name="About Cats on Skis", cats=cats)

    @app.route("/pages/<name>")
    def pages(name):
        matching_cat = next((cat for cat in cats if cat["slug"] == name), None)

        if not matching_cat:
            return "Cat not found", 404

        cat_name = matching_cat["name"]
        cat_image = matching_cat["image"]
        cat_info = backend.get_wiki_page(name)

        return render_template("cat_page.html",
                               page_name=cat_name,
                               cat_name=cat_name,
                               cat_image=cat_image,
                               cat_info=cat_info)

    @app.route("/images/<image>")
    def images(image):
        return send_file(backend.get_image(image), mimetype='image/jpeg')
