class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create a map to store prerequisites for all courses
        preMap = {i: [] for i in range(numCourses)}

        # Populate the map
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        # Create a set of all visited nodes
        visit = set()

        def dfs(course):
            # Cycle has been detected, impossible to take all courses
            if course in visit:
                return False
            
            # End of prerequisites reached, valid path
            if preMap[course] == []:
                return True
            
            # Add the current course to visited nodes
            visit.add(course)

            # Recurse on every prerequisite
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            # Remove the node so it can be used by future iterations
            visit.remove(course)

            # Clear the course since we've already confirmed it's good
            preMap[course] = []

            # Return true for current path
            return True
        
        # Check each course path
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True