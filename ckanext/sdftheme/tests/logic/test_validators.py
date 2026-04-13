"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.sdftheme.logic import validators


def test_sdftheme_reauired_with_valid_value():
    assert validators.sdftheme_required("value") == "value"


def test_sdftheme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.sdftheme_required(None)
