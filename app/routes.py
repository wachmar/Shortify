import re
from app.models import Urls
from app import app, db
from random import choice
import string
from flask import render_template, request, flash, redirect, url_for
from app.forms import AddUrl


def shorten_url(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddUrl()

    if form.validate_on_submit():
        url = form.url.data
        custom_id = form.custom_id.data

        # Checking if url was provided
        if not url:
            flash('Please provide a url!')
            return redirect(url_for('index'))
        #
        if custom_id:
            custom_id = re.sub('[^A-Za-z0-9]+', '', custom_id)[0:7]

        # Checking if exists
        if custom_id and Urls.query.filter_by(url_short=custom_id).first() is not None:
            flash('This custom id already exists, please choose another one!')
            return redirect(url_for('index'))

        if not custom_id:
            custom_id = shorten_url(7)

        # Adding url to DB
        new_link = Urls(
            url_long=url,
            url_short=custom_id
        )
        db.session.add(new_link)
        db.session.commit()
        url_short_full = request.host_url + custom_id

        return render_template('index.html', url_short_full=url_short_full, form=form)

    return render_template('index.html', form=form)

@app.route('/<url_short>')
def redirect_url(url_short):
    print(url_short)
    link = Urls.query.filter_by(url_short=url_short).first()
    print(link)
    if link:
        if link.url_long.startswith("http://"):
            url = link.url_long
        else:
            url = "http://"+link.url_long
        return redirect(url)
    else:
        flash('Sorry, we do not know this URL. But, you can create one!')
        return redirect(url_for('index'))

@app.route('/url_list')
def url_list():
    # Display list of urls from the db
    urls = Urls.query.all()
    return render_template('list.html', urls=urls)
