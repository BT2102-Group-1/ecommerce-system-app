INSERT INTO Administrator (name, gender, password, phoneNo)
VALUES
("John Doe", "M", "password123", "98765432"),
("Chetana Choudhury", "F", "password123", "91234567"),
("Tan Ah Kau", "M", "password123", "84211248"),
("Siti Aslinda binte Muhammad", "F", "password123", "89123456")
ON DUPLICATE KEY UPDATE gender = gender;

INSERT INTO Customer (name, gender, address, email, password, phoneNo)
VALUES
("Firdaus bin Muhammad", "M", "Block 123 Jurong Road #01-23", "firdaus@abc.com", "cpassword", "99887766"),
("Lily Lee Li Li", "F", "9 Bedok Crescent", "lily@abc.com", "cpassword", "82323232"),
("Jair Singh", "M", "Block 10 Woodlands Ring Road #11-12", "jair@abc.com", "cpassword", "81112222"),
("Margaret Morstan", "F", "11 Tanglin Road", "margaret@abc.com", "cpassword", "83456543")
ON DUPLICATE KEY UPDATE gender = gender;