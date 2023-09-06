#![allow(dead_code)]
use dirs;
use lazy_static::lazy_static;


lazy_static! {
    pub static ref HOME: String = {
        let home_dir = dirs::home_dir().unwrap();
        format!("{}/.cocmd", home_dir.to_str().unwrap())
    };
}pub const SOURCE_CONFIG_FILE: &str = "cocmd.yaml";
pub const DEFAULT_TERMINAL: &str = "bash";
pub const CONFIG_FILE: &str = "config.yaml";
pub const SOURCES_FILE: &str = "sources.txt";
pub const TMP_EXEC_FILE_NAME: &str = "cocmd-exec.sh";
pub const CREDENTIALS_FILE: &str = "creds.yaml";