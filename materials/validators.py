import re
from rest_framework.serializers import ValidationError


def validate_youtube_link(value):
    if "youtube.com" in value:
        return
    raise ValidationError("Video from YouTube.com only.")


class ValidatorYouTubeLink:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        domain_videos = re.findall("\/\/(.*?)\/", video_url)
        domain_youtube = "youtube.com"
        if domain_youtube in domain_videos:
            raise ValidationError("Video from YouTube only")
        return None
