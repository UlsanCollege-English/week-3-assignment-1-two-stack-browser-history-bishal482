class BrowserHistory:
    def __init__(self, start="home"):
        self._cur = start
        self._back = []   # stack of pages before current
        self._fwd = []    # stack of pages after current

    def visit(self, url: str) -> None:
        # push current into back stack
        self._back.append(self._cur)
        # set new current
        self._cur = url
        # clear forward stack
        self._fwd.clear()

    def back(self) -> str:
        if not self._back:
            raise IndexError("No pages in back history")
        # push current into forward stack
        self._fwd.append(self._cur)
        # pop from back to current
        self._cur = self._back.pop()
        return self._cur

    def forward(self) -> str:
        if not self._fwd:
            raise IndexError("No pages in forward history")
        # push current into back stack
        self._back.append(self._cur)
        # pop from forward to current
        self._cur = self._fwd.pop()
        return self._cur

    def current(self) -> str:
        return self._cur
