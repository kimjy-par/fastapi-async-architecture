USE mnc_onboarding;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,                        
    username VARCHAR(50) NOT NULL,                           
    email VARCHAR(100) NOT NULL UNIQUE,                      
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,          
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP            
                      ON UPDATE CURRENT_TIMESTAMP        
);

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,            
    user_id INT NOT NULL,                   
    title VARCHAR(255) NOT NULL,               
    content TEXT NOT NULL,                      
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
                       ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE tags (
    id INT AUTO_INCREMENT PRIMARY KEY,            
    user_id INT NOT NULL,
    post_id INT NOT NULL,                   
    tag_name VARCHAR(255) NOT NULL,               
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
                       ON UPDATE CURRENT_TIMESTAMP
);