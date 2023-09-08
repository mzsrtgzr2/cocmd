use anyhow::Result;
use crate::cmd::Settings;
use cocmd::core::source::Source;
use cocmd::utils::repository::find_cocmd_files;
use console::Style;
use dialoguer::{Confirmation, Input};
use std::path::Path;
use tracing::info;

pub fn add_source(settings: &Settings, source: &str) -> Result<cocmd::CmdExit> {
    info!("Add source {:?}", source);

    let source_label = if source == "demo" {
        let resources_path = Path::new(env!("CARGO_MANIFEST_DIR")).join("resources");
        resources_path.join(source)
    } else {
        Path::new(source).to_owned()
    };

    let locations = find_cocmd_files(&source_label, settings.scan_depth)?;

    let lst_locs = locations.join("\n  - ");
    let style = Style::new().bold().green();
    println!(
        "found {} cocmd sources in this path:\n  - {}",
        locations.len(),
        lst_locs
    );

    if Confirmation::new()
        .with_text("Continue?")
        .default(true)
        .interact()?
    {
        for loc in locations {
            let source = Source::new(&loc, settings)?;
            settings.sources_manager.add_source(source)?;
            println!("{}", style.apply(format!("Source '{}' added", source)));
        }
    } else {
        println!("{}", style.apply("Skipped. you answered 'NO'"));
    }

    Ok(cocmd::CmdExit {
        code: exitcode::OK,
        message: None,
    })
}
