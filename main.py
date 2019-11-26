from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, DataRequired
from flask_bootstrap import Bootstrap
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20180301 import iai_client, models


class NameForm(Form):
    name = StringField('input base64', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a string'
bootstrap = Bootstrap(app)


def getu(url):
    try:
        cred = credential.Credential("AKIDSmxtbmRO0Pn45tqeeZHjW6SZXFpLZbOy", "UmodLn1ziCbkkX5U1MRM4a3GQOAnwrV6")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "iai.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = iai_client.IaiClient(cred, "ap-chongqing", clientProfile)
        req = models.SearchFacesRequest()
        params = '{"GroupIds":["1"],"Url":"' + url + '"}'
        print(params)
        req.from_json_string(params)
        resp = client.SearchFaces(req)
        print(resp.Results)
        return resp
    except TencentCloudSDKException as err:
        return err


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    a = ''
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        a = getu(name)
    return render_template('index.html', form=form, name=a)


if __name__ == '__main__':
    app.run(debug=True)
