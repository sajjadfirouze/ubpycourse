from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('home.html')


@app.route('/result', methods=['GET','POST'])
def gif():
    pic = request.files['load']
    pic.save(pic.filename)
    upload = requests.post('https://api.imagga.com/v2/uploads', auth=('acc_3ea586b31ac6cd0', '26cf56c4a313089eabc891bed0de1d89'),
                  files={'image': open(pic.filename, 'rb')}).json()['result']['upload_id']

    result = requests.get('https://api.imagga.com/v2/tags',
                            auth=('acc_3ea586b31ac6cd0', '26cf56c4a313089eabc891bed0de1d89'),
                            params={'image_upload_id': upload}).json()['result']['tags'][0]['tag']['en']

    final = requests.get('http://api.giphy.com/v1/gifs/search',
                            params={'q': result, 'api_key': 'ytB0By3Qe8XoARruGaQsAi1BH9b1Paue'}).json()['data']
    liste = []
    for i in range(0, 10):
        tmp = final[i]['images']['fixed_height']['url']
        liste.append(tmp)
    return render_template('result.html', resp=liste)


if __name__ == '__main__':
    app.run(debug=True)
