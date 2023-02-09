
from protocols import ExtractedLocaleProtocol, FetchedApiDataProtocol, TranslatedDataProtocol


class TranslatedData:
    """
    FetchedApiDataProtocol |
    ExtractedLocaleProtocol -> ( TranslatedData ) -> TranslatedTextProtocol
    """

    # Inputs
    _api_data: FetchedApiDataProtocol
    _extracted_locale: ExtractedLocaleProtocol

    async def output(self) -> TranslatedDataProtocol:
        """
        Producing strongly typed output for other step-components
        """

        _ = self._api_data.data
        _ = self._extracted_locale.locale

        # make a call to translate the text
        # ...
        translated = 'How are you?'

        return TranslatedDataProtocol(text=translated)
