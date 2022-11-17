
from typing import Sequence, Mapping, Optional
from dataclasses import dataclass
from rich.console import Console

from ggist_cli_app.core.os import OS
import subprocess
from ggist_cli_app.utils.console import console, error_console


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

        def out(command):
            p = subprocess.run(command, shell=True)           
            return p

        for ii, cmd in enumerate(self.commands):
            
            console.print(f'[bold]running step {ii+1} out of {len(self.steps)}: "{cmd.cmd}"\n')

            r = out(cmd.cmd)

            if r.returncode:
                error_console.print("failed to run step")
                return
            
                
        console.print("[bold green]Flow completed")
    
    @property
    def commands(self)->Optional[Sequence[WorkflowCommand]]:
        commands = []
        for ii, step in enumerate(self.steps):
            if self.os in step.cmd:
                commands.append(step.cmd[self.os])
            elif OS.any in step.cmd:
                commands.append(step.cmd[OS.any])
            else:
                error_console.print(f'step #{ii}({step.title}) missing your operating system support ({self.os})')
                return None
        return commands
