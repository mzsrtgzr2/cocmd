
#![allow(unused_variables)]
use anyhow::Result;
use crate::cmd::Settings as Settings;
use tracing::info;

pub fn add_source(
    settings: &Settings,
    source: &str,
) -> Result<cocmd::CmdExit> {
    
    info!("Add source {:?}", source);
    Ok(cocmd::CmdExit {
        code: exitcode::OK,
        message: None,
    })
}
