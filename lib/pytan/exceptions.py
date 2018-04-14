"""Provide exceptions for the :mod:`pytan` module."""


class HandlerError(Exception):
    """Exception thrown for errors in :mod:`pytan.handler`."""


class HumanParserError(Exception):
    """Exception thrown for errors while parsing human strings from :mod:`pytan.handler`."""


class DefinitionParserError(Exception):
    """Exception thrown for errors while parsing definitions from :mod:`pytan.handler`."""


class RunFalse(Exception):
    """Exception thrown when run=False from :func:`pytan.handler.Handler.deploy_action`."""


class PytanHelp(Exception):
    """Exception thrown when printing out help."""


class PollingError(Exception):
    """Exception thrown for errors in :mod:`pytan.polling`."""


class TimeoutException(Exception):
    """Exception thrown for timeout errors in :mod:`pytan.polling`."""


class HttpError(Exception):
    """Exception thrown for HTTP errors in :mod:`pytan.sessions`."""


class AuthorizationError(Exception):
    """Exception thrown for authorization errors in :mod:`pytan.sessions`."""


class BadResponseError(Exception):
    """Exception thrown for BadResponse messages from Tanium in :mod:`pytan.sessions`."""


class NotFoundError(Exception):
    """Exception thrown for Not Found messages from Tanium in :mod:`pytan.handler`."""


class VersionMismatchError(Exception):
    """Exception thrown for version_check in :mod:`pytan.utils`."""


class UnsupportedVersionError(Exception):
    """Exception thrown for version checks in :mod:`pytan.handler`."""


class ServerSideExportError(Exception):
    """Exception thrown for server side export errors in :mod:`pytan.handler`."""


class VersionParseError(Exception):
    """Exception thrown for server version parsing errors in :mod:`pytan.handler`."""


class ServerParseError(Exception):
    """Exception thrown for server parsing errors in :mod:`pytan.handler`."""


class PickerError(Exception):
    """Exception thrown for picker errors in :mod:`pytan.handler`."""
