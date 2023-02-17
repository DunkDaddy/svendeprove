from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):

    handlers = {
        'Http500': _handle_generic_exception,
    }

    response = exception_handler(exc, context)

    exception_class=exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_generic_exception(exc, context, response):
    response.data = {
        'error': 'no data'
    }

    return response
