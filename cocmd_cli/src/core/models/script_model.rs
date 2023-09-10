use serde_derive::{Serialize, Deserialize};
use crate::utils::sys::OS;

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Hash, Clone)]
pub enum StepRunnerType {
    SHELL,
    MARKDOWN,
    PYTHON,
    LINK,
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Hash, Clone)]
pub struct StepModel {
    pub runner: StepRunnerType,
    pub content: String,
    pub title: String,
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Hash, Clone)]
pub struct ScriptModel {
    pub steps: Vec<StepModel>,
    pub env: OS,
    pub description: String,
}