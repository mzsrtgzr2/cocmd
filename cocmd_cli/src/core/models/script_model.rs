use serde_derive::{Serialize, Deserialize};
use crate::utils::sys::OS;

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Hash, Clone)]
pub enum StepRunnerType {
    #[serde(alias="shell", alias="SHELL")]
    SHELL,
    #[serde(alias="markdown", alias="MARKDOWN")]
    MARKDOWN,
    #[serde(alias="python", alias="PYTHON")]
    PYTHON,
    #[serde(alias="link", alias="LINK")]
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
    pub env: Option<OS>,
    pub description: Option<String>,
}