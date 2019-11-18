from maze_solving_challenge import maze_result

maze1 = 'XOXXXX XOXOOX XOXOXX XOOOSX XXXXXX'
maze2 = 'XOOOOOX XOXXXOO XSXOOXX XOXXXXX'
maze3 = 'XXXOX XOOOX XOXXX XOOSX XXXXX'
maze4 = 'XXXOX XOOOO XOXXX XOOSX XXXXX'
maze5 = 'XXXXXOX XSOOOOO XXOXXXX XXOOXXX XXXOXXX'
maze6 = 'XXXXX XOOSX XXXXX'
maze7 = 'XXXXXX XOOOOX XOXOXX XSXOXX XXXOXX XXXXXX'

# 
# ## Unit Tests

results_all_paths = {maze1: [[(3, 4), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), 'Freedom!']],
                     maze2 : [[(2, 1), (3, 1), 'Freedom!'], 
                              [(2, 1), (1, 1), (0, 1), 'Freedom!'], 
                              [(2, 1), (1, 1), (0, 1), (0, 2), 'Freedom!'], 
                              [(2, 1), (1, 1), (0, 1), (0, 2), (0, 3), 'Freedom!'], 
                              [(2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (0, 4), 'Freedom!'], 
                              [(2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), 'Freedom!'], 
                              [(2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (1, 6), 'Freedom!']],
                    maze3: [[(3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (0, 3), 'Freedom!']],
                    maze4: [[(3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), 'Freedom!'], 
                            [(3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (0, 3), 'Freedom!']], 
                    maze5: [[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), 'Freedom!'], 
                            [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (0, 5), 'Freedom!'], 
                            [(1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), 'Freedom!']]} 

results_shortest_paths = {maze1: [[(3, 4), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), 'Freedom!']],
                          maze2: [[(2, 1), (3, 1), 'Freedom!']],
                          maze3: [[(3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (0, 3), 'Freedom!']],
                          maze4: [[(3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), 'Freedom!'], 
                                  [(3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (0, 3), 'Freedom!']],
                          maze5: [[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), 'Freedom!'], 
                                  [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (0, 5), 'Freedom!'], 
                                  [(1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), 'Freedom!']]}

results_no_paths = {maze6: "Unfortunately, no way out from the maze!",
                    maze7: "Unfortunately, no way out from the maze!"}

import unittest
from io import StringIO
from unittest import mock

class mazeTest(unittest.TestCase):
    def test_maze_all_paths(self):
        for keys, values in results_all_paths.items():
            path = maze_result(keys, False)
            self.assertEqual(path, values)

    def test_maze_shortest_path(self):
        for keys, values in results_shortest_paths.items():
            path = maze_result(keys, True)
            self.assertEqual(path, values)

    def test_no_paths(self):
        for keys, values in results_no_paths.items():
            path = maze_result(keys, False)
            self.assertEqual(path, values)

if __name__ == '__main__':
    unittest.main()


# ## Test Mazes
# 
# You can directly copy and paste the mazes provided below to test the algorithm.
# 
# **Maze 1**
# <br>XOXXXX 
# <br>XOXOOX 
# <br>XOXOXX 
# <br>XOOOSX 
# <br>XXXXXX
# 
# **Maze 2** 
# <br>XOOOOOX 
# <br>XOXXXOO 
# <br>XSXOOXX 
# <br>XOXXXXX
# 
# **Maze 3**
# <br>XXXOX 
# <br>XOOOX 
# <br>XOXXX 
# <br>XOOSX 
# <br>XXXXX
# 
# **Maze 4**
# <br>XXXOX 
# <br>XOOOO 
# <br>XOXXX 
# <br>XOOSX 
# <br>XXXXX
# 
# **Maze 5**
# <br>XXXXXOX 
# <br>XSOOOOO 
# <br>XXOXXXX 
# <br>XXOOXXX 
# <br>XXXOXXX
# 
# **Maze 6**
# <br>XXXXX 
# <br>XOOSX 
# <br>XXXXX 
# 
# **Maze 7**
# <br>XXXXXX 
# <br>XOOOOX 
# <br>XOXOXX 
# <br>XSXOXX 
# <br>XXXOXX 
# <br>XXXXXX