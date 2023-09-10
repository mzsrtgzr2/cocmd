use crate::utils::sys::OS;
use crate::utils::io::{normalize_path, from_file};
use serde_derive::{Serialize, Deserialize};
use super::script_model::ScriptModel;


#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Hash, Clone)]
pub struct Automation {
    pub name: String,
    pub file: Option<String>,
    pub content: Option<ScriptModel>,
}

impl Automation {
    pub fn load_content(&mut self, location: &str) {
        if let Some(file) = &self.file {
            let normalized_path = normalize_path(file, Some(location));
            
            match from_file::<ScriptModel>(&normalized_path) {
                Ok(script_model) => {
                    self.content = Some(script_model);    
                }
                Err(_) => {
                    // Handle the error if needed
                }
            }
        }
    }

    pub fn supports_os(&self, os: &OS) -> bool {
        if let Some(content) = &self.content {
            // Assuming that content.env is the OS enum variant or a similar value
            return content.env == *os || content.env == OS::ANY;
        }
        false
    }
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub struct SourceConfigModel {
    pub name: String,
    pub aliases: Option<String>,
    pub paths: Vec<String>,
    pub automations: Vec<Automation>,
}

