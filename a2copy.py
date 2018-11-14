# First Create a Chromosome class
class Chromosome():
    '''This class represents a chromomsome
    '''
    def __init__(self):
        '''(Chromosome, pos, nucelo) -> NoneType
        This creates a new chromosome class the postion in the nucleotide pair
        list and the nucelo that wants to be placed at the postion
        '''
        # create a list to hold the nucleotide pairs
        self.nucelotide_list = []

    def set_by_pos(self, pos, nucleo):
        '''(Chromosome, pos, nucelo) -> NoneType
        This method puts the given nucleotide pair at the given pos
        of this chromosome
        REQ: nucleo can only consists of A,T,C,G and from 1->9
        RAISES ManyNucleoError if len(pos) > 2
        '''
        self._nucelo = nucleo
        self._pos = pos
        # Create exceptions for if user inputs invalid str objects for the
        # nucleotides
        nucleo_error = 'Only 2 nucleotides can be assigned to a position'
        if len(str(nucleo)) > 2:
            raise ManyNucleoError(nucleo_error)
        else:
            # Create a loop to add the given nucleo at the given pos
            for index in range(self._pos + 1):
                if index is self._pos:
                    self.nucelotide_list.append('')
                    self.nucelotide_list[self._pos] = str(self._nucelo)
                else:
                    self.nucelotide_list.append('')

    # Create a method that reurns the list of nucelotides that the chromosome
    # holds
    def get_nucleotide_list(self):
        '''(Chromosme) -> list
        This method returns the list of nucleotides that a chromosome holds.
        '''
        return self.nucelotide_list

    def get_pos(self, pos):
        '''(Chromosome, int) -> str
        This method returns the nucelotide pair, given the its position
        '''
        return self.nucelotide_list[pos]

    def __str__(self):
        '''(Chromosome) -> str
        This Method prints out a statment to say what the class represents
        '''
        return 'This class represents 1 Chromosome in a genome sequence'


# Create an animal class for animals to better classify living things
class Animal (Chromosome):
    '''This class represents
    '''
    def __init__(self):
        '''(Animal) -> NoneType
        This method creates an instance of an animal
        '''
    def __str__(self):
        '''(Animal) -> str
        This Method prints out a statment to say what the class represents
        '''
        return 'This class represnts all types of animals'


# Create a mamal class so that for future uses, it is easy to classify other
# animals instead of just humans
class Mammal(Animal):
    '''This class represents a mammal
    '''
    def __init__(self):
        '''(Mammal) -> NoneType
        this method creates a new mammal class
        '''
    def __str__(self):
        '''(Mammal) -> str
        This Method prints out a statment to say what the class represents
        '''
        return 'I am an animal that is a mammal'


# create a class that represents humans
class Human(Mammal):
    '''This class represents a Female human being
    '''
    def __init__(self, client_ID):
        '''(Huamn, str) -> NoneType
        This method creates a human being
        '''
        client_ID = self._client_ID

    def __str__(self):
        '''(Human) -> str
        This Method prints out a statment to say what the class represents
        '''
        return 'I am a Human being with ' + str(self._client_ID)

    def get_id(self):
        '''(Human) -> str
        This method returns the client ID of the human
        '''
        return str(self._client_ID)

    def get_chromosome_list(self):
        '''(Human or Query or Binder) -> list
        This method returns the list of chromosomes in the person's genome
        '''
        return self._chromosome_list

    def set_by_pos(self, pair, pos, nucleo):
        '''(Human or Query or Binder, int, int, str) -> Nonetype
        This method assigns a nucleotide pair to a SPECIFIC chromosome at a
        SPECIFIC position within the chromosome
        REQ: pair has to be an int
        REQ: pos has to be an int
        RAISES InvalidPairError if the pair given < 0 or pair > 22
        RAISES InvalidPosError if the postion < 0
        '''
        pair_error_msg = 'The pair to be assigned has to be >= 0, <= 22'
        # Create an exception for when pair and pos < 0
        if (pair < 0) or (pair > 22):
            raise InvalidPairError(pair_error_msg)
        if pos < 0:
            raise InvalidPosError('The pos to be assigned has to be >= 0')
        else:
            # You want to loop until the pair given
            for index in range(pair + 1):
                if index is pair:
                    self._chromosome_list.append('')
                    # Now check if the chromosome pair had been previously
                    # set so that it will not overide
                    if type(self._chromosome_list[pair]) is Chromosome:
                        self._chromosome_list[pair].set_by_pos(pos, nucleo)
                    else:
                        # append an empty string tp the list so that there is a
                        # value
                        # at the index to change
                        self._chromosome_list.append('')
                        # Now put the chromosome class at the given index.
                        # This way the chromosome pair MATCHES with the list
                        # index. This is useful when you want to use methods
                        # on specific chromosomes later on
                        self._chromosome_list[pair] = Chromosome()
                        self._chromosome_list[pair].set_by_pos(pos, nucleo)
                else:
                    # Keep appending so that when index == self._pair, its
                    # chromosome pair number matches with the index of the list
                    # that holds the person's Chromosomes
                    self._chromosome_list.append('')

    def set_marker(self, marker, pair, pos):
        '''(Human or Query or Binder, str, int, int) -> NoneType
        This method assigns the given marker to a SPECIFIC position within the
        given pair
        REQ: pair has to be an int
        REQ: pos has to be an int
        RAISES InvalidPairError if the pair given < 0
        RAISES InvalidPosError if the postion < 0
        '''
        # Create an exception for when pair < 0 and pos < 0
        if (pair < 0) or (pair > 22):
            raise InvalidPairError('The pair to be assigned must >= 0 or < 22')
        if pos < 0:
            raise InvalidPosError('The pos to be assigned has to be >= 0')
        else:
            # Make the marker given, hold a list containing the desired pair
            # and the pos. It will be [pair, pos] ALWAYS. this way you can
            # easily retrive the desired pair and postion
            self._marker_dict[marker] = [pair, pos]

    def set_by_marker(self, marker, nucleo):
        '''(Human or Query or Binder, str, str) -> NoneType
        This method assigns a new nucleotide pair given a marker that had
        already been assigned to a SPECIFIC position within a chromosome pair.
        RAISES ExceptionKeyError if an unknown marker is given
        '''
        # Create an exception to only assign nucleotides to markers that have
        # been previously set
        # Set the statement for the key error, because the line will be too
        # long
        key_error_state = 'The marker you are trying to assign nucelotides '
        key_error_state = key_error_state + 'has not been set'
        try:
            # First you know that the marker maps to a list which ALWAYS
            # contains the pair in the 0 index. Assign it to a variable to
            # call it later
            pair = self._marker_dict[marker][0]
            # Now do the same for the postion
            pos = self._marker_dict[marker][1]
            # Now using the pair and pos you can now assign a nucleotide pair
            # to the list using the given nucelo
            self.set_by_pos(pair, pos, nucleo)
        # Make nothing happen if the marker does not exist
        except KeyError:
            raise InvalidMarkerError(key_error_state)

    def get_by_marker(self, marker):
        '''(Human or Query or Binder, str) -> str
        This method returns the nucleotide pair that is attached to the maker
        RAISES ExceptionKeyError if an unknown marker is set
        RAISES ExceptionIndexError is the pair attached to the marker is not
        defined
        RAISES ExceptionAttributeError if the there are no nucleotides at the
        position attatched to the marker
        '''
        # Create an exceptio statment to check if marker is valid (if the)
        # marker has been set already
        try:
            # get the chromosome pair it is attched to
            pair = self._marker_dict[marker][0]
            # Create an exception for if the index of pair does not exist in
            # the list of chromosomes
            try:
                # get the pair in the chromosome list of the person
                req_chromosome = self._chromosome_list[pair]
                # get the list of nucleotides that the pair has
                # Create an exception if req_chromosome is not a Chromosome
                # object
                try:
                    nucleo_list = req_chromosome.get_nucleotide_list()
                    # Now get the specific nucleotide pair in the position
                    # that the marker holds
                    pos = self._marker_dict[marker][1]
                    # you want to raise an exception if at the
                    # index, it is empty
                    # Again make the statment to be ouputted when the
                    # exception caught to be a varaiable so that the line
                    # is not too long
                    empty_pos_error = 'The position attached to the marker '
                    empty_pos_error = empty_pos_error + 'does is not defined '
                    empty_pos_error = empty_pos_error + 'in the genome'
                    no_pair_error = 'the pair attached to the marker is not '
                    no_pair_error = no_pair_error + 'defined'
                    if nucleo_list[pos] == '':
                        raise NoPosError(empty_pos_error)
                    else:
                        req_nucleo = nucleo_list[pos]
                    return req_nucleo
                except AttributeError:
                    raise NoPairError(no_pair_error)
            # Catch an index error where there is no pair defined
            except IndexError:
                raise NoPairError(no_pair_error)
        # Catch the key error for when the user tries to get a marker that
        # does not exist
        except KeyError:
            raise Exception('the marker inputed has not been set')

    def get_chromosome(self, pair):
        '''(Female or Male or Query or Binder, int) -> Chromosome
        This method returns the required chromosome class given the number of
        the pair
        RAISES Exception if the pair number < 0
        '''
        # Create an exception for if the user enters pair < 0
        if pair < 0 or pair > 22:
            raise InvalidPairError('only get chromosomes from the > 0, < 22')
        else:
            # First create a Chromosome with the given pair in case if it does
            # not exsist
            # then put it in the index that is equivalent to pair
            # get the required Chromosme class from the list of chromosomes
            # Create an if statement to check con
            # Check if the index exists in the chromosome list
            if pair > (len(self._chromosome_list) - 1):
                # get the difference in the length of the chromosme list - 1
                # so you can add the amount of empty spaces to make the desired
                # index to exist
                pair_difference = pair - (len(self._chromosome_list) - 1)
                for index in range(pair_difference):
                    # add an empty string to the end of the list so it is able
                    # to change to a chromosome
                    # this will work because the loop will stop at 1 before the
                    # pair difference
                    self._chromosome_list.append('')
                chromosome_var = self._chromosome_list[pair] = Chromosome()
            elif type(self._chromosome_list[pair]) is Chromosome:
                chromosome_var = self._chromosome_list[pair]
            else:
                chromosome_var = self._chromosome_list[pair] = Chromosome()
        return chromosome_var

    def set_chromosome(self, old_pair, new_pair):
        '''(Human or Query or Binder, int, Chromosome) -> NoneType
        This method assigns the new_pair given in place of the old pair_given
        REQ: new_pair type  has to be a Chromosome
        RAISES Exception if the pair you are trying to change a pair < 0
        '''
        # Create an exception if the user tries to assign or re-assign a pair
        # < 0
        # Account for if the user tries to change negative postion
        # chromosomes
        if (old_pair < 0) or (old_pair > 22):
            raise InvalidPairError('The old pair has to be > = 0 or <=22')
        else:
            if old_pair > (len(self._chromosome_list) - 1):
                pair_difference = old_pair - (len(self._chromosome_list) - 1)
                for index in range(pair_difference):
                    # add an empty string to the end of the list so it is
                    # able to change to a chromosome
                    # this will work because the loop will stop at 1 before
                    # the pair difference
                    self._chromosome_list.append('')
                self._chromosome_list[old_pair] = new_pair
            else:
                self._chromosome_list[old_pair] = new_pair

    def get_by_pos(self, pair, pos):
        '''(Human or Query or Binder, int, int) -> str
        this method returns the nucelotide pair, given a specific chromosome
        pair and postion
        RAISES ExceptionIndexError if the chromosome pair you are trying to
        retrieve is not defined
        RAISES ExceptionIndexError if the pos inputed is not defined
        RAISES Exception if the pos inputed is empty
        '''
        # Raise an exception if the pair given < 0
        if (pair < 0) or (pos < 0):
            raise InvalidPairError('Cannot retrieve pair of pos that is < 0')
        # Account for if the chromosome pair does not exist
        try:
            chromosome = self._chromosome_list[pair]
            # Before you get the nucleotides at the given position, make sure
            # that nucelotides have been assigned to the position
            nucleo_list = chromosome.get_nucleotide_list()
            # Account for if the position does not exist
            try:
                # Now use the get_pos function in the chromosome
                result_nucelo = chromosome.get_pos(pos)
                # Now use an if-statement check if the position is
                # empty
                if result_nucelo == '':
                    raise NoPosError('The given position is not set')
                # Return the nucleotides at the given position
                return result_nucelo
            except IndexError:
                raise NoPosError('The position inputed has not been set')
        except IndexError:
            raise NoPairError('The chromosome pair inputed has not been set')

    def procreate(self, father, binder):
        '''(Female, Male, binder) -> Human
        This method creates a child male or female, depending on the sex
        assigned to the binder. When a child is being made, the client ID of
        the mother is used and 0 is added to back of the child's ID. This
        will happen everytime a female procreates. This way we can easily
        identify or find the child of mothers
        RAISES ExceptionIndexError if The Father or Mother chromosome pairs
        are undefined where binder was defined
        RAISES ExceptionIndexError if Father or Mother postions are not defined
        where binder was defined
        RAISES Exception if the sex attached to the binder is not male or
        female
        '''
        # FIRST BEFORE ANY CREATION CAN HAPPEN, the 1 paracmeter passed, the
        # type HAS to be Male
        # You want to catch any attribute error that could occur, if the
        # user input's type are not Binder or Father
        # make seperate if statements because you to return specific exceptions
        # to tell the user what they did wrong want to each condition to be
        # passed on at a time.
        # Again assign the error to be raised to a variable so that the line is
        # not too long
        no_binder_error = 'binder input is not an attribute of Binder class'
        if type(binder) is not Binder:
            raise NobinderError(no_binder_error)
        if type(father) is not Male:
            raise ProcreateError('Two Females cannot procreate')
        elif type(father) is Male:
            # First get the sex of the child
            sex_of_child = binder.get_sex()
            # get the client_ID of the mother
            child_id = self.get_id()
            # Then use an if stament to choose whether to create a male or
            # a female
            if sex_of_child == 'F':
                child = Female(str(child_id) + '0')
            elif sex_of_child == 'M':
                child = Male(str(child_id) + '0')
            else:
                raise Exception('You need to set the sex for the binder')
            # now assign nucleotides to the DNA of the child using the binder
            # Get the chromosomes that the binder, and the father has
            binder_chromosomes = binder.get_chromosome_list()
            father_chromosomes = father.get_chromosome_list()
            mother_chromosomes = self.get_chromosome_list()
            # Before looping, get the length of the binder chromosome list
            # so that you do not end up trying to retrieve information from
            # an index that does not exsist
            len_of_binder = len(binder_chromosomes)
            # Now create a loop to iterate through the chromosomes of the
            # binder
            for chromosome_index in range(len_of_binder):
                # get the chromosome list of both the father and the mother
                # for each index
                # ONLY PERFORM THE NEXT LINES IFF the type of the object at the
                # index of the binder is a chromsome
                try:
                    if ((type(binder_chromosomes[chromosome_index])) and
                        (type(father_chromosomes[chromosome_index])) and
                        (type(mother_chromosomes[chromosome_index])) is
                            Chromosome):
                        binder_nucleo = binder_chromosomes[
                            chromosome_index].get_nucleotide_list()
                        father_nucleo = father_chromosomes[
                            chromosome_index].get_nucleotide_list()
                        # Also get the nucelotides of the mother as well
                        mother_nucleo = self._chromosome_list[
                            chromosome_index].get_nucleotide_list()

                        # Again before creating another loop get the length of
                        # the binder nucleo list so that you do not end up
                        # trying to retrieve information from an index that
                        # does not exsist
                        len_of_binder_nucelo = len(binder_nucleo)
                        # Now create the for loop to iterate through each index
                        # of the binder
                        for nucleo_index in range(len_of_binder_nucelo):
                            # Now make sure that the index at the pos of the
                            # father and mother is not empty
                            # Again assign the error to be raised to a variable
                            # so that the line is not too long
                            undefined_pos = 'Father or Mother postions are '
                            undefined_pos = undefined_pos + 'not defined '
                            undefined_pos = undefined_pos + 'where marker '
                            undefined_pos = undefined_pos + 'was defined '
                            undefined_chromo = 'Father or Mother chromosomes '
                            undefined_chromo = undefined_chromo + 'and not '
                            undefined_chromo = undefined_chromo + 'defined '
                            undefined_chromo = undefined_chromo + 'where '
                            undefined_chromo = undefined_chromo + 'marker was '
                            undefined_chromo = undefined_chromo + 'defined '
                            try:
                                # create if statment to check if the postion is
                                # 'LM' or 'RM'
                                if binder_nucleo[nucleo_index] == 'LM':
                                    # set the nucleotide at the current index
                                    # of the child to be the 0 index of the
                                    # mom's
                                    # Check if the position is empty
                                    if ((mother_nucleo[nucleo_index] == '') or
                                            (father_nucleo[nucleo_index] ==
                                             '')):
                                        raise Exception(undefined_pos)
                                    else:
                                        child.set_by_pos(chromosome_index,
                                                         nucleo_index,
                                                         (mother_nucleo[
                                                             nucleo_index][
                                                                 0]) +
                                                         (father_nucleo[
                                                             nucleo_index][1]))
                                elif binder_nucleo[nucleo_index] == 'RM':
                                    # Check if the position is empty
                                    if ((mother_nucleo[nucleo_index] == '') or
                                            (father_nucleo[nucleo_index] ==
                                             '')):
                                        raise Exception(undefined_pos)
                                    else:
                                        child.set_by_pos(chromosome_index,
                                                         nucleo_index,
                                                         father_nucleo[
                                                             nucleo_index][0] +
                                                         mother_nucleo[
                                                             nucleo_index][1])
                            except IndexError:
                                raise NoPosError(undefined_pos)
                except IndexError:
                    raise NoPairError(undefined_chromo)
        return child

    def test(self, query):
        '''(Human, Query) -> bool
        This method is used to check if certain patterns exist in a person's
        genome. The query is rejected of the nucleotides in the postion of
        the query does not match the person's. If the query postition is
        defined where the person's is not, the query will not be rejected
        because there is no position to test.
        The only exception is at the 23 chromosome of a Male, if there are
        unknown nucleotides, then the query is rejected
        '''
        # First, because we are only catching an error when the user tries
        # to compare the 23rd chromosome so set the overall result to True
        # so that the query is only rejected when it is false
        result = True
        # First get the list of chromosomes in the genomeof the person and
        # the query
        person_chromosomes = self.get_chromosome_list()
        query_chromosomes = query.get_chromosome_list()
        # Becuase you want the same memory nucleotides thorugh out the
        # whole genome, you want to create different boolean for each letter
        # so that when it is found the loop that assigns the memory nucleotides
        # stops
        found_matchAL = False
        found_matchAR = False
        found_matchTL = False
        found_matchTR = False
        found_matchCL = False
        found_matchCR = False
        found_matchGL = False
        found_matchGR = False
        # You also want to assign the values memory nucleotides outside the
        # loop so that they dont get reassigned at each new chromosome
        memory_nucleoAL = ''
        memory_nucleoAR = ''
        memory_nucleoTL = ''
        memory_nucleoTR = ''
        memory_nucleoCL = ''
        memory_nucleoCR = ''
        memory_nucleoGL = ''
        memory_nucleoGR = ''
        # You want to catch an exception for if the query is defined where
        # the person's nucleotides is not. The query will not be rejected
        # because there is nothing to cmpare it to, just set the ouput to
        # True
        try:
            index_chromo = 0
            # You want to loop through the list of the query only cause once
            # the query list ends, there is nothing to compare
            while index_chromo < (len(query_chromosomes)) and result is True:
                # Now you want to only perform the next steps if the objects
                # at the current index is a Chromosome object or else there is
                # no point in checking
                if ((type(query_chromosomes[index_chromo]) is Chromosome) and
                        ((type(person_chromosomes[index_chromo])) is
                         (Chromosome))):
                    # Now get the nucleotides assigned to the chromosome pair
                    query_nucleo = query_chromosomes[
                        index_chromo].get_nucleotide_list()
                    person_nucleo = person_chromosomes[
                        index_chromo].get_nucleotide_list()
                    # Now you want to get the value of each memmory nucleotide
                    # create a list of what the memory nucleotides can be
                    memory_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                                   '0']
                    # now you want to use an exception to catch an error if
                    # the there are no nucleotides at the the person's position
                    # again, since there is nothing to compare it to, the query
                    # will not be rejected
                    try:
                        index = 0
                        # Since there are only 4 possible letter nucleotides,
                        # we just need to get what the first letter of each
                        # type is matched with in the query
                        # do it for the 0 index first, then for the 1 index
                        # since there can be only be 2 positions filled
                        while ((index < len(query_nucleo)) and
                               (found_matchAL is False)):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][0] == 'A':
                                    # if in the query it is itself,
                                    # just pass cause we are looking for int
                                    if query_nucleo[index][0] == 'A':
                                        # pass because we don't care if the
                                        # query nucleotide matches the person's
                                        pass
                                    elif ((query_nucleo[index][0]) in
                                          (memory_list)):
                                        memory_nucleoAL = (query_nucleo[
                                            index][0])
                                        found_matchAL = True
                                    # If it is not a match of itself or an int
                                    # then we do not care about it so we just
                                    # pass
                                    else:
                                        pass
                            index = index + 1
                        # Now run the same loop but for the right index
                        # just in case the memory nucleotide is in the right
                        # index
                        # RIGHT
                        index = 0
                        while ((index < len(query_nucleo)) and
                               (found_matchAR is False)):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][1] == 'A':
                                    if query_nucleo[index][1] == 'A':
                                        pass
                                    elif ((query_nucleo[index][1]) in
                                          (memory_list)):
                                        memory_nucleoAR = (query_nucleo[
                                            index][1])
                                        found_matchAR = True
                                    else:
                                        pass
                            index = index + 1
                        # Now Check if both memory nucleotides are thesame
                        # if they are not thesame
                        if memory_nucleoAL == memory_nucleoAR:
                            memory_nucleoA = memory_nucleoAL
                        elif ((memory_nucleoAL == '') and
                              (memory_nucleoAR is not '')):
                            memory_nucleoA = memory_nucleoAR
                        elif ((memory_nucleoAL is not '') and
                              (memory_nucleoAR == '')):
                            memory_nucleoA = memory_nucleoAL
                        else:
                            memory_nucleoA = ''
                        # FIND THE MEMORY NUCLEOTIDE OF T
                        index = 0
                        while ((index < len(query_nucleo)) and
                               (found_matchTL is False)):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][0] == 'T':
                                    if query_nucleo[index][0] == 'T':
                                        pass
                                    elif ((query_nucleo[index][0]) in
                                          (memory_list)):
                                        memory_nucleoTL = (query_nucleo[
                                            index][0])
                                        found_matchTL = True
                                    else:
                                        pass
                            index = index + 1
                        # Now run the same loop but for the right index
                        # just in case the memory nucleotide is in the right
                        # index
                        index = 0
                        while ((index < len(query_nucleo)) and
                               (found_matchTR is False)):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][1] == 'T':
                                    if query_nucleo[index][1] == 'T':
                                        pass
                                    elif ((query_nucleo[index][1]) in
                                          (memory_list)):
                                        memory_nucleoTR = (query_nucleo[
                                            index][1])
                                        found_matchTR = True
                                    else:
                                        pass
                            index = index + 1
                        # Now Check if both memory nucleotides are thesame
                        # if they are not thesame
                        if memory_nucleoTL == memory_nucleoTR:
                            memory_nucleoT = memory_nucleoTL
                        elif ((memory_nucleoTL == '') and
                              (memory_nucleoTR is not '')):
                            memory_nucleoT = memory_nucleoTR
                        elif ((memory_nucleoTL is not '') and
                              (memory_nucleoTR == '')):
                            memory_nucleoT = memory_nucleoTL
                        else:
                            memory_nucleoT = ''
                        # FIND THE MEMORY NUCLEOTIDE OF C
                        index = 0
                        while ((index < len(query_nucleo)) and
                               (found_matchCL is False)):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][0] == 'C':
                                    if query_nucleo[index][0] == 'C':
                                        pass
                                    elif ((query_nucleo[index][0]) in
                                          (memory_list)):
                                        memory_nucleoCL = (query_nucleo[
                                            index][0])
                                        found_matchCL = True
                                    else:
                                        pass
                            index = index + 1
                        # Now run the same loop but for the right index
                        # just in case the memory nucleotide is in the right
                        # index
                        index = 0
                        while ((index < len(query_nucleo)) and
                               (found_matchCR is False)):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][1] == 'C':
                                    if query_nucleo[index][1] == 'C':
                                        pass
                                    elif ((query_nucleo[index][1]) in
                                          (memory_list)):
                                        memory_nucleoCR = (query_nucleo[
                                            index][1])
                                        found_matchCR = True
                                    else:
                                        pass
                            index = index + 1
                        # Now Check if both memory nucleotides are thesame
                        # if they are not thesame
                        if memory_nucleoCL == memory_nucleoCR:
                            memory_nucleoC = memory_nucleoCL
                        elif ((memory_nucleoCL == '') and
                              (memory_nucleoCR is not '')):
                            memory_nucleoC = memory_nucleoCR
                        elif ((memory_nucleoCL is not '') and
                              (memory_nucleoCR == '')):
                            memory_nucleoC = memory_nucleoCL
                        else:
                            memory_nucleoC = ''
                        # FIND THE MEMORY NUCLEOTIDE OF G
                        index = 0
                        while ((index < len(query_nucleo)) and
                               (found_matchGL is False)):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][0] == 'G':
                                    if query_nucleo[index][0] == 'G':
                                        pass
                                    elif ((query_nucleo[index][0]) in
                                          (memory_list)):
                                        memory_nucleoGL = (query_nucleo[
                                            index][0])
                                        found_matchGL = True
                                    else:
                                        pass
                            index = index + 1
                        # Now run the same loop but for the right index
                        # just in case the memory nucleotide is in the right
                        # index
                        index = 0
                        while ((index < len(query_nucleo)) and
                               (found_matchGR is False)):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][1] == 'G':
                                    if query_nucleo[index][1] == 'G':
                                        pass
                                    elif ((query_nucleo[index][1]) in
                                          (memory_list)):
                                        memory_nucleoGR = (query_nucleo[
                                            index][1])
                                        found_matchGR = True
                                    else:
                                        pass
                            index = index + 1
                        # Now Check if both memory nucleotides are thesame
                        # if they are not thesame
                        if memory_nucleoGL == memory_nucleoGR:
                            memory_nucleoG = memory_nucleoGL
                        elif ((memory_nucleoGL == '') and
                              (memory_nucleoGR is not '')):
                            memory_nucleoG = memory_nucleoGR
                        elif ((memory_nucleoGL is not '') and
                              (memory_nucleoGR == '')):
                            memory_nucleoG = memory_nucleoGL
                        else:
                            memory_nucleoG = ''
                        # Now that you have every memory nucleotides to each
                        # letter check if at each letter, it is ALWAYS equal to
                        # the value or itself
                        # START WITH THE LEFT INDEX FOR A
                        index = 0
                        matchAL = True
                        while index < len(query_nucleo) and (matchAL is True):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][0] == 'A':
                                    if query_nucleo[index][0] == 'A':
                                        matchAL = True
                                    elif ((query_nucleo[index][0]) ==
                                          (memory_nucleoA)):
                                        matchAL = True
                                    # Account for when the postion within the
                                    # sex chromosome of a male is not defined
                                    else:
                                        matchAL = False
                            elif ((type(self) is Male) and
                                  (index_chromo is 22) and
                                  (person_nucleo[index] == '') and
                                  (query_nucleo[index] != '')):
                                matchAL = False
                            index = index + 1
                        # Now for the right index
                        index = 0
                        matchAR = True
                        while index < len(query_nucleo) and (matchAR is True):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][1] == 'A':
                                    if query_nucleo[index][1] == 'A':
                                        matchAR = True
                                    elif ((query_nucleo[index][1]) ==
                                          (memory_nucleoA)):
                                        matchAR = True
                                    else:
                                        matchAR = False
                            index = index + 1
                        # NOW LOOK AT T
                        index = 0
                        matchTL = True
                        while index < len(query_nucleo) and (matchTL is True):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][0] == 'T':
                                    if query_nucleo[index][0] == 'T':
                                        matchTL = True
                                    elif ((query_nucleo[index][0]) ==
                                          (memory_nucleoT)):
                                        matchTL = True
                                    else:
                                        matchTL = False
                            index = index + 1
                        # now look at the right index
                        index = 0
                        matchTR = True
                        while index < len(query_nucleo) and (matchTR is True):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][1] == 'T':
                                    if query_nucleo[index][1] == 'T':
                                        matchTR = True
                                    elif ((query_nucleo[index][1]) ==
                                          (memory_nucleoT)):
                                        matchTR = True
                                    else:
                                        matchTR = False
                            index = index + 1
                        # AND NOW FOR C
                        index = 0
                        matchCL = True
                        while index < len(query_nucleo) and (matchCL is True):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][0] == 'C':
                                    if query_nucleo[index][0] == 'C':
                                        matchCL = True
                                    elif ((query_nucleo[index][0]) ==
                                          (memory_nucleoC)):
                                        matchCL = True
                                    else:
                                        matchCL = False
                            index = index + 1
                        # now look at the when 'C' could be in the right index
                        index = 0
                        matchCR = True
                        while index < len(query_nucleo) and (matchCR is True):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][1] == 'C':
                                    if query_nucleo[index][1] == 'C':
                                        matchCR = True
                                    elif ((query_nucleo[index][1]) ==
                                          (memory_nucleoC)):
                                        matchCR = True
                                    else:
                                        matchCR = False
                            index = index + 1
                        # NOW FOR G
                        index = 0
                        matchGL = True
                        while index < len(query_nucleo) and (matchGL is True):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][0] == 'G':
                                    if query_nucleo[index][0] == 'G':
                                        matchGL = True
                                    elif ((query_nucleo[index][0]) ==
                                          (memory_nucleoG)):
                                        matchGL = True
                                    else:
                                        matchGL = False
                            index = index + 1
                        # Now check for the right index
                        index = 0
                        matchGR = True
                        while index < len(query_nucleo) and (matchGR is True):
                            if ((query_nucleo[index] != '') and
                                    (person_nucleo[index] != '')):
                                if person_nucleo[index][1] == 'G':
                                    if query_nucleo[index][1] == 'G':
                                        matchGR = True
                                    elif ((query_nucleo[index][1]) ==
                                          (memory_nucleoG)):
                                        matchGR = True
                                    else:
                                        matchGR = False
                            index = index + 1
                        # Now check if EVERY match is True
                        result = ((matchAL) and (matchAR) and (matchTL) and
                                  (matchTR) and (matchCL) and (matchCR) and
                                  (matchGL) and (matchGR))
                    # set the result to whatever the reult was until the
                    # index error AND True. This way if the query was False
                    # before the indexerror the query will be rejected.
                    # But if the query was True until the index error, it
                    # not be rejected
                    except IndexError:
                        result = result and True
                    # Create an exception for when the query is defined at the
                    # 23 chromosome (22 index) but not defined in the male
                    # You this will work because this will get run if there is
                    # error where the nucleotide list of the query is > than
                    # thatof the person
                    finally:
                        if (index_chromo is 22) and (type(self) is Male):
                            result = result and False
                # You do not want an infinit loop
                index_chromo = index_chromo + 1
        # set the result to whatever the reult was until the
        # index error AND True. This way if the query was False
        # before the indexerror the query will be rejected.
        # But if the query was True until the index error, it
        # not be rejected
        except IndexError:
            result = result and True
        # return th efinal result
        return result


class Female(Human):
    '''This class represents a male human being
    '''
    def __init__(self, client_ID):
        '''(Female, str) -> NoneType
        this mathod creates a Male Class given a client ID
        '''
        self._client_ID = client_ID
        # Create a to hold the person's chromosomes
        self._chromosome_list = list()
        # Create a dictionary that will contain all of the Human's markers
        # that will be created in the future
        self._marker_dict = {}

    def __str__(self):
        '''(Female) -> str
        This Method prints out a statment to say what the class represents
        '''
        return 'I am a Female with ' + str(self._client_ID)


# Create a class for Male and make it inherit all the methods assesible to a
# Human
class Male(Human):
    '''This class represents a male human being
    '''
    def __init__(self, client_ID):
        '''(Male, str) -> NoneType
        this mathod creates a Male Class given a client ID
        '''
        self._client_ID = client_ID
        # Create a to hold the person's chromosomes
        self._chromosome_list = list()
        # Create a dictionary that will contain all of the Human's markers
        # that will be created in the future
        self._marker_dict = {}

    def __str__(self):
        '''(Male) -> str
        This Method prints out a statment to say what the class represents
        '''
        return 'I am a Male with ' + str(self._client_ID)

    # Only females can use the procreate method so create a method that raises
    # an exception when it is implimented
    def procreate(self, binder, female):
        '''(Male, Binder, Female) -> Exception
        This method returns an exception when it is called
        '''
        raise ProcreateError('Only a Female can use the procreate method')


# Create a class for Query it will inherit all the methods a Female can
class Query(Human):
    '''This class represents a Query
    '''
    def __init__(self):
        '''This method creates a query. It inherits all the methods that a
        female has
        '''
        # Create a dictionary to hold the Query's chromosomes
        self._chromosome_list = list()
        # create a dictrionary to hold the person's markers
        self._marker_dict = {}

    def __str__(self):
        '''(Query) -> str
        This Method prints out a statment to say what the class represents
        '''
        return 'Query is used to test certain nucleotides in a persons gene'


# create a binder class for procreation
class Binder(Human):
    '''This class represents a binder that can be used to procreation
    '''
    # Create a method that creates an instances variable of the binder class
    def __init__(self):
        '''(Binder) -> NoneType
        This method creates an instances variable of the binder class
        '''
        # Create a variable for the sex of the binder so that it can retrieved
        # later on
        self._sex = 'L'
        # Create a list for all the binder chromosomes
        self._chromosome_list = []
        # Create a dictionary that will contain all of the Human's markers
        # that will be created in the future
        self._marker_dict = {}

    def __str__(self):
        '''(Binder) -> str
        This Method prints out a statment to say what the class represents
        '''
        return 'This class is used to reproduce with a Male and Female'

    def set_sex(self, sex):
        '''(Binder, str) -> Nonetype
        This method assigns a sex to a bunder when a mothe and a father
        procreate
        REQ: sex must be a string
        '''
        self._sex = sex

    def get_sex(self):
        '''(Binder) -> str
        This method returns the sex attached to this binder
        '''
        return self._sex


class ManyNucleoError(Exception):
    '''This exception is raised when
    the user tries to assign more than 2
    letters to a postion
    '''


class InvalidPairError(Exception):
    '''This Exception is raised when a user tries assign or get a pair < 0
    or if pair > 22
    '''


class InvalidPosError(Exception):
    '''This Exception is raised if a user tries to get or set an pair < 0
    '''


class InvalidMarkerError(Exception):
    '''This error is raised when a user tries to use an invalid marker
    that has not been set
    '''


class NoPairError(Exception):
    '''This error is raised when a user tries to get a pair that is not defined
    in the genome
    '''


class NoPosError(Exception):
    '''this Error is raised when a user tries to get a postion that is not
    defined
    '''


class NoBinderError(Exception):
    '''This Exception is raised if a user tries to use an invalid binder
    '''


class ProcreateError(Exception):
    '''This Exception is raised if a user tries to procreate with two female
    classes
    '''
