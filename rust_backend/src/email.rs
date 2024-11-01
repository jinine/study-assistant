// src/email.rs

use lettre::{Message, SmtpTransport, Transport};

// Make the function public
pub async fn send_email(to: &str, subject: &str, body: &str) -> Result<(), lettre::transport::smtp::Error> {
    let email = Message::builder()
        .from("jinine@gmail.com".parse().unwrap())
        .to(to.parse().unwrap())
        .subject(subject)
        .body(body.to_string())
        .unwrap();

    let mailer = SmtpTransport::unencrypted_localhost();

    // Send the email and propagate any errors
    mailer.send(&email)?;

    Ok(())
}
