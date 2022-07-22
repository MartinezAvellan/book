import redis

from app.utils.constants import REDIS_HOST, REDIS_PORT


class RedisService(object):

    def __init__(self):
        self.redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def get(self, redis_key):
        redis_value = self.redis_client.get(redis_key)
        self.redis_client.close()
        if redis_value:
            return str(redis_value, "utf-8")
        else:
            return None

    def set(self, redis_key, redis_value, time_expire):
        self.redis_client.set(redis_key, redis_value.encode('utf-8'), ex=time_expire)
        self.redis_client.close()

    def delete(self, redis_key):
        self.redis_client.delete(redis_key)
        self.redis_client.close()
