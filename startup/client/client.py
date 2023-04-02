from bluesky_queueserver import ZMQCommSendThreads
from bluesky_queueserver.manager.comms import zmq_single_request

if __name__ == "__main__":
    client = ZMQCommSendThreads(zmq_server_address="tcp://localhost:60615")

    zmq_single_request(method="environment_open")

    zmq_single_request(method="queue_get")

    zmq_single_request(method="plans_allowed", params={"user_group": "primary"})

    zmq_single_request(
        method="queue_item_add",
        params={
            "item": {
                "name": "bo_initialize",
                "kwargs": {"init_scheme": "quasi-random", "n_init": 4},
                "item_type": "plan",
            },
            "user": "mrakitin",
            "user_group": "primary",
        },
    )

    zmq_single_request(
        method="queue_item_remove",
        params={"uid": "dd8a2b46-63af-4ecd-9ae5-697e98b32cf4"},
    )

    zmq_single_request(method="queue_get")

    zmq_single_request(
        method="queue_item_add",
        params={
            "item": {
                "name": "take_background",
                "args": ["psh", ["vstream", "I0"]],
                "kwargs": {},
                "item_type": "plan",
            },
            "user": "mrakitin",
            "user_group": "primary",
        },
    )

    zmq_single_request(
        method="queue_item_add",
        params={
            "item": {
                "name": "bo_initialize",
                "kwargs": {"init_scheme": "quasi-random", "n_init": 4},
                "item_type": "plan",
            },
            "user": "mrakitin",
            "user_group": "primary",
        },
    )

    zmq_single_request(method="queue_get")

    zmq_single_request(method="queue_start")

    zmq_single_request(method="queue_get")

    zmq_single_request(
        method="queue_item_add",
        params={
            "item": {
                "name": "take_background",
                "args": ["psh", ["vstream", "I0"]],
                "kwargs": {},
                "item_type": "plan",
            },
            "user": "mrakitin",
            "user_group": "primary",
        },
    )

    zmq_single_request(
        method="queue_item_add",
        params={
            "item": {
                "name": "bo_initialize",
                "kwargs": {"init_scheme": "quasi-random", "n_init": 8},
                "item_type": "plan",
            },
            "user": "mrakitin",
            "user_group": "primary",
        },
    )

    zmq_single_request(method="queue_get")

    zmq_single_request(method="queue_item_remove", params={"pos": 0})

    zmq_single_request(method="queue_get")

    zmq_single_request(method="queue_start")

    zmq_single_request(method="status")
