import logging

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    """
    Logging middleware for protected routes
    """

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """
        Logging protected route access middleware
        :param request:
        :return:
        """
        protected_routes = ['/', '']  # list of required auth paths
        if request.path in protected_routes:
            logger.info(
                f"[{now()}]: {request.method} {request.path} accessed by {request.user if request.user.is_authenticated else 'Anonymous'}")

        response = self.get_response(request)
        return response


class NotFoundMiddleware:
    """
    Handle 404 error response
    """
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """
        Process not found error
        :param request:
        :return:
        """
        response = self.get_response(request)
        if response.status_code == 404:
            logger.info(
                f"[{now()}]: {request.method} {request.path} Page Not Found")
            return redirect('home')

        return response


class InternalServerErrorMiddleware:
    """
    Handle 500 error response
    """
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """
        Process internal server error
        :param request:
        :return:
        """
        response = self.get_response(request)
        if response.status_code == 500:
            logger.error(
                f"[{now()}]: {request.method} {request.path} {response.status_code} Internal Server Error: {response.content}")
            return redirect('home')
        return response


class RemoveServerHeaderMiddleware(MiddlewareMixin):
    """
    Remove server header from request
    """

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        """
        Reassign server header from request
        :param request:
        :param response:
        :return:
        """
        response.headers['Server'] = 'XXX'
        return response
