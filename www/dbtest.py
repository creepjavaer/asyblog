#dbtest.py
import asyncio
import orm 
from models import User,Blog,Comment

async def test(lp):
	await  orm.create_pool(loop=lp,host='127.0.0.1',user='www-data',password='www-data',db='awesome')
	u = User(loop=lp,name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
	await u.save()

loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

