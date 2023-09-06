#![allow(clippy::missing_const_for_fn)]
// #![warn(missing_docs)] // uncomment for docs

mod data;
mod runner;
mod core;
pub use data::{CmdExit, CMD};
pub use self::core::consts;
pub use self::runner::run;
