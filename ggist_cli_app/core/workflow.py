
import subprocess
import os
from typing import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class WorkflowStep:
    title: str
    description: str
    cmd: str

class Workflow:

    def __init__(self, steps: Sequence[WorkflowStep], os: str):
        self.steps = steps
        self.os = os

    
    def play(self):

        for step in self.steps:
            print(f'running "{step.title}"')
            print(step.cmd)
            os.system(step.cmd)
            # subprocess.Popen([step.cmd], stdout=subprocess.PIPE)
