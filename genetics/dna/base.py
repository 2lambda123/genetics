import abc


class DNABase(metaclass=abc.ABCMeta):
    '''
    DNABase is the base class for all dna. It defines the abstract methods that
    all DNA should have, as well as an __lt__ method for sorting.
    '''
    @abc.abstractmethod
    def total_length(self):
        '''
        This method returns the total length of this DNA. For dna with
        subcomponents, it should return the sum of the lengths of those
        components. See DNASegment for an example
        '''
        pass

    @abc.abstractmethod
    def mutate(self, mask):
        '''
        This method should return a DNA object that is the result of applying
        the mutation mask to each component of this DNA. It is allowed to
        return self if and only if the mask application doesn't change the dna
        at all.
        '''
        pass

    @abc.abstractmethod
    def combine(self, other, mask):
        '''
        Return a tuple of two new DNAs that are the result of combining this
        DNA with other, using the mask.
        '''
        pass

    def __lt__(self, other):
        return self.score < other.score

    def has_score(self):
        return hasattr(self, 'score')


def combine_element_pairs(pairs):
    '''
    When given an iterable that returns pairs- such as
    [(1, 2), (3, 4), (5, 6)] combine them into a pair of iterables, such as
    ((1, 3, 5), (2, 4, 6))
    '''

    return tuple(zip(*pairs))
