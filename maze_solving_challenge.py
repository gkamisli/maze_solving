import numpy as np
import time

class Maze:
    '''
    Objects of this class perform maze creation given by user and find shortest path or all paths
    depending on the choice of the user.  
    '''
    def __init__(self, maze_in_string):
        '''
        Instance for the Maze objects.
        Arguments:
        maze_in_string -- Input provided by the user, format of, XXXX XXXX XXXX
        
        Created parameters:
        maze -- Maze itself to keep track of, numpy array, shape of (maze_rows, maze_columns) 
        maze_rows -- Number of maze rows, number
        maze_columns -- Number of maze columns, number
        
        starting_point -- 2D coordinate of the starting point, tuple
        x -- Coordinate of x-axis for the current point, number
        y -- Coordinate of y-axis for the current point, number
        neighbors -- Coordinates of neighbors that are available to move, list
        
        '''
        rows = maze_in_string.split(" ")
        maze = np.array([list(row) for row in rows])
        self.maze = maze
        self.maze_rows = len(maze)
        self.maze_columns = len(maze[0])

        starting_point = np.where(self.maze == 'S')
        x, y = starting_point[0][0], starting_point[1][0]
        self.starting_point = (x, y)
        self.x = x
        self.y = y
        self.neighbors = []
        
    def _set_coordinate(self, x, y):
        '''
        This void method sets a new coordinate for the Maze object.
        
        Arguments:
        x -- Coordinate of x-axis to set for the current point, number
        y -- Coordinate of y-axis to set for the current point, number
        '''
        self.x = x
        self.y = y
    
    def _end_check(self):
        '''
        This boolean method checks if an ending exists on right, left, up, or down at the current point
        
        Returns:
        True -- if found an exit from the maze
        False -- otherwise
        '''
        
        if self.x-1 < 0 or self.x+1 == self.maze_rows or self.y-1< 0 or self.y+1 == self.maze_columns:
            return True
        else:
            return False
    
    def _backtrace(self, parent, start, end):
        '''
        This method returns the path for given starting and ending points 
        
        Arguments:
        parent -- Dictionary to store parents (previous point) of each point
        start -- Coordinates of the starting point, tuple
        end -- Coordinates of the ending point, tuple
        
        Returns:
        path -- Corresponding path between start and end points, list
        '''
        path = ["Freedom!", end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path
    
    def _find_neighbors(self):
        '''
        This void method finds possible coordinates to move and expands neighbors parameters within the 
        Maze object.
        
        Remark: first if conditions are to check if we are at the edge of the maze
        '''
        
        # Right neighbor search
        if (self.y+1 != self.maze_columns):
            if self.maze[self.x][self.y+1] == 'O' and (self.x, self.y+1) not in self.neighbors:
                self.neighbors.append((self.x, self.y+1))

        # Left neighbor search
        if self.y-1 >= 0:
            if self.maze[self.x][self.y-1] == 'O' and (self.x, self.y-1) not in self.neighbors:
                self.neighbors.append((self.x, self.y-1))

        # Up neighbor search
        if (self.x-1 >= 0):
            if self.maze[self.x-1][self.y] == 'O' and (self.x-1, self.y) not in self.neighbors:
                self.neighbors.append((self.x-1, self.y))


       # Down neighbor search
        if (self.x+1 != self.maze_rows):
            if self.maze[self.x+1][self.y] == 'O' and (self.x+1, self.y) not in self.neighbors:
                self.neighbors.append((self.x+1, self.y))
            
        return self.neighbors
    
    def _shortest_path(self, all_paths): 
        '''
        This method is to return the shortest among all paths found
        
        Arguments:
        all_paths -- List of paths that are available from the start point, list
        '''
        path_lengths = np.array([len(path) for path in all_paths])
        return np.where(path_lengths == min(path_lengths))[0] 
            
    
    def BFS(self, SHORTEST_PATH):
        '''
        This method applies Bread-First Search algorithm for a given maze
        
        Arguments:
        SHORTEST_PATH -- boolean to return the shortest path or all paths
        
        Return:
        SHORTEST_PATH = TRUE --returns only the shortest path
        SHORTEST_PATH = FALSE -- returns all possible paths
        '''
        
        all_paths = []
        visited = set() 
        queue = []
        parent = {}
        
        queue.append((self.x, self.y))
        visited.add((self.x, self.y))
        #starting_point = ((self.x, self.y))
        
        while queue:
            coordinates = queue.pop(0)
            self._set_coordinate(coordinates[0], coordinates[1])
            
            if self._end_check(): 
                path = self._backtrace(parent, self.starting_point, (self.x, self.y))
                if path not in all_paths:
                    all_paths.append(path)
                        
            for i in self._find_neighbors(): 
                if (i[0], i[1]) not in visited:
                    parent[i[0], i[1]] = coordinates
                    queue.append((i[0], i[1]))
                    visited.add((i[0], i[1]))
                    self._set_coordinate(i[0], i[1])
                    
            self.neighbors = []
           
        if all_paths == []:
            return ("Unfortunately, no way out from the maze!")
        else:
            if SHORTEST_PATH:
                return np.array(all_paths)[self._shortest_path(all_paths)].tolist()
            else:
                return all_paths

def maze_result(M, SHORTEST_PATH):
    new_challenge = Maze(M)
    if SHORTEST_PATH:
        paths = new_challenge.BFS(SHORTEST_PATH = True)
    else:
        paths = new_challenge.BFS(SHORTEST_PATH = False)
    return(paths)
