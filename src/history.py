# src/history.py

class BrowserHistory:
    """
    Simulates a simplified web browser's history functionality,
    allowing visits to new pages, and navigating back and forward.
    """
    def __init__(self):
        # List to store the history of visited URLs. Starts with "home".
        self._history = ["home"]
        # Index of the current page in the _history list.
        self._current_index = 0

    def visit(self, url: str) -> None:
        """
        Navigates to a new URL. This action clears any 'forward' history.
        """
        # If we weren't at the end of the history (i.e., we used back()),
        # visiting a new page clears the future history.
        if self._current_index < len(self._history) - 1:
            # Truncate the history list from the current index + 1 onwards
            self._history = self._history[:self._current_index + 1]
        
        # Add the new URL to the history
        self._history.append(url)
        # Update the current index to the new last position
        self._current_index = len(self._history) - 1

    def back(self) -> str:
        """
        Goes back one page in the history.
        
        Raises:
            IndexError: If there are no pages to go back to (i.e., already at the start).
        
        Returns:
            str: The URL of the page after moving back.
        """
        if self._current_index == 0:
            raise IndexError("Cannot go back: Already at the beginning of history.")
        
        # Move the index back one position
        self._current_index -= 1
        # Return the URL at the new index
        return self._history[self._current_index]

    def forward(self) -> str:
        """
        Goes forward one page in the history.
        
        Raises:
            IndexError: If there are no pages to go forward to (i.e., at the end of history).
        
        Returns:
            str: The URL of the page after moving forward.
        """
        if self._current_index == len(self._history) - 1:
            raise IndexError("Cannot go forward: Already at the end of history.")
        
        # Move the index forward one position
        self._current_index += 1
        # Return the URL at the new index
        return self._history[self._current_index]

    def current(self) -> str:
        """
        Returns the URL of the current page.
        """
        return self._history[self._current_index]
