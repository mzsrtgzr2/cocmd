#![allow(clippy::unnecessary_wraps)]
#![allow(clippy::missing_const_for_fn)]
#![allow(unused_variables)]
mod cmd;
mod settings;
use settings::Settings;

fn main() {
    let app = cmd::default::command().subcommand(cmd::validate::command());

    let v = app.render_version();
    let matches = app.get_matches();

    let settings = Settings::new(None, None);

    // use info! or trace! etc. to log
    // to instrument use `#[tracing::instrument(level = "trace", skip(session), err)]`
    cmd::tracing(&matches);
    cmd::banner(&v, &matches);

    let res = matches.subcommand().map_or_else(
        || cmd::default::run(&matches),
        |tup| match tup {
            ("validate", subcommand_matches) => cmd::validate::run(&matches, subcommand_matches),
            _ => unreachable!(),
        },
    );

    cmd::result_exit(res);
}
