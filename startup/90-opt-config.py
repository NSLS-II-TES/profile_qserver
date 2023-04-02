from bloptools import gp

kb_dofs = np.array([kbv.ush, kbv.dsh, kbh.ush, kbh.dsh])

rel_bounds = {
    "kbv_ush": [-1e-1, +1e-1],
    "kbv_dsh": [-1e-1, +1e-1],
    "kbh_ush": [-1e-1, +1e-1],
    "kbh_dsh": [-1e-1, +1e-1],
    "ssa_inboard": [-1e-1, +1e-1],
    "ssa_outboard": [-1e-1, +1e-1],
    "toroidal_mirror_ush": [-1e-1, +1e-1],
    "toroidal_mirror_dsh": [-1e-1, +1e-1],
    "toroidal_mirror_usy": [-1e-1, +1e-1],
    "toroidal_mirror_dsy": [-1e-1, +1e-1],
}
fid_params = {
    "kbv_ush": 0.050,
    "kbv_dsh": 0.030,
    "kbh_ush": 2.485,
    "kbh_dsh": 3.532,
    "ssa_inboard": -0.3700,
    "ssa_outboard": -0.1705,
    "toroidal_mirror_ush": -9.530,
    "toroidal_mirror_dsh": -3.900,
    "toroidal_mirror_usy": -6.280,
    "toroidal_mirror_dsy": -9.160,
}

dofs = kb_dofs[:2]
hard_bounds = np.r_[[fid_params[dof.name] + 1 * np.array(rel_bounds[dof.name]) for dof in dofs]]

print(f"{dofs = }")
print(f"{hard_bounds = }")

boa = gp.BayesianOptimizationAgent(
    detectors=[vstream, I0],
    shutter=psh,
    mode="tes",
    db=db,
    dofs=dofs,
    dof_bounds=hard_bounds,
    verbose=True,
)


def boa_initialize(*args, **kwargs):
    """
    Example call
    ------------
        boa.initialize(init_scheme="quasi-random", n_init=4)
    """
    yield from boa.initialize(*args, **kwargs)


def boa_go_to(*args, **kwargs):
    """
    Example call
    ------------
        boa.go_to(x)
    """
    yield from boa.go_to(*args, **kwargs)


def boa_go_to_optimum(*args, **kwargs):
    """
    Example call
    ------------
        boa.go_to_optimum()
    """
    yield from boa.go_to_optimum(*args, **kwargs)


def boa_learn(*args, **kwargs):
    """
    Example call
    ------------
        boa.learn(strategy, n_iter=1, n_per_iter=1, reuse_hypers=True, upsample=1, verbose=True, plots=[], **kwargs)
    """
    yield from boa.learn(*args, **kwargs)
