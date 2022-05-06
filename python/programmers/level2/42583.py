"""
def solution(bridge_length, weight, truck_weights):
    seconds = 0
    truck_on_bridge = [0] * bridge_length
    while truck_weights:
        seconds += 1
        truck_on_bridge.pop(0)
        if sum(truck_on_bridge) + truck_weights[0] <= weight:
            truck_on_bridge.append(truck_weights.pop(0))
        else:
            truck_on_bridge.append(0)

    return seconds + len(truck_on_bridge)
"""
# 무게를 연산해주는게 sum보다 빠르다.
def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    current_weight = 0
    seconds = 0
    while truck_weights:
        current_weight -= bridge.pop(0)
        seconds += 1
        if current_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            current_weight += truck
            bridge.append(truck)
        else:
            bridge.append(0)

    return seconds + len(bridge)
