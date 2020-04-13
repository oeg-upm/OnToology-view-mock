from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def home():
    user = {"email": "ontoology@ontoology.com", "is_authenticated": True}
    repos = [{
            "id": "123",
            "url": "test_repo",
            "last_used": datetime.now(),
            "state": "Ready",
            "owner": "no",
            "previsual": False,
            "previsual_page_available": False,
            "notes": "notes",
            "progress": 0.0,
            "user": user
        }]
    request = {"user":user, "session": {"avatar_url": "https://github.githubassets.com/images/modules/logos_page/Octocat.png"}}

    return render_template('home.html', repos=repos,request=request, user=user, num_of_users= 0, num_of_repos= 0)


if __name__ == "__main__":
    app.run(debug=True)
