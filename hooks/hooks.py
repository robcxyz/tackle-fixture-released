from tackle import BaseHook, Field


class ReleasedFixtureHook(BaseHook):
    """A fixture."""

    hook_type: str = 'released'
    src: str = Field(..., description="A fixture source.")
    args: list = ['src']

    def exec(self) -> str:
        return self.src
