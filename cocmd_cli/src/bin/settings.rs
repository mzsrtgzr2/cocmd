use cocmd;
use dirs;
use cocmd::Consts;

pub struct Settings {
    home: String,
    terminal: String,
    config_file: String,
    sources_file: String,
    scan_depth: i32,
    os: String,
    // sources_manager: SourcesManager, // You'll need to define this
    // credentials: CredsConfigModel, // You'll need to define this
}

impl Settings {
    fn new(home: Option<&str>, terminal: Option<&str>) -> Self {
        let consts = Consts {
            home: format!("{}/.cocmd", dirs::home_dir().unwrap().to_str().unwrap()),
            source_config_file: "cocmd.yaml",
            default_terminal: "bash",
            config_file: "config.yaml",
            sources_file: "sources.txt",
            tmp_exec_file_name: "cocmd-exec.sh",
            credentials_file: "creds.yamal",
        };

        let home = home.unwrap_or(&consts.home);
        let terminal = terminal.unwrap_or(consts.default_terminal);

        let config_file = format!("{}/{}", home, consts.config_file);
        let sources_file = format!("{}/{}", home, consts.sources_file);

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
            os: "your_os_here".to_string(), // Replace with actual OS info
            // sources_manager: SourcesManager::new(), // Initialize this
            // credentials: CredsConfigModel::new(), // Initialize this
        }
    }

    // fn read_creds(&self) -> CredsConfigModel {
    //     // Implement this function
    // }
}