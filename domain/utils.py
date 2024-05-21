from channel.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_info(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        request = args[1]

        # SUBDOMAIN
        subdomain = request.META.get("HTTP_HOST").split(".")[0]
        method = request.method
        headers = request.headers
        path = kwargs.pop("path", "/")
        #
        request_data = {"method": method, "headers": dict(headers), "path": path}

        if request.method != "GET":
            request_data["data"] = dict(request.data)
        # Generate datas

        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            subdomain,
            {"type": "chat_message", "message": request_data},
        )
        return func(*args, **kwargs)

    return wrapper
