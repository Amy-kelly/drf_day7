from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination
#基础分页器
class MyBasePagination(PageNumberPagination):
    page_size = 2
    #每页的最大数量
    max_page_size = 4
    page_size_query_param = "page_size"
    page_query_param = "page"

#偏移分页器
class MyOffsetPagination(LimitOffsetPagination):
    #每页默认数量
    default_limit = 3
    # 指定前端修改每页数量的key
    limit_query_param = "limit"
    # 前端指定偏移的数量的key
    offset_query_param = "offset"
    max_limit = 5

#游标分页器
class MyCursorPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 5
    ordering = "price"