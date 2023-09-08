use cocmd::consts;
use std::fs;
use cocmd::utils::sys::get_os;
pub struct Settings {
    pub home: String,
    pub terminal: String,
    pub config_file: String,
    pub sources_file: String,
    pub scan_depth: i32,
    pub os: String,
    // sources_manager: SourcesManager, // You'll need to define this
    // credentials: CredsConfigModel, // You'll need to define this
}

impl Settings {
    pub fn new(home: Option<&str>, terminal: Option<&str>) -> Self {

        let home = home.unwrap_or(&consts::HOME);
        let terminal = terminal.unwrap_or(&consts::DEFAULT_TERMINAL);

        let config_file = format!("{}/{}", home, consts::CONFIG_FILE);
        let sources_file = format!("{}/{}", home, consts::SOURCES_FILE);

        // Create directories and files
        fs::create_dir_all(home).unwrap();
        fs::File::create(&sources_file).unwrap();

        // Initialize other fields
        Settings {
            home: home.to_string(),
            terminal: terminal.to_string(),
            config_file,
            sources_file,
            scan_depth: 2,
            os: get_os().to_string()
            // sources_manager: SourcesManager::new(), // Initialize this
            // credentials: CredsConfigModel::new(), // Initialize this
        }
    }

    // fn read_creds(&self) -> CredsConfigModel {
    //     // Implement this function
    // }
}