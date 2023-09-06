use clap::{Parser, Subcommand};

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
    Source(SourceArgs),
}

#[derive(Parser)]
struct SourceArgs {
    #[command(subcommand)]
    command: SourceCommands,
}

#[derive(Subcommand)]
enum SourceCommands {
    Add(AddSourceArgs),
    Remove(RemoveSourceArgs),
    Show(ShowArgs),
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
struct ShowArgs {
    #[command(subcommand)]
    command: ShowCommands,
}

#[derive(Subcommand)]
enum ShowCommands {
    Sources,
    Source(ShowSourceArgs),
}

#[derive(Parser)]
struct ShowSourceArgs {
    source: String,
}

fn main() {
    let cli = Cli::parse();

    match cli.command {
        Commands::ProfileLoader => println!("'cocmd profile_loader' was used"),
        Commands::Refresh => println!("'cocmd refresh' was used"),
        Commands::Run => println!("'cocmd run' was used"),
        Commands::Source(args) => match args.command {
            SourceCommands::Add(add_args) => println!("'cocmd source add' was used, source is: {}", add_args.source),
            SourceCommands::Remove(remove_args) => println!("'cocmd source remove' was used, source is: {}", remove_args.source),
            SourceCommands::Show(show_args) => match show_args.command {
                ShowCommands::Sources => println!("'cocmd source show sources' was used"),
                ShowCommands::Source(show_source_args) => println!("'cocmd source show source' was used, source is: {}", show_source_args.source),
            },
        },
    }
}
