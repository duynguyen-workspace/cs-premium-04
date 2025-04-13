import pygame, sys, random, heapq
from pygame.locals import *
import json

with open('data.json', 'r') as file:
    data = json.load(file)
    
#* GRAPH
class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, key):
        if key not in self.graph:
            self.graph[key] = {"nei": {}}
        
    def add_edge(self, key, dest, weight):
        self.graph[key]["nei"][dest] = weight
        
    def load_data(self, data):
        for node in data:
            key = node["key"]
            
            self.add_vertex(key)
            
            for nei in node["nei"]:
                for dest, weight in nei.items():
                    self.add_edge(key, int(dest), weight)
                    
    def dijskra(self, start, end):
        distances = {vertex: float("infinity") for vertex in self.graph}
        previous = {vertex: None for vertex in self.graph}
        
        distances[start] = 0
        
        heap = [(0, start)]
        
        while heap:
            current_distance, current_vertex = heapq.heappop(heap)
            
            if current_vertex == end:
                break
            
            for neighbor, weight in self.graph[current_vertex]["nei"].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(heap, (distance, neighbor))
        
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        
        return path
                    
    def print_graph(self):
        for node, info in self.graph.items():
            print(f"Node: {node}: {info['nei']}")

graph = Graph()
graph.load_data(data)

# graph.print_graph()
# print(graph.dijskra(1, 12))
        
WINDOW_WIDTH = 1720
WINDOW_HEIGHT = 980

pygame.init()

pygame.display.set_caption("Google Map")
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set font size
font = pygame.font.Font(None, 24)

def check_key(key, data):
    for item in data:
        if item['key'] == key:
            return item
        
    return None

def main():
    selected_locations = []
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                mouse_pos = event.pos
                
                if len(selected_locations) >= 2:
                    selected_locations = []
                
                for item in data:
                    location = pygame.Surface((30, 30))
                    location_pos = (item['X'], item['Y'])
                    
                    rect = location.get_rect(topleft=location_pos)
                    if rect.collidepoint(mouse_pos) and item not in selected_locations:
                        selected_locations.append(item)
                    
        
        # LOAD MAP
        bg_img = pygame.image.load("./img/map.png")
        bg_img = pygame.transform.scale(bg_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        DISPLAY_SURFACE.blit(bg_img, (0,0))
        
        # Nếu chọn được 2 điểm
        if len(selected_locations) >= 2:
            key_start = selected_locations[0]
            key_end = selected_locations[1]
            
            paths = graph.dijskra(key_start["key"], key_end["key"])
            
            # print(paths)
            
            for index, key in enumerate(paths, start=0):
                if index + 1 < len(paths):
                    current_key = check_key(key, data)
                    next_key = check_key(paths[index+1], data)
                    # Vẽ đường
                    pygame.draw.line(DISPLAY_SURFACE, (0, 255, 0), (current_key['X'] + 15, current_key['Y'] + 15), (next_key['X'] + 15, next_key['Y'] + 15), 10)
        
        # load key to map
        for item in data:
            location = pygame.Surface((30, 30))
            text_surface = font.render(str(item['key']), True, (0, 0, 0))
            
            # Tô màu khung nếu được click
            if check_key(item['key'], selected_locations):
                location.fill((255, 255, 0))
            else:
                location.fill((255, 0, 0))
                
            location.blit(text_surface, (10, 10))
            location_pos = (item['X'], item['Y'])
            DISPLAY_SURFACE.blit(location, location_pos)
            
        pygame.display.update()
        pygame.time.Clock().tick(60)

    
main()