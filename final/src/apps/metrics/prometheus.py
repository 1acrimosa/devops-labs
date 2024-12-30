from prometheus_client import Counter, Info, Summary

info = Info(name="thumbnails", documentation="Thumbnail service information.")
info.info({"version": "1.0", "language": "python", "framework": "django"})


resize_image_request_count = Counter(
    name="resize_image_request_count",
    documentation="Number of resize image requests.",
    labelnames=["max_width", "max_height"],
)

resize_image_process_count = Counter(
    name="resize_image_process_count",
    documentation="Number of resize image processes.",
    labelnames=["max_width", "max_height"],
)

resize_image_process_time = Summary(
    name="resize_image_process_time",
    documentation="Time spent processing image.",
    labelnames=["max_width", "max_height"],
)
