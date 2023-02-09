from pydantic import BaseModel, AnyUrl


class ApiDataModel(BaseModel):
    """
    Pydantic validation model for ApiData
    """

    url: AnyUrl
    text: str
    token_id: str
