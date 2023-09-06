use anyhow::Result;
use clap::{Arg, ArgAction, ArgMatches, Command};


pub fn run(
    _matches: &ArgMatches,
    _subcommand_matches: &ArgMatches,
) -> Result<cocmd::CmdExit> {
    Ok(cocmd::CmdExit {
        code: exitcode::OK,
        message: None,
    })
}
