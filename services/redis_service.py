import json
import logging
import os
from redis import Redis


class RedisCache:
    def __init__(self):
        self.load_redis_client()
    def load_redis_client(self):
        host = os.getenv("redis_host")
        port = os.getenv("redis_port")
        self.redis = Redis(host=host, decode_responses=True,
                      port=int(port))

    def set_redis_cache(self, key, value):
        success = True
        try:

            if self.redis.ping():
                self.redis.set(key, json.dumps(value))
                self.redis.expire(key, 86400)
            else:
                self.load_redis_client()
        except Exception as excp:
            success = False
        finally:

            return success

    def get_redis_cache(self, key, is_json=True):
        # sec_key = SecreteData()
        # host = sec_key.REDIS_SERVER
        # port = sec_key.REDIS_PORT
        # prefix = sec_key.REDIS_PREFIX
        success = True
        data = ''

        try:

            if self.redis.ping():

                if is_json:
                    data = self.redis.get(key)
                    if data:
                        data = json.loads(data)

                else:
                    data = self.redis.get(key)
            else:
                self.load_redis_client()

        except Exception as exc:
            success = False

        finally:
            return success, data

    # def remove_redis_cache(self, key):
    #     host = sec_key.REDIS_SERVER
    #     port = sec_key.REDIS_PORT
    #     prefix = sec_key.REDIS_PREFIX
    #     key = prefix + key
    #     success = True
    #     data = ''
    #     try:
    #         redis = Redis(host=host, decode_responses=True,
    #                       port=port)
    #         if redis.ping():
    #             logging.info("Connected to Redis")
    #             data = redis.get(key)
    #             if data:
    #                 redis.delete(key)
    #     except Exception as excp:
    #         success = False
    #         Utils.process_exception(
    #             "REDIS", excp,
    #             self.logger,
    #             AppMessages.SOMETHING_WENT_WRONG,
    #             key
    #         )
    #     finally:
    #         self.logger.info("completed CustomerLoginMgr.do_login")
    #         redis.close()
    #         return success, data
