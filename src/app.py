from flask import Flask, jsonify, render_template, send_from_directory
import datetime
import socket
import random


dev_excuses = [
    "It worked on my machine.",
    "I thought I fixed that.",
    "That's just a warning, not an error.",
    "You must have a corrupted database.",
    "It was working yesterday.",
    "I didn't write that part of the code.",
    "That's a hardware problem.",
    "I can't reproduce the problem.",
    "The client must have done something wrong.",
    "I have never seen that before."
]

app = Flask(__name__)


@app.route('/')

def home():
    return render_template(
        'index.html',
        cat_img=f"images-front/cat{random.randint(1, 7)}.gif",
        dev_excuse=random.choice(dev_excuses)
    )

@app.route('/api/v1/info')

def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'deployed_on': 'kubernetes',
    })

@app.route('/api/v1/healthz')

def health():
    # Do an actual check here
    return jsonify({'status': 'up'}), 200


@app.route('/images-front/<filename>')
def images_frontend(filename):
    return send_from_directory('templates/img', filename)

if __name__ == '__main__':

    app.run(host="0.0.0.0")

