from lit_bashwork import LitBashWork

import lightning_app as la

class LitApp(la.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.w_p0c0 = LitBashWork()
        self.w_p0c1 = LitBashWork(cache_calls=False)
        self.w_p1c0 = LitBashWork(parallel=True)
        self.w_p1c1 = LitBashWork(parallel=True, cache_calls=False)

    def run_test(self,w):
      w.run("sleep 20")
      if w.work_is_free():
        w.run("sleep 5",timeout=0)
      if w.work_is_free():
        w.run("sleep 5",timeout=1)
      if w.work_is_free():
        w.run("sleep 5",timeout=6)
      if w.work_is_free():
        print(f"work is free.  called {w.work_calls_len()}")
        
    def run(self):
      self.run_test(self.w_p0c0)
      self.run_test(self.w_p0c1)
      self.run_test(self.w_p1c0)
      self.run_test(self.w_p1c1)

app = la.LightningApp(LitApp())
