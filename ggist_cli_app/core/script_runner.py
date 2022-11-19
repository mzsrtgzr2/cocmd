
from os import path
from typing import Sequence, Optional
import inquirer
from ggist_cli_app.consts import Consts
from ggist_cli_app.core.models.script_model import ScriptModel, StepRunnerType, StepRefModel, StepsModel
from rich.markdown import Markdown

from ggist_cli_app.core.os import OS
from ggist_cli_app.utils import io
import subprocess
from ggist_cli_app.utils.console import console, error_console
from collections import OrderedDict


class ScriptRunner:
    
    @staticmethod
    def run(script: ScriptModel, os: OS, script_args: Sequence[str]):

        def out(command, *script_args):
            exec_file = path.join(io.get_tmp(), Consts.TMP_EXEC_FILE_NAME)
            io.file_write(exec_file, command)
            io.chmod_x(exec_file)
            p = subprocess.run(exec_file + ' ' + ' '.join(script_args), shell=True)           
            return p

        console.print(script.title, style="frame white on blue")
        
        if script.description:
            console.print(script.description, style="blue")

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

        

        steps_choices = OrderedDict()
        for ii, step in enumerate(ScriptRunner.iterate_steps(script, variation)):
            steps_choices[f'{ii} - {step.title}'] = step

        questions = [
            inquirer.Checkbox(
                "steps",
                message="Select what to execute: (all by default)",
                choices=steps_choices.keys(),
                default=steps_choices.keys(),
            ),
        ]

        answers = inquirer.prompt(questions)

        chosen_steps = tuple(
            step
            for label, step in steps_choices.items()
            if label in answers['steps']
        )
        
        console.print(f'Executing {len(chosen_steps)} steps:')

        for step in chosen_steps:
            is_mark_down = False
            if step.runner != StepRunnerType.MARKDOWN:
                console.print(f'{step.title}', style="frame white on blue")
                if step.description:
                    console.print(step.description)
                
                questions = [
                    inquirer.Confirm("sure", message="Continue?", default=True)]

                answers = inquirer.prompt(questions)
            else:
                is_mark_down = True

            if is_mark_down or answers['sure']: 
                if step.runner == StepRunnerType.SHELL:

                    r = out(step.content, *script_args)

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

    @staticmethod
    def iterate_steps(script: ScriptModel, variation: StepsModel):
        for step in variation.steps:
            if isinstance(step, StepRefModel):
                step = next(
                    global_step
                    for global_step in script.spec.globals
                    if global_step.id == step.ref
                )
            yield step