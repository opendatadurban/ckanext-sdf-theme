"""Tests for views.py."""

import pytest

import ckanext.sdftheme.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "sdftheme")
@pytest.mark.usefixtures("with_plugins")
def test_sdftheme_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("sdftheme.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, sdftheme!"
