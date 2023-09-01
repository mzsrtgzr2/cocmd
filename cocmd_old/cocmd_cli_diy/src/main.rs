extern crate clap;
use clap::{App, Arg, SubCommand};

fn main() {
    let matches = App::new("CoCmd CLI")
        .version("1.0")
        .author("Your Name")
        .about("CLI App in Rust")
        .subcommand(
            SubCommand::with_name("add")
                .about("Add a new item")
                .arg(
                    Arg::with_name("source")
                        .help("Source to add")
                        .required(true)
                        .index(1),
                ),
        )
        .subcommand(
            SubCommand::with_name("remove")
                .about("Remove an item")
                .arg(
                    Arg::with_name("source")
                        .help("Source to remove")
                        .required(true)
                        .index(1),
                ),
        )
        .subcommand(SubCommand::with_name("show").about("Show items"))
        .subcommand(
            SubCommand::with_name("run")
                .about("Run a script")
                .arg(
                    Arg::with_name("name")
                        .help("Name of the script to run")
                        .required(false)
                        .index(1),
                )
                .arg(
                    Arg::with_name("yes")
                        .short('y')
                        .long("yes")
                        .help("Don't ask 'are you sure' for every step"),
                ),
        )
        .subcommand(SubCommand::with_name("profile-loader").about("Load profile"))
        .subcommand(SubCommand::with_name("refresh").about("Refresh settings"))
        .get_matches();

    match matches.subcommand_name() {
        Some("add") => {
            let sub_matches = matches.subcommand_matches("add").unwrap();
            let source = sub_matches.value_of("source").unwrap();
            println!("Adding source: {}", source);
        }
        Some("remove") => {
            let sub_matches = matches.subcommand_matches("remove").unwrap();
            let source = sub_matches.value_of("source").unwrap();
            println!("Removing source: {}", source);
        }
        Some("show") => {
            println!("Showing items");
        }
        Some("run") => {
            let sub_matches = matches.subcommand_matches("run").unwrap();
            let name = sub_matches.value_of("name").unwrap_or("default_script");
            let yes = sub_matches.is_present("yes");
            println!("Running script: {}, Auto confirm: {}", name, yes);
        }
        Some("profile-loader") => {
            println!("Loading profile");
        }
        Some("refresh") => {
            println!("Refreshing settings");
        }
        _ => {}
    }
}