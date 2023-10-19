use enigo::{Enigo, EnigoSettings, KeyboardControllable};
use std::thread;
use std::time::Duration;

fn main() {
    env_logger::init();
    thread::sleep(Duration::from_secs(2));
    let mut enigo = Enigo::new(&EnigoSettings::default()).unwrap();

    // write text and select all
    enigo.key_sequence_parse("{+UNICODE}{{Hello World!}} ❤️{-UNICODE}{+CTRL}a{-CTRL}");
}
