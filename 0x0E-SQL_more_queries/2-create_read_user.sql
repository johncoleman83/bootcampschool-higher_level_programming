-- creates the database btcp_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS btcp_0d_2;
GRANT SELECT ON btcp_0d_2.* TO user_0d_2@localhost
	  IDENTIFIED BY 'user_0d_2_pwd';
