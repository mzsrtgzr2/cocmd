use std::process;

use anyhow::Result;
use cocmd::core::{sources_manager::SourcesManager, models::script_model::{StepModel, StepRunnerType, ScriptModel}};
use dialoguer::{theme::ColorfulTheme, Select};

use std::process::{Command, Stdio};
use execute::{Execute, shell};
use cocmd::utils::sys::OS;

use tracing::{info, error};
use termimad;

pub fn run_automation(sources_manager: &mut SourcesManager, specific_name: Option<String>) -> Result<cocmd::CmdExit> {
    let available_automations = sources_manager.automations();

    let selected_name = match specific_name {
        Some(name) => name,
        None => {
            let script_choices: Vec<&String> = available_automations.keys().collect();
            let selected_script = Select::with_theme(&ColorfulTheme::default())
                .with_prompt("What script to run?")
                .items(&script_choices)
                .default(0) // Set a default selection if needed
                .interact_opt()
                .unwrap_or_else(|_e| {
                    error!("No script selected.");
                    process::exit(1)
                });

            script_choices[selected_script.unwrap()].to_string()
        }
    };

    if let Some(automation) = available_automations.get(&selected_name) {
        
        // let output = ScriptRunner::run(script, &settings.os, &script_args, &settings, auto_yes);
        // info!("{:?}", script);
        // let output = script.content;
        handle_script(&automation.content.as_ref().unwrap(), sources_manager.settings.os);
        // info!("[blue] Script executed:");
        // for line in output {
        //     info!(" - {}", line);
        // }

        info!("Script {} completed", automation.name);
    } else {
        error!("I don't know this script");
    }

    Ok(cocmd::CmdExit {
        code: exitcode::OK,
        message: None,
    })
}

fn interactive_shell(step: &StepModel) {
    let mut command = shell(&step.content.as_ref().unwrap());

    command.stdout(Stdio::piped());
    command.stdin(Stdio::piped());

    print!("{:?}", step.content);
    let output = command.execute_output().unwrap();

    println!("{}", String::from_utf8(output.stdout).unwrap());
}

fn handle_step(step: &StepModel, env: OS) {
    let content = step.content.as_ref().unwrap().as_str();
    let skin = termimad::MadSkin::default();
    match &step.runner {
        StepRunnerType::SHELL => {
            skin.print_text(&format!("# running step - {}", &step.title));
            interactive_shell(step);
            
        }
        StepRunnerType::MARKDOWN => {
            // Print Markdown content
            skin.print_text(content);
        }
        StepRunnerType::PYTHON => {
            // Execute Python script
            let output = Command::new("python")
                .arg("-c")
                .arg(content)
                .output()
                .expect("Failed to execute Python script.");

            println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
            println!("stderr: {}", String::from_utf8_lossy(&output.stderr));
        }
        StepRunnerType::LINK => {
            // Open URL in default browser (platform-specific)
            match env {
                OS::Windows => {
                    Command::new("cmd")
                        .arg("/C")
                        .arg("start")
                        .arg(content)
                        .spawn()
                        .expect("Failed to open link in the default browser.");
                }
                OS::Linux => {
                    Command::new("xdg-open")
                        .arg(content)
                        .spawn()
                        .expect("Failed to open link in the default browser.");
                }
                OS::MacOS => {
                    Command::new("open")
                        .arg(content)
                        .spawn()
                        .expect("Failed to open link in the default browser.");
                }
                OS::Other => todo!(),
                OS::ANY => todo!(),
            }
        
        }
    }
}

fn handle_script(script: &ScriptModel, env: OS) {
    for step in &script.steps {
        handle_step(step, env);
    }
}
