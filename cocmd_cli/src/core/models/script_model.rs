use serde_derive::{Serialize, Deserialize};
use crate::utils::sys::OS;

#[derive(Debug, Serialize, Deserialize)]
pub enum StepRunnerType {
    SHELL,
    MARKDOWN,
    PYTHON,
    LINK,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct StepModel {
    pub runner: StepRunnerType,
    pub content: String,
    pub title: String,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct ScriptModel {
    pub steps: Vec<StepModel>,
    pub env: Option<OS>,
    pub description: Option<String>,
}