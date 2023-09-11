use anyhow::Result;
use cocmd::core::sources_manager::SourcesManager;
use cocmd::core::source::Source;
use cocmd::utils::repository::find_cocmd_files;
use console::Style;
use dialoguer::Confirm;
use std::path::Path;
use tracing::info;

pub fn add_source(sources_manager: &mut SourcesManager, source: &str) -> Result<cocmd::CmdExit> {
    info!("Add source {:?}", source);

    let source_label = if source == "demo" {
        let resources_path = Path::new(env!("CARGO_MANIFEST_DIR")).join("resources");
        resources_path.join(source)
    } else {
        Path::new(source).to_owned()
    };

    let locations = find_cocmd_files(&source_label.to_str().unwrap(), sources_manager.settings.scan_depth);

    let lst_locs = locations.join("\n  - ");
    let style = Style::new().bold().green();
    println!(
        "found {} cocmd sources in this path:\n  - {}",
        locations.len(),
        lst_locs
    );
    
    if Confirm::new().with_prompt("Do you want to continue?").interact()? {
        for loc in locations {
            let source = Source::new(&loc, &sources_manager.settings);
            sources_manager.add_source(source.unwrap());
            println!("{}", style.apply_to(format!("Source '{:?}' added", loc)));
        }
    } else {
        println!("{}", style.apply_to("Skipped. you answered 'NO'"));
    }

    Ok(cocmd::CmdExit {
        code: exitcode::OK,
        message: None,
    })
}
