import redis


class RedisClient:


    def __init__(self):

        self._redis = redis.asyncio.client.Redis.from_url()