# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# oarepo-heartbeat-common is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

from __future__ import absolute_import, print_function

import pytest
from flask import Flask

from oarepo_heartbeat_common import OARepoHeartbeatCommon


@pytest.fixture(scope='module')
def create_app(instance_path):
    """Application factory fixture."""

    def factory(**config):
        app = Flask('testapp', instance_path=instance_path)
        app.config.update(**config)
        OARepoHeartbeatCommon(app)
        return app

    return factory
