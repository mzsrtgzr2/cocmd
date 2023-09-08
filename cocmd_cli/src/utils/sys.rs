use std::fmt;

pub enum OS {
    Windows,
    Linux,
    MacOS,
    Other,
}

impl fmt::Display for OS {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            OS::Windows => write!(f, "Windows"),
            OS::Linux => write!(f, "Linux"),
            OS::MacOS => write!(f, "MacOS"),
            OS::Other => write!(f, "Other"),
        }
    }
}

pub fn get_os() -> OS {
    match std::env::consts::OS {
        "windows" => OS::Windows,
        "linux" => OS::Linux,
        "macos" => OS::MacOS,
        _ => OS::Other,
    }
}