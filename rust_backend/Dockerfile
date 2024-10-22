# Use the official Rust image
FROM rust:1.72

# Set the working directory
WORKDIR /app

# Copy the Rust project files
COPY . .

# Build the Rust project
RUN cargo build --release

# Expose port (e.g., 8080) for the Rust backend
EXPOSE 8080

# Run the Rust binary
CMD ["./target/release/my_rust_app"]
