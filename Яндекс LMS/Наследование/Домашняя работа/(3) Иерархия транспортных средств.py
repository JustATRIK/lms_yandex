class Transport:
    pass


class WaterTransport(Transport):
    pass


class Aircrafts(Transport):
    pass


class LandTransport(Transport):
    pass


class SpaceTransport(Transport):
    pass


class Boats(WaterTransport):
    pass


class Yachts(WaterTransport):
    pass


class CruiseShips(WaterTransport):
    pass


class WaterCargoTransport(WaterTransport):
    pass


class Planes(Aircrafts):
    pass


class Helicopters(Aircrafts):
    pass


class Airships(Aircrafts):
    pass


class Balloons(Aircrafts):
    pass


class RailwayTransport(LandTransport):
    pass


class BusTransport(LandTransport):
    pass


class CargoTransport(LandTransport):
    pass


class PrivateVehicles(LandTransport):
    pass


class SpacePassengerTransport(SpaceTransport):
    pass


class SpaceCargoTransport(SpaceTransport):
    pass
