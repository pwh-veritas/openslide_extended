from openslide import OpenSlide


class OpenSlideExtended(OpenSlide):
    def __init__(self, filename):
        super().__init__(filename)

    def get_thumbnail(self, size=(512, 512)):
        return super().get_thumbnail(size=size)
