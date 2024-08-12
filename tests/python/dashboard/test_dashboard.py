from seleniumbase import SB
from util import set_input_value, start_dashboard, wait_for_ready
import time

def test_simulation():
    """
    This test runs the FODO example on the dashboard and verifies
    that the simulation has ran successfully.
    """

    app_process = start_dashboard()
    time.sleep(10)

    try:
        with SB() as sb:
            url = "http://localhost:8080/index.html#/Input"
            sb.open(url)

            wait_for_ready(sb, 60)

            # Adjust beam properties
            sb.click("#particle_shape")
            sb.click("div.v-list-item:nth-of-type(2)")
            set_input_value(sb, "npart", 10000)
            set_input_value(sb, "kin_energy", 2.0e3)
            set_input_value(sb, "bunch_charge_C", 1.0e-9)

            # Adjust beam distribution
            set_input_value(sb, "selected_distribution", "Waterbag")
            set_input_value(sb, "lambdaX", 3.9984884770e-5)
            set_input_value(sb, "lambdaY", 3.9984884770e-5)
            set_input_value(sb, "lambdaT", 1.0e-3)
            set_input_value(sb, "lambdaPx", 2.6623538760e-5)
            set_input_value(sb, "lambdaPy", 2.6623538760e-5)
            set_input_value(sb, "lambdaPt", 2.0e-3)
            set_input_value(sb, "muxpx", -0.846574929020762)
            set_input_value(sb, "muypy", 0.846574929020762)
            set_input_value(sb, "mutpt", 0.0)

            # Adjust lattice configuration
            sb.click("#lattice_settings_icon")
            sb.sleep(1)
            set_input_value(sb, "nslice_default_value", 25)
            sb.click("#lattice_settings_close")
            sb.click("#clear_button")
            set_input_value(sb, "selected_lattice", "Drift")
            sb.click("#add_button")
            set_input_value(sb, "ds0", 0.25)
            set_input_value(sb, "selected_lattice", "Quad")
            sb.click("#add_button")
            set_input_value(sb, "ds1", 1.0)
            set_input_value(sb, "k1", 1.0)
            set_input_value(sb, "selected_lattice", "Drift")
            sb.click("#add_button")
            set_input_value(sb, "ds2", 0.5)
            set_input_value(sb, "selected_lattice", "Quad")
            sb.click("#add_button")
            set_input_value(sb, "ds3", 1.0)
            set_input_value(sb, "k3", -1.0)
            set_input_value(sb, "selected_lattice", "Drift")
            sb.click("#add_button")
            set_input_value(sb, "ds4", 0.25)

            # Run simulation
            sb.click("#Run_route")
            sb.sleep(1)
            sb.click("#run_simulation_button")
            sb.sleep(25)

            # Check if "Simulation complete" message is printed
            xterm_content = sb.get_text("#xterm_component")
            assert "Simulation complete." in xterm_content
    finally:
        app_process.terminate()