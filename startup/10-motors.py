from ophyd import EpicsSignalRO, EpicsMotor, Device, Component as Cpt


class KBMirror(Device):
    dsh = Cpt(EpicsMotor, "BD}Mtr")
    ush = Cpt(EpicsMotor, "YD}Mtr")

    # BL staff does not want to expose these EpicsMotors PVs via ophyd/bluesky as they are manually controlled via CSS,
    # therefore we add individual components to read the values and record them as configuration attrs:
    dsb_rbv = Cpt(EpicsSignalRO, "BU}Mtr.RBV", kind="config")
    dsb = Cpt(EpicsSignalRO, "BU}Mtr.VAL", kind="config")
    usb_rbv = Cpt(EpicsSignalRO, "YU}Mtr.RBV", kind="config")
    usb = Cpt(EpicsSignalRO, "YU}Mtr.VAL", kind="config")

kbh = KBMirror("XF:08BMES-OP{Mir:KBH-Ax:", name="kbh")
kbv = KBMirror("XF:08BMES-OP{Mir:KBV-Ax:", name="kbv")
