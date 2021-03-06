# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

class Node(object):
    """Basic representation of a node on a map/tree.
       """
    def __init__(self, value, parent=None):
        """Value is exepected to be a triple with the following parts:
            1. Coordinate tupel (x,y)
            2. Direction string (e.g. "west)
            3. Path cost as an integer (e.g. 1)
        Parent is a coordinate.
           """
        self.coordinate = value[0]
        self.direction = value[1]
        self.cost = value[2]
        self.parent = parent

def depthFirstSearch(problem):
    """A hackish DFS algorithm specific to solving single-destination problems.
       """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    starting_position = problem.getStartState()
    current_node = Node((starting_position, "", 0)) 
    
    all_nodes = [starting_position]    # List of coordinates
    fringe_nodes = []                  # List of nodes (we need to know its' parent)
    current_path = [current_node]      # List of coordinates 
    solution = []                      # List of directions from game module

    while not problem.isGoalState(current_node.coordinate):
        for successor in problem.getSuccessors(current_node.coordinate):
            # Prevent loops by only adding new nodes
            if successor[0] not in all_nodes:
                all_nodes.append(successor[0])
                fringe_nodes.append(Node(successor, current_node.coordinate))

        next_node = fringe_nodes.pop()

        # if the next fringe node is not a child of the last node in our path...
        if not next_node.parent == current_path[-1].coordinate:
            # Pop nodes off our current path until it has the next_node as a child 
            while next_node.parent != current_path[-1].coordinate:
                current_path.pop()  

        # Add it to our path and continue descending the tree.
        current_path.append(next_node) 
        current_node = next_node

    if not problem.isGoalState(current_node.coordinate):
        print "Failed to find a path to the goal state..."
    else:
        # Take our curren_path and turn it into a list of directions 
        last_coordinate = starting_position
        for node in current_path:
            if node.coordinate != starting_position:
                direction = node.direction
                if   direction == "West":
                    solution.append(w)
                elif direction == "South":
                    solution.append(s)
                elif direction == "North":
                    solution.append(n)
                elif direction == "East":
                    solution.append(e)
    return solution   
        
def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
