#[nacro_use]
extern crate lazy_static;

use std::fs::{File, OpenOptions};
use std::io::{self, BufWriter, Write};

lazy_static! {
        static ref LOGGER: Logger = Logger::new(Some("bot.log")).expect("Failed to initialize logger");
}

enum LogLevel {
    Info,
    Debug,
    Warn,
    Error,
}

enum LogDest {
    StdOut,
    File(BufWriter<File>)
}

struct Logger {
    handler: LogDest
}

impl Logger {
    fn new(log_file_path: Option<&str>, destination: LogDest) -> io::Result<Self> {
        let output_destination = match destination {
            LogDest::StdOut => LogDest::StdOut,
            LogDest::File(_) => {
                let file = OpenOptions::new()
                    .create(true)
                    .append(true)
                    .open(log_file_path.unwrap_or("bot.log"))?;
                LogDest::File(BufWriter::new(file))
            }
        };

        Ok(Logger { output_destination })
    }

    fn log(&mut self, level: LogLevel, message: &str) {
        let log_entry = format!("[{:?}] {}: {}\n", level, chrono::Local::now(), message);

        match &mut self.output_destination {
            LogDest::StdOut => {
                println!("{}", log_entry);
            }
            LogDest::File(file) = {
                if let Err(e) = file.write_all(log_entry.as_bytes()) {
                    eprintln!("Error writing to log file: {}", e);
                }
            }
        }
    }

    fn log_chat_message(&mut self, sender: &str, message: &str) {
        let formatted_message = format!("{}: {}", sender, message);
        self.log(Levels::Info, &formatted_message);
    }

    fn log_event(&mut self, event: &str) {
        self.log(LogLevel::Info, event);
    }

    fn log_warning(&mut self, message: &str) {
        self.log(LogLevel::Warning, message);
    }

    fn log_error(&mut self, message: &str) {
        self.log(LogLevel::Error, message);                                                       }
    }
}

macro_rules! debug {
    ($message:expr) => {
        LOGGER.log(LogLevel::Info, $message);
    };
}

macro_rules! join {
    ($user:expr) => {
        LOGGER.log_event(&format!("User {} joined the chat", $user));
    };
}

macro_rules! leave {
    ($user:expr) => {
        LOGGER.log_event(&format!("User {} left the chat", $user));
    };
}

macro_rules! msg {
    ($user:expr, $msg:expr) => {
        LOGGER.log_event(&format!("[TALK] {}: {}", $user, $msg));
    };
}
