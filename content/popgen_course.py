import tskit

class GeneticGenealogy(tskit.TableCollection):
    # A simple derived class for a tskit TableCollection, with 
    # helpfully-named wrapper functions for teaching
    def add_genome(self, time):
        return self.nodes.add_row(flags=tskit.NODE_IS_SAMPLE, time=time)

    def connect_genomes(self, left, right, parent, child):
        return self.edges.add_row(left, right, parent, child)

    def validate(self):
        self.sort()
        return self.tree_sequence()
