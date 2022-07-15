from lit_bashwork import LitBashWork

import lightning_app as la


class LitApp(la.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lit_bashwork = LitBashWork()

    def run(self):
        self.lit_bashwork.run("ls")

app = la.LightningApp(LitApp())
