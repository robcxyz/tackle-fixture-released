from tackle import BaseHook, Field


class ReleasedFixtureHook(BaseHook):
    """A fixture."""

    hook_name: str = 'python_hook'
    src: str = Field(..., description="A fixture source.")
    args: list = ['src']

    def exec(self) -> str:
        return self.src


# class AddedLaterReleasedFixtureHook(BaseHook):
#     """A hook that should not be available as it has been added after release."""
#
#     hook_name: str = 'released_added_later'
#     src: str = Field(..., description="A fixture source.")
#     args: list = ['src']
#
#     def exec(self) -> str:
#         return self.src
