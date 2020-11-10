import redis

r = redis.Redis(host='192.168.1.174',
                port=6379,
                db=2,
                password='3cgM0v2P6csVNxxxxxxxacWIf2i70eO')
r.set('hgg_session', '2020-09-04')
print(r.get('hgg_session'))
