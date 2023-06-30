from rest_framework import pagination


class MyPagination(pagination.PageNumberPagination):
	page_size = 5 # ?page=2
	page_query_param = 'my_page' # ?my_page=7 | starts from 31
	page_size_query_param = 'num' # ?my_page=7&num=10
	max_page_size = 100
	last_page_strings = ('end',) # ?my_page=end


class MyLimitPagination(pagination.LimitOffsetPagination):
	default_limit = 15
	limit_query_param = 'mylimit'
	offset_query_param = 'myoffset'
	max_limit = 20