# Limiter Document
 - schema
    ```py
    times: int
    per: int
    memory: ClassVar[Type[Memory]] = Memory
    ex: Type[HTTPException] = HTTPException
    identifier: Callable[[Union[Request, dict]], str] = identifier
    key_maker: Callable[[dict], str] = lambda kwargs: ''
    request_parameter_name: str = 'request'
    message: str = "too many requests"

    def init(cls, memory)
    ```

 - `times`: how many times client can request?
 - `per`: in `ms` , `times` / `per`
 - `memory`: satisfy limiter needs on any memory
   - to shared services you can use `RedisMemory(getter, setter)` from `farlimit.memory`
        ```py
        redis = get_redis_connection()
        Limiter.init(memory=RedisMemory(redis.get, redis.set))
        # done
        ```
 - `ex`: too many requests exception handler 
 - `identifier`: if not set use ip[X-Forwarded-For first], NAT problem, **it's result** use to **embed key** on `memory`
   - if don't set `identifier` you **have to** define `starlette.requests.Request` in endpoint arguments
  - key_maker: use to specification
 - `request_parameter_name`: if use `default identifier` and `starlette.requests.Request` argument has different name from `request` you must pass name in this field 