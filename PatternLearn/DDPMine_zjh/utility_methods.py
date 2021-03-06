from math import log
class UtilityMethods:
    @staticmethod
    def InformationGain(patternSupport,labelSupport,patternLabelUnionSupport):
        if patternSupport == 0 or labelSupport == 0 :
            return 0
        else :
            print("lpsup:",patternLabelUnionSupport)
            return UtilityMethods.__InformationGainFormula(patternSupport,labelSupport,patternLabelUnionSupport/patternSupport)

    @staticmethod
    def InformationGainUpperBound(potentialSupport,labelSupport):
        upperBound = 0

        if labelSupport >= potentialSupport:
            upperBound = UtilityMethods.__InformationGainFormula(potentialSupport,labelSupport,1)
        else:
            upperBound = UtilityMethods.__InformationGainFormula(potentialSupport,labelSupport,labelSupport/potentialSupport)

        return upperBound

    @staticmethod
    def __InformationGainFormula(o,p,q):
        #print "o,p,q"
        #print o
        #print p
        #print q
        print("o:",o," p :",p," q:",q) 
        if o==0 :
            return 0

        conditionalProb_term1 = -o*q*(UtilityMethods.__Log2(q))-o*(1-q)*(UtilityMethods.__Log2(1-q))
        conditionalProb_term2 = (o*q-p)*(UtilityMethods.__Log2_wDivision((p-o*q),(1-o)))
        conditionalProb_term3 = (o*(1-q)-(1-p))*(UtilityMethods.__Log2_wDivision(((1-p)-(o*(1-q))),(1-o)))
        print("c1:",conditionalProb_term1," c2:",conditionalProb_term2," c3:",conditionalProb_term3)
        conditionalProb = conditionalProb_term1 + conditionalProb_term2 + conditionalProb_term3
        print("cp:",conditionalProb)
        #use binary entropy formula to calculate entropy of the pattern
        #see http://en.wikipedia.org/wiki/Binary_entropy_function
        nonCondProb = -p*(UtilityMethods.__Log2(p))-(1-p)*(UtilityMethods.__Log2(1-p))
        print("np:",nonCondProb)

        #calculate and return information gain
        return (nonCondProb - conditionalProb)

    @staticmethod
    def __Log2(x):
        ans = 0
        try:
            if x != 0:
                ans = log(x,2)
        except ValueError:
            pass
        return ans

    @staticmethod
    def __Log2_wDivision(x,y):
        ans = 0
        try:
            if x != 0 and y != 0 and (x/y) != 0:
                ans = log(x/y,2)
        except ValueError:
            pass
        return ans

