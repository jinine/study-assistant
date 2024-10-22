-- Seed data for study_materials
INSERT INTO study_materials (title, description, user_id) VALUES
('Introduction to Python Programming', 'A comprehensive guide to get started with Python, covering basics to advanced concepts.', 1),
('Data Structures and Algorithms', 'An in-depth look at common data structures and algorithms used in computer science.', 1),
('Web Development with Flask', 'Learn how to build web applications using the Flask framework in Python.', 1),
('Machine Learning Basics', 'An introductory course on machine learning concepts and algorithms.', 1),
('Understanding SQL and Databases', 'A foundational resource for learning SQL and how databases work.', 1),
('JavaScript: The Good Parts', 'A deep dive into the features of JavaScript that make it a powerful programming language.', 1),
('Introduction to HTML and CSS', 'A beginner-friendly guide to web design with HTML and CSS.', 1),
('Mobile App Development with React Native', 'Learn to create cross-platform mobile applications using React Native.', 1),
('The Complete Guide to Git', 'Master version control with Git, including workflows and best practices.', 1),
('Cloud Computing Fundamentals', 'An overview of cloud computing concepts and services.', 1);

-- Seed data for study_progress
INSERT INTO study_progress (user_id, study_material_id, progress_percentage) VALUES
(1, 1, 75),
(1, 2, 50),
(1, 3, 100),
(1, 4, 25),
(1, 5, 60);

-- Seed data for quizzes
INSERT INTO quizzes (title, study_material_id) VALUES
('Python Basics Quiz', 1),
('Data Structures Quiz', 2),
('Flask Framework Quiz', 3),
('Machine Learning Concepts Quiz', 4),
('SQL Fundamentals Quiz', 5);

-- Seed data for quiz_questions
INSERT INTO quiz_questions (quiz_id, question_text, correct_answer) VALUES
(1, 'What is the output of print(type([]))?', 'list'),
(1, 'What keyword is used to define a function in Python?', 'def'),
(2, 'Which data structure uses LIFO?', 'Stack'),
(2, 'What is the time complexity of accessing an element in an array?', 'O(1)'),
(3, 'What is the purpose of the @app.route decorator in Flask?', 'To define the URL endpoint'),
(3, 'Which method is used to run a Flask application?', 'run'),
(4, 'What is supervised learning?', 'A type of machine learning where the model is trained on labeled data.'),
(4, 'What does overfitting mean in machine learning?', 'When a model learns the noise in the training data.'),
(5, 'What command is used to retrieve data from a table in SQL?', 'SELECT'),
(5, 'What is a primary key?', 'A unique identifier for each record in a database table.');

-- Seed data for study_notifications
INSERT INTO study_notifications (user_id, message, is_read) VALUES
(1, 'New study material added: Introduction to Python Programming', FALSE),
(1, 'Your quiz on Data Structures is now available!', FALSE),
(1, 'You have completed the Flask Framework quiz!', TRUE),
(1, 'Reminder: Your Machine Learning Basics quiz is due soon.', FALSE),
(1, 'New features have been added to your study progress dashboard.', TRUE);
