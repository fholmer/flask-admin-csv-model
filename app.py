import csv
import pathlib

import flask_admin as admin
from flask import Flask

from flask_admin_csv_model.contrib.csv import Model, ModelView, TextField

app = Flask(__name__)
app.config["SECRET_KEY"] = "123456790"

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


@app.route("/")
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


if __name__ == "__main__":
    import logging

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    admin = admin.Admin(app, name="Example: Csv")
    admin.add_view(DataAdmin(Data))
    app.run(debug=True)
