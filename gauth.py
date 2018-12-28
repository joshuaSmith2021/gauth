#!/usr/bin/env python3

import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

class OAuth:
    """
    Creates an object with multiple methods designed to create and read
    credentials as well as checking if valid credentials exist. It is
    initialized by passing in the path to the OAuth client secrets file and the
    path to the file where credentials are stored.
    """
    def __init__(self, SECRETS_FILE, creds_file):
        self._secrets_file = SECRETS_FILE
        self._creds_file = creds_file
    def create_credentials(self, SCOPES, SERVICE_NAME, VERSION):
        """
        Creates OAuth credentials for a user based for a certain API.
        Returns 'A Resource object with methods for interacting with the service.' -Google Documentation
        """
        flow = InstalledAppFlow.from_client_secrets_file(self._secrets_file, SCOPES)
        credentials = flow.run_console()
        return build(SERVICE_NAME, VERSION, credentials=credentials)
