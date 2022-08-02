r"""
To test a lightning component:

1. Init the component.
2. call .run()
"""
from lit_bashwork.component import LitBashWork


def test_placeholder_component():
    messenger = LitBashWork()
    print("timeout=0")
    messenger.run("sleep 10", timeout=0)
    print("timeout=1")
    messenger.run("sleep 10", timeout=1)
    print("timeout=11")
    messenger.run("sleep 10", timeout=11)
