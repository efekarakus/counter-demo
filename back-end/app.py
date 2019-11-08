from flask import Flask
import json

app = Flask(__name__)

dogs = {
    "Bowie" : {
        "owner": "Austin",
        "breed": "cutey",
        "language": "go-fetch"
    },
    "Clyde": {
        "owner": "Allie",
        "breed": "sweety",
        "language": "pawthon"
    },
    "Rowdy": {
        "owner": "David",
        "breed": "Dalmatian",
        "language": "catlin"
    },
    "Keno": {
        "owner": "Penghao",
        "breed": "Miniature Schnauzer",
        "language": "cloud-fur-mation"
    }
}

@app.route('/')
def get_dogs():
    return json.dumps(dogs)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
