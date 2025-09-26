class BrowserHistory:
    """
    Manages a simple browser history using a list to store the visited URLs
    and an index to track the current position.
    """
    def __init__(self):
        # Stores the history of visited URLs
        self.history = ["home"]
        # Index of the current page in the history list
        self.current_index = 0

    def current(self) -> str:
        """
        Returns the URL of the current page.
        """
        return self.history[self.current_index]

    def visit(self, url: str):
        """
        Visits a new URL. This clears any pages that were in the "forward" history.
        """
        # Slicing clears forward history if current_index is not at the end
        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]

        # Add the new URL and update the index
        self.history.append(url)
        self.current_index = len(self.history) - 1

    def back(self) -> str:
        """
        Goes back to the previous page. Raises IndexError if at the start of history.
        """
        if self.current_index == 0:
            raise IndexError("Cannot go back, already at the start of history.")

        self.current_index -= 1
        return self.history[self.current_index]

    def forward(self) -> str:
        """
        Goes forward to the next page. Raises IndexError if at the end of history.
        """
        if self.current_index == len(self.history) - 1:
            raise IndexError("Cannot go forward, no forward history exists.")

        self.current_index += 1
        return self.history[self.current_index]