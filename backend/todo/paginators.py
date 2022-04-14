from rest_framework.pagination import LimitOffsetPagination


class ProjectPaginator(LimitOffsetPagination):
    default_limit = 10


class TaskPaginator(LimitOffsetPagination):
    default_limit = 20
