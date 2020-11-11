import redis

r = redis.Redis(host='192.168.1.174',
                port=6379,
                db=2,
                password='3cgM0v2P6csVNxxxxxxxacWIf2i70eO')
r.set('hgg_session', '2020-09-04')
print(r.get('hgg_session'))
loglen = r.slowlog_len()
print(r.slowlog_get(loglen))

# cli save rdb to local
# bin/redis-cli -h 192.168.0.2 -p 6379 -a 'password'  --rdb xxx.rdb