use serde_derive::Deserialize;
use std::fs::File;
use std::io::Read;

#[derive(Debug, Deserialize)]
pub struct Config {
    login: LoginConfig,
    bnet: BnetConfig,
    bnls: BnlsConfig,
    opts: OptsConfig
}
#[derive(Debug, Deserialize)]
pub struct LoginConfig {
    acct: String,
    pw: String,
    home: String,
}
#[derive(Debug, Deserialize)]
pub struct BnetConfig {
    host: String,
    port: u16,
    game: String,
    cdkey: String,
    verbyte: String,
}
#[derive(Debug, Deserialize)]
pub struct BnlsConfig {
    bnls: bool,
    host: String,
    port: u16
}
#[derive(Debug, Deserialize)]
pub struct OptsConfig {
    trigger: char,
}

impl Config {
    fn load() -> Result<Self, toml::de::Error> {
        let filename = "config.toml";
        let mut file_content = String::new();
        let mut file = File::open(filename)?;
        file.read_to_string(&mut file_content)?;

        let config: Config = toml::from_str(&file_content)?;
        Ok(config)
    }
}
