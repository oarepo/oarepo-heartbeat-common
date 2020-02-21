# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# oarepo-heartbeat-common is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask

from oarepo_heartbeat_common import OARepoHeartbeatCommon


def test_version():
    """Test version import."""
    from oarepo_heartbeat_common import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = OARepoHeartbeatCommon(app)
    assert 'oarepo-heartbeat-common' in app.extensions

    app = Flask('testapp')
    ext = OARepoHeartbeatCommon()
    assert 'oarepo-heartbeat-common' not in app.extensions
    ext.init_app(app)
    assert 'oarepo-heartbeat-common' in app.extensions
