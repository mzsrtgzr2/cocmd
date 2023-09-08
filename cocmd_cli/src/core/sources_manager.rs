use std::collections::HashSet;
use std::path::Path;
use std::fs;

use crate::cmd::Settings;
use crate::cmd::Source;

pub struct SourcesManager {
    settings: Settings,
    sources_file: String,
    sources: HashSet<Source>,
}

impl SourcesManager {
    pub fn new(settings: Settings) -> Self {
        let sources_file = settings.sources_file.clone();
        let sources = Self::load_sources(&sources_file, &settings);
        Self {
            settings,
            sources_file,
            sources,
        }
    }

    pub fn remove_source(&mut self, source: Source) {
        self.sources.remove(&source);
        self.save();
    }

    pub fn add_source(&mut self, source: Source) {
        self.sources.insert(source);
        self.save();
    }

    pub fn save(&self) {
        Self::save_sources(&self.sources_file, &self.sources);
    }

    fn save_sources(sources_file: &str, sources: &HashSet<Source>) {
        let source_strings: Vec<String> = sources.iter().map(|s| s.to_string()).collect();
        file_write_lines(sources_file, &source_strings);
    }

    fn load_sources(sources_file: &str, settings: &Settings) -> HashSet<Source> {
        match file_read_lines(sources_file) {
            Ok(lines) => {
                let mut sources = HashSet::new();
                for line in lines {
                    let source = Source::new(line.as_str(), settings);
                    sources.insert(source);
                }
                sources
            }
            Err(_) => HashSet::new(),
        }
    }

    pub fn automations(&self) -> HashMap<String, Automation> {
        let mut automations = HashMap::new();
        for source in &self.sources {
            for automation in &source.automations {
                let key = format!("{}.{}", source.name, automation.name);
                automations.insert(key, automation.clone());
            }
        }
        automations
    }
}
