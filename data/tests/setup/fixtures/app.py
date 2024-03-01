import os

import pytest

from data.service import create_app
from data.tests.setup.fixtures.external_modules import mock_create_access_token, mock_binance_client_exchange_info
from data.tests.setup.fixtures.internal_modules import (
    mock_redis_connection,
    mock_settings_env_vars,
    mock_get_strategies,
    mock_redis_connection_bots_api,
    mock_redis_connection_bots_api_helpers,
    mock_redis_connection_external_requests,
    mock_start_stop_symbol_trading_success_true,
    spy_start_symbol_trading,
    mock_get_open_positions,
)
from shared.utils.tests.fixtures.external_modules import mock_jwt_required, mock_requests_post
from shared.utils.tests.fixtures.models import *


TEST_APP_NAME = 'test_app'


@pytest.fixture()
def mock_client_env_vars(mocker):
    mocker.patch.dict(os.environ, {"TEST": "true"})


@pytest.fixture
def app(
    db,
    mock_client_env_vars,
    mock_create_access_token,
    mock_redis_connection,
    mock_redis_connection_bots_api,
    mock_redis_connection_bots_api_helpers,
    mock_redis_connection_external_requests,
    mock_start_stop_symbol_trading_success_true,
    mock_jwt_required,
    mock_settings_env_vars,
    mock_get_strategies,
    mock_binance_client_exchange_info,
    mock_requests_post,
    create_exchange,
    create_assets,
    create_symbol,
    spy_start_symbol_trading,
    monkeypatch,
    mock_get_open_positions
):

    # monkeypatch.setenv("TEST", )
    app = create_app(testing=True)
    return app


@pytest.fixture
def client(app):
    """A test client for the app."""
    with app.test_client() as client:
        yield client


@pytest.fixture
def app_with_open_position(
    db,
    mock_create_access_token,
    mock_redis_connection,
    mock_redis_connection_bots_api,
    mock_redis_connection_bots_api_helpers,
    mock_redis_connection_external_requests,
    mock_jwt_required,
    mock_settings_env_vars,
    mock_get_strategies,
    mock_binance_client_exchange_info,
    mock_get_open_positions,
    mock_start_stop_symbol_trading_success_true,
    mock_requests_post,
    spy_start_stop_symbol_trading,
    fake_executor_submit,
    create_exchange,
    create_assets,
    create_symbol,
    create_positions
):
    app = create_app(testing=True)
    return app


@pytest.fixture
def client_with_open_position(app_with_open_position):
    """A test client for the app."""
    with app_with_open_position.test_client() as client:
        yield client
