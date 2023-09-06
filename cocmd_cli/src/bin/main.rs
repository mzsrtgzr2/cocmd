mod cmd;

use clap::{Parser, Subcommand};
use cmd::Settings;


#[derive(Parser)]
#[command(author = "Your Name", version = "1.0", about = "CoCmd CLI")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    ProfileLoader,
    Refresh,
    Run,
    Show(ShowArgs),
    Add,
    Remove,
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

    match cli.command {
        Commands::ProfileLoader => {
            println!("'cocmd profile_loader' was used");
        }
        Commands::Refresh => {
            println!("'cocmd refresh' was used");
        }
        Commands::Run => {
            println!("'cocmd run' was used");
        }
        Commands::Show(args) => match args.show_commands {
            ShowCommands::Source { name } => {
                println!("'cocmd show source' was used, name is: {}", name);
            }
            ShowCommands::Sources => {
                println!("'cocmd show sources' was used");
            }
        },
        Commands::Add => {
            println!("'cocmd add' was used");
        }
        Commands::Remove => {
            println!("'cocmd remove' was used");
        }
    }
}

