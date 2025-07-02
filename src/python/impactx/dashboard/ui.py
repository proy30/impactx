"""
This file is part of ImpactX

Copyright 2025 ImpactX contributors
Authors: Parthib Roy, Axel Huebl
License: BSD-3-Clause-LBNL
"""

from trame.ui.vuetify import VAppLayout

from . import setup_server
from .Analyze.ui import AnalyzeSimulation

server, state, ctrl = setup_server()


def layout():
    """
    The main layout of the dashboard.
    """
    return VAppLayout(
        ("trame.ui.vuetify.VApp", [("trame.ui.vuetify.VMain", [AnalyzeSimulation()])])
    )
