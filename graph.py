from lib2to3.pgen2.token import MINEQUAL
import sys
from heapq import heapify,heappop,heappush
class graph:
    def d(graph,src,dest):
        inf=sys.maxsize
        vertices={
            "C":{"weight":inf,"source":[]},
            "CR":{"weight":inf,"source":[]},
            "MU":{"weight":inf,"source":[]},
            "M":{"weight":inf,"source":[]},
            "D":{"weight":inf,"source":[]},
            "KR":{"weight":inf,"source":[]},
            "VP":{"weight":inf,"source":[]},
            "A":{"weight":inf,"source":[]},
            "B":{"weight":inf,"source":[]},
            "K":{"weight":inf,"source":[]},
            "MAL":{"weight":inf,"source":[]}
        }
        vertices[src]["weight"]=0
        visited = []
        temp = src
        for u in range(10):
            if temp not in visited:
                visited.append(temp)
                min_q=[]
                for j in graph[temp]:
                    if j not in visited:
                        weight = vertices[temp]["weight"] + graph[temp][j] 
                        if weight < vertices[j]["weight"]:
                            vertices[j]["weight"] = weight
                            vertices[j]["source"]=vertices[temp]["source"] + list(temp)
                        heappush(min_q,([vertices[j]["weight"],j]))
                heapify(min_q)
                temp = min_q[0][1]
        print("SHORTEST DISTANCE IS : " + str(vertices[dest]["weight"]))
        print("SHORTEST PATH IS : " + str(vertices[dest]["source"] + list(dest)))

                        
    if __name__=="__main__":
        graph={
            "C":{"CR":1,},
            "CR":{"C":1,"MU":1},
            "MU":{"CR":1,"M":1},
            "M":{"MU":1,"D":1},
            "D":{"M":1,"KR":1},
            "KR":{"D":1,"VP":1},
            "VP":{"KR":1,"A":1},
            "A":{"VP":1,"B":1},
            "B":{"A":1,"K":1},
            "K":{"B":1,"MAL":1},
            "MAL":{"K":1}
        }
        starting_point = "C"
        dest = str(input(" enter C for churchgate\n enter CR for charni road \n enter MU for Mumbai central\n enter M for mahim\n enter D for Dadar\n enter KR for Khar Road\n enter VP for Vile Parle\n enter A for Andheri\n enter B for Borivali\n enter K for Kandivali\n enter MAL for Malad\n"))
        a = d(graph,starting_point,dest)
        print ("done")


        #I058 == SHREY SHAH
        #I063 == HISHAM SOPARIWALA
        #I065 == SHUBHAM THAKKAR
