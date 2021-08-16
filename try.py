import asyncio
import threading
async def count():
    # for i in range(1,4000000):
    print("one")
    await asyncio.sleep(1)
    print("Two")

async def main():
    for i  in range(0,5):
        await threading.Thread(asyncio.gather(count(), count())).start()
        await threading.Thread(asyncio.gather(count(), count())).start()
        await threading.Thread(asyncio.gather(count(), count())).start()
asyncio.run(main())


# from queue import Queue, LifoQueue, PriorityQueue
#
# # 先进先出队列
# q = Queue(maxsize=5)
# # 后进先出队列
# lq = LifoQueue(maxsize=6)
# # 优先级队列
# pq = PriorityQueue(maxsize=5)
#
# for i in range(5):
#     q.put(i)
#     lq.put(i)
#     pq.put(i)
#
# print("先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" % (q.queue, q.empty(), q.qsize(), q.full()))
#
# print("后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" % (lq.queue, lq.empty(), lq.qsize(), lq.full()))
#
# print("优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" % (pq.queue, pq.empty(), pq.qsize(), pq.full()))
#
#
# print(q.get(), lq.get(), pq.get())
#
#
# print("先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" % (q.queue, q.empty(), q.qsize(), q.full()))
#
# print("后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" % (lq.queue, lq.empty(), lq.qsize(), lq.full()))
#
# print("优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" % (pq.queue, pq.empty(), pq.qsize(), pq.full()))
