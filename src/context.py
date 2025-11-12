from image_search.persistence import ImageSearchPersistence
from image_search.service import ImageSearchService


class ApplicationContext():
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ApplicationContext, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.image_search_persistence = ImageSearchPersistence()
        self.image_search_service = ImageSearchService(
            persistence=self.image_search_persistence
        )
