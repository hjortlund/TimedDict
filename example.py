import time
from TimedDict import timeddict

events_window = timeddict.TimedDict()

now = time.time()

# Assign values like a normal dict like:
events_window[now] = 'value_1'
events_window[now + 1] = 'value_2'

# ...or like:
events_window.update({now + 2: {'values': {'value_3', 'value_4'}}})

print('Raw data:')
print(events_window)

# NOTE:
# As the TimedDict has a thread running purging old elements, it's important to ether
# use the protect() or pause() followed by a resume() when iterating.

# Automatic by the use of context manager, protect() approach
with events_window.protect():
    print('\n- protect()')
    for event in events_window:
        print(event)

# Manual setting, pause() and resume() approach
events_window.pause()
print('\n- pause() followed by resume()')

for event in events_window:
    print(event)

events_window.resume()

# TTL example
print('\nLength of the TimedDict: {}'.format(len(events_window)))
print(events_window)
time.sleep(1.1)
print(events_window)
time.sleep(1)
print(events_window)
time.sleep(1)
print(events_window)

# Gracefully stop the purge thread
events_window.stop()
