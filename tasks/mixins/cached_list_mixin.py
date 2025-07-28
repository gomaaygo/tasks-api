from django.core.cache import cache

from rest_framework.response import Response

class CachedUserListMixin:
    cache_timeout = 300

    def get_user_cache_key(self):
        return f"{self.__class__.__name__}_user_{self.request.user.id}"

    def list(self, request, *args, **kwargs):
        cache_key = self.get_user_cache_key()
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            response = Response(serializer.data)

        cache.set(cache_key, response.data, timeout=self.cache_timeout)
        return response

    def clear_user_cache(self):
        cache.delete(self.get_user_cache_key())

    def perform_create(self, serializer):
        serializer.save()
        self.clear_user_cache()

    def perform_update(self, serializer):
        serializer.save()
        self.clear_user_cache()

    def perform_destroy(self, instance):
        instance.delete()
        self.clear_user_cache()
