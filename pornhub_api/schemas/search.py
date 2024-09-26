from typing import Any, List

from pydantic import BaseModel, RootModel
from pydantic.fields import Field

from pornhub_api.schemas.video import Video


class VideoSearchResult(RootModel[Any]):
    root: List[Video] = Field(..., alias="videos")

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]

    def size(self):
        return len(self.root)
