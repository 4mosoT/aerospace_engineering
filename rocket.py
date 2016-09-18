from math import log


class rocket:
    def __init__(self, structure):
        self.stages = structure['stages']
        self.payload = structure['payload']

    def initial_mass(self, stage):
        data = self.stages[stage:]
        initial_mass = float(sum(sum(x[:2]) for x in data)) + self.payload
        return initial_mass

    def final_mass(self, stage):
        initial_mass = self.initial_mass(stage)
        final_mass = initial_mass - self.stages[stage][0]
        return final_mass

    def prop_mass(self, stage):
        data = self.stages[stage:]
        prop_mass = float(sum(x[0] for x in data))
        return prop_mass

    def payload_mass(self):
        return self.payload

    def prop_fraction(self, stage):
        return self.prop_mass(stage) / self.initial_mass(stage)

    def payload_fraction(self, stage):
        return self.payload_mass() / self.initial_mass(stage)

    def delta_v(self, stage):
        isp = self.stages[stage][2]
        v_ext = 9.8 * isp
        initial_mass = self.initial_mass(stage)
        final_mass = self.final_mass(stage)
        delta_v = v_ext * log(initial_mass / final_mass)
        return delta_v

    def total_deltav(self):
        return sum([self.delta_v(x) for x in range(len(self.stages))])

    def detailed_deltav(self):
        deltas = [self.delta_v(x) for x in range(len(self.stages))]
        for x, y in enumerate(deltas):
            print "Stage {} dV is {}".format(x + 1, y)
        print "Total dV is {}".format(sum(deltas))


if __name__ == '__main__':
    structure = {'payload': 5000, 'stages': [(50000, 5000, 450), (50000, 5000, 450)]}
    rocket_1 = rocket(structure)
    rocket_1.detailed_deltav()
    structure = {'payload': 5000, 'stages': [(100000, 10000, 450)]}
    rocket_2 = rocket(structure)
    rocket_2.detailed_deltav()