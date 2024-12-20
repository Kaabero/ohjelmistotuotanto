class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
        

    def test(self, player):
        count=0
        for matcher in self._matchers:
            if matcher.test(player):
                count+=1

        if count>0:
            return True
        return False


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
    
class Not:
    def __init__(self, condition):
        self._condition = condition

    def test(self, player):
        return not self._condition.test(player)
            
 
class All:
   
    def test(self, player):

        return True



class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher = matcher

    def plays_in(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def one_of(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def not_(self, condition):
        return QueryBuilder(And(self._matcher, Not(condition)))

    def build(self):
        return self._matcher




