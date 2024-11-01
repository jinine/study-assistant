#include <iostream>
#include <cstring>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netdb.h>

#define DEFAULT_PORT "8080"
#define BUFFER_SIZE 2048

void handle_request(int client_socket) {
    char buffer[BUFFER_SIZE];
    ssize_t recv_result = recv(client_socket, buffer, sizeof(buffer) - 1, 0);
    
    if (recv_result > 0) {
        buffer[recv_result] = '\0';
        std::cout << "Received request:\n" << buffer << std::endl;

        // Check for GET request
        if (strncmp(buffer, "GET", 3) == 0) {
            const char* response =
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                "Content-Length: 13\r\n"
                "Connection: close\r\n"
                "\r\n"
                "Hello, World!";
            send(client_socket, response, strlen(response), 0);
        }
        // Check for POST request
        else if (strncmp(buffer, "POST", 4) == 0) {
            const char* response =
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                "Content-Length: 23\r\n"
                "Connection: close\r\n"
                "\r\n"
                "Post received!";
            send(client_socket, response, strlen(response), 0);
        }
        // If neither GET nor POST
        else {
            const char* response =
                "HTTP/1.1 400 Bad Request\r\n"
                "Content-Type: text/plain\r\n"
                "Content-Length: 15\r\n"
                "Connection: close\r\n"
                "\r\n"
                "Bad Request";
            send(client_socket, response, strlen(response), 0);
        }
    }

    close(client_socket);
}

int main() {
    addrinfo hints, *result;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET; // IPv4
    hints.ai_socktype = SOCK_STREAM; // Stream socket
    hints.ai_flags = AI_PASSIVE; // Use my IP

    if (getaddrinfo(NULL, DEFAULT_PORT, &hints, &result) != 0) {
        std::cerr << "getaddrinfo failed: " << gai_strerror(errno) << std::endl;
        return 1;
    }

    int listen_socket = socket(result->ai_family, result->ai_socktype, result->ai_protocol);
    if (listen_socket < 0) {
        std::cerr << "Socket creation failed: " << strerror(errno) << std::endl;
        freeaddrinfo(result);
        return 1;
    }

    if (bind(listen_socket, result->ai_addr, result->ai_addrlen) < 0) {
        std::cerr << "Bind failed: " << strerror(errno) << std::endl;
        close(listen_socket);
        freeaddrinfo(result);
        return 1;
    }

    freeaddrinfo(result);

    if (listen(listen_socket, SOMAXCONN) < 0) {
        std::cerr << "Listen failed: " << strerror(errno) << std::endl;
        close(listen_socket);
        return 1;
    }

    std::cout << "Server is listening on port " << DEFAULT_PORT << std::endl;

    while (true) {
        int client_socket = accept(listen_socket, NULL, NULL);
        if (client_socket >= 0) {
            handle_request(client_socket);
        } else {
            std::cerr << "Accept failed: " << strerror(errno) << std::endl;
        }
    }

    close(listen_socket);
    return 0;
}
