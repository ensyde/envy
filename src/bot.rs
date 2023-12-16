use config::Config;
use bnls::BnlsSocket;
use bncs::Bncs;

pub struct Bot {
    config: Config,
    bncs: Bncs,
    bnls: Option<BnlsSocket>,
}

impl Bot {
    pub fn new(config: Config) -> Self {
        let addr = format!("{}:{}", &config.host, config.port);
        let mut bncs = Bncs::new(addr);
        Bot{
            config: config,
            bncs: bncs
        }
    }
}
