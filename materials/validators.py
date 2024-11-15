from rest_framework.serializers import ValidationError


def validate_youtube_link(value):
    if "youtube.com" in value:
        return
    raise ValidationError("Video from YouTube.com only.")
