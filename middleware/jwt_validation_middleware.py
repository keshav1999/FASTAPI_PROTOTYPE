# import jwt
# from fastapi import Request
# from fastapi.responses import JSONResponse
#
# from common.messages import Messages
# from common.secret_manager import SecreteData


# class JwtMiddleWare:
#     """ This middleware used to validate the jwt token """
#
#     def __init__(self, logger: str):
#         self.logger = logger
#
#     async def __call__(self, request: Request, call_next):
#         # do something with the request object
#         headers = request.headers
#         keys = SecreteData()
#         key = keys.FRESHWORKS_IVR_JWT_SECRET
#         token = None
#         if 'Authorization' in headers:
#             bearer = headers.get('Authorization')
#             if 'Bearer' in bearer:
#                 token = bearer.split()[1]
#             else:
#                 return JSONResponse(status_code=401, content={"code": 401, "message": Messages.AUTHORIZATION_FAILED})
#
#         if not token:
#             return JSONResponse(status_code=401, content={"code": 401, "message": Messages.UNAUTHORIZED})
#         try:
#             data = jwt.decode(token, key, algorithms=["HS256"])
#             response = await call_next(request)
#         except jwt.ExpiredSignatureError as exp:
#             return JSONResponse(status_code=401, content={"code": 401, "message": Messages.AUTHORIZATION_FAILED})
#         except Exception as exp:
#             return JSONResponse(status_code=500, content={"code": 500, "message": Messages.EXCEPTION_JWT})
#         return response
