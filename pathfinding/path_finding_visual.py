import pygame

# Colors for pygame visualization
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (255, 255, 153)
RED = (255, 0, 0)
BLUE = (102, 178, 255)
GREY = (211, 211, 211)


# Maze grid is a global parameter, edited by any function
grid_len = 20
maze = [[0 for i in range(grid_len)] for i in range(grid_len)]

start = (1, 2)
end = (19, 17)

node_set = []
class Node():
    """ node class for A* pathfinding algorithm """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # g is dist between current node and start node
        self.g = 0
        # h is the heuristic (estimated distance from the current node to end node)
        self.h = 0
        # f is the total cost of the node
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f



""" pygame function """
def pygame_visualization():
    pygame.init()

    size = (700, 700)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Pathfinding Visualization")

    screen.fill(GREY)
    margin = 1
    box_len = (size[0] - (len(maze[0])+1)*margin) / len(maze[0])  # Resize boxes depending on screen size

    # Loop until user clicks the close button
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    while not done:
        # --- Game logic should go here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y coordinates to grid/maze coordinates
                column = int(pos[0] // (box_len + margin))
                row = int(pos[1] // (box_len + margin))
                # Set maze paramter to 1, to indicate grey color in grid
                maze[row][column] = 1
                #print ("Click ", pos, "Grid Coords", column, row)
                # Calculate path and map to maze grid
                path = astar()
                #print(path)
                #printmaze()
                for i, j in path:
                    maze[i][j] = 2
                

        


        # --- Screen-clearing code goes here

        # --- Drawing code should go here


        for i in range(len(maze)):
            for j in range(len(maze[1])):
                if (j, i) == start or (j, i) == end:
                    pygame.draw.rect(screen, BLUE, [
                        box_len*i + (i+1)*margin, box_len*j + (j+1)*margin, box_len, box_len], 0)
                elif maze[j][i] == 0:
                    pygame.draw.rect(screen, WHITE, [
                                    box_len*i + (i+1)*margin, box_len*j + (j+1)*margin, box_len, box_len], 0)
                elif maze[j][i] == 1:
                    pygame.draw.rect(screen, GREY, [
                                     box_len*i + (i+1)*margin, box_len*j + (j+1)*margin, box_len, box_len], 0)
                elif maze[j][i] == 2:
                    pygame.draw.rect(screen, GREEN, [
                                     box_len*i + (i+1)*margin, box_len*j + (j+1)*margin, box_len, box_len], 0)


                
        # --- Go ahead and update the screen with what we've drawn
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit
    pygame.quit()








""" A* pathfinding algorithm """

def astar():
    """ Returns list of tuples as a path from the given start to the given end in the maze """

    for i in range(len(maze)):
        for j in range(len(maze[1])):
            if maze[i][j] == 2:
                maze[i][j] = 0

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.h = end_node.h = end_node.f = 0

    # Initialize both open and closed sets
    open_list = []
    closed_list = []

    # Add start node to open list
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
                path = path[::-1]
            return path  # Return reversed path


        # Generate children
        children = []
        # Loop through adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append to children
            children.append(new_node)

        for child in children:

            # Child is in closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create f, g and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0])**2) + ((child.position[1] - end_node.position[1])**2)
            child.f = child.g + child.h

            if child in open_list:
                continue

            # Add the child to the open list
            open_list.append(child)


def printmaze():
    
    print(*maze, sep='\n')



def main():
    pygame_visualization()

if __name__ == '__main__':
    main()
