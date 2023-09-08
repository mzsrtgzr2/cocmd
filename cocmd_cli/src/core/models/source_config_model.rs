use cocmd_cli::core::os::OS;
use cocmd_cli::utils::io::{DictLoader, YamlIO, normalize_path};
use serde_derive::{Serialize, Deserialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct ScriptModel {
    // Define the fields of ScriptModel here
}

#[derive(Debug, Serialize, Deserialize)]
pub struct Automation {
    name: String,
    file: Option<String>,
    content: Option<ScriptModel>,
}

impl Automation {
    pub fn load_content(&mut self, location: &str) {
        if let Some(file) = &self.file {
            let normalized_path = normalize_path(file, Some(location));
            match YamlIO::from_file(&normalized_path) {
                Ok(script_model) => {
                    self.content = Some(script_model);
                }
                Err(_) => {
                    // Handle the error if needed
                }
            }
        }
    }

    pub fn supports_os(&self, os: OS) -> bool {
        if let Some(content) = &self.content {
            // Assuming that content.env is the OS enum variant or a similar value
            return content.env == os || content.env == OS::ANY;
        }
        false
    }
}

#[derive(Debug, Serialize, Deserialize)]
pub struct SourceConfigModel {
    pub name: String,
    pub aliases: Option<String>,
    pub paths: Option<Vec<String>>,
    pub automations: Option<Vec<Automation>>,
}

impl DictLoader for SourceConfigModel {
    // Implement the DictLoader trait methods here
}
