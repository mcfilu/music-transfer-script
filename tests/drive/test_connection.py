import pytest
from unittest.mock import patch

from drive.auth import authenticate

#
# @patch("drive.auth.GoogleAuth")
# def test_authenticate_returns_googleauth_object(mock_googleauth):
#     """Tests if the authenticate function returns a GoogleAuth object."""
#     gauth = authenticate()
#     assert isinstance(gauth, mock_googleauth)
@patch("authentication.GoogleAuth")
def test_authenticate_returns_googleauth_object(mock_googleauth):
    """Tests if the authenticate function returns a GoogleAuth object."""
    gauth = authenticate()
    assert isinstance(gauth, mock_googleauth.return_value)  # Assert against the type of the mock's return value


@patch("drive.auth.GoogleAuth")
def test_authenticate_calls_local_webserver_auth(mock_googleauth):
    """Tests if the authenticate function calls LocalWebserverAuth on the GoogleAuth object."""
    authenticate()
    mock_googleauth.assert_called_once_with()
    mock_googleauth.return_value.LocalWebserverAuth.assert_called_once_with()


@patch("drive.auth.GoogleAuth")
def test_authenticate_handles_local_webserver_auth_error(mock_googleauth):
    """Tests if the authenticate function handles an error raised by LocalWebserverAuth."""
    mock_googleauth.return_value.LocalWebserverAuth.side_effect = Exception("Authentication error")
    with pytest.raises(Exception) as excinfo:
        authenticate()
    assert "Authentication error" in str(excinfo.value)