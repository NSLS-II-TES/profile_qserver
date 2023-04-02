from bloptools.gp.plans import take_background
from bluesky_adaptive.on_stop import recommender_factory
from bluesky_adaptive.per_start import adaptive_plan


def take_tes_background():
    yield from take_background(psh, [vstream])


def boa_adaptive(dets):
    recommender = boa  # defined in 90-opt-config.py
    cb, queue = recommender_factory(
        adaptive_obj=recommender,
        independent_keys=boa.dof_names,
        dependent_keys=boa.det_names,
        target_keys=[],
        max_count=2**4,
    )
    yield from adaptive_plan(
        dets, {k: v for k, v in zip(boa.dofs, boa.optimum)}, to_recommender=cb, from_recommender=queue
    )
    print(f"{recommender.result = }")
