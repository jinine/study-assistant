CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,      -- UUID, default to generated UUID
    username VARCHAR(50) NOT NULL UNIQUE,                 -- Unique username, max length of 50
    email VARCHAR(100) NOT NULL UNIQUE,                    -- Unique email address, max length of 100
    first_name VARCHAR(50),                                -- First name, max length of 50
    last_name VARCHAR(50),                                 -- Last name, max length of 50
    encrypted_pass VARCHAR(128) NOT NULL,                  -- Encrypted password, max length of 128
    profile_picture_url VARCHAR(255),                       -- URL of the user's profile picture, max length of 255
    is_active BOOLEAN DEFAULT TRUE,                         -- User account active status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,        -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP          -- Timestamp of last update
);

--Create Study Materials Table
CREATE TABLE study_materials (
    id SERIAL PRIMARY KEY,           -- Auto-incrementing ID
    title VARCHAR NOT NULL,          -- Title of the study material
    description VARCHAR NOT NULL      -- Description of the study material
);

-- Create StudyProgress table
CREATE TABLE study_progress (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    study_material_id INTEGER NOT NULL,
    progress_percentage DECIMAL(5, 2) NOT NULL CHECK (progress_percentage >= 0 AND progress_percentage <= 100),
    last_accessed TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (study_material_id) REFERENCES study_materials(id) ON DELETE CASCADE
);

-- Create Quiz table
CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    study_material_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (study_material_id) REFERENCES study_materials(id) ON DELETE CASCADE
);

-- Create QuizQuestion table
CREATE TABLE quiz_questions (
    id SERIAL PRIMARY KEY,
    quiz_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    correct_answer VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE
);

-- Create StudyNotification table
CREATE TABLE study_notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    notification_text TEXT NOT NULL,
    is_read BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
