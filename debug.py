import time
from tqdm.contrib.telegram import tqdm, trange

token = '5438553662:AAFbD67ZN3f-nwOa3Ox_8XvbHBVJPrjTto0'
chat_id = '402211218'
# https://api.telegram.org/5438553662:AAFbD67ZN3f-nwOa3Ox_8XvbHBVJPrjTto0/getUpdates
# import ipdb; ipdb.set_trace()

for i in trange(10, token='{token}', chat_id='{chat_id}'):
   time.sleep(0.1)
