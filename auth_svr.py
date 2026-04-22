#!/usr/bin/env python3
import os, sys, datetime, base64, json, bcrypt, subprocess, shlex
from flask import Flask, request, jsonify, render_template, redirect, url_for
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

DEBUG = True
HOST = "0.0.0.0"
PORT = 9982
VERSION = [0x00, 0x04, 0x00]
SERVER_METADATA = {
    "meta": {
        "serverName": "<SERVER_NAME>"
    },
    "skinDomains": [],
    "signaturePublickey": ""
}
INVALID_MSG = {
    "error": "ForbiddenOperationException",
    "errorMessage": "Invalid operation."
}
TEMPLATE_AUTH = {
    "accessToken": "<ACCESS_TOKEN>",
    "clientToken": "<CLIENT_TOKEN>",
    "selectedProfile": {"id": "<UUID>", "name": "<NAME>"}
}
TEMPLATE_PROFILE = {
    "id": "<UUID>",
    "name": "<NAME>",
    "properties": [{
        "name": "textures",
        "value": "<B64_VALUE>",
        "signature": "<SIGNATURE>"
    }]
}
app = Flask("PenzaiAuth")

@app.route("/")
def index():
    return jsonify(SERVER_METADATA), 200

@app.route("/authserver/authenticate", methods=["POST"])
def authenticate():
    pass

@app.route("/authserver/refresh", methods=["POST"])
def refresh():
    pass

@app.route("/authserver/validate", methods=["POST"])
def validate():
    pass

@app.route("/authserver/invalidate", methods=["POST"])
def invalidate():
    pass

@app.route("/authserver/signout", methods=["POST"])
def signout():
    pass

@app.route("/sessionserver/session/minecraft/join", methods=["POST"])
def join():
    pass

@app.route("/sessionserver/session/minecraft/hasJoined", methods=["GET"])
def has_joined():
    pass

@app.route("/sessionserver/session/minecraft/profile/<uuid>", methods=["GET"])
def profile(uuid):
    pass

@app.route("/api/profiles/minecraft", methods=["POST"])
def profiles():
    pass

@app.route("/api/user/profile/{uuid}/{textureType}", methods=["PUT", "DELETE"])
def texture_modify(uuid, textureType):
    pass

if __name__ == "__main__":
    if DEBUG:
        app.run(host=HOST, port=PORT)
    else:
        from waitress import serve
        print(f"Penzai Auth v{VERSION[0]}.{VERSION[1]}.{VERSION[2]}")
        print(f"Serving on http://{HOST}:{PORT}")
        print("----------------------------------------")
        serve(app, host=HOST, port=PORT)
