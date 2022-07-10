from tackle import BaseHook, Field


class ReleasedFixtureHook(BaseHook):
    """A fixture."""

    hook_type: str = 'released'
    src: str = Field(..., description="A fixture source.")
    args: list = ['src']

    def exec(self) -> str:
        return self.src


class AddedLaterReleasedFixtureHook(BaseHook):
    """A hook that should not be available as it has been added after release."""

    hook_type: str = 'released_added_later'
    src: str = Field(..., description="A fixture source.")
    args: list = ['src']

    def exec(self) -> str:
        return self.src
