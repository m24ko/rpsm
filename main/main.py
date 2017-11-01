from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from MockDB import DB

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        song_url = form.youtube_url.data
        DB.data.append(song_url)
        form.reset()
        redirect(url_for('index'))
    return render_template("soundmit.html", form=form, a="vlada")


@app.route("/soundlist")
def soundlist():
    return render_template("soundlist.html", songs=DB.data)


@app.route("/about")
def about():
    return render_template("about.html")


# Soundmit Form Class
class RegisterForm(Form):
    youtube_url = StringField('', [validators.DataRequired(),
                                   validators.URL()])

    def reset(self):
        self.youtube_url.data = ''


if __name__ == '__main__':
    app.run()
