#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# oarepo-heartbeat-common is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

pydocstyle oarepo_heartbeat_common tests docs && \
isort -rc -c -df && \
check-manifest --ignore ".travis-*" && \
python setup.py test
