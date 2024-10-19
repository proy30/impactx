from ...trame_setup import setup_server

server, state, ctrl = setup_server()

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


class DistributionFunctions:
    """
    Helper functions for the
    User-Input section for beam properties.
    """

    @staticmethod
    def convert_distribution_parameters_to_valid_type():
        """
        Helper function to check if user input is valid.
        :return: A dictionary with parameter names as keys and their validated values.
        """

        parameter_input = {
            param["parameter_name"]: float(param["parameter_default_value"])
            if param_is_valid
            else 0.0
            for param in state.selectedDistributionParameters
            if (param_is_valid := param["parameter_error_message"] == [])
        }

        return parameter_input
