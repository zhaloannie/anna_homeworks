import redis
import config

r = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)

success = r.set('foo1111', 'bar1111')
# True

result = r.get('foo1111')
print(result)
# >>> bar

r.set("favorite_car", "Audi")
print(r.get("favorite_car"))

r.setex("favorite_pet", 7200, "My cat Alex")
print(r.get("favorite_pet"))

products =["Fruits", "Dairy Products", "Meat", "Sweets", "Vegetables"]
for product in products:
    for p in products:
        r.rpush("shopping_cart", p)
    r.expire("shopping_cart", 604800)
print(r.lrange("shopping_cart", 0, 2))

r.hset("cake", mapping= {
    "flour": 250,
    "milk": 500
})
r.hset("cake", "sugar", 500)
print(r.hgetall("cake"))
r.delete("cake")