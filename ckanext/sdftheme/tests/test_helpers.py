"""Tests for helpers.py."""

import ckanext.sdftheme.helpers as helpers


def test_sdftheme_hello():
    assert helpers.sdftheme_hello() == "Hello, sdftheme!"
