import sys

from trame.ui.router import RouterViewLayout
from trame.ui.vuetify import SinglePageWithDrawerLayout
from trame.widgets import router, vuetify, xterm

from .Analyze.plotsMain import AnalyzeSimulation
from .Input.distributionParameters.distributionMain import DistributionParameters
from .Input.inputParameters.inputMain import InputParameters
from .Input.latticeConfiguration.latticeMain import LatticeConfiguration
from .Input.trameFunctions import TrameFunctions
from .Input.Visualiztion.twiss_phase_space_ellipse.x_px import VisualizeTwiss
from .start import main
from .Toolbar.toolbarMain import Toolbars
from .trame_setup import setup_server

# -----------------------------------------------------------------------------
# Trame setup
# -----------------------------------------------------------------------------

server, state, ctrl = setup_server()

# -----------------------------------------------------------------------------
# Router Views
# -----------------------------------------------------------------------------

inputParameters = InputParameters()

with RouterViewLayout(server, "/Input"):
    with vuetify.VContainer(fluid=True):
        with vuetify.VRow():
            with vuetify.VCol(cols="auto", classes="pa-2"):
                with vuetify.VRow(no_gutters=True):
                    with vuetify.VCol(cols="auto", classes="pa-2"):
                        inputParameters.card()
                    with vuetify.VCol(cols="auto", classes="pa-2"):
                        DistributionParameters.card()
                with vuetify.VRow(no_gutters=True):
                    with vuetify.VCol(cols="auto", classes="pa-2"):
                        LatticeConfiguration.card()
            with vuetify.VCol(
                cols="auto",
                classes="pa-2",
                v_if="selectedVisualization == 'Twiss Phase Space Ellipses'",
            ):
                with vuetify.VRow(no_gutters=True):
                    with vuetify.VCol(cols="auto", classes="pa-2"):
                        VisualizeTwiss.card_x()
                    with vuetify.VCol(cols="auto", classes="pa-2"):
                        VisualizeTwiss.card_t()
                with vuetify.VRow(no_gutters=True):
                    with vuetify.VCol(cols="auto", classes="pa-2"):
                        VisualizeTwiss.card_y()

with RouterViewLayout(server, "/Analyze"):
    with vuetify.VContainer(fluid=True):
        with vuetify.VRow(no_gutters=True, classes="fill-height"):
            with vuetify.VCol(cols="auto", classes="pa-2 fill-height"):
                AnalyzeSimulation.card()
            with vuetify.VCol(cols="auto", classes="pa-2 fill-height"):
                AnalyzeSimulation.plot()

# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------
def init_terminal():
    with xterm.XTerm(v_if="$route.path == '/Run'") as term:
        ctrl.terminal_print = term.writeln

def application():
    init_terminal()
    with SinglePageWithDrawerLayout(server) as layout:
        layout.title.hide()
        with layout.toolbar:
            with vuetify.Template(v_if="$route.path == '/Analyze'"):
                Toolbars.analyze_toolbar()
            with vuetify.Template(v_if="$route.path == '/Run'"):
                Toolbars.run_toolbar()

        with layout.drawer as drawer:
            drawer.width = 200
            with vuetify.VList():
                vuetify.VSubheader("Simulation")
            TrameFunctions.create_route("Input", "mdi-file-edit")
            TrameFunctions.create_route("Run", "mdi-play")
            TrameFunctions.create_route("Analyze", "mdi-chart-box-multiple")

        with layout.content:
            router.RouterView()
            init_terminal() 
    return layout

application()
# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    sys.exit(main())
