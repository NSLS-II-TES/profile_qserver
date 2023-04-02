import bluesky.plans as bp

# from bluesky.plan_stubs import one_1d_step
# from bluesky.plan_stubs import trigger_and_read
# from nslsii import configure_base
from bluesky import RunEngine
from bluesky.callbacks.best_effort import BestEffortCallback
from databroker import Broker
from nslsii import configure_kafka_publisher

RE = RunEngine({})

db = Broker.named("tes")
bec = BestEffortCallback()

RE.subscribe(db.insert)
RE.subscribe(bec)
res = configure_kafka_publisher(RE, beamline_name="tes")
