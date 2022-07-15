r"""
To test a lightning component:

1. Init the component.
2. call .run()
"""
from lit_bashwork.component import LitBashWork


def test_placeholder_component():
    messenger = LitBashWork()
    messenger.run("ls README.md")
    assert messenger.stdout[0] == "README.md"
