use crate::utils::sys::OS;
use crate::utils::io::{normalize_path, from_file};
use serde_derive::{Serialize as Se, Deserialize as De};
use super::script_model::ScriptModel;


#[derive(Debug, Se, De, PartialEq, Eq, Hash, Clone)]
pub struct Automation {
    pub name: String,
    pub file: Option<String>,
    pub content: Option<ScriptModel>,
}

impl Automation {
    pub fn load_content(&self, location: &str)->Automation {
        if let Some(file) = &self.file {
            let normalized_path = normalize_path(file, Some(location));
            
            match from_file::<ScriptModel>(&normalized_path) {
                Ok(script_model) => {
                    Automation{
                        content: Some(script_model),
                        ..self.clone()
                    }  
                }
                Err(_) => {
                    // Handle the error if needed
                    self.clone()
                }
            }
        } else {
            self.clone()
        }
    }

    pub fn supports_os(&self, os: &OS) -> bool {
        if let Some(content) = &self.content {
            if let Some(content_env) = &content.env {
                *content_env == *os || *content_env == OS::ANY;
            }
        }
        true
    }
}


#[derive(Debug, Se, De, PartialEq, Eq, Hash)]
pub struct SourceConfigModel {
    pub name: String,
    pub aliases: Option<String>,
    pub paths: Option<Vec<String>>,
    pub automations: Option<Vec<Automation>>,
}

