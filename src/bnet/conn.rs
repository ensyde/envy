use tokio::net::TcpStream;
use tokio::sync::mpsc::{Sender, Receiver};
use tokio::io::{AsyncReadExt, AsyncWriteExt};

pub struct Bncs {
    socket: TcpStream,
    recv: Receiver<Vec<u8>>,
    sender: Sender<Vec<u8>>
}

impl Bncs {
    pub async fn new(addr: &str) -> Self {
        let (tx, rx) = mpsc::channel<Vec<u8>>(32);
        let socket = TcpStream::connect(addr).await?;
        Bncs{
            socket: socket,
            recv: rx,
            sender: tx
        }
    }
}
