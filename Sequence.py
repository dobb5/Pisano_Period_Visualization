class Sequence:
   
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
                        result.extend(Sequence.newfunc(period[0:j] + period[i:]))
                        return result
                    result.append(period[j:i+1])
                    result.extend(Sequence.newfunc(period[0:j] + period[i:]))
                    return result

        return result
    
Sequence.newfunc([0,1,1,2,3,5])