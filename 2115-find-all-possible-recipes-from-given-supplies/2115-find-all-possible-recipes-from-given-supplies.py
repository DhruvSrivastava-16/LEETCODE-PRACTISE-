class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Create a graph and an indegree to hold your adjacency and counts, respectively.
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        
        # Cycle through each recipe, grab the related ingredients, and add the edges to the graph.
        # Also increase the indegree for that recipe for each ingredient.
        for index, recipe in enumerate(recipes):
            for ingredient in ingredients[index]:
                graph[ingredient].append(recipe)
                indegree[recipe] += 1
        
        # Supplies are the starting point (i.e. they would have an indegree == 0)
        queue = deque(supplies)
        
        while queue:
            # Remove the first ingredient and cycle through the related mapping which holds the list of edges this ingredient connects to.
            current_ingredient = queue.popleft()
            for ne in graph[current_ingredient]:
                # Remove the ingredient from the recipe mapping, and update the indegree. 
                # If the indegree is zero you can add it to the queue.
                recipe = ne
                # This is a safety check for ingredients from our supply that are never used in any of the recipes.
                # Though, a defaultdict would handle this, and our return list comprehension would only find elements with a parity of 0.
                if recipe in indegree: 
                    indegree[recipe] -= 1
                
                if indegree[recipe] == 0:
                    queue.append(recipe)
        # When the queue is exhausted, we return a list of all recipes with an indegree of 0
        return [key for key in indegree if indegree[key] == 0]
                