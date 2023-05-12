class Series:
   
    def newfunc(period):
        if period is None:
            return None
        if len(period) == 2:
            return period

        result = []
        for i, x in enumerate(period):
            for j, y in enumerate(period[0:i]):
                if x == y:
                    if i - j == 1:
                        result.append([j, j])
                        result.extend(Series.newfunc(period[0:j] + period[i:]))
                        return result
                    result.append(period[j:i+1])
                    result.extend(Series.newfunc(period[0:j] + period[i:]))
                    return result

        return result
    
class Pisano:    
    def pisano_period(modulo):
        """
        Returns the Pisano period for a given modulo.
        """
        pisano = [0, 1]
        while True:
            next_num = (pisano[-1] + pisano[-2]) % modulo
            if next_num == 1 and pisano[-1] == 0:
                return pisano
            pisano.append(next_num)