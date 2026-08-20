class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = set()
        preToReq = {} # maps the prereq to the requisite list
        reqToPre = {} # maps the requisite to the prereq list
        for i in range(numCourses):
            preReqs.add(i)
        
        for pair in prerequisites:
            req, preReq = pair
            if(preReq == req):
                return False
            if(req in preReqs):
                preReqs.remove(req)
            if(req in reqToPre):
                reqToPre[req].append(preReq)
            else:
                reqToPre[req] = [preReq]
            if(preReq in preToReq):
                preToReq[preReq].append(req)
            else:
                preToReq[preReq] = [req]
        
        while(len(preReqs) > 0):
            toRes = next(iter(preReqs))
            preReqs.remove(toRes)
            if(toRes in preToReq):
                toRemove = preToReq[toRes]
                for elem in toRemove:
                    if(elem in reqToPre):
                        reqToPre[elem].remove(toRes)
                        if(len(reqToPre[elem]) == 0):
                            preReqs.add(elem)
                            reqToPre.pop(elem)
                    else:
                        preReqs.add(elem)
                preToReq.pop(toRes)
        
        if(len(reqToPre) > 0):
            return False
        return True
            



