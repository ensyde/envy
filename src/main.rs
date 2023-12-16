use config::Config;
mod bncs;
mod bnls;

fn main() {
    let cfg = Config::load();
    let config = match cfg {
        Ok(c) => c,
        Err(e) => {
            eprintln!("Error loading config: {:?}", e);
            return;
        }
    };
    println!("Hello, world!");
}
