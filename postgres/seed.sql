CREATE TABLE users (
    id SERIAL PRIMARY KEY,                                  -- Auto-incrementing ID
    username VARCHAR(50) NOT NULL UNIQUE,                  -- Unique username, max length of 50
    email VARCHAR(100) NOT NULL UNIQUE,                     -- Unique email address, max length of 100
    first_name VARCHAR(50),                                 -- First name, max length of 50
    last_name VARCHAR(50),                                  -- Last name, max length of 50
    encrypted_pass VARCHAR(128) NOT NULL,                   -- Encrypted password, max length of 128
    profile_picture_url VARCHAR(255),                        -- URL of the user's profile picture, max length of 255
    is_active BOOLEAN DEFAULT TRUE,                          -- User account active status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,         -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP          -- Timestamp of last update
);

CREATE TABLE study_materials (
    id SERIAL PRIMARY KEY,           -- Auto-incrementing ID
    title VARCHAR NOT NULL,          -- Title of the study material
    description VARCHAR NOT NULL      -- Description of the study material
);
