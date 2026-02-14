# test_app.py
import pytest
from app import app  # Import your Dash app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("#dashboard-header")
    assert header is not None
    assert "Pink Morsel Sales Dashboard" in header.text

def test_graph_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    picker = dash_duo.find_element("#region-picker")
    assert picker is not None
