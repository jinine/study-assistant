// src/main.rs

use actix_web::{web, App, HttpResponse, HttpServer};
use std::sync::Mutex;
use serde::Deserialize;

mod email;

#[derive(Deserialize)]
struct Notification {
    message: String,
}

struct AppState {
    notifications: Mutex<Vec<String>>,
}

async fn send_notification(_data: web::Data<AppState>, notification: web::Json<Notification>) -> HttpResponse {
    let notification = notification.into_inner();

    match email::send_email("jinine@gmail.com", "New Notification", &notification.message).await {
        Ok(_) => HttpResponse::Ok().json("Notification sent!"),
        Err(e) => {
            eprintln!("Failed to send email: {}", e);
            HttpResponse::InternalServerError().json("Failed to send notification.")
        }
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let state = web::Data::new(AppState {
        notifications: Mutex::new(Vec::new()),
    });

    HttpServer::new(move || {
        App::new()
            .app_data(state.clone())
            .route("/send_notification", web::post().to(send_notification))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
