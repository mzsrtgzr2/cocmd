
from typing import Sequence, Optional
import inquirer
from ggist_cli_app.core.models.script_model import ScriptModel, StepRunnerType, StepRefModel
from rich.markdown import Markdown

from ggist_cli_app.core.os import OS
import subprocess
from ggist_cli_app.utils.console import console, error_console


class ScriptRunner:
    
    @staticmethod
    def run(script: ScriptModel, os: OS):        

        def out(command):
            p = subprocess.run(command, shell=True)           
            return p

        console.print(script.title, style="frame")
        
        if script.description:
            console.print(script.description, style="frame")

        variations_for_os = script.get_variations_for_os(os)

        if len(variations_for_os) > 1:
            questions = [
                inquirer.List(
                    "variation",
                    message="What variations to run?",
                    choices=tuple(
                        variation.label
                        for variation in variations_for_os
                    ),
                ),
            ]

            answers = inquirer.prompt(questions)
            variation = answers['variation']
        else:
            variation = variations_for_os[0]

        console.print(f'Executing {len(variation.steps)} steps:')

        for ii, step in enumerate(variation.steps):

            if isinstance(step, StepRefModel):
                step = next(
                    global_step
                    for global_step in script.spec.globals
                    if global_step.id == step.ref
                )
            
            is_mark_down = False
            if step.runner != StepRunnerType.MARKDOWN:
                console.print(f'Step {ii+1}/{len(variation.steps)}: {step.title}', style="blue on white")
                if step.description:
                    console.print(step.description)
                
                questions = [
                    inquirer.Confirm("sure", message="Continue?", default=True)]

                answers = inquirer.prompt(questions)
            else:
                is_mark_down = True

            if is_mark_down or answers['sure']: 
                if step.runner == StepRunnerType.SHELL:
                    r = out(step.content)

                    if r.returncode:
                        error_console.print("failed to run step")
                        return
                elif step.runner == StepRunnerType.MARKDOWN:
                    markdown = Markdown(step.content)
                    console.print(markdown)
                else:
                    raise NotImplemented
            else:
                console.print("[gray] Skipped")
                
        console.print("[bold green]Script completed")
