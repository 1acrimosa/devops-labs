from rest_framework.pagination import LimitOffsetPagination

from common.api.responses import OKResponse


class CustomLimitOffsetPagination(LimitOffsetPagination):

    def get_paginated_response(self, data):
        return OKResponse(
            {
                "count": self.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": data,
            }
        )

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "example": "ok",
                },
                "data": {
                    {
                        "type": "object",
                        "properties": {
                            "count": {
                                "type": "integer",
                                "example": 123,
                            },
                            "next": {
                                "type": "string",
                                "nullable": True,
                                "format": "uri",
                                "example": "http://api.example.org/accounts/?{offset_param}=400&{limit_param}=100".format(
                                    offset_param=self.offset_query_param,
                                    limit_param=self.limit_query_param,
                                ),
                            },
                            "previous": {
                                "type": "string",
                                "nullable": True,
                                "format": "uri",
                                "example": "http://api.example.org/accounts/?{offset_param}=200&{limit_param}=100".format(
                                    offset_param=self.offset_query_param,
                                    limit_param=self.limit_query_param,
                                ),
                            },
                            "results": schema,
                        },
                    }
                },
            },
        }
