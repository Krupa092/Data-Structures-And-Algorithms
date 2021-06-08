import math 
import heapq as hpq
from helper import load_map, show_map 

Map_10 = load_map('map-10.pickle')
Map_40 = load_map('map-40.pickle')

def shortest_path(M,start,goal):
    
    closed_route_set = set()
    open_route_set = set()
    available_path_route = list(M.intersections.keys())
    previous_path = {}
    path_cost =  {road : float("inf") for road in available_path_route}
    path_cost[start] = 0
    cost_distance = {road: float("inf") for road in available_path_route}
    cost_distance[start] = heuristic(M,start,goal)
    outer = (cost_distance[start], strat)
    
    while open_route_set:
        route_present =  hpq.heappop(outer)
        
        if route_present[1] == goal:
            print("shortest path called")
            make_pre_paths = reconstruct_path(previous_path, route_path[1])
            make_pre_path.reverse()
            print(make_pre_path)
            return make_pre_path
        if route_present in open_route_set:
            open_route_set.remove(route_present[1])
            closed_route_set.add(route_present[1])
        for i in M.roads[route_present[1]]:
            if i in close_route_set:
                continue 
            if i not in open_route_set:
                open_route_set.add(i)
                
            t_path_cost = path_cost[route_present[1]] + heuristic(M, route_present[1], i)
            if t_path_cost >= path_cost[i]:
                continue
            
            previous_path[i] = previous_path[1]
            path_cost[i] = t_path_cost
            cost_distance[i] = (path_cost[i] + heuristic(M, i, goal))
            h.heappush(outer, (cost_distance[i], i))
    return ("The function isn't worked")
def heuristic(M,start,goal):
     return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))
def generate_route(previous, start, goal):
    path = [goal]
    while goal != start:
        goal = previous[goal]
        path.append(goal)
    path.reverse()
    return path

            