from trame.widgets import vuetify

from ...trame_setup import setup_server

server, state, ctrl = setup_server()

state.max_level = 3
state.level_fields = []


@state.change("max_level")
def on_max_level_change(max_level, **kwargs):
    num_levels = int(max_level) + 1

    state.level_fields = [
        {
            "label": f"prob_relative{i+1}",
            "value": "",
            "type": "number",
            "error_message": "",
        }
        for i in range(num_levels)
    ]


class SpaceChargeConfiguration:

    @staticmethod
    def card():
        """
        Creates UI content for space charge configuration
        """

        with vuetify.VCard(v_show="space_charge", style="width: 340px;"):
            vuetify.VCardTitle("Space Charge Configuration")
            vuetify.VDivider()
            with vuetify.VCardText():
                with vuetify.VRow(classes="my-0"):
                    with vuetify.VCol(cols=6, classes="py-0"):
                        vuetify.VCombobox(
                            v_model=("particle_shape",),
                            label="Particle Shape",
                            items=([1, 2, 3],),
                            dense=True,
                        )
                    with vuetify.VCol(cols=6, classes="py-0"):
                        vuetify.VCombobox(
                            label="Poisson Solver",
                            v_model=("poisson_solver", "Multigrid"),
                            items=(["Multigrid", "FFT"],),
                            dense=True,
                            hide_details=True,
                        )
                with vuetify.VRow(classes="my-0"):
                    with vuetify.VCol(cols=4, classes="py-0"):
                        vuetify.VTextField(
                            label="nCell_X",
                            v_model=("n_cell_x", ""),
                            dense=True,
                        )
                    with vuetify.VCol(cols=4, classes="py-0"):
                        vuetify.VTextField(
                            label="nCell_Y",
                            v_model=("n_cell_y", ""),
                            dense=True,
                        )
                    with vuetify.VCol(cols=4, classes="py-0"):
                        vuetify.VTextField(
                            label="nCell_X",
                            v_model=("n_cell_z", ""),
                            dense=True,
                        )
                with vuetify.VRow(classes="my-0"):
                    with vuetify.VCol(cols=4, classes="py-0"):
                        vuetify.VSelect(
                            v_model=("max_level",),
                            label="Max Level",
                            items=([0, 1, 2, 3, 4],),
                            dense=True,
                        )
                with vuetify.VRow(classes="my-0"):
                    with vuetify.VCol(
                        v_for=("field in level_fields",), cols="auto", classes="py-0"
                    ):
                        vuetify.VTextField(
                            label=("field.label",),
                            dense=True,
                            style="width: 125px;",
                        )
