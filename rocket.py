from math import log


class rocket:
    def __init__(self, structure):
        #Stages have to be a list of tuples [(kg of propellant stage 1, kg structural mass stage 1, isp)]
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
            print "Stage {} dV is {}".format(x, y)
        print "Total dV is {}".format(sum(deltas))


if __name__ == '__main__':
    falcon_9_structure = {'payload': 13150, 'stages': [(395700, 23100, 282), (64820, 3900, 340)]}
    falcon_9 = rocket(falcon_9_structure)
    falcon_9.detailed_deltav()

