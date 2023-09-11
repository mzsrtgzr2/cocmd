use std::process;

use anyhow::Result;
use cocmd::core::sources_manager::SourcesManager;
use dialoguer::{theme::ColorfulTheme, Select};

use tracing::{info, error};

pub fn run_automation(sources_manager: &mut SourcesManager, specific_name: Option<&str>) -> Result<cocmd::CmdExit> {
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

            script_choices[selected_script.unwrap()]
        }
    };

    if let Some(script) = available_automations.get(selected_name) {
        
        // let output = ScriptRunner::run(script, &settings.os, &script_args, &settings, auto_yes);
        print!("{:?}", script);
        // let output = script.content;

        // info!("[blue] Script executed:");
        // for line in output {
        //     info!(" - {}", line);
        // }

        info!("[bold green]Script {} completed", script.name);
    } else {
        error!("I don't know this script");
    }

    Ok(cocmd::CmdExit {
        code: exitcode::OK,
        message: None,
    })
}
