from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime
import time
app = Flask(__name__)


@app.route('/')
def home():
    user = {"email": "ontoology@ontoology.com", "is_authenticated": True}
    repos = [{
        "id": "123",
        "url": "test_repo",
        "last_used": "2020-02-21",
        "state": "Ready",
        "owner": "no",
        "previsual": False,
        "previsual_page_available": False,
        "notes": "notes",
        "progress": 0.0,
        "user": user
    },
        {
            "id": "456",
            "url": "demo2",
            "last_used": "2020-02-01",
            "state": "Ready",
            "owner": "no",
            "previsual": True,
            "previsual_page_available": True,
            "notes": "notes",
            "progress": 100,
            "user": user
        }
    ]
    request = {"user":user, "session": {"avatar_url": "https://github.githubassets.com/images/modules/logos_page/Octocat.png"}}

    return render_template('home.html', repos=repos,request=request, user=user, num_of_users= 0, num_of_repos= 0)


@app.route('/profile')
def profile():
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
        },
        {
            "id": "456",
            "url": "demo2",
            "last_used": datetime.now(),
            "state": "Ready",
            "owner": "no",
            "previsual": True,
            "previsual_page_available": True,
            "notes": "notes",
            "progress": 100,
            "user": user
        }
    ]
    request = {"user":user, "session": {"avatar_url": "https://github.githubassets.com/images/modules/logos_page/Octocat.png"}}
    pnames = [
        {
            'id': "3823",
            'name': "test",
            'user': user,
            'repo': repos[0],
            'ontology': 'another'
        },
        {
            'id': "98123",
            'name': "demo2",
            'user': user,
            'repo': repos[1],
            'ontology': 'one'
        }
    ]
    return render_template('profile.html', repos=repos, manager=False, request=request, user=user, pnames=pnames,strftime=time.strftime)


#    return render(request, 'profile.html', {'repos': repos, 'pnames': PublishName.objects.filter(user=user),
#                                            'error': error_msg, 'manager': request.user.email in get_managers()})




if __name__ == "__main__":
    app.run(debug=True)
