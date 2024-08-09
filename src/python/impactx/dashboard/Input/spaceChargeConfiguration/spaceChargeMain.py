from trame.widgets import vuetify

from ...trame_setup import setup_server

server, state, ctrl = setup_server()

# -----------------------------------------------------------------------------
# User-Interface
# -----------------------------------------------------------------------------


class SpaceChargeConfiguration:

    @staticmethod
    def card():
        """
        Creates UI content for space charge configuration
        """

        with vuetify.VCard(style="width: 340px; height: 300px"):
            vuetify.VCardTitle("Space Charge Configuation")
            vuetify.VDivider()
            with vuetify.VCardText():
                with vuetify.VRow():
                    with vuetify.VCol():
                        vuetify.VCheckbox(
                            label="Space Charge",
                            dense=True,
                            hide_details=True,
                        )
                        vuetify.VCheckbox(
                            label="Dynamic Size",
                            dense=True,
                            hide_details=True,
                        )
                with vuetify.VRow():
                    with vuetify.VCol():
                        vuetify.VTextField(
                            label="mlmg_relative_tolerance",
                            v_model=("mlmg_relative_tolerance", 1.0e-7),
                            dense=True,
                        )
                        vuetify.VTextField(
                            label="mlmg_absolute_tolerance",
                            v_model=("mlmg_relative_tolerance", 1.0e-7),
                        )
