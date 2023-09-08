use std::path::Path;
use std::fs;
use crate::consts;
use crate::core::models::source_config_model::SourceConfigModel;
use crate::utils::io::{from_file, exists, normalize_path};
use crate::cocmd::Settings;
use crate::core::models::source_config_model::Automation;

pub struct Source {
    settings: Settings,
    location: String,
    cocmd_config: Option<SourceConfigModel>,
}

impl Source {
    pub fn new(location: &str, settings: Settings) -> Result<Self, String> {
        let mut source = Source {
            settings,
            location: location.to_lowercase(),
            cocmd_config: None,
        };

        if exists(&source.location) {
            source.location = fs::canonicalize(&source.location)
                .map_err(|e| e.to_string())?
                .to_str()
                .unwrap_or("")
                .to_string();
            
            let config_file_path = Path::new(&source.location)
                .join(consts::SOURCE_CONFIG_FILE);
            
            if config_file_path.exists() {
                let config: SourceConfigModel = from_file(&config_file_path)
                    .map_err(|e| e.to_string())?;
                source.cocmd_config = Some(config);
            }
        } else {
            return Err(format!("Path {} does not exist.", source.location));
        }

        Ok(source)
    }

    pub fn is_exists_locally(&self) -> bool {
        false // Implement this logic as needed
    }

    pub fn aliases(&self) -> Vec<String> {
        match &self.cocmd_config {
            Some(config) => config.aliases.clone(),
            None => vec![], // or any other default behavior
        }
    }

    pub fn name(&self) -> &str {
        match &self.cocmd_config {
            Some(config) => &config.name,
            None => "", // or any other default behavior
        }
    }

    pub fn paths(&self) -> Vec<String> {
        match &self.cocmd_config {
            Some(config) => {
                config.paths.iter().map(|p| normalize_path(p, &self.location)).collect()
            }
            None => vec![], // or any other default behavior
        }
    }

    pub fn automations(&self) -> Vec<Automation> {
        let mut result = vec![];
        if let Some(config) = &self.cocmd_config {
            for automation in &config.automations {
                automation.load_content(&self.location);
                if automation.supports_os(&self.settings.os) {
                    result.push(automation.clone());
                }
            }
        }
        result
    }

    pub fn location(&self) -> &str {
        &self.location
    }
}
