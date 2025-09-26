class BrowserHistory:
    def __init__(self, start="home"):
        self._cur = start
        self._back = []
        self._fwd = []

    def visit(self, url: str) -> None:
        # push current into back if it's not "home"
        if self._cur != "home":
            self._back.append(self._cur)
        self._cur = url
        self._fwd.clear()

    def back(self) -> str:
        if not self._back:
            raise IndexError("No pages in back history")
        self._fwd.append(self._cur)
        self._cur = self._back.pop()
        return self._cur

    def forward(self) -> str:
        if not self._fwd:
            raise IndexError("No pages in forward history")
        self._back.append(self._cur)
        self._cur = self._fwd.pop()
        return self._cur

    def current(self) -> str:
        return self._cur

    def __repr__(self):
        return f"<BrowserHistory back={self._back} current={self._cur!r} forward={list(reversed(self._fwd))}>"
