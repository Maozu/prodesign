from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from . import main
from .forms import NameForm
from .. import db
from ..dealwith import dealwith
# from  ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('xue.html')
# def index():
#     name = None
#     match_attributes = ''
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#         match_attributes = dealwith.main(name)
#     return render_template('xue.html',
#                            name=match_attributes,
#                            known=session.get('know', False),
#                            current_time=datetime.utcnow())


@main.route('/sendAjax2', methods=['POST'])
def sendAjax2():
    # name = None
    # match_attributes = ''
    # form = NameForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     form.name.data = ''
    #     match_attributes = dealwith.main(name)
    data = request.get_data()
    match_attributes = dealwith.main(data)
    print("得到了哦" + match_attributes)
    return render_template('ans.html',
                           name=match_attributes,
                           known=session.get('know', False),
                           current_time=datetime.utcnow())

