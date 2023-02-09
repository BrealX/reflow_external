from pydantic.dataclasses import dataclass

from models import ApiDataModel


@dataclass
class FetchedApiDataProtocol:
    """
    Step-component output data type
    """

    data: ApiDataModel


@dataclass
class TranslatedDataProtocol:
    """
    Step-component output data type
    """

    text: str


@dataclass
class ExtractedLocaleProtocol:
    """
    Step-component output data type
    """

    locale: str
