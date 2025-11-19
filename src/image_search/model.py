from datetime import datetime
from typing import Any, Dict
from pydantic import BaseModel, ConfigDict, Field


class ImageResult(BaseModel):
    title: str
    src: str
    format: str
    width: int
    height: int
    source_site: str


class ImageSearch(BaseModel):
    model_config = ConfigDict(serialize_by_alias=False)

    query_hash: str
    start: int
    search_query: str
    exact_terms: str
    created_at: datetime
    ttl: int = Field(default=60 * 60 * 24)
    results: list[ImageResult]

    def to_db_item(self) -> Dict[str, Any]:
        results_list = [result.model_dump() for result in self.results]

        db_item = {
            "queryHash": self.query_hash,
            "id": str(self.start),
            "searchQuery": self.search_query,
            "exactTerms": self.exact_terms,
            "ttl": self.ttl,
            "createdAt": self.created_at.isoformat(),
            "results": results_list
        }

        return db_item

    @classmethod
    def from_db_item(cls, db_item: Dict[str, Any]):

        data_for_pydantic = {
            "query_hash": db_item["queryHash"],
            "start": int(db_item["id"]),
            "search_query": db_item["searchQuery"],
            "exact_terms": db_item["exactTerms"],
            "created_at": db_item["createdAt"],
            "ttl": db_item["ttl"],
            "results": db_item["results"]
        }

        return ImageSearch.model_validate(data_for_pydantic)
