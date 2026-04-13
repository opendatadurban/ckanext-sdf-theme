from flask import Blueprint


sdftheme = Blueprint(
    "sdftheme", __name__)


def page():
    return "Hello, sdftheme!"


sdftheme.add_url_rule(
    "/sdftheme/page", view_func=page)


def get_blueprints():
    return [sdftheme]
