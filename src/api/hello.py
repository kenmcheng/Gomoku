import logging
from fastapi import FastAPI

from services import spam_creator

def init(app):
    
    @app.route("/api", methods=["GET", "POST"])
    def hello():
        return "Hello World!"

    @app.route("/spam")
    def spam():
        return spam_creator.create()