# flask-admin-csv-model

A CSV-file model backend for Flask-Admin

## Warning

- This is a beta version. Not ready for production.

## Installation

Open command line and and install using pip:

```bash

$ pip install flask-admin-csv-model

```

## Usage

The first step is to initialize an empty admin interface for your Flask app:

```python

from flask import Flask
import flask_admin as admin

app = Flask(__name__)
app.config["SECRET_KEY"] = "123456790"


@app.route("/")
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


if __name__ == "__main__":

    admin = admin.Admin(app, name="Example: Csv")
    app.run(debug=True)

```

Adding Model View:

```python

import pathlib
import csv
from flask_admin_csv_model.contrib.csv import ModelView, Model, TextField

csv_file = pathlib.Path("./example.csv")
with csv_file.open() as f:
    dialect = csv.Sniffer().sniff(f.read(1024))

class BaseModel(Model):
    class Meta:
        file: pathlib.Path = csv_file
        dialect: csv.Dialect = dialect

class Data(BaseModel):
    first = TextField()
    second = TextField()
    third = TextField()
    fourth = TextField()
    fifth = TextField()

class DataAdmin(ModelView):
    can_delete = True
    can_create = True
    can_edit = True

admin = admin.Admin(app, name="Example: Csv")
admin.add_view(DataAdmin(Data))

```

### To run this example

1. Clone the repository:

    ```bash
    git clone https://github.com/fholmer/flask-admin-csv-model
    cd flask-admin-csv-model
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install requirements:

    ```bash
    pip install -r requirements.txt
    ```


4. Run the application::

    ```bash
    python app.py
    ```
