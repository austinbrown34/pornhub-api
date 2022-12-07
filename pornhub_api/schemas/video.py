from typing import Any, List
from datetime import datetime

from pydantic import Field, BaseModel, AnyHttpUrl

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
    rating: str
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


class VideoResult(BaseModel):
    __root__: Video = Field(..., alias="video")

    def __getattr__(self, item):
        return getattr(self.__root__, item)


class IsVideoActiveResult(BaseModel):
    class _Active(BaseModel):
        video_id: str
        is_active: str

    __root__: _Active = Field(..., alias="active")

    def __getattr__(self, item: Any) -> Any:
        return getattr(self.__root__, item)
