from flask import Flask, redirect, url_for, render_template
from flask import request
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
    reques = {"user": user,
              "session": {"avatar_url": "https://github.githubassets.com/images/modules/logos_page/Octocat.png"}}

    return render_template('home.html', repos=repos, request=reques, user=user, num_of_users=0, num_of_repos=0)


@app.route('/profile')
def profile():
    repo = request.args.get("repo")
    if repo:
        return profile_ontologies(repo)
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
    reques = {"user": user,
              "session": {"avatar_url": "https://github.githubassets.com/images/modules/logos_page/Octocat.png"}}
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
    return render_template('profile.html', repos=repos, manager=False, request=reques, user=user, pnames=pnames,
                           strftime=time.strftime)


#    return render(request, 'profile.html', {'repos': repos, 'pnames': PublishName.objects.filter(user=user),
#                                            'error': error_msg, 'manager': request.user.email in get_managers()})


def profile_ontologies(repo):
    return {
        'ontologies': [
            {
                "ar2dtool": True,
                "ontology": "/ontology1-with-themis.owl",
                "oops": True,
                "owl2jsonld": True,
                "pname": "j123",
                "published": True,
                "themis_results": 90,
                "widoco": True, },
            {
                "ar2dtool": True,
                "ontology": "/ontology2-without-themis.owl",
                "oops": True,
                "owl2jsonld": True,
                "pname": "j123",
                "published": True,
                "widoco": True, },
            {
                "ar2dtool": True,
                "ontology": "/ontology3-no-published.owl",
                "oops": True,
                "owl2jsonld": True,
                "pname": "j123",
                "published": False,
                "widoco": True, },
        ]
    }

@app.route('/repository/<int:index>')
def repository (index):
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
    if(0<=index and index<len(repos)):    
        index=index
    else:
        index=-1
    reques = {"user": user,
              "session": {"avatar_url": "https://github.githubassets.com/images/modules/logos_page/Octocat.png"}}
    return render_template('repository.html', repos=repos, manager=False, request=reques, user=user, pnames=pnames,
                           strftime=time.strftime,ontologies=profile_ontologies(repos[index]), index=index)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
