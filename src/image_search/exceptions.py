from exceptions import ItemNotFound


class ImageSearchNotFound(ItemNotFound):
    def __init__(self, msg=None, error_trace=None):
        super(ImageSearchNotFound, self).__init__(
            msg=msg or "Image search cache not found", error_trace=error_trace)
