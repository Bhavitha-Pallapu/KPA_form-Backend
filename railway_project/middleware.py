import logging
import time

logger = logging.getLogger('railway_project')


class RequestResponseLoggingMiddleware:
    """Simple middleware that logs basic request and response info.

    This keeps the project working locally and avoids import errors when
    the middleware referenced in settings.py is missing.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        try:
            logger.info(f"Incoming request: {request.method} {request.get_full_path()}")
        except Exception:
            # avoid crashing on unexpected request objects during startup
            pass

        response = self.get_response(request)

        duration = (time.time() - start) * 1000
        try:
            logger.info(f"Response: {request.method} {request.get_full_path()} -> {response.status_code} ({duration:.1f}ms)")
        except Exception:
            pass

        return response
