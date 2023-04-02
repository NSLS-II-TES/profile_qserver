# IPython startup files to work with `bluesky-queueserver`


This profile is a trimmed subset of the
[profile_collection](https://github.com/NSLS-II-TES/profile_collection) repo to
work with
[bluesky-queueserver](https://blueskyproject.io/bluesky-queueserver/tutorials.html).


## Start RE manager

```console
$ PYTHONPATH=$BS_PYTHONPATH AUTOALIGNMENT=yes start-re-manager --keep-re --startup-profile=qserver --redis-addr=epics-services-tes
```

## ZMQ client

```python

from bluesky_queueserver.manager.comms import zmq_single_request

zmq_single_request(method="environment_open")

In [12]: zmq_single_request(method="plans_allowed", params={"user_group": "primary"})
Out[12]:
({'success': True,
  'msg': '',
  'plans_allowed': {'bo_initialize': {'name': 'bo_initialize',
    'properties': {'is_generator': True},
    'parameters': [{'name': 'args',
      'kind': {'name': 'VAR_POSITIONAL', 'value': 2}},
     {'name': 'kwargs', 'kind': {'name': 'VAR_KEYWORD', 'value': 4}}],
    'module': 'startup_script'},
   'bo_go_to': {'name': 'bo_go_to',
    'properties': {'is_generator': True},
    'parameters': [{'name': 'args',
      'kind': {'name': 'VAR_POSITIONAL', 'value': 2}},
     {'name': 'kwargs', 'kind': {'name': 'VAR_KEYWORD', 'value': 4}}],
    'module': 'startup_script'},
   'bo_go_to_optimum': {'name': 'bo_go_to_optimum',
    'properties': {'is_generator': True},
    'parameters': [{'name': 'args',
      'kind': {'name': 'VAR_POSITIONAL', 'value': 2}},
     {'name': 'kwargs', 'kind': {'name': 'VAR_KEYWORD', 'value': 4}}],
    'module': 'startup_script'},
   'bo_learn': {'name': 'bo_learn',
    'properties': {'is_generator': True},
    'parameters': [{'name': 'args',
      'kind': {'name': 'VAR_POSITIONAL', 'value': 2}},
     {'name': 'kwargs', 'kind': {'name': 'VAR_KEYWORD', 'value': 4}}],
    'module': 'startup_script'},
   'take_background': {'name': 'take_background',
    'properties': {'is_generator': True},
    'parameters': [{'name': 'shutter',
      'kind': {'name': 'POSITIONAL_OR_KEYWORD', 'value': 1}},
     {'name': 'detectors',
      'kind': {'name': 'POSITIONAL_OR_KEYWORD', 'value': 1}}],
    'module': 'bloptools.gp.plans'},
   'take_tes_background': {'name': 'take_tes_background',
    'properties': {'is_generator': True},
    'parameters': [],
    'module': 'startup_script'}},
  'plans_allowed_uid': '8c097313-6ad8-4285-94e1-c5b88b7dc7b0'},

In [13]: zmq_single_request(method="queue_item_add", params={"item": {"name": "bo_initialize", "kwargs": {"init_scheme": "quasi-random", "n_init": 8}, "item_t
    ...: ype": "plan"}, "user": "mrakitin", "user_group": "primary"})
Out[13]:
({'success': True,
  'msg': '',
  'qsize': 1,
  'item': {'name': 'bo_initialize',
   'kwargs': {'init_scheme': 'quasi-random', 'n_init': 8},
   'item_type': 'plan',
   'user': 'mrakitin',
   'user_group': 'primary',
   'item_uid': 'f5516100-47cc-4295-81db-284c99030d73'}},
 '')

In [14]: zmq_single_request(method="queue_item_add", params={"item": {"name": "bo_go_to_optimum", "kwargs": {}, "item_type": "plan"}, "user": "mrakitin", "use
    ...: r_group": "primary"})
Out[14]:
({'success': True,
  'msg': '',
  'qsize': 2,
  'item': {'name': 'bo_go_to_optimum',
   'kwargs': {},
   'item_type': 'plan',
   'user': 'mrakitin',
   'user_group': 'primary',
   'item_uid': '633e98fb-50d1-4cab-a1fe-97e8087c7265'}},
 '')

In [15]: zmq_single_request(method="queue_get")
Out[15]:
({'success': True,
  'msg': '',
  'items': [{'name': 'bo_initialize',
    'kwargs': {'init_scheme': 'quasi-random', 'n_init': 8},
    'item_type': 'plan',
    'user': 'mrakitin',
    'user_group': 'primary',
    'item_uid': 'f5516100-47cc-4295-81db-284c99030d73'},
   {'name': 'bo_go_to_optimum',
    'kwargs': {},
    'item_type': 'plan',
    'user': 'mrakitin',
    'user_group': 'primary',
    'item_uid': '633e98fb-50d1-4cab-a1fe-97e8087c7265'}],
  'running_item': {},
  'plan_queue_uid': '622ce711-14e5-4d59-bb2c-c80813faec1d'},
 '')

In [16]: zmq_single_request(method="queue_start")
Out[16]: ({'success': True, 'msg': ''}, '')

In [17]: zmq_single_request(method="queue_item_add", params={"item": {"name": "bo_learn", "kwargs": dict(strategy="ei", n_iter=2, n_per_iter=2, reuse_hypers=T
    ...: rue, verbose=True, plots=[]), "item_type": "plan"}, "user": "mrakitin", "user_group": "primary"})
Out[17]:
({'success': True,
  'msg': '',
  'qsize': 1,
  'item': {'name': 'bo_learn',
   'kwargs': {'strategy': 'ei',
    'n_iter': 2,
    'n_per_iter': 2,
    'reuse_hypers': True,
    'verbose': True,
    'plots': []},
   'item_type': 'plan',
   'user': 'mrakitin',
   'user_group': 'primary',
   'item_uid': '6bb3e785-ec73-4c6b-b4d5-8b3c75a2bb27'}},
 '')

n [18]: zmq_single_request(method="queue_get")
Out[18]:
({'success': True,
  'msg': '',
  'items': [{'name': 'bo_learn',
    'kwargs': {'strategy': 'ei',
     'n_iter': 2,
     'n_per_iter': 2,
     'reuse_hypers': True,
     'verbose': True,
     'plots': []},
    'item_type': 'plan',
    'user': 'mrakitin',
    'user_group': 'primary',
    'item_uid': '6bb3e785-ec73-4c6b-b4d5-8b3c75a2bb27'}],
  'running_item': {},
  'plan_queue_uid': '7d1f0011-33b5-4fe5-bff2-b337b8472f24'},
 '')

In [19]: zmq_single_request(method="queue_start")
Out[19]: ({'success': True, 'msg': ''}, '')

```
