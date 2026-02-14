# tests/test_app.py
import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_app():
    """Fixture to start the Dash app for testing."""
    app = import_app("app")  # this imports app.py
    return app

def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Dashboard"

def test_graph_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None

def test_radio_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None
