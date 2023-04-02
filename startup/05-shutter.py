from ophyd import Device, Component as Cpt, EpicsSignal, EpicsSignalRO


class PShutter(Device):
    # TODO: extend the class to take care of the flaky state switching.
    open_cmd = Cpt(EpicsSignal, "Cmd:Opn-Cmd")
    close_cmd = Cpt(EpicsSignal, "Cmd:Cls-Cmd")
    status = Cpt(EpicsSignalRO, "Pos-Sts")


psh = PShutter("XF:08BMES-PPS{PSh}", name="psh")