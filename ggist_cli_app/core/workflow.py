
import subprocess
import os
from typing import Sequence, Mapping
from dataclasses import dataclass
from rich.console import Console

from ggist_cli_app.core.os import OS


@dataclass(frozen=True)
class WorkflowCommand:
    cmd: str

@dataclass(frozen=True)
class WorkflowStep:
    title: str
    description: str
    cmd: Mapping[OS, WorkflowCommand]

class Workflow:

    def __init__(self, steps: Sequence[WorkflowStep], os: OS):
        self.steps = steps
        self.os = os

    
    def play(self):
        console = Console()

        from subprocess import PIPE, run

        def out(command):
            result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
            return result.stdout

        for ii, step in enumerate(self.steps):
            
            if self.os in step.cmd:
                flow_cmd = step.cmd[self.os]
            elif OS.any in step.cmd:
                flow_cmd = step.cmd[OS.any]
            else:
                raise LookupError(f'no os config for step {step}')
            console.print(f'[bold]running step {ii+1} out of {len(self.steps)}: "{step.title}"\n')
            
            
            console.print(out(flow_cmd.cmd))

            # subprocess.Popen([step.cmd], stdout=subprocess.PIPE)
            # console.log(f"step {ii+1} complete")
            
                
        console.print("[bold green]Flow completed")
                
