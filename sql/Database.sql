DROP DATABASE `oshes`;

CREATE DATABASE IF NOT EXISTS `oshes` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `oshes`;

CREATE TABLE Administrator(
    adminId		BIGINT 			NOT NULL AUTO_INCREMENT,
    name		VARCHAR(100) 	NOT NULL,
    gender		ENUM('F', 'M')	NOT NULL,
    password 	VARCHAR(30) 	NOT NULL,
    phoneNo 	VARCHAR(15) 	NOT NULL,
    PRIMARY KEY (adminId));

CREATE TABLE Customer(
    customerId	BIGINT			NOT NULL AUTO_INCREMENT,
    name		VARCHAR(30) 	NOT NULL,
    gender		ENUM('F', 'M')	NOT NULL,
    address		VARCHAR(100)	NOT NULL,
    email		VARCHAR(50)		NOT NULL,
    password 	VARCHAR(30) 	NOT NULL,
    phoneNo		VARCHAR(15)		NOT NULL,
    PRIMARY KEY (customerId));

CREATE TABLE Model(
    productId		BIGINT		 			NOT NULL AUTO_INCREMENT,
    categoryName	ENUM('Lights', 'Locks')	NOT NULL,
    modelName		VARCHAR(15)				NOT NULL,
    modelCost		DECIMAL(6,2)			NOT NULL,
    modelPrice		DECIMAL(6,2)			NOT NULL,
    modelWarranty	MEDIUMINT				NOT NULL,
    PRIMARY KEY (productId));
    
CREATE TABLE Item(
    itemId			BIGINT					NOT NULL,
    powerSupply		VARCHAR(15) 			NOT NULL,
    factory			VARCHAR(15) 			NOT NULL,
    color			VARCHAR(15) 			NOT NULL,
    productionYear	YEAR					NOT NULL,
    purchaseStatus	ENUM('Unsold', 'Sold') 	NOT NULL DEFAULT 'Unsold',
    productId 		BIGINT		 			NOT NULL,
    customerId 		BIGINT,
	purchaseDate	DATE,
    PRIMARY KEY (itemId),
    FOREIGN KEY (productId) references Model(productId),
    FOREIGN KEY (customerId) references Customer(customerId));

CREATE TABLE Request(
    requestId		BIGINT	 		NOT NULL AUTO_INCREMENT,
    requestDate		DATE 			NOT NULL,
    requestStatus	ENUM('Submitted', 'Submitted and Waiting for payment', 
							'In progress', 'Approved', 'Canceled', 'Completed') NOT NULL,
    customerId 		BIGINT	 		NOT NULL,
    itemId			BIGINT			NOT NULL,
    PRIMARY KEY (requestId),
    FOREIGN KEY (customerId) references Customer(customerId),
    FOREIGN KEY (itemId) references Item(itemId));
    
    
CREATE TABLE Service(
    serviceId		BIGINT	 		NOT NULL AUTO_INCREMENT,
	serviceStatus 	ENUM('Waiting for approval', 'In progress', 'Completed') NOT NULL,
	adminId			BIGINT,
    requestId		BIGINT 			NOT NULL,
    PRIMARY KEY (serviceId),
	FOREIGN KEY (adminId) references Administrator(adminId),
    FOREIGN KEY (requestId) references Request(requestId));
    
CREATE TABLE Payment(
	requestId		BIGINT	 		NOT NULL,
    serviceFee		DECIMAL(6,2)	NOT NULL,
	paymentDate		DATE			NOT NULL,
	PRIMARY KEY (requestId),
    FOREIGN KEY (requestId) references Request(requestId));