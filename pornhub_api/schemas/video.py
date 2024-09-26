from typing import Any, List, Union
from datetime import datetime

from pydantic import field, BaseModel, AnyHttpUrl, field_validator, RootModel

from pornhub_api.schemas.tag import Tag
from pornhub_api.schemas.thumb import Thumb
from pornhub_api.schemas.pornstart import Pornstar

__all__ = ("Video", "VideoResult", "Category", "IsVideoActiveResult")


class Category(BaseModel):
    category: str


class Video(BaseModel):
    title: str
    duration: str
    views: int
    video_id: str
    rating: Union[float, int]
    ratings: int
    url: AnyHttpUrl
    default_thumb: AnyHttpUrl
    thumb: AnyHttpUrl
    publish_date: datetime
    segment: str
    thumbs: List[Thumb]
    tags: List[Tag]
    categories: List[Category]
    pornstars: List[Pornstar]

    @field_validator("rating")
    def prettify_float(cls, value: Union[float, int]) -> Union[float, int]:
        if value == int(value):
            return int(value)
        return value


class VideoResult(RootModel[Video]):
    video: Video = field(..., alias="video")

    def __getattr__(self, item):
        return getattr(self.video, item)


class IsVideoActiveResult(RootModel[BaseModel]):
    class _Active(BaseModel):
        video_id: str
        is_active: str

    active: _Active = field(..., alias="active")

    def __getattr__(self, item: Any) -> Any:
        return getattr(self.active, item)
