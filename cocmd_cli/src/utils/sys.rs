use std::fmt;

use serde_derive::{Serialize, Deserialize};

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize, Hash, Clone)]
pub enum OS {
    Windows,
    Linux,
    MacOS,
    Other,
    ANY
}

impl fmt::Display for OS {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            OS::Windows => write!(f, "Windows"),
            OS::Linux => write!(f, "Linux"),
            OS::MacOS => write!(f, "MacOS"),
            OS::Other => write!(f, "Other"),
            OS::ANY => write!(f, "Any"),
        }
    }
}

pub fn get_os() -> OS {
    match std::env::consts::OS {
        "windows" => OS::Windows,
        "linux" => OS::Linux,
        "macos" => OS::MacOS,
        "any" => OS::ANY,
        _ => OS::Other,
    }
}