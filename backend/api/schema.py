from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from . import serializers
# Auth

auth_login = swagger_auto_schema(
    operation_description="Log in the system",
    # query_serializer= 
    request_body=serializers.LoginSerializer,
    responses={
        200: openapi.Response(
            "Logged in",
            openapi.Schema(
                type=openapi.TYPE_STRING,
                pattern="username"
            )
        ),
        401: openapi.Response(
            "Login Failed",
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail" : openapi.Schema(type=openapi.TYPE_STRING, pattern="failed to log in")
                }
            )
        )
    }
)
# Game
# leaders
# Progress

permission_denied = openapi.Response("Permission denied",
                                     openapi.Schema(
                                         type=openapi.TYPE_OBJECT,
                                         properties={
                                             "detail":openapi.Schema(type=openapi.TYPE_STRING, pattern="Authentication credentials were not provided.")
                                         }
                                     ))



progress = swagger_auto_schema(
    operation_description=" GET the user progress",
    responses={
        200: openapi.Response(
            description="User's game info",
            schema=openapi.Schema(
                "Info",
                type= openapi.TYPE_OBJECT,
                properties={
                    "best_record" : openapi.Schema(type=openapi.TYPE_INTEGER)
                }
            )
        ),
        400 : permission_denied 
    }
)




# seq
seq_post = swagger_auto_schema(
    operation_description="POST answer as seq",
    manual_parameters=[
        openapi.Parameter("seq", 
                          openapi.IN_QUERY,
                          "Answer",
                          True,
                          type=openapi.TYPE_OBJECT),
    ],
    responses={
        200: openapi.Response("Score", examples={"score":"12"}),

    }
)

seq_get = swagger_auto_schema(
    operation_description="Get a new sequence",
    responses={
        200: openapi.Response("Seq",
                              openapi.Schema(
                                    title="Sequence",
                                    description="The sequence to type",
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        "words": openapi.Schema(title="words", 
                                                                type=openapi.TYPE_ARRAY,
                                                                items=openapi.Schema("word",type=openapi.TYPE_STRING,pattern="word")),
                                        "seq" : openapi.Schema("Sequence", type=openapi.TYPE_STRING, pattern="sequence of given words")
                                    }
                                )
                            ),

        400: openapi.Response(
                "Sequence exist",
                openapi.Schema(
                    title="Error",
                    description="sequence exist",
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(type=openapi.TYPE_STRING, pattern="seq exist")
                    }
                ),
            ),
    }
)


permission_denied = openapi.Response("Permission denied",
                                     openapi.Schema(
                                         type=openapi.TYPE_OBJECT,
                                         properties={
                                             "detail":openapi.Schema(type=openapi.TYPE_STRING, pattern="Authentication credentials were not provided.")
                                         }
                                     ))