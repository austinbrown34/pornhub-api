from typing import List
from pydantic import RootModel, Field
from pornhub_api.schemas.video import Video

class VideoSearchResult(RootModel[List[Video]]):
    videos: List[Video] = Field(..., alias="videos")

    def __iter__(self):
        return iter(self.videos)

    def __getitem__(self, item):
        return self.videos[item]

    def size(self):
        return len(self.videos)
