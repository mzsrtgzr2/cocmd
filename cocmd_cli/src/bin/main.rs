mod cmd;
use cocmd::Settings;
use clap::{Parser, Subcommand};
use cmd::add;
use cmd::tracing;
use cocmd::core::sources_manager::SourcesManager;

use crate::cmd::run::run_automation;

#[derive(Parser)]
#[command(author = "Your Name", version = "1.0", about = "CoCmd CLI")]
struct Cli {
    #[arg(short, long)]
    verbose: bool,

    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    ProfileLoader,
    Refresh,
    Run {
        name: Option<String>
    },
    Show(ShowArgs),
    Add(AddArgs),
    Remove,
}



#[derive(Parser)]
struct AddArgs {
    #[command(subcommand)]
    add_commands: AddCommands
}


#[derive(Subcommand)]
enum AddCommands {
    Source{
        name: String
    }
}

#[derive(Parser)]
struct ShowArgs {
    #[command(subcommand)]
    show_commands: ShowCommands
}


#[derive(Subcommand)]
enum ShowCommands {
    Source{
        name: String
    },
    Sources
}


#[derive(Subcommand)]
enum Remove {
    Source(RemoveSourceArgs),
}

#[derive(Parser)]
struct AddSourceArgs {
    source: String,
}

#[derive(Parser)]
struct RemoveSourceArgs {
    source: String,
}

#[derive(Parser)]
struct ShowSourceArgs {
    source: String,
}

fn main() {
    let cli = Cli::parse();

    let settings = Settings::new(None, None);
    let mut sources_manager = SourcesManager::new(settings);
    tracing(cli.verbose);

    match cli.command {
        Commands::ProfileLoader => {
            println!("'cocmd profile_loader' was used");
        }
        Commands::Refresh => {
            println!("'cocmd refresh' was used");
        }
        Commands::Run {name} => {
            println!("'cocmd run' was used");
            run_automation(&mut sources_manager, name);
        }
        Commands::Show(args) => match args.show_commands {
            ShowCommands::Source { name } => {
                println!("'cocmd show source' was used, name is: {}", name);
            }
            ShowCommands::Sources => {
                println!("'cocmd show sources' was used");
            }
        },
        Commands::Add(args) => match args.add_commands {
            AddCommands::Source { name } => {
                add::add_source(&mut sources_manager,&name);
            }
        },
        Commands::Remove => {
            println!("'cocmd remove' was used");
        }
    }
}

